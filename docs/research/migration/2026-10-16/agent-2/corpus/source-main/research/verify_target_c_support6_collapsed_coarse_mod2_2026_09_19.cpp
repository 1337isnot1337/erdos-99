#define main rotation_cell_base_main
#include "verify_target_c_support6_collapsed_rotation_cells_2026_09_19.cpp"
#undef main

#include <bitset>

struct ParityStats {
    bool consistent;
    int allowed_variables;
    int rank;
    int equations;
};

static vector<uint16_t> all_simple_cycles(const vector<Edge>& E) {
    vector<uint16_t> ans;
    for (int mask=1; mask<(1<<12); mask++) {
        const int k=__builtin_popcount((unsigned)mask);
        if (k<3 || k>6) continue;
        int deg[6]={0};
        for (int e=0;e<12;e++) if ((mask>>e)&1) {
            deg[E[e].a]++; deg[E[e].b]++;
        }
        int used=0, start=-1;
        bool ok=true;
        for (int v=0;v<6;v++) if (deg[v]) {
            used++; start=v;
            if (deg[v]!=2) ok=false;
        }
        if (!ok || used!=k) continue;
        bool vis[6]={false};
        vector<int> stack={start};
        vis[start]=true;
        int seen=0;
        while (!stack.empty()) {
            int v=stack.back(); stack.pop_back(); seen++;
            for (int e=0;e<12;e++) if ((mask>>e)&1) {
                int w=-1;
                if (E[e].a==v) w=E[e].b;
                else if (E[e].b==v) w=E[e].a;
                if (w>=0 && !vis[w]) { vis[w]=true; stack.push_back(w); }
            }
        }
        if (seen==used) ans.push_back((uint16_t)mask);
    }
    return ans;
}

static int pair_variable(int a,int b) {
    if (a>b) swap(a,b);
    assert(a<b);
    int id=0;
    for (int i=0;i<12;i++) for (int j=i+1;j<12;j++,id++)
        if (i==a && j==b) return id;
    assert(false);
    return -1;
}

static bool crossing_window_intersects_cell(int e,int f,const vector<Ineq>& base) {
    // x=3 alpha/pi. Strict rhombus crossing compatibility is
    // 1 < |x_e-x_f| < 2. Test both oriented intervals exactly.
    for (int sign=0;sign<2;sign++) {
        const int a=sign?f:e, b=sign?e:f;
        vector<Ineq> z=base;
        z.push_back({b,a,2});   // x_a-x_b < 2
        z.push_back({a,b,-1});  // x_b-x_a < -1
        if (strict_difference_feasible(z)) return true;
    }
    return false;
}

static int face_alternation(uint16_t C,uint16_t D,int v,const Cell& cell) {
    vector<int> posC, posD;
    for (int j=0;j<4;j++) {
        const int e=cell.order[v][j];
        if ((C>>e)&1) posC.push_back(j);
        if ((D>>e)&1) posD.push_back(j);
    }
    if (posC.empty() || posD.empty()) return 0;
    assert(posC.size()==2 && posD.size()==2);
    return ((posC[1]-posC[0]+4)%4)==2 ? 1 : 0;
}

static ParityStats coarse_mod2_system(const Cell& cell,const vector<Edge>& E) {
    vector<Ineq> base;
    base.reserve(120);
    for (int v=0;v<6;v++) add_gap_constraints(base,cell.order[v]);
    assert(strict_difference_feasible(base));

    bool allowed[12][12]={{false}};
    int allowed_count=0;
    for (int e=0;e<12;e++) for (int f=e+1;f<12;f++) {
        allowed[e][f]=crossing_window_intersects_cell(e,f,base);
        if (allowed[e][f]) allowed_count++;
    }

    const auto cycles=all_simple_cycles(E);
    vector<bitset<67>> rows;
    for (size_t i=0;i<cycles.size();i++) for (size_t j=i+1;j<cycles.size();j++) {
        const uint16_t C=cycles[i], D=cycles[j];
        if (C&D) continue; // MI.1 requires edge-disjoint cycles.
        bitset<67> row;
        int rhs=0;
        for (int v=0;v<6;v++) rhs^=face_alternation(C,D,v,cell);
        for (int e=0;e<12;e++) if ((C>>e)&1)
            for (int f=0;f<12;f++) if ((D>>f)&1) {
                const int a=min(e,f), b=max(e,f);
                assert(a!=b);
                if (allowed[a][b]) row.flip(pair_variable(a,b));
            }
        if (rhs) row.set(66);
        rows.push_back(row);
    }

    int rank=0;
    for (int col=0;col<66 && rank<(int)rows.size();col++) {
        int p=rank;
        while (p<(int)rows.size() && !rows[p].test(col)) p++;
        if (p==(int)rows.size()) continue;
        swap(rows[p],rows[rank]);
        for (int r=0;r<(int)rows.size();r++)
            if (r!=rank && rows[r].test(col)) rows[r]^=rows[rank];
        rank++;
    }

    bool consistent=true;
    for (const auto& row:rows) {
        bool any=false;
        for (int col=0;col<66;col++) if (row.test(col)) { any=true; break; }
        if (!any && row.test(66)) { consistent=false; break; }
    }
    return {consistent,allowed_count,rank,(int)rows.size()};
}

static void run_mod2_case(const string& name,const set<pair<int,int>>& missing,
                          int expected_cells) {
    map<int,int> genus_count, per_orientation;
    const auto cells=enumerate_cells(missing,genus_count,per_orientation);
    const auto E=make_edges(missing);
    assert((int)cells.size()==expected_cells);

    int inconsistent=0;
    int amin=100,amax=-1,rmin=100,rmax=-1,dmin=100,dmax=-1;
    map<int,int> dim_hist;
    for (const auto& cell:cells) {
        const auto p=coarse_mod2_system(cell,E);
        if (!p.consistent) inconsistent++;
        amin=min(amin,p.allowed_variables); amax=max(amax,p.allowed_variables);
        rmin=min(rmin,p.rank); rmax=max(rmax,p.rank);
        const int dim=p.allowed_variables-p.rank;
        dmin=min(dmin,dim); dmax=max(dmax,dim); dim_hist[dim]++;
    }
    assert(inconsistent==0);
    cout << name << ": cells=" << cells.size()
         << ", coarse-parity-inconsistent=0"
         << ", allowed-vars=" << amin << ".." << amax
         << ", rank=" << rmin << ".." << rmax
         << ", affine-dim=" << dmin << ".." << dmax << "\n";
    cout << name << ": affine-dim histogram";
    for (auto [d,n]:dim_hist) cout << " " << d << ":" << n;
    cout << "\n";
}

int main() {
    run_mod2_case("all-cross matching", {{0,3},{1,4},{2,5}}, 180);
    run_mod2_case("mixed matching", {{0,1},{2,3},{4,5}}, 208);
    cout << "PASS: coarse MI.1 parity is consistent on all 388 rotation cells; crossing-wall subdivision is necessary.\n";
    return 0;
}
