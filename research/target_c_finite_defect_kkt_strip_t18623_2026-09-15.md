<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8aa9f5011c2b7ed78d479d7d05ffe2f97444eee7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_finite_defect_kkt_strip_t18623_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0ae4b04f4bf306fdf689ef0ec9c3e101e0174bad2d934c69cb6257be9836369e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the `t<=1.8623` O–O path contains a finite-defect, low-KKT strip

**Date:** 2026-09-15  
**Status:** proof-only high-`t` finite-cusp strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8623`  
**Dependencies:** coupled adaptive O–O path through `1.8623`; exact stopped-train structure and endpoint handshake; exact laminar interval support; Hopf–Pannwitz; positive relative-interior KKT stress; Section-157 cut resultants; phase-free path-region saturation; diameter-path Helly hub  
**Certificate:** `research/verify_target_c_finite_defect_kkt_strip_t18623.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The coupled adaptive path theorem gives more than

\[
m>0.00066D-o(D)
\tag{FD.1}
\]

pairwise-disjoint outer-to-outer complete stopped trains on one simple complement-dual path. The previous consequence averaged only diameter support switches. This note also spends the exact global stopped-train terminal budget and the KKT switch-mass budget on the same internal path layer.

The result is a single nonhub region between consecutive selected O–O cuts whose entire non-rhombic/network obstruction is finite:

\[
\boxed{
N_i+L_i+D B_i<21730
}
\tag{FD.2}
\]

for all sufficiently large sources. Here

- `N_i` is the number of actual diameter rows starting or stopping between the two cuts;
- `L_i` is the number of complete-stopped-train terminal face-side occurrences assigned to the intervening region;
- `B_i` is the switching KKT diameter multiplier mass.

Consequently

\[
N_i\le21729,
\qquad
L_i\le21729,
\qquad
B_i<{21730\over D},
\tag{FD.3}
\]

and the exact Section-157 cut resultants satisfy

\[
\boxed{
\|F_{i+1}-F_i\|<21730.
}
\tag{FD.4}
\]

The same terminal bound has a network interpretation: the two boundary trains have crossing-neighborhood symmetric difference at most `21729`. Every transverse train which crosses one boundary but not the other must terminate in this finite-defect layer.

Thus the high-`t` branch now contains an exact finite-cusp object at the same `1.8623` endpoint as the modern pentagon sea.

---

## 1. Path layers

Use the `t<=1.8623` coupled adaptive path

\[
\tau_1,\ldots,\tau_m,
\qquad
m>0.00066D-o(D).
\]

Its proper O–O midpoint crosscuts are pairwise disjoint and totally ordered. Write the complementary regions in path order as

\[
R_0,R_1,\ldots,R_m,
\]

so internal region `R_i` lies between `tau_i` and `tau_{i+1}`.

The diameter-path Helly theorem supplies one common routing region `R_*`. Delete that one region from the averaging set. This costs only one index. Deleting the two end regions also costs only `O(1)`. Hence the number of eligible nonhub internal regions is still

\[
0.00066D-o(D).
\tag{FD.5}
\]

The phase-free path-region saturation theorem says every one of these regions contains an endpoint of an actual diameter edge. No layer selected below is KKT-invisible or diameter-empty.

---

## 2. Diameter switch-count budget

For an actual diameter edge `h`, let

\[
\varepsilon_{hj}\in\{-1,0,1\}
\]

be its signed incidence on selected cut `tau_j`. Exact laminar interval support gives one constant-sign interval:

\[
(\varepsilon_{h1},\ldots,\varepsilon_{hm})
=0,\ldots,0,s,\ldots,s,0,\ldots,0.
\]

Define

\[
N_i:=\#\{h:\varepsilon_{h,i+1}\ne\varepsilon_{hi}\}.
\]

Each diameter row changes at most twice, so

\[
\sum_iN_i\le2|H|.
\tag{FD.6}
\]

Hopf–Pannwitz gives `|H|<=q`, while every loaded force-hull side has length at least one and the force hull has diameter `D`; hence

\[
q\le\operatorname{per}(F)\le\pi D.
\]

Therefore

\[
\boxed{
\sum_iN_i\le2\pi D.
}
\tag{FD.7}

---

## 3. Exact global train-terminal budget

Let `T_tr` be the total number of complete stopped trains, including singleton trains. The audited exact stopped-train theorem gives

\[
T_{tr}={b+Q\over2}+2f.
\tag{FD.8}
\]

Canonical full-core bookkeeping gives

\[
b+Q=2(q-k),
\]

so with

\[
t={q-k\over D}
\]

one has the exact identity

\[
\boxed{
T_{tr}=tD+2f.
}
\tag{FD.9}
\]

Every complete stopped train is a path with exactly two terminal face-side occurrences. Hence the total occurrence-counted terminal population is

\[
2T_{tr}=2tD+4f.
\tag{FD.10}
\]

Every bounded nonquadrilateral face contributes at least one to

\[
Q=\sum_P(\deg P-4),
\]

so

\[
f\le Q.
\tag{FD.11}
\]

The loaded-hull perimeter ledger gives, uniformly for `t<=T`,

\[
{Q\over D}\le2T-\pi+o(1).
\tag{FD.12}
\]

At

\[
T=1.8623
\]

this yields

\[
\boxed{
{2T_{tr}\over D}
\le 10T-4\pi+o(1)
<6.0567+o(1).
}
\tag{FD.13}
\]

Assign every terminal face-side occurrence to one complement region. For bounded exceptional faces this assignment is canonical: selected O–O crosscuts run only through strict rhombi and the outer face and do not enter a bounded nonquadrilateral face, so the whole face lies in one path region and all of its terminal face-side occurrences are assigned there. Outer-face occurrences are assigned to the path region incident to their boundary subarc; the finitely many cut-endpoint ties may be broken arbitrarily.

Let `L_i` be the number assigned to internal region `R_i`. Then

\[
\boxed{
\sum_iL_i\le2T_{tr}.
}
\tag{FD.14}

In particular, if `mathcal F_i` is the set of bounded nonquadrilateral faces in `R_i`, then

\[
\boxed{
\sum_{P\in\mathcal F_i}\deg P\le L_i.
}
\tag{FD.15}
\]

Since every such face has degree at least five,

\[
|\mathcal F_i|\le L_i/5.
\tag{FD.16}
\]

---

## 4. KKT switch-mass budget

Normalize the positive relative-interior diameter stress by

\[
\sum_h\beta_h=1.
\]

Put

\[
B_i:=\sum_h\beta_h
|\varepsilon_{h,i+1}-\varepsilon_{hi}|.
\tag{FD.17}
\]

The same interval support gives

\[
\boxed{
\sum_iB_i\le2.
}
\tag{FD.18}
\]

Multiplying by `D`,

\[
\sum_iD B_i\le2D.
\tag{FD.19}
\]

For the coherently oriented Section-157 cut resultants,

\[
F_j=A_j u_j
=\sum_h\beta_h\varepsilon_{hj}r_h,
\qquad |r_h|=D.
\tag{FD.20}
\]

Therefore

\[
\boxed{
\|F_{i+1}-F_i\|
\le D B_i.
}
\tag{FD.21}
\]

The reverse triangle inequality also gives

\[
|A_{i+1}-A_i|\le D B_i.
\tag{FD.22}
\]

---

## 5. Joint averaging

For each eligible nonhub internal region define

\[
C_i:=N_i+L_i+D B_i.
\tag{FD.23}
\]

Using (FD.7), (FD.13), and (FD.19),

\[
\sum_iC_i
\le
\left[2\pi+(10T-4\pi)+2\right]D+o(D)
=
(10T-2\pi+2)D+o(D).
\tag{FD.24}
\]

At `T=1.8623`, divide by the path density in (FD.5). The exact Machin-arithmetic certificate proves

\[
{10T-2\pi+2\over0.00066}
<21727.
\tag{FD.25}
\]

Deleting `O(1)` path regions changes the denominator only by `o(D)`. Hence for every sufficiently large source some nonhub internal region satisfies

\[
\boxed{C_i<21730.}
\]

The deliberately rounded `21730` leaves several units of margin beyond the exact limiting average. Since `N_i,L_i` are integers, (FD.3) follows. Equations (FD.21)–(FD.22) give (FD.4) and the same bound for `|A_{i+1}-A_i|`.

Also, from (FD.16), this one strip contains at most

\[
\boxed{4345}
\]

bounded exceptional faces.

---

## 6. Finite crossing-neighborhood change

Let `Gamma(tau)` denote the set of complete stopped trains crossing a selected train `tau` in a strict rhombus.

Take a train

\[
\sigma\in\Gamma(\tau_i)\setminus\Gamma(\tau_{i+1}).
\]

At its unique crossing with `tau_i`, the midpoint path of `sigma` enters the intervening region `R_i`. Distinct complete trains meet in at most one rhombus, so `sigma` cannot leave `R_i` by crossing `tau_i` again. By assumption it does not cross `tau_{i+1}`. Since every complete stopped train is a path, `sigma` must therefore terminate on the outer or bounded exceptional boundary of `R_i`.

That terminal is one of the `L_i` terminal face-side occurrences. Distinct trains have distinct train-terminal occurrences. The same argument applies with `i` and `i+1` reversed. Thus

\[
\boxed{
|\Gamma(\tau_i)\triangle\Gamma(\tau_{i+1})|
\le L_i
\le21729.
}
\tag{FD.26}
\]

Equivalently, apart from at most `21729` defect trains, every train crossing one boundary of the strip also crosses the other. The bulk transverse train system is boundary-to-boundary.

---

## 7. Existing hub/reaction structure survives on this same strip

The selected region is nonhub. Therefore the path Helly theorem makes all switching diameter intervals one-sided toward the hub.

The adjacent-strip reaction nondegeneracy theorem applies to the same two cut boundaries. The strip's exact KKT layer reaction is nonzero. Planar conic Carathéodory then writes that reaction as a positive combination of one or two actual switching diameter bars.

Combining with (FD.2)–(FD.4), one source-level strip simultaneously has

```text
<=21729 switching actual diameter rows
+ switching KKT mass <21730/D
+ cut-resultant difference <21730
+ <=21729 complete-train terminal occurrences
+ <=4345 bounded exceptional faces
+ crossing-neighborhood symmetric difference <=21729 trains
+ every other transverse train crosses both strip boundaries
+ every diameter switch is one-sided toward the common hub
+ exact nonzero layer reaction generated by <=2 actual diameter bars.
```

This is a substantially smaller high-`t` closing target than the entire pentagon sea or the entire O–O path. It reduces the unresolved geometry to a fixed-complexity defect set embedded in an otherwise through-going rhombic train strip.

No claim is made yet that this finite-defect strip admits a strict diameter-decreasing deformation. That is now the concrete local/global-optimality obligation.

**Disposition:** proved a proof-only finite-defect, low-KKT, loaded nonhub strip through `t<=1.8623`. C-II and Level I remain open.
