> Generated reading edition · [exact source](../../research/target_c_support7_h6_bracketing_profile_sharpness_2026-09-20.md) · source SHA-256 `38a311430d3305b9c6b2eb28f717fa541c41dece813c0dc4c24213b8fe950c4f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c4a82a56fd46c268d5d4e62b7556f08ac948e234", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h6_bracketing_profile_sharpness_2026-09-20.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "91749abe2c2e6b1ffd3632c3dde33b498af2b2e90d565265535a36d5e31d09ba"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C support-seven H6: bracketing-profile census and sharpness

Date: 2026-09-20

Status: exact geometric/combinatorial refinement of `target_c_support7_h6_domination_state_bracketing_width_2026-09-19.md`. The theorem-state authority is unchanged. C-II remains open.

## Result

The fixed-state domination support theorem gave the universal bounds

$$
74\quad\text{(hull-hull binary supports)},
\qquad
82=74+8\quad\text{(all binary supports)},
\qquad
110=28+82\quad\text{(unary plus binary supports)}.
$$

Its proof deliberately enlarged the geometric search space by allowing the six bracketing hull edges for one interior target to vary independently among the four hull edges not incident with the root. This note removes that relaxation far enough to answer two questions exactly.

1. For one generic interior target in a strict convex hexagon, the six rootwise bracketing edges have only **26** possible half-turn profiles, rather than the `4^6=4096` independent edge maps used in the earlier upper-bound proof.
2. That geometric coupling does **not** lower the worst-case support bound. The hull-hull maximum remains exactly **74**, and an explicit rational convex-hexagon geometry with two strict interior targets attains it. The same witness therefore attains the full bracketing-only binary bound **82** and unary-plus-binary bound **110**.

Thus the `82/110` bound is sharp under the geometric information used by the bracketing layer itself. Any further reduction must use additional complete-angle affine constraints, force-pentagon constraints, metric integrability, or another part of the reciprocal system. More elaborate bracketing-only case analysis cannot improve the universal bound.

Certificate:

`research/verify_target_c_support7_h6_bracketing_profile_sharpness_2026_09_20.py`

## 1. The 26 single-target profiles

Let the hull vertices be `0,1,...,5` in counterclockwise order and let `t` be a strict interior point. Assume no line through `t` contains two hull vertices. Around `t`, the six hull rays have the same cyclic order.

For a hull root `r`, extend the ray from `r` through `t` beyond `t`. It exits the convex hexagon through one hull edge. Equivalently, viewed from `t`, the exit direction is antipodal to the ray `t->r`.

Define `k_r` to be the number of successive hull rays

$$
r+1,r+2,\ldots
$$

encountered before that antipodal direction. Strict interiority implies

$$
k_r\in\{1,2,3,4\},
$$

because every line through an interior point has hull vertices in both open half-planes. The exit edge is then

$$
\boxed{\{r+k_r,\ r+k_r+1\}}
\tag{1}
$$

with indices modulo six.

Take another hull vertex `r+d`, where `1<=d<=5`. The clockwise angular arc from `r` to `r+d` and the complementary arc from `r+d` back to `r` sum to `2pi`. Genericity excludes equality with `pi`, so exactly one of the two arcs is shorter than a half-turn. In terms of the `k` variables,

$$
\boxed{
 d\le k_r
 \quad\Longleftrightarrow\quad
 6-d>k_{r+d}.
}
\tag{2}
$$

The verifier exhausts the `4^6=4096` possible integer six-tuples in `{1,2,3,4}^6` and keeps precisely those satisfying (2) for every `r,d`. Exactly

$$
\boxed{26}
$$

profiles remain.

This is a necessary profile theorem; no realization claim is needed for the count. It already shrinks the state-independent single-target bracketing catalogue from 4096 maps to 26 half-turn-consistent maps.

## 2. The 74 maximum survives the profile restriction

For opposite-target hull-root clauses `(r,6)` and `(s,7)` with `r!=s`, choose endpoints `h` and `q` from their two bracketing edges. As proved in the preceding domination-width analysis, the two aligned paths

$$
6\to r\to h,
\qquad
7\to s\to q
$$

can occur in one directed simple-cycle template exactly when the six used vertices are distinct. Since the bracketing edges already avoid their own roots, the remaining conditions are

$$
h\ne s,
\qquad q\ne r,
\qquad h\ne q.
\tag{3}
$$

The previous independent-bracketing relaxation has exact maximum 74. The new verifier independently repeats that finite maximization and then maximizes again after restricting both target maps to the 26 profiles from Section 1. The result is still

$$
\boxed{74}.
$$

So the half-turn coupling is a major catalogue reduction but does not improve the universal numerical bound.

The extremal set is very small. Among the `26^2=676` ordered profile pairs, exactly six attain 74. They form one cyclic-label orbit, generated by

$$
(3,2,1,1,4,4),
\qquad
(1,4,4,3,2,1).
\tag{4}
$$

Every other profile pair has hull-hull support count at most

$$
\boxed{69}.
$$

Therefore any fixed state whose two target profiles are not in the six-pair extremal orbit automatically improves from `82` to at most

$$
69+8=\boxed{77}
$$

binary supports, and from `110` to at most `28+77=\boxed{105}` unary-plus-binary supports. This gives a cheap exact prefilter for the state-specific order-cut generator: test the two six-entry half-turn profiles before consulting any of the 8,242 minimal cycle templates.

## 3. Exact rational geometric witness

The verifier gives the following eight rational points. The first six are the labelled convex hull; the last two are the interior targets `6,7`:

```text
0 = ( 403/200,    1/50 )
1 = (  51/50,    99/50 )
2 = ( -41/40,   199/100)
3 = ( -81/40,    -3/200)
4 = (      -1,  -401/200)
5 = ( 101/100,  -397/200)
6 = (   -7/4,     -1/4 )
7 = (   21/20,    13/20)
```

All checks use `Fraction` arithmetic. The certificate verifies:

- the hull is strictly convex in the listed cyclic order;
- both targets are strictly inside every hull supporting half-plane;
- all `C(8,3)=56` triples are noncollinear;
- all 28 reciprocal segment squared lengths are distinct;
- every root-to-target ray has a unique strict exit through the relative interior of one hull edge.

The two hull-root bracketing maps are

```text
target 6:
0 -> 34
1 -> 34
2 -> 34
3 -> 45
4 -> 23
5 -> 34

target 7:
0 -> 12
1 -> 50
2 -> 01
3 -> 01
4 -> 01
5 -> 01
```

Their half-turn profiles are

$$
(3,2,1,1,4,4),
\qquad
(1,4,4,3,2,1),
$$

both among the 26 exact profiles. Direct evaluation of (3) gives exactly 74 hull-hull binary supports.

For the mutual interior roots, the line `6-7` exits through

$$
E_{6,7}=\{0,1\},
\qquad
E_{7,6}=\{3,4\}.
$$

Each selected endpoint of `E_{6,7}` pairs with the two branch endpoints of the corresponding target-6 hull-root clause, giving four hull-interior supports; the reverse interior-root clause gives another four. Hence the same strict rational geometry attains

$$
\boxed{74+8=82}
$$

binary supports. Adding the fixed 28 unary branch literals gives

$$
\boxed{28+82=110}.
$$

The witness also has 28 distinct segment lengths, so the sharpness is not caused by a segment-length tie.

## 4. Consequence for the closure search

The preceding `82/110` bound cannot be lowered from convex-bracketing geometry alone. The next order-layer reduction must therefore use information absent from this witness calculation, principally exact forced signs among the 168 rooted segment comparisons coming from the 85-variable complete-angle affine cell and its physical branch constraints.

The 26-profile theorem is still useful computationally: any state-independent preindexing by one target's bracketing pattern needs at most 26 profiles rather than 4096 arbitrary maps, and a two-target profile table needs at most `26^2=676` pairs rather than `4^12=16,777,216` independent pairs. Only six of those 676 profile pairs can require the full `82/110` support budget; every other pair has the sharper `77/105` budget. This is an implementation reduction, not an H6-cell exclusion.

The explicit generic-H6 endpoint therefore remains

$$
3874=3076\,C_7+798\,(C_3\sqcup C_4).
$$

The theorem does not assert that the rational eight-point witness satisfies the separate force-pentagon or reciprocal closure equations of an actual support-seven endpoint cell. Its role is narrower and exact: it proves that the current bracketing-only support bound is already sharp under strict convexity, interiority, oriented-matroid genericity, and distinct segment lengths. C-II remains open.
