<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "68f1753c4b95ac8328b70372b7413068aafcf4cc", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_phase_star_orbit_capacity_gap_0053_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1b6e7e9336a575ae9103862dcf45163156487fec6f72e73e0901a8649deca723"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — corrected phase-star orbit capacity gives matched gap `0.0053`

**Date:** 2026-09-15  
**Status:** proof-only strengthening of the matched all-train/rhombic atomic gap  
**Scope:** canonical full-core Type-II train-measure branch  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This note supersedes `target_c_phase_star_orbit_capacity_gap_0052_2026-09-15.md`.
The earlier note found the correct low-center capacity mechanism, but it applied the
physical pair theorem to a formal center-mass range `C>K=2/sqrt(3)` outside that
theorem's stated scope.  The repair is simple: split off `C>K` and use the generic
triangle-free bound there.  That branch is far below the required crossing density.
The valid `C<=K` branch retains the phase-star capacity argument and safely supports
the stronger round value

\[
\boxed{g=0.0053.}
\]

Consequently, with

\[
\Delta_2={\pi\over2\sqrt3},
\]

we prove at the same proof-only train-measure scope

\[
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.0053,
}
\tag{PC53.1}
\]

and independently on the strict-rhombus train graph

\[
\boxed{
\liminf {T_R\over D}
\ge2\sqrt{\Delta_2}+0.0053,
\qquad
\liminf {\sigma_R\over D}\ge0.0106.
}
\tag{PC53.2}

The exact rational certificate leaves more than `4.63e-5` crossing-density margin at
`g=0.0053`.  Numerical exploration places the capacity crossing just below `0.00535`;
no value beyond `0.0053` is claimed.

---

## 1. Physical pair input

Put

\[
K={2\over\sqrt3},
\qquad
\alpha={2\over29}.
\]

The hostile-audited iterative-pruning corollary gives the following physical theorem.
For two exact train-phase atom families of masses `a,b<=K`, with projective axes
separated by `pi/3`, their normalized missing-pair mass `rho` satisfies

\[
\boxed{
\rho\ge\alpha(a+b-K)_+^2.
}
\tag{PC53.3}

The upper-size hypothesis `a,b<=K` is binding and is retained explicitly below.

---

## 2. Three-phase orbit and center/leaf correlation

Fix one exact projective `pi/3` orbit and order its three phase-class masses as

\[
C\ge U\ge V\ge0,
\qquad
W=C+U+V.
\tag{PC53.4}

Let `e(C,U)`, `e(C,V)`, and `e(U,V)` be their limiting physical crossing masses and
write

\[
x=CU-e(C,U),
\qquad
y=CV-e(C,V).
\tag{PC53.5}

If `E` is the total crossing mass in this orbit, then

\[
h:=C(U+V)-E=x+y-e(U,V).
\tag{PC53.6}

For each actual `UV` crossing, triangle-freeness makes the endpoint neighborhoods in
the center class disjoint.  Summing the resulting center-degree deficits gives

\[
C e(U,V)\le Vx+Uy.
\]

Therefore, with

\[
a=1-{V\over C},
\qquad
b=1-{U\over C},
\]

we have the exact correlation

\[
\boxed{a x+b y\le h.}
\tag{PC53.7}

---

## 3. Low-center physical capacity

Assume first

\[
C\le K.
\tag{PC53.8}

Then `U,V<=C<=K`, so the pair theorem (PC53.3) applies to both center/leaf pairs:

\[
x\ge\alpha(C+U-K)_+^2,
\qquad
y\ge\alpha(C+V-K)_+^2.
\tag{PC53.9}

For fixed `W,C`, put

\[
\ell={U+V\over2},
\qquad d={U-V\over2}\ge0,
\qquad r=C+\ell-K,
\qquad A=1-\ell/C.
\]

Then

\[
a=A+d/C,
\qquad b=A-d/C.
\]

A direct three-case expansion according to the signs of `r-d` and `r+d` gives

\[
\boxed{
 a(C+U-K)_+^2+b(C+V-K)_+^2
 \ge
 {3C-W\over C}
 \left({W+C\over2}-K\right)_+^2.
}
\tag{PC53.10}

For completeness:

- if `r<=-d`, both sides vanish;
- if `-d<r<=d`, at most the `U` term is active, and for `r>0`,
  `(A+d/C)(r+d)^2>=4Ar^2>=2Ar^2`;
- if `r>d`, expanding both terms gives
  `2Ar^2+2Ad^2+4rd^2/C>=2Ar^2`.

Since `2A=(3C-W)/C`, (PC53.10) follows.

Combining (PC53.7), (PC53.9), and (PC53.10) yields

\[
\boxed{
E\le\Phi(W,C):=
C(W-C)-\alpha{3C-W\over C}
\left({W+C\over2}-K\right)_+^2
}
\tag{PC53.11}

whenever `C<=K`.

---

## 4. High-center scope repair

If instead

\[
C>K,
\tag{PC53.12}

we do **not** use the physical pair theorem.  The generic triangle-free center bound is
always valid:

\[
E\le C(U+V)=C(W-C).
\tag{PC53.13}

On the endpoint interval below, `W<=A_0<2K`, so `K>W/2`.  Hence `C(W-C)` is strictly
decreasing for `C>=K`, and

\[
\boxed{E\le K(W-K).}
\tag{PC53.14}

This branch is quantitatively far from saturation.  The exact verifier shows that even
at the largest relevant orbit mass its total crossing capacity is below `Delta_2` by
more than `0.0348` after the residual-orbit optimization below.  Thus no feasible
near-endpoint atomic measure can use a dominant center with mass above `K`.

This is the scope repair missing from the superseded `0.0052` note.

---

## 5. Low-center optimizer

Set

\[
A_0:=2\sqrt{\Delta_2}+0.0053,
\qquad
M_0:={4\Delta_2\over A_0}.
\tag{PC53.15}

The certificate gives

\[
M_0>1.8993>\sqrt3.
\tag{PC53.16}

For `M_0<=W<=A_0` and `W/3<=C<=W/2`, define

\[
q=3-{W\over C},
\qquad
r={W+C\over2}-K.
\]

Then `0<=q<=1`, `r>0`, and `r<C`.  Equation (PC53.11) becomes

\[
\Phi(W,C)=C(W-C)-\alpha q r^2.
\tag{PC53.17}

Differentiation gives

\[
\Phi_C
=W-2C-\alpha\left({W\over C^2}r^2+qr\right),
\tag{PC53.18}
\]

and

\[
\Phi_{CC}
=-2-\alpha\left[
{2Wr\over C^2}\left(1-{r\over C}\right)+{q\over2}
\right]
\le-2.
\tag{PC53.19}

At `C=W/2`, (PC53.18) is strictly negative.  At `C=W/3`, the exact verifier checks
uniformly on `M_0<=W<=A_0` that

\[
\Phi_C(W,W/3)>0.6285.
\tag{PC53.20}

Therefore the low-center capacity has a unique maximizer

\[
C_*(W)\in(W/3,W/2).
\tag{PC53.21}

Moreover

\[
{W\over2}\le {A_0\over2}<K,
\]

so this optimizer lies strictly within the physical pair theorem's size scope.

Define

\[
\Psi(W):=\Phi(W,C_*(W)).
\tag{PC53.22}

---

## 6. Sum over exact orbits

Let the exact orbit masses be `M_r`, total atomic mass

\[
A=\sum_rM_r,
\]

and dominant orbit mass

\[
M=\max_rM_r.
\]

The audited crossing decomposition gives

\[
\sum_rE_r=\Delta_2.
\tag{PC53.23}

The generic orbit bound `E_r<=M_r^2/4` gives

\[
4\Delta_2\le\sum_rM_r^2\le MA.
\]

Thus if `A<=A_0`,

\[
M\ge {4\Delta_2\over A}\ge M_0.
\tag{PC53.24}

### High-center dominant branch

If the dominant orbit has `C>K`, use (PC53.14), while all residual orbit masses have
total `A-M`.  Hence

\[
\Delta_2
\le K(M-K)+{(A-M)^2\over4}.
\tag{PC53.25}

The right side increases with `A`, so set `A=A_0`.  Its derivative in `M` is

\[
K-{A_0-M\over2}>1,
\]

by the exact certificate.  It is therefore maximized at `M=A_0`, where it equals

\[
K(A_0-K)<\Delta_2-0.0348,
\]

contradiction.

Hence the dominant orbit necessarily lies in the low-center branch.

### Low-center dominant branch

Now the dominant orbit pays `Psi(M)`, and all residual orbits pay at most their generic
square capacity:

\[
\boxed{
\Delta_2
\le\Psi(M)+{(A-M)^2\over4}.
}
\tag{PC53.26}

Again set `A=A_0`.  By the envelope theorem and (PC53.17),

\[
\Psi'(M)=\Phi_W(M,C_*(M))
=C_*+\alpha{r^2\over C_*}-\alpha qr
\ge C_*-\alpha qr.
\]

Using `C_*>=M/3`, `q<=1`, and `r<=3A_0/4-K`,

\[
\Psi'(M)
\ge {M_0\over3}-\alpha\left({3A_0\over4}-K\right).
\tag{PC53.27}

The exact verifier gives

\[
\Psi'(M)>0.6139,
\]

while

\[
{A_0-M\over2}<0.0053.
\]

Thus

\[
{d\over dM}
\left[
\Psi(M)+{(A_0-M)^2\over4}
\right]
>0.6086.
\tag{PC53.28}

The right side of (PC53.26) is maximized at `M=A_0`.  The residual orbit mass vanishes,
leaving

\[
\Delta_2\le\Psi(A_0).
\tag{PC53.29}

---

## 7. Exact certificate at `g=0.0053`

The verifier

`research/verify_target_c_phase_star_orbit_capacity_gap_0053.py`

uses exact `Fraction` arithmetic.  It encloses `pi` by Machin's identity and square
roots by integer-square-root bounds.

For the high-center branch it certifies

\[
K(A_0-K)<0.87206<\Delta_2-0.0348.
\tag{PC53.30}

For the low-center branch, choose

\[
c_0=0.94047.
\]

Because `Phi_CC<=-2`, strong concavity gives

\[
\max_C\Phi(A_0,C)
\le
\Phi(A_0,c_0)+{\Phi_C(A_0,c_0)^2\over4}.
\tag{PC53.31}

The exact outward calculation gives

\[
\boxed{
\Delta_2-\Psi(A_0)>4.63\times10^{-5}.
}
\tag{PC53.32}

This contradicts (PC53.29).  Therefore `A<=A_0` is impossible, and

\[
\boxed{
A>2\sqrt{\Delta_2}+0.0053-o(1).
}
\tag{PC53.33}

The exposed-hull train-measure inequality `A<=(T-q/2)/D` proves (PC53.1).

---

## 8. Strict-rhombus transfer

The hostile-audited matched minimax stack separately verifies the same train-phase
framework on the strict-rhombus train graph: its vertices are complete non-singleton
rhombic trains, its edge count is exactly `R_4`, limiting crossings occur only at
projective separation `pi/3`, and the same physical pair theorem applies to selected
phase families.

The proof above uses only those properties.  Repeating it on that graph gives

\[
\liminf {T_R\over D}
\ge2\sqrt{\Delta_2}+0.0053.
\]

Since `B_4=2T_R` and

\[
\sigma_R=B_4-4\sqrt{R_4},
\]

we obtain

\[
\boxed{\liminf {\sigma_R\over D}\ge0.0106.}
\]

---

## 9. Disposition and downstream use

The superseded `0.0052` note should not be cited as a proof because of its omitted
`C>K` scope split.  This note repairs that issue and improves the safe matched gap at
the same time.

The immediate downstream substitutions are

```text
C_53 = 2 sqrt(Delta_2) + 0.0053,
(T-q/2)/D >= C_53 - o(1),
T_R/D       >= C_53 - o(1),
sigma_R/D   >= 0.0106 - o(1).
```

These strengthen the Section-171 envelope and the current two-bin / rhombus-incidence
low-`t` chain.  They still do not construct a same-cardinality strict sub-`D` source or
force an exact unit equilateral triangle.

**Disposition:** corrected proof-only matched atomic strengthening. C-II and Level I remain open.
