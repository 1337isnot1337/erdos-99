<!-- theorem-state: {"artifact_id":"ART-FF6F95A6BC7A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- arbitrary block transposition inside one open witness cell

Date: 2026-10-01  
Base branch dependency: 97660698eb4b1893f69cc13f11de557d1598f903  
Status: proof-only; C-II remains open.

## Theorem

Work in the fixed-star complete global O--O rectangle. Fix one shore after the
common-witness-cell extraction, and assume its retained train directions lie in one
open cell \(J\) between two consecutive global actual-diameter directions.

Order the retained O--O trains along their complement-dual path. Let
\(\tau_p,\tau_q\), \(p<q\), be any two retained trains with distinct projective
directions. Choose the coherent lift in \(J\), and write their unit directions as
\(u_p,u_q\). Translate the entire physical slab between their two train cuts by

\[
\Delta:=u_q-u_p.
\tag{1}
\]

Put

\[
\varepsilon=d_{\mathbb{RP}^1}([u_p],[u_q])>0,
\qquad
s:=|\Delta|=2\sin{\varepsilon\over2},
\qquad
w:={u_p-u_q\over s},
\tag{2}
\]

so \(\Delta=-sw\). Since the whole retained shore lies in a Section-90 window,

\[
0<s\le\varepsilon\le {4K\over D}.
\tag{3}
\]

Then:

1. every old unit contact is preserved exactly;
2. the two boundary train directions are exchanged:
   \[
   u_p+\Delta=u_q,\qquad
   -u_q+\Delta=-u_p;
   \tag{4}
   \]
3. every moving old actual diameter, oriented from the fixed exterior into the
   translated slab as \(n_h\), satisfies the exact non-grazing estimate
   \[
   \boxed{|n_h\cdot w|>{Ds\over2};}
   \tag{5}
   \]
4. at least one moving actual diameter has \(n_h\cdot w>0\);
5. consequently either

   \[
   \boxed{\text{TWO-SIGN: some moving actual diameter has }n_h\cdot w<0,}
   \tag{6}
   \]

   or

   \[
   \boxed{\text{ONE-SIGN: every moving actual diameter has }n_h\cdot w>0.}
   \tag{7}
   \]

6. in the ONE-SIGN case every moving old diameter strictly shortens under the
   full finite transposition. Canonical minimality therefore forces a previously
   strict source pair \(xy\) with

   \[
   \boxed{1<|xy|\le1+{4K\over D}}
   \tag{8}
   \]

   or

   \[
   \boxed{D-{4K\over D}\le|xy|<D.}
   \tag{9}
   \]

Thus the adjacent TB1 swap is not intrinsically adjacent. Any two distinct phases
inside the same open witness cell admit one exact finite block transposition with
the same active-diameter / inactive-slack fork.

No routing-hub hypothesis is needed.

## 1. Exact contact preservation for an arbitrary slab

Use the nested shore indicators of the ordered O--O train family. The physical slab
between \(\tau_p\) and \(\tau_q\) is the difference of their nested shores. The exact
O--O cutset property gives

\[
\delta_C(\text{slab})=E(\tau_p)\sqcup E(\tau_q).
\tag{10}
\]

Therefore translating the whole slab changes relatively only the two boundary
contact families. With both boundary contacts oriented from the fixed exterior into
the moving slab, their vectors are

\[
a=u_p,\qquad b=-u_q.
\tag{11}
\]

Equation (1) gives immediately

\[
a+\Delta=u_q,
\qquad
b+\Delta=-u_p,
\]

which proves (4) and preserves both boundary contact lengths exactly. All other old
contacts have both endpoints translated together or both endpoints fixed, so their
vectors are unchanged.

This is a finite contact-preserving move, not an infinitesimal shear.

## 2. The swap axis is the midpoint transverse direction

Let \(m\) be the projective midpoint of the two lifted train directions. The vector
\(w\) in (2) is a quarter-turn of \(m\). Directly,

\[
u_p\cdot w={s\over2},
\qquad
(-u_q)\cdot w={s\over2}.
\tag{12}
\]

Let the common open witness cell be \((d_-,d_+)\). Both train directions lie inside
it. Since their separation is \(\varepsilon\), their midpoint has projective distance
strictly larger than \(\varepsilon/2\) from either cell boundary:

\[
d_{\mathbb{RP}^1}(m,\{d_-,d_+\})>{\varepsilon\over2}.
\tag{13}
\]

There is no global actual-diameter direction in the open cell.

The two boundary diameter directions \(d_-,d_+\) are the fixed common witness rows
from the witness-cell extraction. They cross every retained train cut and hence have
the same cut incidence at \(p\) and \(q\); they do not move under the slab
translation. Parallel diameter segments are unique, so no other moving diameter has
either boundary direction.

Hence every moving actual-diameter direction lies strictly outside the closed angular
subinterval from the two train directions through \(m\). In particular,

\[
d_{\mathbb{RP}^1}([n_h],m)>{\varepsilon\over2}.
\tag{14}
\]

Since \(|n_h|=D\) and \(w=Jm\),

\[
|n_h\cdot w|
=
D\sin d_{\mathbb{RP}^1}([n_h],m)
>
D\sin{\varepsilon\over2}
={Ds\over2}.
\]

This proves (5).

## 3. KKT balance forces a positive-sign moving diameter

Sum the positive full-support KKT equilibrium over all source vertices in the slab.
Internal forces cancel. The only crossing contact forces are the two boundary train
families, so for their positive total contact weights \(A_p,A_q>0\),

\[
G_{p,q}
=
A_pu_p+A_q(-u_q)
=
\sum_{h\in H_{p,q}}\beta_h n_h,
\qquad \beta_h>0.
\tag{15}
\]

Taking the scalar product with \(w\) and using (12),

\[
\boxed{
G_{p,q}\cdot w
={s\over2}(A_p+A_q)>0.
}
\tag{16}
\]

Therefore the positive combination on the right side of (15) cannot consist only of
nonpositive \(w\)-projections. At least one moving actual diameter satisfies

\[
n_h\cdot w>0.
\tag{17}
\]

Together with the non-grazing estimate (5), this proves the exhaustive TWO-SIGN /
ONE-SIGN fork (6)--(7).

This argument supplies the needed sign without the old high-\(t\) common routing hub
or a separate slab-reaction nondegeneracy theorem.

## 4. ONE-SIGN gives strict finite diameter descent

For any moving actual diameter, the full slab translation changes its oriented
relative vector by \(\Delta=-sw\). Hence

\[
|r_h(\Delta)|^2-D^2
=
-2s(n_h\cdot w)+s^2.
\tag{18}
\]

In the ONE-SIGN case, (5) gives \(n_h\cdot w>Ds/2\). Therefore

\[
|r_h(\Delta)|^2-D^2
<
-Ds^2+s^2
=-(D-1)s^2<0
\tag{19}
\]

for \(D>1\). Every moving old actual diameter strictly shortens. Every nonswitching
old diameter is unchanged exactly.

If every previously strict noncontact remained \(>1\) and every previously strict
nondiameter pair remained \(<D\) at the endpoint of the swap, the moved source would
have the same old contacts. It would either have diameter \(<D\), contradicting
global minimality, or retain diameter \(D\) only through nonswitching old diameter
pairs while having strictly fewer diameter pairs, contradicting the canonical
diameter-pair-minimal representative.

Thus a previously strict pair must hit or cross one of the distance constraints by
the full swap. Such a pair has one endpoint in the translated slab and one outside,
so its distance changes by at most \(s\). Therefore

\[
1<|xy|\le1+s
\]

or

\[
D-s\le|xy|<D.
\]

Use (3) to obtain (8)--(9).

As in the adjacent theorem, no claim is made that the full endpoint of the swap is
feasible. The first inactive constraint that blocks the move is exactly the witness
recorded here.

## 5. Complete-grid local immunity survives for the block move

Every transverse retained train \(\sigma\) crosses both boundary trains in actual
strict rhombi. On the \(\tau_p\) boundary, the slab translation changes the row side
direction from \(u_p\) to \(u_q\), while every \(\sigma\)-contact edge is unchanged.
Thus the transformed boundary rhombus is congruent to the old
\((\tau_q,\sigma)\) rhombus. The other boundary is the converse.

Therefore no diagonal of a retained boundary-grid rhombus can be the inactive witness
in (8)--(9). The inactive obstruction to a ONE-SIGN block transposition is genuinely
nonlocal to its two complete-grid boundary rows.

## 6. Consequence for the remaining fixed-star branch

Suppose a retained shore contains at least two distinct train directions in its
common open witness cell. Then every chosen pair of distinct directions, no matter
how many selected layers lie between them, has the exact finite fork

\[
\boxed{
\text{bilateral moving-diameter support}
\quad\text{or}\quad
O(D^{-1})\text{ inactive near-activity}.
}
\tag{20}
\]

Hence exact-direction plateaus do not isolate phase changes: one may jump across an
arbitrarily long plateau and apply one finite block transposition to its two bounding
phases.

The only fixed-star shore on which this block mechanism is unavailable is an
exact-phase shore, where all retained train directions coincide. That branch remains
the current TB2/axial-reaction case.

The next closure target is therefore sharply split:

- **nonconstant phase:** exploit the bilateral block supports or the resulting
  nonlocal inverse-\(D\) inactive pairs;
- **constant phase:** exploit the exact axial KKT reactions and their switching-order
  structure.

The split-star O--O and inactive-interface branches remain separate.

No computation, verifier, numerical experiment, CI result, or unexecuted verifier
code is used.
