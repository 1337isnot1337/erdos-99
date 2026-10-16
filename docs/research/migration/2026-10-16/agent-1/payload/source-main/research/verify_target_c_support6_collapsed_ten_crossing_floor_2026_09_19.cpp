#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <functional>
#include <mutex>
#include <thread>
#include <sstream>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

struct Edge { int a,b; };
struct Ineq { int u,v,c; }; // x_v-x_u<c; -1 constant node
using Orders=array<array<int,4>,6>;
struct Cell { uint16_t orientation_bits; Orders order; };
struct Gap {int c,p,n;};

static vector<Edge> make_edges(const set<pair<int,int>>& missing){
 vector<Edge> E; for(int a=0;a<6;a++)for(int b=a+1;b<6;b++) if(!missing.count({a,b})) E.push_back({a,b}); assert(E.size()==12); return E;
}
static void add_lt(vector<Ineq>& z,int pos,int neg,int constant,int rhs){z.push_back({neg,pos,rhs-constant});}
static void add_gap_constraints(vector<Ineq>& z,const array<int,4>& o){
 int a1=o[0],a2=o[1],b1=o[2],b2=o[3];
 Gap g[5]={{0,a1,-1},{0,a2,a1},{3,b1,a2},{0,b2,b1},{3,-1,b2}};
 for(int k=0;k<5;k++){add_lt(z,g[k].p,g[k].n,g[k].c,2); add_lt(z,g[k].n,g[k].p,-g[k].c,0);}
 for(int k=0;k<5;k++){
  Gap A=g[k],B=g[(k+1)%5]; int coeff[12]={0};
  if(A.p>=0) coeff[A.p]++;
  if(A.n>=0) coeff[A.n]--;
  if(B.p>=0) coeff[B.p]++;
  if(B.n>=0) coeff[B.n]--;
  int p=-1,n=-1; for(int i=0;i<12;i++){assert(coeff[i]>=-1&&coeff[i]<=1); if(coeff[i]==1)p=i; if(coeff[i]==-1)n=i;}
  int c=A.c+B.c; add_lt(z,p,n,c,3); add_lt(z,n,p,-c,-2);
 }
}
static bool strict_difference_feasible(const vector<Ineq>& z){
 constexpr int N=13,CONST=12,SCALE=14; int d[N]={0};
 for(int it=0;it<N;it++){ bool changed=false; for(auto&q:z){int u=q.u<0?CONST:q.u,v=q.v<0?CONST:q.v,w=SCALE*q.c-1; if(d[v]>d[u]+w){d[v]=d[u]+w;changed=true;}} if(!changed)return true; }
 return false;
}
static vector<Cell> enumerate_cells(const set<pair<int,int>>& missing){
 auto E=make_edges(missing); vector<Cell> cells;
 for(int bits=0;bits<(1<<12);bits++){
  int out[6]={0},in[6]={0};
  for(int ei=0;ei<12;ei++){auto e=E[ei]; int tail=((bits>>ei)&1)?e.b:e.a; int head=e.a+e.b-tail; out[tail]++;in[head]++;}
  bool ok=true;for(int v=0;v<6;v++)if(out[v]!=2||in[v]!=2)ok=false; if(!ok)continue;
  array<array<array<int,4>,4>,6> choices{};
  for(int v=0;v<6;v++){
   vector<int> outs,ins; for(int ei=0;ei<12;ei++){auto e=E[ei]; if(e.a!=v&&e.b!=v)continue; int tail=((bits>>ei)&1)?e.b:e.a; (tail==v?outs:ins).push_back(ei);} assert(outs.size()==2&&ins.size()==2);
   const vector<int> A=(v<3?outs:ins),B=(v<3?ins:outs); int t=0;
   for(int sa=0;sa<2;sa++)for(int sb=0;sb<2;sb++) choices[v][t++]={A[sa],A[1-sa],B[sb],B[1-sb]};
  }
  for(int code=0;code<4096;code++){
   int x=code; Cell c{}; c.orientation_bits=(uint16_t)bits; vector<Ineq> z; z.reserve(120);
   for(int v=0;v<6;v++){c.order[v]=choices[v][x&3];x>>=2;add_gap_constraints(z,c.order[v]);}
   if(strict_difference_feasible(z)) cells.push_back(c);
  }
 }
 return cells;
}
static vector<uint16_t> all_simple_cycles(const vector<Edge>& E){
 vector<uint16_t> ans;
 for(int mask=1;mask<(1<<12);mask++){int k=__builtin_popcount((unsigned)mask);if(k<3||k>6)continue;int deg[6]={0};for(int e=0;e<12;e++)if((mask>>e)&1){deg[E[e].a]++;deg[E[e].b]++;}int used=0,start=-1;bool ok=true;for(int v=0;v<6;v++)if(deg[v]){used++;start=v;if(deg[v]!=2)ok=false;}if(!ok||used!=k)continue;bool vis[6]={0};vector<int> st={start};vis[start]=1;int seen=0;while(!st.empty()){int v=st.back();st.pop_back();seen++;for(int e=0;e<12;e++)if((mask>>e)&1){int w=-1;if(E[e].a==v)w=E[e].b;else if(E[e].b==v)w=E[e].a;if(w>=0&&!vis[w]){vis[w]=1;st.push_back(w);}}}if(seen==used)ans.push_back((uint16_t)mask);
 }
 return ans;
}
static int pair_variable(int a,int b){if(a>b)swap(a,b);int id=0;for(int i=0;i<12;i++)for(int j=i+1;j<12;j++,id++)if(i==a&&j==b)return id;assert(false);return -1;}
static pair<int,int> variable_pair(int id){int k=0;for(int i=0;i<12;i++)for(int j=i+1;j<12;j++,k++)if(k==id)return {i,j};assert(false);return{-1,-1};}
static bool crossing_window_intersects_cell(int e,int f,const vector<Ineq>& base){
 for(int sign=0;sign<2;sign++){int a=sign?f:e,b=sign?e:f;vector<Ineq> z=base; z.push_back({b,a,2}); z.push_back({a,b,-1}); if(strict_difference_feasible(z))return true;}return false;
}
static int face_alternation(uint16_t C,uint16_t D,int v,const Cell& cell){vector<int> pc,pd;for(int j=0;j<4;j++){int e=cell.order[v][j];if((C>>e)&1)pc.push_back(j);if((D>>e)&1)pd.push_back(j);}if(pc.empty()||pd.empty())return 0;assert(pc.size()==2&&pd.size()==2);return ((pc[1]-pc[0]+4)%4)==2?1:0;}

struct Affine { bool consistent; vector<bitset<66>> basis; bitset<66> particular; int allowed_count; int rank; };
static Affine parity_affine(const Cell& cell,const vector<Edge>& E){
 vector<Ineq> base;for(int v=0;v<6;v++)add_gap_constraints(base,cell.order[v]);assert(strict_difference_feasible(base));
 bool allowed[12][12]={{false}};int ac=0;for(int e=0;e<12;e++)for(int f=e+1;f<12;f++){allowed[e][f]=crossing_window_intersects_cell(e,f,base);if(allowed[e][f])ac++;}
 auto cycles=all_simple_cycles(E);vector<bitset<67>> rows;
 for(size_t i=0;i<cycles.size();i++)for(size_t j=i+1;j<cycles.size();j++){auto C=cycles[i],D=cycles[j];if(C&D)continue;bitset<67> row;int rhs=0;for(int v=0;v<6;v++)rhs^=face_alternation(C,D,v,cell);for(int e=0;e<12;e++)if((C>>e)&1)for(int f=0;f<12;f++)if((D>>f)&1){int a=min(e,f),b=max(e,f);if(allowed[a][b])row.flip(pair_variable(a,b));}if(rhs)row.set(66);rows.push_back(row);}
 int rank=0;vector<int> pivotcol;
 for(int col=0;col<66 && rank<(int)rows.size();col++){int p=rank;while(p<(int)rows.size()&&!rows[p].test(col))p++;if(p==(int)rows.size())continue;swap(rows[p],rows[rank]);for(int r=0;r<(int)rows.size();r++)if(r!=rank&&rows[r].test(col))rows[r]^=rows[rank];pivotcol.push_back(col);rank++;}
 for(auto&row:rows){bool any=false;for(int c=0;c<66;c++)if(row.test(c)){any=true;break;}if(!any&&row.test(66))return{false,{}, {},ac,rank};}
 vector<int> isPivot(66,0);for(int c:pivotcol)isPivot[c]=1;bitset<66> part;for(int r=0;r<rank;r++)if(rows[r].test(66))part.set(pivotcol[r]);
 vector<bitset<66>> basis;for(int f=0;f<66;f++)if(!isPivot[f]){
  auto [a,b]=variable_pair(f); if(!allowed[a][b]) continue;
  bitset<66> v;v.set(f);for(int r=0;r<rank;r++)if(rows[r].test(f))v.flip(pivotcol[r]);basis.push_back(v);
 }
 assert((int)basis.size()==ac-rank);
 return{true,basis,part,ac,rank};
}
static bool triangle_free(const bitset<66>& sol){
 uint16_t adj[12]={0};int id=0;for(int i=0;i<12;i++)for(int j=i+1;j<12;j++,id++)if(sol.test(id)){adj[i]|=(1u<<j);adj[j]|=(1u<<i);}for(int i=0;i<12;i++){uint16_t ni=adj[i];for(int j=i+1;j<12;j++)if((ni>>j)&1){if(adj[i]&adj[j])return false;}}return true;
}

static vector<array<int,6>> sign_preserving_automorphisms(const set<pair<int,int>>& missing) {
    vector<array<int,6>> ans;
    array<int,3> P={0,1,2}, N={3,4,5};
    sort(P.begin(),P.end());
    do {
        sort(N.begin(),N.end());
        do {
            array<int,6> p{};
            for (int i=0;i<3;i++) { p[i]=P[i]; p[i+3]=N[i]; }
            set<pair<int,int>> M2;
            for (auto [a,b]:missing) {
                auto q=minmax(p[a],p[b]); M2.insert({q.first,q.second});
            }
            if (M2==missing) ans.push_back(p);
        } while (next_permutation(N.begin(),N.end()));
    } while (next_permutation(P.begin(),P.end()));
    return ans;
}

static Cell transform_cell(const Cell& c, const vector<Edge>& E,
                           const array<int,6>& p, bool reflect) {
    map<pair<int,int>,int> index;
    for (int i=0;i<12;i++) index[{E[i].a,E[i].b}]=i;
    Cell d{};
    for (int ei=0;ei<12;ei++) {
        auto e=E[ei];
        int tail=((c.orientation_bits>>ei)&1)?e.b:e.a;
        int head=e.a+e.b-tail;
        tail=p[tail]; head=p[head];
        if (reflect) swap(tail,head);
        auto q=minmax(tail,head); int ne=index[{q.first,q.second}];
        if (tail==q.second) d.orientation_bits|=(1u<<ne);
    }
    for (int v=0;v<6;v++) {
        array<int,4> a{};
        for (int j=0;j<4;j++) {
            auto e=E[c.order[v][j]]; auto q=minmax(p[e.a],p[e.b]);
            a[j]=index[{q.first,q.second}];
        }
        d.order[p[v]]=reflect?array<int,4>{a[3],a[2],a[1],a[0]}:a;
    }
    return d;
}

static string cell_key(const Cell& c,const vector<Edge>& E) {
    string s;
    for (int ei=0;ei<12;ei++) {
        auto e=E[ei]; int tail=((c.orientation_bits>>ei)&1)?e.b:e.a;
        s+=to_string(e.a)+to_string(e.b)+":"+to_string(tail)+",";
    }
    s+='|';
    for (int v=0;v<6;v++) {
        for (int j=0;j<4;j++) { auto e=E[c.order[v][j]]; s+=to_string(e.a)+to_string(e.b)+","; }
        s+=';';
    }
    return s;
}

static vector<Cell> canonical_representatives(const set<pair<int,int>>& missing,
                                               int expected_cells,int expected_orbits) {
    auto cells=enumerate_cells(missing); assert((int)cells.size()==expected_cells);
    auto E=make_edges(missing); auto aut=sign_preserving_automorphisms(missing);
    map<string,Cell> reps;
    for (const auto& c:cells) {
        string best(1,'~'); Cell bestc{};
        for (const auto& p:aut) for (int r=0;r<2;r++) {
            Cell d=transform_cell(c,E,p,r!=0); string k=cell_key(d,E);
            if (k<best) { best=k; bestc=d; }
        }
        reps.emplace(best,bestc);
    }
    assert((int)reps.size()==expected_orbits);
    vector<Cell> out; for (auto& kv:reps) out.push_back(kv.second); return out;
}

static vector<vector<int>> crossing_orientations(const Cell& cell,const vector<int>& ids) {
    vector<Ineq> base; for(int v=0;v<6;v++) add_gap_constraints(base,cell.order[v]);
    assert(strict_difference_feasible(base));
    vector<vector<int>> ans; vector<int> cur(ids.size());
    function<void(int,const vector<Ineq>&)> rec=[&](int q,const vector<Ineq>& z) {
        if (q==(int)ids.size()) { ans.push_back(cur); return; }
        auto [e,f]=variable_pair(ids[q]);
        for (int sg=0;sg<2;sg++) {
            int p=sg?f:e, n=sg?e:f; auto z2=z;
            z2.push_back({n,p,2}); z2.push_back({p,n,-1});
            if (strict_difference_feasible(z2)) { cur[q]=sg; rec(q+1,z2); }
        }
    };
    rec(0,base); return ans;
}

static int forced_crossing_flip(const Cell& cell,int e,int f,int sg) {
    int Dsign=sg?1:-1;
    int ce=((cell.orientation_bits>>e)&1)?1:-1;
    int cf=((cell.orientation_bits>>f)&1)?1:-1;
    return ce*cf*Dsign>0?0:1;
}

struct Segment { int u,v,original_edge; };
static int planarized_genus(const Cell& cell,const vector<Edge>& E,
                            const vector<pair<int,int>>& cp,
                            const vector<vector<int>>& order,
                            const vector<int>& flip) {
    int k=(int)cp.size(); vector<Segment> segs; vector<vector<int>> edge_segs(12),edge_chain(12);
    for (int e=0;e<12;e++) {
        vector<int> chain={E[e].a}; for(int cid:order[e]) chain.push_back(6+cid); chain.push_back(E[e].b);
        edge_chain[e]=chain;
        for(int j=0;j+1<(int)chain.size();j++) { int sid=(int)segs.size(); segs.push_back({chain[j],chain[j+1],e}); edge_segs[e].push_back(sid); }
    }
    int V=6+k,M=(int)segs.size(); map<pair<int,int>,int> dart; int nd=0;
    for(int s=0;s<M;s++){dart[{segs[s].u,s}]=nd++;dart[{segs[s].v,s}]=nd++;}
    vector<int> rot(nd,-1),rev(nd,-1);
    for(int s=0;s<M;s++){int a=dart[{segs[s].u,s}],b=dart[{segs[s].v,s}];rev[a]=b;rev[b]=a;}
    for(int v=0;v<6;v++) {
        array<int,4> d{};
        for(int j=0;j<4;j++){int e=cell.order[v][j];int sid=(E[e].a==v?edge_segs[e].front():edge_segs[e].back());d[j]=dart[{v,sid}];}
        for(int j=0;j<4;j++)rot[d[j]]=d[(j+1)%4];
    }
    for(int cid=0;cid<k;cid++) {
        int cv=6+cid,e=cp[cid].first,f=cp[cid].second;
        auto toward_a=[&](int oe){const auto& ch=edge_chain[oe];int pos=-1;for(int i=0;i<(int)ch.size();i++)if(ch[i]==cv)pos=i;assert(pos>0&&pos+1<(int)ch.size());return pair<int,int>{edge_segs[oe][pos-1],edge_segs[oe][pos]};};
        auto ep=toward_a(e),fp=toward_a(f); int eA=dart[{cv,ep.first}],eB=dart[{cv,ep.second}],fA=dart[{cv,fp.first}],fB=dart[{cv,fp.second}];
        array<int,4> d=flip[cid]==0?array<int,4>{eA,fA,eB,fB}:array<int,4>{eA,fB,eB,fA};
        for(int j=0;j<4;j++)rot[d[j]]=d[(j+1)%4];
    }
    vector<int> seen(nd); int F=0;
    for(int d=0;d<nd;d++)if(!seen[d]){F++;int x=d;while(!seen[x]){seen[x]=1;x=rot[rev[x]];}}
    int chi=V-M+F; assert((2-chi)%2==0); return (2-chi)/2;
}

static bool oriented_planarization_exists(const Cell& cell,const vector<Edge>& E,
                                           const vector<int>& ids,const vector<vector<int>>& orientations) {
    vector<pair<int,int>> cp; for(int id:ids)cp.push_back(variable_pair(id));
    for(const auto& sg:orientations) {
        vector<int> flip; for(int c=0;c<(int)ids.size();c++)flip.push_back(forced_crossing_flip(cell,cp[c].first,cp[c].second,sg[c]));
        vector<vector<int>> order(12); for(int c=0;c<(int)cp.size();c++){order[cp[c].first].push_back(c);order[cp[c].second].push_back(c);}
        vector<int> multi; for(int e=0;e<12;e++)if(order[e].size()>1)multi.push_back(e);
        bool planar=false;
        function<void(int)> rec=[&](int q){
            if(planar)return;
            if(q==(int)multi.size()){if(planarized_genus(cell,E,cp,order,flip)==0)planar=true;return;}
            int e=multi[q]; sort(order[e].begin(),order[e].end());
            do{rec(q+1);}while(!planar&&next_permutation(order[e].begin(),order[e].end()));
        };
        rec(0); if(planar)return true;
    }
    return false;
}

struct Counts { long long parity=0,triangle_free=0,metric=0,planar=0; };
struct Job { Cell cell; vector<Edge> edges; string tag; int index; };
struct JobResult { array<Counts,3> c{}; string line; };

static JobResult check_rep(const Job& job) {
    const Cell& cell=job.cell; const auto& E=job.edges;
    auto a=parity_affine(cell,E); assert(a.consistent); int d=(int)a.basis.size(); assert(d<31);
    bitset<66> sol=a.particular; unsigned prev=0,lim=1u<<d; JobResult result;
    for(unsigned t=0;t<lim;t++) {
        if(t){unsigned g=t^(t>>1),diff=g^prev;int k=__builtin_ctz(diff);sol^=a.basis[k];prev=g;}
        int w=(int)sol.count(); if(w<7||w>9)continue; Counts& C=result.c[w-7]; C.parity++;
        if (!triangle_free(sol)) continue;
        C.triangle_free++;
        vector<int> ids; for(int id=0;id<66;id++)if(sol.test(id))ids.push_back(id);
        auto ori=crossing_orientations(cell,ids); if(ori.empty())continue; C.metric++;
        if(oriented_planarization_exists(cell,E,ids,ori)) C.planar++;
    }
    ostringstream ss; ss<<job.index<<" "<<job.tag;
    for(int w=7;w<=9;w++){auto&C=result.c[w-7];ss<<" k"<<w<<"="<<C.parity<<"/"<<C.triangle_free<<"/"<<C.metric<<"/"<<C.planar;}
    result.line=ss.str(); return result;
}

int main(){
    const set<pair<int,int>> MX={{0,3},{1,4},{2,5}}, MM={{0,1},{2,3},{4,5}};
    auto RX=canonical_representatives(MX,180,15), RM=canonical_representatives(MM,208,27);
    vector<Job> jobs; int idx=0; auto EX=make_edges(MX), EM=make_edges(MM);
    for (auto& c:RX) jobs.push_back({c,EX,"X",idx++});
    for (auto& c:RM) jobs.push_back({c,EM,"M",idx++});
    assert(jobs.size()==42);
    vector<JobResult> out(jobs.size()); mutex m; size_t next=0;
    auto worker=[&](){for(;;){size_t j;{lock_guard<mutex> lock(m);if(next>=jobs.size())return;j=next++;}out[j]=check_rep(jobs[j]);}};
    const int nt=8; vector<thread> threads; for(int i=0;i<nt;i++)threads.emplace_back(worker); for(auto&t:threads)t.join();
    array<Counts,3> total{};
    for(const auto&r:out){cout<<r.line<<"\n";for(int k=0;k<3;k++){total[k].parity+=r.c[k].parity;total[k].triangle_free+=r.c[k].triangle_free;total[k].metric+=r.c[k].metric;total[k].planar+=r.c[k].planar;}}
    const array<Counts,3> expected={Counts{4909,3965,2544,0},Counts{11944,9340,5801,0},Counts{27650,19455,10453,0}};
    for(int k=0;k<3;k++){
        cout<<"TOTAL k="<<(k+7)<<" parity="<<total[k].parity<<" tri="<<total[k].triangle_free<<" metric="<<total[k].metric<<" planar="<<total[k].planar<<"\n";
        assert(total[k].parity==expected[k].parity&&total[k].triangle_free==expected[k].triangle_free&&total[k].metric==expected[k].metric&&total[k].planar==0);
    }
    cout<<"PASS: no collapsed support-six symmetry orbit admits a planar, angle-compatible MI.1 crossing pattern with 7, 8, or 9 internal crossings.\n";
    cout<<"Together with the audited <=6 theorem, every global collapsed support-six block has X_K >= 10.\n";
}
