# Target C-II — retuning the whole one-sided shore gives near-full-density deep force blocks

**Date:** 2026-09-17  
**Status:** proof-only high-`t` quantitative/structural strengthening; no canonical promotion claimed  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** linear one-sided rectangle shore and joint-cost budget; host-forced TB1 margin; non-antipodal TB2 direction packing; exact-antipodal force-pair theorem; narrow-force-pair capacity; bilateral birth loading; common-grid phase decomposition; host-forced transverse force margin  
**Certificate:** `research/verify_target_c_high_t_full_shore_deep_force_blocks_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing parameterized deep-force theorem starts from the fixed `4C`-good population. That is convenient, but it caps the leading density at

\[
c_0={113\over20{,}000{,}000}=5.65\times10^{-6}.
\]

The one-sided high-`t` shore itself is twice as large:

\[
|I_D|>{c\over2}D-o(D),
\qquad
c={113\over5{,}000{,}000}=2.26\times10^{-5},
\qquad {c\over2}=1.13\times10^{-5}=2c_0.
\tag{FS.1}
\]

The fixed `4C` threshold is not needed for the exact force pair, the host transverse margin, or the narrow-pair packing argument. Retuning the center threshold separately from the neighborhood threshold nearly recovers the whole one-sided shore. More strongly, every interface in a prescribed finite exact-phase neighborhood can be required to carry a fixed-angle exact force pair.

Put

\[
C=1{,}109{,}000,
\qquad
b={1567\over10000}=0.1567.
\tag{FS.2}
\]

Fix a radius `r>=0` and write

\[
m:=2r+1.
\tag{FS.3}
\]

Choose fixed constants

\[
\eta_0>0,
\qquad
\eta_r>0,
\qquad
0<\rho<\pi/2,
\tag{FS.4}
\]

and fixed thresholds `T_0,T_r` satisfying

\[
T_r\ge T_0,
\qquad
{c\over T_0}<\eta_0,
\qquad
{mc\over T_r}<\eta_r.
\tag{FS.5}
\]

Define

\[
\boxed{
\Lambda_r:={c\over2}-\eta_0-\eta_r-2m\rho.
}
\tag{FS.6}
\]

Assume `Lambda_r>0`.

---

## Theorem FS — near-full-shore deep wide-force blocks

Assume the positive-density non-antipodal TB1 alternative does not occur. Then for every fixed choice above and all sufficiently large `D`, there is a center set

\[
Q_D(r;T_0,T_r,\rho)\subset I_D
\tag{FS.7}
\]

with

\[
\boxed{
|Q_D|>\Lambda_rD-o(D).
}
\tag{FS.8}
\]

For every `i in Q_D`, all of the following hold.

### 1. The entire radius-`r` block is exact phase and bounded complexity

Every interface

\[
j\in[i-r,i+r]
\tag{FS.9}
\]

is exact-antipodal and `T_r`-good:

\[
J_j<T_rC.
\tag{FS.10}
\]

Hence all `2r+2` rows have one exact oriented phase,

\[
\boxed{
u_{i-r}=u_{i-r+1}=\cdots=u_{i+r+1}=:v_i
}
\tag{FS.11}
\]

and at every internal interface

\[
N_j,L_j<T_rC,
\qquad
B_j<{T_rC\over D},
\qquad
S_j+S_{j+1}<T_rC,
\qquad
0<|G_j|<T_rC.
\tag{FS.12}
\]

The center is better controlled:

\[
\boxed{J_i<T_0C,\qquad 0<|G_i|<T_0C.}
\tag{FS.13}
\]

### 2. Every internal interface carries a `rho`-wide exact force diamond

For every `j in [i-r,i+r]` there are two actual switching diameter bars with unit directions `d_j^-,d_j^+` and positive coefficients such that

\[
\boxed{
G_j
=D\bigl(\lambda_j^-d_j^-+\lambda_j^+d_j^+\bigr),
\qquad
\lambda_j^\pm>0,
}
\tag{FS.14}
\]

and

\[
\boxed{
d_{\mathbb{RP}^1}([d_j^-],[d_j^+])\ge\rho.}
\tag{FS.15}
\]

For all sufficiently large `D`, the two bars at each interface have four distinct endpoints and cross. With the common source circumcenter `o` and midpoint error `L_D=O(D^{3/4})`, every one of the `m` force diamonds contains the same disk

\[
\boxed{
B\!\left(o,{D\over2}\sin{\rho\over2}-L_D\right)
}
\tag{FS.16}
\]

and its two diagonals intersect within

\[
\left(1+{2\over\sin\rho}\right)L_D
\tag{FS.17}
\]

of `o`.

### 3. Every force pair is bilateral and uniformly transverse

After deleting only `O_{r,\rho}(1)` possible centers, the two birth endpoints at every internal interface lie on opposite ordered host subarcs. The host theorem also gives pointwise, for both force bars,

\[
\boxed{
|d_j^\pm\cdot Jv_i|\ge0.4143-o(1).
}
\tag{FS.18}
\]

Thus the elementary antipodal dipole coordinate at every internal interface has opposite-sign squared-length slopes with magnitude at least

\[
\boxed{(0.8286-o(1))D.}
\tag{FS.19}
\]

The compressed force coefficients satisfy

\[
\boxed{
(0.4143-o(1)){|G_j|\over D}
\le \lambda_j^\pm
\le {T_rC\over D\sin\rho}.
}
\tag{FS.20}
\]

No absolute coefficient floor is claimed, because `|G_j|` may tend to zero.

### 4. The whole block uses one common inverse-`D` train grid

Let `B_0` be the global column family from the common-grid theorem:

\[
|B_0|>0.0783D-o(D),
\tag{FS.21}
\]

with column phase offsets bounded by

\[
q_b<{3.004\times10^6\over D}+o(D^{-1}).
\tag{FS.22}
\]

Because the center is `T_0`-good,

\[
S_i<S_i+S_{i+1}<T_0C.
\]

The exact additive phase decomposition gives, for every `b in B_0`,

\[
0<\theta(\tau_i,b)-{\pi\over3}
<
\left({T_0C\over0.1567}+3.004\times10^6\right){1\over D}
+o(D^{-1}).
\tag{FS.23}
\]

All rows in (FS.11) have exactly the same oriented phase as `tau_i`. Hence the same bound, with the same constant independent of `r`, holds for every row in the block:

\[
\boxed{
0<\theta(\tau_j,b)-{\pi\over3}
< {K(T_0)\over D}+o(D^{-1}),
\quad
K(T_0):={T_0C\over0.1567}+3.004\times10^6,
}
\tag{FS.24}
\]

for all

\[
i-r\le j\le i+r+1,
\qquad b\in B_0.
\]

The inherited signed-grid orientation gives one common crossing order throughout the full `(2r+2)`-by-`|B_0|` rectangle.

### 5. The exact reactions are ordered through the whole block

Write the cut resultants on the exact phase block as

\[
F_j=A_jv_i,
\qquad A_j>0.
\tag{FS.25}
\]

The one-sided separation functional gives `phi(G_j)>0` at every internal interface. Therefore

\[
\boxed{
A_{i-r},A_{i-r+1},\ldots,A_{i+r+1}
\text{ is strictly monotone},
}
\tag{FS.26}
\]

all `G_j` point in the same ordinary direction, and

\[
\boxed{
\sum_{j=i-r}^{i+r}|G_j|
=|A_{i-r}-A_{i+r+1}|<D.
}
\tag{FS.27}
\]

Thus each retained center carries an arbitrary prescribed finite stack of ordered, same-axis exact KKT reactions, each represented by a fixed-angle central diameter dipole.

---

## 1. Retune the center and neighborhood thresholds separately

The one-sided shore satisfies (FS.1), and the audited joint-cost budget is

\[
\sum_{i\in I_D}J_i<CcD+o(D).
\tag{FS.28}
\]

Call a potential center `T_0`-bad when `J_i>=T_0C`. Markov gives

\[
\boxed{
|Z_D^{center}|<{c\over T_0}D+o(D)<\eta_0D+o(D).
}
\tag{FS.29}
\]

This is the only loss needed to keep the center reaction and the common-grid angle constant uniformly bounded by `T_0`.

For the neighborhood, call an interface `T_r`-bad when `J_i>=T_rC`. Again

\[
|Z_D^{bad}(T_r)|<{c\over T_r}D+o(D).
\tag{FS.30}
\]

At fixed `T_r`, every `T_r`-good non-antipodal interface is TB1 or genuine TB2 under the audited local certificate classification. On the branch considered here, the TB1 population is `o(D)`: host geometry gives every TB1 switching blocker a fixed `(0.4143-o(1))D` opening margin, so a linear TB1 population would be the excluded alternative. The `T_r`-good genuine-TB2 population is also `o(D)`, because its opening width is `O_{T_r}(D^{-1})`, all row phases lie in one `o(1)` projective window, the selected TB2 diameter directions are distinct across interfaces, and C67 separates them by at least `1/D`.

Consequently the separator set

\[
Z_D^{sep}(T_r)
:=\{\text{`T_r`-bad or non-antipodal interfaces}\}
\tag{FS.31}
\]

obeys

\[
\boxed{
|Z_D^{sep}(T_r)|<{c\over T_r}D+o(D).
}
\tag{FS.32}
\]

A separator belongs to the radius-`r` window of at most `m=2r+1` centers. Therefore deleting all centers whose neighborhood meets a separator costs at most

\[
\boxed{
m|Z_D^{sep}(T_r)|<\eta_rD+o(D).}
\tag{FS.33}
\]

Every surviving neighborhood is exact phase and `T_r`-good throughout.

---

## 2. Narrow force pairs cost only `2m rho D`

At every exact-antipodal interface choose the exact positive force pair. Let its projective gap be `eta_i`.

The narrow-pair packing proof is independent of the local cost threshold. It uses only:

1. both bars switch at the same one-sided interface;
2. their transverse signs relative to the exact reaction axis are opposite;
3. all switching directions lie in one common open semicircle;
4. all row axes lie in one shrinking projective window;
5. switching supports at distinct interfaces are disjoint; and
6. C67 separates distinct actual diameter directions by at least `1/D`.

Hence the number of exact interfaces with

\[
\eta_i<\rho
\]

is at most

\[
\boxed{2\rho D+o(D).}
\tag{FS.34}
\]

To require every interface in a radius-`r` block to be `rho`-wide, delete every center whose neighborhood meets this narrow set. The loss is at most

\[
\boxed{2m\rho D+o(D).}
\tag{FS.35}
\]

For fixed `rho`, the bilateral-birth theorem has only `O_\rho(1)` same-host exceptions over the whole shore. Expanding those through radius `r` costs only `O_{r,\rho}(1)` more centers.

Start from (FS.1), delete the `O(r)` shore-end centers, then apply (FS.29), (FS.33), (FS.35), and the bounded bilateral deletion. This gives

\[
|Q_D|
>
\left({c\over2}-{c\over T_0}-{mc\over T_r}-2m\rho\right)D-o(D)
>\Lambda_rD-o(D),
\]

which proves (FS.8).

---

## 3. Force and grid consequences

Every retained internal interface is exact-antipodal, so the exact force-pair theorem gives (FS.14). The `rho`-wide deletion gives (FS.15), after which the central-diamond theorem gives (FS.16)--(FS.17). The bilateral theorem and host-forced transverse theorem give (FS.18)--(FS.19). Since `J_j<T_rC`,

\[
|G_j|\le DB_j<T_rC.
\]

The exact sine-law force representation, the pair gap, and the host margin give (FS.20).

For the grid, every row of the one-sided shore belongs to the complete rectangle row family `A_*` and crosses the common `B_0`. The additive decomposition

\[
\delta_{ab}=g+r_a+q_b,
\qquad g,r_a,q_b\ge0,
\]

gives

\[
g+r_i\le {S_i\over|B_+|}.
\]

Use `S_i<T_0C`, `|B_+|>0.1567D-o(D)`, and (FS.22) to obtain (FS.23)--(FS.24). Exact phase propagates the center angle bound to the whole block, so the grid constant depends on `T_0`, but not on `T_r` or `r`.

Finally, (FS.26)--(FS.27) are the exact constant-phase reaction monotonicity identity applied to the full retained block.

---

## 4. Density can approach the whole one-sided shore

The three losses in (FS.6) are independent fixed parameters.

### Corollary FS.1 — asymptotic `c/2` ceiling

For every fixed `r` and every fixed

\[
0<\varepsilon<{c\over2},
\]

choose

\[
\eta_0=\eta_r={\varepsilon\over4},
\qquad
\rho={\varepsilon\over4m},
\tag{FS.36}
\]

and fixed thresholds satisfying

\[
T_0>{4c\over\varepsilon},
\qquad
T_r>{4mc\over\varepsilon},
\qquad T_r\ge T_0.
\tag{FS.37}
\]

Then

\[
\boxed{
|Q_D|>\left({c\over2}-\varepsilon\right)D-o(D).
}
\tag{FS.38}
\]

Thus the deep fully-wide force-block density can be made arbitrarily close to

\[
\boxed{{c\over2}=1.13\times10^{-5}=2c_0,}
\tag{FS.39}
\]

rather than being capped by the old fixed-good coefficient `c_0`.

### Corollary FS.2 — concrete ninety-percent specialization

Retain ninety percent of `c/2` by taking

\[
\varepsilon={c\over20},
\qquad
\eta_0=\eta_r={c\over80},
\qquad
\rho={c\over80m},
\tag{FS.40}
\]

and

\[
\boxed{T_0=81,\qquad T_r=80m+1.}
\tag{FS.41}
\]

Then

\[
\boxed{
|Q_D|>{9c\over20}D-o(D)
=1.017\times10^{-5}D-o(D).
}
\tag{FS.42}
\]

Every one of the `m=2r+1` internal force pairs has projective gap at least

\[
\boxed{
\rho={2.825\times10^{-7}\over m},
}
\tag{FS.43}
\]

while the common-grid angle bound is independent of `r`:

\[
\boxed{
0<\theta-{\pi\over3}
<{5.763\times10^8\over D}+o(D^{-1}).
}
\tag{FS.44}
\]

The center reaction obeys

\[
\boxed{|G_i|<81C=89{,}829{,}000.}
\tag{FS.45}
\]

The constants are deliberately simple. The structural gain is that at density arbitrarily close to the whole one-sided shore, every prescribed finite exact-phase neighborhood is filled at every interface by a wide, bilateral, force-carrying central diameter dipole, while all rows use the same global inverse-`D` train grid.

---

## 5. Growing-depth diagonal

For each fixed `r`, the leading density in (FS.38) can be chosen independently of `r`; only `rho` and `T_r` change. A diagonal extraction therefore gives radii

\[
r_D\to\infty
\]

and densities arbitrarily close to `c/2`, provided `D` is taken fast enough that the chosen fixed-at-each-stage thresholds remain negligible compared with `D`. The common-grid angle coefficient depends only on the center threshold `T_0`, so it can remain fixed along such a diagonal if the target density loss `epsilon` is fixed.

The pair gap necessarily shrinks with the prescribed block depth in the explicit construction (FS.36), so no depth-independent central-diamond radius is claimed on this diagonal. For every fixed depth, however, `rho` is an absolute positive constant independent of `D`.

---

## 6. Frontier effect

The no-TB1 high-`t` branch can no longer be treated as isolated exact-force centers of density at most `c_0`. After retuning the cost threshold, almost the entire one-sided shore may be organized into overlapping finite blocks with simultaneous structure:

```text
one exact row phase through the whole block
+ one global inverse-D near-triangular train grid
+ a rho-wide central exact-force diameter pair at every interface
+ bilateral ordered births at every interface
+ fixed host-transverse margin on every force ray
+ strictly monotone same-axis KKT reactions through the block.
```

The remaining exact-antipodal target is now local but arbitrarily deep: rule out an arbitrarily long exact-phase strip stack carrying a force-carrying central diameter dipole at every interface while all interfaces share the same ordered near-equilateral train grid and the same two host arcs.

C-II and Level I remain open.

**Disposition:** replaced the fixed-good `c_0` density ceiling by a near-full-shore `c/2=2c_0` ceiling and upgraded deep centers to fixed-depth blocks in which every internal interface carries a wide bilateral exact force diamond on one common inverse-`D` grid. No closure is claimed.
