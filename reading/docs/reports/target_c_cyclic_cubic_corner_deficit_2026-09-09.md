> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_cubic_corner_deficit_2026-09-09.md) · source SHA-256 `5a2f9d871a7cd68c699583beafdb3cf408f0370049d2217478e319b03e38e456`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-34FEC7B121DE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cubic Reuleaux-corner deficit forces `O(D^(2/3))` diameter branching

**Date:** 2026-09-09  
**Run type:** exact support-function stability / cyclic source theorem  
**Target:** Target C C-II cyclic `d_H=0` equality endpoint  
**Depends on:** MR exact Reuleaux composition and area bridge; CA/CY complete-source Oler lower bound; standard support-function area formula, derived below  
**External web search:** not used in the proof  
**Computation:** decimal evaluation only

## LEVEL I STATUS

`STILL OPEN`

MR reduces the exact `d_H=0` shell to a Reuleaux composition

$$
\ell_0+\cdots+\ell_{r-1}=q,
\qquad
\ell_i\in\mathbb Z_{>0},
\qquad
r\text{ odd},
$$

where the Reuleaux side centered at the corresponding diameter-cycle vertex has angular length

$$
\phi_i=\ell_i\frac\pi q.
$$

The missing quantitative input is a penalty for one anomalously long Reuleaux side. A direct support-function argument gives the cubic estimate

$$
\boxed{
\frac{\pi D^2}{4}-\operatorname{area}(R)
\ge
\frac{2D^2\phi^3}{\pi^2(\pi^2-\phi^2)}
>
\frac{2D^2\phi^3}{\pi^4}
}
\tag{CC.1}
$$

for every side of angular length `phi` in any Reuleaux polygon `R` of width `D`.

Applying this to the unique-cycle Reuleaux completion `R_Gamma`, while MR and complete-source Oler give only `O(D)` total area deficit, yields

$$
\boxed{
\phi_{\max}^3
<
\frac{\sqrt3\,\pi^4 q}{8D^2}.
}
\tag{CC.2}

Equivalently,

\[
\boxed{
\ell_{\max}^3
<
\frac{\sqrt3\,\pi}{8}
\frac{q^4}{D^2}.
}
\tag{CC.3}

Since `q<=pi D`,

\[
\boxed{
\ell_{\max}
<
\left(\frac{\sqrt3\,\pi^5}{8}\right)^{1/3}D^{2/3}
=
4.0464421382\ldots D^{2/3}.
}
\tag{CC.4}

MR gives

\[
\deg_H(v_i)=\ell_i+1
$$

at every diameter-cycle vertex, while every off-cycle vertex is a diameter leaf. Therefore

$$
\boxed{
\Delta(H)
<
4.0464421382\ldots D^{2/3}+1.
}
\tag{CC.5}

This is the first sublinear **explicit** branch-degree bound intrinsic to the exact Reinhardt endpoint. It improves the `O(D^{3/4})` scale obtained by combining generic near-disk Bonnesen stability with the primitive-cyclic `O(1/D)` normalized area deficit.

---

## 1. Support-function setup for a constant-width body

Let `R` be a planar convex body of constant width `D`. Write its support function as

\[
h(\theta),
\qquad 0\le\theta<2\pi.
$$

Constant width is exactly

$$
\boxed{
h(\theta)+h(\theta+\pi)=D.}
\tag{1.1}

Put

\[
\boxed{p(\theta):=h(\theta)-\frac D2.}
\tag{1.2}

Then

\[
\boxed{p(\theta+\pi)=-p(\theta).}
\tag{1.3}

Thus `p` is antiperiodic and has only odd Fourier modes. Its first harmonic is the arbitrary choice of origin/translation and will lie in the kernel of the energy below.

For a piecewise `C^2` strictly convex body such as a Reuleaux polygon, the standard support-function area formula is

\[
\boxed{
A(R)
=\frac12\int_0^{2\pi}
\left(h^2-(h')^2\right)d\theta.
}
\tag{1.4}

For completeness, on every smooth support interval the boundary parametrization is

\[
x(\theta)=h(\theta)u(\theta)+h'(\theta)u^\perp(\theta),
$$

so

$$
x'(\theta)=(h+h'')u^\perp.
$$

Then `A=(1/2) int det(x,x') dtheta`, and one integration by parts gives (1.4). The finitely many Reuleaux transition angles do not affect the integral; the formula extends across them by piecewise integration.

Since antiperiodicity gives

$$
\int_0^{2\pi}p=0,
$$

substituting `h=D/2+p` into (1.4) yields

$$
\boxed{
\delta(R)
:=
\frac{\pi D^2}{4}-A(R)
=
\frac12\int_0^{2\pi}
\left((p')^2-p^2\right)d\theta.
}
\tag{1.5}

---

## 2. Curvature forcing on a Reuleaux side

Define the radius-of-curvature density, in support coordinates,

\[
\rho=h+h''.
\tag{2.1}

For a Reuleaux polygon this is piecewise constant almost everywhere:

- on the normal interval corresponding to a circular side of radius `D`,
  \[
  \rho=D;
  $$
- on the antipodal normal interval corresponding to the opposite vertex, constant-width duality gives
  $$
  \rho=0.
  $$

Indeed differentiating (1.1) twice in the distributional/piecewise sense gives

$$
\boxed{
\rho(\theta)+\rho(\theta+\pi)=D.
}
\tag{2.2}

Put

\[
\boxed{f:=\rho-\frac D2=p+p''.}
\tag{2.3}

Thus `f` is also antiperiodic.

Suppose one Reuleaux side has angular/normal length

\[
0<\phi<\pi.
$$

After rotating the angular parameter, write its normal interval as

$$
I=\left(-\frac\phi2,\frac\phi2\right).
$$

Then almost everywhere

$$
\boxed{
f=\frac D2\text{ on }I,}
\tag{2.4}

and by (2.2)

\[
\boxed{
f=-\frac D2\text{ on }I+\pi.}
\tag{2.5}

Nothing is assumed about `f` on the remaining normal directions.

---

## 3. The disk deficit is an `H^{-1}` energy

On the antiperiodic space define

\[
L:=-\frac{d^2}{d\theta^2}-1.
\tag{3.1}

Its Fourier eigenvalues on odd mode `n` are

\[
n^2-1.
$$

The `n=1` translation modes form the kernel; every odd mode `n>=3` has strictly positive eigenvalue.

Equation (2.3) is

$$
\boxed{Lp=-f.}
\tag{3.2}

The function `f` is automatically orthogonal to the translation kernel. Modulo that kernel,

\[
p=-L^{-1}f.
$$

Equation (1.5) becomes

$$
\boxed{
\delta(R)
=\frac12\langle f,L^{-1}f\rangle.
}
\tag{3.3}

Equivalently, for every antiperiodic `H^1` test function `g`, Cauchy--Schwarz in the `L` energy gives

\[
\boxed{
\langle f,g\rangle^2
\le
2\delta(R)
\int_0^{2\pi}\left((g')^2-g^2\right)d\theta.
}
\tag{3.4}

If `g` has a first-harmonic component, subtracting that component changes neither side: `f` is orthogonal to it and its `L` energy is zero. Thus (3.4) applies to the explicit test below without any centering convention.

---

## 4. A localized cosine test gives the cubic penalty

Define an antiperiodic test function supported only on the forced side/opposite-vertex intervals:

\[
g(\theta)
=
\begin{cases}
\cos(\pi\theta/\phi),&\theta\in I,\\
-\cos(\pi(\theta-\pi)/\phi),&\theta\in I+\pi,\\
0,&\text{otherwise},
\end{cases}
\tag{4.1}

extended `2pi`-periodically.

It is continuous, belongs to `H^1`, and satisfies

\[
g(\theta+\pi)=-g(\theta).
$$

Using (2.4)-(2.5),

$$
\begin{aligned}
\langle f,g\rangle
&=2\cdot\frac D2
\int_{-\phi/2}^{\phi/2}
\cos(\pi\theta/\phi)d\theta\\
&=D\cdot\frac{2\phi}{\pi}.
\end{aligned}
$$

Hence

$$
\boxed{
\langle f,g\rangle
=\frac{2D\phi}{\pi}.
}
\tag{4.2}

On one interval,

\[
\int_I g^2=\frac\phi2,
\qquad
\int_I(g')^2=\frac{\pi^2}{2\phi}.
$$

There are two antipodal copies, so

$$
\boxed{
E(g):=
\int_0^{2\pi}\left((g')^2-g^2\right)d\theta
=\frac{\pi^2}{\phi}-\phi
=\frac{\pi^2-\phi^2}{\phi}.
}
\tag{4.3}

Insert (4.2)-(4.3) into (3.4):

\[
\frac{4D^2\phi^2}{\pi^2}
\le
2\delta(R)
\frac{\pi^2-\phi^2}{\phi}.
$$

Therefore

$$
\boxed{
\delta(R)
\ge
\frac{2D^2\phi^3}{\pi^2(\pi^2-\phi^2)}.
}
$$

Since `0<phi<pi`,

$$
\pi^2(\pi^2-\phi^2)<\pi^4,
$$

so

$$
\boxed{
\delta(R)
>
\frac{2D^2\phi^3}{\pi^4}.
}
\tag{4.4}

This proves CC.1.

The cubic exponent is the natural localization scale: the forced curvature imbalance has amplitude `Theta(D)`, support length `phi`, and `H^{-1}` energy `Theta(D^2 phi^3)`.

---

## 5. Apply to the primitive cyclic Reuleaux completion

Let `R_Gamma` be the Reuleaux polygon determined by the unique odd diameter cycle.

MR gives the exact area bridge

\[
A(R_\Gamma)-A(F)
=
S_q
:=
\frac{qD^2}{2}
\left(
\frac\pi q-\sin\frac\pi q
\right)>0.
\tag{5.1}

Complete-source Oler plus global strict minimality gives

\[
A(F)
>
\frac\pi4D^2-rac{\sqrt3}{4}q.
\tag{5.2}

Therefore

\[
\begin{aligned}
\delta(R_\Gamma)
&=\frac\pi4D^2-A(R_\Gamma)\\
&<\frac{\sqrt3}{4}q-S_q\\
&<\frac{\sqrt3}{4}q.
\end{aligned}
\tag{5.3}

Let

\[
\phi_{\max}=\max_i\phi_i.
$$

Apply the weak form (4.4) of CC.1 to a longest side:

$$
\frac{2D^2\phi_{\max}^3}{\pi^4}
<
\frac{\sqrt3}{4}q.
$$

Hence

$$
\boxed{
\phi_{\max}^3
<
\frac{\sqrt3\,\pi^4q}{8D^2}.
}
$$

This proves CC.2. Retaining `S_q` and the exact denominator in CC.1 gives a strictly stronger finite inequality if needed.

---

## 6. Composition and diameter-degree bound

MR gives

$$
\phi_i=\ell_i\frac\pi q.
$$

Thus CC.2 gives

$$
\ell_{\max}^3
\frac{\pi^3}{q^3}
<
\frac{\sqrt3\,\pi^4q}{8D^2},
$$

so

$$
\boxed{
\ell_{\max}^3
<
\frac{\sqrt3\,\pi}{8}
\frac{q^4}{D^2}.
}
$$

This proves CC.3.

Cauchy's perimeter-diameter inequality gives

$$
q=\operatorname{per}(F)\le\pi D.
$$

Therefore

$$
\ell_{\max}^3
<
\frac{\sqrt3\,\pi}{8}\pi^4D^2
=
\frac{\sqrt3\,\pi^5}{8}D^2,
$$

and

$$
\boxed{
\ell_{\max}
<
\left(\frac{\sqrt3\,\pi^5}{8}\right)^{1/3}D^{2/3}.
}
$$

Numerically the coefficient is

$$
4.0464421382\ldots .
$$

At a unique-cycle vertex MR gives

$$
\deg_H(v_i)=\ell_i+1.
$$

Every off-cycle diameter vertex is a leaf. Hence

$$
\boxed{
\Delta(H)\le\ell_{\max}+1
<4.0464421382\ldots D^{2/3}+1.
}
$$

This proves CC.4-CC.5.

---

## 7. Comparison with the previous near-disk degree scale

CA plus full-source Oler gives normalized area deficit

$$
\xi=\frac\pi4-\frac{A(F)}{D^2}=O(D^{-1}).
$$

The generic ND Bonnesen/antipodal theorem gives a diameter-degree bound at scale

$$
O(D\xi^{1/4})=O(D^{3/4}).
$$

CC uses the exact constant-width Reuleaux side structure, rather than only an annular approximation, and improves the exponent to

$$
\boxed{2/3.}
$$

This is genuine new information about the cyclic equality phase.

---

## 8. Additional consequences

### 8.1 Every pendant block is sublinear

Since

$$
p_i=\ell_i-1,
$$

no diameter-cycle vertex carries more than

$$
O(D^{2/3})
$$

pendant leaves.

### 8.2 The odd cycle has at least `Omega(D^(1/3))` vertices from composition alone

Because

$$
q=\sum_i\ell_i
\le r\ell_{\max},
$$

and `q=Theta(D)`, CC gives

$$
r=\Omega(D^{1/3}).
$$

This is weaker than the sharper `Omega(sqrt D)` area-girth theorem CG, but it is obtained from pointwise branch control and remains useful locally.

### 8.3 No macroscopic diameter hub survives

For every fixed `epsilon>0`, eventually

$$
\Delta(H)<\epsilon D.
$$

Thus the exact cyclic equality shell is quantitatively far from every diameter-star or finite-hub model.

---

## 9. Regression audit

- The support-function proof handles the Reuleaux polygon piecewise; no smoothness beyond piecewise `C^2`/`H^1` support is assumed.
- Translation first harmonics lie in the kernel of `L`; the test inequality is invariant under subtracting them.
- Only one forced Reuleaux side and its antipodal zero-curvature interval are used. The behavior on all other arcs is unrestricted.
- The upper deficit bound uses complete-source Oler and MR; no unproved general formula for irregular Reuleaux area is imported.
- The exponent `2/3` is rigorous but not claimed optimal. A sharper localized test or use of the full bang-bang curvature pattern may improve the constant or exponent.

---

## 10. Next target

CC converts the Reinhardt composition from a merely finite/arithmetic object into a uniformly sublinear local structure:

```text
r = Omega(sqrt D),
max ell_i = O(D^(2/3)),
q=sum ell_i ~ pi D,
KKT polytope has exactly r extremes,
each extreme deletes the step-two pair of cycle edges.
```

The next high-value theorem is to combine these with the PP short-component circuits. Every short component now has at most `O(D^(2/3))` shell/contact span, while there are `Omega(sqrt D)` such moving components around a diameter-scale shell. A bounded-overlap response or rigidity argument may convert that moving family into a contradiction.

---

## 11. Compact handoff

```text
For any width-D Reuleaux polygon with a side normal interval I of length phi:
  h=D/2+p, p(theta+pi)=-p(theta),
  f=(h+h'')-D/2=p+p''.
On I, f=D/2; on I+pi, f=-D/2.
Disk deficit is
  delta=1/2 <f,(-d^2-1)^(-1)f>.
Test with the antiperiodic cosine bump supported on I and I+pi:
  <f,g>=2D phi/pi,
  E(g)=pi^2/phi-phi.
Thus
  delta >= 2D^2 phi^3/[pi^2(pi^2-phi^2)]
        > 2D^2 phi^3/pi^4.

For the cyclic completion R_Gamma, MR+Oler gives
  delta(R_Gamma)<sqrt(3)q/4.
Therefore
  phi_max^3 < sqrt(3) pi^4 q/(8D^2).
With phi_i=ell_i pi/q:
  ell_max^3 < (sqrt(3)pi/8) q^4/D^2.
Using q<=pi D:
  ell_max < 4.0464421382... D^(2/3),
and every diameter degree is <=ell_max+1.
```
