#define main rotation_cell_base_main
#include "verify_target_c_support6_collapsed_rotation_cells_2026_09_19.cpp"
#undef main

#include <bitset>

static bool crossing_window_intersects_cell(int e,int f,const vector<Ineq>& base) {
    for (int sign=0;sign<2;sign++) {
        const int a=sign?f:e, b=sign?e:f;
        vector<Ineq> z=base;
        z.push_back({b,a,2});
        z.push_back({a,b,-1});
        if (strict_difference_feasible(z)) return true;
    }
    return false;
}

static bool no_cross(int e, int f, const vector<Ineq>& base) {
    return !crossing_window_intersects_cell(e, f, base);
}

static int edge_id(const vector<Edge>& E, int a, int b) {
    auto q=minmax(a,b);
    for (int i=0;i<(int)E.size();i++)
        if (E[i].a==q.first && E[i].b==q.second) return i;
    return -1;
}

static vector<int> cycle_vertices(uint16_t C, const vector<Edge>& E) {
    vector<int> out;
    int deg[6]={0};
    for (int e=0;e<12;e++) if ((C>>e)&1) {
        deg[E[e].a]++; deg[E[e].b]++;
    }
    for (int v=0;v<6;v++) if (deg[v]) out.push_back(v);
    return out;
}

static vector<uint16_t> triangle_cycles(const vector<Edge>& E) {
    vector<uint16_t> out;
    for (int a=0;a<6;a++) for (int b=a+1;b<6;b++) for (int c=b+1;c<6;c++) {
        const int ab=edge_id(E,a,b), ac=edge_id(E,a,c), bc=edge_id(E,b,c);
        if (ab>=0 && ac>=0 && bc>=0)
            out.push_back((uint16_t(1)<<ab)|(uint16_t(1)<<ac)|(uint16_t(1)<<bc));
    }
    return out;
}

static bool in_ccw_arc(int from, int to, int x) {
    int p=from;
    while (true) {
        p=(p+1)%4;
        if (p==to) return false;
        if (p==x) return true;
    }
}

static int side_of_spoke(int v, int prev, int next, int spoke, const Cell& cell,
                         const vector<Edge>& E) {
    int pin=-1, pout=-1, ps=-1;
    for (int j=0;j<4;j++) {
        const int e=cell.order[v][j];
        const int a=E[e].a, b=E[e].b;
        if (a==prev || b==prev) pin=j;
        if (a==next || b==next) pout=j;
        if (a==spoke || b==spoke) ps=j;
    }
    assert(pin>=0 && pout>=0 && ps>=0 && pin!=pout && ps!=pin && ps!=pout);
    return in_ccw_arc(pin,pout,ps) ? 1 : 0;
}

static bool triangle_non_crossing(uint16_t C, const vector<Ineq>& base) {
    vector<int> ce;
    for (int e=0;e<12;e++) if ((C>>e)&1) ce.push_back(e);
    for (int i=0;i<(int)ce.size();i++) for (int j=i+1;j<(int)ce.size();j++)
        if (!no_cross(ce[i],ce[j],base)) return false;
    return true;
}

static bool jordan_template(const Cell& cell, const vector<Edge>& E,
                            const vector<Ineq>& base,
                            const vector<uint16_t>& triangles) {
    for (uint16_t C:triangles) {
        if (!triangle_non_crossing(C,base)) continue;
        const auto V=cycle_vertices(C,E);
        assert(V.size()==3);
        // Choose either orientation of the triangle.  Reversing it swaps both
        // side labels, so the existence test is orientation-independent.
        for (int start:V) {
            int n1=-1,n2=-1;
            for (int e=0;e<12;e++) if ((C>>e)&1 && (E[e].a==start || E[e].b==start)) {
                int w=(E[e].a==start?E[e].b:E[e].a);
                if (n1<0) n1=w; else n2=w;
            }
            for (int next: {n1,n2}) {
                const int middle=(next==n1?n2:n1);
                int mnext=-1, mprev=-1;
                for (int e=0;e<12;e++) if ((C>>e)&1 && (E[e].a==middle || E[e].b==middle)) {
                    int w=(E[e].a==middle?E[e].b:E[e].a);
                    if (w==next) mnext=next; else if (w==start) mprev=start;
                }
                if (!(mnext>=0 && mprev>=0)) {
                    cerr << "bad triangle orientation start=" << start << " next=" << next
                         << " middle=" << middle << " n1=" << n1
                         << " n2=" << n2 << " C=" << C << "\\n";
                    continue;
                }

                for (int x=0;x<6;x++) if (x!=start && x!=middle && x!=next) {
                    int sx=edge_id(E,start,x);
                    if (sx<0) continue;
                    bool spoke_ok=true;
                    for (int e=0;e<12;e++) if ((C>>e)&1)
                        if (!no_cross(sx,e,base)) spoke_ok=false;
                    if (!spoke_ok) continue;
                    int side_x=side_of_spoke(start,middle,next,x,cell,E);
                    for (int y=0;y<6;y++) {
                        if (y==x || y==start || y==middle || y==next) continue;
                        int sy=edge_id(E,middle,y), bridge=edge_id(E,x,y);
                        if (sy<0 || bridge<0 || side_x==side_of_spoke(middle,next,start,y,cell,E)) continue;
                        bool ok=true;
                        for (int e=0;e<12;e++) if ((C>>e)&1)
                            if (!no_cross(sy,e,base) || !no_cross(bridge,e,base)) ok=false;
                        if (ok) return true;
                    }
                }
            }
        }
    }
    return false;
}

static int templates_for_cell(const Cell& cell, const vector<Edge>& E,
                              const vector<uint16_t>& triangles) {
    vector<Ineq> base;
    for (int v=0;v<6;v++) add_gap_constraints(base,cell.order[v]);
    int n=0;
    for (uint16_t C:triangles) {
        if (!triangle_non_crossing(C,base)) continue;
        // Count only whether this triangle admits any separator; this avoids
        // inflating the certificate with equivalent spoke choices.
        Cell one=cell;
        (void)one;
        // The full predicate is called once below; a boolean count is enough.
        if (jordan_template(cell,E,base,{C})) n++;
    }
    return n;
}

static void run_case(const string& name, const set<pair<int,int>>& missing,
                     int expected_cells) {
    map<int,int> genus_count, per_orientation;
    const auto cells=enumerate_cells(missing,genus_count,per_orientation);
    const auto E=make_edges(missing);
    const auto triangles=triangle_cycles(E);
    int killed=0, min_templates=100, max_templates=0;
    for (const auto& cell:cells) {
        const int t=templates_for_cell(cell,E,triangles);
        if (t) killed++;
        min_templates=min(min_templates,t);
        max_templates=max(max_templates,t);
    }
    cout << name << ": cells=" << cells.size()
         << ", jordan_template_killed=" << killed
         << ", survivors=" << (cells.size()-killed)
         << ", templates_per_cell=" << min_templates << ".." << max_templates << "\n";
    assert((int)cells.size()==expected_cells);
}

int main() {
    run_case("all-cross matching", {{0,3},{1,4},{2,5}}, 180);
    run_case("mixed matching", {{0,1},{2,3},{4,5}}, 208);
    cout << "PASS: exact coarse Jordan-template scan completed; remaining cells require threshold refinement or nonlinear closure.\n";
}
