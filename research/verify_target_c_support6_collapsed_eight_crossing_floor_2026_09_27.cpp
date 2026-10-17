#define main rotation_cell_base_main
#include "verify_target_c_support6_collapsed_rotation_cells_2026_09_19.cpp"
#undef main
#include <bitset>
#include <functional>
#include <unordered_map>
#include <unordered_set>

struct Syndrome { uint32_t target; array<uint32_t,66> col; };

static int pair_id(int a,int b) {
    if (a>b) swap(a,b); int id=0;
    for (int i=0;i<12;i++) for (int j=i+1;j<12;j++,id++) if (i==a&&j==b) return id;
    assert(false); return -1;
}
static pair<int,int> pair_from_id(int id) {
    int k=0; for (int i=0;i<12;i++) for (int j=i+1;j<12;j++,k++) if (k==id) return {i,j};
    assert(false); return {-1,-1};
}
static vector<uint16_t> all_simple_cycles(const vector<Edge>& E) {
    vector<uint16_t> ans;
    for (int mask=1;mask<(1<<12);mask++) {
        int k=__builtin_popcount((unsigned)mask); if(k<3||k>6) continue;
        int deg[6]={0};
        for(int e=0;e<12;e++) if((mask>>e)&1){deg[E[e].a]++;deg[E[e].b]++;}
        int used=0,start=-1; bool ok=true;
        for(int v=0;v<6;v++) if(deg[v]){used++;start=v;if(deg[v]!=2)ok=false;}
        if(!ok||used!=k) continue;
        bool vis[6]={false}; vector<int> st={start}; vis[start]=true; int seen=0;
        while(!st.empty()){int v=st.back();st.pop_back();seen++;for(int e=0;e<12;e++)if((mask>>e)&1){int w=-1;if(E[e].a==v)w=E[e].b;else if(E[e].b==v)w=E[e].a;if(w>=0&&!vis[w]){vis[w]=true;st.push_back(w);}}}
        if(seen==used) ans.push_back((uint16_t)mask);
    }
    return ans;
}
static int face_alternation(uint16_t C,uint16_t D,int v,const Cell& cell) {
    vector<int>a,b;for(int j=0;j<4;j++){int e=cell.order[v][j];if((C>>e)&1)a.push_back(j);if((D>>e)&1)b.push_back(j);}if(a.empty()||b.empty())return 0;assert(a.size()==2&&b.size()==2);return ((a[1]-a[0]+4)%4)==2;
}
static Syndrome parity_syndrome(const Cell& cell,const vector<Edge>& E) {
    const auto cycles=all_simple_cycles(E); vector<bitset<67>> rows;
    for(size_t i=0;i<cycles.size();i++)for(size_t j=i+1;j<cycles.size();j++){uint16_t C=cycles[i],D=cycles[j];if(C&D)continue;bitset<67> row;int rhs=0;for(int v=0;v<6;v++)rhs^=face_alternation(C,D,v,cell);for(int e=0;e<12;e++)if((C>>e)&1)for(int f=0;f<12;f++)if((D>>f)&1)row.flip(pair_id(e,f));if(rhs)row.set(66);rows.push_back(row);}
    int rank=0;for(int col=0;col<66&&rank<(int)rows.size();col++){int p=rank;while(p<(int)rows.size()&&!rows[p].test(col))p++;if(p==(int)rows.size())continue;swap(rows[p],rows[rank]);for(int r=0;r<(int)rows.size();r++)if(r!=rank&&rows[r].test(col))rows[r]^=rows[rank];rank++;}
    for(const auto&row:rows){bool any=false;for(int c=0;c<66;c++)any|=row.test(c);assert(any||!row.test(66));}
    assert(rank<=31); Syndrome s{};s.target=0;s.col.fill(0);for(int r=0;r<rank;r++){if(rows[r].test(66))s.target|=(1u<<r);for(int c=0;c<66;c++)if(rows[r].test(c))s.col[c]|=(1u<<r);}return s;
}
static vector<vector<int>> crossing_orientations(const Cell& cell,const vector<int>& ids) {
    vector<Ineq> base;for(int v=0;v<6;v++)add_gap_constraints(base,cell.order[v]);assert(strict_difference_feasible(base));
    vector<vector<int>> ans;vector<int>cur(ids.size());function<void(int,const vector<Ineq>&)>rec=[&](int q,const vector<Ineq>&z){if(q==(int)ids.size()){ans.push_back(cur);return;}auto[e,f]=pair_from_id(ids[q]);for(int sg=0;sg<2;sg++){int p=sg?f:e,n=sg?e:f;auto z2=z;z2.push_back({n,p,2});z2.push_back({p,n,-1});if(strict_difference_feasible(z2)){cur[q]=sg;rec(q+1,z2);}}};rec(0,base);return ans;
}
static int forced_crossing_flip(const Cell& cell,int e,int f,int sg){const int Dsign=sg?1:-1;const int ce=((cell.orientation_bits>>e)&1)?1:-1;const int cf=((cell.orientation_bits>>f)&1)?1:-1;return ce*cf*Dsign>0?0:1;}
struct Segment{int u,v,original_edge;};
static int planarized_genus(const Cell& cell,const vector<Edge>&E,const vector<pair<int,int>>&cp,const vector<vector<int>>&order,const vector<int>&flip){int k=cp.size();vector<Segment>segs;vector<vector<int>>edge_segs(12),edge_chain(12);for(int e=0;e<12;e++){vector<int>chain={E[e].a};for(int cid:order[e])chain.push_back(6+cid);chain.push_back(E[e].b);edge_chain[e]=chain;for(int j=0;j+1<(int)chain.size();j++){int sid=segs.size();segs.push_back({chain[j],chain[j+1],e});edge_segs[e].push_back(sid);}}int V=6+k,M=segs.size();map<pair<int,int>,int>dart;int nd=0;for(int s=0;s<M;s++){dart[{segs[s].u,s}]=nd++;dart[{segs[s].v,s}]=nd++;}vector<int>rot(nd,-1),rev(nd,-1);for(int s=0;s<M;s++){int a=dart[{segs[s].u,s}],b=dart[{segs[s].v,s}];rev[a]=b;rev[b]=a;}for(int v=0;v<6;v++){array<int,4>d{};for(int j=0;j<4;j++){int e=cell.order[v][j];int sid=(E[e].a==v?edge_segs[e].front():edge_segs[e].back());d[j]=dart[{v,sid}];}for(int j=0;j<4;j++)rot[d[j]]=d[(j+1)%4];}for(int cid=0;cid<k;cid++){int cv=6+cid,e=cp[cid].first,f=cp[cid].second;auto toward_a=[&](int oe){const auto&chain=edge_chain[oe];int pos=-1;for(int i=0;i<(int)chain.size();i++)if(chain[i]==cv)pos=i;assert(pos>0&&pos+1<(int)chain.size());return pair<int,int>{edge_segs[oe][pos-1],edge_segs[oe][pos]};};auto ep=toward_a(e),fp=toward_a(f);int eA=dart[{cv,ep.first}],eB=dart[{cv,ep.second}],fA=dart[{cv,fp.first}],fB=dart[{cv,fp.second}];array<int,4>d=flip[cid]==0?array<int,4>{eA,fA,eB,fB}:array<int,4>{eA,fB,eB,fA};for(int j=0;j<4;j++)rot[d[j]]=d[(j+1)%4];}vector<int>seen(nd);int F=0;for(int d=0;d<nd;d++)if(!seen[d]){F++;int x=d;while(!seen[x]){seen[x]=1;x=rot[rev[x]];}}int chi=V-M+F;assert((2-chi)%2==0);return(2-chi)/2;}
static bool oriented_planarization_exists(const Cell&cell,const vector<Edge>&E,const vector<int>&ids,const vector<vector<int>>&orientations){vector<pair<int,int>>cp;for(int id:ids)cp.push_back(pair_from_id(id));for(const auto&sg:orientations){vector<int>flip;for(int c=0;c<(int)ids.size();c++)flip.push_back(forced_crossing_flip(cell,cp[c].first,cp[c].second,sg[c]));vector<vector<int>>order(12);for(int c=0;c<(int)cp.size();c++){order[cp[c].first].push_back(c);order[cp[c].second].push_back(c);}vector<int>multi;for(int e=0;e<12;e++)if(order[e].size()>1)multi.push_back(e);bool planar=false;function<void(int)>rec=[&](int q){if(planar)return;if(q==(int)multi.size()){if(planarized_genus(cell,E,cp,order,flip)==0)planar=true;return;}int e=multi[q];sort(order[e].begin(),order[e].end());do{rec(q+1);}while(!planar&&next_permutation(order[e].begin(),order[e].end()));};rec(0);if(planar)return true;}return false;}

static vector<Cell> symmetry_reps(const set<pair<int,int>>&missing,const vector<Cell>&cells){const auto E=make_edges(missing);const auto aut=sign_preserving_automorphisms(missing);map<string,Cell> reps;for(const auto&c:cells){string best(1,'~');for(const auto&p:aut){best=min(best,cell_key(transform_cell(c,E,p,false),E));best=min(best,cell_key(transform_cell(c,E,p,true),E));}if(!reps.count(best))reps.emplace(best,c);}vector<Cell>out;for(auto&kv:reps)out.push_back(kv.second);return out;}

struct Stats{long long parity=0,metric=0,planar=0;vector<pair<int,vector<int>>> examples;};

static Stats run_case7(const string&name,const set<pair<int,int>>&missing,int expected_cells,int expected_orbits){map<int,int>gc,pc;auto cells=enumerate_cells(missing,gc,pc);assert((int)cells.size()==expected_cells);auto reps=symmetry_reps(missing,cells);assert((int)reps.size()==expected_orbits);auto E=make_edges(missing);Stats out;int ri=0;
 for(const auto&cell:reps){auto s=parity_syndrome(cell,E);unordered_map<uint32_t,vector<array<int,3>>> triples;triples.reserve(8192);for(int a=0;a<66;a++)for(int b=a+1;b<66;b++)for(int c=b+1;c<66;c++)triples[s.col[a]^s.col[b]^s.col[c]].push_back({a,b,c});
  long long p0=out.parity,m0=out.metric,pl0=out.planar;
  for(int d=0;d<66;d++)for(int e=d+1;e<66;e++)for(int f=e+1;f<66;f++)for(int g=f+1;g<66;g++){
    auto it=triples.find(s.target^s.col[d]^s.col[e]^s.col[f]^s.col[g]);if(it==triples.end())continue;
    for(auto A:it->second){if(A[2]>=d)continue;vector<int>ids={A[0],A[1],A[2],d,e,f,g};out.parity++;auto ori=crossing_orientations(cell,ids);if(ori.empty())continue;out.metric++;if(oriented_planarization_exists(cell,E,ids,ori)){out.planar++;if(out.examples.size()<20)out.examples.push_back({ri,ids});}}
  }
  cerr<<name<<" rep "<<ri<<" parity "<<(out.parity-p0)<<" metric "<<(out.metric-m0)<<" planar "<<(out.planar-pl0)<<"\n";ri++;
 }
 cout<<name<<" reps="<<reps.size()<<" k7 parity="<<out.parity<<" metric="<<out.metric<<" planar="<<out.planar<<"\n";for(auto&ex:out.examples){cout<<"  planar rep="<<ex.first<<" ids";for(int id:ex.second){auto p=pair_from_id(id);cout<<" "<<p.first<<"-"<<p.second;}cout<<"\n";}return out;}

int main(){
    auto A=run_case7("all-cross",{{0,3},{1,4},{2,5}},180,15);
    auto M=run_case7("mixed",{{0,1},{2,3},{4,5}},208,27);
    assert(A.parity==324634 && A.metric==964 && A.planar==0);
    assert(M.parity==543490 && M.metric==1580 && M.planar==0);
    cout<<"TOTAL k7 parity="<<(A.parity+M.parity)<<" metric="<<(A.metric+M.metric)<<" planar="<<(A.planar+M.planar)<<"\n";
    assert(A.planar+M.planar==0);
    cout<<"PASS: no collapsed support-six rotation-cell orbit admits a planar, angle-compatible MI.1 pattern with exactly seven internal crossings.\n";
    cout<<"CONCLUSION: with the audited <=6 certificate, every global collapsed support-six block has X_K >= 8.\n";
    return 0;
}
