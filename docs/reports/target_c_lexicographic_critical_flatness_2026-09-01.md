<!-- theorem-state: {"artifact_id":"ART-7410900FE058","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_lexicographic_critical_flatness_2026-09-01.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=7f5dd9dfb568babf0e16869f8ff9c5fa9168e651; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C C86: lexicographic critical velocities integrate inside the exact active face

**Date:** 2026-09-01  
**Repository base:** `0a6d5871` (main after C85 / PR #90)  
**Run type:** exact nonlinear-normalization / chain-rigidity reduction  
**Target:** Target C Gate C-II, especially C80--C85 chain-face branch  
**Depends on:** C63 Newton--Hoffman integrability; C65 lexicographic contact/diameter normalization; C80 exact straight chain; C83 interval normal form; C84 prefix rank/circulation  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C63 and C65 together imply a stronger finite statement than has been used in the
post-C65 chain analysis.

Work in the C65 lexicographically normalized hypothetical counterexample: first
minimize the number of unit contacts, then among those minimizers minimize the number
of diameter pairs. C65 proves

\[
C=C_*,\qquad H=H_*.
\]

Thus every active unit-contact row and every active diameter row is strong.

C63 says that **every** fixed-diameter critical velocity `v` has an actual nearby
feasible realization

\[
p(t)=p+t v+O(t^2)
\]

satisfying all strong active inequalities. Since inactive rows have strict slack,
small `t` creates no new contact and no new diameter pair. Primary contact minimality
then prevents any old contact from opening; after that, secondary diameter-pair
minimality prevents any old diameter pair from shortening.

Therefore the C63 realization actually remains in the exact active face:

\[
\boxed{
|p_i(t)-p_j(t)|=1\quad(ij\in C),
\qquad
|p_i(t)-p_j(t)|=D\quad(ij\in H).
}
\tag{C86.1}
\]

for all sufficiently small `t`.

This is a general C-II finite-flatness theorem. It has an immediate consequence for
the exact C80 chain face. If

\[
z=x_0,x_1,\ldots,x_D=a
\]

is the literal straight `D`-edge unit-contact chain with `|z-a|=D`, then every
critical velocity must give all `D` chain edges one common angular rate. Otherwise
C86.1 would integrate it to a realization in which the `D` unit segments still join
endpoints at distance `D`, contradicting equality in the triangle inequality.

Hence every nonconstant chain-supported first-order-neutral mode is impossible. In
C84 notation:

\[
\boxed{N_P=\{0\},\qquad G_P\text{ is connected}.}
\tag{C86.2}
\]

The disconnected-prefix branch analyzed in C85 cannot occur in the fully
lexicographically normalized C65 source. Combining C86.2 with C84 gives

\[
\boxed{|H_P|\ge D+1,\qquad |H|\ge D+2.}
\tag{C86.3}
\]

Thus the exact chain-face route is reduced entirely to the **connected bridgeless
prefix-circulation branch**.

---

## 1. Lexicographic normalization

Fix a triangle-free global minimizer `A` of the cardinality under contradiction, and
make the C65 lexicographic choice:

1. minimize `|C(A)|`, the number of unit contacts;
2. subject to that, minimize `|H(A)|`, the number of diameter pairs.

C63 closes Gate C-I, and C65 applies the same critical-cone integrability to the
secondary normalization. The result is

\[
\boxed{C=C_*,\qquad H=H_*.}
\tag{C86.4}
\]

Every initially inactive pair has one of the strict alternatives

\[
1<|p_i-p_j|<D,
\tag{C86.5}
\]

unless it is an active contact or active diameter pair.

Let `v` be any fixed-diameter critical velocity. Because every active row is strong,
its signed first variation vanishes on every active contact and diameter row.

---

## 2. C63 integrates every critical velocity

C63 writes the strong feasibility map exactly as

\[
g_*(x)=A_*x+Q_*(x)
\]

and uses universal PSD, Farkas, and a fixed Hoffman constant to construct, for every
critical tangent `v`, actual small displacements

\[
\boxed{x(t)=t v+O(t^2)}
\tag{C86.6}
\]

such that every strong active row remains feasible.

Since C86.4 says every active row is strong, the resulting configuration `A(t)` is
unit-separated and has diameter at most `D`. Global minimality of `D=D(n)` gives

\[
\operatorname{diam}A(t)=D.
\tag{C86.7}
\]

C63's construction is local. For sufficiently small `t`, every initially inactive
pair retains strict slack by C86.5. Therefore

\[
C(A(t))\subseteq C(A),
\qquad
H(A(t))\subseteq H(A).
\tag{C86.8}
\]

No new active pair appears.

---

## 3. Primary minimality forces every old contact to remain exact

Suppose some original contact `ij in C(A)` opened:

\[
|p_i(t)-p_j(t)|>1.
\]

Then C86.8 would be strict on contacts:

\[
|C(A(t))|<|C(A)|.
\]

The configuration `A(t)` is still triangle-free: no new unit contact appears, while
opening contacts cannot create a contact triangle. By C86.7 it is another global
minimum-diameter configuration. This contradicts the primary lexicographic choice.

Hence

### Lemma C86.1 — exact contact preservation

For every critical `v` and all sufficiently small C63 realizations,

\[
\boxed{C(A(t))=C(A),}
\tag{C86.9}
\]

and, edge by edge,

\[
\boxed{|p_i(t)-p_j(t)|=1\qquad(ij\in C).}
\tag{C86.10}
\]

The equality is edgewise because C86.8 already excludes replacement contacts.

---

## 4. Secondary minimality forces every old diameter pair to remain exact

After Lemma C86.1, `A(t)` lies in the same minimum-contact class used for C65's
secondary normalization.

Suppose some original diameter pair `ij in H(A)` shortened:

\[
|p_i(t)-p_j(t)|<D.
\]

Again C86.8 gives no new diameter pair, so

\[
|H(A(t))|<|H(A)|.
\]

This contradicts the secondary lexicographic choice among contact-minimal global
minimizers.

Therefore:

### Theorem C86.2 — exact active-face integrability

For every fixed-diameter critical velocity `v`, there are actual nearby realizations

\[
p(t)=p+t v+O(t^2)
\]

such that, for all sufficiently small `t`,

\[
\boxed{
|p_i(t)-p_j(t)|=1\quad(ij\in C),
\qquad
|p_i(t)-p_j(t)|=D\quad(ij\in H).
}
\tag{C86.11}
\]

All inactive pairs remain strict.

Thus every first-order critical direction is tangent to a genuine local realization
of the complete active equality framework `(C,H)`.

This statement is stronger than C65's use of C63, which only needed one
relative-interior critical velocity to eliminate weak rows.

---

## 5. Straight-chain equality forces one angular rate

Now assume the exact C80 chain-face branch. Thus one active diameter pair is

\[
h_0=za,
\qquad |z-a|=D,
\]

and the source contains the literal contact path

\[
\boxed{z=x_0,x_1,\ldots,x_D=a}
\tag{C86.12}
\]

with

\[
|x_j-x_{j-1}|=1
\qquad(1\le j\le D).
\]

Let `v` be any critical velocity. Apply C86.2. Along the integrated realization,
all chain edges remain unit contacts and `za` remains a diameter pair. Therefore

\[
D
=|a(t)-z(t)|
\le
\sum_{j=1}^D|x_j(t)-x_{j-1}(t)|
=D.
\tag{C86.13}
\]

Equality holds in the Euclidean triangle inequality. Equality for a sum of nonzero
vectors occurs exactly when all summands are nonnegative scalar multiples of one
common vector. Here every summand has length one, so there is one unit vector `u(t)`
such that

\[
\boxed{x_j(t)-x_{j-1}(t)=u(t)\qquad(1\le j\le D).}
\tag{C86.14}
\]

The entire contact chain remains a literal straight unit-spaced segment for every
small `t`.

Differentiate at `t=0`. If

\[
\dot x_j-\dot x_{j-1}=\omega_j Ju
\]

is the tangential first-order motion of the `j`th chain edge, C86.14 gives

\[
\boxed{\omega_1=\omega_2=\cdots=\omega_D.}
\tag{C86.15}
\]

### Corollary C86.3 — chain angular synchronization

Every fixed-diameter critical velocity gives all chain edges one common angular rate.
No nonconstant first-order bending mode of the exact diameter chain exists in the
C65-normalized source.

---

## 6. Translation to C80 train-angle coordinates

C80 associates to the chain edges `x_{j-1}x_j` the `D` distinct parallel train tracks

\[
P=\{\tau_1,\ldots,\tau_D\},
\]

one track per edge. In the pure-rhombic train-angle parametrization, the velocity
coordinate `v_{\tau_j}` is exactly the angular rate of the unit-edge direction on
that train, after a common global rotation is included in all train coordinates.

Therefore C86.15 becomes

\[
\boxed{
v_{\tau_1}=\cdots=v_{\tau_D}}
\tag{C86.16}
\]

for every train-angle velocity that is first-order neutral for all active diameters.

In particular, on the C80 chain-bending space

\[
W_P=\left\{v:\operatorname{supp}v\subseteq P,
\quad\sum_{\tau\in P}v_\tau=0\right\},
\]

only zero can be critical:

\[
\boxed{W_P\cap\ker G_H=\{0\}.}
\tag{C86.17}
\]

Here `G_H` is the full active diameter-gradient map.

---

## 7. C84 prefix graph must be connected

C84 gives the exact rank formula for chain-supported neutral motions. If `G_P` is the
simple prefix graph on levels `0,...,D`, then

\[
\dim N_P=c(G_P)-1,
\tag{C86.18}
\]

where `N_P` is the mean-zero chain-supported first-order-neutral space used in C85.

C86.17 says `N_P={0}`. Hence:

### Theorem C86.4 — connected-prefix necessity

In the exact C80 chain-face branch of the C65 lexicographically normalized source,

\[
\boxed{c(G_P)=1.}
\tag{C86.19}
\]

So

\[
\boxed{G_P\text{ is connected}.}
\tag{C86.20}
\]

The entire disconnected-prefix branch is impossible. In particular the nonzero
chain-neutral modes used by C85 cannot occur in the canonical counterexample.

This does not invalidate C85 as a conditional KKT theorem; it shows that its
hypothesis `N_P!=0` is excluded once C63/C65 finite normalization is fed back into the
C80 chain geometry.

---

## 8. Combine with C84 circulation

C84 proves that the non-chain interval **multigraph** carries a nowhere-zero KKT
circulation and therefore has no bridges. It also proves that a connected simple
prefix graph on all `D+1` levels requires at least `D+1` non-chain interval bars.

C86.20 activates that bound unconditionally inside the exact chain-face branch:

### Corollary C86.5 — exact chain face forces a linear diameter-bar family

\[
\boxed{|H_P|\ge D+1.}
\tag{C86.21}
\]

Including the chain diameter `h_0` itself,

\[
\boxed{|H|\ge D+2.}
\tag{C86.22}
\]

Moreover every chain cut is crossed by at least two active non-chain interval bars
with opposite signs of the transverse KKT flow `beta_h eta_h`.

Thus the chain-face survivor is now entirely the first-order high-capacity phase:

```text
exact C76/C80 chain face
    -> C63/C65 finite active-face integrability
    -> chain edges must stay straight in every critical motion
    -> no nonconstant chain-supported neutral mode
    -> C84 prefix graph connected and bridgeless
    -> >= D+1 non-chain diameter interval bars
    -> >= D+2 total active diameter bars.
```

---

## 9. Interaction with C81 and C85

C81 proves that a KKT stress sufficiently concentrated on `h_0` has `D-1` strongly
negative directions in the chain-bending Hessian. C86 explains why this does not by
itself create a critical motion: the full active diameter-gradient system must remove
every one of those chain-supported bending directions at first order.

C85 studies the alternative `N_P!=0` and proves a half-mass separation for any
zero-energy secondary stress. C86 shows that, for the lexicographically normalized
C65 source, this alternative does not arise. Thus the live C80 branch is not a
secondary-null-face mass problem; it is a first-order ordered diameter-capacity
problem.

The remaining task is to rule out the connected bridgeless prefix circulation forced
by C84/C86.

---

## 10. What C86 does not prove

C86 does **not** show that the full active framework is rigid. It shows only that every
critical tangent integrates inside the exact active equality realization space.
Nontrivial finite flexes preserving all contacts and all diameter pairs are not
excluded in general.

For the exact straight chain, equality in the triangle inequality freezes only the
relative angular rates of the `D` chain edges. Critical motion may still occur in
other train coordinates while the chain rotates rigidly.

The count `|H|>=D+2` is compatible with the classical planar diameter-edge bound
`|H|<=|V(H)|<=pi D`. A new ordered/geometric argument is still required.

---

## 11. Next target

The C80 branch has now been reduced to one exact combinatorial-geometric object:

a connected bridgeless prefix interval multigraph on `D+1` ordered chain levels,
carrying a nowhere-zero KKT circulation, realized by actual planar diameter chords.
C84 further shows that every backward interval is an interior chord crossing the
straight chain.

The next theorem should attack this high-capacity phase directly. Viable routes are:

1. **Level-capacity theorem.** Use shared-endpoint angle separation and unit spacing to
   bound the number of distinct diameter endpoints that can occupy all `D+1` chain
   levels with minimum prefix degree two.
2. **Thrackle-to-prefix theorem.** Transfer pairwise intersection of actual diameter
   chords into a forbidden ordered pattern in the connected bridgeless prefix graph.
3. **Boundary curvature theorem.** Every prefix level is incident to diameter bars,
   hence contains at least one diameter endpoint. Combine this `D+1`-level occupation
   with the near-disk hull curvature/Barbier boundary budget.
4. **Train-separation theorem.** A backward interval of length `m` forces at least
   `m+|c_h|` non-chain separating trains by projection along the chain direction.
   Sum that cost over a cycle basis of the bridgeless prefix graph.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C86 feeds C63 back through the C65 lexicographic normalization.
In the C65 source every active contact and every active diameter pair is strong.
For any critical velocity v, C63 gives p(t)=p+t v+O(t^2) satisfying all active
inequalities; inactive pairs stay strict. Contact minimality forbids loss of any old
contact, then secondary diameter-pair minimality forbids loss of any old diameter.
Hence the C63 motion actually satisfies, edge by edge,
  |e(t)|=1 for every e in C,
  |h(t)|=D for every h in H.

For the exact C80 chain z=x_0,...,x_D=a,
  D=|a(t)-z(t)| <= sum_j |x_j(t)-x_(j-1)(t)| = D.
Triangle-inequality equality forces all D unit chain edges to remain parallel and
co-oriented. Therefore every critical velocity has one common chain angular rate.
In C80 train coordinates,
  v_tau1=...=v_tauD.
So the mean-zero chain-supported neutral space N_P is zero.

C84 gives dim N_P=c(G_P)-1. Therefore G_P is connected. Its KKT interval multigraph
is already bridgeless by C84, so it has at least D+1 non-chain bars. Including the
chain bar,
  |H|>=D+2.

The C85 disconnected-prefix/null-face branch is therefore excluded in the canonical
C65 source. The only surviving exact-chain phase is a connected bridgeless ordered
prefix circulation realized by actual diameter chords.
```
