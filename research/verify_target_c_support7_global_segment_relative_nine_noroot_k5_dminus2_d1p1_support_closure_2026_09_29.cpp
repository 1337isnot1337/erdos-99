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
static constexpr int MOD = 2147483647;

struct Multiset {
    array<unsigned char, 9> a{};
    unsigned char n = 0;
    bool operator==(Multiset const& o) const { return n == o.n && a == o.a; }
};
struct MultisetHash {
    size_t operator()(Multiset const& x) const {
        size_t h=x.n;
        for(int i=0;i<x.n;++i) h=h*37+x.a[i]+1;
        return h;
    }
};

vector<array<int,4>> SUPPORTS;
int SUPPORT_INDEX[128];
vector<array<int,3>> TRIANGLES;
int TRIANGLE_INDEX[128];
vector<array<int,2>> EDGES;
int EDGE_INDEX[128];
uint64_t SUPPORT_TRIANGLE_MASK[35];
array<array<int,21>,35> TRIANGLE_ROWS;
unordered_map<uint64_t,int> TRIANGLE_RANK_CACHE;

int rank_mod(vector<vector<int>> A){
    if(A.empty()) return 0;
    int m=A.size(), n=A[0].size(), r=0;
    for(auto &row:A) for(int &x:row){x%=MOD; if(x<0)x+=MOD;}
    for(int c=0;c<n && r<m;++c){
        int p=-1; for(int i=r;i<m;++i) if(A[i][c]){p=i;break;}
        if(p<0) continue;
        swap(A[r],A[p]);
        long long inv=1, base=A[r][c], exp=MOD-2;
        while(exp){if(exp&1)inv=inv*base%MOD; base=base*base%MOD; exp>>=1;}
        for(int j=c;j<n;++j) A[r][j]=(long long)A[r][j]*inv%MOD;
        for(int i=0;i<m;++i){
            if(i==r || !A[i][c]) continue;
            int q=A[i][c];
            for(int j=c;j<n;++j){A[i][j]=(A[i][j]-(long long)q*A[r][j])%MOD; if(A[i][j]<0)A[i][j]+=MOD;}
        }
        ++r;
    }
    return r;
}
int triangle_rank(uint64_t mask){
    auto it=TRIANGLE_RANK_CACHE.find(mask); if(it!=TRIANGLE_RANK_CACHE.end()) return it->second;
    vector<vector<int>> A;
    for(int b=0;b<35;++b) if(mask>>b&1ULL) A.emplace_back(TRIANGLE_ROWS[b].begin(),TRIANGLE_ROWS[b].end());
    int r=rank_mod(move(A)); TRIANGLE_RANK_CACHE.emplace(mask,r); return r;
}

Multiset canonical(const Multiset& x){
    int degree[7]={};
    for(int i=0;i<x.n;++i) for(int v:SUPPORTS[x.a[i]]) ++degree[v];
    vector<int> values(degree,degree+7); sort(values.begin(),values.end(),greater<int>()); values.erase(unique(values.begin(),values.end()),values.end());
    vector<vector<int>> groups;
    for(int d:values){vector<int> g; for(int v=0;v<7;++v) if(degree[v]==d) g.push_back(v); groups.push_back(move(g));}
    Multiset best; best.n=x.n; bool initialized=false; int relabel[7];
    function<void(int,int)> rec=[&](int gi,int offset){
        if(gi==(int)groups.size()){
            Multiset image; image.n=x.n;
            for(int i=0;i<x.n;++i){int bits=0; for(int v:SUPPORTS[x.a[i]]) bits|=1<<relabel[v]; image.a[i]=SUPPORT_INDEX[bits];}
            sort(image.a.begin(),image.a.begin()+image.n);
            if(!initialized || lexicographical_compare(image.a.begin(),image.a.begin()+image.n,best.a.begin(),best.a.begin()+best.n)){best=image;initialized=true;}
            return;
        }
        auto g=groups[gi]; sort(g.begin(),g.end());
        do{for(int j=0;j<(int)g.size();++j) relabel[g[j]]=offset+j; rec(gi+1,offset+g.size());}while(next_permutation(g.begin(),g.end()));
    };
    rec(0,0); return best;
}

vector<long long> burnside_counts(){
    vector<long long> fixed(10,0); array<int,7> p={0,1,2,3,4,5,6};
    do{
        int support_map[35];
        for(int i=0;i<35;++i){int bits=0;for(int v:SUPPORTS[i])bits|=1<<p[v];support_map[i]=SUPPORT_INDEX[bits];}
        bool seen[35]={}; vector<int> lens;
        for(int i=0;i<35;++i) if(!seen[i]){int j=i,len=0;while(!seen[j]){seen[j]=true;++len;j=support_map[j];}lens.push_back(len);}
        long long dp[10]={};dp[0]=1;
        for(int len:lens){long long ndp[10]={};for(int t=0;t<=9;++t)if(dp[t])for(int mult=0;mult<=3;++mult){int nx=t+mult*len;if(nx<=9)ndp[nx]+=dp[t];}copy(begin(ndp),end(ndp),begin(dp));}
        for(int k=0;k<=9;++k)fixed[k]+=dp[k];
    }while(next_permutation(p.begin(),p.end()));
    vector<long long> out(10); for(int k=0;k<=9;++k){if(fixed[k]%5040){cerr<<"burnside fail\n";exit(2);}out[k]=fixed[k]/5040;} return out;
}

struct BlockData { uint16_t occ=0; int incidence=0; bool repeated=false; };
array<BlockData,35> block_data(const Multiset& ms,uint64_t& touched){
    int mult[35]={}; for(int i=0;i<ms.n;++i)++mult[ms.a[i]];
    array<BlockData,35> out{}; touched=0;
    for(int b=0;b<35;++b){
        int tb=0;for(int v:TRIANGLES[b])tb|=1<<v;
        uint16_t occ=0; bool rep=false;
        for(int i=0;i<ms.n;++i){int sb=0;for(int v:SUPPORTS[ms.a[i]])sb|=1<<v;if((sb&tb)!=tb)continue;occ|=uint16_t(1u<<i);if(mult[ms.a[i]]>=2)rep=true;}
        int inc=popcount((unsigned)occ); if(!inc)continue; touched|=1ULL<<b; out[b]={occ,inc,rep};
    }
    return out;
}

vector<int> allowed_empty_dims(const BlockData& x){
    vector<int> d;
    if(x.repeated){ if(x.incidence>=6) d.push_back(2); return d; }
    if(x.incidence>=5) d.push_back(1);
    if(x.incidence>=6) d.push_back(2);
    return d;
}

bool pair_compatible(const BlockData& x,int dx,const BlockData& y,int dy){
    int inter=popcount((unsigned)(x.occ&y.occ));
    int uni=x.incidence+y.incidence-inter;
    if(dx==1 && dy==1) return inter>=5 || uni>=6;
    if(dx!=dy) return inter>=5 || uni>=7;
    return inter>=6 || (inter>=5 && uni>=7) || uni>=8;
}
int occurrence_union_size(const vector<pair<int,int>>& chosen,const array<BlockData,35>& data,int singleton=-1){
    uint16_t u=0;for(auto [b,d]:chosen)u|=data[b].occ;if(singleton>=0)u|=data[singleton].occ;return popcount((unsigned)u);
}

bool structural_ok(uint64_t touched,uint64_t incomplete){
    uint64_t complete=touched & ~incomplete;
    int rc=triangle_rank(complete);
    int nullity=popcount(complete)-rc;
    if(nullity>1) return false;
    return triangle_rank(touched)-rc>=5;
}

bool support_survives(const array<BlockData,35>& data,uint64_t touched,long long& tests){
    int h=popcount(touched);
    vector<int> eligible;
    for(int b=0;b<35;++b) if(touched>>b&1ULL) if(!allowed_empty_dims(data[b]).empty()) eligible.push_back(b);
    vector<pair<int,int>> chosen;
    bool found=false;

    auto final_test=[&](int nominal_dim)->bool{
        ++tests;
        uint64_t empty_mask=0; for(auto [b,d]:chosen) empty_mask|=1ULL<<b;
        int e=chosen.size();
        // Singleton untouched (or touched only outside T): all touched incomplete blocks are empty.
        if(e>=h-11 && nominal_dim>=4 && occurrence_union_size(chosen,data)>=8 && structural_ok(touched,empty_mask)) return true;
        // Singleton touched. Its coefficient line may be zero or nonzero.
        if(e<h-12) return false;
        uint64_t remaining=touched & ~empty_mask;
        for(int s=0;s<35;++s) if(remaining>>s&1ULL){
            uint64_t incomplete=empty_mask|(1ULL<<s);
            // Zero singleton line.
            if(nominal_dim>=4 && occurrence_union_size(chosen,data)>=8 && structural_ok(touched,incomplete)) return true;
            // Nonzero singleton line: weight >=5 and pairwise compatible with chosen local spaces.
            if(data[s].incidence<5 || nominal_dim+1<4) continue;
            bool ok=true;for(auto [b,d]:chosen) if(!pair_compatible(data[b],d,data[s],1)){ok=false;break;}
            if(ok && occurrence_union_size(chosen,data,s)>=8 && structural_ok(touched,incomplete)) return true;
        }
        return false;
    };

    function<bool(int,int)> rec=[&](int idx,int nominal_dim)->bool{
        if(idx==(int)eligible.size()) return final_test(nominal_dim);
        int remaining=eligible.size()-idx;
        if((int)chosen.size()+remaining < max(0,h-12)) return false;
        // Skip this block.
        if(rec(idx+1,nominal_dim)) return true;
        int b=eligible[idx];
        for(int d:allowed_empty_dims(data[b])){
            bool ok=true;for(auto [c,dc]:chosen) if(!pair_compatible(data[b],d,data[c],dc)){ok=false;break;}
            if(!ok) continue;
            chosen.push_back({b,d});
            if(rec(idx+1,nominal_dim+d)) return true;
            chosen.pop_back();
        }
        return false;
    };
    found=rec(0,0); return found;
}

void initialize_geometry(){
    fill(begin(SUPPORT_INDEX),end(SUPPORT_INDEX),-1);fill(begin(TRIANGLE_INDEX),end(TRIANGLE_INDEX),-1);fill(begin(EDGE_INDEX),end(EDGE_INDEX),-1);
    for(int a=0;a<7;++a)for(int b=a+1;b<7;++b)for(int c=b+1;c<7;++c)for(int d=c+1;d<7;++d){int bits=(1<<a)|(1<<b)|(1<<c)|(1<<d);SUPPORT_INDEX[bits]=SUPPORTS.size();SUPPORTS.push_back({a,b,c,d});}
    for(int a=0;a<7;++a)for(int b=a+1;b<7;++b)for(int c=b+1;c<7;++c){int bits=(1<<a)|(1<<b)|(1<<c);TRIANGLE_INDEX[bits]=TRIANGLES.size();TRIANGLES.push_back({a,b,c});}
    for(int a=0;a<7;++a)for(int b=a+1;b<7;++b){EDGE_INDEX[(1<<a)|(1<<b)]=EDGES.size();EDGES.push_back({a,b});}
    for(int s=0;s<35;++s){uint64_t mask=0;for(int skip=0;skip<4;++skip){int bits=0;for(int j=0;j<4;++j)if(j!=skip)bits|=1<<SUPPORTS[s][j];mask|=1ULL<<TRIANGLE_INDEX[bits];}SUPPORT_TRIANGLE_MASK[s]=mask;}
    for(int b=0;b<35;++b){TRIANGLE_ROWS[b].fill(0);int a=TRIANGLES[b][0],c=TRIANGLES[b][1],d=TRIANGLES[b][2];TRIANGLE_ROWS[b][EDGE_INDEX[(1<<c)|(1<<d)]]=1;TRIANGLE_ROWS[b][EDGE_INDEX[(1<<a)|(1<<d)]]=-1;TRIANGLE_ROWS[b][EDGE_INDEX[(1<<a)|(1<<c)]]=1;}
}
bool lucas_lehmer_31(){long long s=4;for(int i=0;i<29;++i)s=(s*s-2)%MOD;return s==0;}

int main(){
    initialize_geometry();
    if(!lucas_lehmer_31()) return 10;
    if((long long)MOD*MOD<=14348907LL) return 11;
    vector<long long> expected={1,1,4,14,61,268,1283,6032,27763,121458};
    if(burnside_counts()!=expected) return 12;
    unordered_set<Multiset,MultisetHash> reps; Multiset empty; reps.insert(empty);
    for(int size=1;size<=8;++size){
        unordered_set<Multiset,MultisetHash> next; next.reserve(reps.size()*8);
        for(const auto& ms:reps){int mult[35]={};for(int i=0;i<ms.n;++i)++mult[ms.a[i]];for(int s=0;s<35;++s){if(mult[s]>=3)continue;Multiset x=ms;x.a[x.n++]=s;sort(x.a.begin(),x.a.begin()+x.n);next.insert(canonical(x));}}
        reps.swap(next); if((long long)reps.size()!=expected[size]){cerr<<"augment fail "<<size<<"\n";return 13;}
    }
    unordered_set<Multiset,MultisetHash> all9,h16; all9.reserve(130000);h16.reserve(10000);
    long long raw=0,hraw=0;
    for(const auto& ms:reps){int mult[35]={};uint64_t touched=0;for(int i=0;i<ms.n;++i){++mult[ms.a[i]];touched|=SUPPORT_TRIANGLE_MASK[ms.a[i]];}for(int s=0;s<35;++s){if(mult[s]>=3)continue;++raw;Multiset x=ms;x.a[x.n++]=s;sort(x.a.begin(),x.a.begin()+x.n);Multiset cx=canonical(x);all9.insert(cx);if(popcount(touched|SUPPORT_TRIANGLE_MASK[s])<=16){++hraw;h16.insert(cx);}}}
    if((long long)all9.size()!=expected[9]) return 14;
    long long tests=0,survivors=0; vector<Multiset> first;
    for(const auto& ms:h16){uint64_t touched=0;auto data=block_data(ms,touched);if(support_survives(data,touched,tests)){++survivors;if(first.size()<20)first.push_back(ms);}}
    if(hraw!=16189) return 15;
    if(h16.size()!=2634) return 16;
    if(tests!=2178) return 17;
    if(survivors!=0) return 18;
    cout<<"PASS: nine-no-root k=5 D=-2 d_root=1 p=1 support closure\n";
    cout<<"size9_orbits "<<all9.size()<<"\n";
    cout<<"h_le_16_raw_extensions "<<hraw<<"\n";
    cout<<"h_le_16_size9_orbits "<<h16.size()<<"\n";
    cout<<"relaxed_profile_tests "<<tests<<"\n";
    cout<<"support_level_survivors "<<survivors<<"\n";
    for(size_t i=0;i<first.size();++i){cout<<"survivor "<<i;for(int j=0;j<first[i].n;++j){cout<<' ';for(int v:SUPPORTS[first[i].a[j]])cout<<v;}cout<<"\n";}
    return 0;
}
