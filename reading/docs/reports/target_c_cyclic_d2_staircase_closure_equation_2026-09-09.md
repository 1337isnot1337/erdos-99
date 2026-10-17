> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_staircase_closure_equation_2026-09-09.md) · source SHA-256 `2d565d167a4532a313a61ec1cd0874e6827a5887d85348506a03ce6b214f169c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-66473733F810","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`: exact two-staircase shell-closure equation

**Date:** 2026-09-09  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact complex/trigonometric reduction  
**Target:** finite closure equation for the SW + D2C normal form  
**Depends on:** SW staircase word theorem; D2C two defect cells; D2 four-block shell order  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

SW encodes each of the two `d_H=2` diameter-tree bodies by a binary staircase word. D2C encodes the two cross-tree switches by scalar gaps `G_1,G_2` and midpoint offsets of size at most `1/(2D)`.

These data satisfy one exact complex closure equation.

### Theorem SCE — two-staircase closure

For one staircase body `X in {A,B}`, let

$$
z^X_t=D e^{i(\theta_X+t\delta)},
\qquad 0\le t\le L_X,
$$

be its oriented diameter vectors in projective direction order, where

$$
L_X=|E(T_X)|-1.
$$

Let

$$
\varepsilon^X_t=
\begin{cases}
-1,&\text{if staircase step }t\text{ advances the first shell block},\\
+1,&\text{if staircase step }t\text{ advances the second shell block}.
\end{cases}
$$

Define the restricted Littlewood sum

$$
\boxed{
P_X:=\sum_{t=0}^{L_X-1}\varepsilon^X_t e^{it\delta}.
}
\tag{SCE.1}

Let the two cross-tree gaps be `G_1,G_2` and put

\[
W_j:=\sqrt{1-D^2\sin^2(G_j/2)}.
\tag{SCE.2}

Then there are signs `sigma_j in {+1,-1}` fixed by the cyclic endpoint labeling such that

\[
\boxed{
\frac{i}{2}e^{i(\theta_A+\delta/2)}P_A
+
\frac{i}{2}e^{i(\theta_B+\delta/2)}P_B
+
\sigma_1W_1e^{i\phi_1}
+
\sigma_2W_2e^{i\phi_2}
=0,
}
\tag{SCE.3}

where `phi_j` is the angular bisector of the two oriented diameter directions adjacent to switch `j`.

Equivalently,

\[
\boxed{
\left|
 e^{i(\theta_A+\delta/2)}P_A
+e^{i(\theta_B+\delta/2)}P_B
\right|
\le\frac{2}{D}.
}
\tag{SCE.4}

The phase separation is exact:

\[
\boxed{
\theta_B-\theta_A=L_A\delta+G_1
}
\tag{SCE.5}

for a suitable lift, and

\[
\boxed{
L_A+L_B=q-4,
\qquad
G_1+G_2=(s+4)\delta,
\qquad
s=q_R-q.
}
\tag{SCE.6}

Thus a true cyclic `d_H=2` survivor requires two binary polynomials evaluated at the same near-`q`th root of unity to cancel to **order `1/D`**, with their relative phase itself constrained by one of the two positive defect cells.

At the SSR/Reinhardt boundary `s_1=s_2=0`, SCE becomes the ordinary exact Reinhardt sign-code closure. A true D2 source is a strict two-cell deformation of that equality.

---

## 1. Diameter vectors in one tree form an arithmetic direction progression

D2S proves that every projectively consecutive pair inside one diameter tree has gap exactly

\[
\delta=2\arcsin\frac1{2D}.
$$

Orient every tree edge from its first color block to its second. All of these oriented directions lie in one projective interval and therefore admit a common lift to ordinary angles. Reversing the block labels if necessary, the direction order is increasing.

Hence the diameter vectors are exactly

$$
\boxed{
z_t=D e^{i(\theta+t\delta)}.}
\tag{1.1}

There are `L+1=|E(T)|` such states and `L` staircase steps.

---

## 2. Every internal shell side is one difference of consecutive diameter vectors

Put

\[
d_t:=z_{t+1}-z_t.
$$

Because

$$
|d_t|=2D\sin(\delta/2)=1,
$$

`d_t` is a unit vector. Explicitly,

$$
\boxed{
d_t=i e^{i(\theta+(t+1/2)\delta)}.}
\tag{2.1}

For a first-block staircase step

\[
u_i v_j\to u_{i+1}v_j,
$$

we have

$$
z_t=v_j-u_i,
\qquad
z_{t+1}=v_j-u_{i+1},
$$

so

$$
\boxed{u_{i+1}-u_i=-d_t.}
\tag{2.2}

For a second-block step

\[
u_i v_j\to u_i v_{j+1},
$$

we obtain

$$
\boxed{v_{j+1}-v_j=d_t.}
\tag{2.3}

Therefore the sum of all internal shell side vectors belonging to the two blocks of this tree is

\[
\sum_t\varepsilon_t d_t
=
 i e^{i(\theta+\delta/2)}
\sum_t\varepsilon_t e^{it\delta}.
$$

This is the first two terms in SCE.3 after summing the two trees.

---

## 3. The same sum is twice the diameter-midpoint displacement

Let `m_t` be the midpoint of the diameter edge represented by `z_t`.

On a first-block step only `u_i` moves, by `-d_t`, so

$$
m_{t+1}-m_t=-\frac12d_t.
$$

On a second-block step only `v_j` moves, by `d_t`, so

$$
m_{t+1}-m_t=\frac12d_t.
$$

Thus

$$
\boxed{
m_L-m_0
=\frac12\sum_t\varepsilon_t d_t
=\frac{i}{2}e^{i(\theta+\delta/2)}P.}
\tag{3.1}

Write these total midpoint displacements as `M_A,M_B` for the two bodies.

---

## 4. One defect cell contributes the sum of its two transition sides

At one cross-tree switch use D2C's labels

\[
AC,
\qquad
BD
$$

for the two disjoint diameter edges. Their endpoints occur cyclically as

$$
A,B,C,D.
$$

The two shell block-transition contacts belonging to this switch are `AB` and `CD`. Let

$$
w=\frac{B+D}{2}-\frac{A+C}{2}
$$

be the midpoint offset.

The oriented shell side vectors are

$$
B-A=w+p,
\qquad
D-C=w-p,
$$

with `p=(u-v)/2` as in D2C. Hence their sum is exactly

$$
\boxed{(B-A)+(D-C)=2w.}
\tag{4.1}

D2C proves

\[
w\perp p,
\qquad
|w|=W=\sqrt{1-D^2\sin^2(G/2)},
$$

and `w` is parallel to the angular bisector vector `r=(u+v)/2`. Therefore

$$
\boxed{w=\sigma W e^{i\phi}}
\tag{4.2}

for a sign `sigma` determined by the endpoint labeling and with `phi` the bisector direction.

There are exactly two switch cells, so the four transition contacts contribute

\[
2w_1+2w_2.
$$

---

## 5. Sum the shell side vectors

The complete force hull is the four-block unit shell

$$
A_0|B_0|A_1|B_1.
$$

Its oriented side vectors consist of

1. the internal block sides of the A staircase;
2. the internal block sides of the B staircase;
3. the four block-transition contacts.

A closed polygon has total side-vector sum zero. Sections 2 and 4 therefore give

$$
2M_A+2M_B+2w_1+2w_2=0.
$$

Divide by two and substitute (3.1) and (4.2). This is exactly SCE.3.

---

## 6. Uniform `1/D` error bound

D2C gives

$$
2\delta<G_j\le\Delta_2.
$$

Since `W(G)` decreases on this interval,

$$
0\le W_j<W(2\delta).
$$

At the DGE equality endpoint, direct evaluation gives

$$
W(2\delta)=\frac1{2D}.
$$

Thus

$$
\boxed{0\le W_j<\frac1{2D}.}
\tag{6.1}

From SCE.3,

\[
\frac12
\left|
 e^{i(\theta_A+\delta/2)}P_A
+e^{i(\theta_B+\delta/2)}P_B
\right|
\le W_1+W_2<\frac1D.
$$

This proves SCE.4 (with a strict finite inequality; the displayed weak form is cleaner).

The important scale is exact: the two staircase Littlewood sums must cancel to boundary error `O(1/D)`, not merely `o(D)`.

---

## 7. Relative phases and counts

The A tree has `L_A+1` projective direction states. After its last state, the first cross-tree gap is `G_1`, then the B direction block begins. Thus

$$
\theta_B-\theta_A=L_A\delta+G_1,
$$

which proves SCE.5.

The total number of within-tree direction gaps is

$$
L_A+L_B=q-4
$$

by D2S. D2C gives the remaining gap sum

$$
G_1+G_2=(s+4)\delta.
$$

This proves SCE.6.

---

## 8. Polynomial form

Set

$$
z=e^{i\delta}.
$$

Then

$$
P_A(z)=\sum_{t=0}^{L_A-1}\varepsilon^A_t z^t,
\qquad
P_B(z)=\sum_{t=0}^{L_B-1}\varepsilon^B_t z^t,
$$

with all coefficients in `{+1,-1}`.

The coefficient words are not arbitrary Littlewood words: SW fixes their numbers of plus and minus signs from the two block sizes, and D2R's caterpillar/staircase interpretation records every sign change as an exact center-switch trapezoid.

After rotating by `e^{-i(theta_A+delta/2)}`, SCE.3 has the form

$$
\boxed{
P_A(z)
+e^{i(L_A\delta+G_1)}P_B(z)
=E,
\qquad
|E|<\frac2D.
}
\tag{8.1}

The error `E` is not arbitrary: it is the explicit sum of two bisector-aligned vectors of lengths `2W_1,2W_2`. But even the norm form is already a strong finite necessary condition.

---

## 9. Relation to Reinhardt sign codes

At the formal SSR boundary

\[
s_1=s_2=0,
\qquad
G_1=G_2=2\delta,
$$

the two missing completion chords become actual diameter states. Inserting those states turns the two staircase direction blocks into one `q`-state Reinhardt diameter cycle, and the shell-side coefficients in (8.1) become the standard signed arithmetic direction code.

Thus SCE is an exact two-defect deformation of the Reinhardt closure equation, not a new unrelated Littlewood problem.

The true D2 condition is

$$
s_1,s_2>0.
$$

The target is to show that no admissible staircase/sign code satisfying the Target C block topology can maintain (8.1) under a strictly positive two-cell deformation.

---

## 10. What remains

SCE does not yet exclude positive defect. General Littlewood sums can be small at points near roots of unity, and the admissible staircase words include long star runs.

The next valid strengthening must use one of the restrictions absent from arbitrary Littlewood theory:

1. the word is a monotone staircase between two convex shell blocks;
2. both trees coexist in the four-block order and every A edge crosses every B edge;
3. the error vector directions are fixed by the two switch bisectors;
4. the same geometry supports the unique positive D2 KKT circuit.

A purely norm-based lower bound for arbitrary Littlewood polynomials is unlikely to be true.

---

## 11. Audit classification

| Claim | Status | Reason |
| --- | --- |
| exact arithmetic diameter vector progression inside one tree | proved | D2S |
| staircase side vector is `plus/minus(z_{t+1}-z_t)` | proved | endpoint update identity |
| block-side sum is a restricted Littlewood sum | proved | section 2 |
| midpoint displacement is half that sum | proved | section 3 |
| transition-pair side sum is `2w` | proved | D2C midpoint coordinates |
| exact shell closure SCE.3 | proved | sum of all oriented shell sides |
| error norm `<2/D` | proved | D2C `W_j<1/(2D)` |
| positive-defect impossibility | open | requires staircase/convexity/KKT input beyond arbitrary Littlewood sums |
| Level I | still open | SCE has not been solved |
