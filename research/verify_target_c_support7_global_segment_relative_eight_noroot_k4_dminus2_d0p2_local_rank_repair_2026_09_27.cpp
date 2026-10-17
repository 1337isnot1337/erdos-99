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
vector<array<int,4>> SUP; int SI[128]; vector<array<int,3>> TRI; int TI[128]; vector<array<int,2>> ED; int EI[128]; uint64_t STM[35]; array<array<int,21>,35> TROW; unordered_map<uint64_t,int> RC;
int rankm(vector<vector<int>> A){if(A.empty())return 0;int m=A.size(),n=A[0].size(),r=0;for(auto&row:A)for(int&x:row){x%=MOD;if(x<0)x+=MOD;}for(int c=0;c<n&&r<m;c++){int p=-1;for(int i=r;i<m;i++)if(A[i][c]){p=i;break;}if(p<0)continue;swap(A[r],A[p]);long long inv=1,b=A[r][c],e=MOD-2;while(e){if(e&1)inv=inv*b%MOD;b=b*b%MOD;e>>=1;}for(int j=c;j<n;j++)A[r][j]=(long long)A[r][j]*inv%MOD;for(int i=0;i<m;i++)if(i!=r&&A[i][c]){int q=A[i][c];for(int j=c;j<n;j++){A[i][j]=(A[i][j]-(long long)q*A[r][j])%MOD;if(A[i][j]<0)A[i][j]+=MOD;}}r++;}return r;}
int trank(uint64_t m){auto it=RC.find(m);if(it!=RC.end())return it->second;vector<vector<int>>A;for(int b=0;b<35;b++)if(m>>b&1)A.emplace_back(TROW[b].begin(),TROW[b].end());int r=rankm(move(A));RC[m]=r;return r;}
Multiset canon(const Multiset&x){int deg[7]={};for(int i=0;i<x.n;i++)for(int v:SUP[x.a[i]])deg[v]++;vector<int>vals(deg,deg+7);sort(vals.begin(),vals.end(),greater<int>());vals.erase(unique(vals.begin(),vals.end()),vals.end());vector<vector<int>>gs;for(int d:vals){vector<int>g;for(int v=0;v<7;v++)if(deg[v]==d)g.push_back(v);gs.push_back(g);}Multiset best;best.n=x.n;bool init=false;int rel[7];function<void(int,int)>rec=[&](int gi,int off){if(gi==(int)gs.size()){Multiset im;im.n=x.n;for(int i=0;i<x.n;i++){int bits=0;for(int v:SUP[x.a[i]])bits|=1<<rel[v];im.a[i]=SI[bits];}sort(im.a.begin(),im.a.begin()+im.n);if(!init||lexicographical_compare(im.a.begin(),im.a.begin()+im.n,best.a.begin(),best.a.begin()+best.n)){best=im;init=true;}return;}auto g=gs[gi];sort(g.begin(),g.end());do{for(int j=0;j<(int)g.size();j++)rel[g[j]]=off+j;rec(gi+1,off+g.size());}while(next_permutation(g.begin(),g.end()));};rec(0,0);return best;}
struct BD{uint16_t mask=0;bool repeated=false;int inc=0;};
array<BD,35>bdata(const Multiset&ms,uint64_t&t){int mult[35]={};for(int i=0;i<ms.n;i++)mult[ms.a[i]]++;array<BD,35>o{};t=0;for(int b=0;b<35;b++){int tb=0;for(int v:TRI[b])tb|=1<<v;uint16_t m=0;bool rep=false;for(int i=0;i<ms.n;i++){int sb=0;for(int v:SUP[ms.a[i]])sb|=1<<v;if((sb&tb)!=tb)continue;m|=uint16_t(1u<<i);if(mult[ms.a[i]]>=2)rep=true;}int inc=popcount((unsigned)m);if(!inc)continue;t|=1ULL<<b;o[b]={m,rep,inc};}return o;}
int opts(const BD&x){if(x.repeated)return x.inc>=5?2:0;if(x.inc<4)return 0;if(x.inc==4)return 1;return 3;}
bool compat(const BD&x,int dx,const BD&y,int dy){int in=popcount((unsigned)(x.mask&y.mask)),un=x.inc+y.inc-in;if(dx==1&&dy==1)return in>=4||un>=5;if(dx!=dy)return in>=4||un>=6;return in>=5||(in>=4&&un>=6)||un>=7;}
int usize(uint64_t bm,const array<BD,35>&d){uint16_t u=0;for(int b=0;b<35;b++)if(bm>>b&1)u|=d[b].mask;return popcount((unsigned)u);}
bool structural(uint64_t T,uint64_t I){uint64_t C=T&~I;int rc=trank(C);if(rc!=popcount(C))return false;return trank(T)-rc>=4;}

bool pair_survives(const array<BD,35>&d,uint64_t T,long long&tests){
 int h=popcount(T);vector<int>cand;for(int b=0;b<35;b++)if((T>>b&1)&&opts(d[b]))cand.push_back(b);vector<pair<int,int>>ch;
 auto cw=[&](int b,int db){for(auto[a,da]:ch)if(!compat(d[a],da,d[b],db))return false;return true;};
 auto test=[&](uint64_t em,int nom){tests++;if(nom<4||usize(em,d)<7)return false;int ne=ch.size();
   if(ne>=h-15 && structural(T,em))return true;
   if(ne>=h-16){uint64_t rem=T&~em;for(int pb=0;pb<35;pb++)if(rem>>pb&1)if(structural(T,em|(1ULL<<pb)))return true;}
   return false;};
 function<bool(int,uint64_t,int)>rec=[&](int pos,uint64_t em,int nom){int minE=max(0,h-16);if((int)ch.size()>=minE&&test(em,nom))return true;if(pos==(int)cand.size())return false;if((int)ch.size()+((int)cand.size()-pos)<minE)return false;int maxnom=nom;for(int i=pos;i<(int)cand.size();i++)maxnom+=(opts(d[cand[i]])&2)?2:1;if(maxnom<4)return false;for(int i=pos;i<(int)cand.size();i++){int b=cand[i],op=opts(d[b]);if((op&1)&&cw(b,1)){ch.push_back({b,1});if(rec(i+1,em|(1ULL<<b),nom+1))return true;ch.pop_back();}if((op&2)&&cw(b,2)){ch.push_back({b,2});if(rec(i+1,em|(1ULL<<b),nom+2))return true;ch.pop_back();}}return false;};
 return rec(0,0,0);
}

bool single_survives(const array<BD,35>&d,uint64_t T,long long&tests){
 int h=popcount(T);vector<int>cand;for(int b=0;b<35;b++)if((T>>b&1)&&opts(d[b]))cand.push_back(b);vector<pair<int,int>>ch;
 auto cw=[&](int b,int db){for(auto[a,da]:ch)if(!compat(d[a],da,d[b],db))return false;return true;};
 auto test=[&](uint64_t em,int nom){int ne=ch.size();uint64_t rem=T&~em;vector<int>rb;for(int b=0;b<35;b++)if(rem>>b&1)rb.push_back(b);
   for(int t=0;t<=2;t++){if(35-h<2-t||ne<h-15-t)continue;
     if(t==0){tests++;if(nom>=4&&usize(em,d)>=7&&structural(T,em))return true;continue;}
     if(t==1){for(int s:rb){for(int ds=0;ds<=1;ds++){if(ds&&d[s].inc<4)continue;tests++;if(ds&&!cw(s,1))continue;uint64_t I=em|(1ULL<<s);if(nom+ds<4)continue;uint16_t u=0;for(int b=0;b<35;b++)if(em>>b&1)u|=d[b].mask;if(ds)u|=d[s].mask;if(popcount((unsigned)u)<7)continue;if(structural(T,I))return true;}}continue;}
     for(int ii=0;ii<(int)rb.size();ii++)for(int jj=ii+1;jj<(int)rb.size();jj++){int s1=rb[ii],s2=rb[jj];for(int d1=0;d1<=1;d1++)for(int d2=0;d2<=1;d2++){if(d1&&d[s1].inc<4)continue;if(d2&&d[s2].inc<4)continue;tests++;if(d1&&!cw(s1,1))continue;if(d2&&!cw(s2,1))continue;if(d1&&d2&&!compat(d[s1],1,d[s2],1))continue;uint64_t I=em|(1ULL<<s1)|(1ULL<<s2);if(nom+d1+d2<4)continue;uint16_t u=0;for(int b=0;b<35;b++)if(em>>b&1)u|=d[b].mask;if(d1)u|=d[s1].mask;if(d2)u|=d[s2].mask;if(popcount((unsigned)u)<7)continue;if(structural(T,I))return true;}}
   }
   return false;};
 function<bool(int,uint64_t,int)>rec=[&](int pos,uint64_t em,int nom){int minE=max(0,h-17);if((int)ch.size()>=minE&&test(em,nom))return true;if(pos==(int)cand.size())return false;if((int)ch.size()+((int)cand.size()-pos)<minE)return false;int maxnom=nom;for(int i=pos;i<(int)cand.size();i++)maxnom+=(opts(d[cand[i]])&2)?2:1;if(maxnom+2<4)return false;for(int i=pos;i<(int)cand.size();i++){int b=cand[i],op=opts(d[b]);if((op&1)&&cw(b,1)){ch.push_back({b,1});if(rec(i+1,em|(1ULL<<b),nom+1))return true;ch.pop_back();}if((op&2)&&cw(b,2)){ch.push_back({b,2});if(rec(i+1,em|(1ULL<<b),nom+2))return true;ch.pop_back();}}return false;};
 return rec(0,0,0);
}

void init(){fill(begin(SI),end(SI),-1);fill(begin(TI),end(TI),-1);fill(begin(EI),end(EI),-1);for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++)for(int dd=c+1;dd<7;dd++){int bits=(1<<a)|(1<<b)|(1<<c)|(1<<dd);SI[bits]=SUP.size();SUP.push_back({a,b,c,dd});}for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++){int bits=(1<<a)|(1<<b)|(1<<c);TI[bits]=TRI.size();TRI.push_back({a,b,c});}for(int a=0;a<7;a++)for(int b=a+1;b<7;b++){EI[(1<<a)|(1<<b)]=ED.size();ED.push_back({a,b});}for(int s=0;s<35;s++){uint64_t m=0;for(int sk=0;sk<4;sk++){int bits=0;for(int j=0;j<4;j++)if(j!=sk)bits|=1<<SUP[s][j];m|=1ULL<<TI[bits];}STM[s]=m;}for(int b=0;b<35;b++){TROW[b].fill(0);int a=TRI[b][0],c=TRI[b][1],dd=TRI[b][2];TROW[b][EI[(1<<c)|(1<<dd)]]=1;TROW[b][EI[(1<<a)|(1<<dd)]]=-1;TROW[b][EI[(1<<a)|(1<<c)]]=1;}}
bool ll(){long long s=4;for(int i=0;i<29;i++)s=(s*s-2)%MOD;return s==0;}
int main(){init();if(!ll())return 10;if((long long)MOD*MOD<=14348907LL)return 11;vector<long long>exp={1,1,4,14,61,268,1283,6032,27763};unordered_set<Multiset,MH>reps;Multiset e;reps.insert(e);for(int sz=1;sz<=8;sz++){unordered_set<Multiset,MH>n;n.reserve(reps.size()*8);for(auto&ms:reps){int mult[35]={};for(int i=0;i<ms.n;i++)mult[ms.a[i]]++;for(int ss=0;ss<35;ss++)if(mult[ss]<3){Multiset x=ms;x.a[x.n++]=ss;sort(x.a.begin(),x.a.begin()+x.n);n.insert(canon(x));}}reps.swap(n);if((long long)reps.size()!=exp[sz]){cerr<<"orbit fail "<<sz<<" "<<reps.size()<<"\n";return 12;}}
 long long all=0,h20=0,pt=0,st=0,ps=0,ss=0;for(auto&ms:reps){all++;uint64_t T;auto d=bdata(ms,T);if(popcount(T)>20)continue;h20++;if(pair_survives(d,T,pt))ps++;if(single_survives(d,T,st))ss++;}
 if(all!=27763||h20!=13574||pt!=2091||st!=775064||ps!=0||ss!=0)return 20;
 cout<<"PASS: repaired eight-no-root k=4 D=-2 d_root=0 p=2 support closure\n";
 cout<<"orbit_counts_size_0_through_8 1 1 4 14 61 268 1283 6032 27763\n";
 cout<<"support_multiset_orbits_size_8 "<<all<<"\n";
 cout<<"touch_at_most_20 "<<h20<<"\n";
 cout<<"pair_profile_relaxed_tests "<<pt<<"\n";
 cout<<"two_singleton_profile_relaxed_tests "<<st<<"\n";
 cout<<"pair_profile_survivors "<<ps<<"\n";
 cout<<"two_singleton_profile_survivors "<<ss<<"\n";
 cout<<"hadamard_exact_rank_bound "<<((long long)MOD*MOD>14348907LL)<<"\n";
 return 0;}
