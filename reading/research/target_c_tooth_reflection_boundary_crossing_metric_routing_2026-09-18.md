> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_boundary_crossing_metric_routing_2026-09-18.md) · source SHA-256 `de390b467af9c1163d0085191eb93eb3c86474a461bb80171bcc463e2b489b0b`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9b39a6817e4cad86cabec717cc805a618f1fb29b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_boundary_crossing_metric_routing_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f7b55caeabae028b3ec3fa01afdb68cc7d59b01a9bd2cacba81b326c81192ff3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II - FREE boundary crossings force metric loaded-hull payment

**Date:** 2026-09-18  
**Status:** proved candidate awaiting audit; proof-only strengthening of the all-inactive FREE branch  
**Scope:** every non-anchored all-inactive FREE reflection module in the Type-II full-core branch  
**Dependencies:** monotone FREE parent corridor; FREE total-slack telescope; two-sided outer-face localization; Section-63 loaded-hull outer routes; planar sub-`sqrt(2)` source-pair lemma; Oler convex-container bound  
**Certificate:** `research/verify_target_c_free_boundary_crossing_metric_routing_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding monotone-corridor theorem forces a linear payment in `x_B=b-q` and the exterior isolate population `Z_ext`, but it does not distinguish metric force-hull surplus from repeated outer-route surplus. This note makes that split.

Put

```math
H_D:=\operatorname{per}(F)-q\ge0,
\qquad
\lambda_D:=b-\operatorname{per}(F)\ge0,
```

so that

```math
x_B=H_D+\lambda_D=m+u_B.
\tag{BC.0}
```

For the original FREE parent ancestry `C=(z_0,...,z_ell)`, write

```math
S_D=a_{z_\ell}-a_{z_0}
```

for its support-depth span. The existing corridor results give

```math
S_D\ge {D\over2}-3^{1/8}D^{3/4}-\omega_D\sqrt D-O(\sqrt D),
\tag{BC.1}
```

for every `omega_D -> infinity` with `omega_D=o(D^(1/4))`, and

```math
\sum_j\sigma_j\le t_D,
\qquad
\sigma_j:=|z_{j+1}-z_j|-1>0,
\qquad
t_D<h_*+D^{-1/3},
\tag{BC.2}
```

where

```math
h_*={\sqrt{303}\over52}=0.334747984337100\ldots .
```

For all sufficiently large `D`, `1+t_D<sqrt(2)`.

The main consequence is:

```math
\boxed{
H_D=o(D)
\quad\Longrightarrow\quad
u_B+Z_{\rm ext}\ge {D\over2}-o(D),
}
\tag{BC.3}
```

and hence, because `u_B<=H_D+lambda_D`,

```math
\boxed{
H_D=o(D)
\quad\Longrightarrow\quad
\lambda_D+Z_{\rm ext}\ge {D\over2}-o(D).
}
\tag{BC.4}
```

Since `H_D<=pi D-q`, this gives the terminal metric frontier

```math
\boxed{
\pi D-q=o(D)
\quad\Longrightarrow\quad
(b-\operatorname{per}F)+Z_{\rm ext}
\ge {D\over2}-o(D).
}
\tag{BC.5}
```

In particular,

```math
\boxed{
\pi D-q=o(D),
\qquad
b-\operatorname{per}F=o(D)
\quad\Longrightarrow\quad
Z_{\rm ext}\ge {D\over2}-o(D).
}
\tag{BC.6}
```

The previous monotone-corridor recipient law gave only `lambda_D+3 Z_ext >= D/2-o(D)` after imposing `pi D-q=o(D)`. Equation (BC.5) removes the factor three on the exterior population.

## 1. Crossing diagonals in a unit-separated source

### Lemma BC.1

Let `A,B,C,D` be four unit-separated source points in convex position, and suppose the diagonals `AC` and `BD` cross properly. Put

```math
p=|AC|,
\qquad q=|BD|.
```

Then

```math
\boxed{p^2+q^2\ge4.}
\tag{BC.7}
```

The constant is sharp; every unit rhombus has equality.

### Proof

Let `O=AC cap BD` and write

```math
AO=a,
\quad CO=c,
\quad BO=b,
\quad DO=d,
```

with all four numbers positive. Let `x` be the cosine of the angle from `OA` to `OB`. Unit separation on the four sides of the quadrilateral gives

```math
a^2+b^2-2abx\ge1,
```
```math
c^2+b^2+2cbx\ge1,
```
```math
c^2+d^2-2cdx\ge1,
```
```math
a^2+d^2+2adx\ge1.
\tag{BC.8}
```

Multiply these inequalities respectively by `cd, ad, ab, bc` and add. The cosine terms cancel. The left side factors as

```math
(a+c)(b+d)(ac+bd),
```

while the right side is `(a+c)(b+d)`. Hence

```math
ac+bd\ge1.
\tag{BC.9}
```

Because `p=a+c` and `q=b+d`, AM-GM yields

```math
p^2+q^2\ge4ac+4bd\ge4.
```

This proves the lemma.

## 2. Every entered OP pocket has a long hull base

Take a maximal block of parent-chain vertices lying in `F`. The root `z_0` is outside `F`, so the block has an entering parent edge. Two-sided outer-face localization places the block in one OP outer pocket. Let that pocket have loaded force-hull base `b_i b_{i+1}` of length

```math
s_i=|b_i-b_{i+1}|.
```

Let the entering parent edge have length

```math
p_i=1+\sigma_i<\sqrt2.
```

If its first inside endpoint lies in the relative interior of the hull side, unit separation from the two hull endpoints gives `s_i>=2`. Otherwise the entering edge crosses the relative interior of the base properly. It cannot pass through a loaded hull vertex: a parent edge has length below two, whereas a third source point in its relative interior would split it into two subsegments each of length at least one. Lemma BC.1 therefore gives, in all cases,

```math
\boxed{
s_i\ge f(\sigma_i):=
\sqrt{4-(1+\sigma_i)^2}.
}
\tag{BC.10}
```

Thus every entered pocket has `s_i>sqrt(2)>1`; it is based on a genuinely nonunit hull side.

Let `v_C` be the number of distinct OP pockets entered by the maximal chain-vertex blocks lying in `F`, including singleton inside blocks. If a singleton lies on `partial F`, assign it to the unique nonunit hull side whose relative interior contains it. Choose one entering parent edge for each distinct pocket. These chosen edges are distinct, so

```math
\sum_{i=1}^{v_C}\sigma_i\le t_D.
\tag{BC.11}
```

The function

```math
f(\sigma)=\sqrt{4-(1+\sigma)^2}
```

has

```math
f''(\sigma)=-{4\over f(\sigma)^3}<0.
```

Hence it lies above its secant on `[0,t_D]`. Define

```math
\Delta_D
:=\sqrt3-\sqrt{4-(1+t_D)^2}.
\tag{BC.12}
```

Then

```math
f(\sigma_i)
\ge
\sqrt3-{
\Delta_D\over t_D}\sigma_i.
```

Summing and using (BC.11),

```math
\sum_{i=1}^{v_C}(s_i-1)
\ge
v_C(\sqrt3-1)-\Delta_D.
\tag{BC.13}
```

Every hull side has length at least one, so

```math
H_D=\sum_{j=1}^q(s_j-1)
```

dominates the selected sum. Therefore

```math
\boxed{
v_C
\le
{H_D+\Delta_D\over\sqrt3-1}.
}
\tag{BC.14}
```

Moreover

```math
\Delta_D\to
\Delta_*
:=\sqrt3-\sqrt{4-(1+h_*)^2}
=0.242605334143264\ldots .
\tag{BC.15}
```

Thus `H_D=o(D)` implies `v_C=o(D)`.

## 3. Internal support gain is at most `u_B+2v_C`

For a nonunit loaded hull side `i`, let `ell_i` be its canonical Section-63 outer-route occurrence length. If `P_i` is its OP pocket, then the standard pocket-width estimate gives

```math
w_N(P_i)
\le {\operatorname{per}(P_i)\over2}
\le\ell_i.
\tag{BC.16}
```

The complete parent chain is strictly support-monotone. Therefore all projection intervals contributed by internal parent edges in a fixed pocket have disjoint interiors, including after a leave-and-revisit. If

```math
G_{\rm in}
:=\sum_{z_j,z_{j+1}\in F}
N\cdot(z_j-z_{j+1}),
```

then

```math
G_{\rm in}\le\sum_{i\in V_C}\ell_i,
\tag{BC.17}
```

where `V_C` is the set of entered pockets. Pockets containing no internal parent edge contribute zero on the left and only weaken this upper bound.

Section 63 gives

```math
x_B=\sum_i(\ell_i-1),
\qquad
u_B=x_B-m.
```

Splitting by nonunit and unit hull sides gives the exact algebraic identity

```math
\boxed{
u_B
=
\sum_{i:s_i>1}(\ell_i-2)
+
\sum_{i:s_i=1}(\ell_i-1).
}
\tag{BC.18}
```

All terms are nonnegative. Every entered pocket has `s_i>1`, so

```math
\boxed{
G_{\rm in}\le u_B+2v_C.
}
\tag{BC.19}
```

Using (BC.14),

```math
G_{\rm in}
\le
u_B+{2(H_D+\Delta_D)\over\sqrt3-1}.
\tag{BC.20}
```

## 4. Hull-side surplus also bounds the number of inside blocks

Let `r_C` be the number of maximal nonempty blocks of chain vertices lying in `F`. The previous corridor theorem used only `r_C<=Z_ext`. We can do better when `H_D` is small.

For every inside block, assign its first vertex to the OP pocket entered by the block. For an entered base side of length `s`, every assigned first vertex lies in the inward half-stadium obtained by taking the Euclidean `rho_D`-neighborhood of the base segment and intersecting it with the inward supporting half-plane, where

```math
\rho_D:=1+t_D<\sqrt2.
```

This half-stadium is convex and has

```math
\operatorname{area}
=\rho_Ds+{\pi\rho_D^2\over2},
\qquad
\operatorname{per}
=2s+\pi\rho_D.
\tag{BC.21}
```

The assigned first-entry vertices are original source points and are unit-separated. Oler's convex-container bound therefore gives, for the group assigned to one base,

```math
N_s\le A_Ds+B_D,
\tag{BC.22}
```

where

```math
A_D:=1+{2\rho_D\over\sqrt3},
\qquad
B_D:=1+{\pi\rho_D\over2}
+{\pi\rho_D^2\over\sqrt3}.
\tag{BC.23}
```

The assigned groups are disjoint even if their containers overlap. If `L_V` is the sum of the distinct entered-base lengths, then

```math
r_C\le A_DL_V+B_Dv_C.
\tag{BC.24}
```

Since

```math
L_V
=v_C+
\sum_{i\in V_C}(s_i-1)
\le v_C+H_D,
```

we obtain

```math
\boxed{
r_C
\le
R_{H,D}H_D+R_{\Delta,D}\Delta_D,
}
\tag{BC.25}
```

with

```math
R_{H,D}
:=A_D+{A_D+B_D\over\sqrt3-1},
\qquad
R_{\Delta,D}
:={A_D+B_D\over\sqrt3-1}.
\tag{BC.26}
```

Consequently

```math
H_D=o(D)
\quad\Longrightarrow\quad
\boxed{r_C=o(D).}
\tag{BC.27}
```

The point is that repeated exits and reentries cannot create a linear number of inside blocks when the total metric surplus of the crossed hull sides is sublinear: their first-entry vertices would overpack boundary strips of total Oler capacity `o(D)`.

## 5. Finite support-span inequality

Let

```math
G_{\rm ext}:=S_D-G_{\rm in}.
```

If `z_C=|V(C)\setminus F|`, the exact path-block identity from the preceding corridor theorem is

```math
|E_{\rm ext}|=z_C+r_C-1.
```

Each exterior edge has support gain at most its original length `1+sigma_j`, and the corresponding slacks are part of the global total (BC.2). Hence

```math
G_{\rm ext}
\le z_C+r_C-1+t_D
\le Z_{\rm ext}+r_C-1+t_D.
\tag{BC.28}
```

Define

```math
C_{H,D}:=
R_{H,D}+{2\over\sqrt3-1},
\qquad
C_{\Delta,D}:=
R_{\Delta,D}+{2\over\sqrt3-1}.
\tag{BC.29}
```

Combining (BC.20), (BC.25), and (BC.28) gives the finite inequality

```math
\boxed{
u_B+Z_{\rm ext}+C_{H,D}H_D
\ge
S_D+1-t_D-C_{\Delta,D}\Delta_D.
}
\tag{BC.30}
```

At the worst asymptotic clearing constant `t_D -> h_*`,

```math
C_{H,D}\to17.388878053442944\ldots,
```

```math
C_{\Delta,D}\to14.847643837328274\ldots .
\tag{BC.31}
```

The constants are deliberately not optimized; their finiteness is what matters on the `H_D=o(D)` face. Equations (BC.1) and (BC.30) prove (BC.3).

Finally, (BC.0) gives

```math
u_B=H_D+\lambda_D-m\le H_D+\lambda_D.
\tag{BC.32}
```

Thus (BC.30) also yields

```math
\boxed{
\lambda_D+Z_{\rm ext}+(C_{H,D}+1)H_D
\ge
S_D+1-t_D-C_{\Delta,D}\Delta_D.
}
\tag{BC.33}
```

This proves (BC.4)-(BC.6).

## 6. Normalized frontier and remaining seam

If the normalized limits exist,

```math
{u_B\over D}\to u,
\quad
{Z_{\rm ext}\over D}\to z,
\quad
{H_D\over D}\to h,
\quad
{\lambda_D\over D}\to\lambda,
```

then the finite theorem gives the coarse explicit frontiers

```math
\boxed{
u+z+17.388878054\,h\ge{1\over2},
}
\tag{BC.34}
```

and

```math
\boxed{
\lambda+z+18.388878054\,h\ge{1\over2}.
}
\tag{BC.35}
```

The useful sharp face of this argument is `h=0`:

```math
\boxed{u+z\ge1/2,
\qquad
\lambda+z\ge1/2.}
\tag{BC.36}
```

The implication chain is now

```text
sub-sqrt(2) FREE entry edge crosses a force-hull side
  -> crossing diagonals satisfy p^2+s^2 >= 4
  -> almost-unit entry edge forces base length almost sqrt(3)
  -> bounded total parent slack makes distinct entered pockets cost
     almost (sqrt(3)-1) hull-perimeter surplus each
  -> H_D=o(D) gives o(D) entered pockets
  -> Oler in boundary half-stadiums gives o(D) inside blocks
  -> internal support gain <= u_B+o(D)
  -> external support gain <= Z_ext+o(D)
  -> u_B+Z_ext >= D/2-o(D)
  -> lambda_D+Z_ext >= D/2-o(D).
```

This does not close C-II. Linear exterior population can still pay the corridor, and a linear actual outer-walk detour is compatible with the current canonical full-core scalar ledger.

The remaining recipient split is nevertheless narrower. In the terminal `pi D-q=o(D)` regime, a FREE survivor must put at least half a diameter of linear currency into the sum of actual metric outer-walk detour and exterior isolates. If the detour is also sublinear, the source must have at least `D/2-o(D)` exterior isolates, doubling the previous `D/4-o(D)` lower bound for that branch.

The next useful theorem should attack exactly those two recipients: either prove a strict upper bound below `D/2` for exterior isolates in the terminal full-core geometry, or show that `lambda_D+Z_ext >= D/2-o(D)` overpays the canonical full-source Oler/cap and Sections 122-123 ledgers. Another refinement of the FREE matching count is unlikely to address the remaining obstruction.

**Disposition:** proved the crossing-diagonal lemma, converted FREE pocket entry into metric force-hull surplus, used Oler boundary-strip capacity to remove the extra inside-block/exterior coefficient, and obtained the terminal metric frontier `(b-per(F))+Z_ext >= D/2-o(D)`. The authoritative theorem-state ledger is unchanged; C-II remains open.
