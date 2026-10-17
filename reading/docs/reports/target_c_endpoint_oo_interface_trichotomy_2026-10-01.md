> Generated reading edition · [exact source](../../../docs/reports/target_c_endpoint_oo_interface_trichotomy_2026-10-01.md) · source SHA-256 `8ebafe1218004c9e131b35dbddae131b40f525cbaa43ca5da7ae6c1ad5737fe6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6077686F2A0E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- endpoint O-O / inactive-interface trichotomy

Date: 2026-10-01
Base main: aa872a0e2aa2b74a011e9a86b8083bc985a0bcb7
Stacked dependencies: 5dc33a249690b2e7cde50c5e88c129a3bfb3fcef and 1558ac6d121a87546a5a7a11c7699d3b534570d6
Status: proof-only; C-II remains open.

## 1. Statement

Work at the exact rooted wrapping endpoint. Current main gives

$$
Q_{\mathrm{loc}}:=\sum_r Q_r=o(D),
$$

where $Q_r$ is the bounded nonquadrilateral face-degree excess of the induced
harmonic graph $H_r$.

Apply canonical Section 90 to the macroscopic locally rhombus-saturated wrapping
carrier. Let

$$
G_*=(A_*,B_*,E_*)
$$

be the robust inverse-phase crossing core. There are fixed constants
$C_T,K,\kappa>0$ such that

$$
|A_*|,|B_*|\le C_TD,\qquad |E_*|\ge\kappa^2D^2,
$$

and all train directions on either fixed phase shore lie in a projective interval
of width $4K/D$.

After deleting $o(D)$ train vertices, every remaining Section-90 train is a
complete global stopped train whose two local physical ends lie on the outer face
of the carrier harmonic graph. Hence the retained crossing graph
$G_\partial$ satisfies

$$
|E_\partial|\ge\kappa^2D^2-o(D^2).
\tag{1}
$$

For any fixed $0<\xi<\kappa^2$, one of the following holds:

1. at least $\xi D^2$ edges of $G_\partial$ join two global outer-to-outer
   stopped trains; or
2. at least
   $$
   \left(\frac{\kappa^2-\xi}{2C_T}-o(1)\right)D
   \tag{2}
   $$
   distinct train-end edge occurrences from one fixed Section-90 phase shore lie
   on actual bounded nonquadrilateral faces of the full positive-contact core.
   All these occurrences have projective directions in one interval of width
   $4K/D$.

Thus failure of the local-to-global outer-to-outer transfer is not diffuse at the
rooted endpoint: it produces a linear phase-coherent inactive-interface population.

Taking $\xi=\kappa^2/2$ and composing with the stacked fixed-star-pair theorem gives
the three-way reduction:

- at least $\kappa^2D/(8C_T)$ split-star global O-O trains on one phase shore; or
- fixed distinct diameter vertices $v\ne w$ brace O-O families $A_v,B_w$ with
  $$
  e(A_v,B_w)\ge\frac{\kappa^2}{4C_K^2}D^2,\qquad
  |A_v|,|B_w|\ge\frac{\kappa^2}{4C_K^2C_T}D,
  $$
  where $C_K=\lfloor4K\rfloor+2$; or
- at least
  $$
  \left(\frac{\kappa^2}{4C_T}-o(1)\right)D
  $$
  distinct global inactive-face boundary occurrences lie in one inverse-diameter
  phase window.

## 2. Local bounded-face ends are sublinear

Let $P_*$ be the Section-90 carrier and $Q_*$ its local bounded-face defect.
Since all $Q_r$ are nonnegative and their sum is $o(D)$,

$$
Q_*=o(D).
$$

Every local train segment has two physical rhombus-boundary ends. Such an end faces
either the outer face of $H_*$ or a bounded nonquadrilateral face of $H_*$.
If $f_*$ is the number of those bounded nonquadrilateral faces, then

$$
f_*\le Q_*,
\qquad
\sum_F\deg F=4f_*+Q_*\le5Q_*=o(D).
\tag{3}
$$

Therefore only $o(D)$ local train segments have an end on a bounded face of
$H_*$.

The audited Section-129 localization gives

$$
N_{\rm miss}=R_4-\sum_rR_r\le3c_I+5=o(D)
\tag{4}
$$

for strict rhombi not realized as local harmonic-cell quadrilaterals. Delete complete
trains meeting those rhombi. A missing rhombus belongs to two train directions, so
only $o(D)$ global trains are contaminated. Along a train, changes of local
harmonic-cell label must occur at a missing rhombus, so the corresponding number of
carrier train segments is also $o(D)$.

After (3)-(4), all but $o(D)$ Section-90 train vertices belong to complete stopped
trains and have both physical ends on the carrier outer face. Since each opposite
shore has at most $C_TD$ vertices, deleting these $o(D)$ vertices removes only
$o(D^2)$ crossing edges. This proves (1).

## 3. The only remaining local/global mismatch is an actual inactive face

Take a physical endpoint edge $e$ of a retained train. It has one carrier strict
rhombus on one side. Suppose its other side is not the unbounded face of the full
positive-contact core.

Then the other full-core face is bounded. It cannot be a bounded four-face:
canonical Section 67 makes every bounded four-face a strict unit rhombus. Such an
opposite rhombus would either have the same harmonic-cell label, contradicting that
$e$ is a physical boundary edge of the full local carrier complex, or be one of
the missing rhombi removed in (4). For a loaded-loaded endpoint edge the audited
Type-II $c_B=0$ localization gives the same conclusion directly: the edge is a
force-hull side and cannot border bounded rhombi on both sides.

Hence the other full-core face is bounded and nonquadrilateral. It is an actual
inactive chamber. A stopped train has at most two ends, and each physical boundary
edge is the end of only the train using that edge direction, so choosing one such
interface end per non-O-O train is injective.

The chosen edge direction equals the train direction. Therefore all chosen ends from
one Section-90 phase shore remain in its projective interval of width $4K/D$.

## 4. Counting

Let $I_D$ be the retained trains that are not global O-O, and let $E_{OO}$ be
crossings whose two train endpoints are global O-O trains.

If $|E_{OO}|<\xi D^2$, then by (1)

$$
|E_\partial|-|E_{OO}|
\ge(\kappa^2-\xi)D^2-o(D^2).
$$

Every edge on the left is incident with $I_D$. Each train has degree at most the
size of the opposite Section-90 shore, at most $C_TD$. Thus

$$
|I_D|
\ge
\left(\frac{\kappa^2-\xi}{C_T}-o(1)\right)D.
$$

One phase shore contains at least half of these trains. The injective endpoint
assignment in Section 3 gives (2).

## 5. Remaining target

Alternative 3 is compatible with a long doubled near-geodesic inactive corridor, so
a generic perimeter count is insufficient. The next target is a phase-capacity
theorem for the Section-84 corridor system: bound how much $O(1/D)$-coherent train
endpoint mass the finite family of inactive corridors can absorb without creating
forbidden diameter/outer-detour cost.

Alternatives 1 and 2 retain the previous split-star multiplicity and fixed-star-pair
crossing-capacity targets.

No computation, verifier, numerical evidence, or CI result is used.
