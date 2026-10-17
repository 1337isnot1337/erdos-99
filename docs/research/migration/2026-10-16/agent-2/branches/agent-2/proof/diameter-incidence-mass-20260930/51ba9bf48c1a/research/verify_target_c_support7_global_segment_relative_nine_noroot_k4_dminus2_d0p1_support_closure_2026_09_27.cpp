#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <functional>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

// Exact support-level certificate for the nine-no-root
// k=4, D=-2, d_root=0, p=1 branch.
//
// The search is deliberately a relaxation.  It forgets cycle orientations and
// does not require the nominal local block spaces to glue to an actual rank-five
// coefficient code.  It keeps only necessary generalized-weight, generation,
// complete-row-independence, and face-local-capacity conditions.  Therefore
// zero survivors exclude every actual state in the branch.

static constexpr int MOD = 2147483647;  // 2^31-1

struct Multiset {
    array<unsigned char, 9> a{};
    unsigned char n = 0;
    bool operator==(Multiset const& o) const { return n == o.n && a == o.a; }
};

struct MultisetHash {
    size_t operator()(Multiset const& x) const {
        size_t h = x.n;
        for (int i = 0; i < x.n; ++i) h = h * 37 + x.a[i] + 1;
        return h;
    }
};

vector<array<int, 4>> SUPPORTS;
int SUPPORT_INDEX[128];
vector<array<int, 3>> TRIANGLES;
int TRIANGLE_INDEX[128];
vector<array<int, 2>> EDGES;
int EDGE_INDEX[128];
uint64_t SUPPORT_TRIANGLE_MASK[35];
array<array<int, 21>, 35> TRIANGLE_ROWS;
unordered_map<uint64_t, int> TRIANGLE_RANK_CACHE;

int rank_mod(vector<vector<int>> A) {
    if (A.empty()) return 0;
    const int m = (int)A.size();
    const int n = (int)A[0].size();
    int r = 0;
    for (auto& row : A) {
        for (int& x : row) {
            x %= MOD;
            if (x < 0) x += MOD;
        }
    }
    for (int c = 0; c < n && r < m; ++c) {
        int p = -1;
        for (int i = r; i < m; ++i) {
            if (A[i][c]) {
                p = i;
                break;
            }
        }
        if (p < 0) continue;
        swap(A[r], A[p]);

        long long inv = 1;
        long long base = A[r][c];
        long long exp = MOD - 2;
        while (exp) {
            if (exp & 1) inv = inv * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        for (int j = c; j < n; ++j) A[r][j] = (long long)A[r][j] * inv % MOD;

        for (int i = 0; i < m; ++i) {
            if (i == r || !A[i][c]) continue;
            const int q = A[i][c];
            for (int j = c; j < n; ++j) {
                A[i][j] = (A[i][j] - (long long)q * A[r][j]) % MOD;
                if (A[i][j] < 0) A[i][j] += MOD;
            }
        }
        ++r;
    }
    return r;
}

int triangle_rank(uint64_t mask) {
    auto it = TRIANGLE_RANK_CACHE.find(mask);
    if (it != TRIANGLE_RANK_CACHE.end()) return it->second;
    vector<vector<int>> A;
    for (int b = 0; b < 35; ++b) {
        if (mask >> b & 1ULL) A.emplace_back(TRIANGLE_ROWS[b].begin(), TRIANGLE_ROWS[b].end());
    }
    const int r = rank_mod(move(A));
    TRIANGLE_RANK_CACHE.emplace(mask, r);
    return r;
}

Multiset canonical(const Multiset& x) {
    int degree[7] = {};
    for (int i = 0; i < x.n; ++i) {
        for (int v : SUPPORTS[x.a[i]]) ++degree[v];
    }

    vector<int> values(degree, degree + 7);
    sort(values.begin(), values.end(), greater<int>());
    values.erase(unique(values.begin(), values.end()), values.end());

    vector<vector<int>> groups;
    for (int d : values) {
        vector<int> g;
        for (int v = 0; v < 7; ++v) if (degree[v] == d) g.push_back(v);
        groups.push_back(move(g));
    }

    Multiset best;
    best.n = x.n;
    bool initialized = false;
    int relabel[7];

    function<void(int, int)> rec = [&](int gi, int offset) {
        if (gi == (int)groups.size()) {
            Multiset image;
            image.n = x.n;
            for (int i = 0; i < x.n; ++i) {
                int bits = 0;
                for (int v : SUPPORTS[x.a[i]]) bits |= 1 << relabel[v];
                image.a[i] = SUPPORT_INDEX[bits];
            }
            sort(image.a.begin(), image.a.begin() + image.n);
            if (!initialized || lexicographical_compare(
                    image.a.begin(), image.a.begin() + image.n,
                    best.a.begin(), best.a.begin() + best.n)) {
                best = image;
                initialized = true;
            }
            return;
        }

        auto g = groups[gi];
        sort(g.begin(), g.end());
        do {
            for (int j = 0; j < (int)g.size(); ++j) relabel[g[j]] = offset + j;
            rec(gi + 1, offset + (int)g.size());
        } while (next_permutation(g.begin(), g.end()));
    };

    rec(0, 0);
    return best;
}

// Independent Burnside count for support multisets of size <=9 with
// multiplicity <=3 under S_7.
vector<long long> burnside_counts() {
    vector<long long> fixed(10, 0);
    array<int, 7> p = {0, 1, 2, 3, 4, 5, 6};
    do {
        int support_map[35];
        for (int i = 0; i < 35; ++i) {
            int bits = 0;
            for (int v : SUPPORTS[i]) bits |= 1 << p[v];
            support_map[i] = SUPPORT_INDEX[bits];
        }

        bool seen[35] = {};
        vector<int> cycle_lengths;
        for (int i = 0; i < 35; ++i) {
            if (seen[i]) continue;
            int j = i;
            int len = 0;
            while (!seen[j]) {
                seen[j] = true;
                ++len;
                j = support_map[j];
            }
            cycle_lengths.push_back(len);
        }

        long long dp[10] = {};
        dp[0] = 1;
        for (int len : cycle_lengths) {
            long long ndp[10] = {};
            for (int total = 0; total <= 9; ++total) {
                if (!dp[total]) continue;
                for (int mult = 0; mult <= 3; ++mult) {
                    const int next = total + mult * len;
                    if (next <= 9) ndp[next] += dp[total];
                }
            }
            copy(begin(ndp), end(ndp), begin(dp));
        }
        for (int k = 0; k <= 9; ++k) fixed[k] += dp[k];
    } while (next_permutation(p.begin(), p.end()));

    vector<long long> out(10);
    for (int k = 0; k <= 9; ++k) {
        if (fixed[k] % 5040 != 0) {
            cerr << "Burnside divisibility failure at size " << k << "\n";
            exit(2);
        }
        out[k] = fixed[k] / 5040;
    }
    return out;
}

struct BlockData {
    uint16_t occurrence_mask = 0;
    int dimension = 0;
    int incidence = 0;
};

array<BlockData, 35> block_data(const Multiset& ms, uint64_t& touched_mask) {
    int multiplicity[35] = {};
    for (int i = 0; i < ms.n; ++i) ++multiplicity[ms.a[i]];

    array<BlockData, 35> out{};
    touched_mask = 0;
    for (int b = 0; b < 35; ++b) {
        int triangle_bits = 0;
        for (int v : TRIANGLES[b]) triangle_bits |= 1 << v;

        uint16_t occurrence_mask = 0;
        bool repeated_support = false;
        for (int i = 0; i < ms.n; ++i) {
            int support_bits = 0;
            for (int v : SUPPORTS[ms.a[i]]) support_bits |= 1 << v;
            if ((support_bits & triangle_bits) != triangle_bits) continue;
            occurrence_mask |= uint16_t(1u << i);
            if (multiplicity[ms.a[i]] >= 2) repeated_support = true;
        }

        const int incidence = popcount((unsigned)occurrence_mask);
        if (!incidence) continue;
        touched_mask |= 1ULL << b;
        out[b] = {occurrence_mask, repeated_support ? 2 : 1, incidence};
    }
    return out;
}

bool empty_individually_eligible(const BlockData& x) {
    // (d1,d2) >= (3,4).
    return x.incidence >= (x.dimension == 2 ? 4 : 3);
}

bool pair_compatible(const BlockData& x, const BlockData& y) {
    const int inter = popcount((unsigned)(x.occurrence_mask & y.occurrence_mask));
    const int uni = x.incidence + y.incidence - inter;

    // Necessary consequences of (d1,d2,d3,d4) >= (3,4,6,7), split by
    // possible intersection dimension of the two local subspaces.
    if (x.dimension == 1 && y.dimension == 1) return inter >= 3 || uni >= 4;
    if (x.dimension != y.dimension) return inter >= 3 || uni >= 6;
    return inter >= 4 || (inter >= 3 && uni >= 6) || uni >= 7;
}

int occurrence_union_size(uint64_t block_mask, const array<BlockData, 35>& data) {
    uint16_t occurrence_union = 0;
    for (int b = 0; b < 35; ++b) {
        if (block_mask >> b & 1ULL) occurrence_union |= data[b].occurrence_mask;
    }
    return popcount((unsigned)occurrence_union);
}

bool structural_ok(uint64_t touched_mask, uint64_t incomplete_mask) {
    const uint64_t complete_mask = touched_mask & ~incomplete_mask;
    const int rank_complete = triangle_rank(complete_mask);

    // d_root=0: every touched complete-row subset is independent.
    if (rank_complete != popcount(complete_mask)) return false;

    // k=4: all four independent external relation lifts lie in H(T) and remain
    // independent modulo the complete-root span.
    return triangle_rank(touched_mask) - rank_complete >= 4;
}

bool singleton_profile_survives(
    const array<BlockData, 35>& data,
    uint64_t touched_mask,
    long long& clique_tests) {

    const int h = popcount(touched_mask);
    vector<int> eligible;
    for (int b = 0; b < 35; ++b) {
        if ((touched_mask >> b & 1ULL) && empty_individually_eligible(data[b])) eligible.push_back(b);
    }

    uint64_t adjacent[35] = {};
    for (int i = 0; i < (int)eligible.size(); ++i) {
        for (int j = i + 1; j < (int)eligible.size(); ++j) {
            const int a = eligible[i];
            const int b = eligible[j];
            if (!pair_compatible(data[a], data[b])) continue;
            adjacent[a] |= 1ULL << b;
            adjacent[b] |= 1ULL << a;
        }
    }

    vector<int> chosen;

    auto test = [&](uint64_t empty_mask, int nominal_dimension) -> bool {
        // Selected singleton untouched. Then all touched incomplete blocks are
        // actual-empty. Since complete rows have rank at most 11 here, e>=h-11.
        if ((int)chosen.size() >= h - 11 &&
            nominal_dimension >= 5 &&
            occurrence_union_size(empty_mask, data) == 9 &&
            structural_ok(touched_mask, empty_mask)) {
            return true;
        }

        // Selected singleton touched. Then e>=h-12. Its local constraint is
        // allowed to vanish; if nonzero, it is relaxed to an arbitrary line
        // supported inside its incidence set.
        if ((int)chosen.size() < h - 12) return false;
        const uint64_t remaining = touched_mask & ~empty_mask;
        for (int s = 0; s < 35; ++s) {
            if (!(remaining >> s & 1ULL)) continue;
            const uint64_t incomplete_mask = empty_mask | (1ULL << s);

            bool generators_can_span = false;

            // Vanishing selected singleton line.
            if (nominal_dimension >= 5 && occurrence_union_size(empty_mask, data) == 9) {
                generators_can_span = true;
            }

            // Nonzero selected singleton line.
            if (!generators_can_span && data[s].incidence >= 3 && nominal_dimension + 1 >= 5) {
                BlockData singleton_line = data[s];
                singleton_line.dimension = 1;
                bool compatible = true;
                for (int b : chosen) {
                    if (!pair_compatible(data[b], singleton_line)) {
                        compatible = false;
                        break;
                    }
                }
                if (compatible && occurrence_union_size(incomplete_mask, data) == 9) {
                    generators_can_span = true;
                }
            }

            if (generators_can_span && structural_ok(touched_mask, incomplete_mask)) return true;
        }
        return false;
    };

    function<bool(uint64_t, int)> rec = [&](uint64_t candidates, int nominal_dimension) -> bool {
        const int minimum_empty = max(0, h - 12);
        if ((int)chosen.size() + popcount(candidates) < minimum_empty) return false;

        int maximum_nominal_dimension = nominal_dimension;
        for (int b = 0; b < 35; ++b) {
            if (candidates >> b & 1ULL) maximum_nominal_dimension += data[b].dimension;
        }
        // The selected singleton can add at most one dimension.
        if (maximum_nominal_dimension < 4) return false;

        if ((int)chosen.size() >= minimum_empty) {
            ++clique_tests;
            uint64_t empty_mask = 0;
            for (int b : chosen) empty_mask |= 1ULL << b;
            if (test(empty_mask, nominal_dimension)) return true;
        }

        while (candidates) {
            const int b = countr_zero(candidates);
            candidates &= candidates - 1;
            const uint64_t next = candidates & adjacent[b];
            chosen.push_back(b);
            if (rec(next, nominal_dimension + data[b].dimension)) return true;
            chosen.pop_back();
        }
        return false;
    };

    uint64_t initial = 0;
    for (int b : eligible) initial |= 1ULL << b;
    return rec(initial, 0);
}

void initialize_geometry() {
    fill(begin(SUPPORT_INDEX), end(SUPPORT_INDEX), -1);
    fill(begin(TRIANGLE_INDEX), end(TRIANGLE_INDEX), -1);
    fill(begin(EDGE_INDEX), end(EDGE_INDEX), -1);

    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b)
            for (int c = b + 1; c < 7; ++c)
                for (int d = c + 1; d < 7; ++d) {
                    const int bits = (1 << a) | (1 << b) | (1 << c) | (1 << d);
                    SUPPORT_INDEX[bits] = (int)SUPPORTS.size();
                    SUPPORTS.push_back({a, b, c, d});
                }

    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b)
            for (int c = b + 1; c < 7; ++c) {
                const int bits = (1 << a) | (1 << b) | (1 << c);
                TRIANGLE_INDEX[bits] = (int)TRIANGLES.size();
                TRIANGLES.push_back({a, b, c});
            }

    for (int a = 0; a < 7; ++a)
        for (int b = a + 1; b < 7; ++b) {
            EDGE_INDEX[(1 << a) | (1 << b)] = (int)EDGES.size();
            EDGES.push_back({a, b});
        }

    for (int s = 0; s < 35; ++s) {
        uint64_t mask = 0;
        for (int skip = 0; skip < 4; ++skip) {
            int bits = 0;
            for (int j = 0; j < 4; ++j) if (j != skip) bits |= 1 << SUPPORTS[s][j];
            mask |= 1ULL << TRIANGLE_INDEX[bits];
        }
        SUPPORT_TRIANGLE_MASK[s] = mask;
    }

    for (int b = 0; b < 35; ++b) {
        TRIANGLE_ROWS[b].fill(0);
        const int a = TRIANGLES[b][0];
        const int c = TRIANGLES[b][1];
        const int d = TRIANGLES[b][2];
        TRIANGLE_ROWS[b][EDGE_INDEX[(1 << c) | (1 << d)]] = 1;
        TRIANGLE_ROWS[b][EDGE_INDEX[(1 << a) | (1 << d)]] = -1;
        TRIANGLE_ROWS[b][EDGE_INDEX[(1 << a) | (1 << c)]] = 1;
    }
}

bool lucas_lehmer_31() {
    long long s = 4;
    for (int i = 0; i < 29; ++i) s = (s * s - 2) % MOD;
    return s == 0;
}

int main() {
    initialize_geometry();

    if (!lucas_lehmer_31()) return 10;
    // Every triangle row has squared Euclidean norm 3 and relevant rank <=15.
    // Hadamard gives |det|^2 <= 3^15. Since MOD^2 > 3^15, a nonzero rational
    // minor cannot vanish modulo MOD. All modular triangle ranks are exact over Q.
    if ((long long)MOD * MOD <= 14348907LL) return 11;  // 3^15

    const vector<long long> expected = {1, 1, 4, 14, 61, 268, 1283, 6032, 27763, 121458};
    const vector<long long> burnside = burnside_counts();
    if (burnside != expected) {
        cerr << "Burnside orbit count mismatch\n";
        return 12;
    }

    // Canonical augmentation through size eight, checked against Burnside.
    unordered_set<Multiset, MultisetHash> reps;
    Multiset empty;
    reps.insert(empty);
    for (int size = 1; size <= 8; ++size) {
        unordered_set<Multiset, MultisetHash> next;
        next.reserve(reps.size() * 8);
        for (const auto& ms : reps) {
            int multiplicity[35] = {};
            for (int i = 0; i < ms.n; ++i) ++multiplicity[ms.a[i]];
            for (int s = 0; s < 35; ++s) {
                if (multiplicity[s] >= 3) continue;
                Multiset x = ms;
                x.a[x.n++] = s;
                sort(x.a.begin(), x.a.begin() + x.n);
                next.insert(canonical(x));
            }
        }
        reps.swap(next);
        if ((long long)reps.size() != expected[size]) {
            cerr << "canonical augmentation mismatch at size " << size << "\n";
            return 13;
        }
    }

    // Every size-nine orbit has a representative obtained by adding one support
    // to some size-eight orbit representative. Canonicalize those extensions.
    unordered_set<Multiset, MultisetHash> all_nine;
    unordered_set<Multiset, MultisetHash> h20_nine;
    all_nine.reserve(130000);
    h20_nine.reserve(40000);

    long long raw_extensions = 0;
    long long h20_raw_extensions = 0;
    for (const auto& ms : reps) {
        int multiplicity[35] = {};
        uint64_t touched = 0;
        for (int i = 0; i < ms.n; ++i) {
            ++multiplicity[ms.a[i]];
            touched |= SUPPORT_TRIANGLE_MASK[ms.a[i]];
        }

        for (int s = 0; s < 35; ++s) {
            if (multiplicity[s] >= 3) continue;
            ++raw_extensions;
            Multiset x = ms;
            x.a[x.n++] = s;
            sort(x.a.begin(), x.a.begin() + x.n);
            Multiset cx = canonical(x);
            all_nine.insert(cx);
            if (popcount(touched | SUPPORT_TRIANGLE_MASK[s]) <= 20) {
                ++h20_raw_extensions;
                h20_nine.insert(cx);
            }
        }
    }

    if ((long long)all_nine.size() != expected[9]) return 14;
    if (h20_nine.size() != 33920) return 15;

    long long clique_tests = 0;
    long long survivors = 0;
    for (const auto& ms : h20_nine) {
        uint64_t touched_mask = 0;
        const auto data = block_data(ms, touched_mask);
        if (singleton_profile_survives(data, touched_mask, clique_tests)) ++survivors;
    }

    if (survivors != 0) return 16;

    cout << "PASS: nine-no-root k=4 D=-2 d_root=0 p=1 support closure\n";
    cout << "orbit_counts_size_0_through_9";
    for (auto x : expected) cout << ' ' << x;
    cout << '\n';
    cout << "size8_orbits " << reps.size() << '\n';
    cout << "size9_orbits " << all_nine.size() << '\n';
    cout << "raw_size9_extensions " << raw_extensions << '\n';
    cout << "h_le_20_raw_extensions " << h20_raw_extensions << '\n';
    cout << "h_le_20_size9_orbits " << h20_nine.size() << '\n';
    cout << "compatible_empty_cliques_tested " << clique_tests << '\n';
    cout << "support_level_survivors " << survivors << '\n';
    cout << "hadamard_exact_rank_bound " << ((long long)MOD * MOD > 14348907LL) << '\n';
    return 0;
}
