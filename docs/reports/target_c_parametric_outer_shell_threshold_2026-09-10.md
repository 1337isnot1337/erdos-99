<!-- theorem-state: {"artifact_id":"ART-7BD3B9D37FF4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact parametric threshold for the inactive outer-shell phase

**Date:** 2026-09-10  
**Repository branch:** `research/c2-general-mu05947-20260910`  
**Run type:** phase-boundary theorem  
**Target:** Target C, all post-ZF survivors  
**Depends on:** GR generalized RSJ inequality, EA exact Eppstein force-bulk bound, OS full-source perimeter theorem  
**Computation:** none; decimal values are diagnostic only

## LEVEL I STATUS

`STILL OPEN`.

The preceding outer-shell report used the convenient cutoff `mu<=0.60`.  The same
mechanism has an exact maximal range.

Define

\[
\boxed{
 u_\pi:=
 \frac{\pi\bigl(\sqrt{3\pi^2+4}-1\bigr)}{2(\pi^2+1)}
 =0.6932725422\ldots .
}
\tag{PT.1}
\]

For every fixed

\[
0<u<u_\pi,
\]

there is a unique number

\[
p_u\in(2,\pi)
\]

satisfying

\[
\boxed{
\frac\pi{(\pi-2)^2}\left(\frac{p_u}{2}-1\right)^2
=
\frac\pi4u^2+
\frac{(u+p_u/2)^2}{4\pi}.
}
\tag{PT.2}
\]

Every post-ZF survivor sequence with

\[
\mu_D\le u+o(1),
\qquad
\mu_D:=\frac{e_{BB}+2s_C-3(d_H+s_Z)}D,
\]

then satisfies

\[
\boxed{
\limsup\frac{P_F}{D}\le p_u<\pi.
}
\tag{PT.3}
\]

Since every global minimizer has

\[
P_K>\pi D-\frac{\pi\sqrt3}{2},
\]

it follows that

\[
\boxed{
P_K-P_F\ge(\pi-p_u)D-O(1).
}
\tag{PT.4}
\]

Consequently some source point outside the positive force hull has one-sided support
excess at least

\[
\boxed{
\frac{\pi-p_u}{2\pi}D-O(1).
}
\tag{PT.5}
\]

By C36 and C65 this point is a fully inactive contact-isolated rattler and is not a
diameter endpoint.

At the same time EA gives

\[
\boxed{
\liminf\frac{|R|}{n}
\ge1-\frac{4u^2}{\pi^2}.
}
\tag{PT.6}
\]

Thus every fixed normalized-surplus window below `u_pi` is an inactive outer-shell
phase with both positive source-density and linear geometric protrusion.  At the
limiting cutoff itself the RSR perimeter obstruction disappears: `p=pi` becomes
compatible with the relaxed inequality.  Hence `u_pi` is the exact endpoint of this
particular mechanism, not an arbitrary numerical stopping point.

Level I remains open because the phase `mu>=u_pi-o(1)` has no contradictory upper
bound, while the outer-shell phase still lacks a finite rearrangement theorem.

---

## 1. The perimeter-only necessary inequality

GR proves that every post-ZF subsequential limit `(mu,y,p)` satisfies

\[
\max\{\Phi(y),\Psi(p)\}
\le
\frac\pi4\mu^2+
\frac{(\mu+p/2)^2}{4\pi},
\tag{1.1}
\]

where

\[
\Psi(p)=\frac\pi{(\pi-2)^2}\left(\frac p2-1\right)^2.
\]

Discard the `Phi(y)` term.  If `mu<=u`, monotonicity of the right side in `mu>=0`
gives the necessary condition

\[
\boxed{
\Psi(p)
\le
\frac\pi4u^2+
\frac{(u+p/2)^2}{4\pi}.
}
\tag{1.2}
\]

Define the difference

\[
g_u(p):=
\Psi(p)-
\frac\pi4u^2-
\frac{(u+p/2)^2}{4\pi}.
\tag{1.3}
\]

As a function of `p`, `g_u` is a quadratic with leading coefficient

\[
\frac{\pi}{4(\pi-2)^2}-\frac1{16\pi}>0.
\tag{1.4}
\]

Moreover

\[
g_u(2)<0.
\tag{1.5}
\]

Therefore, if `g_u(pi)>0`, convexity implies that there is exactly one zero
`p_u` above `2`, it lies in `(2,pi)`, and

\[
g_u(p)>0\qquad(p>p_u).
\tag{1.6}
\]

The necessary condition (1.2) then forces `p<=p_u` whenever `p>2`; if `p<=2`, the same
conclusion is automatic because `p_u>2`.  This proves PT.3 once the exact range
`g_u(pi)>0` is identified.

---

## 2. Exact threshold where `p=pi` first becomes feasible

At `p=pi`, the symmetric area lower bound is the disk value:

\[
\Psi(\pi)=\frac\pi4.
\tag{2.1}
\]

Hence

\[
g_u(\pi)>0
\]

is equivalent to

\[
\frac\pi4
>
\frac\pi4u^2+
\frac{(u+\pi/2)^2}{4\pi}.
\tag{2.2}
\]

Multiply by `4pi`:

\[
\pi^2
>
\pi^2u^2+(u+\pi/2)^2.
\]

Equivalently

\[
\boxed{
(\pi^2+1)u^2+\pi u-\frac{3\pi^2}{4}<0.
}
\tag{2.3}
\]

The positive root is exactly

\[
\frac{-\pi+\sqrt{\pi^2+3\pi^2(\pi^2+1)}}{2(\pi^2+1)}
=
\frac{\pi(\sqrt{3\pi^2+4}-1)}{2(\pi^2+1)}
=u_\pi.
\]

Thus

\[
\boxed{g_u(\pi)>0\iff0\le u<u_\pi.}
\tag{2.4}
\]

This proves existence/uniqueness of `p_u` and PT.3.

At `u=u_pi`, `g_u(pi)=0`, so the perimeter-only mechanism can no longer force a
linear deficit from `pi D`.  This proves the claimed optimality of the cutoff for this
argument.

---

## 3. Full-source perimeter converts the deficit into inactive support

OS proves for every global minimizer, without any triangle-free assumption,

\[
P_K>
\pi\left(\sqrt{D^2+\frac34}-\frac{\sqrt3}{2}\right)
>
\pi D-\frac{\pi\sqrt3}{2}.
\tag{3.1}
\]

Combining with PT.3 gives

\[
P_K-P_F
\ge
(\pi-p_u)D-O(1),
\]

which is PT.4.

Cauchy's width formula gives

\[
P_K-P_F
=
\int_0^\pi(w_K-w_F)\,d\theta.
\tag{3.2}
\]

The integrand is nonnegative because `F subseteq K`.  Therefore some direction has

\[
w_K-w_F
\ge
\frac{\pi-p_u}{\pi}D-O(1).
\tag{3.3}
\]

A width is the sum of the two opposite support functions, so one side contributes at
least half this gap.  This proves PT.5.

Every positive-core vertex lies in `F`: loaded vertices by definition, and every
unloaded component by C36's convex-hull attachment theorem.  Hence a source support
point outside `F` lies outside the positive core.  C65 identifies it as fully inactive
and non-diametral.

---

## 4. Simultaneous population consequence

EA proves

\[
\limsup\frac vn
\le
\frac4{\pi^2}
\left(\mu-\frac{s_B}{D}\right)^2
\le
\frac4{\pi^2}\mu^2.
\]

Thus every sequence with `mu_D<=u+o(1)` satisfies PT.6.

For orientation:

- `u=0.60` gives at least `85.4%` rattlers and recovers the previous explicit window;
- `u=0.65` gives at least about `82.9%` rattlers;
- `u=0.69` gives at least about `80.7%` rattlers;
- as `u` approaches `u_pi`, the guaranteed rattler fraction remains above `80%`.

The exact decimal percentages are not used in the proof.

---

## 5. Regression audit

### 5.1 Why the endpoint cannot be pushed past `u_pi` by this proof

At `u=u_pi`, `p=pi` satisfies the perimeter-only relaxed equality.  A nearly circular
force hull with dense inactive filling is therefore an exact regression against any
claim that GR+RSR alone forces `P_K-P_F=Omega(D)` above this threshold.

### 5.2 The regular odd shell

A regular odd diameter shell has asymptotically circular force hull and belongs to the
Woodall cyclic topology.  PT does not exclude it as a graph/response regression; the
outer-shell conclusion is only for `u<u_pi`.

### 5.3 Rattler density is not closure

A scaled near-triangular strict packing can carry positive source density with no unit
contacts.  PT therefore does not infer a packing-density contradiction from PT.6.
Global optimality is used only through EA's source-density normalization and OS's
strict translated-lattice source perimeter theorem.

### 5.4 No hidden hull-saturation normalization

`K` is the actual source hull and `F` the actual positive force hull of the
contact/diameter-lexicographically selected source.  No separate hull-saturated
representative is introduced.

---

## 6. Exact new phase split

The entire post-ZF C-II branch now has a natural quantitative split:

### PT-L: inactive outer-shell phase

For any fixed `u<u_pi`, a sequence with `mu_D<=u+o(1)` has

\[
|R|/n\ge1-4u^2/\pi^2-o(1)
\]

and a fully inactive source point protruding beyond `F` by

\[
\frac{\pi-p_u}{2\pi}D-O(1).
\]

### PT-H: high renormalized-defect phase

Any sequence avoiding every such fixed outer-shell window must satisfy

\[
\boxed{\liminf\mu_D\ge u_\pi=0.6932725422\ldots .}
\tag{6.1}
\]

In exact component/loaded currency,

\[
\mu_DD+6
=
\sum_r(\delta_r+r_r)+s_B.
\]

Thus PT-H requires at least `u_pi D+o(D)` of component boundary/face defect plus loaded
contact-degree slack.

This is a stronger phase description than the earlier ad hoc split at `0.60`.

---

## 7. Precise remaining implication

A full C-II closure can now target the two disjoint mechanisms:

1. prove a finite rearrangement / boundary-order packing theorem excluding PT-L for
   one fixed `u` below `u_pi`; and
2. prove a topology/response upper bound
   \[
   \mu_D<u_\pi-o(1)
   \]
   excluding PT-H.

Either improvement to the second threshold immediately enlarges the first outer-shell
window.  Merely improving the old `0.5947` lower constant no longer changes this phase
boundary.

---

## 8. Claim classification

| Claim | Classification | Reason |
| --- | --- | --- |
| exact threshold PT.1 | proved | solve `g_u(pi)=0` |
| unique `p_u<pi` for `u<u_pi` | proved | convex quadratic, `g_u(2)<0<g_u(pi)` |
| force-hull perimeter PT.3 | proved | GR perimeter-only necessary inequality |
| inactive support gap PT.5 | proved | OS full-source perimeter + Cauchy widths + C36/C65 |
| rattler fraction PT.6 | proved | EA |
| optimality of `u_pi` for GR+RSR perimeter mechanism | proved | `p=pi` becomes feasible at equality |
| exclusion of PT-L | not proved | finite rearrangement still missing |
| exclusion of PT-H | not proved | no upper bound on `mu` below `u_pi` |
| Level I | still open | both phase mechanisms survive |

---

## 9. Promotion recommendation

**Promote after the GR/EA/OS dependency chain is independently audited.**  PT gives the
natural exact phase boundary for that chain and replaces the arbitrary numerical
`0.60` split.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Define
  u_pi = pi(sqrt(3pi^2+4)-1)/(2(pi^2+1))
       = 0.6932725422...

For every fixed u<u_pi, let p_u in (2,pi) be the unique root of
  Psi(p_u)=pi u^2/4+(u+p_u/2)^2/(4pi).

GR implies mu<=u+o(1) => P_F/D<=p_u<pi.
OS gives P_K>pi D-pi sqrt3/2, so
  P_K-P_F >= (pi-p_u)D-O(1).
Cauchy widths then give a fully inactive C65 rattler with one-sided support
protrusion at least
  (pi-p_u)/(2pi) D-O(1).

EA simultaneously gives
  rattler fraction >=1-4u^2/pi^2-o(1).
This remains >80% even as u approaches u_pi.

Above u_pi the current RSR perimeter mechanism genuinely stops: p=pi is feasible
in the relaxed inequality.

Remaining exact split:
  PT-L: rule out the macroscopic inactive outer shell below u_pi by finite
        rearrangement/boundary-order packing;
  PT-H: prove mu<u_pi-o(1) from Woodall/attachment/response topology.
```
