> Generated reading edition · [exact source](../../../docs/audits/target_c_fullcore_loaded_chord_elimination_independent_audit_2026-09-14.md) · source SHA-256 `c525c80ab61ae7d1416c3850741c3a1a3671349eae688e9a88458a40482882d5`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-21A2AAE6BA75","canonical":true,"claim_ids":["C-FULLCORE-LOADED-CHORD"],"claim_statuses":{"C-FULLCORE-LOADED-CHORD":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — full-core loaded-chord elimination

**Date:** 2026-09-14
**Target:** Target C-II, full-core branch
**Audited artifact:** docs/reports/target_c_fullcore_loaded_chord_elimination_2026-09-14.md
**Base state:** 2026-09-14.audit.49
**Verdict:** PASS; promoted as the scoped canonical theorem
C-FULLCORE-LOADED-CHORD; no C-II or Level-I closure.

## Audited statement

Let $`F`$ be the actual loaded force hull in a canonical full-core Type-II
sequence, with $`D\to\infty`$, and assume the canonical near-disk conclusion
```math
 B(o_D,r_D)\subseteq F\subseteq B(o_D,R_D),
\qquad
\frac{r_D}{D},\frac{R_D}{D}\to\frac12.
\tag{A.1}
```
If $`p,q`$ are distinct vertices of $`F`$ which are unit-separated source
points, then, for all sufficiently large $`D`$, they are consecutive vertices
of $`F`$.

Consequently, if $`q_F`$ is the number of loaded hull vertices and $`m_B`$
is the number of nonunit sides of $`F`$, then
```math
c_B=0,\qquad e_{BB}=q_F-m_B.
\tag{A.2}
```
Here $`c_B`$ and $`e_{BB}`$ have the exact meanings in the canonical
loaded-hull ledger. No contact-isolated source point is removed or identified
with a loaded vertex.

## Proof audit

Translate by $`o_D`$. Write $`r=r_D`$, $`R=R_D`$, and let $`p,q`$ be a
unit chord of $`F`$. Since $`r\sim D/2`$, for large $`D`$ the radial angle
$`\gamma\in[0,\pi]`$ between $`p`$ and $`q`$ is $`<\pi/2`$. If
$`p=a e`$ and $`q=b f`$, with $`a,b\ge r`$, then
```math
 |p-q|^2=(a-b)^2+ab|e-f|^2
 \ge4r^2\sin^2(\gamma/2).
```
As $`|p-q|=1`$, this gives
```math
 \gamma\le2\arcsin\frac1{2r}=O(D^{-1}).
\tag{A.3}
```
The preliminary assertion $`\gamma<\pi/2`$ is forced because otherwise
$`|p-q|^2\ge2r^2>1`$.

Assume for contradiction that $`p,q`$ are nonconsecutive hull vertices.
Both cyclic boundary arcs then contain an intermediate hull vertex, so the
arc whose radial angle is $`\gamma`$ contains at least two side occurrences.
This uses only the cyclic order of the vertices; it does not identify repeated
vertices in a contact walk.

For every side occurrence on that short arc, choose an outward unit normal
$`n`$ and a point $`x`$ on the side. Since the inner disk in (A.1) lies in
$`F`$,
```math
n\cdot x=h_F(n)\ge r.
```
Since $`F\subseteq B(0,R)`$, $`|x|\le R`$. If $`e_x=x/|x|`$, then
```math
n\cdot e_x\ge\frac rR,
```
so the angle between $`n`$ and $`e_x`$ is at most
```math
\beta=\arccos(r/R)=o(1).
\tag{A.4}
```

Because $`0`$ is in the interior of $`F`$, the polar angle of a boundary
point is monotone as the boundary is traversed. Hence all radial directions
on the chosen arc lie in an interval of width at most $`\gamma`$. The
outward normals of all its side occurrences therefore lie in an interval
of width at most
```math
\tau_D:=\gamma+2\beta=o(1).
\tag{A.5}
```
Rotating normals by $`90^\circ`$ preserves angular widths, so the positively
oriented side vectors $`v_1,\ldots,v_\ell`$ on the arc lie in a cone of
width $`\tau_D`$. For large $`D`$, $`\tau_D<\pi/2`$.

Let $`w=(q-p)/|q-p|`$. Since
```math
q-p=\sum_{i=1}^{\ell}v_i
```
is a sum of vectors in one cone of width less than $`\pi/2`$, $`w`$ lies
in the same cone. Thus
```math
w\cdot v_i\ge |v_i|\cos\tau_D
```
for every $`i`$. Each side vector joins two distinct source points, so
$`|v_i|\ge1`$. Since nonconsecutivity gives $`\ell\ge2`$,
```math
1=|q-p|
 =w\cdot(q-p)
 =\sum_iw\cdot v_i
\ge \ell\cos\tau_D
\ge2\cos\tau_D>1,
```
a contradiction.

The argument remains valid for a nonsmooth convex polygon: the proof chooses
one outward normal for each side, and no differentiability of the boundary is
used. It also remains valid when the global contact boundary has bridges or
repeated vertices, because the theorem concerns the simple cyclic boundary of
the convex hull and counts no contact-walk occurrence.

Therefore every loaded-loaded unit chord is a side of $`F`$. By the canonical
definitions, the only loaded-loaded unit contacts not represented by unit
convex-hull sides are the $`c_B`$ extra chords. Hence $`c_B=0`$, and the
remaining $`q_F-m_B`$ unit hull sides give
```math
e_{BB}=q_F-m_B.
```
This proves (A.2).

## Exact ledger audit

The canonical loaded-hull identities are
```math
e_{BB}=q_F-m_B+c_B,
\qquad
c_I+e_{BB}+s_C=q_F-2+k,
\qquad
k=d_H+s_Z.
\tag{A.6}
```
Substitution of $`c_B=0`$ gives the exact finite identities
```math
s_C=m_B+k-2-c_I,
\tag{A.7}
```
and
```math
e_{BB}+2s_C-3k
 =q_F+m_B-k-4-2c_I.
\tag{A.8}
```
The canonical nonnegative payment $`e_{BB}\ge Q+2k`$ becomes
```math
q_F-m_B\ge Q+2k.
\tag{A.9}
```
All constant terms are retained in (A.7)--(A.8); dropping them is permitted
only after division by $`D`$ in an asymptotic statement.

If a subsequence has $`\mu_D\to1`$, with
```math
\mu_D=\frac{e_{BB}+2s_C-3k}{D},
```
and $`q_F/D\to q_0`$, $`m_B/D\to m_0`$, $`k/D\to k_0`$, then (A.8)--(A.9)
give
```math
1=q_0+m_0-k_0,
\qquad
q_0-m_0\ge2k_0,
```
and therefore
```math
q_0+3m_0\le2.
\tag{A.10}
```
The difference-body floor $`q_F/D\ge h/D`$ and
```math
\liminf h/D\ge2\rho,\qquad \rho=\cos\rho,
```
then imply
```math
\liminf\frac{s_Z}{D}
\ge m_0+2\rho-1
\ge2\rho-1.
\tag{A.11}
```
This is a genuine endpoint narrowing but not a contradiction.

## Scope and regressions

The theorem is only for the canonical full-core near-disk branch. It does not
apply to the macroscopic-container branch, to a general convex polygon far
from a disk, or to an abstract scaffold whose vertices are not the loaded
source points.

The regular-shell and vanishing-shear regressions are compatible with (A.2):
their loaded unit contacts are hull sides. They do not provide global
minimum-diameter certificates. Contact-isolated source points remain outside
the loaded-hull counts. No Euler path is inferred from diameter edges, and no
affine-kernel extension is used.

The high-$`s_Z`$ implication
```math
s_Z\ge(2\rho-1-o(1))D
\Longrightarrow
\text{exact triangle or source-preserving strict decrease}
```
is not proved. The Section-122 aggregate detour and the Type-I branch remain
unresolved.

## Promotion verdict

The loaded-chord theorem is promoted as
C-FULLCORE-LOADED-CHORD in state 2026-09-14.audit.49. Its scope is only the
canonical full-core near-disk branch. The high-$`s_Z`$ bridge, the
macroscopic-container branch, C-II, and Level I remain open.
