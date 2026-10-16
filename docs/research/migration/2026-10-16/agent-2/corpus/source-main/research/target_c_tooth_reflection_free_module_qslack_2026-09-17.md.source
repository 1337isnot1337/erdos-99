# Target C-II — free reflection modules: triple lower gate, core gate, or exact reflected-diameter witness

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only strengthening of the FREE-MODULE finite-repair branch  
**Scope:** all FREE reflection modules at `eta=3/26`, independent of shallow-apex degree  
**Dependencies:** free-module rigid gate; one-step inactive-guard absorption; retained-tooth reflection lower safety; contact-minimal normalization  
**Certificate:** `research/verify_target_c_tooth_reflection_free_module_qslack_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The two-gate theorem leaves degree-three modules with two inactive lower gates as a possible endpoint. There is an extra finite degree of freedom at the reflected apex itself. Once all upper blockers have been cleared, if `q` has no exact reflected-distance-`D` witness, the two base contacts can be opened simultaneously by moving `q` a sufficiently small distance farther across the loaded base. This loses two additional contacts.

That observation forces a three-way alternative for every FREE module:

\[
\boxed{
\begin{array}{ll}
\text{CORE-GATE:}&\text{the finite blocker repair meets an original nonisolated contact-core vertex;}\\[1mm]
\text{Q-DIAMETER:}&\text{some unmoved original source point }r\text{ satisfies }|q-r|=D;\\[1mm]
\text{TRIPLE-GATE:}&\text{at least three distinct lower gate edges are forced among vertices that}\\
&\text{were fully inactive in the original source.}
\end{array}}
\tag{QS.1}
\]

Every gate edge again comes from an original strict noncontact of length at most

\[
1+h_*+o(1)=1.3347479843\ldots+o(1).
\tag{QS.2}
\]

Thus two inactive gates can survive only if the reflected apex itself is already pinned by an exact upper-distance equality.

---

## 1. Run the repair through at most two inactive gate edges

Use the canonical inward blocker translation from the rigid-gate theorem. Whenever a lower gate reaches an old contact-core vertex, stop with CORE-GATE.

Otherwise its fixed endpoint was contact-isolated in the canonical source, hence fully inactive by C65. Absorb it and continue with the same velocity `-N`, as in the two-gate theorem.

If three distinct gate edges appear, stop with TRIPLE-GATE.

The only remaining case therefore uses at most two inactive gate edges. At most two inactive-guard absorption stages are needed. Their support depths are bounded by

\[
B_D+2(t_D+1)=O(\sqrt D),
\]

so the absorbed-guard upper-safety proof applies uniformly. In particular they can be carried through the blocker-clearing time without creating a distance larger than `D`.

If the last guard is first met exactly at the nominal clearing time, continue the enlarged moving cluster by an arbitrarily small additional positive amount. The same support-cap upper-safety estimate remains valid because the total inward displacement is still below `1/2` for all sufficiently large `D`. If another lower event appears immediately, it supplies the third gate. Otherwise this gives every absorbed guard a strictly positive inward displacement after it joined, while preserving all constraints. The blocker set itself only becomes farther inside the reflected diameter bound.

Consequently, in the surviving at-most-two-gate case, every moved point `p` satisfies

\[
1<|q-p|<D
\tag{QS.3}
\]

at the final clearing configuration.

---

## 2. The only possible upper equality at `q` is an unmoved source witness

For every original source point outside the blocker set,

\[
|q-r|\le D
\]

by definition of `U`. The moved blocker/guard cluster is strict by (QS.3).

If some still-fixed original source point satisfies

\[
\boxed{|q-r|=D,}
\tag{QS.4}
\]

we are in Q-DIAMETER and stop.

Assume Q-DIAMETER does not occur. Then after the blocker-clearing motion,

- every pair involving the future reflected apex `q` is strictly below `D` on the upper side;
- every such pair is strictly above one on the lower side except the two intended base equalities `qa=qb=1`.

All these strict slacks are positive for the fixed finite source.

---

## 3. Open both base contacts at once

Use tooth coordinates

\[
a=p-ct,\qquad b=p+ct,\qquad x=p+hn,\qquad q=p-hn,
\]

with `c^2+h^2=1` and `h>0`.

For `epsilon>0`, put

\[
q_\epsilon:=q-\epsilon n=p-(h+\epsilon)n.
\]

Then

\[
|q_\epsilon-a|^2
=|q_\epsilon-b|^2
=c^2+(h+\epsilon)^2
=1+2h\epsilon+\epsilon^2>1.
\tag{QS.5}
\]

So both base contacts open strictly.

All other distances from `q` were strict in both directions under the no-Q-DIAMETER assumption and (QS.3). By finiteness and continuity, choose `epsilon>0` sufficiently small that replacing `q` by `q_\epsilon` preserves

\[
1<|q_\epsilon-r|<D
\]

for every nonbase source point `r` in the final clearing configuration.

Thus the exact reflection followed by this arbitrarily small outward base-opening perturbation is still a feasible `n`-point source of diameter at most `D`. Global optimality forces its diameter to equal `D`.

---

## 4. At most two gate edges now contradict primary contact minimality for every apex degree

Let

\[
d=\deg_C(x).
\]

Canonical C26 gives `d>=3`.

The perturbed reflected point `q_\epsilon` has no unit contacts at all. Hence every one of the `d` old contacts incident to `x` is removed. If `k<=2` inactive gate edges were created during the clearing motion, the final contact count is

\[
\boxed{|C'|=|C|-d+k.}
\tag{QS.6}
\]

Since `d>=3` and `k<=2`,

\[
|C'|<|C|.
\tag{QS.7}
\]

The final source remains triangle-free. The old contact graph was triangle-free; `q_\epsilon` is contact-isolated; and a set of at most two newly created gate edges cannot contain a triangle because all of their endpoints were old contact isolates.

Therefore (QS.7) contradicts the primary contact-minimal choice among triangle-free global minimizers.

The assumed at-most-two-gate, no-core, no-Q-DIAMETER case is impossible. This proves (QS.1).

---

## 5. Geometry of the Q-DIAMETER witness

Although `q` is not an original source point, an equality witness in (QS.4) is still tightly localized by the existing full-source circumradius geometry.

The simultaneous-reflection theorem gives

\[
|q-o|={D\over2}+O(\sqrt D),
\]

while every original source point lies in

\[
B\!\left(o,{D\over2}+O(\sqrt D)\right).
\]

If `|q-r|=D`, the midpoint identity

\[
\left|{q+r\over2}-o\right|^2
={|q-o|^2+|r-o|^2\over2}-{D^2\over4}
\]

therefore gives

\[
\boxed{
\left|{q+r\over2}-o\right|=O(D^{3/4}).
}
\tag{QS.8}
\]

Since `q-o` is within `O(D^{-1/4})` angle of the module's opposite radial direction, (QS.8) implies

\[
\boxed{|r-y|=O(D^{3/4})}
\tag{QS.9}
\]

for the canonical blocker head `y`, and the equality chord `qr` follows the module normal to angular error `O(D^{-1/4})`.

Thus Q-DIAMETER is not an arbitrary equality elsewhere in the source: it is another antipodal point in the same inverse-quarter blocker cap.

---

## 6. Frontier effect

Combining the module-anchor theorem with (QS.1), the reflection branch can now be organized as

```text
selected slow-scale reflection module
    |
    +-- ANCHORED
    |      -> actual source diameter endpoint in U
    |      -> exact central diameter braid machinery
    |
    +-- FREE
           -> CORE-GATE
           |      -> finite lower repair reaches force-visible core
           |
           +-- Q-DIAMETER
           |      -> exact reflected diameter witness in same inverse-quarter antipodal cap
           |
           +-- TRIPLE-GATE
                  -> three inactive near-unit gate edges
```

The previous DOUBLE-GATE endpoint is gone unless it is accompanied by an exact reflected-distance-`D` equality.

**Disposition:** proved the base-opening perturbation and the resulting CORE/Q-DIAMETER/TRIPLE-GATE trichotomy for every FREE reflection module. C-II remains open. The clean next seams are the exact `q`-diameter witness geometry and the three-gate inactive jam.
