# Target C-II — every modern survivor has either linearly many singleton trains or linearly many fully rhombic pentagonal flowers

**Date:** 2026-09-15  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II train-measure branch; quantitative rows through `t=(q-k)/D<=1.8623`  
**Dependencies:** modern all-train pentagon sea; exact singleton identity `rho_rec=2S`; modern train-slack split  
**Certificate:** `research/verify_target_c_modern_singleton_or_full_pentagon_flower.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The modern all-train theorem forces a large population of bounded pentagonal contact
faces.  The exact stopped-train decomposition gives a sharper local alternative than
the balanced recipient-waste/rhombic-slack split.

Call a bounded pentagon **fully rhombic** if each of its five contact-edge sides has a
strict unit-rhombus face on the other side.  Let

\[
F_5^{full}
\]

be the number of such pentagons and let `S` be the number of singleton stopped trains,
i.e. contact edges incident to no strict rhombus.

Every pentagon which is not fully rhombic has at least one singleton boundary edge.
One singleton edge has only two face sides, so it can witness non-fullness of at most
two pentagons.  Therefore the exact finite inequality is

\[
\boxed{P_5-F_5^{full}\le2S.}
\tag{SF.1}
\]

Combining (SF.1) with the modern pentagon floor gives a balanced dichotomy.  At the
widest current pentagon endpoint `t<=1.8623`, every survivor satisfies

\[
\boxed{
S>0.1327D-o(D)
\quad\text{or}\quad
F_5^{full}>0.1327D-o(D).
}
\tag{SF.2}
\]

At the currently valid corrected O--O path endpoint `t<=1.860`, the common floor is
slightly stronger:

\[
\boxed{
S>0.1346D-o(D)
\quad\text{or}\quad
F_5^{full}>0.1346D-o(D).
}
\tag{SF.3}
\]

The fully rhombic branch has much larger train-isoperimetric slack than the previously
balanced modern split.  At `t<=1.8623`, if the singleton alternative fails then

\[
\boxed{
\sigma_R>1.228D-o(D),
}
\tag{SF.4}
\]

and the exact strict-rhombus train Mantel deficit satisfies

\[
\boxed{
{T_R^2\over4}-R_4>0.679D^2-o(D^2).
}
\tag{SF.5}
\]

Moreover the fully rhombic flowers alone terminate more than

\[
\boxed{0.3317D-o(D)}
\tag{SF.6}
\]

distinct non-singleton stopped trains.  At `t<=1.860` these constants improve to
`sigma_R>1.224D`, Mantel deficit `>0.676D^2`, and more than `0.3366D` trains ending on
fully rhombic flowers.

This is a network normal form, not a local phase-gap theorem.  Explicit near-lattice
pentagon regressions can be surrounded by four strict rhombi, and exploratory local
search shows that the fifth rhombus can also be added with its transverse direction
arbitrarily close to a lattice direction while finite separation slack remains
positive.  No uniform angular or metric payment per fully rhombic flower is claimed.

---

## 1. Modern pentagon floor

The modern all-train gap gives, for every fixed endpoint `t<=T`,

\[
{P_5\over D}
\ge p_5(T)-o(1),
\qquad
p_5(T)=\pi+C_{707}-{5T\over2},
\tag{SF.7}
\]

where

\[
C_{707}=2\sqrt{\Delta_2}+0.007707,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\]

The exact companion certificate gives

\[
\begin{array}{c|c}
T & p_5(T)\\ \hline
1.8500 & >0.4289252\\
1.8550 & >0.4164252\\
1.8593 & >0.4056752\\
1.8600 & >0.4039252\\
1.8623 & >0.3981752.
\end{array}
\tag{SF.8}

---

## 2. Non-full pentagons consume singleton face sides

Fix one bounded pentagonal face `P`.  Each of its five contact edges has exactly one
other incident face-side occurrence in the plane embedding.

If the other face is a strict rhombus, that edge lies in a non-singleton stopped train.
If the other face is not a strict rhombus, then neither side of the edge is a strict
rhombus, because `P` itself is pentagonal.  Hence that contact edge is a singleton
stopped train.

Thus every pentagon outside `F_5^{full}` contains at least one singleton contact edge.
A singleton edge can lie on the boundary of at most two pentagonal faces, one on each
face side.  Counting incidences between non-full pentagons and singleton edges gives
(SF.1):

\[
P_5-F_5^{full}\le2S.
\]

No assumption about which other nonquadrilateral face lies across a singleton edge is
needed.

---

## 3. Balanced dichotomy

For a fixed endpoint `T`, put

\[
s(T):={p_5(T)\over3}.
\tag{SF.9}
\]

If

\[
S\ge s(T)D-o(D),
\]

the singleton branch holds.  Otherwise (SF.1) and (SF.7) give

\[
\begin{aligned}
F_5^{full}
&\ge P_5-2S\\
&>p_5(T)D-2s(T)D-o(D)\\
&=s(T)D-o(D).
\end{aligned}
\]

Hence

\[
\boxed{
\max\{S,F_5^{full}\}
\ge s(T)D-o(D).
}
\tag{SF.10}
\]

The exact certificate gives the safe rows

\[
\begin{array}{c|c}
T & s(T)\\ \hline
1.8500 & >0.142\\
1.8550 & >0.138\\
1.8593 & >0.135\\
1.8600 & >0.1346\\
1.8623 & >0.1327.
\end{array}
\tag{SF.11}

This proves (SF.2)--(SF.3).

---

## 4. The full-flower branch has very large rhombic train slack

The exact modern stopped-train decomposition gives

\[
\rho_{rec}=2S,
\qquad
2\tau_D=\rho_{rec}+\sigma_R,
\tag{SF.12}
\]

and the hostile-audited modern train-slack theorem gives

\[
\tau_D\ge(\tau_0-o(1))D,
\qquad
\tau_0=0.7467921.
\tag{SF.13}
\]

In the full-flower branch of the balanced dichotomy,

\[
S<s(T)D+o(D).
\]

Therefore

\[
\begin{aligned}
\sigma_R
&=2\tau_D-2S\\
&>2[\tau_0-s(T)]D-o(D).
\end{aligned}
\tag{SF.14}
\]

At `T=1.8623`, the exact verifier gives

\[
2[\tau_0-s(T)]>1.228134,
\]

and at `T=1.860` it gives `>1.224300`.  This proves (SF.4) and its `1.860` version.

---

## 5. Exact Mantel deficit in the full-flower branch

Let

\[
T_R={B_4\over2}
\]

be the strict-rhombus stopped-train count.  With

\[
\sigma_R=2T_R-4\sqrt{R_4},
\]

one has the exact identity

\[
\boxed{
{T_R^2\over4}-R_4
={\sigma_R\sqrt{R_4}\over2}
+{\sigma_R^2\over16}.
}
\tag{SF.15}
\]

Since

\[
R_4/D^2\to\Delta_2,
\]

(SF.14) gives an explicit quadratic deficit.  The exact verifier records

\[
\begin{array}{c|c}
T & \liminf D^{-2}(T_R^2/4-R_4)\\ \hline
1.8500 & >0.666\\
1.8550 & >0.671\\
1.8593 & >0.675\\
1.8600 & >0.676\\
1.8623 & >0.679.
\end{array}
\tag{SF.16}

Thus the full-flower branch is much farther from the Mantel endpoint than the generic
balanced R branch.

---

## 6. Fully rhombic flowers force many non-singleton train endpoints

A fully rhombic pentagon has five boundary occurrences, each terminating a
non-singleton strict-rhombus stopped train.  One complete stopped train has only two
terminal occurrences.  Therefore, if `N_full` is the number of distinct non-singleton
trains terminating at at least one fully rhombic pentagon,

\[
\boxed{N_{full}\ge{5\over2}F_5^{full}.}
\tag{SF.17}
\]

Using (SF.10), the full-flower branch gives

\[
\begin{array}{c|c}
T & N_{full}/D\\ \hline
1.8500 & >0.357\\
1.8550 & >0.347\\
1.8593 & >0.338\\
1.8600 & >0.3366\\
1.8623 & >0.3317.
\end{array}
\tag{SF.18}

Every one of these trains belongs to the strict-rhombus train complex.

---

## 7. Local metric regression remains binding

The dichotomy should not be misread as a local phase-gap theorem.

The known exact pentagon regression gives strict convex unit pentagons whose edge
projective directions approach the three triangular-lattice lines while all nonedge
source distances remain above one.  Four rhombus neighbors can be attached along that
family without producing a uniform separation gap.

A direct finite local feasibility probe of the fifth side shows the same mechanism can
persist with all five rhombus neighbors: for the explicit regression, after fixing the
four lattice-near rhombi, the fifth unit transverse vector has an open admissible
angular interval approaching a lattice direction.  Therefore no uniform positive
angular defect per fully rhombic flower is used or claimed here.

This exploratory local observation is included only as a regression warning; the
proved theorem is (SF.1)--(SF.18), which is purely combinatorial plus the existing exact
scalar ledgers.

---

## 8. Frontier effect

Through the valid corrected path endpoint `t<=1.860`, the modern full-core obstruction
can now be split as

```text
singleton branch:
  >0.1346 D singleton contact-edge trains;

or full-flower branch:
  >0.1346 D empty pentagons with rhombi on all five sides;
  >0.3366 D strict-rhombus trains terminating on those flowers;
  sigma_R >1.224 D;
  strict-rhombus train Mantel deficit >0.676 D^2.
```

The corrected joint-feasibility theorem independently supplies a same-phase O--O dual
path and common diameter-routing hub through this entire `t<=1.860` band.  This note
does not assert any localization between that selected O--O path and the singleton or
flower populations.

The next closing work is therefore network-theoretic:

1. in the singleton branch, exploit the linear family of one-edge stopped trains using
   their endpoint-face graph, exact contact directions, and source-preserving local
   flexes; or
2. in the full-flower branch, exploit the incidence graph between a linear family of
   five-rhombus holes and a linear family of strict-rhombus trains, together with the
   very large train-crossing deficit and the common-hub diameter routing.

**Disposition:** proved proof-only singleton/full-rhombic-pentagon-flower dichotomy and
its train-slack consequences.  C-II and Level I remain open.
