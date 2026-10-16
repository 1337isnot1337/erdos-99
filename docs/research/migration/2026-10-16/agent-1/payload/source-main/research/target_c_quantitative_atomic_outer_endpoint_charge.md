# Target C — quantitative atomic outer-endpoint charge

**Date:** 2026-09-12  
**Lifecycle:** proof-only research theorem; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Audited-working §154 proves that an asymptotically geodesic Type-II outer contact walk
has atomless projective direction measure, so the atomic train population from §142
must terminate on bounded defect faces. This note gives a quantitative finite-detour
version.

Let

\[
\lambda_D:={b-\operatorname{per}(F)\over D}\ge0
\]

and work along a Type-II subsequence on which

\[
\lambda_D\to\lambda\ge0.
\tag{AO.1}
\]

Put

\[
\Delta_2={\pi\over2\sqrt3}.
\]

For every threshold

\[
0<\tau<{\Delta_2\over9\pi},
\tag{AO.2}
\]

define

\[
C_{atom}(\lambda)
:=\bigl[6(\pi+\lambda)^2\lambda\bigr]^{1/3}.
\tag{AO.3}
\]

Then the bounded stopped-train endpoint incidence obeys

\[
\boxed{
\liminf {Q+4f\over D}
\ge
4\sqrt{\Delta_2-9\pi\tau}
-{3\pi\over\tau}C_{atom}(\lambda).
}
\tag{AO.4}
\]

Taking the supremum over admissible `tau` gives the strongest version of (AO.4).
As `lambda->0`, one may take `tau->0` more slowly than
`C_atom(lambda)`, and therefore

\[
\boxed{
\liminf {Q+4f\over D}
\ge4\sqrt{\Delta_2}-o_{\lambda\to0}(1).
}
\tag{AO.5}
\]

This recovers the endpoint capacity in §154 and supplies an explicit stability modulus
of order at worst `lambda^(1/6)` after optimizing `tau`.

---

## 1. A cosine-transform atom costs outer-walk excess

Normalize the occurrence-counted outer-walk direction measure by

\[
\mu_D^{out}:={1\over D}
\sum_{e\in\partial_{out}C}^{occ}\delta_{[e]}
\]

on the projective circle `R/pi Z`. Pass to a weak limit `mu_out` along the chosen
subsequence. Type-II perimeter convergence and (AO.1) give

\[
M:=\mu_{out}(\mathbb R/\pi\mathbb Z)
=\pi+\lambda.
\tag{AO.6}
\]

For

\[
K(t):=|\cos t|,
\qquad
H(\alpha):=\int K(\theta-\alpha)\,d\mu_{out}(\theta),
\]

the projection argument of §154 and uniform Type-II width convergence give

\[
H(\alpha)\ge2
\qquad\forall\alpha.
\tag{AO.7}
\]

Also `0<=H<=M` and

\[
\int_0^\pi H(\alpha)\,d\alpha=2M.
\]

Set

\[
g:=H-2\ge0.
\]

Then

\[
\boxed{
\int_0^\pi g=2\lambda.
}
\tag{AO.8}
\]

On the projective circle the kernel satisfies, distributionally,

\[
K''+K=2\delta_{\pi/2}.
\tag{AO.9}
\]

Hence

\[
H''+H=2R_*\mu_{out},
\tag{AO.10}
\]

where `R_*` is rotation by `pi/2`. In particular

\[
g''\ge-H\ge-M
\tag{AO.11}
\]

in the distributional sense.

### Lemma AO.1 — atom cusp bound

If `mu_out` has an atom of mass `A` at one projective direction, then

\[
\boxed{A^3\le6M^2\lambda.}
\tag{AO.12}
\]

#### Proof

The atom produces, at the perpendicular argument, an upward jump `2A` in the
one-sided derivative of `H`, hence of `g`. If the one-sided derivatives are `d_-` and
`d_+`,

\[
d_+-d_-=2A.
\]

Therefore either `d_+>=A` or `d_-<=-A`.

Assume first `d_+>=A` and put the cusp point at zero. Inequality (AO.11) says that the
derivative can decrease at rate at most `M`; positive measure in (AO.10) only creates
additional upward derivative. Thus for

\[
0\le t\le A/M,
\]

\[
g'(t)\ge A-Mt.
\]

Since `g(0)>=0`,

\[
g(t)\ge At-{M\over2}t^2.
\]

Integrating one side of the cusp gives

\[
\int_0^{A/M}g(t)\,dt
\ge {A^3\over3M^2}.
\]

The case `d_-<=-A` is identical after reversing the coordinate. Therefore (AO.8)
gives

\[
2\lambda\ge {A^3\over3M^2},
\]

which is (AO.12). `square`

Using (AO.6), every outer-walk direction atom has mass at most

\[
\boxed{C_{atom}(\lambda).}
\tag{AO.13}
\]

At `lambda=0` this forces atomlessness, recovering the key qualitative conclusion of
§154 without Fourier-transform injectivity.

---

## 2. Heavy train atoms carry almost all quadratic crossing mass

Pass simultaneously to the train-phase subsequence of audited-working §142. Let the
limiting atomic train masses in **absolute `D` normalization** be

\[
a_i:=\lim {\#\{\text{trains in atom }i\}\over D}.
\]

Write

\[
A:=\sum_i a_i.
\]

The exact train ledger and the elementary bounds `h<=q<=pi D`, `f<=Q<=q` give

\[
T=h-s_Z+2f\le3\pi D,
\]

hence

\[
\boxed{A\le3\pi.}
\tag{AO.14}
\]

Audited-working §142 shows that the normalized strict-rhombus crossing measure has
total mass `Delta_2` and, in the limit, is carried by pairs of phase atoms at exact
projective separation `pi/3`. The exact relation graph is a disjoint union of
3-cycles. For every atom there are at most two possible neighboring atoms.

Fix `tau` as in (AO.2). Call an atom **heavy** if

\[
a_i\ge\tau.
\]

Let `H_tau` be the sum of all heavy atom masses.

The total crossing capacity of pairs having at least one light endpoint is at most

\[
3\tau A\le9\pi\tau.
\tag{AO.15}
\]

Indeed:

- heavy-light capacity is at most `2tau` times the total heavy mass, because each heavy
  atom has at most two relation neighbors and every light neighbor has mass `<tau`;
- light-light capacity is at most `tau` times the total light mass, because within one
  three-atom orbit
  \[
  ab+bc+ca\le\tau(a+b+c)
  \]
  whenever `a,b,c<tau`.

Thus heavy-heavy physical crossings have normalized mass at least

\[
\Delta_2-9\pi\tau.
\tag{AO.16}
\]

The heavy atomic crossing graph is triangle-free. Weighted Mantel therefore gives

\[
{H_\tau^2\over4}
\ge\Delta_2-9\pi\tau,
\]

so

\[
\boxed{
H_\tau\ge2\sqrt{\Delta_2-9\pi\tau}.
}
\tag{AO.17}
\]

The number `N_tau` of heavy atoms satisfies

\[
\boxed{
N_\tau\le{A\over\tau}\le{3\pi\over\tau}.
}
\tag{AO.18}

---

## 3. Heavy atomic train endpoints must be hosted somewhere

A complete stopped train has exactly two terminal edge occurrences. An outer terminal
edge has the same projective contact direction as its train.

For one heavy limiting train atom of mass `a_i`, take shrinking phase neighborhoods in
the usual order: first the source limit, then the neighborhood radius to zero. Its
outer terminal occurrences converge to an atom of `mu_out` at the same projective
direction. By Lemma AO.1 their normalized mass is at most
`C_atom(lambda)`.

Therefore bounded defect faces must absorb at least

\[
2a_i-C_{atom}(\lambda)
\]

normalized endpoint incidence from that heavy atom. Summing over all heavy atoms and
using (AO.17)–(AO.18),

\[
\begin{aligned}
\liminf {Q+4f\over D}
&\ge2H_\tau-N_\tau C_{atom}(\lambda)\\
&\ge
4\sqrt{\Delta_2-9\pi\tau}
-{3\pi\over\tau}C_{atom}(\lambda).
\end{aligned}
\]

This proves (AO.4).

No injection of trains into faces is used. Endpoint occurrences are counted with the
same multiplicity as the exact stopped-train handshake

\[
2T=b+Q+4f.
\]

---

## 4. Consequence for the loaded/interface scalar

The exact outer-walk ledger is

\[
b+Q=2(q-k).
\tag{AO.19}
\]

Since

\[
{b\over D}\to\pi+\lambda,
\]

\[
{Q\over D}=2{q-k\over D}-\pi-\lambda+o(1).
\tag{AO.20}
\]

Also `f<=Q`, so

\[
{Q+4f\over D}\le5{Q\over D}.
\]

Combining with (AO.4), every such subsequence satisfies

\[
\boxed{
\liminf {q-k\over D}
\ge
{\pi+\lambda\over2}
+{2\over5}\sqrt{\Delta_2-9\pi\tau}
-{3\pi\over10\tau}C_{atom}(\lambda)
}
\tag{AO.21}
\]

for every admissible `tau`.

At `lambda=0`, send `tau->0` and recover exactly the §154 zero-detour floor

\[
{q-k\over D}
\ge {\pi\over2}+{2\over5}\sqrt{\Delta_2}.
\]

For positive `lambda`, (AO.21) is an explicit continuous tradeoff between outer detour
and bounded-face endpoint capacity. It is intended to be combined with §§134–151,
not treated as a standalone closure.

---

## 5. Scope and audit targets

- All source points are retained.
- The theorem uses only Type-II width/perimeter convergence, audited-working §142, and
  the exact stopped-train endpoint handshake.
- Occurrence multiplicity is retained on the outer walk and bounded faces.
- The cusp lemma uses only positivity of the outer direction measure; it does not assume
  convexity of the old outer contact walk.
- `lambda` is the subsequential normalized excess `b-per(F)`; no pointwise finite-D
  value is substituted into the limiting formula.
- The quantitative exponent `1/6` mentioned after (AO.5) is only the scale obtained by
  balancing the two error terms; (AO.4) is the rigorous statement.
- The light-atom capacity estimate uses the fact that the exact `pi/3` phase relation
  has degree two on the projective phase circle.
- A hostile audit should verify the distributional cusp inequality and the
  heavy/light capacity count before this theorem is used downstream.

**Disposition:** proof-only research theorem pending hostile audit. C-II remains open.
