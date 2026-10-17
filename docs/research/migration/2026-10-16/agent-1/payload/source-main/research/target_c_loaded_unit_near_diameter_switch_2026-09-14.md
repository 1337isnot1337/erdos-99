# Target C-II — loaded unit contacts force shell wedges or near-diameter switches

**Date:** 2026-09-14  
**Status:** proof-only structural synthesis; theorem-state authority unchanged  
**Scope:** canonical full-core near-disk C-II branch, using the proof-only full-source circumradius/midpoint theorem  
**LEVEL I STATUS:** `STILL OPEN`

The low-`t` boundary-atom theorem gives a branch with linearly many exact unit contacts
between consecutive loaded force-hull vertices.  Those contacts interact strongly with
the actual diameter graph.

For a loaded unit edge `AB`, choose actual diameter partners

\[
|A-X|=D,
\qquad
|B-Y|=D.
\]

The full-source circumradius theorem places the midpoint of every actual diameter pair
within `L_D` of one common source circumcenter, where

\[
\eta_D=3^{1/4}\sqrt D,
\qquad
L_D:=\sqrt{D\eta_D+\eta_D^2}=O(D^{3/4}).
\]

This gives a finite four-point estimate:

\[
\boxed{
D-|A-Y|,\ D-|B-X|
<\varepsilon_D:={4L_D+1\over D}
=O(D^{-1/4}).
}
\tag{SW.1}
\]

Thus a unit contact between two loaded diameter endpoints automatically creates two
asymptotically active cross-diameter pairs.

If `X!=Y`, both cross pairs cannot simultaneously be actual diameter edges: otherwise
`AX,BX,BY,AY` form a four-cycle in the actual planar diameter graph, whereas the
canonical Woodall/Hopf--Pannwitz topology has only forests or one odd cycle per
component.  Therefore every loaded unit edge is of one of two types:

1. a **shell wedge**, whose endpoints have one common actual diameter neighbor; or
2. a **switch edge**, which produces an inactive source pair of length at least
   `D-epsilon_D`.

A matching argument then gives a linear version of this dichotomy in the low-`t`
loaded-unit branch.

## 1. Diameter partners of a unit loaded edge are close

Let

\[
m_X={A+X\over2},
\qquad
m_Y={B+Y\over2}.
\]

The full-source midpoint theorem gives

\[
|m_X-o|<L_D,
\qquad
|m_Y-o|<L_D.
\tag{SW.2}
\]

Since

\[
X=2m_X-A,
\qquad
Y=2m_Y-B,
\]

and `|A-B|=1`,

\[
\begin{aligned}
|X-Y|
&=|2(m_X-m_Y)-(A-B)|\\
&\le2|m_X-o|+2|m_Y-o|+|A-B|\\
&<4L_D+1.
\end{aligned}
\tag{SW.3}
\]

This is quantitative; no subsequential disk-limit argument is needed.

## 2. Ptolemy forces the cross pairs to be near-diametral

Euclidean Ptolemy inequality for the four source points `A,B,X,Y` gives

\[
|A-X|\,|B-Y|
\le |A-B|\,|X-Y|+|A-Y|\,|B-X|.
\]

Using the two diameter equalities and `|A-B|=1`,

\[
D^2
\le |X-Y|+|A-Y|\,|B-X|.
\tag{SW.4}
\]

All source distances are at most `D`, so

\[
D^2-|A-Y|\,|B-X|
\ge D(D-|A-Y|)
\]

and symmetrically with `A-Y` and `B-X` exchanged.  Combining with (SW.3)--(SW.4),

\[
D(D-|A-Y|)<4L_D+1,
\]

\[
D(D-|B-X|)<4L_D+1.
\]

This proves (SW.1).

In particular the absolute diameter slack tends to zero:

\[
\varepsilon_D
={4\sqrt{D\eta_D+\eta_D^2}+1\over D}
=(4\,3^{1/8}+o(1))D^{-1/4}.
\tag{SW.5}
\]

The statement is stronger than `|A-Y|,|B-X|>=D-1`; the slack is `o(1)` in the
unscaled source.

## 3. The only exact escape is a common diameter neighbor

Suppose `X!=Y`.  The edges `AX` and `BY` are actual diameter edges.

If both cross pairs were also actual diameter edges, then the full actual diameter
graph would contain

\[
A-X-B-Y-A,
\]

a four-cycle.  The planar diameter graph of the canonical C-II source is a
straight-line thrackle.  In the current Woodall normalization its components are
caterpillar trees when `d_H>0`, and in the zero-defect case the only cycle is odd.
Thus an even four-cycle is impossible.

Therefore, when `X!=Y`, at least one of

\[
AY,\qquad BX
\]

is inactive as a diameter constraint while still satisfying (SW.1).

If `X=Y`, the two loaded endpoints `A,B` have a common actual diameter neighbor.  Call
`AB` a **shell wedge**.  Two distinct common diameter neighbors are impossible, since
they would themselves produce the same forbidden `K_{2,2}` / four-cycle.

Hence every loaded unit contact admits the exact dichotomy

```text
unique common diameter neighbor,
OR
an inactive cross pair of length at least D-epsilon_D.
```

The regular odd shell realizes the first alternative on every boundary unit edge, so
that branch cannot be rejected by local four-point geometry alone.

## 4. Linear matching version

Let `M_BB` be a matching of exact loaded-loaded unit hull contacts.  The boundary-atom
theorem gives

\[
|M_{BB}|\ge {e_{BB}\over2}-O(1).
\tag{SW.6}
\]

Partition `M_BB` into shell wedges and non-shell switch edges.

For every non-shell edge choose one inactive cross pair supplied by Section 3.  One
unordered inactive pair can be chosen by at most two distinct matching edges: each
chosen pair has only two endpoints, while the contact edges in `M_BB` have disjoint
endpoint sets.  Therefore `r` non-shell matching edges supply at least `r/2` distinct
inactive near-diameter pairs.

Consequently at least one of the following holds:

\[
\boxed{
M_{shell}\ge {|M_{BB}|\over2},
}
\tag{SW.7}
\]

or

\[
\boxed{
N_{near}^{inactive}\ge {|M_{BB}|\over4},
\qquad
|u-v|\ge D-\varepsilon_D
\text{ for every selected pair }uv.
}
\tag{SW.8}
\]

Here `M_shell` counts vertex-disjoint loaded unit contacts whose endpoints share an
actual diameter neighbor, while `N_near^inactive` counts distinct inactive source
pairs.

## 5. Low-`t` consequence

The updated boundary-atom theorem gives, on the loaded-unit branch,

\[
{e_{BB}\over D}
\ge {t\over4}+{C_0\over6}-o(1),
\qquad
C_0=2\sqrt{\Delta_2}+0.0021.
\tag{SW.9}
\]

Thus

\[
{|M_{BB}|\over D}
\ge {t\over8}+{C_0\over12}-o(1).
\tag{SW.10}
\]

At the current proof-only floor

\[
t_{21}={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0017279,
\]

this matching density is approximately `0.38654`.

Combining with (SW.7)--(SW.8), the loaded-unit branch has either approximately

\[
0.19327D
\]

vertex-disjoint shell wedges, or approximately

\[
0.09663D
\]

distinct inactive source pairs whose absolute diameter slack is
`O(D^{-1/4})`.

The decimals are orientation only.  The exact theorem is (SW.5)--(SW.10).

## 6. Why this narrows the endpoint

The loaded-unit branch is no longer merely a large boundary matching.  It must choose
between two specific mechanisms:

1. **shell-wedge regime:** a linear set of unit boundary contacts is organized exactly
   like the local diameter geometry of an odd regular shell; or
2. **near-active switch regime:** the source carries a linear set of inactive
   diameter inequalities whose slack tends to zero in absolute units.

The first regime has a known source-level regression: a regular unit shell plus a
quadratic near-density isolated interior cloud admits a strict smaller-diameter global
competitor.  That regression does not yet apply to an arbitrary connected canonical
full core.

The second regime is invisible to a fixed active-set KKT matrix because the switch
pairs remain strictly inactive at every finite `D`.  A closing theorem must therefore
turn their vanishing slack into either an active-set exchange, a second-order
source-preserving deformation, or a global packing loss.  Relative-interior positivity
alone is insufficient.

## 7. Scope audit

- The midpoint estimate is for the full source and retains all contact-isolated points.
- No assumption `F=K` is made; only actual diameter endpoints and the common source
  circumcenter are used.
- Ptolemy is applied to actual source points and uses only the global diameter cap.
- The four-cycle exclusion is applied only to the actual diameter graph.
- `epsilon_D` is an explicit finite bound, not a qualitative `o(1)` placeholder.
- The linear low-`t` constants inherit the proof-only minimax-atomic-gap lifecycle.
- The shell-wedge branch is explicitly retained because the regular odd shell is a
  genuine local regression.
- No exact unit equilateral triangle or strict same-cardinality sub-`D` competitor is
  produced.

**Disposition:** proof-only structural theorem.  C-II and Level I remain open.
