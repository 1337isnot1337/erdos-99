<!-- theorem-state: {"artifact_id":"ART-D780ED88A1B2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_nearcircle_total_harmonic_diameter_cost_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=cb52adb5ae2e86bcd988f6a228933487efb77373; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — near-circle cap area forces total harmonic graph diameter

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** asymptotic cap-cost theorem  
**Target:** UF near-circle harmonic-cell branch after LC/TR  
**Depends on:** repaired LC/TR maximal-cap decomposition, C44 attachment-diameter control, AR Oler cell-area lower bound  
**Computation:** decimal root evaluation only

## LEVEL I STATUS

`STILL OPEN`

LC/TR uses the inclusion-maximal attachment caps only to bound the **largest** component diameter. The same decomposition contains a stronger additive invariant.

Every inclusion-maximal cap is defined by one harmonic component. If the cap's normalized boundary chord has length `mu`, C44 forces that defining component to have graph diameter at least `mu D-O(1)`. Therefore macroscopic cap area has a direct additive cost in

\[
S:=\sum_r\delta_r.
\]

The cap area per diameter cost is strictly increasing, so the cheapest way to accommodate a prescribed total cell area is to concentrate that area into as many full semicircular caps as needed and at most one partial cap.

In the UF near-circle notation

\[
\frac{n-v}{D^2}\to\zeta,
\qquad
\Delta=\frac\pi{2\sqrt3},
\]

put

\[
A_\zeta:=\frac\pi4\left(1-\frac\zeta\Delta\right).
\]

Then

\[
\boxed{
\liminf\frac SD\ge\Sigma_{cap}(A_\zeta),
}
\tag{TD.1}
\]

where, since `0<=A_zeta<=pi/4`,

\[
\boxed{
\Sigma_{cap}(A)=
\begin{cases}
 f^{-1}(A),&0\le A\le\pi/8,\\
 1+f^{-1}(A-\pi/8),&\pi/8\le A\le\pi/4,
\end{cases}
}
\tag{TD.2}
\]

and

\[
\boxed{
f(\mu)=\frac14\left(\arcsin\mu-\mu\sqrt{1-\mu^2}\right),
\qquad 0\le\mu\le1.}
\tag{TD.3}
\]

At UF's worst crossover `zeta_*=0.5572837714...`,

\[
A_{\zeta_*}=0.3027762602\ldots<\pi/8,
\]

so

\[
\boxed{
\liminf\frac SD
\ge0.9835132379\ldots .
}
\tag{TD.4}
\]

At the asymptotically full-core endpoint `zeta=0`,

\[
\boxed{
\liminf\frac SD\ge2.
}
\tag{TD.5}
\]

Moreover equality at the full-core leading scale forces the maximal cap pattern to converge to two complementary semicircles, so there are two harmonic components whose graph diameters are each `(1-o(1))D`.

This substantially strengthens AR's total-diameter floor and CH/LC's one-component description, but it does not by itself contradict the loaded boundary contact budget `S<=pi D+o(D)`.

---

## 1. One circular cap and its diameter cost

Normalize the limiting force hull to the radius-`1/2` disk.

For a circular arc of central angle

\[
\theta\in[0,\pi],
\]

the chord length is

\[
\mu=\sin\frac\theta2\in[0,1],
\tag{1.1}
\]

and the circular-segment area is

\[
A_{cap}(\theta)
=\frac18(\theta-\sin\theta).
\tag{1.2}
\]

Writing `theta=2asin(mu)` gives

\[
\boxed{
A_{cap}=f(\mu)
=\frac14\left(\arcsin\mu-\mu\sqrt{1-\mu^2}\right).
}
\tag{1.3}
\]

The function is continuous, strictly increasing on `[0,1]`, with

\[
f(0)=0,
\qquad
f(1)=\frac\pi8.
\tag{1.4}
\]

Let one inclusion-maximal attachment interval be defined by a component `I_r`, and let its two extreme attachment terminals be `a,b`. If its normalized cap chord tends to `mu`, then

\[
|a-b|=(\mu+o(1))D.
\]

C44 gives

\[
\operatorname{diam}(A_r)\le\delta_r+2.
\]

Since `a,b in A_r`,

\[
\boxed{
\delta_r\ge\mu D-o(D)
}
\tag{1.5}
\]

for every macroscopic maximal cap.

---

## 2. Tiny caps can be removed without losing macroscopic area

There may be `O(D)` inclusion-maximal caps, so summing the finite `-2` error in C44 over all caps would be invalid at linear order. Instead separate the caps by angular size.

Fix `epsilon>0`. Call a maximal cap **large** if its normalized central angle satisfies

\[
\theta\ge\epsilon.
\]

Because the maximal cap arcs have disjoint interiors on the circle,

\[
N_{large}\le\frac{2\pi}{\epsilon}.
\tag{2.1}
\]

Thus the total finite C44 endpoint error over all large caps is `O_epsilon(1)=o(D)`.

For a small cap `theta<epsilon`,

\[
A_{cap}(\theta)=\frac18(\theta-\sin\theta)
\le\frac{\theta^3}{48}.
\]

Since the maximal arc lengths sum to at most `2pi`,

\[
\sum_{small}A_{cap}(\theta_j)
\le
\frac{\epsilon^2}{48}\sum_j\theta_j
\le
\frac{\pi}{24}\epsilon^2.
\tag{2.2}
\]

Therefore the small caps carry arbitrarily little normalized area as `epsilon->0`. All macroscopic area can be assigned to finitely many large caps, for which the additive graph-diameter cost (1.5) is valid without accumulated linear error.

---

## 3. The cap area per unit diameter cost is increasing

We need to minimize total chord cost

\[
\sum_j\mu_j
\]

subject to a required total cap area

\[
\sum_j f(\mu_j)\ge A,
\qquad
0\le\mu_j\le1,
\]

and the circle-angle budget

\[
\sum_j2\arcsin\mu_j\le2\pi.
\tag{3.1}
\]

The relevant efficiency ratio is

\[
\frac{f(\mu)}\mu.
\]

### Lemma TD.1

`f(mu)/mu` is strictly increasing on `(0,1]`.

### Proof

Put `mu=sin x`, `x in (0,pi/2]`. Then

\[
f(\sin x)=\frac14(x-\sin x\cos x).
\]

It is enough to show

\[
\frac{x-\sin x\cos x}{\sin x}
\]

is increasing. Differentiate. After multiplication by the positive factor `sin^2 x`, the numerator becomes

\[
2\sin^3x-\cos x(x-\sin x\cos x)
=
\sin x(1+\sin^2x)-x\cos x.
\]

Its derivative is

\[
3\sin^2x\cos x+x\sin x>0,
\]

and it vanishes at `x=0`. Hence it is positive for `x>0`. `square`

Thus larger caps provide strictly more area per unit chord/diameter cost.

---

## 4. Concentration minimizes total graph-diameter cost

Because `f(mu)/mu` increases, if two partial cap costs satisfy

\[
0<\mu_1\le\mu_2<1,
\]

then moving a small amount of diameter cost from `mu_1` to `mu_2` while keeping total cost fixed increases total cap area, until `mu_1=0` or `mu_2=1`.

Equivalently, for a prescribed required area, total cost is minimized by concentrating cap cost into full caps before opening another cap.

A full cap `mu=1` is a semicircle, with

\[
f(1)=\frac\pi8
\]

and angular cost `pi`. Two full caps exactly exhaust the circle angle budget and have total area `pi/4`, the whole disk.

Since the UF required area never exceeds `pi/4`, the optimizer is therefore:

- for `A<=pi/8`, one partial cap of chord `mu=f^{-1}(A)`;
- for `pi/8<A<=pi/4`, one full semicircle plus one partial cap with `f(mu)=A-pi/8`.

The angular constraint is automatically satisfied in both cases.

This proves the continuum cost formula TD.2.

---

## 5. Transfer to the source

The repaired LC/TR decomposition gives inclusion-maximal cap arcs whose interiors are disjoint, and all harmonic attachment cells are contained in their union. AR gives the lower area obligation

\[
\liminf
\frac1{D^2}\sum_r\operatorname{area}(P_r)
\ge A_\zeta.
\tag{5.1}
\]

The union of cells in one maximal group has area no larger than that maximal circular cap in the disk limit. By Section 2, after discarding caps of angular size below `epsilon`, the discarded normalized cap area is `O(epsilon^2)`, while the remaining number of caps is bounded independently of `D`.

For every remaining maximal cap `j`, let `mu_j` be its limiting normalized chord length. Its defining component contributes

\[
\delta_{r_j}/D\ge\mu_j-o(1).
\]

Hence

\[
\liminf\frac SD
\ge\sum_j\mu_j-o_epsilon(1).
\]

Their cap areas must total at least

\[
A_\zeta-O(\epsilon^2).
\]

Apply the continuum optimization of Section 4 and then let `epsilon->0`. This proves TD.1-TD.2.

---

## 6. UF crossover

At

\[
\zeta_*=0.5572837714\ldots,
\]

UF/AR gives

\[
A_{\zeta_*}
=0.302776260248\ldots
<\frac\pi8.
\]

Therefore the cost is one partial cap. The equation

\[
f(\mu)=0.302776260248\ldots
\]

has the unique solution

\[
\boxed{
\mu=0.9835132379\ldots .
}
\tag{6.1}
\]

Thus

\[
\boxed{
\liminf S/D\ge0.9835132379\ldots .
}
\]

This is substantially stronger than the first AR bound

\[
S/D\ge0.6208918647\ldots .
\]

It is also stronger than merely knowing one component has diameter `0.759166D`; it says the total harmonic graph-diameter cost is almost one full source diameter already at the worst UF population split.

---

## 7. Full-core endpoint

If

\[
\zeta=0,
\]

then

\[
A_0=\frac\pi4=2f(1).
\]

TD.2 gives

\[
\boxed{
\liminf S/D\ge2.
}
\]

Moreover the strict increase of `f(mu)/mu` shows that leading-order equality requires the cap-cost distribution to converge to two full caps `mu_1=mu_2=1`. Their arcs each have length `pi` and, because the maximal arcs have disjoint interiors and exhaust total angle `2pi`, they are complementary semicircles.

Thus any asymptotically full-core near-circle survivor contains two harmonic components `I_1,I_2` with

\[
\boxed{
\delta_1/D\to1,
\qquad
\delta_2/D\to1,
}
\tag{7.1}
\]

whose attachment hulls asymptotically occupy complementary semicircular caps.

This is a much sharper full-core normal form than CH's existence of one diameter-scale component.

---

## 8. Interaction with the exact post-ZF ledgers

AR gives

\[
S+R_I+s_B=x_B+Q+4-c_I+s_C.
\]

In the near-circle branch `x_B=o(D)`, TD therefore yields the additional necessary condition

\[
\boxed{
\liminf\frac{Q+s_C}{D}
\ge\Sigma_{cap}(A_\zeta).
}
\tag{8.1}
\]

This is independent of UF's direct lower bound on `Q`.

The loaded-degree/C40 budget and the mandatory direct hull-side contacts still give only

\[
S\le\pi D+o(D),
\]

so TD does not close the scalar system by itself.

For `zeta=0`, however, the survivor is reduced to two complementary diameter-scale harmonic components with total graph diameter at least `2D-o(D)`, plus UF's independent linear bounded-face defect. Future work can specialize to this two-cap geometry instead of an arbitrary harmonic-cell family.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| one maximal cap of chord `mu` costs `mu D-o(D)` graph diameter | proved | C44 on defining attachment endpoints |
| tiny cap total area `O(epsilon^2)` | proved | cubic circular-segment area + total arc budget |
| `f(mu)/mu` strictly increasing | proved | elementary derivative calculation |
| cap-cost optimizer TD.2 | proved | area-per-cost monotonicity + semicircle angle budget |
| crossover total cost `0.983513...D` | numerical evaluation of proved scalar equation | no proof depends on decimal |
| full-core two complementary diameter-scale components | proved asymptotically at leading equality | optimizer rigidity |
| Level I | still open | two dense half-disk components remain geometrically feasible at leading order |

---

## 10. Next target

The full-core endpoint is now exceptionally concrete:

```text
near-circle loaded hull
+ almost all hull intervals direct unit contacts
+ two harmonic components I_1,I_2
+ delta_1,delta_2 = (1-o(1))D
+ attachment hulls -> complementary semicircles
+ no contact edge between I_1 and I_2 after deleting B_+
+ complete diameter support near antipodal by NS/QR
+ Q = Omega(D) by UF.
```

The natural next theorem is a **two-semicircle interface stability theorem**: quantify the unavoidable boundary-order packing/contact loss along the common diameter interface between two positive harmonic components whose combined cells carry asymptotically full Oler density.

Such an interface theorem would attack the exact `O(D)` scale where the global problem remains open.
