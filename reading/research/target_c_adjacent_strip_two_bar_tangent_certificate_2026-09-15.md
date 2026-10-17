> Generated reading edition · [exact source](../../research/target_c_adjacent_strip_two_bar_tangent_certificate_2026-09-15.md) · source SHA-256 `4264b7266d5a762663d33e222ff255191493d7019b5c12ffadcd9175b71a9ec1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "dbae472ac6df206d4851eb12ead1a185c114eabc", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_adjacent_strip_two_bar_tangent_certificate_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ebe411e4afb1818092e0a550f3cf9ee8190cdf5e0cb5b4614f11167f2f952365"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — every blocked adjacent-strip opening has a one/two-diameter tangent certificate

**Date:** 2026-09-15  
**Status:** proof-only exact source-level structural theorem  
**Scope:** any adjacent O--O strip in the canonical contact-minimal full-core Type-II source for which the audited strip-translation reduction applies  
**Dependencies:** `target_c_adjacent_strip_opening_reduction_2026-09-15.md`; canonical contact-minimal/global-minimal normalization  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The adjacent-strip opening theorem reduces a finite source replacement to translating one physical layer `R` between two consecutive O--O cuts. Its complete moving diameter set can still contain hundreds or thousands of switching edges. For the **first-order translation obstruction**, almost all of those edges are redundant.

There are always one or two actual switching diameter edges which already certify that no infinitesimal translation ray can open both boundary train families while strictly decreasing every moving diameter bar to first order.

This is an exact two-dimensional Helly reduction. It does **not** say that the switching graph itself has at most two edges, and it does not remove the second-order/inactive-slack issue for a direction lying on a blocker tangent.

---

## Theorem TB — one/two-bar tangent certificate

Use the notation of the adjacent-strip opening theorem. Let `R` be the translated middle layer and let `a,b` be the two unit boundary-contact vectors, each oriented from the fixed side into `R`, so a translation by `v` changes the two boundary contact vectors to

$$
a+v,
\qquad
b+v.
\tag{TB.1}
$$

For every moving actual diameter edge `h=xy`, choose any orientation and write

$$
r_h=p_y-p_x,
\qquad
\delta_h=\mathbf 1_R(y)-\mathbf 1_R(x)\in\{+1,-1\}.
$$

Define its inward signed diameter vector

$$
\boxed{n_h:=\delta_h r_h.}
\tag{TB.2}
$$

Reversing the orientation of `h` changes both `r_h` and `delta_h`, so `n_h` is orientation-independent. Geometrically, `n_h` is the length-`D` vector from the endpoint outside `R` toward the endpoint inside `R`.

Then there exists a set

$$
J\subseteq E(H_{sw}),
\qquad
1\le |J|\le2,
\tag{TB.3}
$$

such that every nonzero vector `w` satisfying

$$
a\cdot w\ge0,
\qquad
b\cdot w\ge0
\tag{TB.4}
$$

also satisfies

$$
\boxed{
\max_{h\in J} n_h\cdot w\ge0.
}
\tag{TB.5}
$$

Equivalently, among all switching diameter bars, one or two already certify the absence of a translation **tangent direction** which opens both boundary train families and strictly shortens every moving diameter bar.

---

## 1. Exact directional criterion for a strip translation

Take a nonzero direction `w` and a scalar `s>0`, and translate the middle layer by

$$
v=sw.
$$

For the two boundary train contacts,

$$
|a+sw|^2
=1+2s(a\cdot w)+s^2|w|^2,
\tag{TB.6}
$$

$$
|b+sw|^2
=1+2s(b\cdot w)+s^2|w|^2.
\tag{TB.7}
$$

Hence if (TB.4) holds, both boundary contact families become **strictly longer than one** for every `s>0`. Equality in one of the linear terms causes no problem because the positive quadratic term opens that contact family.

For a moving old diameter edge, the exact strip formula gives

$$
r_h(sw)=r_h+\delta_h sw,
$$

so, using `|r_h|=D` and (TB.2),

$$
\boxed{
|r_h(sw)|^2
=D^2+2s(n_h\cdot w)+s^2|w|^2.
}
\tag{TB.8}
$$

Therefore if

$$
n_h\cdot w<0
\tag{TB.9}
$$

for every moving diameter edge, then one can choose `s>0` small enough that every moving old diameter is strictly shorter than `D`.

Because the source is finite, the same sufficiently small `s` preserves every strict old lower-distance slack and every strict old nondiameter upper slack. Every old contact away from the two boundary trains is unchanged exactly, and every nonswitching old diameter is unchanged exactly.

Thus a vector `w` satisfying

$$
a\cdot w\ge0,
\quad
b\cdot w\ge0,
\quad
n_h\cdot w<0\quad\forall h\in E(H_{sw})
\tag{TB.10}
$$

would give a unit-separated same-cardinality source of diameter at most `D` with both boundary train contact families removed. If some nonswitching old diameter remains, this contradicts canonical contact minimality. If none remains, the diameter becomes strictly smaller than `D`, contradicting global minimality.

Consequently a canonical survivor satisfies

$$
\boxed{
\nexists w\ne0:
\ a\cdot w\ge0,
\ b\cdot w\ge0,
\ n_h\cdot w<0\ \forall h\in E(H_{sw}).
}
\tag{TB.11}
$$

In particular `H_sw` is nonempty.

---

## 2. Non-antipodal boundary directions reduce to intervals on one arc

Assume first

$$
b\ne-a.
$$

Normalize directions to the unit circle and put

$$
\Omega
:=\{w\in S^1:\ a\cdot w\ge0,\ b\cdot w\ge0\}.
\tag{TB.12}
$$

The intersection of the two closed half-planes through the origin is one convex cone. Since `b` is not antipodal to `a`, its unit directions form one nonempty closed circular arc of length at most `pi`.

For every moving diameter edge define

$$
I_h
:=\{w\in\Omega:\ n_h\cdot w<0\}.
\tag{TB.13}
$$

The set

$$
\{w:n_h\cdot w<0\}
$$

is an open half-plane through the origin. Its intersection with the opening cone is convex. Therefore `I_h`, viewed in a linear angular parametrization of the arc `Omega`, is an interval, possibly empty and with any combination of open/closed endpoints inherited from `Omega`.

Equation (TB.11) says exactly

$$
\bigcap_{h\in E(H_{sw})} I_h=\varnothing.
\tag{TB.14}
$$

Finite intervals on a line have Helly number two. Hence either

1. some `I_h` is already empty; or
2. there are two edges `h_1,h_2` with
   $$
   I_{h_1}\cap I_{h_2}=\varnothing.
   $$

Take `J={h}` in the first case and `J={h_1,h_2}` in the second. By the definition of the `I_h`, this is precisely (TB.5).

---

## 3. The antipodal case also needs at most two bars

Now suppose

$$
b=-a.
$$

Then (TB.4) forces

$$
a\cdot w=0,
$$

so after normalization

$$
\Omega=\{Ja,-Ja\}.
\tag{TB.15}
$$

Because the total intersection in (TB.14) is empty, at least one moving diameter edge excludes the direction `Ja`, and at least one moving diameter edge excludes `-Ja`. If one edge excludes both, it alone is a certificate. Otherwise the two edges excluding the two opposite directions form a two-bar certificate.

Thus (TB.3)--(TB.5) hold in the antipodal case as well.

---

## 4. Geometric meaning of a minimal certificate

The theorem leaves only two load-bearing tangent types.

### TB1 — one-bar certificate

One actual switching diameter vector `n_h` satisfies

$$
n_h\cdot w\ge0
$$

for every contact-opening tangent direction `w` in the cone (TB.4). Equivalently, in the non-antipodal case its inward normal belongs to the dual opening cone

$$
 n_h\in\operatorname{cone}\{a,b\}.
\tag{TB.16}
$$

A single old diameter bar already blocks every tangent ray that opens both train boundaries.

### TB2 — two-bar certificate

Neither bar alone blocks the entire opening cone, but their two allowable-shortening direction intervals inside `Omega` are disjoint. The two inward diameter vectors bracket the opening cone in angular order.

The two certificate edges are actual edges of the planar diameter thrackle. Therefore, if they are distinct, they either share an endpoint or cross properly.

Combining this with the current adjacent switching-order theorem reduces the translation obstruction to three finite geometric pictures:

```text
one switching diameter bar;

two vertex-disjoint switching diameter bars which cross;

two switching diameter bars sharing one loaded endpoint
(a two-edge star, possibly at the middle-arc transition hub).
```

The full switching caterpillar may contain many other edges, but none are needed to certify the nonexistence of a strictly diameter-decreasing tangent ray in the two-dimensional strip-translation cone.

---

## 5. Why this is stronger than the blocker-count reductions

The existing adjacent-strip line successively bounds the complete moving diameter set by an absolute constant. Those theorems remain useful for finite nonlinear replacement arguments.

The present theorem attacks a different quantity: the **minimal tangent obstruction certificate**. Its size is bounded by two independently of every numerical switch-count estimate.

Thus the live strip-opening normal form becomes

```text
one physical layer between consecutive O-O cuts
+ exact two-dimensional layer translation
+ only the two boundary train contact families move among old contacts
+ all nonswitching old diameter pairs are invariant exactly
+ complete moving diameter set = ordered one-arc caterpillar forest
+ tangent infeasibility certified by one or two actual switching diameter edges.
```

A closing theorem can now attack the TB1/TB2 chord geometry directly rather than classify hundreds of switching rows.

---

## 6. Scope audit and non-conclusions

- This theorem does **not** assert that `H_sw` has at most two edges. It bounds only a minimal first-order obstruction certificate.
- The inequalities in (TB.4)--(TB.5) are tangent-ray statements. A direction with `n_h dot w=0` is blocked at second order by the positive `s^2|w|^2` term in (TB.8), but the theorem does not claim that the selected one/two bars by themselves control every curved or direction-varying finite translation path.
- No KKT multiplier lower bound or KKT support reduction is used.
- No phase-gap estimate is used.
- Contact-isolated source points remain in the source and translate according to their geometric membership in `R`, exactly as in the parent strip-opening theorem.
- The finite-slack step is source-dependent; no uniform inactive-distance margin in `D` is asserted.
- No exact triangle or strict-diameter competitor has yet been obtained.

**Disposition:** proved proof-only exact one/two-bar tangent-certificate reduction for the adjacent-strip opening obstruction. C-II and Level I remain open.
