# Target C-II — a linear far-terminal rail forces macroscopic terminal span

**Date:** 2026-09-17
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed
**Scope:** the far-terminal branch of the physical-piece support normal form through `t=(q-k)/D<=1.8687`
**Dependencies:** physical-piece support normal form; one-sided disjoint switching supports; canonical C67 diameter-direction separation; unit separation of the source; full-source circumradius/midpoint localization
**Certificate:** `research/verify_target_c_high_t_terminal_piece_macroscopic_span_t18687.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The physical-piece theorem leaves one genuinely non-host alternative: a positive-linear family of actual diameter bars

\[
e_j=x_jy_j,
\qquad j=1,\ldots,M,
\tag{TM.1}
\]

whose birth endpoints `x_j` are distinct and occur in order on one fixed pre-hub host arc, while every partner endpoint `y_j` lies on the single far terminal boundary piece `T_m`.

The terminal piece was previously allowed to be geometrically tiny even if many rail bars shared partner vertices. A linear rail cannot be confined to such a microscopic terminal cap. Unit separation makes the ordered birth vertices have macroscopic Euclidean diameter. The full-source near-circle theorem then transfers that diameter almost antipodally to the terminal partners, with only `O(D^(3/4))` loss.

Thus a linear terminal rail forces `T_m` itself to have positive limiting chord diameter and positive limiting angular span about the common source circumcenter.

---

## Theorem TM — macroscopic terminal-piece span

Assume the far-terminal branch contains

\[
M>\mu D-o(D),
\qquad \mu>0,
\tag{TM.2}
\]

selected actual diameter bars `e_j=x_jy_j` with distinct birth endpoints `x_j` on one fixed source-hull host arc and partner endpoints `y_j in T_m`.

Let `o` and `L_D` be the common source circumcenter and midpoint radius from the full-source near-circle theorem:

\[
L_D=\sqrt{D\eta+\eta^2},
\qquad
\eta=3^{1/4}\sqrt D,
\qquad
L_D=(3^{1/8}+o(1))D^{3/4}.
\tag{TM.3}
\]

Then there are two selected indices `a,b` such that

\[
\boxed{
|x_a-x_b|\ge {M-1\over\pi}
}
\tag{TM.4}
\]

and

\[
\boxed{
|y_a-y_b|
\ge {M-1\over\pi}-4L_D.
}
\tag{TM.5}
\]

Consequently

\[
\boxed{
\operatorname{diam}(T_m\cap S)
\ge {M-1\over\pi}-4L_D
}
\tag{TM.6}
\]

for the source `S`, and therefore

\[
\boxed{
\liminf_{D\to\infty}
{\operatorname{diam}(T_m\cap S)\over D}
\ge {\mu\over\pi}.
}
\tag{TM.7}
\]

There is also a fixed angular consequence. Put

\[
u_y={y-o\over |y-o|}
\]

for a terminal partner. For the same pair `a,b`, if `theta_ab` is the smaller angle between `u_{y_a}` and `u_{y_b}`, then

\[
\boxed{
\sin{\theta_{ab}\over2}
\ge
{M-1\over\pi D}-{6L_D\over D}.
}
\tag{TM.8}
\]

Hence

\[
\boxed{
\liminf_{D\to\infty}
\operatorname{angdiam}_o(T_m\cap S)
\ge
2\arcsin\!\left({\mu\over\pi}\right)>0.
}
\tag{TM.9}
\]

Here `angdiam_o` is the maximum smaller central angle about the common source circumcenter `o` between two source vertices in the terminal piece.

---

## 1. Diameter endpoints are source-hull vertices

Every endpoint of an actual diameter edge is an extreme source point. Indeed, suppose an endpoint `x` of a diameter edge `xy` were a nontrivial convex combination

\[
x=(1-t)p+tq,
\qquad 0<t<1,
\qquad p\ne q,
\tag{TM.10}
\]

of source-hull points. Strict convexity of squared distance gives

\[
|x-y|^2
< (1-t)|p-y|^2+t|q-y|^2
\le D^2,
\tag{TM.11}
\]

contrary to `|x-y|=D`.

Thus all selected births `x_j` are vertices of the source convex hull. Since the physical-piece theorem orders them along one fixed host arc, after relabeling they occur in cyclic hull order

\[
x_1,x_2,\ldots,x_M.
\tag{TM.12}
\]

---

## 2. Unit separation gives macroscopic birth diameter

The source is unit-separated, so

\[
|x_{j+1}-x_j|\ge1
\qquad(1\le j<M).
\tag{TM.13}
\]

Let

\[
P=\operatorname{conv}\{x_1,\ldots,x_M\}.
\]

A subset of vertices of a convex polygon remains in convex position in the inherited cyclic order. Therefore every segment `x_jx_{j+1}` is a boundary edge of `P`, and

\[
\operatorname{per}(P)
\ge
\sum_{j=1}^{M-1}|x_{j+1}-x_j|
\ge M-1.
\tag{TM.14}
\]

Cauchy's perimeter formula gives

\[
\operatorname{per}(P)
=
\int_0^\pi w_P(\phi)\,d\phi
\le
\pi\operatorname{diam}(P),
\tag{TM.15}
\]

because every directional width is at most the Euclidean diameter. Hence

\[
\operatorname{diam}(P)\ge {M-1\over\pi}.
\tag{TM.16}
\]

The diameter of a finite convex polygon is attained by two vertices, proving (TM.4).

This step uses the full linear family directly. No source-degree thinning and no endpoint-disjoint partner extraction is needed.

---

## 3. Near-central diameter chords transfer birth span to terminal span

For each selected diameter edge let

\[
m_j={x_j+y_j\over2}.
\]

The full-source midpoint theorem gives

\[
|m_j-o|<L_D
\tag{TM.17}
\]

simultaneously for every actual diameter edge.

Since

\[
y_j=2m_j-x_j,
\tag{TM.18}
\]

we have for the pair `a,b` from (TM.4)

\[
\begin{aligned}
|y_a-y_b|
&=|-(x_a-x_b)+2(m_a-m_b)|\\
&\ge |x_a-x_b|-2|m_a-m_b|\\
&>{M-1\over\pi}-4L_D.
\end{aligned}
\tag{TM.19}
\]

Both partners lie in `T_m`, so this proves (TM.5)--(TM.7).

The point is stronger than merely obtaining many distinct terminal partners. A linear birth rail cannot be compressed into a terminal cluster of diameter `o(D)` at all.

---

## 4. The terminal piece also has positive central angular width

The same midpoint bound implies

\[
\left||y_j-o|-{D\over2}\right|<L_D.
\tag{TM.20}
\]

Define the radial projection of a terminal partner to the radius-`D/2` circle about `o` by

\[
z_j=o+{D\over2}u_{y_j}.
\tag{TM.21}
\]

Then

\[
|y_j-z_j|<L_D.
\tag{TM.22}
\]

Using (TM.5),

\[
|z_a-z_b|
\ge |y_a-y_b|-2L_D
>{M-1\over\pi}-6L_D.
\tag{TM.23}
\]

But if `theta_ab` is their smaller central angle,

\[
|z_a-z_b|=D\sin{\theta_{ab}\over2}.
\tag{TM.24}
\]

This proves (TM.8). Since `L_D/D=O(D^{-1/4})` and `liminf M/D >= mu` along the survivor sequence, (TM.9) follows.

---

## 5. Direction separation gives a stronger terminal spread

The preceding argument uses only unit separation of the ordered birth vertices. The canonical C67 separation of **diameter directions** gives a stronger conclusion for the present rail.

The selected bars belong to distinct one-sided switching sets, hence they are distinct actual diameter edges. Their projective chord directions are therefore pairwise separated by

\[
\delta_D=2\arcsin{1\over2D}\ge {1\over D}.
\tag{TM.25}
\]

Let

\[
\Delta_D
:=
\operatorname{diam}_{\mathbb{RP}^1}
\{[y_j-x_j]:1\le j\le M\}.
\tag{TM.26}
\]

A simple circle-packing lemma gives the uniform finite-set bound

\[
\boxed{
\Delta_D\ge \min\!\left\{{\pi\over3},(M-1)\delta_D\right\}.
}
\tag{TM.27}
\]

Indeed, suppose a finite subset of a circle of circumference `pi` has geodesic diameter `d<pi/3`. Fix one point and lift the others into `[-d,d]`. If the extreme lifted points are `-q` and `p`, then their circular distance is

\[
\min\{p+q,\pi-(p+q)\}\le d.
\]

The second alternative would require `p+q>=pi-d`, while `p+q<=2d`, impossible for `d<pi/3`. Hence `p+q<=d`, so the whole set lies in one arc of length `d`. Pairwise `delta_D` separation then gives `d>=(M-1)delta_D`. If instead the projective diameter is at least `pi/3`, the minimum in (TM.27) is automatic. This proves (TM.27) without any upper assumption on `M`.

Now orient each selected chord from birth to terminal partner,

\[
d_j={y_j-x_j\over D}.
\tag{TM.28}
\]

Since

\[
y_j-o={D\over2}d_j+(m_j-o),
\qquad |m_j-o|<L_D,
\]

the terminal radial line differs projectively from the chord line by at most

\[
\epsilon_D
:=
\arcsin\!\left({L_D\over D/2-L_D}\right)
=O(D^{-1/4}).
\tag{TM.29}
\]

Choose two chord directions realizing `Delta_D`. Their terminal radial projective separation is at least

\[
\Delta_D-2\epsilon_D.
\tag{TM.30}
\]

The ordinary smaller central angle between the corresponding terminal rays is at least their projective separation. Therefore

\[
\boxed{
\operatorname{angdiam}_o(T_m\cap S)
\ge
\min\!\left\{{\pi\over3},(M-1)\delta_D\right\}-2\epsilon_D.
}
\tag{TM.31}
\]

and, from `M>mu D-o(D)`,

\[
\boxed{
\liminf_{D\to\infty}
\operatorname{angdiam}_o(T_m\cap S)
\ge \mu.
}
\tag{TM.32}
\]

This supersedes (TM.9), since `mu>2 asin(mu/pi)` for the small current densities.

Radially projecting the same two terminal vertices to the radius-`D/2` circle and using (TM.22) gives

\[
\operatorname{diam}(T_m\cap S)
\ge
D\sin\!\left(
{\min\{\pi/3,(M-1)\delta_D\}-2\epsilon_D\over2}
\right)-2L_D,
\tag{TM.33}
\]

whenever the displayed angular lower bound is positive. Hence

\[
\boxed{
\liminf_{D\to\infty}
{\operatorname{diam}(T_m\cap S)\over D}
\ge \sin(\mu/2).
}
\tag{TM.34}
\]

Thus C67 upgrades the terminal rail from the perimeter-transfer scale `mu/pi` to the sharper direction-packing scale `sin(mu/2)~mu/2` in chord diameter and `mu` in central angle.

---

## 6. Current explicit consequences

### Unconditional corrected blocker fork

The physical-piece theorem has terminal-branch density

\[
\mu_0={s_0\over6}
={791\over1{,}920{,}000{,}000}
\approx4.11979166667\times10^{-7}.
\tag{TM.39}
\]

If the unconditional survivor lands in the far-terminal branch, the perimeter-transfer bounds give

\[
\liminf {\operatorname{diam}(T_m\cap S)\over D}
\ge {\mu_0\over\pi}
\approx1.311370\times10^{-7},
\]

but the direction-packing bounds sharpen this to

\[
\boxed{
\liminf {\operatorname{diam}(T_m\cap S)\over D}
\ge \sin(\mu_0/2)
\approx2.059896\times10^{-7},
}
\tag{TM.35}
\]

and

\[
\boxed{
\liminf\operatorname{angdiam}_o(T_m\cap S)
\ge\mu_0
\approx4.119792\times10^{-7}\text{ radians}.
}
\tag{TM.36}
\]

### Parameterized deep exact-force branch

For the ninety-percent choice in the deep exact-force rail,

\[
\lambda=5.085\times10^{-6},
\qquad
\mu_{deep}={\lambda\over3}=1.695\times10^{-6}.
\tag{TM.40}
\]

A far-terminal survivor then has the stronger direction-packing bounds

\[
\boxed{
\liminf {\operatorname{diam}(T_m\cap S)\over D}
\ge \sin(1.695\times10^{-6}/2)
\approx8.47500\times10^{-7},
}
\tag{TM.37}
\]

and

\[
\boxed{
\liminf\operatorname{angdiam}_o(T_m\cap S)
\ge1.695\times10^{-6}\text{ radians}.
}
\tag{TM.38}
\]

The constants are small because the current blocker-density constants are small, but the qualitative conclusion is scale-sharp: the terminal boundary piece must have `Theta(D)` Euclidean extent and a nonvanishing angular extent after normalization.

---

## 7. Frontier effect

The far-terminal escape is no longer an arbitrary concentration of a linear number of incidences into a possibly microscopic terminal cap. It must contain a macroscopic geometric object:

```text
far-terminal branch:
  M = Omega(D) exact diameter bars
  + M distinct ordered birth hull vertices on one fixed host
  + every partner lies in T_m
  + all supports persist to terminal tag m
  + birth-set diameter >= (M-1)/pi
  + terminal partner-set diameter >= D sin(mu/2) - o(D)
  + terminal central angular diameter >= mu - o(1)
  + the weaker perimeter-transfer bounds remain independently valid.
```

This creates a direct next target. Any independent terminal-ledger or stopped-train theorem that puts `T_m` inside an `o(D)` chord-diameter cap, or an `o(1)` central-angle cap, would now eliminate the terminal branch outright. Alternatively, a pair realizing the stronger C67 direction spread can be combined with the common train rectangle and terminal endpoint-energy geometry.

C-II remains open. No such upper bound on the size of `T_m` is currently proved in the repository.

**Disposition:** proved that a positive-linear far-terminal rail forces the far terminal boundary piece itself to have positive limiting Euclidean and central-angular span. The terminal branch cannot survive by collapsing all hubward partners into a microscopic cap. C-II and Level I remain open.
