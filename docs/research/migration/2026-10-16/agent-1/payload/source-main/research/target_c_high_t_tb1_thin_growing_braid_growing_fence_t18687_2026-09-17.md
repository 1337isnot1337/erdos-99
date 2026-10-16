# Target C-II - the THIN growing braid admits a growing two-sided fixed train fence

**Date:** 2026-09-17  
**Status:** proof-only continuation of the growing-braid fixed-bracket theorem; no canonical promotion claimed  
**Scope:** THIN side of the 15-spaced one-sign strong-TB1 Horn upper family through `t=(q-k)/D<=1.8687`  
**Dependencies:** THIN growing-braid common spine; growing-braid fixed-bracket theorem; low-defect rich-row purification; triangle-free complete-train crossing graph  
**Certificate:** `research/verify_target_c_high_t_tb1_thin_growing_braid_growing_fence_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The fixed-bracket theorem synchronizes one left-flank train and one right-flank train across a growing THIN braid. The same double count can retain an arbitrary fixed number of trains on each flank, and then be diagonalized in the number of retained trains as well as in the braid width.

Thus the THIN branch contains, simultaneously,

```text
r_D -> infinity vertex-disjoint THIN almost-diameters,
all pairwise properly crossing;

s_D -> infinity fixed complete trains on the left flank;
s_D -> infinity fixed complete trains on the right flank;
all 2 s_D fixed trains pairwise noncrossing;

D^(1-o(1)) common selected rows;
one inverse-D row phase;
every braid chord crosses every retained row;
every fixed train crosses every retained row;
every left-train crossing lies below -0.01D;
every right-train crossing lies above +0.01D.
```

The braid chords still share one consecutive exact selected-cut support block of length `D^(1-o(1))`. The train fence is asserted on the retained near-linear row family, not on every row of that consecutive support block.

This turns the two fixed bracket trains into a growing fixed train fence. In particular the surviving THIN geometry contains a genuinely two-dimensional complete train grid of growing width and near-linear height, while an independently growing straight-line superdiameter braid crosses every row of that grid.

---

## 1. Uniform row inputs

Retain the notation of the fixed-bracket theorem. Put

\[
\gamma={791\over9{,}600{,}000{,}000},
\qquad
N:=|T_D|>\left({\gamma\over16}-o(1)\right)D,
\tag{GF.1}
\]

\[
p_0={1609\over2500}=0.6436,
\qquad
T_*={6121\over2000}=3.0605,
\tag{GF.2}
\]

and at `mu=0.01`

\[
q_0:=p_0-{1.02\over\sqrt3}
=0.05470272542658\ldots .
\tag{GF.3}
\]

There is a low-defect rich-row family `R_D` such that, uniformly for `a in R_D`,

\[
|R_D|>\left({3\over2}-o(1)\right)N,
\tag{GF.4}
\]

\[
|B_a|>\left({1\over5}-o(1)\right)N,
\tag{GF.5}
\]

and the THIN blocker graph on `a` has

\[
\Delta(B_a)=O(D^{3/4})=o(N).
\tag{GF.6}
\]

The purified train family `P_a` has two flank subfamilies

\[
P_a^-:=\{b:h_a(z_{a,b})<-0.01D\},
\qquad
P_a^+:=\{b:h_a(z_{a,b})>+0.01D\},
\tag{GF.7}
\]

with

\[
|P_a^-|,|P_a^+|>(q_0-o(1))D.
\tag{GF.8}
\]

Every train in either flank crosses `a` in a purified rhombus at angle `pi/3+O(D^-1)`. The total number of complete trains in the source is at most

\[
(T_*+o(1))D.
\tag{GF.9}
\]

For fixed `r`, the number `M_r(a)` of `r`-edge matchings in `B_a` satisfies

\[
M_r(a)>
\left({1\over r!5^r}-o(1)\right)N^r.
\tag{GF.10}
\]

Every such matching is a pairwise-properly-crossing THIN braid.

---

## 2. Fixed braid width and fixed fence width

Fix positive integers `r,s`. Count quintuples

\[
(a,F,L,R)
\tag{GF.11}
\]

where

- `a in R_D`;
- `F` is an `r`-edge matching in `B_a`;
- `L` is an `s`-element subset of `P_a^-`;
- `R` is an `s`-element subset of `P_a^+`.

For fixed `s`, (GF.8) gives

\[
{ |P_a^-|\choose s},
{ |P_a^+|\choose s}
>
\left({q_0^s\over s!}-o(1)\right)D^s.
\tag{GF.12}
\]

Hence (GF.4), (GF.10), and (GF.12) give

\[
\#\{(a,F,L,R)\}
>
\left(
{3q_0^{2s}\over2r!(s!)^2 5^r}-o(1)
\right)
N^{r+1}D^{2s}.
\tag{GF.13}
\]

There are at most

\[
{N\choose r}\le {N^r\over r!}
\tag{GF.14}
\]

possible blocker `r`-sets. There are at most

\[
{(T_*+o(1))D\choose s}^2
\le
\left(
{T_*^{2s}\over(s!)^2}+o(1)
\right)D^{2s}
\tag{GF.15}
\]

ordered pairs of global train `s`-sets.

Pigeonhole therefore produces one fixed braid `F_*`, one fixed left train set `L_*`, and one fixed right train set `R_*` occurring together on more than

\[
\left(
{3\over2\,5^r}
\left({q_0\over T_*}\right)^{2s}
-o(1)
\right)N
\tag{GF.16}
\]

rows.

Relative to any one fixed train in `L_*`, those rows have only two possible projective phase signs. Retain the larger sign class. We obtain `A_D(r,s)` with

\[
\boxed{
|A_D(r,s)|>
\left(
{3\over4\,5^r}
\left({q_0\over T_*}\right)^{2s}
-o(1)
\right)N.
}
\tag{GF.17}
\]

For every row `a in A_D(r,s)`:

\[
h_a(z_{a,b})<-0.01D
\qquad(b\in L_*),
\tag{GF.18}
\]

\[
h_a(z_{a,b})>+0.01D
\qquad(b\in R_*).
\tag{GF.19}
\]

Every chord of `F_*` crosses every such row, and all rows have one projective phase to `O(D^-1)`.

---

## 3. The fixed train fence is pairwise noncrossing and has one common order

Take two distinct trains `b,c in L_* union R_*`. Both cross every retained row. If `b` and `c` crossed each other, then `b,c` together with any retained row would form a triangle in the complete-train crossing graph. That graph is triangle-free. Therefore

\[
\boxed{
L_*\cup R_*\text{ is pairwise noncrossing.}
}
\tag{GF.20}
\]

The retained rows are also pairwise noncrossing, while every row crosses every train in `L_* union R_*`. The standard two-shore order lemma therefore gives one train order common to all retained rows, up to global reversal.

Because every left crossing has `h<-0.01D` and every right crossing has `h>+0.01D`, every left train precedes every right train in the orientation used by (GF.18)-(GF.19). Thus the fixed train fence has the same two-block order on every retained row:

\[
\boxed{
L_*\quad\text{then}\quad R_*.
}
\tag{GF.21}
\]

Within either block, consecutive selected crossing centers have row-normal separation greater than `sqrt(3)/2`. Hence each flank block itself has row-normal span more than

\[
{\sqrt3\over2}(s-1).
\tag{GF.22}
\]

The total fence spans the `+-0.01D` corridor on every retained row.

---

## 4. Simultaneously growing braid and fence

The fixed-parameter theorem can be diagonalized in both parameters.

Let `epsilon_D->0` dominate all uniform asymptotic errors in (GF.1)-(GF.10), and put

\[
\Delta_D:=\max_{a\in R_D}\Delta(B_a)=O(D^{3/4}).
\]

Choose integers `k_D->infinity` sufficiently slowly that

\[
k_D\epsilon_D\to0,
\qquad
{k_D^2\Delta_D\over N}\to0,
\qquad
{k_D^2\over D}\to0,
\qquad
{k_D\over\log D}\to0.
\tag{GF.23}
\]

Set

\[
r_D=s_D=k_D.
\tag{GF.24}
\]

The first two conditions make the growing matching estimate uniform; the third makes the falling-factorial estimates for both train flanks uniform. Repeating the count from Section 2 gives fixed objects

\[
F_D,\qquad L_D,\qquad R_D^{+}
\]

with

\[
|F_D|=|L_D|=|R_D^{+}|=k_D\to\infty,
\tag{GF.25}
\]

and a common row family `A_D` satisfying

\[
|A_D|>
\left({3\over4}-o(1)\right)
{N\over
5^{k_D}(T_*/q_0)^{2k_D}}.
\tag{GF.26}
\]

Put

\[
C_*:=5\left({T_*\over q_0}\right)^2
=15650.8108585\ldots .
\tag{GF.27}
\]

Then

\[
|A_D|>
\left({3\over4}-o(1)\right){N\over C_*^{k_D}}.
\tag{GF.28}
\]

Since `N=Theta(D)` and `k_D=o(log D)`,

\[
C_*^{k_D}=D^{o(1)},
\]

so

\[
\boxed{|A_D|=D^{1-o(1)}.}
\tag{GF.29}
\]

This proves the simultaneous growing-braid/growing-fence normal form.

---

## 5. Common braid support survives the stronger extraction

Every row in `A_D` belongs to the exact selected-cut support interval of every braid chord in `F_D`. If

\[
a_-:=\min A_D,
\qquad
a_+:=\max A_D,
\]

then every braid chord supports the entire consecutive block

\[
\{a_-,a_-+1,\ldots,a_+\}.
\tag{GF.30}
\]

Its length is at least `|A_D|=D^(1-o(1))`. Therefore

\[
\boxed{
\text{all }k_D\text{ braid chords share one consecutive support block of }D^{1-o(1)}\text{ rows.}
}
\tag{GF.31}
\]

Again, no interval assertion is made for the fixed train fence outside the selected row family `A_D`.

---

## 6. Phase-pure subfences

All retained rows have one common projective row phase to `O(D^-1)`. Every fixed fence train crosses every retained row at angle `pi/3+O(D^-1)`. Relative to the common row phase, each fixed train therefore has one of two projective column-phase signs.

Split `L_D` by these two signs and keep the larger class; do the same independently to `R_D^{+}`. This leaves subfences

\[
L_D',\qquad R_D'
\]

with

\[
|L_D'|,|R_D'|\ge {k_D\over2}\to\infty.
\tag{GF.32}
\]

Each subfence has projective phase spread `O(D^-1)`. The left and right surviving signs may be equal or opposite. Thus the final train geometry has only two cases:

1. the two growing flank bundles are in the same inverse-`D` column phase;
2. the two growing flank bundles occupy the two opposite `+-pi/3` column phases relative to the common row phase.

This is a finite phase dichotomy, not a row-dependent choice.

---

## 7. Frontier effect

The rowwise dense train families are no longer needed merely as a reservoir from which one or two persistent trains are extracted. A growing number of fixed trains can be made persistent on each side of the circumcenter corridor while the blocker braid also grows.

The surviving THIN object is now

```text
k_D -> infinity pairwise-crossing THIN hull chords;
all k_D chords cross D^(1-o(1)) common rows;
all chord support intervals share a D^(1-o(1)) consecutive block;

k_D fixed left-flank complete trains;
k_D fixed right-flank complete trains;
all 2 k_D trains pairwise noncrossing and in one common order;
all fixed trains cross every retained row;
left crossings are always below -0.01D;
right crossings are always above +0.01D;

D^(1-o(1)) retained rows in one inverse-D phase;
after phase thinning, both flank bundles still have unbounded size and each bundle has inverse-D column phase.
```

The remaining THIN closure problem is consequently an incidence/order problem between two growing structures of opposite type: a straight-line convex-hull crossing braid and a pairwise-noncrossing complete-train fence, both spanning the same near-linear ordered row stack. A successful next step must force the braid to cross the fence in an impossible order, or use the metric `+-0.01D` separation and near-equilateral row/column phases to obtain a strict diameter descent.

**Disposition:** upgraded the fixed two-train circumcenter bracket to two growing fixed train flank bundles while retaining a simultaneously growing pairwise-crossing THIN braid and `D^(1-o(1))` common phase-pure rows. C-II and Level I remain open.
