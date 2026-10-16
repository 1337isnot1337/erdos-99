<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bd5c37e80984a640b81917f0464db9dc9bebb68d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_g0050_low_t_bridge_pentagon_split_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a3f75cc732a2a13d032b6f2680900716862daeb06c4e56c62caa71ecd1daedc3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdos Problem #99 - matched `g=0.0050` low-`t` bridge and pentagon split

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Repository branch:** `research/c2-gluing-sol-20260914-r10`  
**Claim class:** proof-only composition of the matched atomic theorem, Section 171, and hostile-audited bridge subtraction  
**LEVEL I STATUS:** `STILL OPEN`

The iterative-pruning minimax theorem on this branch gives the matched train floors

\[
{T-q/2\over D}\ge2\sqrt{\Delta_2}+0.0050-o(1),
\qquad
{T_R\over D}\ge2\sqrt{\Delta_2}+0.0050-o(1),
\tag{BP50.1}
\]

where

\[
\Delta_2={\pi\over2\sqrt3}.
\]

The exact Section-171 certificate gives

\[
{q-k\over D}\ge t_{50}-o(1),
\qquad
t_{50}:={4\over9}(\pi+\sqrt{\Delta_2})+0.0023374
=1.821850937979444\ldots .
\tag{BP50.2}
\]

The corresponding low-`t` detour and topology budgets are

\[
{b-P_F\over D}\le\delta_{50}+o(1),
\qquad
{Q-f\over D}\le\delta_{50}+o(1),
\tag{BP50.3}
\]

with

\[
\boxed{\delta_{50}=0.00275915.}
\tag{BP50.4}
\]

The main new composition is that bridge subtraction and pentagon localization almost
entirely remove the singleton escape.  Put `S_5` for singleton stopped trains having at
least one pentagonal terminal incidence.  Then

\[
\boxed{
\sigma_R+2S_5
\ge(1.795981987979444\ldots-o(1))D.
}
\tag{BP50.5}
\]

Consequently, after fixing a branch subsequence, either

\[
\boxed{
\sigma_R/D\ge0.897990993989722\ldots-o(1)
}
\tag{BP50.6}
\]

or

\[
\boxed{
S_5/D\ge0.448995496994861\ldots-o(1).
}
\tag{BP50.7}
\]

The first alternative has rhombic Mantel deficit

\[
\boxed{
M_R/D^2\ge0.477983401092869\ldots-o(1).
}
\tag{BP50.8}
\]

The second alternative localizes nearly half a train per unit diameter directly on
pentagonal defect faces.  This is substantially stronger than the earlier detour-free
singleton gate.

---

## 1. Low-`t` structural constants at `g=0.0050`

Put

\[
s:=\sqrt{\Delta_2},
\qquad C_0:=2s+0.0050.
\]

The Section-171 feasible-detour endpoint at `t=t_50` is

\[
\delta_{50}
={{9\over2}(0.0023374)-0.0050\over2}
=0.00275915.
\]

The exact low-`t` identities and inequalities therefore give

\[
{f\over D}\ge {C_0\over2}-{t_{50}\over4}-o(1)
=0.499350072369096\ldots-o(1),
\tag{BP50.9}
\]

\[
{Q-f\over D}\le0.00275915+o(1),
\tag{BP50.10}
\]

and

\[
\boxed{
{p_5\over D}\ge
\pi+C_0-{5t_{50}\over2}-o(1)
=0.496590922369096\ldots-o(1).
}
\tag{BP50.11}
\]

The same endpoint squeeze gives

\[
{k\over D}\le0.01103660+o(1).
\tag{BP50.12}
\]

Hence the pentagon closure-rank theorem yields

\[
\boxed{
{\operatorname{rank} C_{P_5}\over D}
\ge0.982145244738192\ldots-o(1).
}
\tag{BP50.13}
\]

The outer-to-outer train floor remains

\[
\boxed{
{L_{OO}\over D}\ge3\pi-5t_{50}-o(1)
=0.315523270872156\ldots-o(1).
}
\tag{BP50.14}
\]

Thus the survivor is simultaneously a `>99.4%` pentagon defect sea, a nearly maximal
Woodall/mixed-rigidity system, and a train network with a macroscopic exact
outer-to-outer shear subspace.

---

## 2. Lossless total train defect with the matched gain

Let `T_R` be the non-singleton strict-rhombus train count and

\[
S:=T-T_R
\]

the singleton train count.  Use the exact currencies

\[
\rho_{rec}=2S,
\qquad
\sigma_R=2T_R-4\sqrt{R_4}.
\tag{BP50.15}
\]

Then

\[
\boxed{
\rho_{rec}+\sigma_R=2T-4\sqrt{R_4}.
}
\tag{BP50.16}
\]

From the all-train half of (BP50.1),

\[
2T\ge q+2(2s+0.0050)D-o(D).
\]

Since `q>=q-k`, equation (BP50.2) applies, while

\[
\sqrt{R_4}/D\to s.
\]

Therefore

\[
\boxed{
\liminf {\rho_{rec}+\sigma_R\over D}
\ge L_{50}:=t_{50}+0.0100
=1.831850937979444\ldots .
}
\tag{BP50.17}
\]

This is the matched-`g` version of the lossless train-defect split.  It is an exact
composition; no new geometry is used here.

---

## 3. Subtract pure outer bridge singletons

Split the singleton trains as

\[
S=S_o+S_E,
\]

where `S_E` has a terminal incidence on a bounded nonquadrilateral face and `S_o` does
not.

A singleton train in `S_o` has no strict-rhombus continuation and no bounded
exceptional-face terminal incidence.  Its contact edge therefore has the unbounded face
on both sides and is an outer graph bridge.  Hence `S_o` injects into the outer bridge
set.

The hostile-audited bridge-subtracted isoperimetry on `main` gives, in the full-core
near-isodiametric branch,

\[
2S_o\le b-P_F+o(D).
\tag{BP50.18}
\]

Using `rho_rec=2S_o+2S_E` in (BP50.17), then subtracting (BP50.18), yields

\[
\boxed{
\sigma_R+2S_E+(b-P_F)
\ge(L_{50}-o(1))D.
}
\tag{BP50.19}
\]

At the low-`t` endpoint, (BP50.3) removes almost all outer-detour escape:

\[
\boxed{
\sigma_R+2S_E
\ge(1.829091787979444\ldots-o(1))D.
}
\tag{BP50.20}
\]

The symmetric two-block split already gives either

\[
\sigma_R/D\ge0.914545893989722\ldots-o(1)
\]

or

\[
S_E/D\ge0.457272946994861\ldots-o(1).
\]

The pentagon localization below is stronger for the branch we actually need.

---

## 4. Localize exceptional singleton trains to pentagons

Put

\[
X:=Q-f
=\sum_{\deg F\ge6}(\deg F-5).
\]

If `P_{>=6}` is the total bounded-face edge-occurrence count over exceptional faces of
degree at least six, then

\[
P_{\ge6}\le6X.
\tag{BP50.21}
\]

Indeed, with `n_d` the number of degree-`d` exceptional faces,

\[
P_{\ge6}=\sum_{d\ge6}d n_d
=X+5\sum_{d\ge6}n_d
\le6X.
\]

Let `S_5` count singleton trains with at least one pentagonal terminal incidence.
Every train in `S_E\setminus S_5` consumes at least one distinct terminal occurrence on
a degree-at-least-six face.  Thus

\[
\boxed{S_E\le S_5+6X.}
\tag{BP50.22}
\]

Insert (BP50.22) into (BP50.19):

\[
\sigma_R+2S_5+12X+(b-P_F)
\ge(L_{50}-o(1))D.
\tag{BP50.23}
\]

Now use both low-`t` caps in (BP50.3):

\[
X/D\le\delta_{50}+o(1),
\qquad
(b-P_F)/D\le\delta_{50}+o(1).
\]

Therefore

\[
\boxed{
\sigma_R+2S_5
\ge
\left(L_{50}-13\delta_{50}-o(1)\right)D
}
\tag{BP50.24}
\]

with

\[
\boxed{
L_{50}-13\delta_{50}
=1.795981987979444\ldots .
}
\tag{BP50.25}
\]

Equations (BP50.6)--(BP50.7) follow by a two-block split.

---

## 5. Rhombic branch has nearly half-`D^2` missing crossings

The exact rhombic rationalization is

\[
M_R={T_R^2\over4}-R_4
={\sigma_R\over8}
\left(4\sqrt{R_4}+{\sigma_R\over2}\right).
\tag{BP50.26}
\]

On the branch (BP50.6), use `sqrt(R_4)/D->s` and

\[
c_R:=0.897990993989722\ldots .
\]

Then

\[
\liminf {M_R\over D^2}
\ge {c_R\over8}\left(4s+{c_R\over2}\right)
=0.477983401092869\ldots,
\]

which proves (BP50.8).

This is a branch statement: the singleton-pentagon alternative may carry the train
defect instead.

---

## 6. Consequences on proof-only Groemer/odd-face overlays

The following two consequences use proof-only structural modules currently developed
on the advanced C-II research branches.  They are recorded as overlays, not promoted
here beyond those dependencies.

### 6.1 Singleton-anchored almost triangles on `R_F=o(D)`

The edgewise Groemer theorem says that on the small true force-hull residual branch
`R_F=o(D)`, all but `o(D)` singleton-hit pentagons admit an almost-equilateral source
triple whose exact unit base is that singleton train edge.  The conflict-graph
extraction retains at least one triple per 65 singleton-hit trains.  Hence (BP50.7)
implies a scale `eta_D->0` with

\[
\boxed{
{A^{sing}_{\eta_D}\over D}
\ge {0.448995496994861\ldots\over65}-o(1)
=0.006907623030690\ldots-o(1).
}
\tag{BP50.27}
\]

These triples are pairwise vertex-disjoint and satisfy

\[
|u-v|=1,
\qquad
|u-w|,|v-w|=1+o(1),
\]

with `uv` an exact singleton stopped-train edge.

### 6.2 Two-window escape

The odd-pentagon two-window lemma gives one off-window terminal occurrence on each
singleton-hit pentagon.  Its incidence conversion yields

\[
T_{off}\ge S_5/10.
\]

Thus branch (BP50.7) gives, for every fixed admissible pair of direction windows,

\[
\boxed{
T_{off}/D\ge0.044899549699486\ldots-o(1).
}
\tag{BP50.28}
\]

A three-phase lattice-like train system can still accommodate this much third-phase
mass, so (BP50.28) is not itself contradictory.  Its value is that the forced third
phase is attached to the same pentagons carrying the singleton defect.

---

## 7. Other propagated diagnostics

For reference, the matched endpoint also gives

\[
J/D\ge2.499509511845480\ldots-o(1),
\]

\[
H/D\ge1.500809367107288\ldots-o(1),
\]

and the corrected genuine residual cap

\[
(R_F+\Sigma_{ext})/D
\le {3\pi\over2}-t_{50}+o(1)
=2.890538042405245\ldots+o(1).
\]

The outer-tooth/long-side burden is almost stationary under the improved atomic gain:

\[
\max\{N_2,L_{>2}\}/D
\ge0.436235038536782\ldots-o(1).
\]

Using the merged shallow-tooth penetration theorem with `eta=0.02`, the tooth side of
this alternative forces at least

\[
\boxed{0.074569384634195\ldots D-o(D)}
\]

distinct inward penetration contacts.

Thus further scalar tuning of `g` is no longer a plausible closure mechanism.

---

## 8. Frontier

The low-`t` survivor has now been reduced to two source-geometric mechanisms:

```text
large rhombic branch:
    sigma_R >= 0.89799099 D
    -> M_R >= 0.47798340 D^2 missing train crossings;

pentagon-singleton branch:
    S_5 >= 0.44899549 D
    -> on R_F=o(D), at least 0.00690762 D
       vertex-disjoint almost-equilateral triples
       whose exact base is a singleton train edge.
```

The remaining missing implication is not numerical.  It must use one of:

1. a geometric theorem converting the large rhombic missing-crossing pattern into
   unavoidable area/diameter loss; or
2. a train-coupled activation theorem for the singleton-anchored near-triangle family.

Near-contact counting alone is insufficient: the existing generic Groemer extraction
already produces an even larger disjoint family without closing C-II.

**Disposition:** new proof-only closing reduction. C-II and Level I remain open.
