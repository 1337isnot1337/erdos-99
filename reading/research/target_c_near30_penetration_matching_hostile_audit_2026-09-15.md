> Generated reading edition · [exact source](../../research/target_c_near30_penetration_matching_hostile_audit_2026-09-15.md) · source SHA-256 `b9420675d35c8d292a8874bfed05946635517de54ef7da94fdb32d2a3f7eb402`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "97732d34e6e48e6e81a555f9247ce9bcae9854eb", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_near30_penetration_matching_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "468f33b24c8c56d3a524e01a3b4d6e6b48f02399b421bf13c01451847dcbb245"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — near-30-degree convex-route penetration matching

**Date:** 2026-09-15  
**Reviewed:** `research/target_c_near30_penetration_matching_2026-09-15.md`  
**Disposition:** **PASS at proof-only current low-`t` full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The theorem pushes the straightness window close to the limiting `30` degrees, so the
important audit question is whether the small fixed angular margin survives the
near-disk normal-comparison error. It does, but only because the theorem chooses
`epsilon=0.003` rather than taking `beta=pi/6` exactly.

---

## 1. Convex-route count is applied at the correct occurrence level

The merged convex-route theorem proves for every fixed `beta<=pi/6`

```math
S_\beta\ge x_B-{d_{out}\over1-\cos\beta}.
```

This is an outer-route **occurrence** count. At

```math
\beta_*={\pi\over6}-0.003,
```

the coefficient

```math
A_*={1\over1-\cos\beta_*}-1
=6.5483948971\ldots
```

is larger than `4`. Under

```math
2\delta+\kappa/2\le R(t),
```

the worst penalty is therefore at `delta=R/2`, `kappa=0`, exactly as claimed. The
certificate gives

```math
S_*/D\ge1.3018186084367357\ldots-o(1).
```

**Verdict:** PASS.

---

## 2. Occurrence deduplication uses the full repetition surplus, not a per-route claim

Let `s_x` be the number of straight outer occurrences of physical vertex `x` and
`m_x` its total outer-walk multiplicity. If `s_x>0`,

```math
s_x-1\le m_x-1.
```

Summation gives

```math
S_*-V_*
=\sum_{s_x>0}(s_x-1)
\le\sum_x(m_x-1)
=b-V_{out}.
```

This remains valid if one physical vertex lies on different distinguished pocket
routes. No per-route physical injectivity is assumed.

The merged near-simple theorem gives

```math
(b-V_{out})/D
\le0.0459365399110338116\ldots+o(1),
```

hence

```math
V_*/D\ge1.2558820685257019\ldots-o(1).
```

For simple-outer vertices one loses the repetition budget once more, because the
number of repeated physical vertices is itself at most `b-V_out`. Therefore

```math
V_{simp,*}\ge S_*-2(b-V_{out}),
```

which gives the displayed `1.2099455286...D` floor.

**Verdict:** PASS.

---

## 3. Degree collapse still holds this close to 30 degrees

The degree-collapse proof requires only `beta<=pi/6`. At one straight occurrence the
outer face sector has angle

```math
g>\pi-2\beta,
```

and the complementary sector contains `d-1` contact-ray gaps, all strictly larger than
`pi/3`. Thus

```math
(d-1){\pi\over3}<\pi+2\beta\le{4\pi\over3},
```

so `d<=4`. Loaded-route exclusion makes the physical tail unloaded, and C26 gives
`d>=3`.

Thus every selected physical tail really has an extra contact available after its two
route incidences are fixed.

**Verdict:** PASS.

---

## 4. The signed margin is larger than the nearby-normal error

For

```math
\varepsilon=0.003,
\qquad
\beta_*=\pi/6-\varepsilon,
```

a selected extra contact satisfies

```math
e\cdot n_x>\sin(\pi/6+\varepsilon)
=0.5025958223159282\ldots .
```

A route edge at another `beta_*`-straight occurrence has

```math
|e\cdot n_w|<\sin\beta_*
=0.4973996776874467\ldots .
```

The difference is

```math
0.0051961446284815\ldots .
```

For bounded-distance outer-route occurrences the audited route-midpoint / near-disk
argument gives

```math
\angle(n_x,n_w)
\le
\theta_0+o(1),
\qquad
\theta_0=2\arcsin(0.002883975/2)
=0.0028839759994559\ldots .
```

For unit normals,

```math
|e\cdot n_x-e\cdot n_w|
\le|n_x-n_w|
\le\angle(n_x,n_w).
```

Hence the normal-comparison error is strictly smaller than the signed/route gap.

**Verdict:** PASS.

---

## 5. One physical edge cannot be selected at two tails

If the same undirected unit edge were extra at both selected tails, orient it from
`x` to `y` as `e`. Then

```math
e\cdot n_x>s_*,
\qquad
e\cdot n_y<-s_*,
\qquad
s_*:=\sin(\pi/6+\varepsilon).
```

Thus the two normals are separated by more than

```math
\pi-2\arccos s_*
={\pi\over3}+2\varepsilon.
```

Type-II near-disk geometry then separates the corresponding loaded-hull side midpoints
by a fixed positive fraction of `D`. The two outer tails themselves are unit distance
apart, while each lies within

```math
s_i+d_i/2
```

of its side midpoint, with `max s_i=o(D)` and `d_i+d_j<=d_out<=0.002883975D+o(D)`.
The resulting upper bound is `o(D)+0.001442D`, far below the fixed-fraction lower
bound. Contradiction.

This is the same hostile-audited mechanism as the merged signed-injectivity theorem,
with a slightly stronger angular separation than its limiting `pi/3` threshold.

**Verdict:** PASS.

---

## 6. Common opposite-endpoint multiplicity is at most two

If selected contacts `x_aw` share an opposite endpoint `w`, then
`|x_a-x_b|<=2`. Their associated normals therefore all lie in a projective angular
cluster of diameter at most `theta_0+o(1)`.

Each selected direction `e_a=w-x_a` lies within

```math
\gamma_*={\pi\over3}-\varepsilon
```

of its local normal. A deliberately loose common interval bound is

```math
2(\gamma_*+\theta_0)+o(1).
```

The numerical margin is

```math
{2\pi\over3}
-2(\gamma_*+\theta_0)
=2(\varepsilon-\theta_0)
=0.0002320480010881\ldots>0.
```

So for sufficiently large `D` all selected directions at `w` lie in an interval
strictly shorter than `2pi/3`. Triangle-freeness makes any two contact rays at `w`
separated by strictly more than `pi/3`. Three cannot fit.

Hence the opposite-endpoint degree is at most two.

The fixed positive margin is small, but it is not asymptotically zero; this is why the
choice `0.003` is safe.

**Verdict:** PASS.

---

## 7. The opposite endpoint cannot itself be a selected straight tail

Suppose selected edge `xw` ends at another selected straight tail `w`. The two hull
normals differ by at most `theta_0+o(1)` because `|x-w|=1`.

If the edge is extra at `w`, the two signed inequalities are incompatible with nearly
equal normals.

If it is a route edge at `w`, then

```math
e\cdot n_x
\le|e\cdot n_w|+|n_x-n_w|
<\sin\beta_*+\theta_0+o(1).
```

The finite certificate verifies

```math
\sin\beta_*+\theta_0
<\sin(\pi/6+\varepsilon).
```

This contradicts signed inwardness at `x`.

Therefore the chosen tail set and opposite-endpoint set are disjoint.

**Verdict:** PASS.

---

## 8. Matching and train restriction are exact

The selected penetration graph is bipartite. Every left tail has degree exactly one by
construction; every right endpoint has degree at most two. Therefore each connected
component is a star of one or two edges, and a maximum matching has size at least half
the edge count. This gives

```math
M_*/D\ge0.6279410342628509\ldots-o(1).
```

The chosen physical edges are distinct. A singleton stopped train contains exactly one
physical edge, so at most the total singleton-train population can escape the strict
rhombus trains. Using the conservative independently audited singleton bound rather
than the newer unaudited `0.00042` increment gives

```math
E_{R,*}/D\ge0.3396497995359795\ldots-o(1)
```

and

```math
M_{R,*}/D\ge0.1698248997679897\ldots-o(1).
```

The simple-outer version similarly gives

```math
M_{R,simp,*}/D\ge0.1468566298124728\ldots-o(1).
```

Restricting an already maximum-degree-two bipartite graph to an edge subset cannot
invalidate the matching bound.

**Verdict:** PASS.

---

## 9. What the theorem does not prove

A long one-rhombus-thick convex boundary strip is a genuine regression. One train can
carry linearly many pairwise vertex-disjoint penetration edges, so the matching does
not imply a linear number of distinct trains.

Likewise, the theorem does not assign KKT weight to the selected contacts and does not
make their individual motions independently feasible.

The gain is narrower but real: endpoint concentration, physical-edge reuse, and the
near-30-degree angular loss are no longer the bottlenecks. The remaining obstruction is
macroscopic strip/train occupancy or simultaneous deformation.

**Final verdict:** **PASS at proof-only current low-`t` full-core Type-II scope. C-II
remains open.**
