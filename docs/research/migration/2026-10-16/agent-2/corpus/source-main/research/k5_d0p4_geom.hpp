#pragma once
#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
static constexpr int MOD=2147483647;
struct Multiset{array<unsigned char,9>a{};unsigned char n=0;bool operator==(Multiset const&o)const{return n==o.n&&a==o.a;}};
struct H{size_t operator()(Multiset const&x)const{size_t h=x.n;for(int i=0;i<x.n;++i)h=h*37+x.a[i]+1;return h;}};
inline vector<array<int,4>> SUPPORTS; inline int SUPPORT_INDEX[128];
inline vector<array<int,3>> TRIANGLES; inline int TRIANGLE_INDEX[128];
inline vector<array<int,2>> EDGES; inline int EDGE_INDEX[128];
inline uint64_t STM[35]; inline array<array<int,21>,35> ROWS; inline unordered_map<uint64_t,int> RCACHE;
inline int rank_mod(vector<vector<int>> A){if(A.empty())return 0;int m=A.size(),n=A[0].size(),r=0;for(auto&row:A)for(int&x:row){x%=MOD;if(x<0)x+=MOD;}for(int c=0;c<n&&r<m;++c){int p=-1;for(int i=r;i<m;++i)if(A[i][c]){p=i;break;}if(p<0)continue;swap(A[r],A[p]);long long inv=1,b=A[r][c],e=MOD-2;while(e){if(e&1)inv=inv*b%MOD;b=b*b%MOD;e>>=1;}for(int j=c;j<n;++j)A[r][j]=(long long)A[r][j]*inv%MOD;for(int i=0;i<m;++i){if(i==r||!A[i][c])continue;int q=A[i][c];for(int j=c;j<n;++j){A[i][j]=(A[i][j]-(long long)q*A[r][j])%MOD;if(A[i][j]<0)A[i][j]+=MOD;}}++r;}return r;}
inline int trank(uint64_t m){auto it=RCACHE.find(m);if(it!=RCACHE.end())return it->second;vector<vector<int>>A;for(int b=0;b<35;++b)if(m>>b&1ULL)A.emplace_back(ROWS[b].begin(),ROWS[b].end());int r=rank_mod(move(A));RCACHE.emplace(m,r);return r;}
inline Multiset canonical(const Multiset&x){int deg[7]={};for(int i=0;i<x.n;++i)for(int v:SUPPORTS[x.a[i]])++deg[v];vector<int>vals(deg,deg+7);sort(vals.begin(),vals.end(),greater<int>());vals.erase(unique(vals.begin(),vals.end()),vals.end());vector<vector<int>>gs;for(int d:vals){vector<int>g;for(int v=0;v<7;++v)if(deg[v]==d)g.push_back(v);gs.push_back(move(g));}Multiset best;best.n=x.n;bool init=false;int rel[7];function<void(int,int)>rec=[&](int gi,int off){if(gi==(int)gs.size()){Multiset im;im.n=x.n;for(int i=0;i<x.n;++i){int bits=0;for(int v:SUPPORTS[x.a[i]])bits|=1<<rel[v];im.a[i]=SUPPORT_INDEX[bits];}sort(im.a.begin(),im.a.begin()+im.n);if(!init||lexicographical_compare(im.a.begin(),im.a.begin()+im.n,best.a.begin(),best.a.begin()+best.n)){best=im;init=true;}return;}auto g=gs[gi];sort(g.begin(),g.end());do{for(int j=0;j<(int)g.size();++j)rel[g[j]]=off+j;rec(gi+1,off+g.size());}while(next_permutation(g.begin(),g.end()));};rec(0,0);return best;}
inline vector<long long> burn(){vector<long long>fixed(10);array<int,7>p={0,1,2,3,4,5,6};do{int sm[35];for(int i=0;i<35;++i){int bits=0;for(int v:SUPPORTS[i])bits|=1<<p[v];sm[i]=SUPPORT_INDEX[bits];}bool seen[35]={};vector<int>ls;for(int i=0;i<35;++i)if(!seen[i]){int j=i,l=0;while(!seen[j]){seen[j]=true;++l;j=sm[j];}ls.push_back(l);}long long dp[10]={};dp[0]=1;for(int l:ls){long long nd[10]={};for(int t=0;t<=9;++t)if(dp[t])for(int m=0;m<=3;++m){int nx=t+m*l;if(nx<=9)nd[nx]+=dp[t];}copy(begin(nd),end(nd),begin(dp));}for(int k=0;k<=9;++k)fixed[k]+=dp[k];}while(next_permutation(p.begin(),p.end()));vector<long long>out(10);for(int k=0;k<=9;++k){if(fixed[k]%5040)exit(2);out[k]=fixed[k]/5040;}return out;}
inline void init_geom(){fill(begin(SUPPORT_INDEX),end(SUPPORT_INDEX),-1);fill(begin(TRIANGLE_INDEX),end(TRIANGLE_INDEX),-1);fill(begin(EDGE_INDEX),end(EDGE_INDEX),-1);for(int a=0;a<7;++a)for(int b=a+1;b<7;++b)for(int c=b+1;c<7;++c)for(int d=c+1;d<7;++d){int x=(1<<a)|(1<<b)|(1<<c)|(1<<d);SUPPORT_INDEX[x]=SUPPORTS.size();SUPPORTS.push_back({a,b,c,d});}for(int a=0;a<7;++a)for(int b=a+1;b<7;++b)for(int c=b+1;c<7;++c){int x=(1<<a)|(1<<b)|(1<<c);TRIANGLE_INDEX[x]=TRIANGLES.size();TRIANGLES.push_back({a,b,c});}for(int a=0;a<7;++a)for(int b=a+1;b<7;++b){EDGE_INDEX[(1<<a)|(1<<b)]=EDGES.size();EDGES.push_back({a,b});}for(int s=0;s<35;++s){uint64_t m=0;for(int skip=0;skip<4;++skip){int x=0;for(int j=0;j<4;++j)if(j!=skip)x|=1<<SUPPORTS[s][j];m|=1ULL<<TRIANGLE_INDEX[x];}STM[s]=m;}for(int b=0;b<35;++b){ROWS[b].fill(0);int a=TRIANGLES[b][0],c=TRIANGLES[b][1],d=TRIANGLES[b][2];ROWS[b][EDGE_INDEX[(1<<c)|(1<<d)]]=1;ROWS[b][EDGE_INDEX[(1<<a)|(1<<d)]]=-1;ROWS[b][EDGE_INDEX[(1<<a)|(1<<c)]]=1;}}
inline bool ll31(){long long s=4;for(int i=0;i<29;++i)s=(s*s-2)%MOD;return s==0;}
