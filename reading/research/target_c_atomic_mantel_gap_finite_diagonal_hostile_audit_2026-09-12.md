> Generated reading edition · [exact source](../../research/target_c_atomic_mantel_gap_finite_diagonal_hostile_audit_2026-09-12.md) · source SHA-256 `084824ff2079597017ac9afdaf8a7dcfa1eeba14f83c17dfa7ad7deaee9e4bb0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Hostile audit — all-regime atomic Mantel gap via finite diagonal

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_atomic_mantel_gap_finite_diagonal_2026-09-12.md`  
**Disposition:** **PASS at proof-only scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit specifically rechecks the point that invalidated the earlier compactness
attempt: atomic mass is not semicontinuous under a second weak limit. The repaired proof
does not take such a limit. It freezes atom neighborhoods inside each fixed near-extremal
train-measure limit and then chooses one sufficiently large finite source from that same
realizing sequence. The resulting finite graphs themselves form the diagonal sequence
to which the robust near-complete-grid theorem is applied.

The theorem survives.

---

## 1. Orbit decomposition and weighted Mantel are legitimate

Fix one Type-II subsequential limit from audited §142. Let `mu` be its projective train
direction probability measure, let `x=lim T/D`, and write the atomic masses in absolute
`D` normalization as

$$
a_i=x\,\mu(\{\phi_i\}).
$$

The exact relation

$$
\psi=\phi\pm\pi/3\pmod\pi
$$

partitions the projective circle into three-point orbits. For one orbit let `M_r` be the
sum of its atomic masses and `E_r` the normalized limiting strict-rhombus crossing mass
carried by relation pairs in that orbit.

Audited §142 gives two facts needed here:

1. every limiting quadratic crossing measure is supported on the exact `pi/3` relation;
2. that crossing measure is dominated by the product train-phase measure.

The second point implies that the exact relation carries product mass only through
atoms:

$$
(\mu\times\mu)
\{(\phi,\psi):\psi=\phi+\pi/3\}
=
\int \mu(\{\phi+\pi/3\})\,d\mu(\phi).
$$

Thus no diffuse or singular-continuous part is omitted by the orbit decomposition.

The physical train-crossing graphs are triangle-free. On the three atom vertices of one
orbit, the weighted crossing graph is therefore triangle-free, so weighted Mantel gives

$$
E_r\le M_r^2/4.
$$

This bound remains valid if one or two atom masses vanish.

---

## 2. Near equality forces one dominant orbit without any compactness step

In the contradiction setup of the source, the `j`-th **fixed** subsequential limit has
absolute atomic mass

$$
A_j=x_j\sigma_j
\in[2s_2,2s_2+1/j].
$$

Let `M_{j,r}` and `E_{j,r}` be its orbit masses and crossing masses. Then

$$
s_2^2
=
\sum_rE_{j,r}
\le {1\over4}\sum_rM_{j,r}^2
\le {A_j^2\over4}
=s_2^2+O(1/j).
$$

Hence

$$
A_j^2-\sum_rM_{j,r}^2=o_j(1).
$$

This does force concentration in one orbit even if there are infinitely many positive
orbits. Indeed, if

$$
m_j:=\max_rM_{j,r},
$$

then

$$
\sum_rM_{j,r}^2\le m_jA_j,
$$

so

$$
m_j\ge{\sum_rM_{j,r}^2\over A_j}=A_j-o_j(1).
$$

Thus one orbit has

$$
M_j=2s_2-o_j(1),
$$

and the total mass of all other orbits is `o_j(1)`. Their total crossing capacity is
also `o_j(1)`, so the dominant orbit carries

$$
E_j=s_2^2-o_j(1).
$$

No limit in `j` of the measures themselves is taken.

---

## 3. Shrinking atom neighborhoods are valid continuity sets

For the three atom locations of the dominant orbit, choose disjoint projective arcs of
radius at most `1/j`. Their boundaries can be chosen to have zero `mu_j` mass while the
non-atomic `mu_j` mass captured by the arcs is at most `1/j` beyond the atom masses.
This follows from continuity from above at each point.

The limiting crossing measure is dominated by `mu_j x mu_j`. Therefore a product-set
boundary built from `mu_j`-null arc boundaries also has zero crossing-measure mass.
Consequently the empirical train counts and empirical crossing counts of these fixed
arcs converge along the source sequence realizing the `j`-th limit.

It is therefore legitimate to choose one finite source, with diameter `D_j` as large as
needed, satisfying simultaneously

$$
N_j/D_j=2s_2-o_j(1),
$$

$$
R_j^{orb}/D_j^2=s_2^2-o_j(1),
$$

and Type-II normalized container errors `o_j(1)`. Choosing farther along each realizing
sequence also ensures `D_j->infinity`.

This is the decisive repair over the rejected semicontinuity proof: every statistic is
measured on a finite source after the atom windows have been frozen.

---

## 4. The selected finite crossing graph is genuinely near-Mantel

The complete stopped-train crossing graph is simple and triangle-free by audited §142.
The induced graph on the selected window trains inherits both properties. From

$$
N_j=(2s_2-o_j(1))D_j
$$

and

$$
e(G_j)=(s_2^2-o_j(1))D_j^2
$$

we obtain

$$
e(G_j)=N_j^2/4-o(D_j^2).
$$

Hence the elementary finite near-Mantel lemma from §153 applies directly. It supplies
shores `X_j,Y_j` of size `s_2D_j+o(D_j)`, with only `o(D_j^2)` missing cross-shore
pairs.

No graph-limit or stability theorem beyond that finite lemma is used.

---

## 5. Three shrinking atom windows force a large opposite pair

For large `j`, every selected atom window has projective diameter `<pi/3`. Two trains
from the same window cannot cross in a strict triangle-free unit rhombus, because such a
crossing requires acute projective separation strictly greater than `pi/3`.

If one window had `Omega(D_j)` trains on both Mantel shores, all corresponding
cross-shore same-window pairs would be absent, giving `Omega(D_j^2)` missing pairs.
Thus every linearly populated window belongs, up to `o(D_j)` trains, to one shore.

There are only three windows and both shores have size `s_2D_j+o(D_j)`. Therefore at
least one shore consists, up to `o(D_j)`, of a single window of size

$$
s_2D_j+o(D_j),
$$

while the other shore contains a window of size at least

$$
(s_2/2)D_j+o(D_j).
$$

The two windows are distinct members of one `pi/3` orbit, so their projective axes have
acute separation exactly `pi/3`. Since the total cross-shore missing count is
`o(D_j^2)`, the chosen pair also has only `o(D_j^2)` missing physical rhombus
crossings.

Thus all hypotheses of the independently hostile-audited robust near-complete-grid
theorem hold.

---

## 6. Numerical margin is macroscopic

The robust theorem forces

$$
{3\over2}s_2\le{2\over\sqrt3}.
$$

But

$$
{3\over2}s_2
=1.428469210295936\ldots,
\qquad
{2\over\sqrt3}
=1.1547005383792517\ldots .
$$

The margin is about `0.27377`, so no `o(D)` pruning or shrinking-window error can erase
the contradiction.

---

## 7. Propagation to §§142 and 146

Once the uniform qualitative constant `eta_grid>0` is established, the source's
propagation is algebraic.

Audited §142 gives

$$
q/T\le2(1-\sigma),
$$

hence

$$
(T-q/2)/D\ge x\sigma\ge2s_2+\eta_{grid}.
$$

Using `T-q=2f-k` and `q/D<=pi+o(1)` gives

$$
(2f-k)/D\ge2s_2-\pi/2+\eta_{grid}-o(1).
$$

Repeating the audited §146 elimination with this strengthened input adds exactly
`(2/9)eta_grid` to the weighted diameter-edge floor. The coefficients of `d_H` and
`s_Z` are unchanged.

---

## 8. Scope

- `eta_grid` is existential, not numerically certified.
- No outer-walk detour assumption is used.
- The proof never deletes contact-isolated source points and never inserts them into the
  Section-57 core kernel.
- The result strengthens the Type-II all-regime frontier but does not close Type II or
  the inactive-container branch by itself.
- The earlier file using atomic-mass semicontinuity was deleted; its failure mode remains
  recorded separately as a regression.

**Verdict:** PASS at proof-only scope.
