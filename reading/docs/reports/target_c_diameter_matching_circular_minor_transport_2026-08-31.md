> Generated reading edition · [exact source](../../../docs/reports/target_c_diameter_matching_circular_minor_transport_2026-08-31.md) · source SHA-256 `ecdd3bcba6319b8aa6c21be9a694c3f5285bf6e7abd53d75285768f6d0e36607`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-80F437152804","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: diameter-matching circular-minor transport

**Date:** 2026-08-31  
**Repository base:** `8d953efb` (main after C65 / PR #68)  
**Run type:** exact circular-minor / response-defect theorem  
**Target:** Target C Gate C-II  
**Depends on:** C41 response energy identity, C43 uniform anti-Reuleaux gap, C53/C64 PSD response defect, C65 full diameter visibility  
**Literature input:** circular-minor positivity for circular-planar response matrices; Hopf–Pannwitz planar diameter-edge bound

## LEVEL I STATUS

**STILL OPEN.**

C65 makes the selected diameter graph equal to the actual source diameter graph. This allows the geometric crossing property of diameter edges to be combined directly with circular total positivity of the contact-network response.

The result is a quantitative transport theorem. If `J` is any matching of pairwise vertex-disjoint diameter edges and `c_e` is the response conductance on the same terminal pair, then the C41 defect

```math
\varepsilon:=\sum_{b<k}c_{bk}-1
=\frac12\operatorname{tr}(\Lambda-L_H)
```

satisfies

```math
\boxed{
\varepsilon
\ge
2\gamma_0\sum_{\{e,f\}\subset J}\sqrt{c_ec_f},
}
```

where `gamma_0>0` is the uniform C43 squared-distance deficit.

The PSD defect also gives

```math
\boxed{
\sum_{e\in J}|c_e-\beta_e|\le\varepsilon.
}
```

Consequently a near-zero response defect cannot coexist with two disjoint diameter edges carrying non-negligible KKT weight. More globally, every sufficiently heavy diameter edge belongs to one common star. Using the classical planar diameter bound `|H|<=|V(H)|<=pi D`, one gets the explicit concentration statement

```math
\boxed{
\sum_{e\ni z}\beta_e
\ge
1-C_0D\varepsilon
}
```

for some diameter vertex `z`, whenever the right side is positive. Thus the only possible `o(1/D)` C-II response-defect phase is an **asymptotically stress-star diameter graph**.

This is stronger than the abstract near-star regression: the near-star shape is now forced in the *mechanical diameter stress itself*, not merely allowed by the electrical response cone.

## 1. Setup and defect normalization

Work in the C65 lexicographically normalized C-II source. Thus

```math
C=C_*,\qquad H=H_*.
```

Choose a relative-interior normalized KKT stress. Write

```math
\sum_{h\in H}\beta_h=1,
```

and let

```math
c_{bk}:=-\Lambda_{bk}\ge0
\qquad(b\ne k)
```

be the circular-planar response conductances on the complete diameter-endpoint boundary `B=V(H)`.

Put

```math
M:=\Lambda-L_H\succeq0
```

by C64, and

```math
\varepsilon:=\sum_{b<k}c_{bk}-1.
\tag{C66.1}
```

Since `tr Lambda=2 sum c` and `tr L_H=2`,

```math
\boxed{\operatorname{tr}M=2\varepsilon.}
\tag{C66.2}
```

C41's affine energy identity is equivalently

```math
\boxed{
\varepsilon
=
\sum_{b<k}c_{bk}
\left(1-\frac{|p_b-p_k|^2}{D^2}\right).
}
\tag{C66.3}
```

Thus `epsilon` is exactly the response conductance weighted by normalized squared-distance deficit.

Let

```math
\rho_0=1-\eta_0,
\qquad
\gamma_0=1-\rho_0^2>0
\tag{C66.4}
```

be the C43 constants. Call a terminal pair **short** if its distance is at most `rho_0D`.

## 2. Four-terminal circular inequalities

Let four distinct boundary terminals occur cyclically as

```math
a,b,c,d.
```

Circular-planar response matrices have nonnegative circular minors. Apply this to the circular pair with rows `(a,b)` and reversed columns `(d,c)`. Since the minor size is two,

```math
\det
\begin{pmatrix}
\Lambda_{ad}&\Lambda_{ac}\\
\Lambda_{bd}&\Lambda_{bc}
\end{pmatrix}
\ge0.
```

Using `Lambda_ij=-c_ij` off diagonal gives

```math
\boxed{c_{ad}c_{bc}\ge c_{ac}c_{bd}.}
\tag{C66.5}
```

Rotating the cyclic order by one vertex and using rows `(b,c)` with reversed columns `(a,d)` gives

```math
\boxed{c_{ab}c_{cd}\ge c_{ac}c_{bd}.}
\tag{C66.6}
```

Therefore the response product on two crossing terminal chords is bounded above by the response product on **either** noncrossing side pairing.

These are standard size-two circular-minor inequalities; no Kalmanson approximation or equality classification is used.

## 3. Two disjoint diameter edges force a short side pairing

Let

```math
ac,bd\in H
```

be vertex-disjoint diameter edges. Any two vertex-disjoint diameter segments in the plane cross, so their four endpoints occur cyclically as

```math
a,b,c,d
```

and

```math
|a-c|=|b-d|=D.
```

Apply C43 to the four triples

```math
abc,\quad bcd,\quad cda,\quad dab.
```

Because each triple contains one diameter diagonal, C43 says respectively

```math
\begin{aligned}
&ab\text{ short or }bc\text{ short},\\
&bc\text{ short or }cd\text{ short},\\
&cd\text{ short or }da\text{ short},\\
&da\text{ short or }ab\text{ short}.
\end{aligned}
\tag{C66.7}
```

These are exactly the vertex-cover conditions on a four-cycle. They imply that one of its two opposite edge pairs is entirely short:

```math
\boxed{
(ab,cd)\text{ are both short}
\quad\text{or}\quad
(ad,bc)\text{ are both short}.}
\tag{C66.8}
```

Choose such a short pairing and call its two edges `s(ac,bd)` and `t(ac,bd)`.

By C66.5-C66.6,

```math
c_s c_t\ge c_{ac}c_{bd},
```

so AM-GM gives

```math
\boxed{
c_s+c_t\ge2\sqrt{c_{ac}c_{bd}}.}
\tag{C66.9}
```

Thus two crossing diameter-response edges force a definite amount of response conductance onto uniformly subdiametral terminal pairs.

## 4. Matching pairs do not double-count their forced side edges

Let

```math
J=\{e_1,\ldots,e_m\}\subset H
```

be a matching. For each unordered pair `{e_i,e_j}`, choose the two short side edges supplied by C66.8.

Every selected side edge has one endpoint on `e_i` and one endpoint on `e_j`. Since the diameter edges in `J` are vertex-disjoint, that side edge uniquely determines the unordered pair `{e_i,e_j}`. Hence selected side edges from distinct matching-edge pairs are distinct.

C66.3 and shortness then give

```math
\varepsilon
\ge
\gamma_0
\sum_{i<j}
(c_{s(i,j)}+c_{t(i,j)}).
```

Use C66.9 termwise.

### Theorem C66.1 — diameter-matching response transport

For every matching `J` in the full diameter graph,

```math
\boxed{
\varepsilon
\ge
2\gamma_0
\sum_{\{e,f\}\subset J}\sqrt{c_ec_f}.
}
\tag{C66.10}
```

Equivalently,

```math
\boxed{
\varepsilon
\ge
\gamma_0
\left[
\left(\sum_{e\in J}\sqrt{c_e}\right)^2
-
\sum_{e\in J}c_e
\right].
}
\tag{C66.11}
```

This is an aggregate inequality: the forced short response edges from the `binom(m,2)` diameter-edge pairs are disjoint in response-support accounting.

## 5. PSD converts response conductance back to KKT diameter weight

For a diameter edge `e=uv`,

```math
M_{uv}=\beta_e-c_e.
```

Write

```math
\Delta_u:=M_{uu}\ge0.
```

PSD of the `2x2` principal minor gives

```math
|c_e-\beta_e|
\le
\sqrt{\Delta_u\Delta_v}.
\tag{C66.12}
```

If `J` is a matching, its endpoints are disjoint. Therefore

```math
\begin{aligned}
\sum_{e=uv\in J}|c_e-\beta_e|
&\le
\sum_{e=uv\in J}\sqrt{\Delta_u\Delta_v}\\
&\le
\frac12\sum_{u\in V(J)}\Delta_u\\
&\le
\frac12\operatorname{tr}M
=\varepsilon.
\end{aligned}
```

### Theorem C66.2 — matching weight transfer

For every diameter matching `J`,

```math
\boxed{
\sum_{e\in J}|c_e-\beta_e|\le\varepsilon.
}
\tag{C66.13}
```

In particular

```math
\boxed{
\sum_{e\in J}c_e
\ge
\sum_{e\in J}\beta_e-\varepsilon.
}
\tag{C66.14}
```

The matching hypothesis is essential only for the final disjoint-diagonal sum in C66.13.

## 6. Heavy disjoint diameter edges force a quantitative defect

Take two disjoint diameter edges `e,f` and suppose

```math
\beta_e,\beta_f\ge\tau.
```

Applying C66.12 individually and using `Delta_u+Delta_v<=tr M=2epsilon` gives the weaker bound `|c_e-beta_e|<=epsilon`; it also follows directly from C66.13 for the two-edge matching. Thus

```math
c_e,c_f\ge\tau-\varepsilon.
```

If `epsilon<tau`, C66.10 with the two-edge matching gives

```math
\varepsilon
\ge
2\gamma_0\sqrt{c_ec_f}
\ge
2\gamma_0(\tau-\varepsilon).
```

Hence

```math
\boxed{
\varepsilon
\ge
\kappa_0\tau,
\qquad
\kappa_0:=\frac{2\gamma_0}{1+2\gamma_0}.
}
\tag{C66.15}
```

So whenever

```math
\varepsilon<\kappa_0\tau,
\tag{C66.16}
```

there cannot be two vertex-disjoint diameter edges of KKT weight at least `tau`.

## 7. Heavy diameter edges form one star

For sufficiently large `n`, C43 excludes a diameter triangle. Therefore any pairwise-intersecting family of diameter edges has a common endpoint: an intersecting family of 2-subsets with no common endpoint would contain exactly the three edges of a triangle.

Define the heavy diameter set

```math
H_{\ge\tau}:=\{e\in H:\beta_e\ge\tau\}.
```

Under C66.16 every two heavy edges intersect, hence:

### Corollary C66.3 — heavy-star concentration

If `epsilon<kappa_0 tau`, then there is one diameter vertex `z` such that

```math
\boxed{H_{\ge\tau}\subseteq\{e:e\ni z\}.}
\tag{C66.17}
```

This is already a topology reduction driven by the numerical response defect.

## 8. Use the planar diameter-edge bound

The classical Hopf–Pannwitz theorem gives, for a planar point set with `q` diameter endpoints,

```math
|H|\le q.
\tag{C66.18}
```

Here every diameter endpoint lies in convex position. Consecutive hull vertices are unit-separated, so

```math
q\le\operatorname{per}(\operatorname{conv}B).
```

Every convex planar body of diameter `D` has perimeter at most `pi D`, hence

```math
\boxed{|H|\le q\le\pi D.}
\tag{C66.19}
```

Set

```math
\tau=\frac{2\varepsilon}{\kappa_0}.
\tag{C66.20}
```

Then `epsilon<kappa_0 tau` whenever `epsilon>0`, so all edges of weight at least `tau` share one endpoint `z`. The total weight of all lighter edges is at most

```math
|H|\tau
\le
\frac{2\pi}{\kappa_0}D\varepsilon.
```

Because the full diameter weight is normalized to one:

### Theorem C66.4 — near-zero defect forces a mechanical stress star

There exists a diameter vertex `z` such that

```math
\boxed{
\sum_{\substack{e\in H\\e\ni z}}\beta_e
\ge
1-rac{2\pi}{\kappa_0}D\varepsilon.
}
\tag{C66.21}
```

In particular, along any hypothetical C-II sequence with

```math
D\varepsilon\longrightarrow0,
```

the normalized KKT diameter stress concentrates asymptotically on one star:

```math
\max_z\sum_{e\ni z}\beta_e\longrightarrow1.
\tag{C66.22}
```

This conclusion concerns the **actual full diameter graph and its mechanical KKT weights**, not an abstract electrical approximation.

## 9. Relation to the near-star regression

The cycle-with-leaves regression shows that bounded-degree circular-planar networks can approach an additive star response with arbitrarily small circular minors. C66 does not contradict that network theorem.

Instead it proves that, in an actual Target C source, a defect small compared with `1/D` forces the diameter stress itself to become star-supported. Therefore a closing stability theorem no longer has to treat arbitrary mechanical diameter loads:

```text
epsilon = o(1/D)
    -> one diameter vertex carries 1-o(1) of all beta mass.
```

The remaining near-star problem is now explicitly mechanical:

> can a force-visible triangle-free unit-contact equilibrium of scale `D`, terminal degree at most three, and `Theta(D)` actual diameter endpoints carry `1-o(1)` of its normalized diameter stress through one diameter star while its response defect is `o(1/D)`?

The abstract electrical regression does not answer this because it does not satisfy the unit-edge equilibrium equations or the fixed total contact-stress tensor.

## 10. Diameter-graph structure input

A classical stronger characterization is also available: every connected component of a planar diameter graph is a caterpillar, with its spine possibly closed into one odd cycle. This follows from the straight-line thrackle property that every two diameter edges intersect.

C66 does not require that full characterization; only the edge bound `|H|<=q` and triangle exclusion are used. The characterization is useful for the next star-versus-matching decomposition.

## 11. Regressions and scope

- **One star:** C66.10 is vacuous on the star edges because there is no two-edge matching. This is exactly the surviving phase.
- **Odd diameter cycle:** it has a matching of linear size, so C66.10 forces substantial short response unless almost all corresponding KKT weight collapses onto one or two adjacent edges.
- **Tiny positive diameter weights:** allowed. C66.21 counts them only through the `O(D)` edge bound.
- **Near-star electrical network:** allowed abstractly; C66 says such a response can have `o(1/D)` defect in Target C only if the mechanical `beta` weights themselves are star-concentrated.
- **C-I:** no longer relevant; Gate C-I is closed.

## 12. Literature notes

The circular-minor nonnegativity used in C66.5-C66.6 is the standard connection theorem for circular-planar electrical networks, already imported elsewhere in the repository through S. Forcey's treatment of Kalmanson–Kron reconstruction.

The planar diameter bound and caterpillar/odd-cycle characterization go back to Hopf–Pannwitz and Sutherland; a modern summary is K. Swanepoel, *The number of diameters* (2007), which records `|H|<=q` and the component characterization.

## 13. Compact handoff

**LEVEL I STATUS:** still open.

**C66.1:** every diameter matching transports pairwise products of response conductance onto disjoint uniformly short side pairs:

`epsilon >= 2 gamma_0 sum_(e<f in J) sqrt(c_e c_f)`.

**C66.2:** PSD gives `sum_(e in J)|c_e-beta_e|<=epsilon`.

**C66.3:** if `epsilon<kappa_0 tau`, all diameter edges with `beta_e>=tau` share one endpoint.

**C66.4:** using `|H|<=|B|<=pi D`, one vertex carries at least

`1-(2pi/kappa_0)D epsilon`

of the full normalized diameter stress.

**Next:** exclude the mechanical stress-star phase, or prove an `Omega(1/D)` defect lower bound there. The non-star near-zero phase is now eliminated.
