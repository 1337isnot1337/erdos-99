> Generated reading edition · [exact source](../../research/target_c_exceptional_singleton_two_window_gate_2026-09-14.md) · source SHA-256 `12dbd6ad29a55e24ac261a6394edad672b210fd3a29d95198b5936edf1c81dd1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c1df7a886044c89972338d0450715713a8a80235", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_exceptional_singleton_two_window_gate_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d98445148bc4b11792697d74de7d5bfa470a9590751db8798bf017523dcd9c18"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdos Problem #99 - exceptional-singleton two-window gate

**Date:** 2026-09-14
**Repository base:** `8e628641`
**State version:** `2026-09-14.audit.51`
**Run type:** closing-proof reduction / exact exceptional-face incidence composition
**Target:** Target C-II, canonical full-core Type-II branch
**Claim class:** proved candidate awaiting independent audit
**External literature:** no new import
**Computation:** dependency-free arithmetic and incidence regression only

## LEVEL I STATUS

`STILL OPEN`

The q-k amplified bridge-subtracted theorem gives

$$
\sigma_R+2S_E+(b-P_F)\ge (L_*-o(1))D,
\qquad L_*=1.821728637979444\ldots .
\tag{EW.1}
$$

Here `S_E` is the number of singleton stopped trains with at least one terminal
incidence on a bounded nonquadrilateral face. Put `X:=Q-f`. We prove

$$
\boxed{\sigma_R+(b-P_F)+2S_5+12X\ge(L_*-o(1))D,}
\tag{EW.2}
$$

where `S_5` counts singleton stopped trains with at least one pentagonal terminal
incidence. Combining this with the odd-face two-window lemma yields, for every fixed
pair of projective directions `[u],[v]` and every fixed
`0<epsilon<2 arcsin(1/10)`,

$$
\boxed{\sigma_R+(b-P_F)+12(Q-f)+20T_{off}(u,v;\epsilon)
\ge(L_*-o(1))D.}
\tag{EW.3}
$$

`T_off` counts complete stopped trains whose projective direction lies outside both
`epsilon`-windows. Thus a two-window model cannot hide the exceptional-singleton
branch: small off-window population must be paid by outer detour, high-degree face
excess, or rhombic non-Mantel slack.

## 1. Degree-excess bookkeeping

For `d>=5`, let `n_d` be the number of bounded nonquadrilateral contact faces of degree
`d`. Then

$$
f=\sum_{d\ge5}n_d,\qquad Q=\sum_{d\ge5}(d-4)n_d,
$$

so

$$
\boxed{X=Q-f=\sum_{d\ge6}(d-5)n_d\ge0.}
\tag{EW.4}
$$

Let `N_{>=6}=sum_{d>=6}n_d` and let `P_{>=6}` be the total boundary edge-occurrence
count on faces of degree at least six. Then

$$
P_{\ge6}=\sum_{d\ge6}dn_d=X+5N_{\ge6}.
\tag{EW.5}
$$

Every such face contributes at least one to `X`, so `N_{>=6}<=X`. Therefore

$$
\boxed{P_{\ge6}\le6X.}
\tag{EW.6}
$$

The coefficient six is sharp at the level of degree data: one hexagon contributes six
boundary occurrences and one unit to `Q-f`.

## 2. Localize exceptional singleton trains

Define `S_5` as above. Every train in `S_E\setminus S_5` has no pentagonal terminal
incidence but has, by the definition of `S_E`, at least one terminal incidence on a
face of degree at least six. Choose one such incidence per train. Distinct complete
stopped trains have distinct terminal edge-side incidences, hence

$$
S_E-S_5\le P_{\ge6}\le6X.
$$

Thus

$$
\boxed{S_E\le S_5+6(Q-f).}
\tag{EW.7}
$$

Insert this upper bound into the right side of (EW.1):

$$
L_*D-o(D)
\le\sigma_R+(b-P_F)+2S_E
\le\sigma_R+(b-P_F)+2S_5+12(Q-f),
$$

which proves (EW.2). This uses actual global contact-face incidences only. It does not
identify them with induced attachment-cell faces from Section 123.

## 3. Pentagon incidence gives two-window escape

Let `p_5^{hit}` be the number of bounded pentagons incident with at least one singleton
train counted by `S_5`. Every `S_5` train touches at least one such pentagon, while a
pentagon has only five boundary edges. Therefore

$$
\boxed{p_5^{hit}\ge S_5/5.}
\tag{EW.8}
$$

Fix `[u],[v]` and `epsilon<epsilon_5:=2 arcsin(1/10)`. The odd-face two-window lemma
supplies at least one off-window boundary-edge occurrence on every pentagon. Applied
to the `p_5^{hit}` pentagons, this gives at least `p_5^{hit}` off-window exceptional
terminal occurrences. A complete stopped train has at most two terminal incidences,
so

$$
T_{off}(u,v;\epsilon)\ge p_5^{hit}/2\ge S_5/10.
\tag{EW.9}
$$

Equivalently,

$$
\boxed{S_5\le10T_{off}(u,v;\epsilon).}
\tag{EW.10}
$$

Since the right side of (EW.2) only increases when `2S_5` is replaced by
`20T_off`, equation (EW.3) follows.

The escaping edge need not be the singleton edge that made the pentagon belong to
`p_5^{hit}`. The singleton population is used only to force many distinct pentagons;
the parity lemma is then applied independently to those pentagons.

## 4. Uniform four-currency gate

The coefficients in (EW.3) sum to `34`. Hence pointwise along every sufficiently
large full-core sequence,

$$
\max\left\{
{\sigma_R\over D},
{b-P_F\over D},
{Q-f\over D},
{T_{off}(u,v;\epsilon)\over D}
\right\}
\ge {L_*\over34}-o(1).
\tag{EW.11}
$$

Numerically,

$$
\boxed{L_*/34=0.053580253\ldots .}
\tag{EW.12}
$$

Thus every fixed two-window model pays a linear amount in at least one of four actual
source-derived defects.

A stronger conditional form is useful. If along a subsequence

$$
T_{off}=o(D),\qquad Q-f=o(D),
$$

then

$$
\boxed{\sigma_R+(b-P_F)\ge(L_*-o(1))D.}
\tag{EW.13}
$$

After selecting a branch, one of these two currencies has scale at least

$$
L_*/2=0.910864318989722\ldots .
\tag{EW.14}
$$

If additionally `b-P_F=o(D)`, then `sigma_R>=(L_*-o(1))D`, which through

$$
M_R={\sigma_R\over8}\left(4\sqrt{R_4}+{\sigma_R\over2}\right)
$$

forces a very large quadratic Mantel deficit. This remains a structural alternative,
not a contradiction.

## 5. Scope and next target

- The theorem inherits the proof-only AG42/Section-171 status of (EW.1).
- The bridge subtraction is independently audited.
- The odd-face lemma is a finite proof-only lemma awaiting independent audit.
- Even-degree exceptional faces are paid entirely by `Q-f`; no parity claim is made
  for them.
- No global two-phase theorem is assumed. Equation (EW.3) holds for every chosen pair
  of projective directions.
- Contact-isolated source points remain in the source.
- No exact unit triangle or same-cardinality strict sub-`D` source is produced.

A useful next theorem would derive two-window concentration from a specified
low-rhombic-slack or low-detour profile. Equation (EW.3) would then force one of the
remaining geometric currencies to be much larger than the current scalar ledgers
record.

C-II and Level I remain open.
