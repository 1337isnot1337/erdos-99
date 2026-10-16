#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <functional>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
static constexpr int MOD=2147483647;
struct Multiset{array<unsigned char,8>a{};unsigned char n=0;bool operator==(Multiset const&o)const{return n==o.n&&a==o.a;}};
struct MH{size_t operator()(Multiset const&x)const{size_t h=x.n;for(int i=0;i<x.n;i++)h=h*37+x.a[i]+1;return h;}};
vector<array<int,4>> SUP; int SI[128]; vector<array<int,3>> TRI; int TI[128]; vector<array<int,2>> ED; int EI[128]; array<array<int,21>,35> TROW; unordered_map<uint64_t,int> RC;
int rankm(vector<vector<int>> A){if(A.empty())return 0;int m=A.size(),n=A[0].size(),r=0;for(auto&row:A)for(int&x:row){x%=MOD;if(x<0)x+=MOD;}for(int c=0;c<n&&r<m;c++){int p=-1;for(int i=r;i<m;i++)if(A[i][c]){p=i;break;}if(p<0)continue;swap(A[r],A[p]);long long inv=1,b=A[r][c],e=MOD-2;while(e){if(e&1)inv=inv*b%MOD;b=b*b%MOD;e>>=1;}for(int j=c;j<n;j++)A[r][j]=(long long)A[r][j]*inv%MOD;for(int i=0;i<m;i++)if(i!=r&&A[i][c]){int q=A[i][c];for(int j=c;j<n;j++){A[i][j]=(A[i][j]-(long long)q*A[r][j])%MOD;if(A[i][j]<0)A[i][j]+=MOD;}}r++;}return r;}
int trank(uint64_t m){auto it=RC.find(m);if(it!=RC.end())return it->second;vector<vector<int>>A;for(int b=0;b<35;b++)if(m>>b&1)A.emplace_back(TROW[b].begin(),TROW[b].end());int r=rankm(move(A));RC[m]=r;return r;}
Multiset canon(const Multiset&x){int deg[7]={};for(int i=0;i<x.n;i++)for(int v:SUP[x.a[i]])deg[v]++;vector<int>vals(deg,deg+7);sort(vals.begin(),vals.end(),greater<int>());vals.erase(unique(vals.begin(),vals.end()),vals.end());vector<vector<int>>gs;for(int d:vals){vector<int>g;for(int v=0;v<7;v++)if(deg[v]==d)g.push_back(v);gs.push_back(g);}Multiset best;best.n=x.n;bool init=false;int rel[7];function<void(int,int)>rec=[&](int gi,int off){if(gi==(int)gs.size()){Multiset im;im.n=x.n;for(int i=0;i<x.n;i++){int bits=0;for(int v:SUP[x.a[i]])bits|=1<<rel[v];im.a[i]=SI[bits];}sort(im.a.begin(),im.a.begin()+im.n);if(!init||lexicographical_compare(im.a.begin(),im.a.begin()+im.n,best.a.begin(),best.a.begin()+best.n)){best=im;init=true;}return;}auto g=gs[gi];sort(g.begin(),g.end());do{for(int j=0;j<(int)g.size();j++)rel[g[j]]=off+j;rec(gi+1,off+g.size());}while(next_permutation(g.begin(),g.end()));};rec(0,0);return best;}
struct BD{uint16_t mask=0;bool repeated=false;int inc=0;};
array<BD,35>bdata(const Multiset&ms,uint64_t&t){int mult[35]={};for(int i=0;i<ms.n;i++)mult[ms.a[i]]++;array<BD,35>o{};t=0;for(int b=0;b<35;b++){int tb=0;for(int v:TRI[b])tb|=1<<v;uint16_t m=0;bool rep=false;for(int i=0;i<ms.n;i++){int sb=0;for(int v:SUP[ms.a[i]])sb|=1<<v;if((sb&tb)!=tb)continue;m|=uint16_t(1u<<i);if(mult[ms.a[i]]>=2)rep=true;}int inc=popcount((unsigned)m);if(!inc)continue;t|=1ULL<<b;o[b]={m,rep,inc};}return o;}
// rank options bitmask: bit0=rank1, bit1=rank2. We use only implications sound from support data and d1>=2,d2>=4.
int opts(const BD&x){if(x.repeated)return x.inc>=4?2:0;if(x.inc<2)return 0;if(x.inc<4)return 1;return 3;}
bool compat(const BD&x,int dx,const BD&y,int dy){int in=popcount((unsigned)(x.mask&y.mask)),un=x.inc+y.inc-in;if(dx==1&&dy==1)return in>=2||un>=4;if(dx!=dy)return in>=2||un>=5;return in>=4||(in>=2&&un>=5)||un>=7;}
int usize(uint64_t bm,const array<BD,35>&d){uint16_t u=0;for(int b=0;b<35;b++)if(bm>>b&1)u|=d[b].mask;return popcount((unsigned)u);}
struct Census{long long all=0,h24=0,finaltests=0,nullitytests=0,surv=0;};
bool survives(const array<BD,35>&d,uint64_t T,Census&z){int h=popcount(T);vector<int>cand;for(int b=0;b<35;b++)if((T>>b&1)&&opts(d[b]))cand.push_back(b);vector<pair<int,int>>ch;int minE=max(0,h-16);
 auto cw=[&](int b,int db){for(auto[a,da]:ch)if(!compat(d[a],da,d[b],db))return false;return true;};
 auto test=[&](uint64_t em,int nom){if((int)ch.size()<minE||nom<4||usize(em,d)<7)return false;z.finaltests++;uint64_t C=T&~em;int rc=trank(C);if((int)popcount(C)-rc>1)return false;z.nullitytests++;if(trank(T)-rc>=4){z.surv++;return true;}return false;};
 function<bool(int,uint64_t,int)>rec=[&](int pos,uint64_t em,int nom){if((int)ch.size()>=minE&&test(em,nom))return true;if(pos==(int)cand.size())return false;if((int)ch.size()+((int)cand.size()-pos)<minE)return false;int maxnom=nom;for(int i=pos;i<(int)cand.size();i++)maxnom+=(opts(d[cand[i]])&2)?2:1;if(maxnom<4)return false;for(int i=pos;i<(int)cand.size();i++){int b=cand[i],op=opts(d[b]);if((op&1)&&cw(b,1)){ch.push_back({b,1});if(rec(i+1,em|(1ULL<<b),nom+1))return true;ch.pop_back();}if((op&2)&&cw(b,2)){ch.push_back({b,2});if(rec(i+1,em|(1ULL<<b),nom+2))return true;ch.pop_back();}}return false;};
 return rec(0,0,0);
}
void init(){fill(begin(SI),end(SI),-1);fill(begin(TI),end(TI),-1);fill(begin(EI),end(EI),-1);for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++)for(int d=c+1;d<7;d++){int bits=(1<<a)|(1<<b)|(1<<c)|(1<<d);SI[bits]=SUP.size();SUP.push_back({a,b,c,d});}for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++){int bits=(1<<a)|(1<<b)|(1<<c);TI[bits]=TRI.size();TRI.push_back({a,b,c});}for(int a=0;a<7;a++)for(int b=a+1;b<7;b++){EI[(1<<a)|(1<<b)]=ED.size();ED.push_back({a,b});}for(int b=0;b<35;b++){TROW[b].fill(0);int a=TRI[b][0],c=TRI[b][1],d=TRI[b][2];TROW[b][EI[(1<<c)|(1<<d)]]=1;TROW[b][EI[(1<<a)|(1<<d)]]=-1;TROW[b][EI[(1<<a)|(1<<c)]]=1;}}
bool ll(){long long s=4;for(int i=0;i<29;i++)s=(s*s-2)%MOD;return s==0;}
int main(){init();if(!ll())return 10;if((long long)MOD*MOD<=14348907LL)return 11;vector<long long>exp={1,1,4,14,61,268,1283,6032,27763};unordered_set<Multiset,MH>reps;Multiset e;reps.insert(e);for(int sz=1;sz<=8;sz++){unordered_set<Multiset,MH>n;n.reserve(reps.size()*8);for(auto&ms:reps){int mult[35]={};for(int i=0;i<ms.n;i++)mult[ms.a[i]]++;for(int ss=0;ss<35;ss++)if(mult[ss]<3){Multiset x=ms;x.a[x.n++]=ss;sort(x.a.begin(),x.a.begin()+x.n);n.insert(canon(x));}}reps.swap(n);if((long long)reps.size()!=exp[sz]){cerr<<"orbit fail "<<sz<<" "<<reps.size()<<"\n";return 12;}}
 Census z;for(auto&ms:reps){z.all++;uint64_t T;auto d=bdata(ms,T);if(popcount(T)>24)continue;z.h24++;survives(d,T,z);}
 if(z.all!=27763||z.h24!=26580||z.finaltests!=33192||z.nullitytests!=909||z.surv!=0)return 20;
 cout<<"PASS: repaired eight-no-root k=4 D=-1 d_root=1 p=0 support closure\n";
 cout<<"orbit_counts_size_0_through_8 1 1 4 14 61 268 1283 6032 27763\n";
 cout<<"support_multiset_orbits_size_8 "<<z.all<<"\n";
 cout<<"touch_at_most_24 "<<z.h24<<"\n";
 cout<<"relaxed_final_tests "<<z.finaltests<<"\n";
 cout<<"touched_complete_nullity_at_most_1 "<<z.nullitytests<<"\n";
 cout<<"capacity_survivors "<<z.surv<<"\n";
 cout<<"hadamard_exact_rank_bound "<<((long long)MOD*MOD>14348907LL)<<"\n";
 return 0;}
