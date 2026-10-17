> Generated reading edition · [exact source](../../../docs/reports/target_c_extreme_loaded_terminal_inheritance_2026-09-10.md) · source SHA-256 `c4411386c8a3c10e5a4ba8c07004fba595775673b0f633b3406b9afb9ee67c23`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-675D8627F67A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — loaded-terminal inheritance for extreme positive circuits

**Date:** 2026-09-10  
**Repository state:** PR #178 after EDB  
**Run type:** exact force-hull support transfer / asymptotic endpoint localization  
**Target:** Target C, C-II after ZF  
**Depends on:** C65 full actual force hull, canonical selected force-hull trapping, CT degeneracy identity, DB/EDB diameter-density bounds  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

Let `B` be the full relative-interior loaded terminal set, i.e. the endpoints of all
actual diameter edges, and let

$$
F=\operatorname{conv}B.
$$

For an extreme normalized KKT stress, let `B_* subseteq B` be its positive diameter
endpoints and let `V_*` be the vertex set of its connected positive contact component.
The selected force-hull theorem gives

$$
V_*\subseteq\operatorname{conv}B_*.
$$

Every point of `B` is an extreme point of the full force hull `F`. Therefore an omitted
loaded terminal cannot remain in the selected positive contact support:

$$
\boxed{B\cap V_*=B_*.}
\tag{LI.1}
$$

Consequently, with

$$
u_*:=v-v_*,
\qquad
q:=|B|,
\qquad
q_*:=|B_*|,
$$

we have the exact support-loss bound

$$
\boxed{u_*\ge q-q_*.}
\tag{LI.2}
$$

CT defines

$$
\kappa_*:=z_*-s_Z=2u_*+\sigma_*.
$$

Hence

$$
\boxed{
\kappa_*\ge2(q-q_*)+\sigma_*.
}
\tag{LI.3}
$$

This upgrades the interpretation of low circuit degeneracy: if
`kappa_*=o(D)`, then the extreme circuit omits only `o(D)` full loaded terminals and
has `sigma_*=o(D)`. EDB then forces at least DB-scale positive diameter support.
Thus every low-degeneracy extreme circuit satisfies

$$
\boxed{
q_*=q-o(D),
\qquad
h_*\ge(2\rho-o(1))D,
\qquad
\sigma_*=o(D),
}
\tag{LI.4}
$$

where `rho=cos rho`.

At the full DB endpoint `h/D->2rho`, the transfer becomes stronger:

$$
\boxed{
h-h_*=o(D),\qquad q-q_*=o(D).}
\tag{LI.5}
$$

Hence a low-degeneracy extreme ray in the minimal full-diameter-density phase contains
all but `o(D)` actual diameter edges and all but `o(D)` loaded terminals. Together
with EDB, its selected force hull also has

$$
Q_*=o(D),
\qquad
\operatorname{per}F_*/D\to4\rho.
\tag{LI.6}
$$

This is the first direct support-transfer statement from the full C65 force hull to one
extreme positive circuit.

---

## 1. Proof of loaded-terminal inheritance

The full C65 relative-interior normalization makes every actual diameter edge positive,
so its endpoint set is exactly `B`. The force-hull theorem gives

$$
F=\operatorname{conv}B
$$

and every member of `B` is a convex-hull vertex.

Fix an extreme selected stress. Its positive contact support is one connected component
on vertex set `V_*`, and the selected force-hull trapping theorem gives

$$
V_*\subseteq\operatorname{conv}B_*.
\tag{1.1}
$$

Certainly `B_* subseteq B cap V_*`. Conversely suppose

$$
b\in(B\cap V_*)\setminus B_*.
$$

Then (1.1) gives

$$
b\in\operatorname{conv}B_*
\subseteq\operatorname{conv}(B\setminus\{b\}).
$$

This contradicts the fact that `b` is an extreme point of `conv B`. Therefore
`B cap V_*=B_*`, proving LI.1.

Every full loaded terminal in `B\B_*` is consequently absent from `V_*`. The omitted
core vertex set has cardinality `u_*=v-v_*`, so LI.2 follows.

Insert LI.2 into CT's exact identity

$$
\kappa_*=2u_*+\sigma_*
$$

to obtain LI.3. `square`

---

## 2. Low degeneracy means near-full boundary support

Assume along an unbounded sequence

$$
\kappa_*=o(D).
$$

All quantities in

$$
\kappa_*=2u_*+\sigma_*
$$

are nonnegative integers, so

$$
u_*=o(D),
\qquad
\sigma_*=o(D).
\tag{2.1}
$$

LI.2 then gives

$$
q-q_*=o(D).
\tag{2.2}
$$

EDB proves that `sigma_*=o(D)` forces

$$
h_*\ge(2\rho-o(1))D,
\tag{2.3}
$$

which proves LI.4.

This is substantially stronger than saying only that the extreme circuit has many
rows. It says its selected positive diameter endpoints cover asymptotically the entire
full loaded boundary, even though the full stress polytope may have dimension
`s_Z=Theta(D)`.

---

## 3. Exact quantitative form away from low degeneracy

Every selected diameter endpoint has positive selected diameter degree, so

$$
q_*\le2h_*.
\tag{3.1}
$$

DB gives for the full support

$$
q\ge h\ge(2\rho-o(1))D.
\tag{3.2}
$$

Hence LI.3 gives, if `h_*/D->y` and `sigma_*/D->s`,

$$
\boxed{
\liminf\frac{\kappa_*}{D}
\ge
4\max\{0,\rho-y\}+s.
}
\tag{3.3}
$$

EDB independently gives

$$
s\ge\max\{0,\cos(y/2)-y/2\}.
\tag{3.4}
$$

Therefore every extreme ray with `y<2rho` has a quantitatively linear degeneracy. For
`0<=y<=rho` the stronger combined form is

$$
\boxed{
\liminf\frac{\kappa_*}{D}
\ge
4(\rho-y)+\cos(y/2)-y/2.
}
\tag{3.5}
$$

For `rho<=y<2rho`, EDB alone gives the positive lower bound

$$
\boxed{
\liminf\frac{\kappa_*}{D}
\ge\cos(y/2)-y/2.
}
\tag{3.6}
$$

Thus the only way `kappa_*/D` can tend to zero is for

$$
h_*/D\ge2rho-o(1)
$$

and for the selected boundary terminal set to be asymptotically full.

---

## 4. Transfer at the full DB endpoint

Assume additionally

$$
\frac hD\to2\rho.
\tag{4.1}
$$

Since `H_* subseteq H`,

$$
h_*\le h.
$$

EDB plus `sigma_*=o(D)` gives the reverse asymptotic inequality

$$
h_*\ge(2\rho-o(1))D.
$$

Therefore

$$
h-h_*=o(D),
$$

which is the first half of LI.5. LI.2 and `u_*=o(D)` give the second half.

EDB Section 6 then gives

$$
Q_*=o(D),
\qquad
b_* - \operatorname{per}F_*=o(D),
\qquad
\operatorname{per}F_*/D\to4\rho.
$$

Thus at the full DB endpoint, a low-degeneracy extreme circuit is simultaneously near
full support on `H`, near full support on the loaded boundary, and near equality in its
own selected difference-body/contact-walk perimeter comparison.

---

## 5. Scope and regressions

- LI says nothing comparable for full **interior** core vertices: an omitted interior
  point may still lie geometrically inside `conv B_*`. The exact bound is only
  `u_*>=q-q_*`, not equality.
- ESR regular even shells are compatible: their selected stress is the whole local
  support, so `q=q_*` in that standalone regression, while `sigma=Theta(D)` keeps
  `kappa` large.
- Straight-chain extremes are compatible: `q_*=2`; when embedded in a full C65 source
  with `q=Omega(D)`, LI forces linear omitted-vertex degeneracy in addition to the
  chain's own linear `sigma`.
- No lower bound on individual KKT coefficients is used.

---

## 6. Next target

The extreme-circuit problem now has a sharper dichotomy.

1. **Low `kappa_*`:** one extreme circuit already contains almost the whole loaded
   boundary and at least `2rho D-o(D)` actual diameter edges. Existing `s_Z=0`
   circuit/near-endpoint machinery should be transferred to this near-full selected
   support.
2. **Uniform high `kappa_*`:** every extreme stress omits linearly many full boundary
   terminals, has linearly many selected flex dimensions, or both. The full positive
   stress is a convex combination of at most `s_Z+1=O(D)` such circuits; a closing
   theorem must price the resulting boundary-support cover.

The next useful ensemble lemma is therefore a boundary-cover statement, not a generic
polytope nondegeneracy claim.

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Full loaded terminals B are extreme points of F=conv B. For any selected KKT stress,
its positive contact component V_* lies in conv B_*. Hence a full loaded terminal
b not in B_* cannot lie in V_*; otherwise b would lie in conv(B\{b}), contradicting
extremality. Therefore exactly
    B cap V_*=B_*,
and
    u_*=v-v_* >= q-q_*.

CT then gives
    kappa_*=2u_*+sigma_* >=2(q-q_*)+sigma_*.
Thus kappa_*=o(D) implies
    q_*=q-o(D), sigma_*=o(D).
EDB adds
    h_* >=(2rho-o(1))D.
At the full DB endpoint h/D->2rho, also
    h-h_*=o(D), Q_*=o(D),
    per(F_*)/D->4rho.

Next: transfer the existing circuit endpoint machinery to this near-full selected
support, or prove the complementary high-kappa extreme family cannot cover the full
loaded boundary consistently.
```
