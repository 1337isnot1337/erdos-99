> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_endpoint_unbalanced_pseudosegment_completion_2026-09-14.md) · source SHA-256 `f75a992756669d6ef46b4539b849c117052ac6b84121a597665c3c1200352502`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 4 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-C1AC7951D8C5","canonical":true,"claim_ids":["C-FULLCORE-FLOOR-ENDPOINT-EXCLUSION"],"claim_statuses":{"C-FULLCORE-FLOOR-ENDPOINT-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — full-core floor endpoint: unbalanced pseudosegment completion

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.50
**Run type:** closing-proof attempt / full-core endpoint audit
**Target:** Target C-II / Level I
**Starting status:** canonical full-core train-coupled surplus floor
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used; Fox–Pach–Suk Theorem 2.10 is imported with its exact hypotheses
**Computation:** none required

## LEVEL I STATUS

STILL OPEN

This report proves a new report-level endpoint exclusion. A canonical full-core
sequence cannot satisfy

```math
\mu_D\longrightarrow \mu_{\rm TC}
 :=\frac{2\pi+2\sqrt{\Delta_2}}5,
\qquad \Delta_2:=\frac{\pi}{2\sqrt3}.
```

The proof closes the apparent gap in the previous Mantel endpoint audit:
near-complete crossing density is converted into an almost-full complete
phase-pure grid even when the two phase classes have unequal sizes. The only
crossings that can have the wrong orientation form a threshold bipartite graph;
the canonical phase cut bounds its edge count by `O(D)`, and a chain-graph
matching estimate removes only `O(sqrt(D))` trains.

This does **not** settle C-II. It excludes only the exact scalar-floor endpoint.
The full-core branch with $`\mu_D`$ bounded above the endpoint, the
macroscopic-container/exterior-cap branch, and the other global branches remain.

The candidate implication chain is

```text
mu_D -> mu_TC in the canonical full-core branch
    -> T_D/D -> 2 sqrt(Delta_2), and the train graph is Mantel-extremal
    -> two unequal phase classes A_D,B_D with
         |A_D|+|B_D| >= 3 T_D/4-o(T_D),
         |A_D||B_D|-cross(A_D,B_D)=o(T_D^2)
    -> Fox--Pach--Suk Theorem 2.10 plus cloning
         gives a complete actual biclique of almost the same two sizes
    -> O(D) wrong-orientation pairs form a chain graph;
         delete O(sqrt(D)) vertices to make every crossing retained and forward
    -> Section 76 gives
         D >= (sqrt(3)/2)(a+b)-O(1)
    -> (sqrt(3)/2)(3/2 sqrt(Delta_2)) > 1,
       contradiction.
```

The contradiction is directly with the source-hull diameter `D`; no source
cloning, source deletion, or unproved global competitor is used.

## 1. Canonical endpoint inputs

Use the canonical full-core endpoint package recorded in the preceding
Mantel-stability report
[`target_c_fullcore_mantel_endpoint_stability_2026-09-14.md`](target_c_fullcore_mantel_endpoint_stability_2026-09-14.md).
Along a hypothetical sequence with $`\mu_D\to\mu_{\rm TC}`$, its promoted
equality analysis gives

```math
\frac{R_D}{D^2}\to\Delta_2,
\qquad
\frac{T_D}{D}\to\tau_{\rm TC}:=2\sqrt{\Delta_2},
\qquad
\frac{R_D}{T_D^2}\to\frac14.
\tag{1.1}
```

Here `R_D` is the number of strict-rhombus faces in the full-core train
complex, and `T_D` is the number of its global train curves. The canonical
phase-circle cut deletes a set `F_D` of crossing pairs with

```math
|F_D|=O(D).
\tag{1.2}
```

The graph `G_D^o` of retained train crossings is simple and triangle-free, and
has

```math
e(G_D^o)=R_D-O(D).
\tag{1.3}
```

Mantel stability therefore supplies a partition

```math
\mathcal T_D=X_D\sqcup Y_D
```

with

```math
|X_D|=\frac{T_D}{2}+o(T_D),
\qquad
|Y_D|=\frac{T_D}{2}+o(T_D),
\tag{1.4}
```

and `o(T_D^2)` missing retained cross edges. The phase-circle cut gives each
train a label in $`\mathbb Z/3\mathbb Z`$. Same-label trains do not cross,
because their projective direction separation is strictly below $`\pi/3`$,
whereas a strict-rhombus crossing has acute separation strictly above
$`\pi/3`$.

All statements in this section are canonical inputs or the report-level Mantel
lemma already proved in the preceding report. Contact-isolated source points
remain in the original source; they are not used as train vertices and are not
silently removed.

## 2. A three-label allocation lemma with the correct shore sum

The earlier endpoint audit retained only the coarse bounds `T_D/6` on the two
largest label classes. The following elementary refinement is the quantitative
point needed here.

### Lemma 2.1 — disjoint-support allocation


**Source formatting excerpt (unbalanced inline math in the original):**

```text

Let (T_j\to\infty), let (X_j,Y_j\) be two sets with
```



```math
|X_j|=\frac{T_j}{2}+o(T_j),
\qquad
|Y_j|=\frac{T_j}{2}+o(T_j),
```

and partition each set into three label classes. Write

```math
x_{j,i}:=|X_j\cap\ell^{-1}(i)|,
\qquad
y_{j,i}:=|Y_j\cap\ell^{-1}(i)|.
```

If

```math
\sum_{i=0}^2 x_{j,i}y_{j,i}=o(T_j^2),
\tag{2.1}
```

then, for the largest class on each side, with

```math
i_j\in\arg\max_i x_{j,i},
\qquad
j_j\in\arg\max_i y_{j,i},
```

one has

```math
i_j\ne j_j,
\qquad
x_{j,i_j}+y_{j,j_j}\ge\frac34T_j-o(T_j),
\tag{2.2}
```

and

```math
x_{j,i_j},y_{j,j_j}\ge\frac14T_j-o(T_j).
\tag{2.3}
```

#### Proof

Pass to any subsequence on which the six normalized quantities

```math
\bar x_i:=\lim_j x_{j,i}/T_j,
\qquad
\bar y_i:=\lim_j y_{j,i}/T_j
```

exist. Then

```math
\sum_i\bar x_i=\sum_i\bar y_i=\frac12,
\qquad
\bar x_i\bar y_i=0\quad(i=0,1,2).
\tag{2.4}
```

Thus the positive supports of ((\bar x_i)) and ((\bar y_i)) are disjoint.
They are both nonempty, so their support sizes are one and two, two and one,
or one and one. The sum of the largest coordinate on each side is therefore
at least

```math
\frac12+\frac14=\frac34.
```

The maximizing labels cannot agree: if (i_j=j_j) along a subsequence, then
both corresponding classes are at least (T_j/6+o(T_j)), contradicting (2.1).
Finally, a positive support on one side forces the corresponding coordinate on
the other side to vanish; with three labels this forces each largest coordinate
to be at least (1/4) in the limiting normalization. Since every convergent
subsequence has the same lower bounds, (2.2)--(2.3) follow. $`\square`$

Apply the lemma to the Mantel partition. Let

```math
\mathcal A_D:=X_D\cap\ell^{-1}(i_D),
\qquad
\mathcal B_D:=Y_D\cap\ell^{-1}(j_D),
```

and set (a_D:=|\mathcal A_D|), (b_D:=|\mathcal B_D|). Then

```math
a_D+b_D\ge\frac34T_D-o(T_D),
\qquad
a_D,b_D\ge\frac14T_D-o(T_D).
\tag{2.5}
```

Since all same-label cross pairs are missing retained edges, the Mantel missing
edge count gives

```math
a_Db_D-e_{G_D^o}(\mathcal A_D,\mathcal B_D)=o(T_D^2).
\tag{2.6}
```

In particular the retained crossing density between these two unequal phase
classes tends to one.

## 3. Unbalanced near-complete pseudosegment extraction

The needed external theorem is the following exact density statement.

### Imported theorem — Fox–Pach–Suk, Theorem 2.10

In *A structure theorem for pseudo-segments and its applications*,
arXiv:2312.01028, Theorem 2.10 states that there is an absolute constant
(c>0) such that, if `R` is a collection of `n` red curves and `B` a
collection of `n` blue curves in the plane, `R union B` is a collection of
pseudosegments, and at least $`\varepsilon n^2`$ red-blue pairs cross, then
there are subcollections `R'` and `B'` with

```math
|R'|,|B'|\ge\varepsilon^c n
```

such that every red curve in `R'` crosses every blue curve in `B'`.

The source explicitly notes that pseudosegment intersection graphs are closed
under cloning by drawing sufficiently close parallel copies. This gives the
following unbalanced consequence, which is proved here rather than quoted as a
black box.

### Lemma 3.1 — unbalanced density consequence

Let `R` and `B` be disjoint finite subcollections of pseudosegments, with

```math
r:=|R|,
\qquad b:=|B|,
```

and suppose at least $`\varepsilon rb`$ pairs in `R times B` cross. Then there
are complete-crossing subcollections `R' subset R`, `B' subset B` with

```math
|R'|\ge\varepsilon^c r,
\qquad
|B'|\ge\varepsilon^c b.
\tag{3.1}
```

#### Proof

Make (b) sufficiently close parallel clones of each red curve and (r)
sufficiently close parallel clones of each blue curve. The two cloned color
classes both have size (rb). The cloning can be performed so that every
clone pair crosses exactly when the corresponding original red-blue pair
crosses, and the full cloned collection remains a pseudosegment collection.
Consequently at least $`\varepsilon (rb)^2`$ cloned red-blue pairs cross.

Apply Fox–Pach–Suk Theorem 2.10 with (n=rb). The resulting complete shores
have at least $`\varepsilon^c rb`$ clones each. After projecting clones back to
their originals, the red shore contains at least

```math
\frac{\varepsilon^c rb}{b}=\varepsilon^c r
```

distinct red curves, and the blue shore contains at least

```math
\frac{\varepsilon^c rb}{r}=\varepsilon^c b
```

distinct blue curves. Completeness survives projection: a selected clone pair
crosses only if its two originals cross. $`\square`$



**Source formatting excerpt (unbalanced inline math in the original):**

```text
Apply Lemma 3.1 to the actual train curves in \(\mathcal A_D,\mathcal B_D).
The train curves are pseudosegments by the canonical train theorem. By (2.6)
and (2.5), their actual crossing density is at least (1-o(1)), because the
retained crossing relation is a subset of the actual crossing relation. Hence
there are complete actual-crossing subfamilies
```



```math
\mathcal A'_D\subseteq\mathcal A_D,
\qquad
\mathcal B'_D\subseteq\mathcal B_D
```

with

```math
|\mathcal A'_D|=(1-o(1))a_D,
\qquad
|\mathcal B'_D|=(1-o(1))b_D.
\tag{3.2}
```

The use of cloning is internal to the external graph theorem. No cloned train
is interpreted as a source point or as a physical packing competitor.

## 4. Wrong-orientation crossings are a chain graph and cost only (o(D)) trains

It remains necessary to make the actual complete crossing rectangle compatible
with the canonical retained phase law. Applying the external theorem to actual
crossings may include a crossing deleted by the phase-circle cut. The following
argument removes this issue without losing a linear shore.

Let (L:=\pi/3). Lift the reduced phase of every train to

```math
x_\tau\in(s,s+L),
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
and retain its label \(\ell(\tau)\in\mathbb Z/3\mathbb Z\). The two selected
label classes have distinct labels. Rename the classes, if necessary, so that
the label difference from `A` to `B` is (+1\) modulo three on their retained
crossings. Equation (2.6) guarantees that retained crossings exist in
quadratic number, so this orientation is well-defined.
```



For an actual crossing (a\in\mathcal A'_D), (b\in\mathcal B'_D), put

```math
d_{ab}:=x_b-x_a.
```

The common lift interval gives (-L<d_{ab}<L). For a strict rhombus crossing,
the acute angle is (L+\delta_{ab}) with (0<\delta_{ab}\le L/2). There are
two possible orientations of the same undirected crossing relative to the two
fixed labels:

* the retained/forward case (d_{ab}=\delta_{ab}\le L/2);
* the cut/wrong-orientation case (d_{ab}=L-\delta_{ab}\ge L/2).

Every strict wrong-orientation pair is one of the deleted phase-cut crossings.
The equality case need not agree with the arbitrary right-angle orientation
chosen by the phase cut, but every equality pair has defect L/2 and therefore
there are only O(D) of them under the global O(D) defect budget. Therefore the set

```math
H_D:=\{(a,b):d_{ab}\ge L/2\}
```

has

```math
|H_D|\le |F_D|+2\Delta_{train}/L=O(D),
\tag{4.1}
```

Viewed as a bipartite graph on $`\mathcal A'_D`$ and $`\mathcal B'_D`$, (H_D)
is a chain graph: after ordering the `A` trains by (x_a), the neighborhoods

```math
N_H(a)=\{b:x_b\ge x_a+L/2\}
```

are nested. This threshold structure is important; an arbitrary graph with
`O(D)` forbidden pairs could have a linear matching.

### Lemma 4.1 — sparse chain graph vertex cover

If a finite chain graph has (m) edges, it has a vertex cover of size at most

```math
\sqrt{2m}.
\tag{4.2}
```

#### Proof


**Source formatting excerpt (unbalanced inline math in the original):**

```text

Let $`\nu`$ be the maximum matching size. By König's theorem, the minimum
vertex-cover size is $`\nu`$. Order the `A` vertices in a matching by nested
neighborhood inclusion. For the first (i) such vertices, their matched blue
vertices are distinct and all lie in the neighborhood of the (i\)-th vertex.
Thus that vertex has degree at least (i). Summing over the $`\nu`$ matched
vertices gives
```



```math
m\ge1+2+\cdots+\nu=\frac{\nu(\nu+1)}2.
```

Hence $`\nu\le\sqrt{2m}`$, and a vertex cover of that size exists. $`\square`$

Use Lemma 4.1 and delete a vertex cover of (H_D). Let the remaining train
families be $`\mathcal A''_D,\mathcal B''_D`$. By (3.2), (4.1), and (4.2),

```math
|\mathcal A''_D|=(1-o(1))a_D,
\qquad
|\mathcal B''_D|=(1-o(1))b_D.
\tag{4.3}
```

Every pair in $`\mathcal A''_D\times\mathcal B''_D`$ is now a retained
forward crossing. Hence, after writing

```math
a_D'':=|\mathcal A''_D|,
\qquad b_D'':=|\mathcal B''_D|,
```

we have

```math
a_D''+b_D''\ge\frac34T_D-o(T_D),
\qquad
\min\{a_D'',b_D''\}\ge\frac14T_D-o(T_D).
\tag{4.4}
```

For every such pair, the canonical phase identity holds in the forward form

```math
\delta_{ab}=x_b-x_a>0.
\tag{4.5}
```

This is exactly the orientation hypothesis needed by the hole-stable complete
grid theorem, apart from its strict common phase-bin-width condition. The global
phase cut gives an interval of width L, not automatically one of width below
L/2, so we now remove that remaining tail explicitly.

For the complete forward grid put

```math
S_D:=\sum_{a\in\mathcal A''_D,\,b\in\mathcal B''_D}(x_b-x_a).
```

This is at most the global angular-defect sum, hence S_D=O(D). Let

```math
x_A^+=\max_a x_a,\quad x_B^-=\min_b x_b,\quad
g=x_B^--x_A^+,\quad r_a=x_A^+-x_a,\quad q_b=x_b-x_B^-.
```

Then g,r_a,q_b are nonnegative and

```math
x_b-x_a=g+r_a+q_b.
```

Since both shores are linear, S_D=O(D) implies g=O(D^{-1}),
sum_a r_a=O(1), and sum_b q_b=O(1). Delete every train with
r_a>D^{-1/4} or q_b>D^{-1/4}. At most O(D^{1/4}) trains are deleted from
each shore. The remaining complete grid has the same normalized shore sizes,
and its reduced phases lie in one interval of width O(D^{-1/4})<L/2. Rechoose
the phase-bin origin at the left endpoint of that interval. Thus the exact
hypotheses of canonical Section 76 hold after an o(T_D) deletion, including
the common-cone and common-order conclusions.

## 5. Diameter contradiction

Apply canonical Section 76 to the trimmed complete phase-pure forward grid
$`\mathcal A''_D\times\mathcal B''_D`$. Its defect sum satisfies

```math
S_D:=\sum_{a\in\mathcal A''_D,\,b\in\mathcal B''_D}\delta_{ab}
\le C_{\rm phase}D,
\tag{5.1}
```

because each grid rhombus is a distinct strict source rhombus and the global
angular-defect sum is `O(D)`. Section 76 gives the finite source-hull inequality

```math
D\ge\frac{\sqrt3}{2}(a_D''+b_D'')
 -\frac{S_D}{\min\{a_D'',b_D''\}}-2.
\tag{5.2}
```

By (1.1) and (4.4), the defect term in (5.2) is (O(1)), while

```math
\frac{a_D''+b_D''}{D}
\ge\frac34\tau_{\rm TC}-o(1)
=\frac32\sqrt{\Delta_2}-o(1).
\tag{5.3}
```

The leading coefficient in (5.2) is strictly larger than one:

```math
\frac{\sqrt3}{2}\cdot\frac32\sqrt{\Delta_2}
>1.
\tag{5.4}
```

Equivalently,

```math
\frac32\sqrt{\Delta_2}>\frac2{\sqrt3},
```

which follows after squaring from

```math
\Delta_2=\frac{\pi}{2\sqrt3}>\frac{16}{27}.
```

For example, the elementary bounds $`\pi>3`$ and $`\sqrt3<2`$ give
$`\Delta_2>3/4>16/27`$. Thus (5.2) becomes, for all sufficiently large
members of the hypothetical sequence,

```math
D\ge(1+\eta)D-O(1)
```

for some fixed $`\eta>0`$, an impossibility.

We have proved:

> **Endpoint exclusion theorem (report-level).** There is no canonical full-core
> Type-II sequence satisfying $`\mu_D\to\mu_{\rm TC}`$.

### Uniform-gap corollary

There exist constants $`\varepsilon_*>0`$ and $`D_*>0`$, depending only on the
canonical theorem stack, such that every canonical full-core Type-II minimizer
with $`D\ge D_*`$ satisfies

```math
\mu_D\ge\mu_{\rm TC}+\varepsilon_*.
\tag{5.5}
```

This gap is qualitative and not numerically evaluated.

#### Proof

Suppose no such pair $`(\varepsilon_*,D_*)`$ exists. Then for each integer
$`j\ge1`$ there is a canonical full-core minimizer with $`D_j\ge j`$ and

```math
\mu_{D_j}<\mu_{\rm TC}+1/j.
```

Apply the canonical train-coupled floor theorem to this selected sequence. It
gives $`\liminf_j\mu_{D_j}\ge\mu_{\rm TC}`$. The displayed upper bounds give
$`\limsup_j\mu_{D_j}\le\mu_{\rm TC}`$. Hence $`\mu_{D_j}\to\mu_{\rm TC}`$, contradicting
the endpoint-exclusion theorem. Therefore (5.5) holds. $`\square`$

The source-hull diameter in (5.2) is the diameter of the full original source.
The proof does not replace the source by a scaffold and does not discard
contact-isolated source points. Global minimum-diameter optimality enters through
the canonical full-core endpoint package (1.1)--(1.3), not through an unproved
local-stress-to-finite-motion implication.

## 6. Adversarial audit

| Potential failure | Audit result |
| --- | --- |
| Unequal phase shores | Lemma 3.1 uses the exact cloning argument, giving separate lower bounds proportional to both original shore sizes. |
| The old `T/6` loss | Lemma 2.1 uses the three-label disjoint-support limit and obtains shore sum `3T/4-o(T)`, not merely `T/3`. |
| Actual versus retained crossings | Retained crossings are a subset of actual crossings, so actual density is at least `1-o(1)`. The chain-graph step then removes all wrong-orientation actual crossings. |
| `O(D)` forbidden pairs | They are not removed by an arbitrary vertex bound. Their threshold/chain structure gives a vertex cover of only `O(sqrt(D))`. |
| Right-angle equality | Equality `d=L/2` is charged directly to the global defect budget; all wrong-orientation pairs therefore still number `O(D)`. |
| Section-76 phase-bin width | The global width-`L` cut is not used directly; an additional `O(D^(1/4))`-tail deletion produces a width-`o(1)` complete grid. |
| Holes, interfaces, repeated boundary occurrences | Section 76's source-hull path argument is the invoked canonical theorem and does not require a disk or a single outer boundary. |
| Contact-isolated points | They remain in the full source and its hull; no affine-kernel statement is extended to them. |
| Source/scaffold confusion | The train curves are only an auxiliary representation. Section 76 endpoints are centers of actual source rhombi, so their distance is at most the full source diameter. |
| Cloned curves as a competitor | Cloning occurs only inside the proof of the external graph-extraction lemma and is never interpreted as a packing configuration. |
| Global optimality | It is used only through the canonical endpoint hypotheses. The report does not claim the theorem for arbitrary dense unit-rhombus complexes. |
| Asymptotic-to-finite step | Assuming a sequence converging to the endpoint gives the fixed positive margin in (5.4); after increasing the sequence threshold, the `O(1)` defect error cannot absorb it. |
| Level-I quantifiers | This excludes one full-core scalar endpoint only. It does not quantify over all triangle-free global minimizers or all sufficiently large cardinalities. |

## 7. Exact remaining obstruction

The theorem removes the exact equality endpoint of the promoted full-core scalar
floor and, by the corollary, gives a non-explicit uniform positive gap above it.
It does not provide an upper bound on $`\mu_D`$, so the remaining full-core
branch may still have a limit at or strictly above $`\mu_{\rm TC}+\varepsilon_*`$. The current
source-level obstruction remains the aggregate outer-walk detour

```math
\sum_r(L_r-2d_r)
```

coupled to (e_{BB}-k), as recorded by canonical Sections 122--123. The
macroscopic inactive-chamber/exterior-cap branch also remains uncovered. No
strict source-preserving diameter decrease or exact unit equilateral triangle has
been obtained.

The endpoint theorem therefore advances the route as follows:

```text
canonical mu >= mu_TC floor
    + no sequence can converge to mu_TC
    -> still missing: eliminate every higher-surplus full-core sequence,
       or close the macroscopic-container branch.
```

This is a sequence-level endpoint exclusion. Together with the canonical floor it
also gives a qualitative, non-explicit uniform gap above the floor: there are
some ε_*>0 and D_*>0 such that every canonical full-core minimizer with
D≥D_* has μ_D≥μ_TC+ε_*. No numerical value or effective threshold is claimed.
It is not a Level-I conclusion.

## 8. Literature and applicability record

The imported source is Fox, Pach, and Suk, *A structure theorem for pseudo-segments
and its applications*, arXiv:2312.01028:
[`arXiv abstract and paper`](https://arxiv.org/abs/2312.01028).

The used result is Theorem 2.10, not the weaker Theorem 2.12:

* **Hypotheses:** two red/blue families of equal size `n`; their union is a
  collection of pseudosegments; at least $`\varepsilon n^2`$ red-blue pairs
  cross.
* **Conclusion:** complete-crossing subfamilies of both size at least
  $`\varepsilon^c n`$, for one absolute (c>0).
* **Normalization:** crossing-pair density is measured against the full
  red-blue product `n^2`; no unit-distance, diameter, or packing hypothesis is
  part of the theorem.
* **Use here:** Lemma 3.1 derives the unequal-size version by cloning. The
  actual train curves satisfy the pseudosegment hypothesis by the canonical
  train theorem, while the source-level diameter conclusion comes separately
  from canonical Section 76.
* **Non-applicability by itself:** the external theorem alone would not give a
  source-preserving competitor or a Level-I conclusion. The chain-graph
  orientation repair and Section 76 are essential.

No other external theorem is imported. The elementary Mantel endpoint stability,
the label allocation lemma, and the sparse-chain vertex-cover lemma are proved
in this report.

## 9. Computation

No computation is needed for the endpoint proof. The only numerical comparison is
the exact inequality $`\Delta_2>16/27`$, certified in Section 5 by elementary
bounds for $`\pi`$ and $`\sqrt3`$. No floating-point margin is used.

## 10. Claim classification and promotion status

* **Canonical trusted inputs:** the current Target C full-core floor, loaded-chord
  and train-count squeeze, phase-cut `O(D)` bound, train pseudosegment theorem,
  and Section 76 source-hull complete-grid inequality.
* **Proved in this report:** Lemma 2.1; the unbalanced extraction Lemma 3.1 from
  the imported Theorem 2.10; Lemma 4.1; the endpoint exclusion conditional only
  on the canonical endpoint package; and the qualitative uniform-gap corollary.
* **Status:** canonical after the independent audit
  `target_c_fullcore_endpoint_unbalanced_pseudosegment_completion_independent_audit_2026-09-14.md`.
* **Not proved:** an explicit value of the uniform gap, elimination of the whole
  full-core branch, closure of the macroscopic-container branch, or Level I.

The theorem-state transaction for canonical ID
`C-FULLCORE-FLOOR-ENDPOINT-EXCLUSION` records the exact sequence-level scope.

## 11. Reproducibility and handoff

The complete proof is contained in this report and depends only on the cited
canonical modules and the primary paper linked in Section 8. The preceding Mantel
endpoint report supplies the explicit endpoint squeeze used in Section 1.

The phase-cut check has been repaired to include the arbitrary right-angle choice:
strict wrong orientations are deleted pairs, while right-angle pairs are charged
separately to the O(D) defect budget. The added phase-tail deletion discharges the
width-below-L/2 hypothesis of Section 76. The independent audit verified the
cloning extraction and phase-lift case split. The live task therefore returns to
the higher-surplus detour payment and the macroscopic-container branch.
