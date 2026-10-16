<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f03b9e7124b532ba16296fb7bc5b42a1180f58d2", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_thin_common_spine_ladder_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e342830716f4d7042444eac392e0986a85ae1ee1bf156cf2ccccc3397a839cfe"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — THIN obstruction forces one blocker and one train through linearly many phase-pure rows

**Date:** 2026-09-17  
**Status:** proof-only continuation of the THIN rich-cut theorem; no canonical promotion claimed  
**Scope:** THIN side of the 15-spaced one-sign strong-TB1 Horn upper family through `t=(q-k)/D<=1.8687`  
**Dependencies:** THIN rich-cut phase synchronization; global angular-defect budget; global complete-train count; high-`t` crossing-neighbor floor; exact path support  
**Certificate:** `research/verify_target_c_high_t_tb1_thin_common_spine_ladder_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The THIN rich-cut theorem was used previously to choose one blocker-rich row with `O(1)` total angular defect. The same incidence count contains more information. There are linearly many blocker-rich rows, so a positive fraction of them have uniformly bounded total defect. Purify each such row separately, then double-count

\[
(\text{row},\text{THIN blocker},\text{good transverse train})
\]

triples.

The result is a single THIN blocker `e_*` and a single complete stopped train `b_*` that both cross a **linear number of the same selected O--O rows**. At every one of those rows the `b_*` crossing rhombus is inverse-`D` near-equilateral. After one two-color phase split, all those rows have one common projective phase to `O(D^-1)`.

Put

\[
\gamma={791\over9{,}600{,}000{,}000},
\qquad
p_0=0.6436={1609\over2500},
\qquad
T_*=3.0605={6121\over2000}.
\tag{SL.1}
\]

If `N_D` is the THIN owned-blocker population from the rich-cut theorem, then

\[
N_D>\left({\gamma\over16}-o(1)\right)D.
\tag{SL.2}

Define

\[
\boxed{
\kappa:={3p_0\over10T_*}
={9654\over153025}
=0.0630877307629\ldots .
}
\tag{SL.3}
\]

Then there are one blocker `e_*`, one complete train `b_*`, and a selected-row family `A_D` satisfying

\[
\boxed{|A_D|>(\kappa-o(1))N_D.}
\tag{SL.4}

After fixing one of the two possible row phases relative to `b_*`, there remains

\[
\boxed{|A_D^{\rm phase}|>
\left({\kappa\over2}-o(1)\right)N_D}
\tag{SL.5}
\]

rows. In diameter scale,

\[
\boxed{
|A_D^{\rm phase}|>
\left(
{1{,}272{,}719\over7{,}834{,}880{,}000{,}000{,}000}
-o(1)
\right)D
}
\tag{SL.6}

with numerical coefficient

\[
\boxed{1.62442692166\ldots\times10^{-10}.}
\tag{SL.7}

Every row in `A_D^{phase}` simultaneously has:

```text
- the same THIN almost-diameter e_* crossing it;
- the same complete train b_* crossing it;
- b_* x row acute angle pi/3 + O(1/D), uniformly;
- one common projective row phase up to O(1/D);
- > (1/5-o(1)) N_D THIN blocker chords crossing it;
- > (0.6436-o(1))D individually purified transverse columns;
- and the usual rowwise circumcenter flank populations.
```

Thus the THIN branch contains a linear-height near-equilateral ladder with two fixed transversals: one is an inactive almost-diameter straight chord, the other is an actual complete contact train.

This is stronger than a single phase-pure rich row. It does not yet say that `e_*` intersects `b_*`, nor that their crossing points with the common rows stay at bounded train distance. That relative-position problem is the new seam.

---

## 1. Recall the rich-row incidence theorem

Let `T_D` be the full THIN owned-blocker family and write

\[
N:=|T_D|.
\]

The rich-cut theorem proves that there is a set `Q_D` of distinct selected O--O rows with

\[
\boxed{|Q_D|>(3-o(1))N}
\tag{SL.8}
\]

such that every `a in Q_D` is supported by more than

\[
\boxed{\left({1\over5}-o(1)\right)N}
\tag{SL.9}

THIN blockers from `T_D`.

For a row `a`, let

\[
F_a=\sum_{b\in\Gamma_a}\delta_{ab}
\]

be its full strict-rhombus angular-defect sum. The global budget is

\[
\sum_a F_a\le C_{\rm phase}D,
\qquad
C_{\rm phase}={\pi^2\sqrt3(2+\sqrt3)\over12}.
\tag{SL.10}

Also

\[
N>\left({\gamma\over16}-o(1)\right)D.
\tag{SL.11}

Therefore the average `F_a` over `Q_D` is bounded by

\[
{C_{\rm phase}D\over|Q_D|}
< {16C_{\rm phase}\over3\gamma}+o(1).
\tag{SL.12}

The right-hand constant is the previous

\[
H_{\rm thin}=344128111.925\ldots .
\]

---

## 2. Linearly many rich rows have a uniform `O(1)` defect bound

Set, for definiteness,

\[
\boxed{
H_0={32C_{\rm phase}\over3\gamma}+1.
}
\tag{SL.13}

For all sufficiently large sources, Markov's inequality applied to (SL.12) shows that at least half of the rows in `Q_D` satisfy

\[
F_a\le H_0.
\]

Let `R_D` be this low-defect rich-row set. Then

\[
\boxed{|R_D|>\left({3\over2}-o(1)\right)N.}
\tag{SL.14}

Every row in `R_D` still has the blocker lower bound (SL.9).

The high-`t` crossing-neighbor floor gives

\[
|\Gamma_a|>(0.6536-o(1))D
\tag{SL.15}

for every retained row.

Delete from `Gamma_a` every column with

\[
\delta_{ab}>{100H_0\over D}.
\tag{SL.16}

Because `F_a<=H_0`, at most `0.01D` columns are deleted. Thus each low-defect rich row has a purified column set `P_a` with

\[
\boxed{|P_a|>(p_0-o(1))D,
\qquad p_0=0.6436,}
\tag{SL.17}

and

\[
\boxed{
0<\theta(a,b)-{\pi\over3}
\le {100H_0\over D}
\qquad(b\in P_a).
}
\tag{SL.18}

The threshold constant is source-independent.

---

## 3. Triple counting forces one blocker-train pair through many rows

For `a in R_D`, let `B_a subset T_D` be the THIN blockers whose exact path support contains `a`. By (SL.9),

\[
|B_a|>\left({1\over5}-o(1)\right)N.
\tag{SL.19}

Count triples

\[
(a,e,b)
\]

with

\[
a\in R_D,
\qquad
e\in B_a,
\qquad b\in P_a.
\]

Equations (SL.14), (SL.17), and (SL.19) give

\[
\boxed{
\#\{(a,e,b)\}
>
\left({3p_0\over10}-o(1)\right)N^2D.
}
\tag{SL.20}

The audited global complete-train count gives at most

\[
(T_*+o(1))D
\tag{SL.21}

possible complete trains `b`. There are exactly `N` possible blockers `e`. Hence there are at most

\[
(T_*+o(1))ND
\]

blocker-train pairs `(e,b)`.

Pigeonhole applied to (SL.20) yields one pair

\[
\boxed{(e_*,b_*)}
\tag{SL.22}

which occurs with more than

\[
\boxed{
\left({3p_0\over10T_*}-o(1)\right)N
=(\kappa-o(1))N
}
\tag{SL.23}

rows. Call this row set `A_D`.

For every `a in A_D`:

- `e_*` has endpoints in path regions separated by `a`, so the straight segment `e_*` crosses the selected O--O crosscut `a` geometrically;
- `b_* in P_a`, so the complete train `b_*` crosses `a` in a strict rhombus satisfying (SL.18).

Thus `e_*` and `b_*` are two fixed transversals of the same linearly large ordered row family.

The exact constant is

\[
\kappa
={3(1609/2500)\over10(6121/2000)}
={9654\over153025}.
\tag{SL.24}

---

## 4. One more factor two gives one inverse-`D` row phase

A complete train has one fixed projective track-edge direction. Let `[v_*]` be the projective direction of `b_*`.

For every `a in A_D`, equation (SL.18) says that the acute angle between the row direction `[u_a]` and `[v_*]` is

\[
{\pi\over3}+O(D^{-1}).
\]

Relative to `[v_*]`, there are only two possible projective sides for a row with this acute angle. Split `A_D` by those two phase signs and retain the larger class `A_D^{phase}`. Then

\[
\boxed{
|A_D^{phase}|>
\left({\kappa\over2}-o(1)\right)N.
}
\tag{SL.25}

After choosing one oriented representative `u_*^\dagger`, uniformly over this class

\[
\boxed{
 d_{\mathbb{RP}^1}([u_a],[u_*^\dagger])=O(D^{-1}).
}
\tag{SL.26}

So the common-spine extraction synchronizes the row phase across linearly many separated rich cuts, not merely across one row.

Using (SL.11),

\[
|A_D^{phase}|>
\left({\kappa\gamma\over32}-o(1)\right)D.
\tag{SL.27}

Since

\[
{\kappa\gamma\over32}
={1{,}272{,}719\over7{,}834{,}880{,}000{,}000{,}000}
=1.62442692166\ldots\times10^{-10},
\]

this proves (SL.6)--(SL.7).

---

## 5. Geometry retained by the fixed THIN blocker

The selected blocker `e_*` belongs to the THIN family, so

\[
\boxed{
D-{1\over4D}<|e_*|<D.
}
\tag{SL.28}

In particular

\[
|e_*|>\sqrt{D^2-1}.
\]

Therefore both endpoints of `e_*` are convex-hull vertices. The standard near-diameter midpoint estimate also gives

\[
\boxed{
\left|m(e_*)-o\right|=O(D^{3/4}).
}
\tag{SL.29}

Every row in `A_D^{phase}` belongs to the exact selected-cut support interval of this **same** chord. Hence the chord traverses a linear-height ordered stack of pairwise disjoint O--O rows whose phases have collapsed to one inverse-`D` cone relative to the same complete train `b_*`.

The row family is not asserted consecutive. Its cardinality is linear, and its order is inherited from the selected path.

---

## 6. Every common row remains blocker-rich and locally dense

The choice of `(e_*,b_*)` did not thin the blocker or column populations attached to its rows. For every `a in A_D^{phase}` we still have

\[
\boxed{|B_a|>\left({1\over5}-o(1)\right)N}
\tag{SL.30}

and

\[
\boxed{|P_a|>(0.6436-o(1))D.}
\tag{SL.31}

Thus the same common row stack is simultaneously:

- traversed by one fixed almost-diameter straight chord;
- traversed by one fixed complete train;
- inverse-`D` co-phased;
- individually crossed by linearly many THIN blockers;
- and individually equipped with a dense near-equilateral transverse train family.

Because `0.6436>1.02/sqrt(3)`, the standard train-step/circumdisk capacity argument can also be applied rowwise to every `P_a`: each such row has positive-density crossing-center populations below `-0.01D` and above `+0.01D` in its own oriented row-normal coordinate. These flank **column identities need not be common across different rows**; only the spine train `b_*` is common by construction.

---

## 7. Frontier effect

The previous THIN normal form concentrated a linear blocker family on one phase-pure row. The new double count produces a different concentration:

```text
one THIN almost-diameter straight chord e_*;
one complete stopped train b_*;
Theta(D) selected O--O rows A_D^phase;
e_* crosses every one of those rows;
b_* crosses every one of those rows;
all those b_* x row rhombi are pi/3 + O(1/D);
all retained rows share one projective phase to O(1/D);
each row still supports Theta(D) THIN blockers;
each row still carries >0.6436D purified transverse trains.
```

This converts the THIN branch from a one-row concentration into a linear-height two-transversal ladder.

The missing theorem is now a relative-position statement for the two fixed transversals. Nothing here proves that the straight chord `e_*` meets the train `b_*`, or that their crossing points with the common rows stay within bounded train distance. A closing continuation should exploit the facts that `e_*` is almost diametrical and straight, `b_*` is a complete unit-rhombus train, and the intervening common rows are pairwise disjoint and inverse-`D` co-phased.

**Disposition:** double-counted the linear rich-cut family to force one THIN chord and one complete train through linearly many common inverse-`D` phase rows. C-II and Level I remain open.
