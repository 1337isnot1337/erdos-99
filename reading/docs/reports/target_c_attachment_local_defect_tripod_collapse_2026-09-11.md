> Generated reading edition · [exact source](../../../docs/reports/target_c_attachment_local_defect_tripod_collapse_2026-09-11.md) · source SHA-256 `817601e4fa23a111c242676b407cf2049fef153784333eb88138310fa091b63f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7475E8691B55","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact local attachment defect and three-attachment collapse

**Date:** 2026-09-11  
**Repository base:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** exact post-ZF local structure / component-capacity sharpening  
**Target:** Target C, C-II after ZF  
**Depends on:** C36 harmonic attachment containment, C42/C51 face convexity, ZJ incidence slacks, ZK pinned-component rank/nullity  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`.

For one unloaded component `I_r`, let `A_r` be its distinct loaded attachment set and
`a_r=|A_r|>=3`.  This report proves an exact local Euler/stress identity that was not
present in the current report stack:

$$
\boxed{
2(a_r-3)
=d_r+Q_r^{\rm loc}+2s_r+c_r^\partial+2c_r^{\rm ch}.
}
\tag{LA.1}
$$

All terms on the right are nonnegative and have direct geometry.  In particular,

$$
\boxed{|A_r|=3\Longrightarrow I_r\text{ is exactly one degree-three tripod vertex}.}
\tag{LA.2}
$$

Thus the three-attachment components that dominate the old low-surplus normal form do
not need separate non-singleton or pinned-stress exception charges: three distinct
attachments already force the exact singleton tripod geometry.

The same identity gives

$$
\operatorname{per}(\operatorname{conv}A_r)\le4a_r-6,
\qquad
\operatorname{diam}(\operatorname{conv}A_r)\le2a_r-3,
\tag{LA.3}
$$

and an Oler component-population bound with leading quadratic coefficient
`8/(pi sqrt(3))`, replacing C40's much coarser coefficient `36` when one works in
attachment count rather than graph diameter.

These are finite exact statements.  They do not by themselves settle Level I.

---

## 1. Local notation

Fix one connected component `I=I_r` of the unloaded induced contact graph.  Write

- `n=|I|`;
- `A=A_r` for the distinct loaded vertices adjacent to `I`;
- `a=|A|>=3`;
- `e_I` for internal contact edges of `I`;
- `t` for contact edges from `I` to `A`;
- `c` for contact edges with both endpoints in `A`.

Let

$$
G_r=C[I\cup A].
\tag{1.1}
$$

C36 gives

$$
I\subseteq P:=\operatorname{conv}A.
\tag{1.2}
$$

Every vertex of `A` is an extreme vertex of the global force hull, so every vertex of
`A` remains an extreme vertex of `P` and the cyclic order is inherited from the force
hull.

Let `L` be the outer-face boundary-walk length of `G_r`, with bridge occurrences
counted with multiplicity.  Define

$$
Q^{\rm loc}:=
\sum_{F\text{ bounded face of }G_r}(\deg F-4)\ge0.
\tag{1.3}
$$

Triangle-freeness makes every bounded face walk have degree at least four.

ZK defines the component pinned-stress surplus

$$
\boxed{s:=e_I+t-2n-1\ge0.}
\tag{1.4}
$$

Globally, `sum_r s_r=s_C`.

---

## 2. Exact local face/stress identity

The local graph `G_r` is connected and has

$$
V=n+a,
\qquad
E=e_I+t+c=2n+1+s+c.
\tag{2.1}
$$

Euler gives `F_b=E-V+1` bounded faces.  Face incidence gives

$$
2E=L+4F_b+Q^{\rm loc}.
\tag{2.2}
$$

Eliminate `F_b`:

$$
E=2(n+a)-2-\frac{L+Q^{\rm loc}}2.
\tag{2.3}
$$

Equating (2.1) and (2.3) proves

### Theorem LA.1 — local outer-walk identity

$$
\boxed{
L+Q^{\rm loc}+2s+2c=4a-6.
}
\tag{LA.4}
$$

No Eppstein bound is used.  The identity uses the actual pinned left-nullity, not only
a lower bound on the number of contact rows.

---

## 3. Resolve the outer walk into genuine geometric defects

Split the attachment-attachment contacts as

$$
c=c^\partial+c^{\rm ch},
\tag{3.1}
$$

where `c^partial` counts contacts that are sides of the convex polygon `P`, and
`c^ch` counts the remaining attachment-attachment contact chords.

Between two consecutive vertices of `A` on `partial P`, the outer walk of `G_r` uses
exactly one edge only when that hull side itself is a contact.  Otherwise it uses at
least two edge occurrences.  Hence

$$
L\ge2a-c^\partial.
\tag{3.2}
$$

Define the exact nonnegative detour slack

$$
\boxed{d:=L-(2a-c^\partial)\ge0.}
\tag{3.3}
$$

Substitute `L=2a-c^partial+d` and (3.1) in LA.4.  This gives the main identity.

### Theorem LA.2 — exact attachment-defect decomposition

$$
\boxed{
2(a-3)
=d+Q^{\rm loc}+2s+c^\partial+2c^{\rm ch}.
}
\tag{LA.5}
$$

Every term is nonnegative.  Therefore

$$
\boxed{s\le a-3.}
\tag{LA.6}
$$

The identity is sharper than combining C40's `t>=delta+3` with a loaded-degree bound:
it directly resolves attachment count into outer detour, local face defect, pinned
stress redundancy, and loaded-loaded contacts.

---

## 4. Attachment count directly controls Euclidean cell size

The image of the outer boundary walk contains every extreme point of `P`, so its convex
hull is exactly `P`.  The closed-walk perimeter lemma used in OP therefore gives

$$
\operatorname{per}P\le L.
\tag{4.1}
$$

LA.4 gives `L<=4a-6`, hence

$$
\boxed{\operatorname{per}P\le4a-6.}
\tag{LA.7}
$$

For every convex body, `per(P)>=2 diam(P)`: project the two boundary arcs joining a
diameter pair onto the diameter direction; each arc has length at least the diameter.
Thus

$$
\boxed{\operatorname{diam}P\le2a-3.}
\tag{LA.8}
$$

This is a Euclidean bound on the entire harmonic attachment cell from the number of
distinct pins alone.

Oler applied to the `n+a` unit-separated points of `I union A` in `P` gives

$$
\frac{\sqrt3}{2}(n+a-1)
\le\operatorname{area}P+\frac{\sqrt3}{4}\operatorname{per}P.
\tag{4.2}
$$

Use the isoperimetric inequality and LA.7:

$$
\operatorname{area}P\le\frac{(4a-6)^2}{4\pi}.
$$

After division by `sqrt(3)/2`,

$$
\boxed{
n
\le
\frac{(4a-6)^2}{2\pi\sqrt3}+a-2.
}
\tag{LA.9}
$$

The leading coefficient is

$$
\frac8{\pi\sqrt3}=1.4702\ldots,
$$

whereas C40's attachment-only consequence `(6a-5)^2` has leading coefficient `36`.
The two estimates use different mechanisms; LA.9 is useful when attachment count is the
available currency.

---

## 5. Three attachments force zero local defect

Assume now

$$
a=3.
\tag{5.1}
$$

LA.5 has zero left side, so every term on the right vanishes:

$$
\boxed{
d=Q^{\rm loc}=s=c^\partial=c^{\rm ch}=0.}
\tag{5.2}
$$

In particular

$$
L=6,
\qquad c=0.
\tag{5.3}
$$

Let the three attachments be `A,B,C` in cyclic order.  Since no attachment pair is a
contact, each of the three outer-walk portions between consecutive attachments has at
least two edges.  Their total is six, hence each has exactly two edges:

$$
A-x-B,
\qquad
B-y-C,
\qquad
C-z-A,
\tag{5.4}
$$

for `x,y,z in I`.

We next prove these three intermediate vertices coincide.

---

## 6. Geometric two-edge tripod lemma

### Lemma LA.3

Under (5.4),

$$
\boxed{x=y=z.}
\tag{LA.10}
$$

### Proof

It is enough to prove `x=y`; the other equalities follow cyclically.

Put

$$
c=|AB|,
\qquad a_1=|BC|.
$$

There are no attachment contacts, while the two-edge paths in (5.4) give

$$
1<c,a_1\le2.
\tag{6.1}
$$

Define

$$
\alpha=\arccos(c/2),
\qquad
\gamma=\arccos(a_1/2),
\qquad
B_0=\angle ABC.
\tag{6.2}
$$

Thus

$$
0\le\alpha,\gamma<\pi/3.
\tag{6.3}
$$

Because `x,y in I subset triangle ABC`, the ray `Bx` lies inside angle `ABC` at
base angle `alpha` from `BA`, while `By` lies at base angle `gamma` from `BC`.
Therefore

$$
\angle xBy=|B_0-\alpha-\gamma|.
\tag{6.4}
$$

If `B_0<alpha+gamma`, containment of both rays in the angle at `B` gives
`alpha<=B_0` and `gamma<=B_0`, hence

$$
\angle xBy=\alpha+\gamma-B_0
\le\min\{\alpha,\gamma\}<\pi/3.
$$

Since `|Bx|=|By|=1`, distinct `x,y` would then have `|x-y|<1`, impossible.

Assume therefore `x!=y` and `B_0>=alpha+gamma`.  Unit separation gives
`angle xBy>=pi/3`, while equality would make `Bxy` a unit equilateral triangle.
Triangle-freeness therefore forces

$$
B_0>\alpha+\gamma+\pi/3.
\tag{6.5}
$$

We show that already at the boundary value

$$
B_*=\alpha+\gamma+\pi/3
$$

the opposite side `AC` has length at least two.

Set

$$
u=\tan\alpha,
\qquad v=\tan\gamma,
\qquad 0\le u,v<\sqrt3.
\tag{6.6}
$$

Using `AB=2 cos alpha`, `BC=2 cos gamma`, the cosine law at angle `B_*` simplifies
exactly to

$$
\boxed{
\frac{(|AC|^2-4)(1+u^2)(1+v^2)}4
=\sqrt3(u+v)+uv-u^2v^2.
}
\tag{6.7}
$$

The right side is nonnegative.  If `uv<=1`, this is immediate.  If
`1<uv<3`, put `w=uv`.  AM-GM gives

$$
\sqrt3(u+v)\ge2\sqrt{3w},
$$

while

$$
w(w-1)\le2\sqrt{3w}
$$

because this is equivalent after squaring to

$$
w(w-1)^2\le12,
$$

and `w(w-1)^2` is increasing on `[1,3]` with value `12` at `3`.
Thus (6.7) gives `|AC|>=2` at `B_*`.

For fixed adjacent sides `AB,BC`, the cosine law shows `|AC|` is strictly increasing
with the included angle on `(0,pi)`.  Equation (6.5) therefore gives

$$
|AC|>2.
$$

But (5.4) contains the two-unit-edge path `C-z-A`, so `|AC|<=2`, a contradiction.
Hence `x=y`.  Cyclic repetition proves `x=y=z`. `square`

---

## 7. No additional component vertex can exist

Write

$$
p:=x=y=z.
$$

Then

$$
|p-A|=|p-B|=|p-C|=1.
\tag{7.1}
$$

Therefore the attachment triangle is contained in the closed unit disk centered at
`p`:

$$
\operatorname{conv}\{A,B,C\}\subseteq\overline B(p,1).
\tag{7.2}
$$

C36 gives `I subset conv{A,B,C}`.  If another `w in I`, `w!=p`, existed, unit
separation from `p` would require `|w-p|>=1`; (7.2) gives the reverse inequality.
Equality in the strictly convex Euclidean disk is possible for a convex combination of
`A,B,C` only at one of the three circle points themselves.  Since `w` is unloaded and
therefore distinct from `A,B,C`, equality is impossible.  Thus

$$
I=\{p\}.
\tag{7.3}
$$

Together with (5.4):

### Theorem LA.4 — exact three-attachment collapse

$$
\boxed{
|A_r|=3
\Longrightarrow
I_r=\{p\},\quad
N_C(p)=A_r,\quad
\deg_C(p)=3,\quad
s_r=0.
}
\tag{LA.11}
$$

The attachment triangle has circumradius one with circumcenter `p`; positive contact
equilibrium places `p` in its interior, so the familiar acute tripod geometry follows.

---

## 8. Global cross-ledger with pinned surplus eliminated

Let

$$
u_A:=\sum_r(a_r-3).
$$

Summing LA.5 and using `sum_r s_r=s_C` gives

$$
\boxed{
 u_A-s_C
 =\frac12\sum_r d_r
 +\frac12\sum_rQ_r^{\rm loc}
 +\frac12\sum_rc_r^\partial
 +\sum_rc_r^{\rm ch}.
}
\tag{8.1}
$$

For `c_I>0`, ZJ gives

$$
e_{BB}+s_C-k=u_A+p_A+2(s_{inc}-1)+u_0,
\qquad k=d_H+s_Z.
\tag{8.2}
$$

Substitute (8.1):

$$
\boxed{
\begin{aligned}
e_{BB}-k={}&
\frac12\sum_r d_r
+\frac12\sum_rQ_r^{\rm loc}
+\frac12\sum_rc_r^\partial
+\sum_rc_r^{\rm ch}\\
&+p_A+2(s_{inc}-1)+u_0.
\end{aligned}
}
\tag{LA.12}
$$

PC gives independently

$$
e_{BB}=d_P+Q+2k+c_B.
$$

Therefore

$$
\boxed{
\begin{aligned}
d_P+Q+k+c_B={}&
\frac12\sum_r d_r
+\frac12\sum_rQ_r^{\rm loc}
+\frac12\sum_rc_r^\partial
+\sum_rc_r^{\rm ch}\\
&+p_A+2(s_{inc}-1)+u_0.
\end{aligned}
}
\tag{LA.13}
$$

This is an exact equality between global boundary/face/diameter defect and actual local
attachment-cell defect.  The abstract pinned surplus `s_C` cancels completely.

---

## 9. Scope and regressions

- The three-attachment theorem does **not** say every unloaded component has three
  attachments.  Components with `a_r>=4` remain live.
- LA.9 is a cell-capacity estimate, not a global force-bulk theorem.  A linear number
  of attachment pins can still support a quadratic cell population.
- No lower area gap per exceptional face is used.
- The exact `a=3` proof permits the limiting near-equilateral degeneracies that defeat
  any uniform pentagon/rhombus area-gap shortcut; it uses only strict unit separation
  and exact triangle-freeness.
- Contact-isolated source points outside the positive core are untouched.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For unloaded component I_r with a_r distinct loaded attachments, form the local contact
graph on I_r union A_r.  Let L_r be its outer-walk length, Q_r^loc its bounded-face
4-defect, s_r its pinned left-nullity surplus, and c_r the attachment-attachment
contacts.  Euler plus e_r+t_r=2n_r+1+s_r gives exactly
    L_r+Q_r^loc+2s_r+2c_r=4a_r-6.
Writing c_r=c_r^partial+c_r^ch and
    d_r=L_r-(2a_r-c_r^partial)>=0
gives
    2(a_r-3)=d_r+Q_r^loc+2s_r+c_r^partial+2c_r^ch.

Consequences:
    per(conv A_r)<=4a_r-6,
    diam(conv A_r)<=2a_r-3,
    n_r<=(4a_r-6)^2/(2pi sqrt3)+a_r-2.

If a_r=3, every defect vanishes and L_r=6.  The three outer boundary pieces are
A-x-B, B-y-C, C-z-A.  Unit separation plus the exact cosine-law argument forces
x=y=z=p.  Since I_r lies in triangle ABC and that triangle lies in the unit disk
centered at p, no other component vertex can exist.  Hence every three-attachment
component is exactly one degree-three tripod and has s_r=0.

Summing the local identity and substituting ZJ/PC eliminates s_C and yields LA.12-LA.13,
an exact local/global defect balance.
```
