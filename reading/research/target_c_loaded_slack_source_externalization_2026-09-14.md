> Generated reading edition · [exact source](../../research/target_c_loaded_slack_source_externalization_2026-09-14.md) · source SHA-256 `aeb410ca83a2c3e840106d0f7b4a7b0d9757b01f9cb7af2e50b1ac7c0f570ae4`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f22f86b84644085d11d1fe8b6df24be0df1f877c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_loaded_slack_source_externalization_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "63b14e43003f7a6333dbb47d7c30c0c6f4499c1aeba342f598fedddc2dc85a9e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — loaded contact-degree slack externalizes to source objects

**Date:** 2026-09-14  
**Target:** C-II, canonical contact-minimal full-core Type-II branch  
**Dependencies:** canonical C35 loaded degree bound; loaded-chord elimination; loaded-unit inward-bisector squeeze; double-unit/flat-center overlap; bridge-subtracted isoperimetry; low-`t` degree-excess ledger  
**Claim class:** proof-only source-level reduction awaiting independent audit  
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The strongest current loaded-unit squeeze still leaves the abstract currency

```math
s_B:=\sum_{v\in B}(3-\deg_Cv).
```

This note removes it.  Canonical C35 gives `1<=deg_C(v)<=3` at every loaded force-hull vertex.  A degree-one loaded vertex must attach to an unloaded vertex.  A degree-two loaded vertex either has both hull sides as exact unit contacts, or also attaches to an unloaded vertex.  Thus loaded degree deficit itself creates physical loaded-to-unloaded unit contacts, except at degree-two double-unit corners.  The existing double-unit/flat-center theorem then converts those exceptional corners to loaded flat pentagon centers after explicit bridge, high-degree-face, and residual payments.

Let

- `B_1,B_2` be the loaded vertices of contact degree one and two;
- `C_11^(2)` be the contact-degree-two loaded vertices whose two adjacent loaded-hull sides are both exact unit contacts;
- `J_def` be a set containing one loaded-to-unloaded contact selected at every vertex of `B_1` and every vertex of `B_2\C_11^(2)`;
- `E_bis` be the strongly inward loaded-to-unloaded contacts from the loaded-unit inward-bisector theorem;
- `E_att:=J_def union E_bis`;
- `L_flat^bd` be the loaded flat-pentagon centers from the double-unit/flat-center theorem;
- `N_2` be the genuine two-edge outer-tooth count;
- `B_o` be the number of outer-face graph bridges;
- `X:=Q-f` be exceptional-face degree excess; and
- `R_F` be the true force-hull residual.

For the same fixed residual threshold `theta_*>0` used in the double-unit/flat-center theorem, every sufficiently large finite source obeys

```math
\boxed{
N_2+2|L_{flat}^{bd}|+4|E_{att}|
+4B_o+12X+{10R_F\over\theta_*}+16
\ge3q-b.
}
\tag{LS.1}
```

Thus `s_B` disappears completely.  Outside the explicit error budget, the loaded boundary must create an actual outer tooth, an actual loaded flat-pentagon center, or an actual loaded-to-unloaded unit contact.

On a convergent low-`t`, small-residual subsequence put

```math
t={q-k\over D},\qquad
\kappa={k\over D},\qquad
\delta={b-P_F\over D},\qquad
R_F=o(D),
```

and suppose an audited atomic gap `g` gives

```math
C_g:=2\sqrt{\Delta_2}+g,
\qquad \Delta_2={\pi\over2\sqrt3}.
```

Then bridge-subtracted isoperimetry and the exact low-`t` degree-excess ceiling turn (LS.1) into

```math
\boxed{
\liminf {N_2+2|L_{flat}^{bd}|+4|E_{att}|\over D}
\ge
11\pi+6C_g-24t+9\delta+6\kappa.
}
\tag{LS.2}
```

In particular,

```math
\boxed{
\liminf {N_2+2|L_{flat}^{bd}|+4|E_{att}|\over D}
\ge A_g(t):=11\pi+6C_g-24t.
}
\tag{LS.3}
```

Whenever `A_g(t)>0`,

```math
\boxed{
\liminf {1\over D}
\max\{N_2,|L_{flat}^{bd}|,|E_{att}|\}
\ge {A_g(t)\over7}.
}
\tag{LS.4}
```

Using the hostile-audited current value `g=0.002123` and

```math
t_{23}={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0017327,
```

we obtain

```math
\boxed{A_{0.002123}(t_{23})
=2.2881011603485408\ldots,}
```

so the three-way unweighted alternative in (LS.4) has coefficient
`0.3268715943355058...`.

The outer-tooth currency can also be removed.  For every fixed admissible shallow-tooth threshold `eta`, the penetration theorem gives

```math
N_2\le4E_{pen}(\eta)+{d_{out}\over\eta},
\qquad d_{out}=b-P_F.
\tag{LS.5}
```

Insert this into (LS.2):

```math
\boxed{
\liminf {4E_{pen}(\eta)+2|L_{flat}^{bd}|+4|E_{att}|\over D}
\ge
A_g(t)+\left(9-{1\over\eta}\right)\delta+6\kappa.
}
\tag{LS.6}
```

For `eta<1/9`, the coefficient of `delta` is negative.  The topology envelope

```math
2\delta+{\kappa\over2}\le
R_g(t):={9t\over2}-2\pi-C_g
\tag{LS.7}
```

shows that the right side of (LS.6) is minimized at `kappa=0`, `delta=R_g(t)/2`.  Hence

```math
\boxed{
\liminf {4E_{pen}(\eta)+2|L_{flat}^{bd}|+4|E_{att}|\over D}
\ge
B_g(t,\eta):=
A_g(t)+{1\over2}\left(9-{1\over\eta}\right)R_g(t).
}
\tag{LS.8}
```

Therefore, when `B_g(t,eta)>0`,

```math
\boxed{
\liminf {1\over D}
\max\{E_{pen}(\eta),|L_{flat}^{bd}|,|E_{att}|\}
\ge {B_g(t,\eta)\over10}.
}
\tag{LS.9}
```

At the hostile-audited `g=0.002123` endpoint and `eta=0.06`,

```math
B_{0.002123}(t_{23},0.06)
=2.2663502520152075\ldots,
```

so (LS.9) forces one of the three physical currencies at density at least
`0.2266350252015207...`.

---

## 1. Every unit of loaded degree deficit is physical

C35 gives

```math
1\le\deg_C(v)\le3
\qquad(v\in B).
\tag{LS.10}
```

Therefore

```math
s_B=2|B_1|+|B_2|.
\tag{LS.11}
```

Fix `v in B_1`.  If its unique contact joined another loaded vertex, loaded-chord elimination would make it an exact unit loaded-hull side.  But the loaded-unit endpoint lemma says every endpoint of such a side has contact degree at least two.  Contradiction.  Hence the unique contact at every degree-one loaded vertex joins an unloaded vertex.

Now fix `v in B_2`.  If both contacts joined loaded vertices, loaded-chord elimination makes both contacts loaded-hull sides.  A convex hull vertex has only its two adjacent hull sides, so both sides are exact unit contacts and `v in C_11^(2)`.  Consequently every vertex in `B_2\C_11^(2)` has at least one loaded-to-unloaded contact.

Choose one such edge at every vertex of `B_1` and `B_2\C_11^(2)`.  The choices are distinct because a loaded-to-unloaded edge has exactly one loaded endpoint.  Thus

```math
\boxed{
|J_{def}|\ge |B_1|+|B_2|-|C_{11}^{(2)}|.
}
\tag{LS.12}
```

Since `C_11^(2) subset B_2`,

```math
\begin{aligned}
2|J_{def}|+|C_{11}^{(2)}|
&\ge2|B_1|+2|B_2|-|C_{11}^{(2)}|\\
&\ge2|B_1|+|B_2|=s_B.
\end{aligned}
```

Therefore

```math
\boxed{s_B\le2|J_{def}|+|C_{11}^{(2)}|.}
\tag{LS.13}
```

No multiplier lower bound is used.

---

## 2. Pay only the degree-two double-unit corners

The proof of the double-unit/flat-center overlap theorem gives a sharper statement when restricted to degree-two double-unit corners.  Among `C_11^(2)`:

- at most eight have exterior turn at least `pi/4`;
- at most `2B_o` are lost to an incident outer bridge;
- at most `6X` incidences lie on nonpentagonal exceptional faces; and
- at most `5R_F/theta_*` incidences lie on high-residual pentagons.

Every remaining degree-two double-unit corner is exactly the distinguished loaded flat center of a cheap pentagonal exceptional face.  Hence

```math
\boxed{
|C_{11}^{(2)}|
\le
|L_{flat}^{bd}|+8+2B_o+6X+{5R_F\over\theta_*}.
}
\tag{LS.14}
```

This is strictly cheaper than paying all double-unit corners because degree-three corners contribute no `s_B` in the first place.

---

## 3. Insert into the exact loaded-unit squeeze

The inward-bisector theorem proves the finite inequality

```math
\boxed{N_2+2s_B+2|E_{bis}|\ge3q-b.}
\tag{LS.15}
```

Insert (LS.13):

```math
N_2+4|J_{def}|+2|C_{11}^{(2)}|+2|E_{bis}|
\ge3q-b.
\tag{LS.16}
```

Now insert (LS.14).  The selected sets `J_def` and `E_bis` are disjoint: their loaded endpoints have contact degree at most two and exactly three, respectively.  Thus

```math
|E_{att}|=|J_{def}|+|E_{bis}|.
\tag{LS.17}
```

Using `2|E_bis|<=4|E_bis|` gives precisely (LS.1).

The coefficient four on `E_att` is a deliberate safe unification of the two loaded-endpoint classes; no edge multiplicity is hidden.

---

## 4. Normalize the error budget

On `R_F=o(D)`, the residual term in (LS.1) is `o(D)`.  Bridge-subtracted outer-face isoperimetry gives

```math
\limsup {2B_o\over D}\le\delta,
\tag{LS.18}
```

so `4B_o/D<=2delta+o(1)`.

The low-`t` degree-excess ceiling is

```math
\boxed{
{x}:={X\over D}
\le {9t\over4}-\pi-{C_g\over2}-\delta-{\kappa\over4}+o(1).
}
\tag{LS.19}
```

Finally

```math
{3q-b\over D}
=3t+3\kappa-\pi-\delta+o(1).
\tag{LS.20}
```

Subtract the bridge and degree-excess payments in (LS.1):

```math
\begin{aligned}
&3t+3\kappa-\pi-\delta
-2\delta
-12\left({9t\over4}-\pi-{C_g\over2}-\delta-{\kappa\over4}\right)\\
&=11\pi+6C_g-24t+9\delta+6\kappa,
\end{aligned}
```

which proves (LS.2).

---

## 5. Eliminate the loaded-flat-center term too

The remaining loaded-flat-center term in (LS.6) is itself capacity-limited by the
singleton stopped-train population.  Let `L` be the full loaded flat-center class.
Then

```math
L_{flat}^{bd}\subseteq L,
\qquad
2|L|\le S,
\tag{LS.21}
```

where `S=T-T_R` is the singleton stopped-train count.  The exact terminal ledger and
`f<=Q` give

```math
\limsup {T\over D}\le5t-2\pi-2\delta,
\tag{LS.22}
```

while the same atomic-gap input gives

```math
\liminf {T_R\over D}\ge2\sqrt{\Delta_2}+g=C_g.
\tag{LS.23}
```

Therefore

```math
\boxed{
\limsup {|L_{flat}^{bd}|\over D}
\le {5t\over2}-\pi-\delta-\sqrt{\Delta_2}-{g\over2}.
}
\tag{LS.24}
```

Subtract twice (LS.24) from (LS.6).  With

```math
E_{src}(\eta):=E_{pen}(\eta)\cup E_{att},
\tag{LS.25}
```

we first obtain the sum-count inequality

```math
\boxed{
\liminf {4E_{pen}(\eta)+4|E_{att}|\over D}
\ge
13\pi+7C_g-29t
+\left(11-{1\over\eta}\right)\delta
+6\kappa.
}
\tag{LS.26}
```

Here every edge in `E_src(eta)` is an actual unit contact.  The `E_att` subfamily
consists of loaded-to-unloaded contacts.  The `E_pen` subfamily consists of the
physical tooth-penetration contacts from the shallow-tooth theorem.  No claim is made
that the two subfamilies are disjoint or that every `J_def` edge has the strong
bisector-angle bound enjoyed by `E_bis`.

For

```math
0<\eta<{1\over11},
\tag{LS.27}
```

the coefficient of `delta` in (LS.26) is negative.  Under the topology envelope

```math
2\delta+{\kappa\over2}\le
R_g(t):={9t\over2}-2\pi-C_g,
\tag{LS.28}
```

the right side is minimized at `kappa=0`, `delta=R_g(t)/2`.  Hence

```math
\boxed{
\liminf {4E_{pen}(\eta)+4|E_{att}|\over D}
\ge
C_g^{src}(t,\eta),
}
\tag{LS.29}
```

where

```math
\boxed{
C_g^{src}(t,\eta)
:=13\pi+7C_g-29t
+{1\over2}\left(11-{1\over\eta}\right)R_g(t).
}
\tag{LS.30}
```

Because

```math
|E_{pen}|+|E_{att}|\le2|E_{src}|,
```

(LS.29) gives the all-contact conclusion

```math
\boxed{
\liminf {|E_{src}(\eta)|\over D}
\ge {C_g^{src}(t,\eta)\over8}.
}
\tag{LS.31}
```

This is the strongest source externalization in the note: the loaded degree slack,
outer-tooth count, and loaded-flat-center count have all disappeared.

For the hostile-audited current value `g=0.002123`, at `t=t_23` and `eta=0.06`,

```math
\boxed{
\liminf {|E_{src}(0.06)|\over D}
\ge0.1694658916281856\ldots .
}
\tag{LS.32}
```

For comparison, the earlier independently hostile-audited `g=0.0021` value gives
`0.1694626707948523...`; the new audited refinement is slightly stronger.

---

## 6. Frontier effect

The endpoint has now been stripped of another bookkeeping currency:

```text
small R_F + low t
  -> a large weighted population of
       actual outer teeth,
       actual loaded flat-pentagon centers,
       actual loaded-to-unloaded contacts.
```

After the shallow-tooth and singleton-capacity conversions, even the outer-tooth and loaded-flat-center terms disappear.  Equation (LS.31) forces a linear population of actual unit contacts.  A substantial subfamily consists of loaded-to-unloaded attachments; the remaining tooth-penetration contacts have the explicit inward-normal geometry of the shallow-tooth theorem.

No contact multiplier lower bound is assumed.  The next useful target is therefore a packing, stress-transport, or deformation theorem for this linear physical contact population, preferably one that uses the simultaneous weak-contact family already forced by the flat-center branch.

---

## 7. Scope audit

- C35 supplies both `deg_C>=1` and `deg_C<=3` for loaded vertices in the canonical positive-contact core.
- Loaded-chord elimination is used only to classify loaded-loaded contacts as hull sides.
- The degree-one argument uses the exact loaded-unit endpoint lemma; it does not assume that every loaded vertex already has a unit hull side.
- `J_def` and `E_bis` count distinct physical loaded-to-unloaded contact edges.
- The degree-two double-unit payment reuses the finite incidence bounds from the committed double-unit/flat-center theorem.
- The normalized theorem additionally assumes the true small-residual branch `R_F=o(D)`.
- The current numerical specialization uses the hostile-audited `g=0.002123`; the symbolic formula accepts any later audited/certified gap with the same dependencies and corresponding lifecycle.
- No unit equilateral triangle or strict same-cardinality sub-`D` competitor is produced.

**Disposition:** new proof-only source-level reduction. C-II and Level I remain open.
