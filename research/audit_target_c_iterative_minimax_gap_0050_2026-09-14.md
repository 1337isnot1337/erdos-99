# Independent hostile audit — iterative-pruning matched atomic gap `0.0050`

**Date:** 2026-09-14  
**Source branch:** `research/c2-gluing-sol-20260914-r10`  
**Audited inputs:** iterative-pruning pair payment `a85427bc`; matched minimax theorem `45f90ce0`; Section-171 certificate `c4d18925`  
**Target:** C-II, canonical full-core Type-II branch  
**Disposition:** **PASS at proof-only scope**  
**Theorem-state authority:** unchanged

## LEVEL I STATUS

`STILL OPEN`

This audit checks the jump from the independently audited minimax excess `g=0.002123`
to the matched all-train/rhombic excess

\[
\boxed{g=0.0050.}
\]

The gain is not decimal tuning.  It comes from a new two-shore iterative-pruning lemma
which prevents residual missing edges from being charged independently on both shores.

## 1. Iterative residual pruning is correctly single-charged

After the existing inversion-chain cover, write the normalized inversion and residual
missing masses as `u+v=rho`.  The inversion cover deletes at most
`sqrt(2u)D+o(D)` trains in total.  The surviving missing graph has at most
`(v+o(1))D^2` edges.

Set `tau=sqrt(v/2)`.  Repeatedly delete, from either shore, a current vertex whose
current residual missing degree exceeds `tau D+o(D)`.  Each deletion removes more
than that many currently surviving missing edges.  A residual edge disappears at its
first deleted endpoint and cannot pay for a second deletion.  Therefore the total
number of iterative-pruning deletions across both shores is at most

\[
{v\over\tau}D+o(D)=\sqrt{2v}\,D+o(D).
\]

At termination every retained train misses at most `tau D+o(D)` opposite trains.
This is a valid improvement over two independent Markov prunings.

## 2. The large-family threshold guarantees triple common neighbors

On the branch

\[
m_*:=\min(a,b)>\sqrt{2u}+{5\over\sqrt2}\sqrt v,
\]

even if all inversion-cover and iterative-pruning losses fall on one shore, each
retained family has mass greater than

\[
{5\over\sqrt2}\sqrt v-\sqrt{2v}=3\sqrt{v/2}=3\tau.
\]

Every retained train misses at most `tau D+o(D)` opposite trains, so the union of the
missing-neighbor sets of any three retained trains has size at most
`3 tau D+o(D)`, strictly below the opposite retained population.  Thus every pair and
triple has a common opposite neighbor, exactly the input needed by the already-audited
`K_{2,2}` consistency and triple-neighbor transitivity arguments.

## 3. The denominator `10` and fallback branch are correct

Relative to the original two family masses, the opposite-corner selected degree sum
loses at most

- `sqrt(2u)` from the inversion cover;
- `sqrt(2v)` from all iterative deletions combined; and
- `2 tau=sqrt(2v)` from the two selected corner missing-degree deficits.

With `K=2/sqrt(3)` and `g_*=(a+b-K)_+`, the audited source-diameter projection gives

\[
g_*\le\sqrt{2u}+2\sqrt{2v}\le\sqrt{10\rho}.
\]

Hence the large-family branch pays `rho>=g_*^2/10`.
If the large-family threshold fails, Cauchy gives

\[
m_*\le\sqrt{29\rho/2},
\qquad \rho\ge2m_*^2/29.
\]

The branches are exhaustive.

## 4. The unconditional pair corollary has the right minimum direction

In the matched minimax application `a,b<=K`.  If `M=max(a,b)` and `m=min(a,b)`, then

\[
g_*=m+M-K\le m.
\]

Therefore both entries of

\[
\min\{g_*^2/10,2m^2/29\}
\]

are at least `2g_*^2/29`, since `1/10>2/29`.  Thus

\[
\boxed{\rho\ge{2\over29}(a+b-K)_+^2,}
\]

or equivalently

\[
a+b-\sqrt{29/2}\sqrt\rho\le K.
\]

This direction is correct; reversing it would invalidate the `0.0050` jump.

## 5. Weighted two-leaf minimax remains valid

For dominant-orbit phases `C>=U>=V`, the already-audited triangle-free correlation is

\[
(1-V/C)x+(1-U/C)y\le h.
\]

Applying the unconditional pair inequality to both leaves and taking the corresponding
positive weighted average yields

\[
\max(F_U,F_V)\ge {W+C\over2}
-\sqrt{29/2}\sqrt{h\,{C\over3C-W}}.
\]

The outward rational verifier covers a strict superset of the actual center-imbalance
domain and gives

\[
\max(F_U,F_V)>{2\over\sqrt3}+0.00160857.
\]

The independent run of `verify_target_c_iterative_minimax_atomic_gap_0050.py` passes
with worst interval near `z=-0.01387`.

## 6. Rhombic-only transfer is legitimate

The argument is rerun on the strict-rhombus train graph rather than deleting singleton
trains after an all-train proof.  The graph is simple and triangle-free, its edge mass
is exactly the strict-rhombus mass, limiting crossings occur at projective separation
`pi/3`, and the iterative pair theorem uses the same train-order/missing-crossing
structure.  Hence

\[
\boxed{
\liminf T_R/D\ge2\sqrt{\Delta_2}+0.0050,
\qquad
\liminf\sigma_R/D\ge0.0100.
}
\]

## 7. Section-171 propagation passes independently

With

\[
\epsilon_0=0.0023374,
\qquad
\delta_0={{9\over2}\epsilon_0-0.0050\over2}=0.00275915,
\]

the Fraction certificate proves the Section-171 endpoint function negative by more
than `2.7e-5` and its detour derivative greater than `142` on the feasible interval.
Together with the already-audited monotonicity in `t`, this yields

\[
\boxed{
\liminf {q-k\over D}
\ge {4\over9}(\pi+\sqrt{\Delta_2})+0.0023374.
}
\]

The independent run of `verify_target_c_g0050_global_propagation.py` passes.

## 8. Disposition

**PASS at proof-only scope.**  The matched iterative-pruning theorem supersedes the
`g=0.002123` scalar chain:

\[
\boxed{(T-q/2)/D\ge2\sqrt{\Delta_2}+0.0050-o(1),}
\]

\[
\boxed{T_R/D\ge2\sqrt{\Delta_2}+0.0050-o(1),\quad
\sigma_R/D\ge0.0100-o(1),}
\]

\[
\boxed{(q-k)/D\ge {4\over9}(\pi+\sqrt{\Delta_2})+0.0023374-o(1).}
\]

This remains proof-only and does not close C-II.  The next useful work is to propagate
the stronger matched rhombic floor into the source-level low-`t` structure rather than
tune `g` further.
