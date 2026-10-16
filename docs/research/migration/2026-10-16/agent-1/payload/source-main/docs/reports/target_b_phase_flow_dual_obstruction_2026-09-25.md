<!-- theorem-state: {"artifact_id":"ART-B1FC2CFA98D4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Erdős Problem #99 — Target B phase-flow obstruction

**Date:** 2026-09-25  
**Repository commit:** `f5f68718da7d742128fb7b297854161550d2cce8`  
**State version:** `2026-09-14.audit.51`  
**Run type:** closing proof / exact geometric regression  
**Target:** B  
**Starting status:** canonical Target B endpoint open  
**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`  
**External literature search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting canonical endpoint

The exact sufficient Target B closure is the joint outer-shell stability inequality

\[
G+E\ge {\sqrt3\over4}B+{\sqrt3\over2}(t+\chi-1).
\]

At the selected local endpoint, Proposition 50.4 of
`docs/targets/target-b/01-jammed-rhombic-branch.md` says that failure of a strict
defect-decreasing, diameter-nonincreasing train-angle velocity forces
\(B_H^{\mathsf T}\alpha+G_D^{\mathsf T}\beta=0\), with \(\alpha\ge0\),
\(\alpha\ne0\), and \(\beta\ge0\). The intended chain was

```text
interpret the positive flow-to-diameter certificate
    -> exact canonical shell-surplus quantity
    -> joint shell-stability closure or a source-preserving strict sub-D competitor
```

The last two arrows were not proved. The work below establishes that the certificate
cannot be excluded from dense low-defect acyclic-core data alone.

## 2. Strongest genuinely new result

**Classification:** proved candidate awaiting promotion (linear-algebra lemma);
regression (geometric obstruction to a core-only strengthening).

### Statement: rank-work and sparse-support lemma

Let \(H=(V,E)\) be a finite directed acyclic graph with incidence matrix \(B\),
whose row for \(u\to v\) is \(e_v-e_u\). Let \(G\) have \(q\) rows in
\(\mathbb R^V\). Suppose

\[
\alpha\ge0,\quad \alpha\ne0,\quad \beta\ge0,\quad
B^{\mathsf T}\alpha+G^{\mathsf T}\beta=0.
\]

Let \(L\) be the maximum directed path length in \(H\). There is a longest-path rank
\(r:V\to\mathbb Z\) with \(1\le r(v)-r(u)\le L\) on every directed edge.
Normalize \(\sum_e\alpha_e=1\). Then

\[
1\le \sum_{h=1}^q\beta_h\,G_h(-r)\le L.
\]

Moreover, the certificate can be chosen with
\[
|\operatorname{supp}\alpha|+|\operatorname{supp}\beta|\le |V|+1.
\]

### Proof

Set \(r(v)\) equal to the length of a longest directed path ending at \(v\).
For an edge \(u\to v\), extending a longest path to \(u\) by this edge shows
\(r(v)-r(u)\ge1\); the difference is at most the longest path length \(L\).
Taking the inner product of the balance equation with \(r\) gives

\[
0=\alpha^{\mathsf T}Br+\beta^{\mathsf T}Gr
 =\sum_{u\to v}\alpha_{uv}(r(v)-r(u))
   -\sum_h\beta_hG_h(-r).
\]

The first sum is a convex combination of numbers in \([1,L]\), proving the
rank-work bound.

For the support bound, impose the normalization as an extra equation and write
\[
\begin{pmatrix}B^{\mathsf T}&G^{\mathsf T}\\ \mathbf1^{\mathsf T}&0\end{pmatrix}
\binom\alpha\beta=\binom0 1,
\qquad (\alpha,\beta)\ge0.
\]
Among feasible vectors choose one with minimal support. Its positive-coordinate
columns are linearly independent: a dependence permits a nonzero kernel
perturbation, in one of its two signs, until a positive coordinate reaches zero,
contradicting minimality. There are at most \(|V|+1\) independent columns. \(\square\)

### Exact geometric regression

For integer \(m\ge6\), set
\[
\theta_m=\pi/3+1/m,\qquad u=(1,0),\qquad
v=(\cos\theta_m,\sin\theta_m),
\]
and
\[
A_m=\{iu+jv:0\le i,j\le m\}.
\]
Then \(|A_m|=(m+1)^2\), its diameter is
\[
D_m=2m\cos(\theta_m/2),
\]
and its unit-contact graph is the bipartite square grid. In particular, it contains
no unit equilateral triangle.

To check all pair distances, any difference is \(au+bv\) with integers
\(|a|,|b|\le m\). If \(ab\ge0\) and both coefficients are nonzero, its squared
length is \(a^2+b^2+2|ab|\cos\theta_m>1\). If \(ab<0\), put
\(p=|a|,q=|b|\); then
\[
|au+bv|^2=(p-q)^2+2pq(1-\cos\theta_m).
\]
For \(p=q=1\) this exceeds one because \(\theta_m>\pi/3\). For \(p\ne q\),
the first term is at least one and the second is positive; for \(p=q\ge2\),
the second is at least \(8(1-\cos\theta_m)>1\). If one coefficient is zero,
the vector has length one exactly when the other coefficient has absolute value one.
Thus the only unit differences are \(\pm u,\pm v\), and their graph is bipartite
by the parity of \(i+j\). Convexity of squared norm on the coefficient square shows
that the longest difference is a same-sign corner, giving the displayed diameter.

View this as an \(m\)-by-\(m\) rhombic tiling. Its train-crossing graph is
\(K_{m,m}\), with one family \(U_1,\ldots,U_m\), the other
\(V_1,\ldots,V_m\), and every crossing oriented \(U_i\to V_j\). All crossing
defects equal \(1/m\). There are \(T=2m\) trains and \(m^2\) crossing edges.
For \(m\ge6\),
\[
m\le D_m\le2m,
\]
so with \(\eta=\lambda=1/2\) every edge survives the defect cutoff
\(\delta\le D_m^{-1/2}\), every vertex survives the degree cutoff
\(\deg\ge D_m/2\), \(\sum_e\delta_e=m\le D_m\), and \(T\le2D_m\).
The component is dense, low-defect, and acyclic in the canonical orientation.

Let \(s=\sin(\theta_m/2)\), and let \(r\) be the opposite-corner diameter
vector. In independent train-angle coordinates, assign velocities \(a_i\) to
the \(U_i\) and \(b_j\) to the \(V_j\). Each crossing defect has derivative
\(b_j-a_i\). If all defects decrease, then summing \(b_j<a_i\) over all pairs
gives \(\sum_j b_j<\sum_i a_i\). The diameter derivative is
\[
G_D(a,b)=s\left(\sum_i a_i-\sum_j b_j\right)>0.
\]
Thus no velocity decreases all core defects while keeping this active diameter
bar nonincreasing.

There is an exact certificate: choose a perfect matching \(M\) of \(K_{m,m}\),
set \(\alpha_e=s\) for \(e\in M\) and zero otherwise, and set the multiplier
of the opposite-corner diameter bar to \(\beta=1\). Then
\(B^{\mathsf T}\alpha\) equals \(-s\) on each \(U_i\) and \(+s\) on each
\(V_j\), while \(G_D\) has the opposite coefficients. Hence
\(B^{\mathsf T}\alpha+G_D^{\mathsf T}\beta=0\), with support sizes \(m\)
and one. After normalizing \(\sum\alpha=1\), the rank-work is exactly one,
so the general lower bound is sharp.

This configuration is not a global minimizer. A triangular-lattice hexagon of
radius \(k\) contains \(1+3k(k+1)\) points and has diameter \(2k\). Choose
\[
k=\left\lceil{\sqrt{12(m+1)^2-3}-3\over6}\right\rceil.
\]
It contains at least \((m+1)^2\) points, so selecting that many gives a
unit-separated competitor with diameter at most
\(2(m+1)/\sqrt3+1\). Also
\(D_m\ge\sqrt3m-1\), since \(\cos(x+y)\ge\cos x-y\). For \(m\ge6\),
\[
\sqrt3m-1>2(m+1)/\sqrt3+1,
\]
so this is a strict same-cardinality smaller-diameter competitor. The parallelogram
also fails the global near-roundness condition: its perimeter is \(4m\), while
\(\pi D_m-4m=\Theta(m)\), not \(O(1)\).

### Scope and dependencies

The rank-work lemma is finite-dimensional linear algebra. The geometric regression is
an explicit family of feasible triangle-free rhombic disks and its certificate for
the local train-angle system. It is not a global-minimizer regression and makes no
claim about the full survivor with non-rhombic boundary points. Its purpose is to
disprove any attempted inference from the density, low-defect, acyclicity, and
first-order train-angle data alone to the absence of a flow-to-diameter certificate.

The notation and meaning of the core are those of Theorem 50.1 and Proposition 50.4
in the active Target B module. No external theorem or computational result is used.

## 3. Exact frontier effect

No canonical branch is eliminated, and the Target B endpoint is unchanged. The
certificate's normalized rank-work and an \(O(|V|)\) support representation are
available for future global charging arguments. The exact regression shows that a
global hull/roundness input is necessary in any route that tries to rule out the
Section 50.4 obstruction.

## 4. Exact remaining lemma

For an actual global minimizer in the pure rhombic-disk branch, prove that every
nonzero certificate
\[
B_H^{\mathsf T}\alpha+G_D^{\mathsf T}\beta=0,\qquad
\alpha,\beta\ge0,
\]
with \(\alpha\ne0\), either forces the joint shell-stability inequality or
integrates to a same-cardinality strict smaller-diameter source configuration,
while retaining every source point and controlling every active diameter bar.
The counterexample proves this needs a hypothesis using the actual near-round global
source or shell ledger.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| DAG certificate rank-work lies in \([1,L]\) after \(\sum\alpha=1\) | proved candidate | incidence-matrix identity | Complete finite-dimensional proof above |
| A certificate exists with total support at most \(|V|+1\) | proved candidate | elementary nonnegative linear feasibility | Minimal-support argument above |
| Dense low-defect acyclic core data force absence of a blocker | regression | exact rhombic patch above | The patch has an explicit blocker |
| The rhombic patch is a Level I counterexample | rejected | triangular-lattice competitor | Strict same-cardinality smaller-diameter competitor exists |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Local/jammed or rhombic structure implies global minimum | fails | The triangular-lattice subset has strictly smaller diameter at the same cardinality |
| Acyclicity alone permits simultaneous defect relaxation with nonincreasing diameter | fails | The matching-flow certificate blocks every strict relaxation direction in the displayed active-bar system |
| Farkas support may be assumed large and diffuse | fails | The explicit certificate has support \(m+1=O(T)\) total |
| Fixed-hull information is enough to transfer the certificate to global optimality | not claimed | The construction's perimeter deficit is linear in \(D_m\), not bounded |

## 7. Literature imports

None.

## 8. Computation

No computation was used. The distance, dual-certificate, and competitor inequalities
are exact symbolic calculations.

## 9. Corrections / supersessions

None. This report narrows the Section 50.4 obstruction; it does not supersede the
active route module.

## 10. Promotion recommendation

**unreviewed** for the rank-work lemma and **regression/rejection only** for the
core-only universal inference. Do not promote the result to the canonical Target B
route: it does not change the shell endpoint and has not been independently audited.

## 11. Handoff

1. Strongest new theorem: a normalized DAG flow-to-diameter certificate performs at
   least one unit of longest-path-rank work and can be represented with at most
   \(|V|+1\) nonzero multipliers.
2. Exact canonical dependency: Target B Theorem 50.1 and Proposition 50.4 are the
   local definitions; neither is extended beyond its existing scope.
3. Exact remaining lemma: use the global near-round source/shell ledger to show that
   every actual-minimizer certificate forces shell closure or a finite strict
   source-preserving diameter decrease.
4. Binding regressions: this does not infer global optimality from a rhombic patch,
   does not integrate a first-order direction, and does not ignore active diameter
   bars.
5. Read next: the Target B module's Sections 25, 36, 40, 50, and the active Section
   51 endpoint before attempting a global charge.
