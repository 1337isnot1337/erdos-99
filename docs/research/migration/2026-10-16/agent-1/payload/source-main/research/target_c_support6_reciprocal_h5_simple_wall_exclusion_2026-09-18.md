# Target C-II — simple-wall reciprocal `H5` support-six blocks are impossible

**Date:** 2026-09-18  
**Status:** proof-only structural strengthening; theorem-state authority unchanged  
**Scope:** the noncollapsed degree-pure support-six reciprocal `H5` endpoint after the exact finite reduction  
**Depends on:** `target_c_support6_reciprocal_h5_reduction_2026-09-18.md`; the ground-cone bound `phi_0<pi/3`; the already proved same-sign duplicate-ray lemma  
**Certificate:** `research/verify_target_c_support6_reciprocal_h5_simple_wall_exclusion_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding exact reduction left ten symmetry orbits on simple ground-collinearity walls. This note eliminates all ten directly from the ground unit-force equation.

The point is that a simple wall has only five distinct ground rays. After merging the duplicated pair, the signed multiplicities are forced into one of two words. Both words contradict the strict angular ordering of forward unit-circle chords.

Therefore

\[
\boxed{\text{every simple-ground-wall reciprocal `H5` support-six candidate is impossible.}}
\]

Together with the preceding double-wall exclusion, every nonuniform reciprocal `H5` support-six candidate is now empty. Before the uniform-orbit strengthening in the companion note, the noncollapsed `H5` branch consists only of the six uniform symmetry orbits.

---

## 1. Ground rays on a simple wall

Use the notation of the exact `H5` reduction. The reciprocal hull is

\[
0,1,2,3,4,
\]

with ground point `0`, while `5,6` are interior reciprocal points. The ground hull angle satisfies

\[
\phi_0<\frac\pi3.
\]

Hence all six raw ground rays lie in one open cone of width less than `pi/3`.

On a simple wall exactly one allowed triple `0,u,v` is collinear, and `uv` is a missing matching edge. The rays `0u` and `0v` coincide. The preceding duplicate-ray lemma proves that their reciprocal signs are equal. All other ground rays are distinct from each other and from that duplicated ray.

Collapse the tied pair to one direction. Write the resulting five distinct unit directions in increasing angular order as

\[
v_1,v_2,v_3,v_4,v_5,
\qquad
\theta_1<\theta_2<\theta_3<\theta_4<\theta_5,
\qquad
\theta_5-\theta_1<\frac\pi3.
\]

Each distinct ray has a signed multiplicity `c_j`: a singleton contributes `+1` or `-1`, and the duplicated ray contributes `+2` or `-2`. The ground equilibrium is

\[
\sum_{j=1}^5 c_jv_j=0.
\tag{1.1}
\]

Because the original ground split is `3+3`, one has

\[
\sum_{j=1}^5 c_j=0.
\tag{1.2}
\]

---

## 2. Exact enumeration leaves only two multiplicity words

Re-run the exact simple-wall survivor enumeration from the preceding certificate. For each of its eighty labelled survivors:

1. merge the unique tied ground-ray pair;
2. sort the five distinct ray classes by the exact rank-three chirotope;
3. sum the two edge signs in the duplicated class and keep the singleton signs; and
4. globally reverse all reciprocal signs if necessary so the first coefficient is positive.

The result is exactly

\[
\boxed{
(c_1,\ldots,c_5)
\in
\left\{
(1,-2,1,-1,1),
(1,-1,1,-2,1)
\right\}.
}
\tag{2.1}
\]

Each word occurs for exactly forty of the eighty labelled survivors. No floating-point geometry is used in this classification.

---

## 3. Summation by parts converts the two words to impossible chord identities

Put

\[
\Delta_k=v_{k+1}-v_k,
\qquad
S_k=\sum_{j=1}^k c_j,
\qquad 1\le k\le4.
\]

Since the total signed multiplicity is zero, summation by parts gives

\[
\sum_{j=1}^5 c_jv_j
=-\sum_{k=1}^4 S_k\Delta_k.
\tag{3.1}
\]

For the first word in (2.1),

\[
(S_1,S_2,S_3,S_4)=(1,-1,0,-1),
\]

so (1.1) would force

\[
\boxed{\Delta_1=\Delta_2+\Delta_4.}
\tag{3.2}
\]

For the second word,

\[
(S_1,S_2,S_3,S_4)=(1,0,1,-1),
\]

so (1.1) would force

\[
\boxed{\Delta_4=\Delta_1+\Delta_3.}
\tag{3.3}
\]

But for unit vectors

\[
\Delta_k
=2\sin\frac{\theta_{k+1}-\theta_k}{2}
\exp i\left(\frac{\theta_k+\theta_{k+1}}2+\frac\pi2\right).
\tag{3.4}
\]

Thus

\[
\arg\Delta_1<\arg\Delta_2<\arg\Delta_3<\arg\Delta_4,
\tag{3.5}
\]

and all four chord directions lie in one open halfplane; in fact their total angular spread is less than `pi/3`.

The argument of a positive sum of two nonparallel vectors in an open halfplane lies strictly between their arguments. Hence:

- `Delta_2+Delta_4` has argument strictly between `arg Delta_2` and `arg Delta_4`, so it cannot equal `Delta_1`; and
- `Delta_1+Delta_3` has argument strictly between `arg Delta_1` and `arg Delta_3`, so it cannot equal `Delta_4`.

Both possible ground words are impossible.

Therefore none of the eighty labelled simple-wall survivors from the preceding finite reduction can satisfy the exact ground unit-force equilibrium.

---

## 4. Consequence for the `H5` branch

The previous work already proved:

- the simple `056` wall has no sign/order survivor; and
- every higher-codimension double-ground-wall configuration is impossible.

This note removes the remaining simple walls. Hence

\[
\boxed{\text{the noncollapsed support-six reciprocal `H5` branch is uniform.}}
\tag{4.1}
\]

At this stage that leaves the six uniform symmetry orbits from the exact finite reduction. The companion uniform-angle note removes three of those six.

No theorem-state file is changed.

**Disposition:** proved that the full simple-wall family violates the ground unit-force equation. C-II remains open.
