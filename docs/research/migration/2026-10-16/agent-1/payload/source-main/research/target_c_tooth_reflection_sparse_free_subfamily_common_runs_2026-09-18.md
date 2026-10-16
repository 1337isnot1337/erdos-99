# Target C-II — sparse FREE subfamilies improve common-run currency to an `omega^(3/2)` loss

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion; proof-only refinement of the all-inactive FREE multi-module branch  
**Scope:** slow-scale FREE side of the module ANCHORED/FREE dichotomy, especially `Z_D=|A\setminus F|=o(sqrt(D))`  
**Dependencies:** slow-scale central reflection braid; module anchor dichotomy; multi-module lower-edge reuse; upper-gate injection into `A\setminus F`; common-run Euler-characteristic identity; two-normal common-trunk cone theorem  
**Certificate:** `research/verify_target_c_tooth_reflection_sparse_free_subfamily_common_runs_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The fixed extreme-pair endpoint removes all slow-scale loss from the heavy common-run branch, but its complementary matching branch is only linear in `D`. The preceding growing-family theorem keeps a superlinear matching branch but paid `omega_D^(5/2)` in the common-run currency. There is a better interpolation.

Thin the full FREE family to only `m=m_D` evenly spaced modules, with

\[
m\to\infty,
\qquad
m=o(N_D),
\]

where `N_D` is the available FREE-module count. Apply the lower-edge reuse theorem with threshold `R=1`. The light branch is already `Omega(mD)`, while the heavy branch needs only two occurrences of one edge. Assign each heavy edge to its first and last participating selected modules. The selected normal spacing is `Theta(1/m)`, so the pair already has enough two-normal separation. No majority-orientation extraction is required because common-trunk traversal parity can be handled componentwise.

The result is a strictly stronger Pareto fork than the previous `m=Theta(omega_D^2), R=Theta(omega_D)` tuning:

\[
\boxed{
\Omega(mD)\text{ inverse-}D\text{ matching}
\quad\text{or}\quad
\Omega\!\left(
\frac{\sqrt D}{(Z_D+1)m^{3/2}}
\right)
\text{ cycle-rank / two-normal drift.}
}
\tag{SF.1}
\]

Taking `m=omega_D` gives an `omega_D^(3/2)` loss instead of `omega_D^(5/2)` while preserving a superlinear matching alternative.

Fix

\[
c_*:=0.129220199818177\ldots,
\qquad
h_*:=\frac{\sqrt{303}}{52},
\qquad
K>h_*,
\qquad
\alpha_K:=1-\frac{h_*}{K}>0.
\tag{SF.2}
\]

## 1. Evenly thinning the FREE family gives `Theta(1/m)` angular spacing

Use any admissible slow reflection scale

\[
\kappa_D\to\infty,
\qquad
\kappa_D=o(D^{1/4}).
\]

On the FREE side of the module dichotomy there are

\[
\boxed{
N_D\ge
\left(\frac{c_*}{2}-o(1)\right)
\frac{D^{1/4}}{\kappa_D}
}
\tag{SF.3}
\]

FREE modules in normal order. Consecutive FREE modules are separated by at least the original selected-normal gap

\[
\delta_D=(2-o(1))\kappa_DD^{-1/4}.
\tag{SF.4}
\]

Let `m=m_D` satisfy

\[
2\le m\le N_D,
\qquad
m\to\infty,
\qquad
m=o(N_D).
\tag{SF.5}
\]

Choose `m` FREE modules at approximately equally spaced indices in the ordered FREE list, including its first and last elements. The index gap between consecutive chosen modules is at least

\[
\left\lfloor\frac{N_D-1}{m-1}\right\rfloor.
\]

Therefore the thinned family has consecutive normal gap

\[
\begin{aligned}
\gamma_D
&\ge
\delta_D
\left\lfloor\frac{N_D-1}{m-1}\right\rfloor\\
&\ge
\boxed{
\left(c_*-o(1)\right)\frac1m.
}
\end{aligned}
\tag{SF.6}
\]

The floor loss is `o(1/m)` because `m=o(N_D)`. The underlying selected base normals remain in one quadrant, and the canonical support normals differ from them by `O(D^-1/4)`.

## 2. Use the reuse theorem at the minimal threshold `R=1`

Apply the multi-module lower-edge reuse theorem to these `m` selected FREE modules with

\[
R=1.
\]

Every module contributes at least `(alpha_K-o(1))D` good original lower edges satisfying

\[
1<|e|\le1+\frac KD.
\tag{SF.7}
\]

At least one of the following occurs.

### SPARSE-MULTI-MATCHING

The original source contains a vertex-disjoint matching of old fully inactive outer-face source pairs of size

\[
\boxed{
\left(\frac{\alpha_K}{22}-o(1)\right)mD
}
\tag{SF.8}
\]

satisfying (SF.7).

Because `m->infinity`, this matching is superlinear in `D`.

### SPARSE-HEAVY-REUSE

There are at least

\[
\boxed{
\left(\frac{\alpha_K}{2}-o(1)\right)D
}
\tag{SF.9}

distinct original good lower edges occurring in at least two selected ancestries.

The rest of the note treats SPARSE-HEAVY-REUSE.

## 3. A fixed selected pair shares `Omega(D/m^2)` edges with angle `Omega(1/m)`

For each heavy edge `e`, take the first and last selected modules containing `e`. Because `e` appears in at least two selected modules, these are distinct. Assign `e` to that module pair.

By (SF.6), every assigned pair has normal separation at least

\[
\boxed{
\theta\ge\gamma_D
\ge
\left(c_*-o(1)\right)\frac1m.
}
\tag{SF.10}
\]

There are at most `binom(m,2)` assigned pairs. Pigeonholing (SF.9) gives one fixed pair `i,j` sharing at least

\[
\boxed{
\left(\alpha_K-o(1)\right)
\frac{D}{m^2}
}
\tag{SF.11}

distinct original good lower edges.

This uses all shared edges. There is no degree-six matching thinning and no orientation-majority thinning.

## 4. Pigeonhole directly into a pair of all-lower runs

Put

\[
Z_D:=|A\setminus F|.
\]

Every all-inactive ancestry has at most `Z_D+1` maximal lower runs. Distributing the shared edges in (SF.11) among the at most `(Z_D+1)^2` run pairs yields one pair

\[
P\subset\mathcal A_i,
\qquad
Q\subset\mathcal A_j
\]

sharing `q` distinct good edges with

\[
\boxed{
q\ge
\left(\alpha_K-o(1)\right)
\frac{D}{m^2(Z_D+1)^2}.
}
\tag{SF.12}

Let

\[
I:=P\cap Q.
\]

Every edge-containing component of `I` is a common path. On each component, the traversal of `Q` is either the same as or opposite to the traversal of `P`; the parity is constant on that component. Thus the two-normal cone theorem applies componentwise without any global orientation extraction.

## 5. Componentwise cone geometry and Euler characteristic

For any threshold `s>=1`, if no component of `I` contains at least `s` selected common edges, those `q` edges occupy at least `q/s` different components. Since `P,Q` are connected paths sharing edges,

\[
\boxed{
\beta(P\cup Q)\ge\frac qs-1.
}
\tag{SF.13}

The union lies in the common plane short-edge graph, so this is also its bounded-face count.

Otherwise one common component `C` contains at least `s` selected edges and therefore at least `s` path edges. Let `X` be its endpoint displacement and let `theta` be the angle between `N_i,N_j`.

- If the component traversal is SAME, the two-normal cone theorem gives
  \[
  X\cdot B>s\sin(\theta/2),
  \qquad
  B=\frac{N_i+N_j}{|N_i+N_j|}.
  \]
- If it is OPPOSITE, it gives
  \[
  X\cdot T>s\cos(\theta/2),
  \qquad
  T=\frac{N_i-N_j}{|N_i-N_j|}.
  \]

The selected base normals lie in one quadrant and the canonical support-normal error is `O(D^-1/4)`, so `theta<=pi/2+o(1)`. By (SF.10), monotonicity of sine, and `m->infinity`,

\[
\sin(\theta/2)
\ge
\sin\left(\frac{c_*-o(1)}{2m}\right)
=
\left(\frac{c_*}{2}-o(1)\right)\frac1m.
\tag{SF.14}
\]

The OPPOSITE coefficient is larger because `cos(theta/2)>=cos(pi/4)-o(1)`. Hence every common component with `s` selected edges has drift at least

\[
\boxed{
\left(\frac{c_*}{2}-o(1)\right)\frac{s}{m}
}
\tag{SF.15}

in its appropriate two-normal axis.

## 6. Optimized sparse-family fork

Set

\[
b_m:=\left(\frac{c_*}{2}-o(1)\right)\frac1m.
\]

Choosing

\[
s=\sqrt{q/b_m}
\]

up to integer rounding balances (SF.13) and (SF.15). Therefore SPARSE-HEAVY-REUSE implies

\[
\boxed{
\text{either }
\beta(P\cup Q)
\ge
\sqrt{b_mq}-O(1),
\quad\text{or one common component has drift }
\ge
\sqrt{b_mq}-O(1).
}
\tag{SF.16}
\]

Using (SF.12),

\[
\boxed{
\sqrt{b_mq}
\ge
\left(
\sqrt{\frac{\alpha_Kc_*}{2}}-o(1)
\right)
\frac{\sqrt D}{(Z_D+1)m^{3/2}}.
}
\tag{SF.17}

Thus the finite proof-only fork is

\[
\boxed{
\begin{array}{ll}
\text{SPARSE-MULTI-MATCHING:}
&\displaystyle
\left(\frac{\alpha_K}{22}-o(1)\right)mD
\text{ disjoint }(1+K/D)\text{-pairs};\\[3mm]
\text{or}\quad\text{COMMON-RUN CURRENCY:}
&\displaystyle
\left(
\sqrt{\frac{\alpha_Kc_*}{2}}-o(1)
\right)
\frac{\sqrt D}{(Z_D+1)m^{3/2}}
\text{ bounded faces or two-normal drift.}
\end{array}
}
\tag{SF.18}
\]

For `K=1`,

\[
\boxed{
\frac{\alpha_1}{22}
=0.0302387279846773\ldots
}
\tag{SF.19}
\]

and

\[
\boxed{
\sqrt{\frac{\alpha_1c_*}{2}}
=0.207321005198949\ldots .
}
\tag{SF.20}
\]

## 7. Small-external tuning

Assume

\[
Z_D=o(\sqrt D),
\qquad
S_D:=\frac{\sqrt D}{Z_D+1}\to\infty.
\tag{SF.21}
\]

Take, for example, the base slow scale

\[
\kappa_D=\log\log D.
\]

Then the available FREE population has order at least `D^(1/4)/log log D`. Choose any `omega_D` satisfying

\[
\omega_D\to\infty,
\qquad
\omega_D=o\left(\frac{D^{1/4}}{\log\log D}\right),
\qquad
\omega_D^{3/2}=o(S_D),
\tag{SF.22}
\]

and set

\[
m=\lfloor\omega_D\rfloor.
\]

Such a scale always exists because both upper envelopes in (SF.22) diverge. An explicit diagonal choice is

\[
\omega_D
=
\min\left\{
\left(\frac{D^{1/4}}{\log\log D}\right)^{1/2},
S_D^{1/3}
\right\},
\tag{SF.23}
\]

up to harmless truncation for small `D`.

Then (SF.18) becomes

\[
\boxed{
\Omega(D\omega_D)
\text{ vertex-disjoint inverse-}D\text{ pairs}
}
\tag{SF.24}
\]

or

\[
\boxed{
\Omega\left(\frac{S_D}{\omega_D^{3/2}}\right)
\to\infty
}
\tag{SF.25}

bounded-face cycle rank or common-trunk Euclidean drift.

For an arbitrarily slowly diverging admissible `omega_D`, the common-run currency is again

\[
S_D^{1-o(1)},
\]

but the explicit slow loss has improved from the preceding `omega_D^(5/2)` to `omega_D^(3/2)` while retaining a superlinear matching branch.

## 8. Relation to the fixed-pair endpoint

The fixed extreme-pair theorem corresponds to taking a bounded `m`. It obtains the natural `Theta(S_D)` heavy-branch currency, but the complementary matching branch is only `Theta(D)`, a conclusion already available from one FREE module. The present sparse-family theorem keeps `m->infinity`, so its matching side is genuinely amplified to `Omega(mD)` while losing only `m^(3/2)` on the common-run side.

This is the relevant frontier improvement over the previous `omega_D^(5/2)` theorem. It does not close C-II and does not change the canonical theorem ledger.

The remaining bridge is unchanged in kind but quantitatively sharper: turn either the superlinear inactive inverse-`D` matching or the diverging outer-face cycle-rank/two-normal drift into the canonical aggregate outer-walk detour/force-hull currency, an exact unit triangle, or a source-preserving strict diameter decrease.

**Disposition:** evenly thinned the full FREE normal family, used the minimal heavy-reuse threshold `R=1`, assigned each twice-reused edge directly to a separated selected module pair, retained all shared edges through the lower-run pigeonhole, and applied componentwise two-normal cone geometry. The resulting common-run loss is `m^(3/2)` rather than `m^(5/2)` while the complementary matching remains superlinear.