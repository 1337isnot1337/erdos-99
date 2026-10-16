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
struct Multiset{array<unsigned char,9>a{};int n=0;bool operator==(Multiset const&o)const{return n==o.n&&a==o.a;}};
struct MH{size_t operator()(Multiset const&x)const{size_t h=x.n;for(int i=0;i<x.n;i++)h=h*37+x.a[i]+1;return h;}};
void sort_prefix(Multiset& x){
    if(x.n<0||x.n>9) abort();
    for(int i=1;i<x.n;++i){
        unsigned char v=x.a[i]; int j=i;
        while(j>0 && x.a[j-1]>v){x.a[j]=x.a[j-1]; --j;}
        x.a[j]=v;
    }
}

vector<array<int,4>> SUP; int SI[128]; vector<array<int,3>> TRI; int TI[128]; vector<array<int,2>> ED; int EI[128]; uint64_t STM[35]; array<array<int,21>,35>TROW; unordered_map<uint64_t,int>RC;
int rankm(vector<vector<int>>A){if(A.empty())return 0;int m=A.size(),n=A[0].size(),r=0;for(auto&row:A)for(int&x:row){x%=MOD;if(x<0)x+=MOD;}for(int c=0;c<n&&r<m;c++){int p=-1;for(int i=r;i<m;i++)if(A[i][c]){p=i;break;}if(p<0)continue;swap(A[r],A[p]);long long inv=1,b=A[r][c],e=MOD-2;while(e){if(e&1)inv=inv*b%MOD;b=b*b%MOD;e>>=1;}for(int j=c;j<n;j++)A[r][j]=(long long)A[r][j]*inv%MOD;for(int i=0;i<m;i++)if(i!=r&&A[i][c]){int q=A[i][c];for(int j=c;j<n;j++){A[i][j]=(A[i][j]-(long long)q*A[r][j])%MOD;if(A[i][j]<0)A[i][j]+=MOD;}}r++;}return r;}
int trank(uint64_t m){auto it=RC.find(m);if(it!=RC.end())return it->second;vector<vector<int>>A;for(int b=0;b<35;b++)if(m>>b&1)A.emplace_back(TROW[b].begin(),TROW[b].end());int r=rankm(move(A));RC[m]=r;return r;}
Multiset canon(const Multiset&x){if(x.n<0||x.n>9) abort(); int deg[7]={};for(int i=0;i<x.n;i++)for(int v:SUP[x.a[i]])deg[v]++;vector<int>vals(deg,deg+7);sort(vals.begin(),vals.end(),greater<int>());vals.erase(unique(vals.begin(),vals.end()),vals.end());vector<vector<int>>gs;for(int d:vals){vector<int>g;for(int v=0;v<7;v++)if(deg[v]==d)g.push_back(v);gs.push_back(g);}Multiset best;best.n=x.n;bool init=false;int rel[7];function<void(int,int)>rec=[&](int gi,int off){if(gi==(int)gs.size()){Multiset im;im.n=x.n;for(int i=0;i<x.n;i++){int bits=0;for(int v:SUP[x.a[i]])bits|=1<<rel[v];im.a[i]=SI[bits];}sort_prefix(im);if(!init||lexicographical_compare(im.a.begin(),im.a.begin()+im.n,best.a.begin(),best.a.begin()+best.n)){best=im;init=true;}return;}auto g=gs[gi];sort(g.begin(),g.end());do{for(int j=0;j<(int)g.size();j++)rel[g[j]]=off+j;rec(gi+1,off+g.size());}while(next_permutation(g.begin(),g.end()));};rec(0,0);return best;}
vector<long long> burnside_counts(){vector<long long>fixed(10,0);array<int,7>p={0,1,2,3,4,5,6};do{int sm[35];for(int i=0;i<35;i++){int bits=0;for(int v:SUP[i])bits|=1<<p[v];sm[i]=SI[bits];}bool seen[35]={};vector<int>lens;for(int i=0;i<35;i++)if(!seen[i]){int j=i,len=0;while(!seen[j]){seen[j]=true;len++;j=sm[j];}lens.push_back(len);}long long dp[10]={};dp[0]=1;for(int len:lens){long long ndp[10]={};for(int t=0;t<=9;t++)if(dp[t])for(int m=0;m<=3;m++){int nx=t+m*len;if(nx<=9)ndp[nx]+=dp[t];}copy(begin(ndp),end(ndp),begin(dp));}for(int k=0;k<=9;k++)fixed[k]+=dp[k];}while(next_permutation(p.begin(),p.end()));vector<long long>out(10);for(int k=0;k<=9;k++){if(fixed[k]%5040){cerr<<"burnside div fail\n";exit(2);}out[k]=fixed[k]/5040;}return out;}
struct BD{uint16_t mask=0;bool repeated=false;int inc=0;};
array<BD,35>bdata(const Multiset&ms,uint64_t&t){int mult[35]={};for(int i=0;i<ms.n;i++)mult[ms.a[i]]++;array<BD,35>o{};t=0;for(int b=0;b<35;b++){int tb=0;for(int v:TRI[b])tb|=1<<v;uint16_t m=0;bool rep=false;for(int i=0;i<ms.n;i++){int sb=0;for(int v:SUP[ms.a[i]])sb|=1<<v;if((sb&tb)!=tb)continue;m|=uint16_t(1u<<i);if(mult[ms.a[i]]>=2)rep=true;}int inc=popcount((unsigned)m);if(!inc)continue;t|=1ULL<<b;o[b]={m,rep,inc};}return o;}
int opts(const BD&x){if(x.repeated)return x.inc>=4?2:0;if(x.inc<2)return 0;if(x.inc<4)return 1;return 3;}
bool compat(const BD&x,int dx,const BD&y,int dy){int in=popcount((unsigned)(x.mask&y.mask)),un=x.inc+y.inc-in;if(dx==1&&dy==1)return in>=2||un>=4;if(dx!=dy)return in>=2||un>=5;return in>=4||(in>=2&&un>=5)||un>=7;}
int usize(uint64_t bm,const array<BD,35>&d){uint16_t u=0;for(int b=0;b<35;b++)if(bm>>b&1)u|=d[b].mask;return popcount((unsigned)u);}
bool structural(uint64_t T,uint64_t I){uint64_t C=T&~I;int rc=trank(C);if(rc!=popcount(C))return false;return trank(T)-rc>=4;}
struct Census{long long final_states=0;long long pair_placements=0;long long survivors=0;};
bool selected_pair_survives(const array<BD,35>&d,uint64_t T,Census&z){int h=popcount(T);vector<int>cand;for(int b=0;b<35;b++)if((T>>b&1)&&opts(d[b]))cand.push_back(b);vector<pair<int,int>>ch;
 auto cw=[&](int b,int db){for(auto[a,da]:ch)if(!compat(d[a],da,d[b],db))return false;return true;};
 auto test=[&](uint64_t em,int nom)->bool{if(nom<5||usize(em,d)<8)return false;z.final_states++;bool ok=false;
   // pair untouched: e >= h-11
   if((int)ch.size()>=h-11){z.pair_placements++;if(structural(T,em))ok=true;}
   // pair touched: e >= h-12; choose any remaining touched block
   if((int)ch.size()>=h-12){uint64_t rem=T&~em;while(rem){int s=countr_zero(rem);rem&=rem-1;z.pair_placements++;if(structural(T,em|(1ULL<<s)))ok=true;}}
   return ok;};
 function<bool(int,uint64_t,int)>rec=[&](int pos,uint64_t em,int nom)->bool{int minE=max(0,h-12);if((int)ch.size()>=minE&&test(em,nom))return true;if(pos==(int)cand.size())return false;if((int)ch.size()+((int)cand.size()-pos)<minE)return false;int maxnom=nom;for(int i=pos;i<(int)cand.size();i++)maxnom+=(opts(d[cand[i]])&2)?2:1;if(maxnom<5)return false;for(int i=pos;i<(int)cand.size();i++){int b=cand[i],op=opts(d[b]);if((op&1)&&cw(b,1)){ch.push_back({b,1});if(rec(i+1,em|(1ULL<<b),nom+1))return true;ch.pop_back();}if((op&2)&&cw(b,2)){ch.push_back({b,2});if(rec(i+1,em|(1ULL<<b),nom+2))return true;ch.pop_back();}}return false;};
 return rec(0,0,0);
}
void init(){fill(begin(SI),end(SI),-1);fill(begin(TI),end(TI),-1);fill(begin(EI),end(EI),-1);for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++)for(int d=c+1;d<7;d++){int bits=(1<<a)|(1<<b)|(1<<c)|(1<<d);SI[bits]=SUP.size();SUP.push_back({a,b,c,d});}for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++){int bits=(1<<a)|(1<<b)|(1<<c);TI[bits]=TRI.size();TRI.push_back({a,b,c});}for(int a=0;a<7;a++)for(int b=a+1;b<7;b++){EI[(1<<a)|(1<<b)]=ED.size();ED.push_back({a,b});}for(int s=0;s<35;s++){uint64_t m=0;for(int skip=0;skip<4;skip++){int bits=0;for(int j=0;j<4;j++)if(j!=skip)bits|=1<<SUP[s][j];m|=1ULL<<TI[bits];}STM[s]=m;}for(int b=0;b<35;b++){TROW[b].fill(0);int a=TRI[b][0],c=TRI[b][1],d=TRI[b][2];TROW[b][EI[(1<<c)|(1<<d)]]=1;TROW[b][EI[(1<<a)|(1<<d)]]=-1;TROW[b][EI[(1<<a)|(1<<c)]]=1;}}
bool ll(){long long s=4;for(int i=0;i<29;i++)s=(s*s-2)%MOD;return s==0;}
void print_ms(const Multiset&ms){for(int i=0;i<ms.n;i++){if(i)cout<<' ';auto s=SUP[ms.a[i]];cout<<'['<<s[0]<<s[1]<<s[2]<<s[3]<<']';}cout<<'\n';}
int main(){init();if(!ll())return 10;if((long long)MOD*MOD<=14348907LL)return 11;vector<long long>exp={1,1,4,14,61,268,1283,6032,27763,121458};if(burnside_counts()!=exp)return 12;unordered_set<Multiset,MH>reps;Multiset e;reps.insert(e);for(int sz=1;sz<=8;sz++){unordered_set<Multiset,MH>n;n.reserve(reps.size()*8);for(auto&ms:reps){int mult[35]={};for(int i=0;i<ms.n;i++)mult[ms.a[i]]++;for(int s=0;s<35;s++)if(mult[s]<3){Multiset x=ms;if(x.n>=9)abort();x.a[x.n]=s;++x.n;sort_prefix(x);n.insert(canon(x));}}reps.swap(n);if((long long)reps.size()!=exp[sz])return 13;}
 unordered_set<Multiset,MH>all9,h24;all9.reserve(130000);h24.reserve(110000);long long raw=0,rawh=0;for(auto&ms:reps){int mult[35]={};uint64_t t=0;for(int i=0;i<ms.n;i++){mult[ms.a[i]]++;t|=STM[ms.a[i]];}for(int s=0;s<35;s++)if(mult[s]<3){raw++;Multiset x=ms;if(x.n>=9)abort();x.a[x.n]=s;++x.n;sort_prefix(x);Multiset cx=canon(x);all9.insert(cx);if(popcount(t|STM[s])<=24){rawh++;h24.insert(cx);}}}
 if((long long)all9.size()!=exp[9]){cerr<<"all9 "<<all9.size()<<"\n";return 14;}cout<<"size9 "<<all9.size()<<" h24 "<<h24.size()<<" raw "<<raw<<" rawh "<<rawh<<"\n";
 Census z;vector<Multiset>surv;long long scanned=0;for(auto&ms:h24){scanned++;uint64_t T;auto d=bdata(ms,T);if(selected_pair_survives(d,T,z)){surv.push_back(ms);}}
 if(h24.size()!=103247||raw!=966977||rawh!=802570||z.final_states!=14480||z.pair_placements!=168944||surv.size()!=2)return 20;
 sort(surv.begin(),surv.end(),[](const Multiset&a,const Multiset&b){return lexicographical_compare(a.a.begin(),a.a.begin()+a.n,b.a.begin(),b.a.begin()+b.n);});
 vector<vector<int>> expected_surv={{0,0,0,1,1,1,4,10,20},{0,0,0,1,4,7,10,13,20}};
 for(int i=0;i<2;i++){vector<int> got;for(int j=0;j<surv[i].n;j++)got.push_back(surv[i].a[j]);if(got!=expected_surv[i]){cerr<<"survivor mismatch\n";return 21;}}
 cout<<"PASS: selected-pair support relaxation leaves exactly two orbits\n";
 cout<<"size9_orbits "<<all9.size()<<"\n"<<"touch_at_most_24 "<<h24.size()<<"\n"<<"raw_size9_extensions "<<raw<<"\n"<<"h_le_24_raw_extensions "<<rawh<<"\n";
 cout<<"relaxed_final_states "<<z.final_states<<"\n"<<"pair_placements_tested "<<z.pair_placements<<"\n"<<"support_survivors "<<surv.size()<<"\n";for(auto&ms:surv)print_ms(ms);
 cout<<"hadamard_exact_rank_bound 1\n"; return 0;}
