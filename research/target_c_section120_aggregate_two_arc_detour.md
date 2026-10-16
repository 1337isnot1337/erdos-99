<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b7c4dd6650220580384843662fff0b18e0f35e6a", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section120_aggregate_two_arc_detour.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "851865968de4e66b8caee26ac44e7e7656109bca84af7fc5b688965bf809aeec"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — Section 120: aggregate the two-arc detour over the harmonic-cell tiling

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate.  
**Dependencies:** canonical Sections 62, 80, 83 and proof-only Section 116 two-arc zero-host transport.

Section 116 gives an exact all-regime route-excess inequality inside one harmonic
attachment cell. The full-core branch contains many harmonic cells, and Section 83
makes their unloaded-only strict-rhombus areas genuinely additive. Summing Section 116
over the actual cells therefore yields a source-level linear detour floor without
selecting a carrier, a phase bin, or a near-endpoint slack regime.

The point of the theorem is not a new carrier constant. It converts the entire
quadratic Type-II rhombic area into one aggregate outer-walk currency.

---

## 120.1 Local notation

Let `I_r` range over the unloaded positive-contact components of the canonical post-ZF
representative. Put

\[
A_r\subset B,
\qquad
P_r:=\operatorname{conv}(A_r),
\qquad
d_r:=\operatorname{diam}(P_r).
\]

Let `H_r` be the induced positive-contact graph on `I_r\cup A_r`, including every
loaded-loaded unit contact with both endpoints in `A_r`. Write

- `L_r` for the occurrence-counted outer-face walk length of `H_r`;
- `P_{{\rm exc},r}` for the total boundary degree of the bounded
  nonquadrilateral faces of `H_r`; and
- `A_{4,r}` for the total area of all bounded strict-rhombus faces of `H_r`.

Canonical Section 62 gives `|A_r|>=3` and harmonic trapping `P_r\subset F`; hence
`d_r>0` and

\[
0<d_r\le D.
\tag{120.1}
\]

Define the local two-arc detour

\[
E_r:=L_r+P_{{\rm exc},r}-2d_r.
\tag{120.2}
\]

Proof-only Section 116 gives the exact finite inequality

\[
\boxed{
d_rE_r\ge(4-2\sqrt3)A_{4,r}.
}
\tag{120.3}
\]

In particular `E_r>=0`.

---

## 120.2 Use only unloaded-only rhombi to make the sum injective

A bounded strict rhombus of the full positive-contact core is called
**unloaded-only** if all four of its vertices are unloaded. Let `A_4^0` be the total
area of all unloaded-only strict rhombi.

Every unloaded-only rhombus has a connected four-cycle of unloaded contact vertices,
so all four vertices lie in one and only one unloaded component `I_r`. Consequently
its face occurs in the corresponding induced graph `H_r`. Distinct unloaded
components have disjoint unloaded vertex sets, so an unloaded-only rhombus cannot be
assigned to two different cells.

Let `A_{4,r}^0` be the total area of the unloaded-only rhombi assigned to `I_r`.
Then

\[
0\le A_{4,r}^0\le A_{4,r},
\qquad
\boxed{\sum_r A_{4,r}^0=A_4^0.}
\tag{120.4}
\]

This is the only area sum used below. Rhombi incident to loaded vertices are simply
discarded; no claim is made that the full local quantities `A_{4,r}` are globally
disjoint.

Applying (120.3), then (120.4), gives

\[
E_r
\ge(4-2\sqrt3){A_{4,r}\over d_r}
\ge(4-2\sqrt3){A_{4,r}^0\over d_r}.
\]

Summing over all unloaded components yields the finite aggregate theorem

\[
\boxed{
\sum_r E_r
\ge
(4-2\sqrt3)\sum_r{A_{4,r}^0\over d_r}.
}
\tag{120.5}
\]

Since `d_r<=D`, this immediately implies

\[
\boxed{
\sum_r\bigl(L_r+P_{{\rm exc},r}-2d_r\bigr)
\ge
{4-2\sqrt3\over D}\,A_4^0.
}
\tag{120.6}
\]

Equation (120.5) is strictly stronger than (120.6) whenever a positive area fraction
lies in cells of diameter bounded away from `D`.

---

## 120.3 Type-II consequence

Work along a Type-II full-core sequence. Canonical Section 80 gives

\[
{A_4\over D^2}\longrightarrow{\pi\over4}.
\tag{120.7}
\]

Canonical Section 83 proves that only `O(D)` strict rhombi are incident to the loaded
set. Every unit rhombus has area at most one, so

\[
A_4-A_4^0=O(D).
\tag{120.8}
\]

Therefore

\[
{A_4^0\over D^2}\longrightarrow{\pi\over4}.
\tag{120.9}
\]

Divide (120.6) by `D` and use (120.9):

\[
\boxed{
\liminf_{D\to\infty}
{1\over D}
\sum_r\bigl(L_r+P_{{\rm exc},r}-2d_r\bigr)
\ge
{\pi\over4}(4-2\sqrt3).
}
\tag{120.10}
\]

Equivalently,

\[
\boxed{
\liminf_{D\to\infty}
{1\over D}
\sum_r\bigl(L_r+P_{{\rm exc},r}-2d_r\bigr)
\ge
{\pi\over2}(2-\sqrt3)
=0.42089\ldots .
}
\tag{120.11}
\]

The decimal is only for scale; (120.10) is the theorem.

No selection of a distinguished harmonic carrier is needed. The bound is all-regime
and uses the complete Type-II rhombic mass up to the canonical `O(D)` loaded-touching
loss.

---

## 120.4 What the theorem does and does not buy

The aggregate lower bound removes one escape from the Section-116 route: the required
return detour cannot be hidden by distributing the quadratic rhombic area among many
harmonic cells. The total actual local outer-walk/nonquadrilateral detour is always
linear with the explicit coefficient in (120.10).

It does **not** yet contradict the canonical attachment ledgers. Summing the exact
local face identity

\[
L_r+Q_r=4a_r-6-2s_r-2c_r
\]

and using only the present global incidence bounds leaves an upper capacity of order
`q=O(D)` with a coefficient much larger than (120.10). In particular, the coarse
estimate `q<=\pi D` is nowhere near sufficient. A closing theorem still needs one of

1. an upper bound on the **same aggregate detour** from global diameter minimality;
2. a theorem showing that a fixed positive fraction of `A_4^0` lies in cells with
   `d_r<=\lambda D` for some useful `\lambda<1`, strengthening (120.5);
3. an injective transport from the aggregate cell detour into the already limited
   global interface/diameter-load currency; or
4. a source-preserving deformation showing that the forced aggregate detour permits a
   strict decrease of the old diameter-carrying core.

Thus Section 120 is structural progress, not C-II closure.

---

## 120.5 Dependency and regression audit

- **Section 116 scope:** (120.3) is used only on one actual harmonic induced graph at a
  time. No extension of the ZR/ZF affine-kernel theorem to isolated source points is
  involved.
- **Source retention:** no source point is deleted or moved. Contact-isolated source
  points remain part of the full configuration throughout.
- **Area injectivity:** only unloaded-only rhombi are summed. This avoids any possible
  repeated use of a loaded-touching rhombus by overlapping attachment sets.
- **Boundary occurrence injectivity:** none is assumed across cells. Equation (120.5)
  is a sum of already valid scalar inequalities; it does not interpret equal physical
  boundary edges in different induced graphs as distinct global resources.
- **Cell diameters:** `d_r<=D` follows from `P_r\subset F\subset conv(A)` and is the
  only global diameter comparison used.
- **Type-II asymptotics:** (120.7) and the `O(D)` loaded-touching loss are canonical
  Section-80/83 inputs. Section 120 does not change theorem authority.
- **No numerical carrier optimization:** the coefficient comes from the exact
  two-arc return constant and the full Type-II area limit, not from improving `mu`.

**Disposition:** proof-only research candidate. C-II remains open.
