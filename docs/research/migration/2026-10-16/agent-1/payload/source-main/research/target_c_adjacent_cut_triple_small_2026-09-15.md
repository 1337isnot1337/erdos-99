# Target C-II — one live adjacent O--O cut pair is simultaneously phase-close and low-switch

**Date:** 2026-09-15  
**Repository base:** `82ed6442ebf6313b364bde645076b2934aceeb57`  
**Status:** proof-only source-level structural strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.844`; after the current two-leaf exclusion this is live on `1.84362<t<=1.844`  
**Dependencies:** audited `0.7404D` smallest-leaf weighted center fan; corrected good-leaf complement-dual path construction; canonical global strict-rhombus angular-defect budget; exact laminar O--O interval rows; audited §157 KKT cut resultants; Hopf--Pannwitz diameter-edge count  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The exact laminar multishear theorem reduces a consecutive O--O backbone to an interval-row diameter system.  Two separate obstructions remained:

1. a useful adjacent pair should have almost the same leaf direction, so opposite shears nearly cancel on diameter rows spanning both cuts; and
2. only a bounded number of actual diameter rows should start or stop between those cuts, with small total KKT multiplier mass.

Both can be forced on the **same adjacent pair**.  The proof spends three global budgets on one good-leaf backbone:

- each actual diameter interval starts/stops at most twice;
- each diameter multiplier is spent in at most two interval switches; and
- the whole strict-rhombus system has only `O(D)` angular defect.

Averaging the sum of these three nonnegative costs gives the following finite/asymptotic normal form.

### Theorem AC — triple-small adjacent pair

Every unbounded survivor sequence in the stated `t<=1.844` scope has, for all sufficiently large members, two **consecutive** smallest-leaf outer-to-outer trains

\[
\tau_i,\tau_{i+1}
\]

on one complement-dual backbone path such that, writing their coherently oriented unit contact directions as `u_i,u_{i+1}`:

1. the number `N_i` of actual diameter edges whose interval incidence changes between the two cuts obeys
   \[
   \boxed{N_i<21200+o(1);}
   \tag{AC.1}
   \]
2. their switching diameter KKT multiplier mass
   \[
   B_i:=\sum_h\beta_h
   |\varepsilon_{h,i+1}-\varepsilon_{hi}|
   \]
   obeys
   \[
   \boxed{B_i<{21200\over D}+o(D^{-1});}
   \tag{AC.2}
   \]
3. the projective leaf-phase gap satisfies
   \[
   \boxed{
   d_{\mathbb{RP}^1}(u_i,u_{i+1})
   <{21200\over D}+o(D^{-1});
   }
   \tag{AC.3}
   \]
4. for the exact §157 KKT cut resultants
   \[
   F_j=A_j u_j,
   \qquad
   A_j=\sum_{e\in E(\tau_j)}\alpha_e,
   \]
   one has
   \[
   \boxed{
   \|F_{i+1}-F_i\|<21200+o(1),
   \qquad
   |A_{i+1}-A_i|<21200+o(1).
   }
   \tag{AC.4}
   \]

The constant `21200` is deliberately coarse.  The exact rational certificate bounds the combined average by

\[
21175.904\ldots .
\]

The point is the scale, not the decimal: the same consecutive pair has **finite support change**, **inverse-`D` switching KKT mass**, and **inverse-`D` phase mismatch**.

This is the first current theorem that reduces the live consecutive-cut multishear obstruction to finitely many first-order diameter rows while keeping the two train directions asymptotically identical.

---

## 1. A high-phase center train crosses a linear good-leaf path

Use the current `t<=1.844` smallest-leaf fan notation.  For a retained smallest-leaf O--O train `tau`, let `w_tau in (0,1]` be its retained pair weight and let

\[
d_\tau D
\]

be the number of center-phase complete trains crossing it.  The audited inputs are

\[
{\sum_\tau w_\tau d_\tau\over\sum_\tau w_\tau}
>0.7404-o(1),
\tag{AC.5}
\]

\[
{1\over D}\sum_\tau w_\tau>0.0848-o(1),
\tag{AC.6}
\]

and the total center-train count

\[
N_C<1.063D+o(D).
\tag{AC.7}

Fix the simple rational threshold

\[
\lambda={677\over1000}
\]

and call a leaf train **good** if

\[
d_\tau>\lambda.
\]

Weighted thresholding gives normalized retained good weight, hence also distinct good-train count density, at least

\[
\begin{aligned}
g
&={ (0.7404-0.677)(0.0848)\over1.063-0.677}\\
&={16801\over1206250}\\
&=0.0139282901\ldots .
\end{aligned}
\tag{AC.8}

Order the actual center trains by real phase representative inside their frozen center window.  Let `H` be the top

\[
r={61\over125}=0.488
\]

fraction in this order.  Up to `O(1)` rounding,

\[
|H|\le rN_C.
\]

The complementary lower block contains at most `(1-r)N_C` center trains.  Hence every good leaf has at least

\[
\begin{aligned}
d_{top}D-o(D)
&:=\bigl[\lambda-(1-r)(1.063)\bigr]D-o(D)\\
&={16593\over125000}D-o(D)\\
&=0.132744D-o(D)
\end{aligned}
\tag{AC.9}

neighbors in `H`.

There are at least `gD-o(D)` distinct good leaves, so good-leaf/`H` incidence exceeds

\[
d_{top}gD^2-o(D^2).
\]

Since `|H|<=r(1.063)D+o(D)`, some center train

\[
\gamma\in H
\]

crosses more than

\[
\begin{aligned}
pD-o(D)
&:={d_{top}g\over r(1.063)}D-o(D)\\
&={278778993\over78216868750}D-o(D)\\
&=0.0035641799\ldots D-o(D)
\end{aligned}
\tag{AC.10}

distinct good smallest-leaf O--O trains.

Good leaves are pairwise noncrossing.  Their complement-region dual is a tree, and the leaves crossed by one center train form one simple path in that tree.  Thus order the path crossed by `gamma` as

\[
P=(\tau_1,\ldots,\tau_m),
\qquad
m>pD-o(D).
\tag{AC.11}

---

## 2. The same path has only `O(1)` total phase offset

Let `alpha_gamma` be the real phase angle of the chosen center train and `beta_j` the real phase angle of leaf train `tau_j`, oriented as in the current center/leaf phase theorem.  Since `gamma` crosses every `tau_j`,

\[
q_j:=\beta_j-\alpha_\gamma-{\pi\over3}>0.
\tag{AC.12}

Because `gamma` lies in the top `r` center-phase fraction, the number of center trains with phase strictly greater than `alpha_gamma` is at most

\[
rN_C+O(1)
\le r(1.063)D+o(D).
\]

Every `tau_j` is good, so it has at least

\[
\begin{aligned}
d_{low}D-o(D)
&:=\bigl[\lambda-r(1.063)\bigr]D-o(D)\\
&={9891\over62500}D-o(D)\\
&=0.158256D-o(D)
\end{aligned}
\tag{AC.13}

center neighbors `c` with

\[
\alpha_c\le\alpha_\gamma.
\]

At such a center/leaf strict-rhombus crossing, the angular excess over `pi/3` is

\[
\delta_{cj}
=\beta_j-\alpha_c-{\pi\over3}
=q_j+(\alpha_\gamma-\alpha_c)
\ge q_j.
\tag{AC.14}

The canonical global strict-rhombus angular-defect budget is

\[
\sum_R\delta_R<C_{phase}D,
\qquad
C_{phase}={\pi^2\sqrt3(2+\sqrt3)\over12}.
\tag{AC.15}

The crossings counted for different leaves are different strict rhombi.  Summing (AC.14) over the `d_low D-o(D)` lower-phase center neighbors of every path leaf gives

\[
\boxed{
\sum_{j=1}^m q_j
\le {C_{phase}\over d_{low}}+o(1).
}
\tag{AC.16}

Thus a path of linear length has only bounded **total** phase offset from the single center train `gamma`.

For two adjacent leaves,

\[
d_{\mathbb{RP}^1}(u_i,u_{i+1})
=|\beta_{i+1}-\beta_i|
=|q_{i+1}-q_i|
\le q_i+q_{i+1}.
\tag{AC.17}

---

## 3. Diameter interval rows have two independent global switch budgets

Root the complement-dual path at one end and choose the nested shores from the exact laminar multishear theorem.  For every actual diameter edge `h`, let

\[
\varepsilon_{hj}\in\{-1,0,1\}
\]

be its signed shore incidence on cut `tau_j`.  The exact interval theorem gives

\[
(\varepsilon_{h1},\ldots,\varepsilon_{hm})
=0,\ldots,0,s,\ldots,s,0,\ldots,0
\]

for one sign `s`.  Hence an actual diameter edge can change incidence at at most two internal path boundaries.

Let

\[
N_i:=\#\{h:\varepsilon_{h,i+1}\ne\varepsilon_{hi}\}.
\tag{AC.18}

Then

\[
\sum_{i=1}^{m-1}N_i\le2h,
\tag{AC.19}

where `h` is the number of actual diameter edges.  Hopf--Pannwitz gives

\[
h\le q.
\]

Every consecutive loaded force-hull side has length at least one, so

\[
q\le\operatorname{per}(F)\le\pi D.
\]

Therefore

\[
\boxed{
\sum_{i=1}^{m-1}N_i\le2\pi D.
}
\tag{AC.20}

Now use the positive diameter KKT multipliers normalized by

\[
\sum_h\beta_h=1.
\]

Put

\[
B_i:=\sum_h\beta_h
|\varepsilon_{h,i+1}-\varepsilon_{hi}|.
\tag{AC.21}

The same interval variation gives

\[
\boxed{
\sum_{i=1}^{m-1}B_i\le2.
}
\tag{AC.22}

Finally, the coherently oriented §157 cut resultant is

\[
F_j=A_j u_j
=\sum_h\beta_h\varepsilon_{hj}r_h,
\qquad |r_h|=D.
\tag{AC.23}

Thus

\[
\boxed{
\|F_{i+1}-F_i\|
\le DB_i.
}
\tag{AC.24}

---

## 4. Average all three costs on the same adjacent boundary

For each internal boundary define the nonnegative combined cost

\[
T_i
:=N_i+DB_i+D(q_i+q_{i+1}).
\tag{AC.25}

Equations (AC.16), (AC.20), and (AC.22) give

\[
\begin{aligned}
\sum_{i=1}^{m-1}T_i
&\le
2\pi D+2D
+2D\sum_{j=1}^m q_j\\
&\le
\left(
2\pi+2+{2C_{phase}\over d_{low}}
\right)D+o(D).
\end{aligned}
\tag{AC.26}

Since `m>pD-o(D)`, some internal boundary satisfies

\[
T_i
\le
{2\pi+2+2C_{phase}/d_{low}\over p}+o(1).
\tag{AC.27}

Use the outward rational enclosures already standard in the current certificate stack,

\[
\pi<{355\over113},
\qquad
\sqrt3<{17321\over10000}.
\]

They give

\[
C_{phase}
<{3258689123681\over612912000000}
=5.3167324569\ldots
\tag{AC.28}

and the exact companion verifier proves

\[
\boxed{
{2\pi+2+2C_{phase}/d_{low}\over p}
<21175.904
<21200.
}
\tag{AC.29}

Because the three summands in `T_i` are nonnegative, each is individually below `21200+o(1)`.  This proves (AC.1)--(AC.3).  Equation (AC.24) proves the first part of (AC.4), and the reverse triangle inequality gives

\[
|A_{i+1}-A_i|
=\bigl||F_{i+1}|-|F_i|\bigr|
\le\|F_{i+1}-F_i\|.
\]

---

## 5. Why this is stronger than the separate rectangle and rank statements

The current live band now contains an adjacent pair with all of the following on the **same two exact finite cut coordinates**:

```text
consecutive O-O leaf cuts tau_i, tau_{i+1}
+ exact finite two-coordinate contact-preserving multishear
+ leaf directions differ by O(1/D)
+ at most O(1) actual diameter rows start/stop between the cuts
+ total KKT multiplier of those switching rows is O(1/D)
+ KKT cut-resultant vectors differ by O(1).
```

This is precisely the regime where the opposite two-cut shear

\[
(\theta_i,\theta_{i+1})=(t,-t)
\]

nearly cancels on every diameter row spanning both cuts.  Only the finitely many switching rows fail that cancellation at first order.

The theorem does **not** yet show those finitely many rows can all be made nonincreasing.  Their number is bounded independently of `D`, but `21200` is still much larger than the two available shear parameters.  No false finite-dimensional separation claim is made.

The next closing target is now finite and explicit: use the planar diameter-thrackle geometry of the switching rows, together with their total multiplier `O(D^{-1})` and the exact finite multishear formula, to reduce the active cusp set further or construct a finite same-cardinality strict-`D` competitor.

---

## 6. Certificate

Run

`python3 research/verify_target_c_adjacent_cut_triple_small.py`.

It uses exact `Fraction` arithmetic for all fan/backbone constants and the outward rational enclosures `pi<355/113`, `sqrt(3)<17321/10000`.  The exact computed combined constant is below `21175.904`, leaving more than `24` units of room below the advertised `21200`.

**Disposition:** proved proof-only consecutive-cut reduction; theorem-state authority unchanged. C-II and Level I remain open.
