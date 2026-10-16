// Exact seven-outsider exchange verifier for Target C.
//
// Input is generated from the committed Python four-exchange verifier.  The
// core uses F_251 only to index quotient spans and determine ranks.  Residual
// entries are in {-1,0,1}; Hadamard bounds make every rank<=4 decision exact
// over Q because any nonzero 5x5 minor has absolute value < 56 < 251.
// Every residual set of rank <=4 is covered: rank-4 sets lie in an enumerated
// rank-4 flat, while lower-rank sets extend to rank 4 in the ambient residual
// vector matroid and hence lie in such a flat.  Hash collisions in the flat
// table can only merge flats and over-enumerate seven-sets. Every emitted
// seven-set is re-ranked, so hashing is not a proof assumption.
#include <bits/stdc++.h>
using namespace std; using i64=long long; using i128=__int128_t; static const int P=251,N=59,C=165,K=45;
int RES[C][N],F2[C][K];
int detn(const vector<vector<int>>& M){int n=M.size(); if(n==1)return M[0][0]; long long total=0; for(int j=0;j<n;j++){vector<vector<int>> m(n-1,vector<int>(n-1));for(int r=1;r<n;r++){int cc=0;for(int c=0;c<n;c++)if(c!=j)m[r-1][cc++]=M[r][c];}int d=detn(m); total += (j&1?-1:1)*(long long)M[0][j]*d;} return (int)total;}
int invp(int a){int r=1,b=a,e=P-2;while(e){if(e&1)r=r*b%P;b=b*b%P;e>>=1;}return r;}
struct Kern{int r; vector<array<int,7>> rel;};
Kern kernel(uint64_t z){int E[7];for(int i=0;i<7;i++)E[i]=(z>>(8*i))&255;vector<int> basis,pivs; for(int idx=0;idx<7;idx++){int *v=RES[E[idx]]; if(basis.empty()){int q=0;while(q<N && ((v[q]%P)+P)%P==0)q++;basis.push_back(idx);pivs.push_back(q);continue;}int r=basis.size();int A[4][5]{};for(int i=0;i<r;i++){for(int j=0;j<r;j++)A[i][j]=(RES[E[basis[j]]][pivs[i]]%P+P)%P;A[i][r]=(v[pivs[i]]%P+P)%P;}for(int col=0;col<r;col++){int p=col;while(p<r&&!A[p][col])p++;assert(p<r);for(int j=col;j<=r;j++)swap(A[p][j],A[col][j]);int inv=invp(A[col][col]);for(int j=col;j<=r;j++)A[col][j]=A[col][j]*inv%P;for(int i=0;i<r;i++)if(i!=col&&A[i][col]){int q=A[i][col];for(int j=col;j<=r;j++){A[i][j]=(A[i][j]-q*A[col][j])%P;if(A[i][j]<0)A[i][j]+=P;}}}int coeff[4];for(int i=0;i<r;i++)coeff[i]=A[i][r];int bad=-1;for(int q=0;q<N;q++){long long s=0;for(int j=0;j<r;j++)s+=(long long)coeff[j]*RES[E[basis[j]]][q];int d=(v[q]-s)%P;if(d<0)d+=P;if(d){bad=q;break;}}if(bad>=0){basis.push_back(idx);pivs.push_back(bad); assert(basis.size()<=4);}}
 int r=basis.size(); vector<vector<int>> M(r,vector<int>(r));for(int i=0;i<r;i++)for(int j=0;j<r;j++)M[i][j]=RES[E[basis[j]]][pivs[i]];int D=detn(M);assert(D&&D%P);vector<array<int,7>> rel;for(int j=0;j<7;j++){if(find(basis.begin(),basis.end(),j)!=basis.end())continue;vector<int> nums(r);for(int k=0;k<r;k++){auto Mk=M;for(int i=0;i<r;i++)Mk[i][k]=RES[E[j]][pivs[i]];nums[k]=detn(Mk);}array<int,7>a{};a[j]=D;for(int k=0;k<r;k++)a[basis[k]]-=nums[k];rel.push_back(a);}return {r,rel};}
struct V3{i64 x[3];};
V3 cross(V3 a,V3 b){return {{a.x[1]*b.x[2]-a.x[2]*b.x[1],a.x[2]*b.x[0]-a.x[0]*b.x[2],a.x[0]*b.x[1]-a.x[1]*b.x[0]}};}
i64 dot(V3 a,V3 b){return a.x[0]*b.x[0]+a.x[1]*b.x[1]+a.x[2]*b.x[2];}bool nz(V3 a){return a.x[0]||a.x[1]||a.x[2];}
bool compensate_r4(uint64_t z,const Kern& k){assert(k.r==4&&k.rel.size()==3);int E[7];for(int i=0;i<7;i++)E[i]=(z>>(8*i))&255;V3 full[15];bool fgood[15]{};V3 dbl[15][3];bool dgood[15][3]{};for(int b=0;b<15;b++){ // compute each H row at 3 coords
 i64 h[3][3]{};for(int rr=0;rr<3;rr++)for(int t=0;t<7;t++){int a=k.rel[rr][t];if(!a)continue;for(int p=0;p<3;p++)h[rr][p]+=(i64)a*F2[E[t]][3*b+p];}
 bool ok=true;V3 u{};for(int rr=0;rr<3;rr++){u.x[rr]=h[rr][0];if(h[rr][1]!=-u.x[rr]||h[rr][2]!=-u.x[rr])ok=false;}if(ok){fgood[b]=true;full[b]=u;}
 for(int o=0;o<3;o++){int ps[2],q=0;for(int p=0;p<3;p++)if(p!=o)ps[q++]=p;V3 v{};ok=true;for(int rr=0;rr<3;rr++){int p0=ps[0];i64 coeff=h[rr][p0]*(p0==0?1:-1);v.x[rr]=coeff;for(int ii=0;ii<2;ii++){int p=ps[ii];i64 g=(p==0?1:-1);if(h[rr][p]!=coeff*g)ok=false;}}if(ok){dgood[b][o]=true;dbl[b][o]=v;}}
 }
 for(int d=0;d<15;d++)for(int o=0;o<3;o++)if(dgood[d][o]&&nz(dbl[d][o])){vector<V3> U;for(int b=0;b<15;b++)if(b!=d&&fgood[b]&&nz(full[b]))U.push_back(full[b]);if(U.size()<2)continue;V3 u=U[0],normal{};int rank=1;for(size_t i=1;i<U.size();i++){V3 n=cross(u,U[i]);if(nz(n)){normal=n;rank=2;break;}}if(rank<2)continue;bool r3=false;for(auto w:U)if(dot(normal,w)!=0){r3=true;break;}if(r3)return true;if(dot(normal,dbl[d][o])!=0)return true;}
 return false;}

struct V4 { i64 x[4]; };
bool nz4(const V4 &a){return a.x[0]||a.x[1]||a.x[2]||a.x[3];}
bool prop4(const V4 &a,const V4 &b){
    int p=-1; for(int i=0;i<4;i++) if(a.x[i]){p=i;break;}
    if(p<0) return true; // zero with anything doesn't raise rank
    for(int i=0;i<4;i++) if((i128)a.x[p]*b.x[i]!=(i128)b.x[p]*a.x[i]) return false;
    return true;
}
i128 det4v(const V4&a,const V4&b,const V4&c,const V4&d){
    i64 M[4][4]; for(int i=0;i<4;i++){M[i][0]=a.x[i];M[i][1]=b.x[i];M[i][2]=c.x[i];M[i][3]=d.x[i];}
    i128 tot=0;
    for(int p0=0;p0<4;p0++)for(int p1=0;p1<4;p1++)if(p1!=p0)for(int p2=0;p2<4;p2++)if(p2!=p0&&p2!=p1){int p3=6-p0-p1-p2; if(p3<0||p3>3||p3==p0||p3==p1||p3==p2)continue; int perm[4]={p0,p1,p2,p3},inv=0;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)if(perm[i]>perm[j])inv++; i128 term=(i128)M[0][p0]*M[1][p1]*M[2][p2]*M[3][p3];tot += (inv&1)?-term:term;}
    // loop above counts each permutation once
    return tot;
}
bool rank3cols(const V4&a,const V4&b,const V4&c){
    // any 3x3 minor nonzero
    const V4 v[3]={a,b,c};
    for(int omit=0;omit<4;omit++){int rr[3],q=0;for(int i=0;i<4;i++)if(i!=omit)rr[q++]=i; i128 det=(i128)v[0].x[rr[0]]*(v[1].x[rr[1]]*v[2].x[rr[2]]-v[1].x[rr[2]]*v[2].x[rr[1]])-(i128)v[1].x[rr[0]]*(v[0].x[rr[1]]*v[2].x[rr[2]]-v[0].x[rr[2]]*v[2].x[rr[1]])+(i128)v[2].x[rr[0]]*(v[0].x[rr[1]]*v[1].x[rr[2]]-v[0].x[rr[2]]*v[1].x[rr[1]]);if(det)return true;}
    return false;
}
struct Block4 {V4 full; V4 fdev1,fdev2; bool fgood; V4 dbl[3],ddev[3]; bool dgood[3]; V4 single[3];};
void blocks_r3(uint64_t z,const Kern& k, Block4 B[15]){assert(k.r==3&&k.rel.size()==4);int E[7];for(int i=0;i<7;i++)E[i]=(z>>(8*i))&255;for(int b=0;b<15;b++){i64 h[4][3]{};for(int rr=0;rr<4;rr++)for(int t=0;t<7;t++){int a=k.rel[rr][t];if(!a)continue;for(int p=0;p<3;p++)h[rr][p]+=(i64)a*F2[E[t]][3*b+p];}
  V4 a{},d1{},d2{};for(int rr=0;rr<4;rr++){a.x[rr]=h[rr][0];d1.x[rr]=h[rr][1]+h[rr][0];d2.x[rr]=h[rr][2]+h[rr][0];}B[b].full=a;B[b].fdev1=d1;B[b].fdev2=d2;B[b].fgood=!nz4(d1)&&!nz4(d2);
  for(int o=0;o<3;o++){int ps[2],q=0;for(int p=0;p<3;p++)if(p!=o)ps[q++]=p;int p0=ps[0],p1=ps[1];V4 c{},dev{};for(int rr=0;rr<4;rr++){i64 g0=(p0==0?1:-1),g1=(p1==0?1:-1);c.x[rr]=h[rr][p0]*g0;dev.x[rr]=h[rr][p1]-c.x[rr]*g1;}B[b].dbl[o]=c;B[b].ddev[o]=dev;B[b].dgood[o]=!nz4(dev);}
  for(int p=0;p<3;p++){V4 c{};i64 gp=(p==0?1:-1);for(int rr=0;rr<4;rr++)c.x[rr]=h[rr][p]*gp;B[b].single[p]=c;}
 }}
bool comp_r3_t3(Block4 B[15]){
 for(int a=0;a<15;a++)for(int b=a+1;b<15;b++)for(int c=0;c<15;c++)if(c!=a&&c!=b)for(int o=0;o<3;o++){
   V4 devs[5]={B[a].fdev1,B[a].fdev2,B[b].fdev1,B[b].fdev2,B[c].ddev[o]};V4 d{};bool have=false,bad=false;for(auto &v:devs)if(nz4(v)){if(!have){d=v;have=true;}else if(!prop4(d,v)){bad=true;break;}}if(bad)continue;
   if(!have){if(rank3cols(B[a].full,B[b].full,B[c].dbl[o]))return true;}
   else if(det4v(B[a].full,B[b].full,B[c].dbl[o],d)!=0)return true;
 }
 return false;
}
bool comp_r3_t4(Block4 B[15], long long *optcounts=nullptr){
 vector<int> F; vector<pair<int,int>> D; for(int b=0;b<15;b++){if(B[b].fgood)F.push_back(b);for(int o=0;o<3;o++)if(B[b].dgood[o])D.push_back({b,o});}
 if(optcounts){optcounts[0]+=F.size();optcounts[1]+=D.size();}
 // 3+3+1+1
 for(size_t ia=0;ia<F.size();ia++)for(size_t ib=ia+1;ib<F.size();ib++){int a=F[ia],b=F[ib];for(int c=0;c<15;c++)if(c!=a&&c!=b)for(int d=c+1;d<15;d++)if(d!=a&&d!=b)for(int p=0;p<3;p++)for(int q=0;q<3;q++)if(det4v(B[a].full,B[b].full,B[c].single[p],B[d].single[q])!=0)return true;}
 // 3+2+2+1
 for(int a:F)for(size_t i=0;i<D.size();i++)if(D[i].first!=a)for(size_t j=i+1;j<D.size();j++){auto [b,ob]=D[i];auto [c,oc]=D[j];if(c==b||c==a)continue;for(int d=0;d<15;d++)if(d!=a&&d!=b&&d!=c)for(int p=0;p<3;p++)if(det4v(B[a].full,B[b].dbl[ob],B[c].dbl[oc],B[d].single[p])!=0)return true;}
 // 2+2+2+2
 for(size_t i=0;i<D.size();i++)for(size_t j=i+1;j<D.size();j++){auto [a,oa]=D[i];auto [b,ob]=D[j];if(a==b)continue;for(size_t k=j+1;k<D.size();k++){auto [c,oc]=D[k];if(c==a||c==b)continue;for(size_t l=k+1;l<D.size();l++){auto [d,od]=D[l];if(d==a||d==b||d==c)continue;if(det4v(B[a].dbl[oa],B[b].dbl[ob],B[c].dbl[oc],B[d].dbl[od])!=0)return true;}}}
 return false;
}
bool compensate_r3(uint64_t z,const Kern& k,long long *optcounts=nullptr){Block4 B[15];blocks_r3(z,k,B);if(comp_r3_t3(B))return true;if(comp_r3_t4(B,optcounts))return true;return false;}

struct FlatMask { uint64_t lo=0, hi=0; };
static inline uint64_t mix64(uint64_t x){
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

uint64_t rank4_span_hash(const vector<array<unsigned char,N>>& dirs, int a,int b,int c,int d,int &rank){
    int ids[4]={a,b,c,d}; unsigned char R[4][N];
    for(int i=0;i<4;i++)for(int j=0;j<N;j++)R[i][j]=dirs[ids[i]][j];
    int r=0;
    for(int col=0;col<N && r<4;col++){
        int piv=-1; for(int i=r;i<4;i++) if(R[i][col]){piv=i;break;}
        if(piv<0) continue;
        if(piv!=r) for(int j=0;j<N;j++) swap(R[piv][j],R[r][j]);
        int inv=invp(R[r][col]);
        for(int j=col;j<N;j++) R[r][j]=R[r][j]*inv%P;
        for(int i=0;i<4;i++) if(i!=r && R[i][col]){
            int q=R[i][col];
            for(int j=col;j<N;j++){
                int z=R[i][j]-q*R[r][j]%P; if(z<0)z+=P; R[i][j]=z;
            }
        }
        r++;
    }
    rank=r;
    uint64_t h=0x123456789abcdef0ULL ^ (uint64_t)r;
    for(int i=0;i<r;i++)for(int j=0;j<N;j++)
        h=mix64(h ^ ((uint64_t)R[i][j] + 0x100ULL*(j+1) + 0x10000ULL*(i+1)));
    return h;
}

uint64_t pack7(const int a[7]){
    uint64_t z=0; for(int i=0;i<7;i++) z |= (uint64_t)a[i] << (8*i); return z;
}

vector<uint64_t> build_candidate_superset(const vector<vector<int>>& class_cycles,
                                          const vector<array<unsigned char,N>>& dirs){
    const int M=(int)class_cycles.size();
    assert(M==105);
    unordered_map<uint64_t,FlatMask> flats;
    flats.reserve(5000000);
    for(int a=0;a<M;a++)for(int b=a+1;b<M;b++)for(int c=b+1;c<M;c++)for(int d=c+1;d<M;d++){
        int r; uint64_t h=rank4_span_hash(dirs,a,b,c,d,r); if(r<4) continue;
        FlatMask &m=flats[h]; int ids[4]={a,b,c,d};
        for(int q:ids){ if(q<64)m.lo|=1ULL<<q; else m.hi|=1ULL<<(q-64); }
    }
    unordered_set<uint64_t> cand;
    cand.reserve(12000000);
    for(const auto &kv:flats){
        vector<int> cyc;
        const auto &m=kv.second;
        for(int ci=0;ci<M;ci++){
            bool in=ci<64 ? ((m.lo>>ci)&1ULL) : ((m.hi>>(ci-64))&1ULL);
            if(in) for(int e:class_cycles[ci]) cyc.push_back(e);
        }
        sort(cyc.begin(),cyc.end());
        int s=(int)cyc.size(); if(s<7) continue;
        int a[7];
        for(int i0=0;i0<s;i0++)for(int i1=i0+1;i1<s;i1++)for(int i2=i1+1;i2<s;i2++)
        for(int i3=i2+1;i3<s;i3++)for(int i4=i3+1;i4<s;i4++)for(int i5=i4+1;i5<s;i5++)
        for(int i6=i5+1;i6<s;i6++){
            a[0]=cyc[i0];a[1]=cyc[i1];a[2]=cyc[i2];a[3]=cyc[i3];a[4]=cyc[i4];a[5]=cyc[i5];a[6]=cyc[i6];
            cand.insert(pack7(a));
        }
    }
    vector<uint64_t> out(cand.begin(),cand.end()); sort(out.begin(),out.end()); return out;
}

int mod_rank7(uint64_t z){
    int E[7]; for(int i=0;i<7;i++)E[i]=(z>>(8*i))&255;
    int A[7][N]; for(int i=0;i<7;i++)for(int j=0;j<N;j++)A[i][j]=(RES[E[i]][j]%P+P)%P;
    int r=0;
    for(int col=0;col<N && r<7;col++){
        int piv=-1;for(int i=r;i<7;i++)if(A[i][col]){piv=i;break;} if(piv<0)continue;
        for(int j=col;j<N;j++)swap(A[piv][j],A[r][j]); int inv=invp(A[r][col]);
        for(int j=col;j<N;j++)A[r][j]=A[r][j]*inv%P;
        for(int i=r+1;i<7;i++)if(A[i][col]){int q=A[i][col];for(int j=col;j<N;j++){A[i][j]=(A[i][j]-q*A[r][j])%P;if(A[i][j]<0)A[i][j]+=P;}}
        r++;
    }
    return r;
}

int main(int argc,char**argv){
    string input; size_t start=0, stop=numeric_limits<size_t>::max();
    for(int i=1;i<argc;i++){
        string a=argv[i];
        if(a=="--input" && i+1<argc) input=argv[++i];
        else if(a=="--start" && i+1<argc) start=stoull(argv[++i]);
        else if(a=="--stop" && i+1<argc) stop=stoull(argv[++i]);
        else { cerr<<"unknown argument: "<<a<<"\n"; return 2; }
    }
    if(input.empty()){ cerr<<"--input is required\n"; return 2; }
    ifstream f(input); int c,n,k; f>>c>>n>>k; assert(c==C && n==N && k==K);
    vector<int> hint(C); string line; getline(f,line);
    int max_abs_res=0,max_abs_f2=0;
    for(int e=0;e<C;e++){
        getline(f,line); auto pos=line.find('|'); assert(pos!=string::npos);
        stringstream a(line.substr(0,pos)), b(line.substr(pos+1)); a>>hint[e];
        for(int j=0;j<N;j++){a>>RES[e][j];max_abs_res=max(max_abs_res,abs(RES[e][j]));}
        for(int j=0;j<K;j++){b>>F2[e][j];max_abs_f2=max(max_abs_f2,abs(F2[e][j]));}
    }
    assert(max_abs_res==1); assert(max_abs_f2<=2);

    int M=*max_element(hint.begin(),hint.end())+1; assert(M==105);
    vector<vector<int>> class_cycles(M);
    for(int e=0;e<C;e++){assert(0<=hint[e]&&hint[e]<M);class_cycles[hint[e]].push_back(e);}
    int singles=0,pairs=0; vector<array<unsigned char,N>> dirs(M);
    for(int ci=0;ci<M;ci++){
        if(class_cycles[ci].size()==1) singles++; else if(class_cycles[ci].size()==2) pairs++; else assert(false);
        int e0=class_cycles[ci][0]; int first=0;while(first<N&&!RES[e0][first])first++;assert(first<N);int sign=RES[e0][first]>0?1:-1;
        for(int j=0;j<N;j++)dirs[ci][j]=(sign*RES[e0][j]%P+P)%P;
        for(int e:class_cycles[ci]){
            int p=0;while(p<N&&!RES[e][p])p++;int s=RES[e][p]>0?1:-1;
            for(int j=0;j<N;j++)assert((s*RES[e][j]%P+P)%P==dirs[ci][j]);
        }
    }
    assert(singles==45 && pairs==60);

    auto ledger=build_candidate_superset(class_cycles,dirs);
    vector<uint64_t> valid; valid.reserve(ledger.size()); long long rank3=0,rank4=0,collision_artifacts=0;
    for(uint64_t z:ledger){int r=mod_rank7(z);if(r>4){collision_artifacts++;continue;}assert(r>=3);valid.push_back(z);if(r==3)rank3++;else {assert(r==4);rank4++;}}
    assert(valid.size()==9382140); assert(rank3==10020); assert(rank4==9372120);
    assert(collision_artifacts==0);

    if(stop==numeric_limits<size_t>::max()) stop=valid.size();
    assert(start<=stop && stop<=valid.size());
    long long checked3=0,checked4=0;
    for(size_t i=start;i<stop;i++){
        uint64_t z=valid[i]; Kern ke=kernel(z); assert(ke.r==mod_rank7(z));
        bool bad;
        if(ke.r==4){checked4++;bad=compensate_r4(z,ke);} else {assert(ke.r==3);checked3++;bad=compensate_r3(z,ke);}
        if(bad){cerr<<"compensating seven-outsider candidate at ledger index "<<i<<"\n";return 1;}
    }
    cout<<"PASS: seven-outsider 44-cycle exchange barrier slice\n";
    cout<<"candidate ledger: "<<valid.size()<<" exact rank<=4 seven-outsider sets\n";
    cout<<"global ranks: rank3="<<rank3<<" rank4="<<rank4<<"\n";
    cout<<"checked slice: ["<<start<<", "<<stop<<") rank3="<<checked3<<" rank4="<<checked4<<"\n";
    if(start==0 && stop==valid.size()) cout<<"conclusion: any sufficient 44-cycle family must use >=8 external cycles\n";
    return 0;
}
