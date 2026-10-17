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
struct Ineq { int u,v,c; };
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

struct CycleO { uint16_t mask; array<int,12> q{}; array<int,6> in{}; array<int,6> out{}; };
static vector<CycleO> oriented_cycles(const vector<Edge>&E){
 vector<CycleO> ans;for(uint16_t mask:all_simple_cycles(E)){CycleO C{};C.mask=mask;C.in.fill(-1);C.out.fill(-1);C.q.fill(0);vector<vector<pair<int,int>>>adj(6);for(int e=0;e<12;e++)if((mask>>e)&1){adj[E[e].a].push_back({E[e].b,e});adj[E[e].b].push_back({E[e].a,e});}int s=-1;for(int v=0;v<6;v++)if(!adj[v].empty()){s=v;break;}sort(adj[s].begin(),adj[s].end());int prev=-1,cur=s,nxt=adj[s][0].first;for(;;){int eid=-1;for(auto [w,e]:adj[cur])if(w==nxt){eid=e;break;}assert(eid>=0);C.out[cur]=eid;C.in[nxt]=eid;int lo=E[eid].a,hi=E[eid].b;
 C.q[eid]=(cur==lo&&nxt==hi)?1:-1;
 prev=cur;cur=nxt;if(cur==s)break;auto a=adj[cur];nxt=(a[0].first==prev?a[1].first:a[0].first);
 }ans.push_back(C);}return ans;
}
static int chord_local_sign(const Cell&cell,const CycleO&C,const CycleO&D,int v){
 int ci=C.in[v],co=C.out[v],di=D.in[v],do_=D.out[v];if(ci<0||di<0)return 0;int pos[12];for(int i=0;i<12;i++)pos[i]=-1;for(int j=0;j<4;j++)pos[cell.order[v][j]]=j;int a=pos[ci],b=pos[co],c=pos[di],d=pos[do_];assert(a>=0&&b>=0&&c>=0&&d>=0);auto dist=[](int x,int y){return (y-x+4)%4;};bool cin=(dist(a,c)>0&&dist(a,c)<dist(a,b));bool din=(dist(a,d)>0&&dist(a,d)<dist(a,b));if(cin==din)return 0;return cin?1:-1;
}
static bool signed_intersection_ok(const Cell&cell,const vector<Edge>&E,const vector<int>&ids,const vector<int>&sg){
 int sgn[66]={0};for(int k=0;k<(int)ids.size();k++)sgn[ids[k]]=sg[k]?1:-1;
 auto cyc=oriented_cycles(E);
 for(size_t i=0;i<cyc.size();i++)for(size_t j=i+1;j<cyc.size();j++){auto&C=cyc[i];auto&D=cyc[j];if(C.mask&D.mask)continue;long total=0;
   for(int e=0;e<12;e++)if((C.mask>>e)&1)for(int f=0;f<12;f++)if((D.mask>>f)&1){int id=pair_variable(e,f);if(!sgn[id])continue;int qce=C.q[e],qdf=D.q[f];
      int canon_e=((cell.orientation_bits>>e)&1)?-1:1;int canon_f=((cell.orientation_bits>>f)&1)?-1:1;
      int relc=qce*canon_e, reld=qdf*canon_f; total+=relc*reld*sgn[id];}
   for(int v=0;v<6;v++)if(C.in[v]>=0&&D.in[v]>=0)total+=chord_local_sign(cell,C,D,v);
   if(total!=0)return false;
 }
 return true;
}

struct Job { Cell cell; vector<Edge> edges; string tag; int index; };
struct Stat { unsigned long long parity=0,tri=0,metric_sets=0,metric_orients=0,signed_orients=0; };
struct JR { array<Stat,37> s{}; unsigned long long affine_total=0; int d=0; string tag; int index=0; };

static void audit_signed_lift(const Cell& cell,const vector<Edge>& E) {
    auto cyc=oriented_cycles(E);
    for(size_t i=0;i<cyc.size();i++) for(size_t j=i+1;j<cyc.size();j++) {
        const auto& C=cyc[i]; const auto& D=cyc[j];
        if(C.mask&D.mask) continue;
        int signed_local=0, mod2_local=0;
        for(int v=0;v<6;v++) {
            int s=chord_local_sign(cell,C,D,v);
            signed_local += s;
            mod2_local ^= face_alternation(C.mask,D.mask,v,cell);
            assert((s!=0)==(face_alternation(C.mask,D.mask,v,cell)!=0));
        }
        assert(((signed_local%2)+2)%2 == mod2_local);
    }
}

static JR runjob(const Job&job){
    JR r; r.tag=job.tag; r.index=job.index;
    audit_signed_lift(job.cell,job.edges);
    auto a=parity_affine(job.cell,job.edges); assert(a.consistent);
    r.d=(int)a.basis.size(); assert(r.d<31);
    bitset<66> sol=a.particular; unsigned prev=0,lim=1u<<r.d; r.affine_total=lim;
    for(unsigned t=0;t<lim;t++) {
        if(t){unsigned g=t^(t>>1),diff=g^prev;int k=__builtin_ctz(diff);sol^=a.basis[k];prev=g;}
        int w=(int)sol.count(); r.s[w].parity++;
        if(!triangle_free(sol)) continue;
        r.s[w].tri++;
        vector<int> ids; for(int id=0;id<66;id++) if(sol.test(id)) ids.push_back(id);
        auto ori=crossing_orientations(job.cell,ids); if(ori.empty()) continue;
        r.s[w].metric_sets++; r.s[w].metric_orients+=ori.size();
        for(const auto& sg:ori) if(signed_intersection_ok(job.cell,job.edges,ids,sg)) r.s[w].signed_orients++;
    }
    return r;
}

int main(){
    const set<pair<int,int>> MX={{0,3},{1,4},{2,5}}, MM={{0,1},{2,3},{4,5}};
    auto RX=canonical_representatives(MX,180,15), RM=canonical_representatives(MM,208,27);
    vector<Job> jobs; int idx=0; auto EX=make_edges(MX),EM=make_edges(MM);
    for(auto&c:RX)jobs.push_back({c,EX,"X",idx++});
    for(auto&c:RM)jobs.push_back({c,EM,"M",idx++});
    assert(jobs.size()==42);

    vector<JR> out(42); mutex m; size_t next=0;
    auto work=[&](){for(;;){size_t j;{lock_guard<mutex>l(m);if(next>=jobs.size())return;j=next++;}out[j]=runjob(jobs[j]);}};
    vector<thread> th; for(int i=0;i<8;i++) th.emplace_back(work); for(auto&t:th)t.join();

    array<Stat,37> T{}; unsigned long long affine=0; int mind=100,maxd=0;
    for(auto&r:out){
        affine+=r.affine_total; mind=min(mind,r.d); maxd=max(maxd,r.d);
        for(int w=0;w<=36;w++){
            T[w].parity+=r.s[w].parity; T[w].tri+=r.s[w].tri;
            T[w].metric_sets+=r.s[w].metric_sets; T[w].metric_orients+=r.s[w].metric_orients;
            T[w].signed_orients+=r.s[w].signed_orients;
        }
    }

    const array<unsigned long long,37> EP={0,0,17,34,191,407,1916,4909,11944,27650,58377,115221,210197,345201,520106,677710,790014,818048,743201,621404,451767,297653,176014,87969,43426,16318,6765,1997,685,131,36,4,0,0,0,0,0};
    const array<unsigned long long,37> ET={0,0,17,34,189,395,1740,3965,9340,19455,40324,68769,111761,147900,182236,176890,150897,99956,60563,26851,11870,3563,1255,196,52,3,3,0,0,0,0,0,0,0,0,0,0};
    const array<unsigned long long,37> EMET={0,0,15,32,134,279,1140,2544,5801,10453,20349,29112,43138,49043,58456,49474,41475,24221,15022,5522,2922,609,302,38,6,1,0,0,0,0,0,0,0,0,0,0,0};

    cout<<"cells=42 affine_total="<<affine<<" d="<<mind<<".."<<maxd<<"\n";
    unsigned long long signed_total=0,metric_sets_total=0,metric_orients_total=0;
    for(int w=0;w<=36;w++){
        assert(T[w].parity==EP[w]); assert(T[w].tri==ET[w]); assert(T[w].metric_sets==EMET[w]);
        assert(T[w].metric_orients==T[w].metric_sets);
        assert(T[w].signed_orients==0);
        if(T[w].parity||T[w].tri||T[w].metric_sets) {
            cout<<"w="<<w<<" parity="<<T[w].parity<<" tri="<<T[w].tri
                <<" metric="<<T[w].metric_sets<<" signed="<<T[w].signed_orients<<"\n";
        }
        signed_total+=T[w].signed_orients; metric_sets_total+=T[w].metric_sets; metric_orients_total+=T[w].metric_orients;
    }
    assert(affine==6029312ULL); assert(mind==14&&maxd==19);
    assert(metric_sets_total==360088ULL); assert(metric_orients_total==360088ULL); assert(signed_total==0);
    cout<<"TOTAL metric="<<metric_sets_total<<" signed="<<signed_total<<"\n";
    cout<<"PASS: signed integer cycle-intersection excludes every triangle-free, jointly angle-feasible collapsed support-six crossing state in all 42 symmetry orbits.\n";
}
