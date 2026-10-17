> Generated reading edition · [exact source](../../../docs/reports/target_c_nearzero_series_extremality_2026-09-09.md) · source SHA-256 `a6b315a1f60bee35c4c2d448e539e52b27765ce108af73521e24093955a40607`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 1 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-D8293663BF20","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — NSE: near-zero response saturates the series/cut bound

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-nearzero-physical-carrier`  
**Run type:** exact electrical cut bound + equality-case localization  
**Target:** Target C C-II, C66 phase `D epsilon ->0`  
**Depends on:** C41/C64, C66/C70, UCM, contact-stress normalization  
**New external literature:** none; the cut argument is the elementary Nash--Williams/Cauchy resistance bound, proved below  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

Let `z` be the C66 star center and let

```math
P:=N_H(z)=\{k:zk\in H\}
```

be its actual diameter partners. Assume

```math
D\varepsilon\to0.
\tag{NSE.1}
```

Then the contact network, viewed electrically with conductances equal to positive KKT contact stresses, is asymptotically an equality case of the elementary series bound between `z` and the sink set `P`.

Let

```math
L:=d_C(z,P)
```

be the minimum contact-graph distance from `z` to a diameter partner. Since every contact edge has Euclidean length one and every `k in P` satisfies `|z-k|=D`,

```math
L\ge D.
\tag{NSE.2}
```

Let `A_i` be the total contact stress on edges joining graph-distance layer `i` from `z` to layer `i+1`, for `0<=i<L`.

Then:

### Theorem NSE — series extremality

Under NSE.1,

```math
\boxed{\frac LD\to1,}
\tag{NSE.3}
```

```math
\boxed{
\frac1{D^2}\sum_{i=0}^{L-1}A_i\to1,
}
\tag{NSE.4}
```

and therefore the total contact stress on edges whose graph-distance endpoints lie in the same layer is `o(D^2)`.

If

```math
\mu:=\frac1L\sum_{i=0}^{L-1}A_i,
```

then

```math
\boxed{\frac\mu D\to1}
\tag{NSE.5}
```

and

```math
\boxed{
\frac1L
\sum_{i=0}^{L-1}
\frac{(A_i-\mu)^2}{\mu A_i}
\to0.
}
\tag{NSE.6}
```

Consequently, for every fixed `eta>0`, all but `o(D)` layer cuts satisfy

```math
\boxed{
(1-\eta)D<A_i<(1+\eta)D.
}
\tag{NSE.7}
```

Thus the near-zero phase has an almost-uniform series profile: approximately `D` edge-disjoint graph layers, each carrying total contact conductance approximately `D`, using essentially the entire `D^2` mechanical stress budget.

This is stronger than C72's pointwise lower bound on graph-layer stress, but it remains compatible with a square/rhombic ladder whose transverse contacts have vanishing stress. That regression is retained explicitly.

---

## 1. Response mass is concentrated on the actual diameter partners of `z`

Let

```math
s_b:=\sum_{bk\in H}\beta_{bk},
\qquad
d_b^c:=\sum_{k\ne b}c_{bk}.
```

For every terminal `b`, UCM with the singleton cut gives

```math
0\le d_b^c-s_b\le2\varepsilon.
\tag{1.1}
```

At the C66 center,

```math
s_z=S_z=1-\delta_z=1-o(1).
```

Hence

```math
\boxed{d_z^c=1-o(1).}
\tag{NSE.8}
```

Let

```math
O:=B_+\setminus(\{z\}\cup P).
```

Every beta incidence at a vertex in `O` comes from a nonstar diameter edge, so

```math
\sum_{b\in O}s_b\le2\delta_z=o(1).
\tag{1.2}
```

Summing (1.1) over `O` and using `q=O(D)` gives

```math
\sum_{b\in O}d_b^c
\le2\delta_z+2q\varepsilon
=o(1)
\tag{1.3}
```

under NSE.1.

Therefore

```math
\sum_{k\in O}c_{zk}=o(1).
```

Subtracting from NSE.8,

```math
\boxed{
\sum_{k\in P}c_{zk}=1-o(1).
}
\tag{NSE.9}
```

This identifies the actual mechanical diameter partners, not merely arbitrary far response terminals, as the electrical sink set carrying asymptotically unit response.

---

## 2. Effective conductance from `z` to the shorted partner set tends to one

Work first in the Kron-reduced response graph on `B_+`. Short all terminals in `P` to voltage one, fix `z` at voltage zero, and leave all terminals in `O` electrically free. Let `G_eff` be the resulting effective conductance.

Every edge `zk` with `k in P` has fixed voltage drop one under every admissible potential, so NSE.9 gives

```math
G_{eff}
\ge\sum_{k\in P}c_{zk}
=1-o(1).
\tag{2.1}
```

For the reverse bound, use the admissible potential assigning voltage one to every terminal other than `z`. Its energy is exactly `d_z^c`. Thus by NSE.8,

```math
G_{eff}\le d_z^c=1-o(1).
\tag{2.2}
```

Therefore

```math
\boxed{G_{eff}=1-o(1).}
\tag{NSE.10}
```

Schur complementation preserves effective conductance, so the same `G_eff` is obtained in the original contact network with conductances `alpha_e`, after fixing `z=0`, shorting `P=1`, and leaving every other vertex free.

---

## 3. Graph-distance layer cuts

Let

```math
d(v):=d_C(z,v).
```

For `0<=i<L`, define

```math
U_i:=\{v:d(v)\le i\}.
```

No sink in `P` lies in `U_i` by definition of `L`. Every contact edge joins vertices whose graph distances differ by at most one. Hence the contact cut `partial U_i` consists exactly of edges joining layer `i` to layer `i+1`.

Let its total contact conductance/stress be

```math
A_i:=\sum_{\substack{uv\in C\\d(u)=i,\ d(v)=i+1}}\alpha_{uv}.
\tag{3.1}
```

The cut edge sets for different `i` are pairwise disjoint.

Consider the unit electrical current from `z` to the shorted sink set `P` realizing effective resistance

```math
R_{eff}:=1/G_{eff}.
```

The net current crossing every cut `partial U_i` is one. If the edge currents on that cut are `I_e`, Cauchy gives

```math
1
=\left(\sum_{e\in\partial U_i}I_e\right)^2
\le
\left(\sum_{e\in\partial U_i}\frac{I_e^2}{\alpha_e}\right)
\left(\sum_{e\in\partial U_i}\alpha_e\right).
```

Therefore the dissipated energy on the `i`th cut satisfies

```math
\sum_{e\in\partial U_i}\frac{I_e^2}{\alpha_e}
\ge\frac1{A_i}.
\tag{3.2}
```

The cut edge sets are disjoint, so summing their energy contributions gives the elementary Nash--Williams bound

```math
\boxed{
R_{eff}\ge\sum_{i=0}^{L-1}\frac1{A_i}.
}
\tag{NSE.11}
```

No external theorem is needed beyond this one-line Cauchy proof.

---

## 4. Chain the resistance and stress inequalities

Cauchy again gives

```math
\left(\sum_iA_i\right)
\left(\sum_i\frac1{A_i}\right)
\ge L^2.
\tag{4.1}
```

Each contact edge belongs to at most one graph-distance layer cut. The normalized KKT virial identity gives total contact stress

```math
\sum_{e\in C}\alpha_e=D^2.
```

Hence

```math
\sum_iA_i\le D^2.
\tag{4.2}
```

Combining NSE.11, (4.1), and (4.2),

```math
\boxed{
\frac1{G_{eff}}
\ge
\sum_i\frac1{A_i}
\ge
\frac{L^2}{\sum_iA_i}
\ge
\frac{L^2}{D^2}
\ge1.
}
\tag{NSE.12}
```

But NSE.10 gives

```math
1/G_{eff}=1+o(1).
```

Therefore every inequality in NSE.12 is asymptotically tight.

In particular

```math
\frac{L^2}{D^2}\to1,
```
which proves NSE.3.

Also

```math
\frac{L^2}{\sum_iA_i}\to1.
```
Together with `L/D->1` and `sum A_i<=D^2`, this gives NSE.4.

The only contact edges not counted in `sum A_i` have equal graph-distance endpoints. Since total contact stress is `D^2`, NSE.4 proves that their total stress is `o(D^2)`.

---

## 5. Near equality forces almost-uniform layer capacities

Put

```math
S_A:=\sum_iA_i,
\qquad
\mu:=S_A/L.
```

NSE.3--NSE.4 give

```math
\mu/D\to1,
```
which is NSE.5.

From NSE.12 and NSE.10,

```math
\sum_i\frac1{A_i}\to1,
```
while

```math
\frac{L^2}{S_A}\to1.
```
Hence

```math
\frac{S_A}{L^2}\sum_i\frac1{A_i}\to1.
\tag{5.1}
```

Now

```math
\begin{aligned}
\frac1L\sum_i
\left(
\frac{A_i}{\mu}+\frac{\mu}{A_i}-2
\right)
&=
1+\frac{\mu}{L}\sum_i\frac1{A_i}-2\\
&=
\frac{S_A}{L^2}\sum_i\frac1{A_i}-1.
\end{aligned}
```

The right side tends to zero by (5.1). Since

```math
\frac{A_i}{\mu}+\frac{\mu}{A_i}-2
=
\frac{(A_i-\mu)^2}{\mu A_i},
```

we obtain NSE.6.

For fixed `eta>0`, if

```math
A_i\notin[(1-\eta)\mu,(1+\eta)\mu],
```

then the summand in NSE.6 is bounded below by a positive constant depending only on `eta`. Therefore only `o(L)=o(D)` layers are exceptional. Since `mu/D->1`, this proves NSE.7.

---

## 6. Equality interpretation

NSE shows that the entire near-zero contact network is close, in its **weighted graph-distance profile**, to a series conductor of length `D` and cross-sectional conductance `D`:

- minimum contact distance from the C66 center to its actual diameter partners is `D+o(D)`;
- almost all `D^2` contact stress lies on graph-distance-advancing edges;
- almost every layer cut has total contact stress `(1+o(1))D` in the fixed-eta sense;
- the effective conductance from `z` to the diameter-partner sink set is `1-o(1)`.

This is compatible with several parallel chains or a strict-rhombic ladder whose vertices in each graph layer are nearly equipotential. Therefore NSE does **not** claim a single combinatorial path.

The equality class is best thought of as a layered network with negligible transverse/same-layer stress.

---

## 7. Interaction with C72/C74 and S1E

C72 already proves a pointwise lower bound on every pre-sink graph-layer cut, asymptotically at least `~0.866D` from the star reaction. NSE improves this on all but `o(D)` layers to the sharp value `(1+o(1))D` and simultaneously proves the matching total stress upper budget.

C74 gives a Euclidean-radius analogue with outward signed stress at least `0.90348D-o(D)` through every radius. Thus a near-zero survivor is simultaneously almost-series in graph distance and strongly outward in Euclidean radius.

At the S1E slope-one endpoint, all nonvanishing response/stress lies in one physical branch and one harmonic component. NSE then applies entirely inside that carrier up to `o(D^2)` stress.

---

## 8. Regression audit

- A two-rail square ladder with each longitudinal rail carrying approximately half the cross-sectional stress is compatible with NSE.
- More generally, a layered network with several parallel chains and negligible transverse stress can attain the same series bound.
- NSE controls **stress weight**, not the number of transverse contacts.
- The sink set is the actual diameter-neighbor set `P=N_H(z)`, not an arbitrary response-defined far set.
- `L` is graph distance in the full positive contact network. Since every contact edge has length one, `L>=D` is exact.
- The conclusion `sum same-layer stress=o(D^2)` does not imply same-layer edge count is small.

## 9. Next target

Combine NSE with the geometric unit-contact structure. In a strict-rhombic region, graph-distance advancing edges belong to train directions separated by angles in `(pi/3,2pi/3)`. A layered network can remain near Euclidean diameter only if the stress-bearing train directions are overwhelmingly aligned with one radial direction.

A useful next theorem is an **angular series stability inequality** that charges any fixed fraction of stress transported in two train directions separated by at least `pi/3` to a fixed loss in the `L>=D` / effective-conductance equality chain.

Such a theorem would force the stressed part of the S1E carrier into one train direction. The residual transverse contacts would then have negligible stress, exactly the regime where PR #126's hinge-rank peeling and Target B's light-transverse-train machinery apply.

## 10. Compact handoff

```text
NSE series extremality in D epsilon->0 phase.
Let z be C66 center and P=N_H(z) its actual diameter partners.
UCM + C66 imply response mass sum_{k in P} c_zk=1-o(1).
Short P to voltage 1, fix z=0, free all other terminals. Effective conductance G_eff=1-o(1).
Let L=d_C(z,P)>=D and A_i be total alpha on graph-layer cut i->i+1.
Unit current and Cauchy on each disjoint layer cut give
    1/G_eff >= sum_i 1/A_i
              >= L^2/sum_i A_i
              >= L^2/D^2
              >=1.
Since 1/G_eff=1+o(1), every inequality is tight:
    L/D->1,
    sum_i A_i/D^2->1,
    same-layer contact stress=o(D^2).
With mu=(sum A_i)/L,
    mu/D->1,
    (1/L)sum (A_i-mu)^2/(mu A_i)->0.
Hence for every fixed eta, all but o(D) layers have A_i=(1+/-eta)D.
Remaining regression: parallel-chain/rhombic ladders with negligible transverse stress.
```
