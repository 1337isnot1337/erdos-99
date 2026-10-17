> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_adaptive_radial_corridor_2026-09-09.md) · source SHA-256 `15d91e886170907ec945a015072f3bba4fad3a4fc22aa82308aab468425e54a6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4B0C83B8690B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZAC: all but o(D) trunk blocks admit asymptotically radial force corridors

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** quantitative diagonalization of the ZHN corridor theorem  
**Target:** Target C bridge-dominant near-zero phase  
**Depends on:** ZHT, ZHN, ZRP/C68  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZHN proves, for every fixed `rho>0`, that a `(1-rho)` fraction of the macroscopic ZHT trunk blocks have bounded combinatorial size, negligible side load, and a port-to-port contact path on which every contact stress is `Omega_{eta,rho}(D)`. The fixed-`rho` formulation leaves a positive exceptional fraction.

The near-zero hypothesis contains enough scale separation to diagonalize that argument. Put

$$
\delta_D:=D\varepsilon\to0.
$$

Choose the allowed block diameter `K_D` to tend to infinity sufficiently slowly that the maximum number `E_D` of edges in a degree-five graph of diameter `K_D` still satisfies

$$
\delta_D E_D\to0.
$$

Then only `o(D)` trunk blocks exceed `K_D`, only `o(D)` blocks carry nonnegligible side endpoint mass, and every remaining nonsingleton block has a corridor path with edge stresses at least

$$
\gamma_DD,
\qquad
\gamma_D\asymp E_D^{-1},
\qquad
\delta_D/\gamma_D\to0.
$$

C68 can now be applied at the moving scale `gamma_D`: after choosing a radial-defect threshold `zeta_D->0`, only `o(D)` selected corridor edges fail that threshold. Hence all but `o(D)` trunk blocks are either singleton blocks or admit a port-to-port contact path every one of whose edges is simultaneously mechanically significant relative to the defect and has radial progress `1-o(1)`.

This removes the fixed positive exceptional fraction from ZHN.

---

## 1. ZHT trunk and defect scale

Fix `eta>0`. Assume along an unbounded sequence

$$
S_{br}\ge\eta D^2,
\qquad
\delta_D:=D\varepsilon\to0.
\tag{1.1}
$$

ZHT supplies one harmonic cell with a consecutive bridge trunk

$$
f_1,\ldots,f_H,
\qquad
H\ge c_HD,
\qquad
c_H:=\frac{\eta^2}{16\pi},
\tag{1.2}
$$

and

$$
\alpha_{f_j}\ge c_BD,
\qquad
c_B:=\frac{\eta}{32\pi}.
\tag{1.3}
$$

Let `X_0,...,X_H` be the successive bridge blocks. C39 gives

$$
\boxed{
\sum_X\delta_X\le2\pi D.
}
\tag{1.4}
$$

ZHN assigns endpoint mass `mu_i` to trunk layers with

$$
\boxed{
\sum_{i=0}^H\mu_i=2,
}
\tag{1.5}
$$

and proves the side-force estimate

$$
F_{side}(X_i)\le2D\mu_i.
\tag{1.6}
$$

C68 gives, at the C66 center `z`,

$$
\boxed{
Q_z
:=\sum_{uv\in C}\alpha_{uv}[1-(r_u-r_v)^2]
\le C_0D^3\varepsilon
=C_0D^2\delta_D.
}
\tag{1.7}
$$

---

## 2. Choose a moving combinatorial scale

Every triangle-free unit-contact graph has maximum degree at most five. A connected graph of maximum degree five and graph diameter at most `K` has at most

$$
M(K):=1+5\sum_{j=0}^{K-1}4^j
\tag{2.1}
$$

vertices and at most

$$
E(K):=\frac52M(K)
\tag{2.2}
$$

edges.

Because `delta_D->0`, define for sufficiently large `D`

$$
K_D
:=
\max\left\{1,
\left\lfloor\frac18\log_4\frac1{\delta_D}\right\rfloor
\right\}.
\tag{2.3}
$$

Then

$$
K_D\to\infty.
\tag{2.4}
$$

Put

$$
M_D:=M(K_D),
\qquad
E_D:=E(K_D).
\tag{2.5}
$$

There is an absolute constant `C_E` with

$$
E_D\le C_E4^{K_D}
\le C_E\delta_D^{-1/8}.
\tag{2.6}
$$

Therefore

$$
\boxed{
\delta_DE_D\to0.
}
\tag{ZAC1}
$$

The exponent `1/8` is arbitrary; any fixed exponent strictly between zero and one gives the required diagonalization.

---

## 3. Only o(D) trunk blocks are combinatorially large or side-loaded

By (1.4), the number of trunk blocks satisfying

$$
\delta_{X_i}>K_D
$$

is at most

$$
\frac{2\pi D}{K_D}=o(D).
\tag{3.1}
$$

For side load choose

$$
\lambda_D:=D^{-1/2}.
\tag{3.2}
$$

By (1.5), the number of trunk layers satisfying

$$
\mu_i>\lambda_D
$$

is at most

$$
2D^{1/2}=o(D).
\tag{3.3}
$$

Call an internal trunk block **adaptive-regular** when

$$
\delta_{X_i}\le K_D,
\qquad
\mu_i\le D^{-1/2}.
\tag{3.4}
$$

Then

$$
\boxed{
\#\{\text{internal trunk blocks not adaptive-regular}\}=o(D).
}
\tag{ZAC2}

Every adaptive-regular block has at most `M_D` vertices and `E_D` internal contact edges, and by (1.6)

\[
F_{side}(X_i)\le2\sqrt D=o(D).
\tag{3.5}
$$

---

## 4. Moving-scale macroscopic corridor in every adaptive-regular block

Fix a nonsingleton adaptive-regular block `X_i` with parent and child trunk ports `p^-`,`p^+`.

Exactly as in ZHN, sum mechanical equilibrium over any vertex shore separating the two ports. The parent trunk force has magnitude at least `c_BD`, while all nontrunk external forces have total magnitude at most `2sqrt(D)`. Hence for all sufficiently large `D`, every separating internal contact cut has scalar alpha-capacity at least

$$
\frac{c_B}{2}D.
\tag{4.1}
$$

Max-flow/min-cut produces a port-to-port scalar flow of that value. Delete cycles and decompose it into simple paths. Since the block has at most `E_D` internal contact edges, one simple path `P_i` carries at least

$$
\frac{c_B}{2E_D}D.
$$

Every contact on that path therefore satisfies

$$
\boxed{
\alpha_e\ge\gamma_DD,
\qquad
\gamma_D:=\frac{c_B}{2E_D}.
}
\tag{ZAC3}

By ZAC1,

\[
\boxed{
\frac{\delta_D}{\gamma_D}
=\frac{2E_D}{c_B}\delta_D
\to0.
}
\tag{ZAC4}

Thus the selected path stress may decay relative to `D`, but it decays much more slowly than the normalized response-defect scale `delta_D`.

Singleton adaptive-regular blocks require no internal path and are declared automatically corridor-good.

---

## 5. C68 radializes the moving-scale corridors

Define

\[
\zeta_D
:=
\sqrt{\frac{\delta_D}{\gamma_D}}.
\tag{5.1}
$$

By ZAC4,

$$
\boxed{\zeta_D\to0.}
\tag{5.2}
$$

Call a selected corridor edge **radially bad** if

$$
1-(r_u-r_v)^2>\zeta_D.
\tag{5.3}
$$

Every radially bad selected edge has stress at least `gamma_DD`, so it contributes more than

$$
\gamma_DD\zeta_D
$$

to `Q_z`. Therefore (1.7) gives

$$
N_{bad}\,\gamma_DD\zeta_D
\le C_0D^2\delta_D,
$$

hence

$$
N_{bad}
\le
C_0D\frac{\delta_D}{\gamma_D\zeta_D}
=
C_0D\sqrt{\frac{\delta_D}{\gamma_D}}
=C_0D\zeta_D
=o(D).
\tag{5.4}
$$

Thus only `o(D)` selected corridor edges are radially bad.

A nonsingleton adaptive-regular block whose selected path contains a radially bad edge accounts for at least one such edge. Therefore:

### Theorem ZAC.1 — adaptive radial corridor theorem

All but `o(D)` internal ZHT trunk blocks are either singleton blocks or admit a port-to-port contact path `P_i` such that every edge `uv in P_i` satisfies simultaneously

$$
\boxed{
\alpha_{uv}\ge\gamma_DD,
}
\tag{ZAC5}
$$

and

$$
\boxed{
|r_u-r_v|
\ge
\sqrt{1-\zeta_D}
=1-o(1).
}
\tag{ZAC6}

where

\[
\gamma_D>0,
\qquad
\frac{\delta_D}{\gamma_D}\to0,
\qquad
\zeta_D\to0.
$$

This replaces ZHN's fixed `(1-rho)` regular fraction by an `1-o(1)` fraction, at the cost of allowing the finite block-size and stress constants to vary slowly with `D`.

---

## 6. Almost every selected corridor belongs to the strong radial path forest

Let

$$
c_*:=\cos(\pi/12)<1
$$

be the ZRP strongly-radial threshold. Since the right side of ZAC6 tends to one, for all sufficiently large `D`, every edge in every ZAC-good selected path satisfies

$$
|r_u-r_v|>c_*.
\tag{6.1}
$$

Hence all selected edges in all but `o(D)` trunk blocks lie in the ZRP strongly-radial graph `C_rad`.

ZRP proves `C_rad` is a path forest and every vertex other than `z` has degree at most two in it. Therefore each selected corridor `P_i` is not merely an arbitrary max-flow path: in the complete source it lies on one simple strongly-radial path component.

ZHT/ZRP also show that all but `o(D)` trunk bridge edges themselves are strongly radial. Consequently, after discarding `o(D)` trunk positions, the parent bridge, selected internal corridor, and child bridge at each remaining internal block all lie in one path component of `C_rad`.

At every internal vertex of such a path component away from `z`, ZRP's one-inward/one-outward rule forces one adjacent strongly-radial edge to decrease radius and the other to increase radius. Thus each connected good trunk segment is strictly monotone in radius.

### Corollary ZAC.2 — asymptotically radial route segmentation

After deleting `o(D)` trunk blocks/bridge positions, the remaining `H-o(D)=Omega_eta(D)` trunk positions decompose into simple contact-path segments for which

- every selected contact has radial progress `1-o(1)`;
- every selected contact stress is at least `gamma_DD`, with `delta_D/gamma_D->0`;
- radius is strictly monotone along each segment;
- the segment belongs to the global strongly-radial path forest.

The number and total internal diameter of the deleted blocks are not controlled strongly enough to concatenate these segments into one globally narrow contact path. That is the surviving obstruction.

---

## 7. What this advances and what remains

ZHN left a fixed positive fraction of potentially uncontrolled route blocks for each fixed finite-complexity scale. ZAC removes that fraction completely: the uncontrolled **number** of trunk blocks is `o(D)`.

It also removes the fixed-threshold radial error on the selected corridors: their radial defect tends to zero at a scale chosen directly from `D epsilon`.

The remaining loophole is now concentrated in `o(D)` exceptional bridge blocks. The global C39 budget permits those few blocks to carry `Theta(D)` total internal graph diameter, so they can still account for a macroscopic geometric detour. Pure counting cannot rule this out.

A sufficient next lemma is therefore sharply localized:

> **Exceptional-block detour lemma.** In the ZHT/ZAC phase, the `o(D)` exceptional trunk blocks cannot carry `Theta(D)` total geometric/contact-path detour while joining the radial corridor segments in a globally diameter-minimal triangle-free source.

Any proof that their total route detour is `o(D)` would produce an almost-geodesic radial contact path from the ZHT endpoint data. The sharp Theorem P/C98 machinery could then become applicable after a final angular conversion.

---

## 8. Regression checks

### One giant exceptional block

Still allowed. It can consume a positive fraction of the entire `sum delta_X=O(D)` budget while the other `Omega(D)` trunk blocks satisfy ZAC. This is exactly the remaining obstruction.

### Slowly growing regular block size

Allowed and essential. `K_D` grows to infinity, so ZAC does not falsely assert a fixed finite list of block types captures all but `o(D)` positions.

### Vanishing corridor stress coefficient

Allowed. `gamma_D` may tend to zero. The only required quantitative relation is `delta_D/gamma_D->0`, which is what lets C68 radialize the moving-scale selected paths.

### Weak transverse braces

Still allowed, but outside the selected radial corridors. They may preserve redundant rigidity with total normalized stress tending to zero.

---

## 9. Classification

**Status:** proved report-level quantitative refinement of ZHN.  
**Level I:** still open.  
**Computation:** none.  
**External literature:** none.  
**Dependencies:** ZHT, ZHN cut-capacity argument, C39, C68, ZRP.
