> Generated reading edition · [exact source](../../../docs/reports/target_c_uniform_terminal_cut_matching_2026-09-09.md) · source SHA-256 `10d700953f2351a995a345da79397498035f18cdfd83eb47479fa4d9ee558073`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-41323D557A2E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — UCM: uniform matching of every terminal response cut to the diameter-beta cut

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-nearzero-physical-carrier`  
**Run type:** exact PSD cut-function theorem  
**Target:** Target C C-II, especially `D epsilon -> 0`  
**Depends on:** C64 PSD response domination, C66 normalization, `q<=pi D`  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

C64 proves

```math
M:=\Lambda-L_H\succeq0,
\qquad M\mathbf 1=0,
\qquad \operatorname{tr}M=2\varepsilon,
```

where

```math
\varepsilon=\sum_{b<k}c_{bk}-1.
```

BRM used this on terminal sets arising from physical branches of `C-z`. The same argument works for **every** terminal subset and the Laplacian kernel gives a sharper centered-indicator estimate.

For `S subseteq B_+`, define

```math
C(S):=\sum_{\substack{b\in S\\k\notin S}}c_{bk},
\qquad
B(S):=\sum_{\substack{b\in S\\k\notin S}}\beta_{bk}.
```

Then:

### Theorem UCM — uniform terminal-cut matching

For every `S subseteq B_+`, with `q=|B_+|`,

```math
\boxed{
0\le C(S)-B(S)
\le
2\varepsilon\,\frac{|S|(q-|S|)}q.
}
\tag{UCM.1}
```

In particular,

```math
\boxed{
0\le C(S)-B(S)
\le\frac q2\varepsilon
\le\frac{\pi D}{2}\varepsilon.
}
\tag{UCM.2}
```

Hence the difficult C66 phase

```math
D\varepsilon\to0
```

satisfies the uniform cut-function convergence

```math
\boxed{
\sup_{S\subseteq B_+}|C(S)-B(S)|\to0.
}
\tag{UCM.3}
```

So the electrical response and mechanical diameter-reaction Laplacians agree not merely entrywise on selected matchings or branchwise at the C66 center, but on **every terminal cut simultaneously**.

---

## 1. Indicator quadratic forms are cut weights

Let

```math
x=\mathbf 1_S\in\mathbb R^{B_+}.
```

For any weighted graph Laplacian `L_w`,

```math
x^TL_wx
=\sum_{\substack{b\in S\\k\notin S}}w_{bk}.
\tag{1.1}
```

Therefore

```math
x^T\Lambda x=C(S),
\qquad
x^TL_Hx=B(S),
```

and hence

```math
\boxed{x^TMx=C(S)-B(S).}
\tag{UCM.4}
```

PSD gives the lower bound in UCM.1 immediately.

---

## 2. Center the indicator using the Laplacian kernel

Because

```math
M\mathbf 1=0,
```

we may subtract any constant multiple of the all-ones vector without changing the quadratic form. Put

```math
y:=x-\frac{|S|}{q}\mathbf 1.
```

Then

```math
x^TMx=y^TMy.
\tag{2.1}
```

A direct calculation gives

```math
\|y\|^2
=|S|\left(1-\frac{|S|}{q}\right)^2
+(q-|S|)\left(\frac{|S|}{q}\right)^2
=\frac{|S|(q-|S|)}q.
\tag{2.2}
```

Since `M` is PSD,

```math
\lambda_{max}(M)
\le\operatorname{tr}M
=2\varepsilon.
```

Thus

```math
C(S)-B(S)
=y^TMy
\le2\varepsilon\|y\|^2
=2\varepsilon\frac{|S|(q-|S|)}q.
```

This proves UCM.1.

The quadratic `s(q-s)/q` is maximized at `s=q/2`, with value `q/4`. Therefore

```math
C(S)-B(S)\le\frac q2\varepsilon.
```

Finally `q<=pi D` gives UCM.2.

---

## 3. Immediate local consequences

### 3.1 Every terminal degree matches its beta incidence

Take `S={b}`. Then

```math
\boxed{
0\le
\sum_{k\ne b}c_{bk}
-
\sum_{k\ne b}\beta_{bk}
\le
2\varepsilon\left(1-\frac1q\right).
}
\tag{UCM.5}
```

So in any `epsilon->0` sequence the total response degree of each individual terminal converges uniformly to its total beta incidence.

### 3.2 Every prescribed boundary interval is matched

If `S` is any cyclic interval of force-hull terminals, UCM.1 applies without any planarity or interval-specific loss. Under `D epsilon->0`, its response cut and beta cut differ by `o(1)` uniformly over all such intervals.

This is useful because circular-planar minors and physical contact separators naturally produce cyclic intervals.

### 3.3 BRM is recovered with a stronger error term

For a component `R` of `C-z`, BRM identifies

```math
C(B_R)=r_R,
\qquad
B(B_R)=w_R+\lambda_R.
```

Therefore UCM gives

```math
0\le r_R-(w_R+\lambda_R)
\le
2\varepsilon\frac{|B_R|(q-|B_R|)}q,
```

which improves BRM's earlier `2epsilon |B_R|` bound and automatically uses the smaller side of a large branch cut.

---

## 4. Near-zero star interpretation

At the C66 center `z`, let

```math
\delta_z:=\sum_{h\not\ni z}\beta_h=o(1).
```

For any terminal subset `S` not containing `z`, the beta cut is

```math
B(S)
=
\sum_{zk\in H,\ k\in S}\beta_{zk}
+O(\delta_z),
\tag{4.1}
```

where the absolute error is at most `delta_z` because only off-star beta edges can contribute anything beyond the `z`-star term.

Thus UCM implies uniformly for all `S` with `z notin S`:

```math
\boxed{
C(S)
=
\sum_{zk\in H,\ k\in S}\beta_{zk}
+o(1).
}
\tag{UCM.6}
```

Similarly, if `z in S`, apply the same statement to the complementary cut.

So the complete response cut function becomes the cut function of an additive star measure centered at `z`, uniformly over all `2^q` terminal subsets.

This is stronger than saying the total off-star response mass is `o(1)`: every nested, laminar, or cyclic terminal cut sees the same asymptotic star measure.

---

## 5. Why UCM is useful for the depth-D carrier

S1E reduces the RCC slope-one endpoint to one physical branch containing a harmonic component of graph diameter `D+o(D)` and response mass `1-o(1)`.

Any sequence of nested terminal intervals cut off by separators along that branch now has response cut values determined, to `o(1)` uniformly, by the beta mass of the corresponding `z`-star leaves.

The next target is therefore no longer a generic electrical-network estimate. It is a **laminar star-cut realization problem**:

> Can a bounded-degree planar unit-contact network of graph depth `D+o(D)` realize, on `Theta(D)` cyclically ordered boundary terminals, a response cut function that is uniformly `o(1)` from one additive star measure, while the same network carries the C72/C74 `Omega(D)` radial contact-stress flux through every depth/radius?

A negative answer would close the RCC slope-one endpoint.

---

## 6. Regression audit

- UCM is an exact consequence of PSD and does not use circular planarity.
- The bound is uniform over all subsets because it depends only on `q`, not on a union bound or number of cuts.
- `epsilon->0` alone gives excellent estimates on small terminal sets, but UCM.3 over all cuts requires `q epsilon=O(D epsilon)->0`.
- UCM does not imply entrywise equality of `c` and `beta` for nonmatching edges without additional algebra; cut functions determine edge weights, but subtracting several `o(1)` cut errors only gives `o(1)` entrywise, not an `o(1/D)` aggregate bound.
- Near-star electrical networks remain possible abstractly. The missing input is the unit-contact/radial carrier geometry.

## 7. Compact handoff

```text
UCM exact cut theorem.
M=Lambda-L_H PSD, M1=0, trM=2epsilon.
For S subset B+, x=1_S and y=x-(|S|/q)1,
    C(S)-B(S)=x^T M x=y^T M y >=0,
while
    ||y||^2=|S|(q-|S|)/q.
Hence
    0 <= C(S)-B(S)
       <=2epsilon |S|(q-|S|)/q
       <=(q/2)epsilon
       <=(pi D/2)epsilon.
Thus D epsilon->0 gives uniform convergence of every response cut to the beta cut.
At C66 star center z, every cut is therefore uniformly the cut of the z-star beta measure plus o(1).
Next: combine nested/cyclic cuts along the S1E depth-D carrier with C72/C74 radial flux.
```
