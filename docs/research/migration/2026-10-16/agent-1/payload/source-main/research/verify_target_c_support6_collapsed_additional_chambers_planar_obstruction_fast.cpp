// Finite exact-combinatorial planarization verifier for ch4, ch5, and ch6.
//
// The companion Python interval certificate proves the strict local roots, cyclic
// rotations, and angle-eligible pair lists.  This file exhausts the remaining
// crossing subsets, train orders, crossing rotations, and face permutations using
// only integer combinatorics.  Compile with:
//   g++ -O3 -std=c++17 this_file.cpp -o /tmp/collapsed_planar_fast
// and run the resulting binary.  A planar system would have F=E-V+2; none occurs.

#include <algorithm>
#include <array>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
using Edge = array<int, 2>;
const Edge E[12]={{0,1},{0,2},{0,4},{0,5},{1,2},{1,3},{1,5},{2,3},{2,4},{3,4},{3,5},{4,5}};
const int ROT4[6][4]={{0,2,3,1},{5,4,0,6},{1,7,8,4},{10,9,5,7},{8,11,9,2},{3,6,10,11}};
const int ROT5[6][4]={{1,2,0,3},{0,6,5,4},{4,7,1,8},{5,9,10,7},{11,8,9,2},{10,3,11,6}};
const int ROT6[6][4]={{1,2,0,3},{0,6,5,4},{4,7,8,1},{5,9,10,7},{8,11,9,2},{10,3,11,6}};
const int ROT7[6][4]={{1,2,3,0},{0,6,5,4},{8,4,1,7},{5,7,9,10},{9,11,8,2},{3,10,11,6}};

vector<pair<int,int>> eligible(int which){
  static const int A[10][2]={{0,7},{0,9},{0,11},{1,10},{2,5},{2,6},{3,9},{4,10},{5,11},{6,7}};
  static const int B[9][2]={{0,7},{0,8},{1,6},{2,4},{2,5},{2,10},{3,7},{5,8},{7,11}};
  static const int C[4][2]={{0,7},{2,5},{2,10},{6,8}};
  static const int D[4][2]={{2,4},{2,10},{3,7},{6,8}};
  vector<pair<int,int>> out;
  int n=which==0?10:(which==1?9:4);
  for(int i=0;i<n;i++) out.push_back(which==0?pair<int,int>{A[i][0],A[i][1]}:which==1?pair<int,int>{B[i][0],B[i][1]}:which==2?pair<int,int>{C[i][0],C[i][1]}:pair<int,int>{D[i][0],D[i][1]});
  return out;
}

bool triangle_free(const vector<pair<int,int>>& crossings){
  bool g[12][12]={};
  for(auto [a,b]:crossings) g[a][b]=g[b][a]=true;
  for(int a=0;a<12;a++) for(int b=a+1;b<12;b++) for(int c=b+1;c<12;c++)
    if(g[a][b]&&g[a][c]&&g[b][c]) return false;
  return true;
}

int faces(const vector<pair<int,int>>& crossings, const vector<vector<int>>& order,
          const vector<int>& bits, const int rotation[6][4]){
  int n=crossings.size(), N=6+n;
  vector<vector<int>> adj(N);
  for(int ei=0;ei<12;ei++){
    int a=E[ei][0], b=E[ei][1]; vector<int> chain{a};
    for(int x:order[ei]) chain.push_back(6+x);
    chain.push_back(b);
    for(int k=0;k+1<(int)chain.size();k++){
      adj[chain[k]].push_back(chain[k+1]);
      adj[chain[k+1]].push_back(chain[k]);
    }
  }
  for(int v=0;v<6;v++){
    adj[v].clear();
    for(int k=0;k<4;k++){
      int ei=rotation[v][k], x;
      if(order[ei].empty()) x=(E[ei][0]==v?E[ei][1]:E[ei][0]);
      else x=6+(E[ei][0]==v?order[ei].front():order[ei].back());
      adj[v].push_back(x);
    }
  }
  for(int k=0;k<n;k++){
    auto neighbors=[&](int ei){
      int p=0; while(order[ei][p]!=k) p++;
      int a=E[ei][0], b=E[ei][1];
      int x=(p==0?a:6+order[ei][p-1]);
      int y=(p+1==(int)order[ei].size()?b:6+order[ei][p+1]);
      return pair<int,int>{x,y};
    };
    auto a=neighbors(crossings[k].first), b=neighbors(crossings[k].second);
    adj[6+k]=(bits[k]==0?vector<int>{a.first,b.first,a.second,b.second}
                         :vector<int>{a.first,b.second,a.second,b.first});
  }
  set<pair<int,int>> seen; int f=0;
  for(int v=0;v<N;v++) for(int w:adj[v]) if(!seen.count({v,w})){
    f++; int a=v,b=w;
    while(!seen.count({a,b})){
      seen.insert({a,b}); auto &z=adj[b];
      int p=find(z.begin(),z.end(),a)-z.begin();
      int c=b,d=z[(p+1)%z.size()]; a=c; b=d;
    }
  }
  return f;
}

long long run(int which){
  auto allowed=eligible(which); const int (*rotation)[4]=which==0?ROT4:(which==1?ROT5:(which==2?ROT6:ROT7));
  long long subset_count=0, system_count=0; int m=allowed.size();
  for(int mask=0;mask<(1<<m);mask++){
    vector<pair<int,int>> crossings;
    for(int k=0;k<m;k++) if(mask&(1<<k)) crossings.push_back(allowed[k]);
    if(!triangle_free(crossings)) continue;
    subset_count++;
    vector<vector<int>> incidence(12);
    for(int k=0;k<(int)crossings.size();k++){
      incidence[crossings[k].first].push_back(k);
      incidence[crossings[k].second].push_back(k);
    }
    vector<int> multi;
    for(int e=0;e<12;e++) if(incidence[e].size()>1) multi.push_back(e);
    vector<vector<int>> permutations(multi.size());
    function<void(int)> recurse = [&](int q){
      if(q==(int)multi.size()){
        for(int bitmask=0;bitmask<(1<<crossings.size());bitmask++){
          vector<int> bits(crossings.size());
          for(int k=0;k<(int)bits.size();k++) bits[k]=(bitmask>>k)&1;
          vector<vector<int>> order=incidence;
          for(int k=0;k<(int)multi.size();k++) order[multi[k]]=permutations[k];
          system_count++;
          int V=6+crossings.size(), Ecount=12+2*crossings.size();
          if(faces(crossings,order,bits,rotation)==Ecount-V+2){
            cerr<<"UNEXPECTED_PLANARIZATION ch="<<(which+4)<<"\n";
            exit(1);
          }
        }
        return;
      }
      int e=multi[q]; vector<int> p=incidence[e]; sort(p.begin(),p.end());
      do{ permutations[q]=p; recurse(q+1); }while(next_permutation(p.begin(),p.end()));
    };
    recurse(0);
  }
  cout<<"ch"<<(which+4)<<" legal_crossing_subsets "<<subset_count
      <<" rotation_systems_tested "<<system_count<<"\n";
  return system_count;
}

int main(){ run(0); run(1); run(2); run(3); }
