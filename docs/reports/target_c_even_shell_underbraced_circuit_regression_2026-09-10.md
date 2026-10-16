<!-- theorem-state: {"artifact_id":"ART-2487A7CA84EE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — regular even shells are 2D underbraced positive PSD circuits

**Date:** 2026-09-10  
**Repository state:** PR #178 after EC/CT/TP  
**Run type:** exact regression / no-go theorem  
**Target:** Target C extreme-circuit continuation  
**External input:** none  
**Computation:** exploratory numerical checks for `N=6,8,10,12` preceded the proof; the theorem below is exact

## LEVEL I STATUS

`STILL OPEN`.

The EC/CT route isolates the flex deficit

\[
\sigma_*=2v_*-2-(e_*+h_*)
\]

of an extreme positive rigidity circuit. A tempting next step would be to prove that
`sigma_*>0` forces a one-dimensional or otherwise weak selected geometry. That is
false, even with positivity, exact unit contacts, exact diameter bars, and a PSD stress
matrix with only the affine kernel.

For every even integer `N=2m>=6`, take the regular `N`-gon scaled to have side length
one. Let

- `C` be its `N` side contacts;
- `H` be the `m=N/2` opposite-vertex diameter matching.

Then the full mixed edge set `C union H` is a rigidity-matroid circuit in the actual
realization, its unique signed KKT dependence has strictly positive contact and
diameter multipliers, and

\[
\boxed{
\sigma=rac N2-2.
}
\tag{ESR.1}
\]

Moreover the signed stress matrix

\[
\Omega=L_C(\alpha)-L_H(\beta)
\]

is PSD and has kernel exactly

\[
\boxed{
\ker\Omega=\operatorname{span}\{\mathbf1,P_x,P_y\}.
}
\tag{ESR.2}
\]

Thus there are genuinely two-dimensional, highly underbraced, positive PSD extreme
circuits. Any proof of Level I must use information absent from this family, such as
full actual-diameter support, global minimum-diameter capacity, or compatibility among
multiple extreme circuits.

---

## 1. Geometry and counts

Put

\[
\theta:=\frac{2\pi}{N},
\qquad
R:=\frac1{2\sin(\pi/N)}.
\]

The vertices are

\[
p_j=R(\cos j\theta,\sin j\theta),
\qquad j\in\mathbb Z/N\mathbb Z.
\]

Then consecutive vertices are at distance one and opposite vertices are at distance

\[
D=2R=\csc(\pi/N).
\]

For a regular polygon, no nonconsecutive chord has length one, so the unit-contact
graph on these vertices is exactly `C_N`. The diameter graph is exactly the opposite
perfect matching.

Hence

\[
v=N,
\qquad
e=N,
\qquad
h=N/2,
\qquad
|C\cup H|=3N/2.
\]

If this support is a circuit, its flex deficit is therefore

\[
2N-2-\frac{3N}{2}
=\frac N2-2,
\]

which is ESR.1.

The configuration is triangle-free with respect to unit contacts because `C_N` has no
3-cycle.

---

## 2. The mixed self-stress space is one-dimensional

Give the cycle edge `j(j+1)` coefficient `a_j` and the opposite diameter edge
`j(j+m)` coefficient `b_j`, with the signed equilibrium convention

\[
L_C(a)P=L_H(b)P.
\]

At vertex `j`, the two side vectors are symmetric around the radial line through
`p_j`, while the opposite diameter vector is radial. Project equilibrium onto the
tangent line at `p_j`. The diameter term vanishes there, and the two side projections
are nonzero and opposite. Therefore

\[
\boxed{a_{j-1}=a_j}
\tag{2.1}
\]

for every `j`.

Thus all cycle coefficients equal one scalar `a`. The radial equilibrium then fixes
every diameter coefficient. Since

\[
(p_j-p_{j-1})+(p_j-p_{j+1})
=2(1-\cos\theta)p_j
\]

and

\[
p_j-p_{j+m}=2p_j,
\]

equilibrium gives

\[
\boxed{b=a(1-\cos\theta).}
\tag{2.2}
\]

The same value is obtained at the opposite endpoint of each matching edge. Hence the
entire signed self-stress space is one-dimensional.

For `a!=0`, equations (2.1)-(2.2) make every edge coefficient nonzero. Consequently
no proper subset of `C union H` is dependent. Therefore:

### Theorem ESR.1

`C union H` is an actual rigidity-matroid circuit.

Choosing `a>0` makes `b>0`, so the circuit dependence has exactly the KKT sign pattern:
positive contact multipliers and positive diameter multipliers after the fixed sign
change on diameter rows.

---

## 3. Normalized positive stress

Normalize

\[
\sum_{h\in H}\beta_h=1.
\]

By symmetry,

\[
\boxed{
\beta=\frac2N
}
\tag{3.1}
\]

on each of the `N/2` diameter edges. Equation (2.2) gives

\[
\boxed{
\alpha
=\frac{2}{N(1-\cos(2\pi/N))}
}
\tag{3.2}
\]

on each side contact.

Both are strictly positive.

---

## 4. Exact Fourier audit of the stress matrix

The stress matrix is the circulant matrix

\[
\Omega=\alpha L(C_N)-\beta L(M),
\tag{4.1}
\]

where `M` is the opposite perfect matching.

For the Fourier mode

\[
f_k(j)=\exp(2\pi i k j/N),
\]

the cycle Laplacian has eigenvalue

\[
\lambda_C(k)=4\sin^2\frac{\pi k}{N}.
\tag{4.2}
\]

The opposite matching Laplacian has eigenvalue

\[
\lambda_M(k)=1-(-1)^k
=
\begin{cases}
0,&k\text{ even},\\
2,&k\text{ odd}.
\end{cases}
\tag{4.3}
\]

From (2.2),

\[
\beta
=2\alpha\sin^2\frac\pi N.
\tag{4.4}
\]

Therefore

\[
\mu_k:=\lambda_\Omega(k)
=
\begin{cases}
4\alpha\sin^2(\pi k/N),&k\text{ even},\\[1mm]
4\alpha\left(
\sin^2(\pi k/N)-\sin^2(\pi/N)
\right),&k\text{ odd}.
\end{cases}
\tag{4.5}
\]

For `1<=k<=N-1`,

\[
\sin^2\frac{\pi k}{N}
\ge
\sin^2\frac\pi N,
\]

with equality only at `k=1,N-1`. Thus every `mu_k>=0`, and the zero modes are exactly

\[
k=0,1,N-1.
\]

The `k=0` mode is the constant vector; the real and imaginary parts of `k=1` are the
coordinate vectors `P_x,P_y`. Hence ESR.2 follows.

This is stronger than merely having a PSD selected stress: the stress matrix has the
maximum possible rank `N-3` for an affinely spanning planar configuration even though
the bar-rigidity circuit has a linear flex deficit.

---

## 5. Relation to EC/CT/TP

For this family

\[
h=\frac N2,
\qquad
q=N,
\qquad
d=q-h=\frac N2,
\qquad
\sigma=\frac N2-2.
\]

The contact graph is the convex `N`-cycle, so

\[
b=N,
\qquad
Q=N-4,
\qquad
x=b-q=0.
\]

EC's exact selected face identity is saturated:

\[
b+Q
=2N-4
=2h+2\sigma.
\]

CT's terminal ledger is also exact:

\[
q+2\sigma
=2N-4
=x+Q+2d.
\]

As `N->infinity`,

\[
D=\csc(\pi/N)\sim\frac N\pi,
\]

so

\[
\frac hD\to\frac\pi2,
\qquad
\frac\sigma D\to\frac\pi2.
\]

This lies well inside TP's allowed high-flex region; TP does not falsely exclude it.

---

## 6. Why this is a regression, not a counterexample to Erdős #99

The regular even shells are not asserted to be global minimum-diameter configurations
for their cardinalities. More importantly, the repository's post-ZF perfect-matching
branch theorem excludes an unbounded sequence whose **full actual** diameter graph is
a perfect matching under the global-minimizer hypotheses.

The point here is narrower. An extreme selected stress of a larger full-support C65
framework is allowed to omit actual diameter edges. Therefore its selected `H_*` can
be a matching even when the full actual diameter graph branches linearly.

Consequently none of the following implications is valid by local circuit/PSD theory
alone:

- `sigma_*>0` implies a one-dimensional selected force hull;
- `sigma_*>0` implies extra scalar PSD kernel;
- maximal-rank PSD stress matrix implies `sigma_*=0`;
- selected perfect matching can be excluded by the full-support matching theorem.

Any use of those statements must add a full-support or global-capacity hypothesis.

---

## 7. Corrected next target

The high-`sigma_*` branch cannot be killed by classifying underbraced circuits as weak.
The exact missing ingredient is compatibility with the omitted actual C65 rows.

A useful target is now:

> **Circuit-extension incompatibility.** Starting from an extreme positive circuit
> `S`, quantify how many omitted actual diameter rows can be added while preserving
> the KKT sign cone before the selected perfect-matching/even-shell type is forced to
> acquire a larger positive circuit. Combine that expansion with TP until one obtains
> an extreme circuit with `sigma_*=o(D)` or a full-support face/capacity contradiction.

The even-shell family is the binding regression for this statement: it must be escaped
using the omitted full actual rows, not the internal geometry of `S` alone.

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Exact regression family:
Take a regular even N-gon with side length 1. Contacts are the N-cycle; actual
diameters are the N/2 opposite pairs. The mixed self-stress equations force all side
coefficients equal and all diameter coefficients equal, so the stress space is 1D and
all coefficients are nonzero. Hence the whole support is a rigidity-matroid circuit.

Counts:
    v=N, e=N, h=N/2,
    sigma=2N-2-(e+h)=N/2-2.
So sigma is linear and the circuit is genuinely 2D.

With beta=2/N and alpha=2/[N(1-cos(2pi/N))], Fourier modes give
    mu_k=4alpha sin^2(pi k/N)                    (k even),
    mu_k=4alpha[sin^2(pi k/N)-sin^2(pi/N)]      (k odd).
Thus Omega is PSD with kernel exactly k=0,1,N-1 = span{1,P_x,P_y}.

Therefore high sigma cannot be excluded by 1D geometry, PSD-kernel enlargement, or
local circuit rigidity. The next argument must use compatibility with omitted full
C65 rows / global capacity.
```
