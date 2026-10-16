# Hostile audit — paired-remainder path through `t<=1.8659`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_paired_remainder_path_t18659_2026-09-15.md`
- `research/verify_target_c_paired_remainder_path_t18659.py`

**Verdict:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This audit treats the `1.865` paired-remainder theorem and its hostile audit as parent
inputs. The only new issue is whether the same functional, retained-mass feasibility
box, and physical branch inequality remain valid at `T=1.8659`.

## 1. The exact certificate is outward

The verifier does not use floating-point values to decide any sign.  It encloses `pi`
with Machin-series rational bounds, `sqrt(3)` and every derived square root by integer
square-root intervals, and `sin` by an alternating Taylor enclosure.  Every theorem
sign is an exact `Fraction` assertion.

A separate execution gives

```text
U0 upper                    2.1133646928204137
delta max                   0.10056953954624942
H(2.0675)                   -9.4162419414e-05
opposite-branch margin       1.3733216829e-04
pair-weight floor            0.1552743862720853
residual occurrence mass     1.7569512274558294
residual bathtub floor       0.0250013357628610
low-energy pair floor        0.00064331652911746
one-phase pair floor         0.00021443884303915
```

The displayed decimals are diagnostics only.

**Verdict:** PASS.

## 2. The corrected retained-mass box is rechecked, not extrapolated

At `T=1.8659` the verifier recomputes

\[
U_0={9T\over2}-2\pi,
\qquad
\delta_{max}={U_0-C_{76}\over2}.
\]

It checks `delta_max<0.101`, `U0<2.114`, the discriminant gate
`5 U0^2<32 Delta_2`, and the same derivative bounds used by the parent corrected
feasibility theorem.  For `z0=2.0675` it checks

\[
F'(z_0)<1/16,
\]

through the same elementary square bound and obtains an exact negative outward upper
bound for `H(z0)`.  Therefore the parent monotonicity argument gives

\[
z>2.0675-o(1)
\]

on the enlarged endpoint box.  No old `1.865` numerical sign is reused.

**Verdict:** PASS.

## 3. Substituting the pair floor remains legitimate

The parent hostile audit proves for

\[
L(P)=P-{\delta-F(z-2P)\over\lambda}
\]

that

\[
L_P=1-{2F'(z-2P)\over\lambda}>0
\]

whenever the residual mass lies in `[0,pi]` and `lambda>2-sqrt(3)`.
The new threshold is `lambda=0.4887`, so the same strict inequality holds.

The certificate checks the adverse floor

\[
P_0=z_0-U_0+2\delta_{max}>0
\]

and

\[
2P_0<z_0.
\]

Thus its residual mass is nonnegative.  It is explicitly below `pi` because the exact
outward quantities give `r0<z0<2.068<pi`.  Therefore the parent derivative bound is
applicable at the substituted floor.

If at any physical survivor the lower pair floor exceeded `z/2`, the endpoint-count
inequality would itself contradict the fact that pair weight consumes two occurrence
weights, so no omitted negative-residual case survives.

**Verdict:** PASS.

## 4. Endpoint monotonicities retain their signs

After inserting

\[
P_0=z-U_0+2\delta+\kappa/2,
\]

the parent audit computes

\[
L_z=1-F'(r)/\lambda>0,
\]

\[
L_\kappa={1\over2}-F'(r)/\lambda>0,
\]

\[
L_\delta=2-{1\over\lambda}-{4F'(r)\over\lambda}<0,
\]

and

\[
L_{U_0}=-1+{2F'(r)\over\lambda}<0.
\]

The first, second, and fourth inequalities follow from
`lambda>2-sqrt(3)`; the third is even stricter because `lambda<1/2`.
Both hold for `lambda=0.4887`.  Hence the adverse substitution

\[
t=T,\quad z=z_0,\quad\kappa=0,\quad\delta=\delta_{max}
\]

is valid throughout the new box.

**Verdict:** PASS.

## 5. The residual bathtub uses genuinely unspent occurrence weight

For each retained O--O train with terminal weights `a,b`, subtracting
`w=min(a,b)` from both terminals leaves nonnegative residual weights.  Pair and
residual weights partition the original retained occurrence weights exactly.  The
residual measure is therefore still dominated by the same three-phase perimeter
measure and has total mass `z-2P`.

The three-well bathtub lower bound

\[
E_{res}\ge F(z-2P)-o(1),
\qquad F(s)=s-6\sin(s/6),
\]

uses no extra energy budget.  This was the load-bearing new step in the parent `1.865`
audit and is unchanged here.

**Verdict:** PASS.

## 6. Physical branch orientation still has strict margin

For terminal energy at most `lambda`, the same-oriented chord upper bound is

\[
{r_\tau^2\over D^2}
\le\lambda-\lambda^2/4+o(1),
\]

while Section 157 gives

\[
{r_\tau\over D}
\ge1-\delta-\lambda/2-o(1).
\]

The verifier evaluates the adverse `delta_max` and proves the squared difference is
strictly positive.  The diagnostic margin is `1.37e-4`, larger than at the `1.865`
parent endpoint.  Since `lambda<1/2`, the two opposite terminal host arcs remain
disjoint with a fixed positive angular gap.

**Verdict:** PASS.

## 7. The train-count and integer switch bound are correctly rounded

The exact low-energy pair floor exceeds `0.0006-o(1)`.  Among at most three phase
windows, one phase has pair weight greater than `0.0002-o(1)`.  Since one train carries
pair weight at most one, the same phase contains more than `0.0002D-o(D)` actual
trains.

The inherited path/hub theorem makes their crosscut dual a path with a single hub.
The complete diameter graph contributes at most two interval endpoints per edge, so

\[
\sum_i N_i\le2\pi D+o(D).
\]

After removing the one hub boundary, the number of eligible boundaries is still
`>0.0002D-o(D)`.  The exact rational estimate

\[
{2(355/113)\over0.0002}=31415.9292\ldots<31416
\]

implies that, for all sufficiently large sources, one integer `N_i` is strictly below
`31416`, hence

\[
N_i\le31415.
\]

**Verdict:** PASS.

## 8. Scope and remaining obstruction

This theorem does not exclude the finite one-sided strip.  It supplies neither a
uniform KKT multiplier floor nor a strict-diameter deformation.  It also does not
address the separate Type-I macroscopic inactive-container branch.

The numerical root near `1.8659664` quoted in the theorem is explicitly descriptive,
not theorem authority; no claim at that endpoint depends on floating-point root
finding.

**Final verdict:** **PASS.**  The paired-remainder O--O path/hub/one-sided-strip normal
form is valid through `t<=1.8659` at proof-only full-core Type-II scope. C-II and Level
I remain open.
