#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <functional>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

#include "k5_d0p4_geom.hpp"

using namespace std;

struct BlockData {
    uint16_t occurrence_mask = 0;
    int incidence = 0;
    bool repeated_containing_support = false;
};

static array<BlockData,35> block_data(const Multiset& ms, uint64_t& touched) {
    int mult[35] = {};
    for (int i = 0; i < ms.n; ++i) ++mult[ms.a[i]];

    array<BlockData,35> out{};
    touched = 0;
    for (int b = 0; b < 35; ++b) {
        int tb = 0;
        for (int v : TRIANGLES[b]) tb |= 1 << v;
        uint16_t occ = 0;
        bool repeated = false;
        for (int i = 0; i < ms.n; ++i) {
            int sb = 0;
            for (int v : SUPPORTS[ms.a[i]]) sb |= 1 << v;
            if ((sb & tb) != tb) continue;
            occ |= uint16_t(1u << i);
            if (mult[ms.a[i]] >= 2) repeated = true;
        }
        const int inc = popcount((unsigned)occ);
        if (!inc) continue;
        touched |= 1ULL << b;
        out[b] = {occ, inc, repeated};
    }
    return out;
}

// Safe local-rank relaxation for generalized weights >= (3,4,6,7).
static vector<int> allowed_empty_dimensions(const BlockData& x) {
    vector<int> dims;
    if (x.repeated_containing_support) {
        if (x.incidence >= 4) dims.push_back(2);
        return dims;
    }
    if (x.incidence >= 3) dims.push_back(1);
    if (x.incidence >= 4) dims.push_back(2);
    return dims;
}

static bool pair_compatible(const BlockData& x, int dx,
                            const BlockData& y, int dy) {
    const int inter = popcount((unsigned)(x.occurrence_mask & y.occurrence_mask));
    const int uni = x.incidence + y.incidence - inter;
    if (dx == 1 && dy == 1) return inter >= 3 || uni >= 4;
    if (dx != dy) return inter >= 3 || uni >= 6;
    return inter >= 4 || (inter >= 3 && uni >= 6) || uni >= 7;
}

// R = T \ E contains all complete blocks plus at most five selected
// nonempty incomplete blocks.  Since d_root=0, C is independent.  Thus an
// actual state requires some independent C subset R satisfying |R\C|<=5 and
// rank H(T)-|C|>=5.  The inequality below is only a necessary condition.
static bool structural_relaxation(uint64_t touched, uint64_t empty) {
    const int h = popcount(touched);
    const int e = popcount(empty);
    const int r_size = h - e;
    const int rank_t = trank(touched);
    const int rank_r = trank(touched & ~empty);
    const int lo = max(0, r_size - 5);
    const int hi = min({r_size, rank_r, rank_t - 5});
    return lo <= hi;
}

static bool support_survives(const array<BlockData,35>& data,
                             uint64_t touched,
                             long long& tests) {
    const int h = popcount(touched);
    const int need = max(0, h - 15);

    vector<int> eligible;
    for (int b = 0; b < 35; ++b) {
        if ((touched >> b & 1ULL) && !allowed_empty_dimensions(data[b]).empty())
            eligible.push_back(b);
    }

    vector<pair<int,int>> chosen;
    function<bool(int)> rec = [&](int at) -> bool {
        if ((int)chosen.size() + (int)eligible.size() - at < need) return false;

        if ((int)chosen.size() >= need) {
            ++tests;
            uint64_t empty = 0;
            for (auto [b, dim] : chosen) empty |= 1ULL << b;
            if (structural_relaxation(touched, empty)) return true;
        }

        for (int j = at; j < (int)eligible.size(); ++j) {
            const int b = eligible[j];
            for (int dim : allowed_empty_dimensions(data[b])) {
                bool ok = true;
                for (auto [c, cdim] : chosen) {
                    if (!pair_compatible(data[b], dim, data[c], cdim)) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) continue;
                chosen.push_back({b, dim});
                if (rec(j + 1)) return true;
                chosen.pop_back();
            }
        }
        return false;
    };

    return rec(0);
}

static string support_key(const Multiset& ms) {
    string s;
    for (int i = 0; i < ms.n; ++i) {
        s.push_back('[');
        for (int v : SUPPORTS[ms.a[i]]) s.push_back(char('0' + v));
        s.push_back(']');
    }
    return s;
}

int main() {
    init_geom();
    if (!ll31()) return 10;
    if ((long long)MOD * MOD <= 14348907LL) return 11;

    const vector<long long> expected_orbits =
        {1,1,4,14,61,268,1283,6032,27763,121458};
    if (burn() != expected_orbits) return 12;

    unordered_set<Multiset,H> level;
    Multiset zero;
    level.insert(zero);
    for (int n = 1; n <= 8; ++n) {
        unordered_set<Multiset,H> next;
        next.reserve(level.size() * 8);
        for (const auto& ms : level) {
            int mult[35] = {};
            for (int i = 0; i < ms.n; ++i) ++mult[ms.a[i]];
            for (int support = 0; support < 35; ++support) {
                if (mult[support] >= 3) continue;
                Multiset x = ms;
                x.a[x.n++] = support;
                sort(x.a.begin(), x.a.begin() + x.n);
                next.insert(canonical(x));
            }
        }
        level.swap(next);
        if ((long long)level.size() != expected_orbits[n]) return 13;
    }

    unordered_set<Multiset,H> all9, h22;
    all9.reserve(130000);
    h22.reserve(90000);
    long long raw_extensions = 0;
    long long h22_raw_extensions = 0;

    for (const auto& ms : level) {
        int mult[35] = {};
        uint64_t touched = 0;
        for (int i = 0; i < ms.n; ++i) {
            ++mult[ms.a[i]];
            touched |= STM[ms.a[i]];
        }
        for (int support = 0; support < 35; ++support) {
            if (mult[support] >= 3) continue;
            ++raw_extensions;
            Multiset x = ms;
            x.a[x.n++] = support;
            sort(x.a.begin(), x.a.begin() + x.n);
            x = canonical(x);
            all9.insert(x);
            if (popcount(touched | STM[support]) <= 22) {
                ++h22_raw_extensions;
                h22.insert(x);
            }
        }
    }
    if ((long long)all9.size() != expected_orbits[9]) return 14;

    long long tests = 0;
    long long active = 0;
    vector<string> survivors;
    for (const auto& ms : h22) {
        uint64_t touched = 0;
        auto data = block_data(ms, touched);
        const long long before = tests;
        if (support_survives(data, touched, tests)) survivors.push_back(support_key(ms));
        if (tests > before) ++active;
    }
    sort(survivors.begin(), survivors.end());

    const vector<string> expected_survivors = {
        "[0123][0123][0123][0124][0124][0124][0134][0134][0134]",
        "[0123][0123][0123][0124][0124][0124][0134][0134][0234]",
        "[0123][0123][0123][0124][0124][0124][0134][0134][0235]",
        "[0123][0123][0123][0124][0124][0124][0135][0135][0234]",
        "[0123][0123][0123][0124][0124][0134][0134][0234][0234]",
        "[0123][0123][0123][0124][0124][0134][0134][0234][1234]",
        "[0123][0123][0123][0124][0124][0134][0134][0235][0235]",
        "[0123][0123][0124][0124][0124][0135][0135][0135][0145]"
    };

    if (raw_extensions != 966977) return 15;
    if (h22_raw_extensions != 523527) return 16;
    if (h22.size() != 70084) return 17;
    if (active != 4896) return 18;
    if (tests != 17770) return 19;
    if (survivors != expected_survivors) return 20;

    cout << "PASS: nine-no-root k=5 D=-1 d_root=0 p=5 support narrowing\n";
    cout << "size9_orbits " << all9.size() << "\n";
    cout << "raw_size9_extensions " << raw_extensions << "\n";
    cout << "h_le_22_raw_extensions " << h22_raw_extensions << "\n";
    cout << "h_le_22_size9_orbits " << h22.size() << "\n";
    cout << "supports_with_empty_candidate " << active << "\n";
    cout << "relaxed_empty_tests " << tests << "\n";
    cout << "relaxed_survivors " << survivors.size() << "\n";
    for (const string& s : survivors) cout << "survivor " << s << "\n";
    return 0;
}
