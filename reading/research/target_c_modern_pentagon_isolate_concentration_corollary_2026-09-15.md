> Generated reading edition · [exact source](../../research/target_c_modern_pentagon_isolate_concentration_corollary_2026-09-15.md) · source SHA-256 `d795e5d05af0b4cde56a0cfc25afda07da4057b637fdcfd620e44e49fec93634`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3b58d923f06c48a5704d3e88c5b20014c69e2062", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_modern_pentagon_isolate_concentration_corollary_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f733377e7b10b41f8565ee42a28c59a0393d4a32c1d7f154a14f2939decd1a3c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — modern high-`t` pentagon sea is isolate-free and forces isolate-host concentration

**Date:** 2026-09-15  
**Status:** proof-only composition corollary  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch in the modern bounded-`t` staircase  
**Dependencies:** `target_c_isolate_host_face_degree7_2026-09-15.md`; current modern all-train pentagon-sea certificate through `t<=1.8623`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The exact isolate-host theorem proves that bounded contact faces of degree five or six contain no assigned contact-isolated source point.  The current all-train ledger independently forces a very large bounded pentagon population in the live high-`t` branch.  Combining them gives a sharper normal form than either statement alone:

- a linear sea of actual bounded pentagons is completely empty of source points in its interior;
- all bounded-face isolate mass is concentrated in a much smaller family of degree-`>=7` faces;
- almost one full `D`-scale of stopped trains terminate on isolate-free pentagons at the widest certified endpoint.

## 1. Modern all-train face data

The current exact pentagon-sea certificate gives the safe staircase

$$
\begin{array}{c|c|c|c|c}
T & f/D\text{ lower} & Q/D\text{ upper} & P_5/D\text{ lower} & P_5/f\text{ lower}\\ \hline
1.850  & 0.493 & 0.558408 & 0.428 & 0.86\\
1.855  & 0.492 & 0.568408 & 0.416 & 0.84\\
1.860  & 0.491 & 0.578408 & 0.403 & 0.82\\
1.8623 & 0.490 & 0.583008 & 0.398 & 0.81.
\end{array}
\tag{MIC.1}
$$

The same certificate proves at `T=1.8623` that more than

$$
\boxed{0.99D-o(D)}
\tag{MIC.2}
$$

distinct all-stopped trains touch pentagonal faces.

## 2. Every one of those pentagons is source-empty

Let `P` be one bounded pentagonal contact face.  The degree-`>=7` isolate-host theorem gives

$$
z_P=0.
$$

Canonical face assignment says every source point in `int P` would be one of those assigned contact-isolates.  Therefore

$$
\boxed{A\cap\operatorname{int}P=\varnothing.}
\tag{MIC.3}
$$

Thus `P` is not merely an exceptional contact chamber with no counted rattler mass; its open interior contains **no source point at all**.

Consequently every pentagon counted in (MIC.1), including every pentagon touched by the train family in (MIC.2), is an empty convex unit-edge hole in the positive-contact core.

## 3. All bounded-face isolate hosts fit inside `(Q-f)/2`

Let

$$
f_{iso}:=\#\{P:z_P>0\}.
$$

The exact local theorem gives

$$
f_{iso}\le{Q-f\over2}.
\tag{MIC.4}
$$

Using the certified safe rows of (MIC.1):

$$
\boxed{
t\le1.850\Longrightarrow f_{iso}<0.03271D+o(D),}
\tag{MIC.5}
$$

$$
\boxed{
t\le1.855\Longrightarrow f_{iso}<0.03821D+o(D),}
\tag{MIC.6}
$$

$$
\boxed{
t\le1.860\Longrightarrow f_{iso}<0.04371D+o(D),}
\tag{MIC.7}
$$

and

$$
\boxed{
t\le1.8623\Longrightarrow f_{iso}<0.04651D+o(D).}
\tag{MIC.8}
$$

The arithmetic is exact at the rounded parent level.  For example,

$$
{0.583008-0.490\over2}=0.046504<0.04651.
$$

A Pyroam `Fraction` regression checks all four displayed margins.

## 4. Quantitative separation of roles

At the widest endpoint, (MIC.1) and (MIC.8) give simultaneously

$$
P_5>0.398D-o(D)
$$

and

$$
f_{iso}<0.04651D+o(D).
$$

Hence there are more than eight times as many empty pentagonal defect faces as there are bounded faces capable of hosting even one isolate.

More importantly, the two populations have disjoint roles:

```text
>0.398 D empty pentagonal holes
+ isolate-free degree-6 exceptional faces
+ <0.04651 D possible bounded isolate-host chambers, all degree >=7
+ >0.99 D distinct stopped trains touching the empty pentagon sea.
```

No isolate multiplicity bound inside one degree-`>=7` host is asserted.

## 5. Frontier consequence

The modern high-`t` obstruction can no longer treat exceptional faces as one homogeneous Oler reservoir.  In the certified staircase, most bounded exceptional faces are empty degree-5 holes, while every inactive source point assigned to a bounded face must be stored in a sparse high-degree subfamily.

This sharpens two current closure routes:

1. **train/defect coupling:** the stopped-train terminal population is overwhelmingly incident to genuinely empty pentagonal holes, so it can be studied without an unknown interior source packing;
2. **inactive-packing concentration:** any substantial bounded-face isolate population must concentrate into fewer than `0.04651D+o(D)` degree-`>=7` hosts through `t<=1.8623`.

The statement is still structural: one high-degree near-geodesic face may store many isolates, and empty pentagons can be geometrically close to the known thin-corridor regressions.  No C-II contradiction is claimed.

**Disposition:** exact composition of the degree-`>=7` isolate-host theorem with the modern all-train pentagon sea. C-II and Level I remain open.
