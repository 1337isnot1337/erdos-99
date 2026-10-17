> Generated reading edition · [exact source](../../../docs/reports/target_c_nearzero_slope_one_endpoint_2026-09-09.md) · source SHA-256 `a9aae6310e4d2ade6145b238e92bd1ba8bdf2e692cc67405e1e90cff23f7c6f7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D6B33D2F2564","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — S1E: classification of the RCC slope-one near-zero endpoint

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-nearzero-physical-carrier`  
**Run type:** equality-case structural reduction  
**Target:** Target C C-II, `D epsilon ->0` and minimum RCC slope  
**Depends on:** RCC, NLC, BRM, HSR, ZK/ZU, C40/C41  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

RCC proves that every sequence with response defect `epsilon->0` satisfies

```math
\liminf\frac{e_{BB}+2s_C}{D}\ge1.
```

S1E classifies the equality endpoint of this new bound.

Assume an unbounded post-ZF survivor sequence satisfies

```math
D\varepsilon\to0
\tag{S1E.1}
```

and

```math
\boxed{
\frac{e_{BB}+2s_C}{D}\to1.
}
\tag{S1E.2}
```

Then there is a unique unloaded harmonic component `I_*` with

```math
\boxed{
\delta_*=D+o(D),
\qquad
\sum_{r\ne *}\delta_r=o(D),
}
\tag{S1E.3}
```

and it carries asymptotically all mechanical contact stress and electrical response:

```math
\boxed{
S_*=D^2-o(D^2),
\qquad
C_*=1-o(1).
}
\tag{S1E.4}
```

The exact ZK remainder simultaneously collapses:

```math
\boxed{
R_I=o(D),
\qquad
s_B=o(D),
\qquad
d_H=o(D),
\qquad
s_Z=o(D).
}
\tag{S1E.5}
```

Consequently:

- the giant component itself has Eppstein slack `r_*=o(D)`;
- the loaded contact-degree budget is asymptotically saturated;
- the full diameter graph has `q-h=o(D)` and hence asymptotically saturates Hopf--Pannwitz;
- by BRM, one physical component of `C-z` carries `1-o(1)` of the `z`-star beta mass, `z`-response mass, and contact-stress mass;
- every other unloaded component has total graph diameter `o(D)`.

This is the exact slope-one survivor that remains after RCC. It is simultaneously a near-geodesic harmonic conductor, a near-Eppstein extremal triangle-free penny graph, and a near-maximal diameter thrackle.

---

## 1. NLC gives at least one depth-`D` component

Under S1E.1, NLC gives a nonempty family `R_z` of at most three harmonic components, each satisfying

```math
\delta_r>D-3,
```

and carrying together `1-o(1)` long `z`-response mass.

Let

```math
m:=|R_z|.
```

NLC's branch-count inequality is

```math
e_{BB}+2s_C
\ge
mD-(3m+6)+3(d_H+s_Z).
\tag{1.1}
```

Divide by `D` and use S1E.2. Since `d_H,s_Z>=0`, necessarily

```math
\boxed{m=1}
\tag{S1E.6}
```

for all sufficiently large members of the sequence.

Call the unique long harmonic component `I_*`. Then

```math
\boxed{\delta_*>D-3.}
\tag{1.2}
```

---

## 2. The whole component-diameter budget collapses onto `I_*`

Put

```math
L:=e_{BB}+2s_C,
\qquad
k:=d_H+s_Z.
```

ZK gives

```math
\sum_r\delta_r
\le
L_2:=6-3k+L
\le6+L.
\tag{2.1}
```

S1E.2 says

```math
L=D+o(D).
```

Together with (1.2),

```math
D-3<\delta_*
\le\sum_r\delta_r
\le D+o(D).
```

Hence

```math
\boxed{\delta_*=D+o(D).}
\tag{S1E.7}
```

Subtracting from (2.1),

```math
0\le\sum_{r\ne *}\delta_r
\le6+L-\delta_*
=o(D),
```

which proves S1E.3.

---

## 3. Exact ZK slack vanishes linearly

ZK's exact identity is

```math
\sum_r\delta_r+R_I+s_B+3(d_H+s_Z)
=6+L.
\tag{3.1}
```

By S1E.3 and S1E.2,

```math
\sum_r\delta_r=D+o(D),
\qquad
6+L=D+o(D).
```

Every remaining term on the left side of (3.1) is nonnegative. Therefore

```math
R_I+s_B+3(d_H+s_Z)=o(D).
```

Thus separately

```math
\boxed{
R_I=o(D),
\quad s_B=o(D),
\quad d_H=o(D),
\quad s_Z=o(D).
}
```

This proves S1E.5.

Because

```math
R_I=\sum_rr_r,
\qquad r_r\ge0,
```

the giant Eppstein slack satisfies

```math
\boxed{r_*=o(D).}
\tag{3.2}
```

For `I_*`, with `n_*` internal vertices and `e_*` internal contacts,

```math
r_*=2n_*-\delta_*-2-e_*.
```

Hence

```math
\boxed{
e_*=2n_*-\delta_*-2-o(D).}
\tag{S1E.8}
```

So the giant internal contact graph asymptotically saturates Eppstein's triangle-free penny-graph edge bound at graph diameter `D+o(D)`.

Also

```math
s_B=3q-e_{BI}-2e_{BB}=o(D),
```

so

```math
\boxed{e_{BI}+2e_{BB}=3q-o(D).}
\tag{S1E.9}
```

The loaded contact-degree budget is asymptotically saturated.

Finally

```math
d_H=q-h=o(D),
```

so

```math
\boxed{h=q-o(D).}
\tag{S1E.10}
```

Thus the full diameter graph also asymptotically saturates the Hopf--Pannwitz edge bound.

---

## 4. The giant component carries all long response and almost all stress

Since `I_*` is the unique NLC long component and the total long `z`-response mass is `1-o(1)`, it has

```math
\sum_{\substack{k\in A_*\\|z-k|>D-1}}
c^{(*)}_{zk}
=1-o(1).
\tag{4.1}
```

Therefore its total response conductance satisfies

```math
\boxed{C_*\ge1-o(1).}
\tag{4.2}
```

The global total response conductance is `1+epsilon=1+o(1)`, so in fact

```math
\boxed{C_*=1-o(1).}
\tag{S1E.11}
```

HSR/C41 coordinate energy gives

```math
S_*
=\sum_{s<t\in A_*}c^{(*)}_{st}|s-t|^2.
```

Use only the long star terms in (4.1):

```math
S_*
\ge(D-1)^2(1-o(1))
=D^2-o(D^2).
```

The total contact stress is exactly `D^2`, so

```math
\boxed{S_*=D^2-o(D^2).}
\tag{S1E.12}
```

This proves S1E.4.

The same argument gives that every contact edge outside `I_*` and its attachment edges carries aggregate stress `o(D^2)`.

---

## 5. Physical branch concentration

BRM compares each component `R` of `C-z` branch-by-branch:

```math
r_R=w_R+o(1),
```

where `r_R` is response mass from `z` into `R` and `w_R` is `z`-star beta mass in `R`.

Since only `I_*` carries nonvanishing long response, exactly one physical component `R_*` of `C-z` has

```math
\boxed{r_{R_*}=1-o(1).}
\tag{S1E.13}
```

BRM then gives

```math
\boxed{w_{R_*}=1-o(1).}
\tag{S1E.14}
```

and NLC/coordinate energy gives total contact stress in that branch

```math
\boxed{S_{R_*}=D^2-o(D^2).}
\tag{S1E.15}
```

Thus electrical response, diameter reaction, and contact stress all choose the same physical branch.

The branch may still be a C71 multi-port return component; S1E does not falsely turn it into a single physical edge.

---

## 6. Rhombic-bulk / external-population split

C42 applies to the full force-visible contact core. If its core population `m_C` satisfies

```math
m_C=\Omega(D^2),
```

then all but `O(D)` bounded-face incidences lie in strict unit rhombi. In that case S1E says a quadratic rhombic bulk coexists with a single depth-`D`, near-Eppstein, almost-all-stress harmonic carrier.

If instead

```math
m_C=o(D^2),
```

then the global source has a quadratic population not represented by the force-visible core. OP/ER localize the only unpaid population to contact-isolated points outside the force hull unless the force-hull Oler capacity itself is asymptotically saturated.

Thus the slope-one endpoint reduces to the same two global structures that remain in the project, but now with the additional strong carrier constraints S1E.3--S1E.15.

---

## 7. Why this is not yet Level I

Two regressions remain genuine.

1. A long strict-rhombic ladder/grid can have a `D+o(D)` geodesic direction and make transverse positive stresses arbitrarily small.
2. The global source can contain a quadratic weakly loaded or contact-isolated population outside the mechanically dominant branch.

S1E eliminates neither regression by local graph counting alone.

What it does eliminate is the possibility that the RCC slope-one endpoint is mechanically diffuse: it is forced into one near-geodesic component that simultaneously saturates the relevant response, stress, Eppstein, loaded-degree, and diameter-graph ledgers.

---

## 8. Next target

The strongest next theorem is a **joint Eppstein/radial stability theorem**:

> A triangle-free penny graph carrying a harmonic component with `delta=D+o(D)`, Eppstein slack `o(D)`, contact stress `D^2-o(D^2)`, and C74 radial flux `(0.90348-o(1))D` through every Euclidean radius must, outside `o(D)` defects, be a bounded-width strict-rhombic train aligned with the `z` radial direction.

Once such a train is obtained, PR #126's bridge-hinge peeling theorem handles articulation-rich portions, while Target B's train/phase machinery handles the 2-connected rhombic portions. The remaining requirement would be to make one of those two existing exclusions uniform under `o(D)` defects.

## 9. Compact handoff

```text
S1E endpoint classification.
Assume D epsilon->0 and L=(e_BB+2s_C)=D+o(D).
NLC branch-count inequality forces exactly one long harmonic component I_*.
It has delta_*>D-3. ZK gives sum delta<=6+L, hence
    delta_*=D+o(D),
    sum_{r!=*}delta_r=o(D).
Exact ZK identity then forces
    R_I=o(D), s_B=o(D), d_H=o(D), s_Z=o(D).
Therefore
    r_*=o(D),
    e_*=2n_*-delta_*-2-o(D)  (near Eppstein equality),
    e_BI+2e_BB=3q-o(D)       (loaded degree saturation),
    h=q-o(D)                  (Hopf-Pannwitz saturation).
The unique long component carries response 1-o(1) and stress D^2-o(D^2).
BRM puts beta star mass, response mass, and contact stress in the same physical C-z branch.
Remaining endpoint: one depth-D near-Eppstein harmonic carrier + rhombic bulk or quadratic external population.
```
