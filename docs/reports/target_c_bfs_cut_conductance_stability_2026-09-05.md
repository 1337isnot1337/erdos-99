<!-- theorem-state: {"artifact_id":"ART-67DAFF9F3A47","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - Target C BFS cut-conductance and force stability

**Date:** 2026-09-05  
**Run type:** exact electrical/mechanical strengthening  
**Target:** dominant-edge near-geodesic branch  
**Depends on:** C53 PSD domination; C11 virial identity; KKT cut equilibrium; effective-conductance/contact-distance theorem  
**LEVEL I STATUS:** STILL OPEN

## 1. Setup

Work in the fully force-visible C65/C53 branch with positive contact conductances `alpha_e` and normalized diameter weights `beta_h`.

Fix an active diameter edge

`za in H`,

put

`b=beta_za`,

and let

`k=d_C(z,a)`

be the unweighted graph distance in the positive unit-contact graph. Put

`u=(p_a-p_z)/D`.

For every source vertex `v`, let

`d(v)=d_C(z,v)`.

For `0<=i<k`, define the BFS ball

`S_i={v:d(v)<=i}`,

the BFS cut edge set

`E_i={xy in C: {d(x),d(y)}={i,i+1}}`,

and its total contact conductance

`C_i=sum_(e in E_i) alpha_e`.

Because graph distance changes by at most one across a contact edge, `E_i` is exactly the contact cut from `S_i` to its complement. Since `d(a)=k`, each such cut separates `z` from `a`. The edge sets `E_0,...,E_(k-1)` are pairwise disjoint.

Put

`S=sum_(i=0)^(k-1) C_i`.

The virial identity gives

`sum_(e in C) alpha_e=D^2`,

so

`S<=D^2`.                                                   (1.1)

## 2. Effective conductance is bounded by the harmonic cut profile

Let `C_eff(z,a)` be the effective conductance of the positive contact network with edge conductances `alpha_e`, and `R_eff=1/C_eff` its effective resistance.

Take any unit electrical flow from `z` to `a`. Its signed net flow across every BFS cut `E_i` is one. By Cauchy-Schwarz, if the edge currents on `E_i` are `I_e`,

`1=(sum_(e in E_i) I_e)^2`

`<= (sum_(e in E_i) alpha_e)(sum_(e in E_i) I_e^2/alpha_e)`

`=C_i sum_(e in E_i) I_e^2/alpha_e`.

Hence the electrical energy spent on `E_i` is at least `1/C_i`.

The cuts are edge-disjoint, so every unit flow has total energy at least

`sum_(i=0)^(k-1) 1/C_i`.

Minimizing over unit flows gives

`R_eff(z,a)>=sum_i 1/C_i`.

Equivalently,

### Theorem BCS1 - harmonic BFS-cut bound

`C_eff(z,a) <= [sum_i 1/C_i]^(-1)`.                    (2.1)

C53 PSD domination gives the opposite lower bound

`C_eff(z,a)>=b`,

because any scalar potential with values `0,1` at `z,a` has contact Dirichlet energy at least the `za` diameter contribution `b`.

Therefore

`sum_(i=0)^(k-1) 1/C_i <= 1/b`.                       (2.2)

## 3. Recover the distance bound and quantify stress capture

Cauchy-Schwarz gives

`(sum_i C_i)(sum_i 1/C_i)>=k^2`.

Using (2.2),

`S>=b k^2`.                                             (3.1)

Together with `S<=D^2`,

`b<=D^2/k^2`,

which recovers the effective-conductance/contact-distance theorem.

But (3.1) also identifies where the contact stress must live:

### Corollary BCS2 - first-k-layer stress capture

`D^2-S <= D^2-bk^2 <= (1-b)D^2`,                      (3.2)

where the last inequality uses the Euclidean lower bound `k>=D`.

The left side contains all contact stress on

- edges whose endpoints lie in one BFS layer;
- edges between layers `i,i+1` with `i>=k`;
- any other contact edge not belonging to the first `k` successive BFS cuts.

Thus if `b=1-o(1)`, almost the entire normalized contact-stress mass lies on edges that advance exactly one of the first `k` BFS layers from `z` toward the dominant leaf.

## 4. Exact harmonic-flatness identity

Let

`mu=S/k`

be the arithmetic mean of the cut conductances. For each `C_i>0`,

`1/C_i - 1/mu + (C_i-mu)/mu^2`

`=(C_i-mu)^2/(C_i mu^2)`.

Summing over `i`, the linear term vanishes because `sum_i(C_i-mu)=0`. Hence

`sum_i 1/C_i - k^2/S`

`=sum_i (C_i-mu)^2/(C_i mu^2)`.                       (4.1)

Combining (2.2) with (4.1) gives:

### Theorem BCS3 - weighted cut-profile stability

`sum_(i=0)^(k-1) (C_i-mu)^2/(C_i mu^2)`

`<= 1/b-k^2/S`

`<= 1/b-k^2/D^2`.                                     (4.2)

In the dominant-edge regime `b=1-o(1)`, `k=D+o(D)`, the right side tends to zero.

## 5. Exact mechanical force carried by every BFS cut

The electrical estimates above use only PSD domination. KKT equilibrium gives an additional vector statement on each cut.

Orient every contact edge in `E_i` from its endpoint in layer `i` to its endpoint in layer `i+1`, and write its unit displacement vector as

`t_e=p_out-p_in`.

Sum the KKT equilibrium equations over all vertices in the BFS ball `S_i`. Internal contact forces cancel in pairs, as do internal diameter reactions. Multiplying the resulting identity by `-1` gives

`sum_(e in E_i) alpha_e t_e`

`=sum_(xy in H, x in S_i, y notin S_i) beta_xy (p_y-p_x)`.   (5.1)

Because `z in S_i` and `a notin S_i` for every `i<k`, the dominant diameter edge occurs on the right of every one of these cut identities and contributes exactly

`b D u`.

All other crossing diameter edges have total beta weight at most `1-b`, and every diameter vector has norm `D`. Therefore, if

`F_i=sum_(e in E_i) alpha_e t_e`,

then

### Theorem BCS4 - uniform BFS cut-force corridor

`|F_i-bDu| <= (1-b)D`                                  (5.2)

for every `0<=i<k`.

In particular, for `b>1/2`,

`u dot F_i >= (2b-1)D`,                                (5.3)

`|F_i| >= (2b-1)D`,                                    (5.4)

and therefore

`C_i >= (2b-1)D`.                                      (5.5)

This is a uniform statement for every BFS layer, not an average statement.

Summing (5.5) and using `S<=D^2` gives the topology-independent weaker distance estimate

`k <= D/(2b-1)`

for `b>1/2`. The effective-conductance bound `k<=D/sqrt(b)` is stronger near `b=1`, but BCS4 carries vector-direction information that the scalar conductance estimate does not.

## 6. Oriented alignment energy across the whole corridor

For one cut define

`Q_i=sum_(e in E_i) alpha_e |t_e-u|^2`.

Since `|t_e|=|u|=1`,

`Q_i=2(C_i-u dot F_i)`.                                (6.1)

By (5.3),

`Q_i <= 2[C_i-(2b-1)D]`.                              (6.2)

Summing over the `k` cuts,

`sum_i Q_i`

`<=2[S-k(2b-1)D]`

`<=2[D^2-k(2b-1)D]`.

Since `k>=D`,

### Theorem BCS5 - global oriented corridor energy

`sum_(i=0)^(k-1) sum_(e in E_i) alpha_e |t_e-u|^2`

`<=4(1-b)D^2`.                                         (6.3)

This is stronger in orientation content than the projective transverse-energy estimate: an edge pointing approximately `-u` has small projective angle from the diameter line but pays almost the maximum possible cost in (6.3).

For every fixed oriented angle `theta_0>0`, the total stress on first-`k` corridor edges whose oriented angle from `+u` is at least `theta_0` is therefore at most

`(1-b)D^2 / sin^2(theta_0/2)`,                         (6.4)

because `|t_e-u|^2=4 sin^2(theta_e/2)`.

Combining BCS2 and BCS5 gives an exact near-one normal form:

### Corollary BCS6 - layered one-way stress transport

If `b=1-o(1)`, then

1. all but `o(D^2)` contact stress lies on the first `k` BFS transitions;
2. all but `o(D^2)` of that corridor stress points within every fixed oriented cone about `+u`;
3. every BFS cut has a resultant vector `F_i=(1-o(1))D u` uniformly in `i`;
4. the cut-conductance profile is harmonic-flat in the weighted sense (4.2).

Thus the C71-B/C98 survivor is an asymptotically one-way force-transport corridor, not merely a graph containing one near-straight shortest path.

## 7. Interface with the existing global direction-energy theorem

The dominant-edge contact-direction theorem gives

`sum_(e in C) alpha_e sin^2 angle_projective(e,u) <= (1-b)D^2`. (7.1)

BCS5 complements it by choosing the BFS orientation from `z` toward increasing distance. The two statements together distinguish three possible ways to spend non-dominant stress:

- off-corridor edges, controlled by BCS2;
- corridor edges geometrically transverse to the diameter line, controlled by (7.1);
- corridor edges nearly parallel but pointing backward, controlled by BCS5.

All three carry only `o(D^2)` stress when `b->1`.

## 8. What remains

This still does not prove a uniform gap from `b=1`.

A two-dimensional contact-minimal framework can in principle retain many geometrically essential side contacts with positive but arbitrarily small KKT weights. The current theorem controls stress mass, not contact cardinality.

The next viable targets are now narrower:

1. use near-quadrangulation plus cut equilibrium to show that a long one-way corridor necessarily transports a fixed amount of stress into side contacts;
2. prove a finite deformation theorem showing that a framework whose entire positive stress is `o(D^2)` away from one oriented layered corridor cannot be contact-minimal;
3. combine the uniform cut resultants with the C71 single-port cut law to iterate an actual high-stress spine and force the terminal-twist obstruction quantitatively.

No one of these is proved here.

## Handoff

```text
For a diameter edge za of beta weight b, k=d_C(z,a), BFS cuts E_i, cut conductances C_i, and outward unit contact vectors t_e:

  b <= C_eff(z,a) <= 1/sum_i(1/C_i),
  sum_i C_i >= b k^2,
  D^2-sum_i C_i <= (1-b)D^2.

More strongly, cut equilibrium gives for every i<k:

  F_i:=sum_{e in E_i} alpha_e t_e,
  |F_i-bDu| <= (1-b)D,
  C_i >= (2b-1)D.

And globally:

  sum_i sum_{e in E_i} alpha_e |t_e-u|^2
    <= 4(1-b)D^2.

So beta->1 forces almost all contact stress into an oriented, layered, uniformly loaded z-to-a corridor.

Next: force quantitative side-stress leakage from planarity/rhombic geometry, or integrate a deformation from its failure.
```
