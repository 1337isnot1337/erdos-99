> Generated reading edition · [exact source](../../research/target_c_structural_omnibus_hostile_audit_2026-09-12.md) · source SHA-256 `fc8f103e34961a9b40e5b81d89850852f66ffa0f8763dc9c85bd9bb4def4ed40`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "0d9bdd33ac604f48122b5494eca647fd1b3af96b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_structural_omnibus_hostile_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "49f4574a3a2dc1be0ed5194f60e7f2288654b73ba4383939ca2e9478a37386cc"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Target C structural C-II omnibus

**Date:** 2026-09-12  
**Reviewed branch:** `research/cii-closure-sol-20260912-0953`  
**Disposition:** **PASS after the two binding repair notes already on the branch.**  
**Theorem authority:** unchanged; canonical state remains audit.46.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit covers the theorem-level content that remains unique on the omnibus branch:

1. the all-defect stopped-train / phase gap;
2. the resulting bounded-degree defect-face transport network;
3. the corrected interval-neighborhood biclique theorem;
4. direct ordered-grid extraction from one full phase-label pair; and
5. the Type-II phase/perimeter diameter-edge-density floor.

It also records two real defects already repaired on the branch:

- the original stopped-train path proof oriented opposite-edge links independently and did not justify a consistent orientation of an undirected auxiliary component;
- the original exact interval-biclique statement omitted the necessary existence condition `k<=b` for a consecutive `k`-block on the ordered shore.

The corresponding repair notes are binding parts of the audited theorem record.

## 1. All-defect finite stopped-train ledger

Let `Xi` have one vertex per positive contact edge and two opposite-edge links for every strict-rhombus face. A component has one fixed projective contact direction `u`.

The orientation repair is correct. Put

```math
h(e)=Ju\cdot m(e)
```

for the midpoint of a contact edge. Every rhombus link joins different `h` values. At a degree-two train edge, the two incident rhombi occupy opposite local sides of the physical contact edge, so one opposite side has larger `h` and the other smaller `h`. Thus one auxiliary link enters and one leaves. A cyclic component would become a consistently directed cycle on which `h` strictly increases, impossible.

Hence every auxiliary component is a path, including singleton paths, and

```math
\boxed{T=e-2R.}
```

Occurrence-counted face incidence gives

```math
2e=4R+b+4f+Q,
```

so

```math
\boxed{T={b+Q\over2}+2f.}
```

Canonical core-only ZR/ZF gives

```math
b+Q=2(h-s_Z),
```

and with `d_H=q-h`, `k=d_H+s_Z`,

```math
\boxed{T-q=2f-k.}
```

The train-crossing graph is simple: each train is monotone in its normal coordinate, and two crossing train tangent cones have disjoint slope intervals in a common bisector coordinate. It is triangle-free because three projective directions on a circle of circumference `pi` cannot have all pairwise separations strictly greater than `pi/3`.

**Verdict:** PASS after the orientation repair.

## 2. Phase-atomic lower bound

Type II gives

```math
R/D^2\to\Delta_2={\pi\over2\sqrt3},
```

while total strict-rhombus area excess is `o(D^2)`. Since the crossing graph is simple, normalized crossing mass is dominated by the product of the empirical train-phase measure with itself. Almost every quadratic-scale crossing must have projective phase separation tending `pi/3`; the product measure charges the exact `+-pi/3` relation only through atoms. Weighted Mantel on finitely many heavy atoms therefore gives

```math
2\sqrt{\Delta_2}\le xs,
```

where `x=T/D` and `s` is the limiting atomic phase mass.

The exposed-hull argument remains valid with exceptional faces and singleton trains. After truncating outer loaded-to-loaded walks to fixed length `M`, a walk using only small neighborhoods of finitely many atomic train directions has displacement in a finite family of small angular neighborhoods. Near-disk perimeter-measure convergence makes the number of such hull intervals `O_M(delta D)+o(D)`. Every remaining short interval uses an outer occurrence from a non-atomic train; one complete train has at most two outer occurrences. Sending limits in the stated order yields

```math
{q\over T}\le2(1-s).
```

Combining the two inequalities and `q/D<=pi` gives

```math
\boxed{
\liminf {T-q\over D}
\ge2\sqrt{\Delta_2}-{\pi\over2}
=\gamma=0.333829286933018\ldots .
}
```

Since `T-q=2f-k`,

```math
\boxed{
\liminf {2f-k\over D}\ge\gamma.
}
```

No train-angle flex theorem, coefficient floor, or full-source ZR/ZF extension enters this proof.

**Verdict:** PASS.

## 3. Linear bounded-degree defect-face network

Canonical Section 63 gives

```math
q-x_B=Q+2k,
\qquad x_B\ge0,
```

and loaded hull unit separation gives `q<=per(F)<=pi D`. Hence

```math
Q\le\pi D-2k.
```

If `f_{>K}` counts bounded nonquadrilateral faces of degree at least `K+1`, then each contributes at least `K-3` to `Q`, so

```math
f_{>K}\le {Q\over K-3}.
```

Together with the all-defect lower bound this yields

```math
\boxed{
\liminf {f_{\le K}\over D}
\ge {\gamma\over2}-{\pi\over K-3}.
}
```

For `K=22` the right side is positive. The arithmetic and quantifier order are correct.

The endpoint multigraph is also exact: vertices are the outer face and bounded nonquadrilateral faces; stopped trains are edges, with singleton face-side occurrences treated separately. Face degrees equal multigraph degrees occurrence-by-occurrence.

The singleton bounded-face loop exclusion is valid. A bridge with the same bounded face on both sides can be crossed once by a small transverse segment and closed inside that face. The resulting Jordan cut lies in the force hull and its bounded shore contains no loaded extreme vertex, hence no crossing diameter reaction. Summed positive KKT equilibrium would then require the one positive contact force across the bridge cut to vanish, impossible.

Thus bounded vertices of the train endpoint multigraph are loop-free.

**Verdict:** PASS.

## 4. Corrected interval-neighborhood biclique theorem

The original exact statement was false without `k<=b`; the branch repair gives the necessary correction.

Let `|A|=a`, `|B|=b`, order `B`, and assume every `A`-row neighborhood is an interval. For

```math
1\le k\le b,
```

if

```math
\boxed{e+a\ge k(a+b-k+1),}
```

then a consecutive `k`-block of `B` lies in at least `k` row neighborhoods and therefore spans a `K_{k,k}`.

Indeed the row/block incidence count obeys

```math
I_k\ge e-a(k-1)\ge k(b-k+1),
```

strictly above `(k-1)(b-k+1)` because `b-k+1>=1`.

For

```math
k_0=\left\lfloor{e\over a+b}\right\rfloor,
```

the missing size condition is automatic whenever `k_0>=1`, since

```math
k_0\le {ab\over a+b}<\min(a,b).
```

Thus the linear-density biclique corollary used downstream survives unchanged.

**Verdict:** original finite statement REJECTED as written; repaired statement and all actual Section-91 applications PASS.

## 5. Direct phase-pair ordered grid

After the canonical phase-circle cut, fix one pair of distinct phase labels and orient both shores canonically. The reduced phases lie in one open interval of width `L=pi/3`; the two canonical centerline displacement cones together have angular width

```math
(x_+-x_-)+2L<3L=\pi.
```

Therefore one linear coordinate is strictly monotone along every selected train. Same-label trains do not cross, while every cross-label rhombus crossing has one common sign.

The endpoint-balanced slab argument is valid. With `N<=C_0D` total selected trains and `M` slabs, the total number of crossings for which both trains have an endpoint in their crossing slab is at most

```math
{N^2\over M}+N.
```

Choosing fixed `M` above the stated threshold leaves quadratic many nonbad crossings. Each nonbad crossing has at least one spanning train; a pigeonhole choice yields one slab with a pairwise-disjoint spanning shore and quadratic many incident crossings. Monotonicity and common crossing sign give interval neighborhoods. The corrected interval theorem then yields a balanced linear-size complete grid.

The branch correctly does not claim this grid closes C-II; the oblique-lattice regression has the same qualitative ordered-grid geometry.

**Verdict:** PASS.

## 6. Type-II phase/perimeter diameter-edge density

The all-defect theorem gives the stronger pre-elimination form

```math
\liminf {T-q/2\over D}\ge2\sqrt{\Delta_2}.
```

Using

```math
T=q+2f-k,
\qquad q=h+d_H,
\qquad k=d_H+s_Z,
```

one obtains

```math
\liminf {f\over D}
\ge\sqrt{\Delta_2}-{y\over4}+{d\over4}+{s\over2}
```

along a normalized subsequence with `h/D->y`, `d_H/D->d`, `s_Z/D->s`.

The exact outer-walk ledger is

```math
b=2h-Q-2s_Z.
```

Type-II near-disk convergence gives `per(F)/D->pi`, while always `per(F)<=b`, so

```math
\limsup {Q\over D}+2s\le2y-\pi.
```

Since `Q>=f`, combination yields

```math
{9y\over4}
\ge\pi+\sqrt{\Delta_2}+{d\over4}+{5s\over2},
```

and hence

```math
\boxed{
\liminf {1\over D}
\left(h-{d_H\over9}-{10s_Z\over9}\right)
\ge {4\over9}\left(\pi+\sqrt{\frac\pi{2\sqrt3}}\right).
}
```

In particular

```math
\boxed{
\liminf h/D\ge1.8195135379794445\ldots .
}
```

The inequality directions and retained defect coefficients are correct.

**Verdict:** PASS.

## 7. Regressions and non-implications

The even-hole, oblique-lattice, and protected-contact-creation regressions are useful negative tests and are consistent with the proved theorems. They correctly block stronger claims such as:

- every bounded defect face contributing positive phase transport;
- ordered-grid geometry alone forcing global minimality contradiction; or
- first-contact activation of isolates automatically producing positive KKT force.

None should be promoted as a positive theorem beyond its stated counterexample role.

## 8. Final disposition

The omnibus contains several valid results that remain unique and should eventually be normalized into the post-123 theorem chain. Two repairs are binding:

1. use the corrected stopped-train orientation proof; and
2. use the corrected interval-biclique statement with `1<=k<=b`.

The branch is not stale. It should not be closed until these unique structural results have been integrated elsewhere.

**Overall:** PASS after repairs; theorem-state remains audit.46; C-II remains open.
