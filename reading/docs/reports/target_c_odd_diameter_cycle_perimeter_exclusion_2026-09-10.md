> Generated reading edition · [exact source](../../../docs/reports/target_c_odd_diameter_cycle_perimeter_exclusion_2026-09-10.md) · source SHA-256 `6470b99c0c3d3f066334cab317c1ec961c5b097bbaa250e009a0c85da540e013`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-EA43B48CC5CC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — low pinned/contact surplus excludes every diameter cycle

**Date:** 2026-09-10  
**Repository state:** draft PR #178 after CM commit `e9de80b217faf404210f91eee64e12686525203a`; current `main` includes `ff31de4783ff49173d9f4bfdf61364735ff5a590`  
**Run type:** exact diameter-thrackle geometry / branch elimination  
**Target:** Target C, C-II  
**Depends on:** C65 full actual diameter visibility; FS.3 shared-endpoint angle collapse; CP full-source perimeter defect; MP maximal-force-perimeter threshold; classical planar diameter-thrackle crossing property  
**External literature:** checked only for provenance of straight-line thrackle cycle structure; the proof below is elementary and does not import Woodall/Cairns--King classification  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

Put

$$
\lambda_D:=\frac{e_{BB}+2s_C}{D},
\qquad
\lambda_{\rm disk}
=\frac{\pi(\sqrt{3\pi^2+4}-1)}{2(\pi^2+1)}
=0.693272542288314\ldots .
$$

The new theorem eliminates an entire topological branch of the actual diameter graph.
For every fixed

$$
\lambda_0<\lambda_{\rm disk},
$$

there is `D_0(lambda_0)` such that every post-ZF survivor with `D>=D_0` and
`lambda_D<=lambda_0` has an **acyclic actual diameter graph**.

The mechanism is exact.  An odd diameter cycle forces its projective edge directions
to wind around the entire projective direction circle.  FS.3 says consecutive cycle
edges differ by only `O(D^{-1/4})` in projective angle.  Hence actual diameter
directions are `o(1)`-dense in every direction.  Because both the source hull `K` and
force hull `F` have width exactly `D` in every actual diameter direction, their
perimeter difference is only `o(D)`.  CP then gives

$$
\operatorname{per}F=\pi D-o(D),
$$

and MP forces `liminf lambda_D>=lambda_disk`, contradicting the assumed low-surplus
regime.

Since every cycle in a planar diameter graph is odd, no cycle survives.

---

## 1. Exact implication chain

```text
odd actual diameter cycle
    -> every 4-path has crossing first/third diameter edges
    -> all signed turns of the polygonal cycle have the same sign
    -> projective edge directions have nonzero odd winding
FS.3
    -> every projective direction is O(D^(-1/4)) from a cycle edge direction
C65 + width Lipschitz
    -> per(K)-per(F)=O(D^(3/4))=o(D)
CP
    -> per(F)/D -> pi
MP
    -> liminf (e_BB+2s_C)/D >= lambda_disk.
```

This closes the cyclic diameter-support branch below `lambda_disk`; it is not a
numerical refinement of the pinned/contact floor.

---

## 2. A diameter-cycle 4-path has coherent turning sign

Let

$$
v_0v_1\cdots v_{m-1}v_0
$$

be a cycle in the actual diameter graph, and orient its polygonal edges

$$
u_i:=v_{i+1}-v_i,
\qquad |u_i|=D,
$$

with indices modulo `m`.

Every two nonincident diameter segments properly cross.  In particular, in every
4-path

$$
A=v_{i-1},\quad B=v_i,\quad C=v_{i+1},\quad D'=v_{i+2},
$$

the segments `AB` and `CD'` cross.

### Lemma DC.1 — turn-sign coherence

For every `i`,

$$
\operatorname{sgn}\det(u_{i-1},u_i)
=
\operatorname{sgn}\det(u_i,u_{i+1}).
\tag{2.1}
$$

Hence all signed principal turns of the oriented polygonal cycle have the same sign.

### Proof

Apply an orientation-preserving affine change of coordinates taking

$$
B=(0,0),\qquad C=(1,0).
$$

Write

$$
A=(a_x,a_y),\qquad D'=(d_x,d_y).
$$

Then

$$
\operatorname{sgn}\det(B-A,C-B)=\operatorname{sgn}(a_y),
$$

and

$$
\operatorname{sgn}\det(C-B,D'-C)=\operatorname{sgn}(d_y).
$$

Because `AB` and `CD'` cross properly, `A` and `D'` must lie in the same open
half-plane bounded by the line `BC`.  If they lay in opposite half-planes, the
interiors of `AB` and `CD'` would lie in disjoint open half-planes and could not meet.
Thus `a_y d_y>0`, proving (2.1). `square`

No generic thrackle classification is used here; only the pairwise crossing property
of planar diameter segments.

---

## 3. Consecutive projective directions wind monotonically

At vertex `v_i`, let `tau_i in (-pi,pi)` be the signed principal turn from incoming
vector `u_{i-1}` to outgoing vector `u_i`.

The skip chord satisfies

$$
|v_{i+1}-v_{i-1}|\le D.
$$

Since both adjacent cycle edges have length `D`,

$$
|u_{i-1}+u_i|^2
=2D^2+2u_{i-1}\cdot u_i
\le D^2.
$$

Therefore

$$
\frac{u_{i-1}\cdot u_i}{D^2}\le-\frac12,
$$

so

$$
\frac{2\pi}{3}\le|\tau_i|<\pi.
\tag{3.1}
$$

Define the projective angle between the two incident diameter lines by

$$
\alpha_i:=\pi-|\tau_i|.
\tag{3.2}
$$

Then

$$
0<\alpha_i\le\frac\pi3.
$$

The angle `alpha_i` is exactly the smaller angle at `v_i` between the two outgoing
diameter rays `v_iv_{i-1}` and `v_iv_{i+1}`.

By Lemma DC.1, after reversing the cycle orientation if necessary,

$$
\boxed{\tau_i=\pi-\alpha_i\quad\text{for every }i.}
\tag{3.3}
$$

For any closed polygonal curve with no collinear consecutive edges, the sum of signed
principal turns is an integer multiple of `2pi`.  Hence

$$
\sum_{i=0}^{m-1}(\pi-\alpha_i)=2\pi k
\tag{3.4}
$$

for an integer `k>0`.  Thus

$$
\boxed{
\sum_i\alpha_i=(m-2k)\pi.
}
\tag{3.5}
$$

Every planar diameter-graph cycle is odd.  Therefore `m-2k` is a positive odd integer,
and in particular

$$
\boxed{\sum_i\alpha_i\ge\pi.}
\tag{3.6}
$$

Passing from oriented edge vectors to their unoriented projective directions subtracts
`pi` at each turn.  Equation (3.3) therefore says that successive projective edge
directions move with one consistent sign through angle `alpha_i`.  By (3.5) the
resulting closed walk in

$$
\mathbb{RP}^1\cong\mathbb R/\pi\mathbb Z
$$

has nonzero odd winding number.  Consequently it traverses every projective direction
at least once.

This is the only cycle-order fact needed below.

---

## 4. FS makes a diameter cycle direction-dense

FS.3 gives the uniform bound for every pair of actual diameter edges sharing an
endpoint

$$
\alpha_i<\Theta_D
:=2\arccos\!\left(
\frac{D}{D+2\,3^{1/4}\sqrt D}
\right)
=O(D^{-1/4}).
\tag{4.1}
$$

Because the projective direction walk in Section 3 covers the whole projective circle
and every step has length below `Theta_D`, every projective direction `theta` is within
`Theta_D` of the direction of some cycle edge.  Thus the actual diameter direction set
is a `Theta_D`-net in `RP^1`.

This conclusion uses an actual cycle.  A forest can leave a fixed projective gap and is
not covered by this theorem.

---

## 5. Direction density forces force/source perimeter equality to first order

Let

$$
g(\theta):=w_K(\theta)-w_F(\theta)\ge0.
$$

C65 puts every actual diameter endpoint in the force-visible core, so for every actual
diameter direction `theta_h`,

$$
w_K(\theta_h)=w_F(\theta_h)=D,
$$

and therefore

$$
g(\theta_h)=0.
\tag{5.1}
$$

For every diameter-`D` convex body its width function is `D`-Lipschitz on
`RP^1`; this is the support-function bound for the difference body.  Hence `g` is
`2D`-Lipschitz.

By the `Theta_D`-net property, for every projective direction `theta`,

$$
0\le g(\theta)\le2D\Theta_D.
\tag{5.2}
$$

Cauchy's width formula then gives

$$
\boxed{
0\le\operatorname{per}K-\operatorname{per}F
=\int_0^\pi g(\theta)\,d\theta
\le2\pi D\Theta_D
=O(D^{3/4})=o(D).
}
\tag{5.3}
$$

CP gives independently, for every global source,

$$
0\le\pi D-\operatorname{per}K<\frac{\pi\sqrt3}{2}.
\tag{5.4}
$$

Therefore every unbounded post-ZF sequence whose actual diameter graph contains a
cycle satisfies

$$
\boxed{
\frac{\operatorname{per}F}{D}\longrightarrow\pi.
}
\tag{5.5}
$$

---

## 6. Theorem DC — cyclic diameter support is high-surplus

### Theorem DC.2

Let `(A_j)` be any unbounded sequence of post-ZF C-II survivors whose actual diameter
graphs contain cycles.  Then

$$
\boxed{
\liminf_{j\to\infty}
\frac{e_{BB,j}+2s_{C,j}}{D_j}
\ge\lambda_{\rm disk}.
}
\tag{6.1}
$$

### Proof

Section 5 gives `per(F_j)/D_j->pi`.  Apply MP.1. `square`

### Corollary DC.3 — low-surplus diameter graph is a forest

For every fixed `lambda_0<lambda_disk`, there is `D_0(lambda_0)` such that any
post-ZF survivor with

$$
D\ge D_0,
\qquad
\frac{e_{BB}+2s_C}{D}\le\lambda_0
$$

has an acyclic actual diameter graph.

#### Proof

Otherwise choose a sequence with `D_j->infinity`, `lambda_j<=lambda_0`, and a cycle in
every `H_j`.  Theorem DC.2 gives

$$
\liminf\lambda_j\ge\lambda_{\rm disk}>\lambda_0,
$$

a contradiction. `square`

For a forest on `q` nonisolated diameter endpoints and `h` edges,

$$
d_H=q-h
$$

is exactly the number of diameter-tree components.  Thus the low-surplus branch is now
forced into the forest/caterpillar side of the straight-thrackle classification.

---

## 7. Interaction with the new `s_Z=0` theorem on main

The main-branch report at `ff31de4783ff49173d9f4bfdf61364735ff5a590` proves in the
mixed-circuit phase `s_Z=0` that, for an absolute `epsilon_0>0`,

$$
\frac{e_{BB}+2s_C-3d_H}{D}
\ge\lambda_R+\epsilon_0
\tag{7.1}
$$

for all sufficiently large survivors.

DC now shows that throughout the range below `lambda_disk`, that same phase has
`H` a forest, so

$$
\boxed{d_H=\#\{\text{diameter-tree components}\}.}
\tag{7.2}
$$

Hence in the `s_Z=0` low-surplus phase,

$$
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_R+\epsilon_0
+3\frac{\#\text{diameter components}}D.
}
\tag{7.3}
$$

This does not yet eliminate the forest phase, but it converts the formerly abstract
`d_H` defect into a literal component count on the whole remaining low-surplus class.

---

## 8. Adversarial audit and regressions

### Regular odd shell

Its diameter graph is an odd cycle and its force/source hulls coincide.  DC therefore
correctly places it in the high-surplus side: its normalized loaded-contact currency is
asymptotically `pi`, far above `lambda_disk`.

### Dense isolated shell filling

Adding contact-isolated points does not alter the shell diameter cycle or force hull,
so the same conclusion holds.  No global-optimality claim is extracted from the
filling; MP's full-source hypothesis remains the decisive source-specific input.

### Diameter star or caterpillar

These are not excluded.  They are acyclic and can leave a macroscopic projective
direction gap.  This is exactly the surviving branch.

### Turn-sign proof

The proof does not assume that the cycle vertices form a regular polygon, that the
cycle is the standard geometric musquash, or that the projective directions are ordered
by convex-hull vertex order.  The only topological inputs are proper crossing of
nonincident diameter edges and oddness of planar diameter cycles.  The projective
winding follows from the signed-turn calculation.

### Collinearity

Consecutive diameter edges cannot be collinear.  If their outgoing rays from the
shared vertex were equal, their other endpoints would coincide; if opposite, those
endpoints would be distance `2D`, impossible in a diameter-`D` set.  Thus every
principal turn and `alpha_i` used above is well-defined.

---

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| DC.1 coherent turn signs | proved | elementary 4-path crossing geometry |
| nonzero projective winding of odd diameter cycle | proved | coherent turns + closed-polygon turning number + odd parity |
| cycle directions are `Theta_D`-dense | proved | FS.3 step bound + nonzero winding |
| `P_K-P_F=O(D^(3/4))` in cyclic phase | proved | C65 width zeros + Lipschitz + Cauchy |
| cyclic phase implies `lambda>=lambda_disk` asymptotically | proved | CP + MP |
| low-surplus `H` is a forest | proved | all planar diameter cycles are odd |
| forest phase impossible | not proved | caterpillar/star regressions remain |
| Level I | still open | low-surplus forest and high-surplus branches remain |

---

## 10. Exact next obligation

The low-surplus Target C-II problem has now lost its cyclic diameter branch.  A closing
theorem can focus on actual diameter **caterpillar forests**.

The strongest concrete next target is:

> **DCF — diameter-caterpillar forest closure.**  In a post-ZF survivor with
> `lambda_D<lambda_disk-o(1)`, combine FS.3 almost-antipodal shared-endpoint geometry,
> the forest identity `d_H=#components`, RR's three actual bypass edges across every
> nonsingleton contact bridge, and the CM macroscopic isolated chamber to prove either
> `b+Q>2h` or a cardinality-preserving strict sub-`D` competitor.
>
> In the `s_Z=0` subcase, equation (7.3) may be used as an exact component cost.

A proof need no longer handle odd diameter cycles in this low-surplus regime.
