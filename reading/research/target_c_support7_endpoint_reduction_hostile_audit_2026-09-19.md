> Generated reading edition · [exact source](../../research/target_c_support7_endpoint_reduction_hostile_audit_2026-09-19.md) · source SHA-256 `d3313a939111d606e5c311c1eb385e984fcd38e9ee5c939820db9ce6b525a318`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "13bef8b8cd067e39c870bbe1784465508f2dee7d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_endpoint_reduction_hostile_audit_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "30a8bf8b4ff18bcfa4383d757a0e2f2ccb8d2fe65886c389b127faf15aef7c55"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — degree-pure support-seven endpoint reduction

**Date:** 2026-09-19  
**Audited source:** `research/target_c_support7_endpoint_reduction_2026-09-19.md`  
**Certificate:** `research/verify_target_c_support7_endpoint_reduction_2026_09_19.py`  
**Verdict:** PASS at the stated scope  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

## 1. Scope under audit

The source does not claim to exclude support seven. It claims only:

1. a degree-pure support-seven one-anchor relation graph is four-regular with complement `C7` or `C3+C4`;
2. repeated non-ground dual values are impossible, including total collapse;
3. the reciprocal is therefore nondegenerate on `K8` minus that complement;
4. local hull-angle control excludes `H5` and forces ground `3+4` in `H6`;
5. in the fully convex `H8` branch, exact local sign compatibility reduces to 23 reflection orbits, two `2+5` orbits are killed by signed-length certificates, and one further `3+4` orbit is killed by a direct ground projection, leaving 20 reflection orbits.

No statement is made about degree-excess support-seven components, and no global `1/8` corank coefficient is claimed.

Verdict on scope: correctly limited.

---

## 2. Relation graph classification: PASS

At the degree-pure endpoint every support face is a degree-five one-anchor face. It has exactly four residual internal side occurrences. The audited one-anchor theorem gives relation degree at least four in any nonzero component. Therefore all four internal occurrences are relation edges and the relation degree is exactly four.

The residual endpoint graph is simple, so `R` is a simple four-regular graph on seven vertices. Its complement is simple two-regular. A simple two-regular graph is a disjoint union of cycles of length at least three. The only cycle-size partitions of seven are `7` and `3+4`.

Thus `R=K7-C7` or `R=K7-(C3+C4)`.

No hidden assumption about planarity or train crossings enters this classification.

Verdict: PASS.

---

## 3. Collision propagation: PASS

The source uses a stronger form of the support-six common-neighbor argument.

Suppose two distinct dual-value classes are `A,B`. If one vertex `i in A` had two relation neighbors `j,k in B`, then `y_j=y_k` and `y_i!=y_j`, so

```math
y_i-y_j=y_i-y_k\ne0.
```

Each difference is projectively parallel to its physical relation-train direction at face `i`. Hence two distinct pentagon sides at `i` would be projectively parallel. The audited bounded-pentagon theorem forbids this.

Therefore the relation edges between any two distinct value classes form a matching.

For a proper equal-value class `S` of size `s>=2`, every outside vertex has at most one relation neighbor in `S`, hence at least `s-1` complement neighbors in `S`. Since the complement degree is two:

- `s>=4` is immediately impossible;
- `s=3` requires at least `4*2=8` complement cross edges, but the three vertices of `S` have total complement degree only six;
- `s=2` requires at least five complement cross edges, but the two vertices of `S` have total complement degree only four.

The counting is on cross edges, so there is no double-counting issue: summing from vertices outside `S` counts each `S`--outside edge exactly once.

The independent verifier enumerates all 877 set partitions for one representative of each complement type and confirms that the matching condition permits only the discrete partition and total collapse.

Verdict: PASS.

---

## 4. Total collapse parity: PASS

If all seven `y_i` equal the same nonzero vector, every outside anchor is projectively parallel to that vector. Because relation degree is already exactly four, every residual internal side of every support face is paired with another face inside the component. Summing the seven pentagon closure equations therefore cancels every internal side occurrence.

The remaining seven oriented unit anchor vectors are all `+u` or `-u` for one unit direction `u`. Their sum can vanish only if the number of `+u` and `-u` occurrences is equal. Seven is odd.

This is an exact obstruction. It does not use genericity, reciprocal convexity, or a numerical closure solve.

Verdict: PASS.

---

## 5. Reciprocal nondegeneracy and equilibrium: PASS

The collision argument proves the seven non-ground dual points are pairwise distinct; the one-anchor form already gives `y_i!=0`, so they are also distinct from the ground `y_0=0`.

Every edge of

```math
H=K_8-\overline R
```

therefore has nonzero reciprocal difference. The support-six reciprocal construction applies without a collapsed-edge exception. Each present edge carries a signed unit-force coefficient, the seven non-ground pentagon closures give equilibrium there, and summing those equations gives the ground equilibrium.

The tensor identity and trace

```math
\sum_{e\in E(H)}s_e d_e=0
```

use the same algebra as the already-audited support-five/support-six reciprocal notes.

Verdict: PASS.

---

## 6. Transfer of the local hull theorem: PASS

Every non-ground support-seven reciprocal vertex still has exactly five incident reciprocal edges: one anchor plus four relation edges. At a non-ground hull vertex those five raw rays lie in the open hull cone. No edge is collapsed.

The prior local theorem proving:

- exact `2+3` sign split;
- size-two class at raw positions two and four; and
- reciprocal hull angle `>2pi/3`

uses only this five-ray pentagon geometry, not the support-six missing-matching graph.

Therefore its reuse at support seven is legitimate.

Verdict: PASS.

---

## 7. Hull-size argument: PASS

If the ground is interior, every hull vertex is non-ground and contributes angle greater than `2pi/3`. For hull size `h`,

```math
(h-2)\pi>2h\pi/3
```

forces `h>6`. With only seven non-ground points, the only possibility is `h=7`.

If the ground lies on the hull, `h<=4` is excluded by the same angle sum applied to the other `h-1` vertices. Hence only `H5,H6,H7,H8` remain before the ground resultant argument.

For ground-on-hull size `h`, the ground angle bound

```math
\phi_0<(h-4)\pi/3
```

is exact from the polygon angle sum and strict non-ground bounds.

Verdict: PASS.

---

## 8. Ground resultant bounds: PASS

All seven raw ground rays lie in the closed hull cone of width `phi_0<pi`. This remains true even if an interior reciprocal point is collinear with a hull edge from the ground; distinctness of the ray directions is not needed.

Let the smaller sign class have size `p<=3`. Move it to the other side of the unit-vector equilibrium. Projection of each majority vector onto the hull-cone bisector is at least `cos(phi_0/2)`, so the majority resultant has bisector projection at least

```math
(7-p)\cos(\phi_0/2).
```

The minority resultant has norm at most `p`. Therefore

```math
(7-p)\cos(\phi_0/2)\le p
```

is necessary.

For `H5`, `phi_0<pi/3`. The weakest case is `p=3`, but

```math
4\cos(\pi/6)=2\sqrt3>3.
```

So `H5` is impossible.

For `H6`, `phi_0<2pi/3`. If `p<=2`,

```math
(7-p)\cos(\phi_0/2)\ge5\cos(\phi_0/2)>5/2>2\ge p.
```

Therefore only `p=3` survives, giving ground `3+4`.

Verdict: PASS.

---

## 9. Fully convex raw-ray order: PASS

In the `H8` branch all eight reciprocal points are vertices of one strict convex polygon. Label them cyclically `0,...,7`, with ground `0`.

At non-ground vertex `i`, the rays to the other seven hull vertices appear in cyclic order

```math
i+1,i+2,\ldots,i+7\pmod8.
```

Deleting the two missing complement neighbors leaves the exact five-ray order used by the local sign rule. Reversal of hull orientation does not change positions two and four as an unordered parity class; it only reflects the complete configuration.

There are exactly 360 labelled `C7` edge sets and 105 labelled `C3+C4` edge sets on positions `1,...,7`. The verifier generates them without duplicate starting-point or orientation choices.

Verdict: PASS.

---

## 10. H8 sign census: PASS

For each missing graph the verifier enumerates all `2^7` choices of whether the chosen global sign color is the local size-two or local size-three class. It prescribes the sign of every present reciprocal edge at each non-ground endpoint and rejects a choice if the two endpoint prescriptions disagree.

Every reciprocal edge has at least one non-ground endpoint, so no edge sign is left unspecified.

The exact output is:

```text
labelled H8 local-sign survivors: C7=24, C3+C4=14
reflection orbits: C7=15, C3+C4=8
ground split orbits before metric exclusion: C7 2+5=2, C7 3+4=13, C3+C4 3+4=8
```

Every surviving labelled missing graph has exactly two signings, and the verifier asserts they are global complements.

The quotient used is deliberately only reflection fixing the ground position. It need not be the maximal abstract-graph symmetry quotient; failing to quotient further can only leave duplicate cases, not lose an actual configuration.

Verdict: PASS.

---

## 11. Strict metric residuals: PASS

Every `H8` point is a strict convex-hull vertex, so every triangle on three of the eight points is noncollinear. Thus

```math
d_{ab}<d_{ac}+d_{bc}
```

is strict whenever `a,b,c` are distinct.

For cyclically ordered convex quadrilateral `a,b,c,d`, let `X` be the intersection of diagonals `ac` and `bd`. Then

```math
d_{ab}<d_{aX}+d_{Xb},
\qquad
d_{cd}<d_{cX}+d_{Xd}.
```

Adding gives

```math
d_{ab}+d_{cd}<d_{ac}+d_{bd}.
```

The analogous inequality for the other opposite-side pair is identical after relabeling.

Thus every `T` and `Q` residual used in the source is strictly negative. Missing reciprocal edges may appear as auxiliary distances in the residual identities; this is legitimate because the identities are geometric linear identities in all pairwise distances and the missing-edge coefficients cancel exactly.

Verdict: PASS.

---

## 12. Two `2+5` trace certificates: PASS

The verifier identifies exactly two `C7` reflection orbits with ground `2+5` and fixes canonical representatives `A,B`. For each, it constructs

```math
L=\sum_{P}d_e-\sum_{H\setminus P}d_e.
```

It then checks coefficient-by-coefficient, using integer `Counter` arithmetic, that:

- `6 L_A` is the positive integer combination of 25 strict residuals printed in the source;
- `2 L_B` is the sum of the 14 strict residuals printed in the source.

No floating point or LP solver appears in the committed verifier. The discovery of the identities is irrelevant to their proof; the checked identities are exact.

Hence `L_A<0` and `L_B<0`, while reciprocal trace equilibrium requires `L=0`. Global sign complement changes `L` to `-L` and is equally impossible.

Verdict: PASS.

---

## 13. Ground projection exclusion: PASS

For convex `H8`, the seven raw ground angles satisfy

```math
\theta_1<\cdots<\theta_7<\theta_1+\pi.
```

The source excludes minority pattern `{1,3,7}` by rewriting equilibrium as

```math
0=(u_2-u_1)+(u_4-u_3)+u_5+(u_6-u_7)
```

and dotting with `u_5`.

Every difference term has positive dot product because for `0<a<b<pi`, cosine is strictly decreasing. For example

```math
(u_2-u_1)\cdot u_5
=\cos(\theta_5-\theta_2)-\cos(\theta_5-\theta_1)>0.
```

The other two difference terms satisfy the same ordered-angle condition, and `u_5.u_5=1`.

The reflected pattern `{1,5,7}` is excluded analogously by dotting

```math
0=(u_2-u_1)+u_3+(u_4-u_5)+(u_6-u_7)
```

with `u_3`.

The exact census confirms these two labelled patterns form one reflection orbit among the surviving `C7,3+4` cases.

Verdict: PASS.

---

## 14. Final count and nonclaim: PASS

Starting from 23 reflection orbits:

- remove two `C7,2+5` orbits by signed-length trace certificates;
- remove one `C7,3+4` reflection orbit by the ground projection argument.

This leaves 20 fully convex `H8` reflection orbits, all ground `3+4`.

The source correctly leaves `H6`, `H7`, and those 20 `H8` cases open. It does not infer that support seven is impossible and does not change the global support coefficient from `1/7` to `1/8`.

Verdict: PASS.

---

## 15. Reproducibility

The committed verifier uses only Python standard-library exact integer/set arithmetic. It was run locally under Python 3 and produced:

```text
PASS
labelled H8 local-sign survivors: C7=24, C3+C4=14
reflection orbits: C7=15, C3+C4=8
ground split orbits before metric exclusion: C7 2+5=2, C7 3+4=13, C3+C4 3+4=8
two exact 2+5 signed-length certificates: PASS
ground-projection exclusion removes one further C7 3+4 reflection orbit
remaining fully-convex H8 local-sign/metric orbits: 20
```

`python3 -m py_compile` also succeeds.

Final verdict: **PASS at the stated scope.** Degree-pure support seven is sharply reduced but not excluded. C-II remains open.
