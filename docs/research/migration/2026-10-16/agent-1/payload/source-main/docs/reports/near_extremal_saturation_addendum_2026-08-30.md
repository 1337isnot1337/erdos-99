<!-- theorem-state: {"artifact_id":"ART-A1B460424FB5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — same-hull saturation addendum to the near-extremal regression

**Date:** 2026-08-30
**Repository state:** `research/bhs-scale-activation-regression-2026-08-30`
**Run type:** exact regression / audit addendum
**Target:** A
**Depends on:** `near_extremal_activation_monomer_regression_2026-08-30.md`
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This addendum resolves the “same-hull saturation discriminator” posed in the preceding report. The answer is negative: the near-extremal regression can be made same-hull unit-covering saturated, in exactly the geometric sense used by canonical Theorem 63.1, while retaining its triangle-free contact graph and protected zero-nullity monomer core.

## 1. Starting point

The preceding report constructs, for every integer \(L\ge10\), a triangle-free unit-separated configuration \(A_L\) with

\[
D_L=2L,
\qquad
\left||A_L|-\frac{D_L^2}{c}\right|\le4D_L,
\qquad
0\le\pi D_L-P_L\le6\pi,
\]

where \(P_L\) is the perimeter of \(H_L=\operatorname{conv}A_L\), and with a persistent activation forest of rank \(|A_L|-O(D_L)\). Its protected patch shore has exact three-site monomer neighborhoods and a matching saturating that shore.

The open discriminator was whether same-hull saturation might force a new Hall obstruction absent from this regression.

## 2. Theorem: saturation still does not force the missing transport

> **Theorem 154 candidate (near-extremal same-hull saturated regression).**  For every integer \(L\ge10\), the configuration \(A_L\) from the preceding report has a finite extension
> \[
> A_L\subseteq\widehat A_L\subseteq H_L
> \]
> such that:
>
> 1. \(\widehat A_L\) is unit-separated and triangle-free;
> 2. \(\operatorname{conv}\widehat A_L=H_L\) and \(\operatorname{diam}\widehat A_L=D_L=2L\);
> 3. \(\widehat A_L\) is unit-covering saturated in its own hull:
>    \[
>    \boxed{
>    H_L\subseteq\bigcup_{p\in\widehat A_L}\overline B(p,1);
>    }
>    \tag{154.1}
>    \]
> 4. only boundary-order many points are added:
>    \[
>    \boxed{
>    |\widehat A_L\setminus A_L|
>    \le\left(4+\frac\pi2\right)D_L+1;
>    }
>    \tag{154.2}
>    \]
> 5. the unit-contact graph of \(\widehat A_L\) is exactly the unit-contact graph of \(A_L\); in particular every added point is a strict noncontact point;
> 6. the original activation forest therefore has rank
>    \[
>    \boxed{
>    \operatorname{rank}R_L
>    \ge
>    |\widehat A_L|
>    -\left(4+\frac\pi2+\frac2{\sqrt3}\right)D_L-23;
>    }
>    \tag{154.3}
>    \]
>    so the activation rank is still \(|\widehat A_L|-O(D_L)\); and
> 7. the protected patch points retain exactly the same three-site lattice conflict neighborhoods and the same injective matching as before, hence that coherent monomer subshore still has zero left transversal nullity.
>
> Consequently, even the conjunction
> \[
> \boxed{
> \begin{array}{c}
> n=D^2/c+O(D),\\
> \pi D-P=O(1),\\
> \text{same-hull unit-covering saturation},\\
> \operatorname{rank}R_{\rm act}=n-O(D),\\
> \text{triangle-free persistent activation},\\
> \text{protected coherent zero-nullity monomer core}
> \end{array}
> \not\Longrightarrow
> \text{the Target A Schur rank loss}
> }
> \tag{154.4}
> \]
> without an additional exact global-optimality/plateau/source-to-scaffold hypothesis.

### Proof

Start with \(A_L^{(0)}=A_L\). While there exists a point \(y\in H_L\) satisfying

\[
|y-p|>1
\qquad
\text{for every }p\in A_L^{(r)},
\tag{154.5}
\]

adjoin such a point and set

\[
A_L^{(r+1)}=A_L^{(r)}\cup\{y\}.
\]

The process terminates after finitely many insertions because \(H_L\) is bounded and a bounded planar set contains only finitely many mutually unit-separated points.

Let \(\widehat A_L\) be the terminal set. Every insertion is at strict distance greater than one from all existing points. Therefore no insertion creates a unit contact. In particular:

- unit separation is preserved;
- the unit-contact graph never changes;
- triangle-freeness is preserved; and
- every added point is incident to no unit edge.

Since every added point lies in \(H_L\) and the original set \(A_L\) is retained,

\[
\operatorname{conv}\widehat A_L
=\operatorname{conv}A_L
=H_L.
\tag{154.6}
\]

The original anchor pair remains at distance \(D_L\), while every pair in \(H_L\) is at distance at most \(D_L\). Hence

\[
\operatorname{diam}\widehat A_L=D_L.
\tag{154.7}
\]

At termination there is no \(y\in H_L\) with distance strictly greater than one from every point of \(\widehat A_L\). Equivalently, every \(y\in H_L\) lies in at least one closed unit disk centered at \(\widehat A_L\), proving (154.1). This is exactly the unit-covering saturation conclusion used in canonical Theorem 63.1; unlike that theorem, no global-optimality claim is made here.

It remains to bound the number of inserted points. Let

\[
\widehat n_L=|\widehat A_L|,
\qquad n_L=|A_L|.
\]

Oler's finite packing inequality applied to the convex hull \(H_L\) gives

\[
\widehat n_L
\le
\frac{\operatorname{area}H_L}{a_0}
+\frac{P_L}{2}+1.
\tag{154.8}
\]

Because \(\operatorname{diam}H_L=D_L\), the isodiametric inequality and Cauchy's perimeter inequality give

\[
\operatorname{area}H_L\le\frac{\pi D_L^2}{4},
\qquad
P_L\le\pi D_L.
\tag{154.9}
\]

Using \(a_0=\sqrt3/2\) and \(c=2\sqrt3/\pi\),

\[
\frac{1}{a_0}\frac{\pi D_L^2}{4}
=\frac{D_L^2}{c}.
\tag{154.10}
\]

Hence

\[
\widehat n_L
\le
\frac{D_L^2}{c}+\frac\pi2D_L+1.
\tag{154.11}
\]

The preceding report proves

\[
n_L\ge\frac{D_L^2}{c}-4D_L.
\tag{154.12}
\]

Subtracting yields

\[
|\widehat A_L\setminus A_L|
=\widehat n_L-n_L
\le
\left(4+\frac\pi2\right)D_L+1,
\]

which is (154.2).

The original activation forest has, by the preceding report,

\[
\operatorname{rank}R_L
\ge n_L-\frac2{\sqrt3}D_L-22.
\tag{154.13}
\]

Combining (154.2) and (154.13),

\[
\begin{aligned}
\operatorname{rank}R_L
&\ge
\widehat n_L
-|\widehat A_L\setminus A_L|
-\frac2{\sqrt3}D_L-22\\
&\ge
\widehat n_L
-\left(4+\frac\pi2+\frac2{\sqrt3}\right)D_L-23,
\end{aligned}
\]

proving (154.3).

Finally, the inserted points do not move any protected patch point or any lattice site in the auxiliary monomer conflict geometry. Therefore every protected patch point retains the same exact three lattice conflicts, and the old injective lower-left-vertex matching remains a matching saturating the protected patch shore. Its left transversal nullity remains zero.

This proves the theorem. \(\square\)

## 3. Exact consequence for Target A

The canonical saturation theorem for a genuine triangle-free global minimizer proves more than unit-covering saturation: every intermediate enlarged configuration is itself globally optimal at its new cardinality, so the whole enlargement lies on the same diameter plateau.

Theorem 154 shows that the purely geometric conclusion

\[
H\subseteq\bigcup_{p\in A}\overline B(p,1)
\]

is not the missing ingredient. The distinction that survives this regression is the **plateau-wise global-optimality content** of canonical Theorem 63.1, together with the later relation to the independently chosen smaller optimum and the plateau-terminalized Schur response.

Thus the activation route should no longer target “saturation + high rank implies nullity.” It must use at least one exact statement that fails for \(\widehat A_L\), for example:

\[
D(|\widehat A_L|)=D_L,
\]

an exact same-source plateau endpoint condition, the continuum source Hall inequality with the correct plateau slack, or a direct source-to-response transport.

## 4. Revised highest-value discriminator

The next clean question is now:

> **Plateau-optimality discriminator.** Can a family with the geometry of \(\widehat A_L\) be modified so that \(D(n)=D_L\) at its cardinality (or across a nontrivial same-diameter plateau) while retaining the protected zero-nullity monomer core? If not, identify an exact finite replacement certificate proving strict suboptimality and determine whether that certificate factors through the canonical Schur response.

This is materially narrower than the previous saturation question. Unit-covering saturation is now eliminated as the relevant distinction.

## 5. Promotion recommendation

**Promote regression only after independent audit.**

If both reports survive audit, they should be promoted together as one strengthened successor to Section 152, because the saturated extension is a direct corollary of the near-extremal construction and is the sharper no-go statement.

## 6. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New addendum:
The near-extremal Section-153 candidate regression can be extended inside the same hull
by repeatedly inserting points at distance >1 from the current set. The process ends
unit-covering saturated, creates no new unit contacts, remains triangle-free, keeps the
same hull and diameter, and adds at most (4+pi/2)D+1 points by Oler.

Therefore the protected activation rank is still n-O(D), and the protected exact
monomer core remains perfectly matchable with zero left nullity.

New no-go:
Same-hull unit-covering saturation, even together with n=D^2/c+O(D), pi D-P=O(1),
and almost-full activation rank, does not force the Target A Schur rank loss.

What still distinguishes a genuine source:
plateau-wise global minimum-diameter optimality, exact source Hall/plateau slack, and
the source-to-independent-scaffold coupling.

Highest-value next discriminator:
plateau optimality rather than saturation.
```
