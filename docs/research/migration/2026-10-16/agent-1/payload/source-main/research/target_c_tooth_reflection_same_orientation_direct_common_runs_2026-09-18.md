# Target C-II — heavy FREE reuse forces same-orientation far-pair common runs without the order-extraction loss

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion; proof-only refinement of the small-external heavy-reuse branch  
**Scope:** ordered slow-scale all-inactive FREE family, especially `Z_D=|A\setminus F|=o(sqrt(D))`  
**Dependencies:** multi-module FREE corridor reuse; inverse-`D` degree-six matching bound; upper-gate injection into `A\setminus F`; common-run Euler-characteristic fork; two-normal SAME/SAME cone theorem  
**Certificate:** `research/verify_target_c_tooth_reflection_same_orientation_direct_common_runs_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous two-normal common-run route first thinned a shared matching to one relative edge orientation and then used Erdos-Szekeres to recover a coherent ancestry order. That square-root loss is unnecessary if the target is a same-direction common trunk. A heavily reused original edge already occurs in many module ancestries. A majority of those occurrences traverse the edge in one absolute direction, and the first and last modules in that majority class are still far apart in the ordered normal family.

This gives, from the same heavy-edge population, a fixed separated module pair sharing `Omega(D/m^2)` edges with **SAME relative traversal orientation from the start**. One may then pigeonhole directly into a pair of maximal all-lower runs. No order-subsequence theorem is needed.

Fix

\[
h_*={\sqrt{303}\over52},\qquad K>h_*,\qquad
\alpha_K:=1-{h_*\over K}>0.
\]

Let `m=m_D` selected all-inactive FREE modules occur in their ordered normal family, with consecutive normal gap at least `gamma_D`. Apply the existing multi-module theorem with an integer threshold

\[
1\le H<m.
\]

As before, either `MULTI-MATCHING` holds, giving

\[
\boxed{
\left({\alpha_K\over22}-o(1)\right){mD\over H}
}
\tag{SO.1}

vertex-disjoint old fully inactive source pairs satisfying

\[
1<|x-y|\le1+{K\over D},
\tag{SO.2}

or `HEAVY-REUSE` holds, with at least

\[
\left({\alpha_K\over2}-o(1)\right)D
\tag{SO.3}

distinct original edges appearing as lower gates in at least `H+1` module ancestries.

The new conclusion concerns the second branch.

## 1. Same-orientation far-pair extraction

Fix an arbitrary orientation on one heavy unordered source edge `e={x,y}`. Every participating module ancestry traverses `e` either as `x->y` or as `y->x`. One orientation class contains at least

\[
\left\lceil{H+1\over2}\right\rceil
\]

participating modules.

Take the first and last participating module in that majority orientation class. Their indices differ by at least

\[
\left\lceil{H+1\over2}\right\rceil-1
\ge {H-1\over2}.
\]

Thus their normals differ by at least

\[
\boxed{
{H-1\over2}\,\gamma_D.
}
\tag{SO.4}

Assign `e` to that ordered module pair. There are at most `binom(m,2)` possible pairs. Pigeonholing (SO.3) gives one fixed pair `i,j` with normal separation

\[
\boxed{
\theta_{ij}:=\angle(N_i,N_j)
\ge {H-1\over2}\gamma_D
}
\tag{SO.5}

that shares at least

\[
\boxed{
(\alpha_K-o(1)){D\over m^2}
}
\tag{SO.6}

distinct original inverse-`D` lower-gate edges, every one traversed in the SAME relative endpoint direction by the two ancestries.

The inverse-`D` source-pair graph has maximum degree at most six. Greedy matching therefore leaves a vertex-disjoint common matching `M_ij` with

\[
\boxed{
|M_{ij}|
\ge
\left({\alpha_K\over11}-o(1)\right){D\over m^2}.
}
\tag{SO.7}

No orientation thinning is required: SAME traversal was built into the pair assignment.

## 2. Direct lower-run-pair pigeonhole

Put

\[
Z_D:=|A\setminus F|.
\]

Every upper gate in either all-inactive ancestry activates a distinct source vertex outside the force hull. Hence each ancestry has at most

\[
Z_D+1
\]

maximal all-lower runs.

Every edge of `M_ij` belongs to exactly one maximal lower run in ancestry `i` and exactly one in ancestry `j`. There are at most `(Z_D+1)^2` lower-run pairs. Therefore one fixed run pair

\[
P\subseteq\mathcal A_i,\qquad Q\subseteq\mathcal A_j
\]

contains the same vertex-disjoint matching `M^*_{ij}` of size

\[
\boxed{
q:=|M^*_{ij}|
\ge
\left({\alpha_K\over11}-o(1)\right)
{D\over m^2(Z_D+1)^2}.
}
\tag{SO.8}

Every selected edge still satisfies (SO.2), is a lower gate in both repairs, and is traversed in the SAME endpoint direction in `P` and `Q`.

This direct run-pair pigeonhole replaces the earlier order-coherent route for this branch. It does not require an Erdos-Szekeres square-root extraction, and it does not require monotonicity of the run-pair sequence.

## 3. Same orientation turns every selected common component into a SAME/SAME trunk

Let

\[
I:=P\cap Q.
\]

Every edge-containing component of `I` is a path. If such a component contains one selected edge, then the restrictions of `P` and `Q` traverse that component in the same direction, because the selected edge itself has SAME relative traversal orientation. Therefore every selected edge in that component lies on a genuine `SAME + SAME-ORDER` common trunk.

For every real threshold `s>=1`, either one component of `I` contains at least `s` selected edges, or the exact two-path identity gives

\[
\boxed{
\beta(P\cup Q)\ge {q\over s}-1.
}
\tag{SO.9}

In the first case, because the selected matching is vertex-disjoint, that common component contains at least `2s-1` path edges. The SAME/SAME cone theorem then gives, with

\[
B={N_i+N_j\over|N_i+N_j|},
\]

endpoint displacement `X` satisfying

\[
\boxed{
X\cdot B>(2s-1)\sin(\theta_{ij}/2).
}
\tag{SO.10}

Thus the branch is now a direct topological-or-geometric minimax.

Put

\[
a:=2\sin(\theta_{ij}/2).
\]

Choosing

\[
s=\sqrt{q/a}
\]

up to integer rounding yields

\[
\boxed{
\text{either }\beta(P\cup Q)\ge\sqrt{aq}-O(1)
\quad\text{or}\quad
X\cdot B\ge\sqrt{aq}-O(1+a).
}
\tag{SO.11}

The plane short-edge embedding converts the cycle rank in (SO.11) into the same number of bounded faces.

---

## 4. Small-external tuning gives an almost-`sqrt(D)/(Z_D+1)` obstruction scale

Assume now

\[
\boxed{Z_D=o(\sqrt D).}
\tag{SO.12}

Define

\[
S_D:={\sqrt D\over Z_D+1}\longrightarrow\infty.
\tag{SO.13}

Choose any scale `omega_D` satisfying

\[
\omega_D\to\infty,
\qquad
\omega_D=o(D^{1/8}),
\qquad
\omega_D^{5/2}=o(S_D).
\tag{SO.14}

For example,

\[
\omega_D=\log\log(S_D+e^e)
\]

is admissible for all sufficiently large `D`.

Choose the slow reflection scale so that

\[
\kappa_D=\Theta(D^{1/4}/\omega_D^2).
\tag{SO.15}

Then

\[
\kappa_D\to\infty,
\qquad
\kappa_D=o(D^{1/4}),
\]

and a full-order retained module family has

\[
\boxed{m=\Theta(\omega_D^2)}
\tag{SO.16}

with consecutive normal gap

\[
\boxed{\gamma_D=\Theta(\omega_D^{-2}).}
\tag{SO.17}

Take

\[
H=\left\lfloor{m\over\omega_D}\right\rfloor
=\Theta(\omega_D).
\tag{SO.18}

Then the old `MULTI-MATCHING` branch (SO.1) already gives

\[
\boxed{\Omega(D\omega_D)}
\tag{SO.19}

vertex-disjoint original inverse-`D` pairs.

Otherwise, in `HEAVY-REUSE`, (SO.5) gives

\[
\boxed{\theta_{ij}=\Omega(\omega_D^{-1}),}
\tag{SO.20}

so

\[
a=2\sin(\theta_{ij}/2)=\Omega(\omega_D^{-1}).
\tag{SO.21}

The direct run-pair estimate (SO.8) becomes

\[
\boxed{
q=\Omega\left({S_D^2\over\omega_D^4}\right).
}
\tag{SO.22}

Therefore the minimax scale in (SO.11) is

\[
\boxed{
\sqrt{aq}
=\Omega\left({S_D\over\omega_D^{5/2}}\right)
=\Omega\left(
{\sqrt D\over (Z_D+1)\omega_D^{5/2}}
\right)
\longrightarrow\infty.
}
\tag{SO.23}

With the explicit logarithmic choice above, this is

\[
{\sqrt D\over Z_D+1}
\big/\bigl(\log\log(S_D+e^e)\bigr)^{5/2}
\]

up to a fixed positive constant.

Thus, in the small-external heavy-reuse branch, one can force the following finite fork without the prior order-extraction loss:

\[
\boxed{
\begin{array}{ll}
\text{MULTI-MATCHING:}
&\Omega(D\omega_D)\text{ vertex-disjoint }(1+K/D)\text{-pairs};\\[1mm]
\text{or}\quad\text{COMMON-RUN CURRENCY:}
&\Omega(S_D/\omega_D^{5/2})\text{ bounded-face cycle rank}\\
&\text{or the same order of actual bisector displacement on one}\
&\text{SAME/SAME common inactive trunk.}
\end{array}
}
\tag{SO.24}

The common-run currency tends to infinity for every admissible `omega_D` satisfying (SO.14), and can be made `S_D^{1-o(1)}` by choosing `omega_D` sufficiently slowly.

This does not close C-II. It does remove two avoidable losses from the small-external common-run route: the orientation half-thinning and the Erdos-Szekeres square-root thinning. The remaining geometry is now a direct dichotomy between a large plane cycle rank and a same-direction common inactive corridor with large Euclidean support-bisector drift.

C-II remains open. No theorem-state authority is changed.

**Disposition:** reassigned heavy reused edges by their majority traversal orientation, extracted a separated same-orientation module pair with `Omega(D/m^2)` common edges, pigeonholed those edges directly into one lower-run pair, and optimized the resulting cycle-rank versus common-trunk displacement fork. In the sub-square-root external regime the surviving common-run obstruction has scale `Omega((sqrt(D)/(Z_D+1))/omega_D^(5/2))` for an arbitrarily slow admissible `omega_D`.
