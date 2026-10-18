> Generated reading edition · [exact source](../../../docs/audits/target_a_zero_slack_matching_image_overlap_regression_2026-10-17.md) · source SHA-256 `585d984a913b92dbe9d7d6dd63d02ad1c77a20f0caa35ff3fa0ffb35274c3502`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-D6EEF46F9598","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Exact incidence regression: two source matchings can reuse their images

Date: 2026-10-17  
Source base: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`  
State: `2026-10-15.publication.2`; priority `public-frontier.3`; catalogue `public-frontier.7`  
Classification: finite rational incidence-geometry regression; no theorem-state promotion.

## Result and scope

The separate matching facts used on the zero-slack source side do not, by
themselves, produce a joint matching with distinct source labels. This fixture
has a full-dimensional response hull, a unit-separated source, a triangular
lattice set strictly inside the response hull, and two individually unique
source matchings. Their source images overlap in two labels. The combined
conflict graph has five target vertices but only three source neighbors, so its
Hall deficiency is exactly two even though the source has five labels.

This is a regression only to the additive inference “two separate source
matchings give disjoint source images.” It realizes the local matching and
source-gate geometry with rational coordinates, but it does not satisfy or
claim the global-optimality and zero-slack capacity hypotheses of Section 168.
It has no Schur matrix and proves no Schur-rank inequality or source-cardinality
competitor.

## Exact fixture

Let the three response points be

```math
x_1=(-1/5,-1/5),\qquad x_2=(16/5,-1/5),\qquad x_3=(3/2,2),
```

and put $`K=\operatorname{conv}\{x_1,x_2,x_3\}`$. Its squared diameter is
$`289/25`$, attained by $`x_1x_2`$; the other two squared distances are
$`773/100`$. Thus $`K`$ is a nondegenerate triangle with $`d=17/5`$.
The two triangular-lattice points

```math
y_1=(0,0),\qquad y_2=(3,0)
```

lie strictly inside $`K`$, as the exact oriented-area checks in the verifier
show. They are unit-separated.

Take the five source labels

```math
a_1=(-1/2,-1/5),\quad a_2=(7/2,-1/5),\quad
a_3=(3/2,29/10),\quad a_4=(6,0),\quad a_5=(9,-1/5).
```

They are pairwise more than one unit apart, so the source set is
unit-separated and triangle-free; its actual diameter is $`19/2`$, attained
by $`a_1a_5`$. All five labels lie outside $`K`$. Every coordinate is
rational, and all pair tests below use exact squared distances.

## Separate matchings and the Hall obstruction

Use strict conflict as the bipartite adjacency relation: two labels are
adjacent exactly when their distance is less than one. Direct exact distance
enumeration gives

```math
N_A(x_1)=\{a_1\},\qquad N_A(x_2)=\{a_2\},\qquad
N_A(x_3)=\{a_3\},
```

and

```math
N_A(y_1)=\{a_1\},\qquad N_A(y_2)=\{a_2\}.
```

The unique saturating matchings are therefore

```math
M_X=\{x_1a_1,x_2a_2,x_3a_3\},\qquad
M_Y=\{y_1a_1,y_2a_2\}.
```

The source images satisfy

```math
\operatorname{im}(M_X)=\{a_1,a_2,a_3\},\quad
\operatorname{im}(M_Y)=\{a_1,a_2\},\quad
|\operatorname{im}(M_X)\cap\operatorname{im}(M_Y)|=2.
```

Moreover, the two pairs $`(x_1,y_1)`$ and $`(x_2,y_2)`$ are themselves
strict conflicts, and each corresponding source point is within one unit of
both endpoints:

```math
|x_1-y_1|^2=|x_2-y_2|^2=2/25<1,
\qquad
|a_1-y_1|^2=|a_2-y_2|^2=29/100<1.
```

Thus the shared source images occur even in two disjoint geometric source
gates through distinct interior lattice vertices. The combined left shore
$`X\sqcup Y`$ has five vertices, while its exact source neighborhood is
$`\{a_1,a_2,a_3\}`$, of size three. Hall's condition fails by two. The
unused labels $`a_4,a_5`$ cannot help because neither has a strict conflict
with any vertex of $`X\sqcup Y`$. The largest simultaneous matching has size
three, although each individual shore is saturated by its own matching.

The response/source pairs $`x_1a_1,x_2a_2,x_3a_3`$ are disjoint segments
crossing the boundary of $`K`$; the selected lattice gates $`y_1,y_2`$ are
inside $`K`$. In the notation of the zero-slack capacity defect, this fixture
has $`|X|=3`$ and $`|A\cap K|=0`$, so its exterior count is $`r=3`$. It is
consistent with the boundary-order estimate $`r\le12d+9`$, but that estimate
does not separate the two matching images.

## Reproduction

From the repository root, run:

```sh
python research/verify_target_a_zero_slack_matching_overlap_2026_10_17.py
python tools/check_public.py
git diff --check
```

The standalone verifier uses only rational arithmetic and the standard
library. It checks all source, response, lattice, and cross-set squared
distances; the hull containments; the two unique matchings; the common-source
image count; and the exact Hall deficiency. Its scope is this finite fixture.

## Exact remaining gap

Closing the canonical zero-slack branch still requires a source-specific
coupling theorem that converts the boundary-order defect, genuine-source gates,
and their actual overlap into the required Schur deficiency or a strict
source-cardinality competitor. The fixture shows why matching counts cannot be
added by treating the independently chosen images as disjoint. It does not
show that the overlap has the displayed size in a canonical global optimum,
bound that overlap in the canonical branch, or establish any Schur rank loss.
Target A and Level I remain open.

**Predecessor credit:** Sections 168 and 176 provide separate source matchings,
boundary-order localization, and genuine-source gates. This artifact audits
only the compatibility step between separate matching images.

**AI role:** OpenAI Codex (GPT-6) selected the task, constructed the rational
fixture and exact checker, and wrote this scoped report. **Independent review:**
none; status remains unreviewed.
