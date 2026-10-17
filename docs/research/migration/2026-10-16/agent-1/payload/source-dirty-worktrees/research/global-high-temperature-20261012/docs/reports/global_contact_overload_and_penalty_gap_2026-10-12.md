# Global contact overload and the failure of a fixed overlap penalty

**Date:** 2026-10-12  
**Repository checkpoint:** `200a64287158938d9e8c8f3f3e2fd627350c2f95`  
**Canonical base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`  
**State version:** `2026-10-10.audit.234`  
**Target:** independent whole-problem / Level I  
**Run type:** global variational exploration, duality, and regression  
**Classification:** unreviewed proof candidates; conditional closure; rejected penalty bridge  
**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`

**LEVEL I STATUS: STILL OPEN.** No result here is promoted.

## 1. Global closure chain being tested

The selected quantity concerns every source point and all actual contacts and
diameter pairs. It does not assume a chart, a particular contact component, a
grain, a boundary shell, or deletion of contact-isolated labels.

For a unit-separated source of diameter \(D\), let \(\mathcal S(A)\) be the
normalized nonnegative equilibrium stresses from shared-theory Theorem 4.1:
\[
B_C\alpha=B_H\beta,\qquad \sum_H\beta=1,\qquad \alpha,\beta\ge0.
\]
Here each edge column of \(B\) has \(p_i-p_j\) at endpoint \(i\), its
negative at \(j\), and zero at every other label. Define
\[
E_c(A)=\min_{(\alpha,\beta)\in\mathcal S(A)}
             \sum_{e\in C}(\alpha_e-c)_+ . \tag{1}
\]
The minimum is over all available normalized stresses, not one selected stress.

The proposed implication chain is
\[
\boxed{\text{a global-optimality theorem giving }E_{1/2}(A)<D^2/16}
\ \Longrightarrow\ \text{an exact triangle when }D\ge64.
\]

The inequality inside the box is **unproved**. The report proves the implication,
an exact dual formula for its quantity, and a global obstruction to one attempted
derivation. A reduction to this inequality does not settle Level I.

## 2. Macroscopic overload in every large triangle-free stressed source

**Claim status: proved candidate awaiting promotion; no independent audit yet.**

Suppose \(A\) is unit-separated, its actual contact graph is triangle-free,
and \(\mathcal S(A)\ne\varnothing\). If \(D\ge64\), then
\[
\boxed{E_{1/2}(A)\ge D^2/16.} \tag{2}
\]
This applies in particular to every hypothetical triangle-free global minimizer,
but is not confined to global minimizers.

**Proof.** Virial equilibrium gives \(\sum_C\alpha=D^2\) for every stress.
Consequently, with \(e=|C|\),
\[
\sum_C(\alpha_e-1/2)_+\ge D^2-e/2.
\]
The unit-contact graph has a crossing-free straight-line embedding. Indeed, two
crossing unit segments each have an endpoint within \(1/2\) of their crossing;
the two selected endpoints would then have distance strictly below one. A segment
also cannot pass through another source label. The triangle-free planar edge bound
is \(e\le2n-4\) for \(n\ge3\), including disconnected graphs and isolates.
Thus every stress has overload at least \(D^2-n+2\).

Oler's finite inequality applied to the full hull, followed by the isodiametric
and perimeter bounds, gives
\[
n\le aD^2+\frac\pi2D+1,\qquad a=\frac\pi{2\sqrt3}.
\]
Hence
\[
E_{1/2}(A)\ge(1-a)D^2-\frac\pi2D+1.
\]
Using \(\sqrt3>173/100\) and \(\pi<22/7\) gives
\(1-a>111/1211\). For \(D\ge64\),
\[
\frac{111}{1211}-\frac{11}{7D}
\ge\frac{111}{1211}-\frac{11}{448}>\frac1{16}.
\]
This proves (2). All source labels enter \(n\), including labels carrying zero
stress. No full-source affine-kernel or rigidity theorem is used. \(\square\)

More generally,
\(E_c(A)\ge D^2-c(2n-4)\). Any uniform cap \(\alpha_e\le c\) with
\(c<\sqrt3/\pi\), if supplied by genuine global optimality for large sources,
would contradict triangle-freeness. The half-threshold allows a total excess
below \(D^2/16\), so it does not require every individual contact weight to be small.

## 3. Exact full-source work dual

For a velocity assignment \(v=(v_i)_{i=1}^n\), put
\[
w_{ij}(v)=(p_i-p_j)\cdot(v_i-v_j).
\]
Whenever the normalized stress set is nonempty, (1) has the exact dual
\[
\boxed{
E_c(A)=\max_{v:\ w_e(v)\le1\ (e\in C)}
\left\{\min_{h\in H}w_h(v)
       -c\sum_{e\in C}(w_e(v))_+\right\}.} \tag{3}
\]
The velocities are arbitrary full-source velocities. They are not asserted to be
feasible motions of the original packing. Negative contact work is permitted.

**Proof.** Write (1) as the finite linear program
\[
\min\sum_C t_e:\quad
B_C\alpha-B_H\beta=0,\quad\sum_H\beta=1,
\quad\alpha_e-t_e\le c,\quad\alpha,\beta,t\ge0.
\]
Use a vector multiplier \(-v\) for equilibrium, a scalar \(-\tau\) for
\(\sum\beta-1=0\), and \(\gamma_e\ge0\) for the cap inequalities.
Minimizing the Lagrangian over the nonnegative variables requires
\[
0\le\gamma_e\le1,\qquad\gamma_e\ge w_e(v),
\qquad\tau\le w_h(v)\quad(h\in H).
\]
The dual objective is \(\tau-c\sum\gamma_e\). Since \(c>0\), optimize
\(\tau=\min_Hw_h\) and \(\gamma_e=(w_e)_+\). This gives (3).
The primal is feasible by assumption and bounded below by zero. Its stress
variables are bounded, since \(\sum\alpha=D^2\) and \(\sum\beta=1\),
and the minimizing \(t\)'s can be restricted to a bounded set. Finite linear
programming duality therefore supplies equality and attainment.

The standard finite LP duality theorem was checked in Boyd and Vandenberghe,
[*Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
Section 5.2.3. No constraint qualification for a nonlinear motion is imported.

The dilation velocity \(v_i=p_i\) gives \(w_e=1\) on contacts and
\(w_h=D^2\) on diameter pairs, recovering the lower bound \(D^2-ce\).
This also checks the signs and the absence of an extra factor of two in (3).

## 4. Why a global fixed-penalty proof cannot supply the cap

Consider the all-pair energy on arbitrary distinct planar clouds,
\[
F_\gamma(P)=\operatorname{diam}(P)^2
       +\gamma\sum_{i<j}(1-|p_i-p_j|^2)_+ . \tag{4}
\]
At a unit-separated source, its first-order stationarity is equivalent to
existence of a normalized equilibrium stress with \(0\le\alpha_e\le\gamma\).
Indeed the directional derivative is
\[
F_\gamma'(A;v)=2\max_Hw_h(v)
                    +2\gamma\sum_C(-w_e(v))_+;
\]
this is the support function of the compact convex set of vectors
\(2(B_H\beta-B_C\alpha)\), with \(\beta\) a probability vector and
\(\alpha\in[0,\gamma]^C\). It is nonnegative in every direction exactly
when that set contains zero, by finite-dimensional separation.

But global minimization of (4) is **not** equivalent to the hard unit-separation
problem at any fixed \(\gamma< b:=2\sqrt3/\pi\), even for large populations.
In fact, for every sufficiently large \(n\), a distinct \(n\)-point cloud has
energy strictly below \(D(n)^2\). Its graph of pairs at distance at most one can
be just a matching.

**Proof.** Let \(m=\lceil n/2\rceil\). Triangular-lattice translation averaging
in the open radius-\(\sqrt{a_0m/\pi}\) disk gives an \(m\)-point
unit-separated cloud of diameter below \(\sqrt{bm}\), where
\(a_0=\sqrt3/2\). Scale it by \(1+2\varepsilon\) and replace
\(\lfloor n/2\rfloor\) of its points by pairs displaced horizontally by
\(\pm\varepsilon/2\). If \(n\) is odd, keep one undisplaced singleton.
Different clusters have pair distances at least \(1+\varepsilon\); each twin
pair has distance \(\varepsilon\). The points are distinct. Their energy is
at most
\[
((1+2\varepsilon)\sqrt{bm}+\varepsilon)^2
 +\gamma\lfloor n/2\rfloor(1-\varepsilon^2).
\]
Choose \(\varepsilon=n^{-2}\). This upper bound is
\(\tfrac12(b+\gamma)n+O(1)\). The full-source Oler diameter lower bound
gives \(D(n)^2\ge bn-O(\sqrt n)\). The strict energy comparison follows
whenever \(\gamma<b\). \(\square\)

Thus any eventual globally exact coefficient for this particular penalty would
have to be at least \(b\), while a uniform stress cap sufficient for the
triangle-free edge-count contradiction would need coefficient below \(b/2\).
This factor-two separation rejects the proposed **global exact-penalty** bridge.
It does not reject a separate theorem about local stability or sufficiently small
overlaps. The clouds in this proof have very short twin distances and are not
unit-separated competitors for Erdős #99.

For a triangle-free stressed source, uniform contraction itself lowers
\(F_{1/2}\). Before any old noncontact becomes short, the exact energy is
\[
F_{1/2}((1-t)A)
=D^2-(2t-t^2)(D^2-e/2).
\]
The contraction violates hard separation, so this is not a diameter improvement
for a valid source. Repairing those violations without losing cardinality or the
strict diameter gain is an additional global theorem, not supplied by stress duality.

## 5. Exact finite countercheck

An explicit relaxed cloud uses a unit triangular-lattice hexagon of radius \(k\),
with \(m=3k(k+1)+1\) sites. Put \(\varepsilon=k^{-3}\),
\(\lambda=1+2\varepsilon\), and replace every site by its two horizontal
\(\pm\varepsilon/2\) copies after scaling by \(\lambda\).
It has \(2m\) labels, exactly \(m\) short pairs, and
\[
\operatorname{diam}(P)=2k\lambda+\varepsilon,
\qquad F_{1/2}(P)=(2k\lambda+\varepsilon)^2
                   +\tfrac m2(1-\varepsilon^2).
\]
All other distances exceed one. As \(k\to\infty\), its energy per label tends
to \(11/12<b\), so this is also an explicit unbounded counterfamily.
A finite certificate checks the entire k=10 cloud against the universal Oler lower
bound for every 662-point unit-separated source. It is not an example of a
triangle-free global hard-packing minimizer.

## 6. Dependencies, claim classification, and remaining work

Canonical inputs are shared-theory Theorem 4.1 in
`docs/theory/01-local-structure.md` and Lemma 21.1 / Equation (21.3) in
`docs/theory/03-oler-shell.md`. Planarity, the full-source edge bound, lattice
averaging, stress duality, and the relaxed comparison are justified above.
The preceding odd-rim report is a regression lead rather than a canonical premise.

| Claim | Classification | Scope |
| --- | --- | --- |
| Macroscopic overload (2) | Proved candidate awaiting promotion | Every triangle-free unit-separated stressed source with D>=64 |
| Work dual (3) | Proved candidate awaiting promotion | Every full source with a nonempty normalized stress set |
| Global overload cap implies Level I | Conditional | The cap is unproved |
| Eventual globally exact penalty below b | Rejected | Distinct twin clouds defeat it for all sufficiently large populations |
| Half-penalty contraction is a valid hard competitor | Rejected inference | It shortens unit pairs below one |
| Global diameter / exact triangle conclusion | Open | No general hard-separation repair or independent replacement follows |

The exact next obligation is to obtain a genuinely global source-replacement or
near-overlap repair theorem that yields the bound in Section 1, or to reject the
overload route with an actual global-minimizer regression. A proof based only on
normalized stress, sparse contacts, or a global exact penalty has not supplied it.
No canonical state, route, or prompt is changed. Promotion is not requested.
