#include <iostream>
#include "k5_d1p2_search.hpp"

int main() {
    init_geom();
    if (!ll31()) return 10;
    if ((long long) MOD * MOD <= 14348907LL) return 11;

    vector<long long> expected = {1,1,4,14,61,268,1283,6032,27763,121458};
    if (burn() != expected) return 12;

    unordered_set<Multiset,H> level;
    Multiset zero;
    level.insert(zero);

    for (int n = 1; n <= 8; ++n) {
        unordered_set<Multiset,H> next;
        next.reserve(level.size() * 8);
        for (auto const& m : level) {
            int q[35] = {};
            for (int i = 0; i < m.n; ++i) ++q[m.a[i]];
            for (int s = 0; s < 35; ++s) {
                if (q[s] >= 3) continue;
                Multiset y = m;
                y.a[y.n++] = s;
                sort(y.a.begin(), y.a.begin() + y.n);
                next.insert(canonical(y));
            }
        }
        level.swap(next);
        if ((long long) level.size() != expected[n]) return 13;
    }

    unordered_set<Multiset,H> all9, h20;
    all9.reserve(130000);
    h20.reserve(40000);

    long long raw = 0;
    long long hraw = 0;

    for (auto const& m : level) {
        int q[35] = {};
        uint64_t t = 0;
        for (int i = 0; i < m.n; ++i) {
            ++q[m.a[i]];
            t |= STM[m.a[i]];
        }
        for (int s = 0; s < 35; ++s) {
            if (q[s] >= 3) continue;
            ++raw;
            Multiset y = m;
            y.a[y.n++] = s;
            sort(y.a.begin(), y.a.begin() + y.n);
            y = canonical(y);
            all9.insert(y);
            if (popcount(t | STM[s]) <= 20) {
                ++hraw;
                h20.insert(y);
            }
        }
    }

    if ((long long) all9.size() != expected[9]) return 14;

    long long tests = 0;
    long long survivors = 0;
    long long active = 0;

    for (auto const& m : h20) {
        uint64_t t = 0;
        auto d = bdata(m, t);
        long long before = tests;
        if (survives(d, t, tests)) ++survivors;
        if (tests > before) ++active;
    }

    if (raw != 966977) return 15;
    if (hraw != 239349) return 16;
    if (h20.size() != 33920) return 17;
    if (active != 534) return 18;
    if (tests != 1070) return 19;
    if (survivors != 0) return 20;

    cout << "PASS: nine-no-root k=5 D=-1 d_root=1 p=2 support closure\n";
    cout << "size9_orbits " << all9.size() << "\n";
    cout << "raw_size9_extensions " << raw << "\n";
    cout << "h_le_20_raw_extensions " << hraw << "\n";
    cout << "h_le_20_size9_orbits " << h20.size() << "\n";
    cout << "supports_with_empty_candidate " << active << "\n";
    cout << "relaxed_empty_tests " << tests << "\n";
    cout << "relaxed_survivors " << survivors << "\n";
}
