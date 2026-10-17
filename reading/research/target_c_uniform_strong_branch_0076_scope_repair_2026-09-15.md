> Generated reading edition · [exact source](../../research/target_c_uniform_strong_branch_0076_scope_repair_2026-09-15.md) · source SHA-256 `89935723cb2863d87184f2c5a2eed014487920a8e29a4303f1411f7267b7a7d2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 6 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5782d6f19b7873226c137353d762e0178a2342fe", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_uniform_strong_branch_0076_scope_repair_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7f02b478d57a36b64f843313639a02b2838d542aaf363fba8c828060e59c693b"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — scope repair for the uniform strong-branch `g=0.0076` orbit theorem

**Date:** 2026-09-15  
**Base candidate:** `research/target_c_uniform_strong_branch_orbit_capacity_gap_0076_2026-09-15.md`  
**Status:** proof-only repair; theorem-state authority unchanged  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The `g=0.0076` candidate has the right low-center capacity mechanism, but as written its
fallback region repeats a scope defect that had already been repaired in the earlier
`g=0.0053` theorem.  The physical pair theorem

```math
\rho\ge
\min\left\{
{(a+b-K)_+^2\over10},
{2\min(a,b)^2\over29}
\right\},
\qquad K={2\over\sqrt3},
```

is stated only for phase-family masses `a,b<=K`.  The candidate correctly proves that
the strong region extends to `C_s(W)>W/2`, but then applies the weak `2/29` coefficient
to **all** `C>=C_s(W)`.  Since the formal center range extends beyond `C=K`, that last
step is not justified for `C>K`.

The repair is to split the fallback exactly as in the corrected `g=0.0053` theorem:

1. `C_s(W)<=C<=K`: use the weak physical-pair capacity `Phi_{2/29}`;
2. `C>K`: do not use the physical pair theorem; use only the generic triangle-free
   bound `E<=C(W-C)`.

The high-center branch has more than `0.032` crossing-density margin at `g=0.0076`, so
this repair preserves the claimed matched gap.

---

## 1. What remains unchanged

Retain the candidate notation

```math
\Delta_2={\pi\over2\sqrt3},
\qquad
K={2\over\sqrt3},
\qquad
r_*={\sqrt{20/29}},
```

```math
g=0.0076,
\qquad
A_0=2\sqrt{\Delta_2}+g,
\qquad
M_0={4\Delta_2\over A_0}.
```

For a dominant exact orbit of mass `W`, write its ordered phase masses

```math
C\ge U\ge V\ge0,
\qquad W=C+U+V.
```

The candidate's Sections 1--4 remain valid.  In particular:

- on `W/3<=C<=W/2`, both center/leaf pairs lie in the strong `1/10` branch;
- the strong capacity
  ```math
  \Phi_{1/10}(W,C)
  =C(W-C)-{1\over10}{3C-W\over C}
   \left({W+C\over2}-K\right)^2
  
  ```
  is strictly concave and has a unique maximizer `C_*(W)` in `(W/3,W/2)`;
- the strong branch remains valid through
  ```math
  C_s(W)=W-{W-K\over r_*}>W/2.
  
  ```

The exact certificate places `C_s(W)` well below `K` throughout the contradiction
interval.  The smallest separation at the worst endpoint is still about `0.1546`, so
there is no ambiguity about the ordering

```math
W/2<C_s(W)<K.
\tag{SR.1}
```

---

## 2. Valid weak fallback: `C_s(W)<=C<=K`

On this interval all three phase masses are at most `K`, so the unconditional physical
pair theorem is available and gives

```math
E\le\Phi_{2/29}(W,C).
```

For `C>=W/2`, the derivative formula from the candidate is

```math
\partial_C\Phi_{2/29}
=W-2C
-{2\over29}
\left[
{W\over C^2}r^2+qr
\right]<0,
```

with

```math
r={W+C\over2}-K,
\qquad q=3-{W\over C}.
```

Therefore the valid weak region is maximized at its left endpoint:

```math
\boxed{
E\le B_0(W):=\Phi_{2/29}(W,C_s(W)).
}
\tag{SR.2}
```

This is exactly the same `B_0` used by the original candidate, but it is now claimed
only on the interval where the pair theorem actually applies.

---

## 3. High-center branch: `C>K`

For `C>K`, discard the physical pair theorem completely.  Triangle-freeness alone gives

```math
E\le C(U+V)=C(W-C).
\tag{SR.3}
```

The contradiction domain has

```math
W\le A_0<2K,
```

so

```math
K>W/2.
```

Hence `C(W-C)` is decreasing for `C>=K`, and

```math
\boxed{
E\le K(W-K).
}
\tag{SR.4}
```

The residual exact orbits have total mass at most `A_0-W`, so their total crossing mass
is at most

```math
{(A_0-W)^2\over4}.
```

Thus the entire high-center branch obeys

```math
\Delta_2
\le H(W):=
K(W-K)+{(A_0-W)^2\over4}.
\tag{SR.5}
```

Differentiate:

```math
H'(W)=K-{A_0-W\over2}.
```

For `M_0<=W<=A_0`,

```math
H'(W)
\ge K-{A_0-M_0\over2}>0.
\tag{SR.6}
```

Therefore the high-center capacity is largest at `W=A_0`, where

```math
\boxed{
H(W)\le K(A_0-K).
}
\tag{SR.7}
```

The exact companion certificate proves

```math
\boxed{
\Delta_2-K(A_0-K)>0.0321.
}
\tag{SR.8}
```

So no high-center dominant orbit can occur in a hypothetical `A<=A_0` source.  The
margin is hundreds of times larger than the low-center endpoint margin.

---

## 4. Correct global capacity statement

Every dominant orbit in the contradiction domain falls into one of three valid regions:

1. strong region `C<=C_s(W)`, with capacity at most `Psi_1(W)`;
2. weak physical fallback `C_s(W)<=C<=K`, with capacity at most `B_0(W)`;
3. high-center region `C>K`, excluded by (SR.8) after residual-orbit capacity is added.

The original candidate already proves that, after adding residual-orbit capacity, both
`Psi_1(W)` and `B_0(W)` are increasing in `W` and are maximized at `W=A_0`.  Its exact
endpoint certificate gives positive gaps for both low-center branches at `g=0.0076`.
The new high-center certificate supplies the missing third branch.

Consequently the contradiction hypothesis

```math
A\le2\sqrt{\Delta_2}+0.0076
```

is impossible, and the repaired theorem is

```math
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.0076.
}
\tag{SR.9}
```

The same repair applies verbatim when the argument is rerun on the strict-rhombus train
graph.  Therefore

```math
\boxed{
\liminf {T_R\over D}
\ge2\sqrt{\Delta_2}+0.0076,
\qquad
\liminf {\sigma_R\over D}\ge0.0152.
}
\tag{SR.10}
```

---

## 5. Scope and next use

The repair changes no numerical optimizer in the valid low-center region.  It only
removes an unjustified use of the pair theorem for `C>K` and replaces it by a much
stronger generic exclusion.

The matched `g=0.0076` input is therefore safe to propagate through the already-audited
energy-restored complement-rhombus-incidence theorem.  That downstream composition is
independent of the scope repair: it needs only the simultaneous all-train and
rhombic-only matched floors (SR.9)--(SR.10).

C-II and Level I remain open.
