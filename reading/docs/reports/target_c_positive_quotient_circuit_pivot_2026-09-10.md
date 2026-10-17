> Generated reading edition · [exact source](../../../docs/reports/target_c_positive_quotient_circuit_pivot_2026-09-10.md) · source SHA-256 `27b118fa1c1410ac35be38fda7babff65bce68fd605e1a0a575b4285ae5e71c5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6F97B0A134BF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — positive quotient-circuit pivots between extreme KKT stresses

**Date:** 2026-09-10  
**Repository state:** PR #178 after EC/CT/EDB/LI/ENB  
**Run type:** exact oriented-matroid / polytope edge theorem  
**Target:** Target C, C-II extreme-circuit ensemble  
**Depends on:** C65 relative-interior full positive KKT stress, EC extreme-support circuit theorem, CT rank-gap identity  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The remaining high-degeneracy problem is an ensemble problem: one extreme positive
circuit may omit many actual C65 rows, and ESR shows that its internal geometry need
not be weak. The full-support relative-interior KKT stress nevertheless forces a very
rigid local exchange structure among the extreme circuits.

Let `E` be the full actual mixed row set. Use the KKT sign convention, so each actual
contact row is taken with the contact sign and each actual diameter row with the
opposite sign. Write the resulting row vectors as

```math
a_i\in\mathbb R^{2v},\qquad i\in E,
```

and let

```math
\mathcal K:=\{x\in\mathbb R_{>=0}^{E}:\sum_{i\in E}x_i a_i=0\}
```

be the unnormalized nonnegative KKT stress cone. Its normalized section is the ES
polytope `P`.

Fix an extreme ray `c` of `K`, with support `S`. By EC, `S` is an actual rigidity-row
circuit. Put

```math
W:=\operatorname{span}\{a_s:s\in S\},
\qquad
r_S:=\dim W,
```

and let

```math
\kappa:=\operatorname{rank}R-r_S.
```

By CT this is exactly

```math
\boxed{\kappa=z_*-s_Z=2(v-v_*)+\sigma_*.}
\tag{QP.1}
```

The new theorem is an exact circuit pivot.

### Theorem QP — positive quotient-circuit pivot

Assume `kappa>0`. Let `f\in E\setminus S` be any omitted row whose image modulo `W`
is nonzero. Then there exists a set

```math
T\subseteq E\setminus S,
\qquad f\in T,
\qquad 2\le |T|=:t\le\kappa+1,
\tag{QP.2}
```

such that:

1. the images of `T` in the quotient row space `span(E)/W` form a positive vector-matroid circuit;
2. the coordinate face of `K` supported on
   ```math
   U:=S\cup T
   
   ```
   is a two-dimensional pointed cone;
3. its two extreme rays are `c` and a second extreme KKT stress `c'`;
4. `c'` is strictly positive on every row of `T`;
5. if
   ```math
   A:=S\setminus\operatorname{supp}c',
   \qquad a:=|A|,
   
   ```
   then `a>=1`,
   ```math
   \operatorname{supp}c'=(S\setminus A)\cup T,
   \tag{QP.3}
   
   ```
   and its exact rank-gap parameter is
   ```math
   \boxed{\kappa'=\kappa-t+a.}
   \tag{QP.4}
   
   ```

After normalization by `sum_H beta=1`, `c` and `c'` are adjacent vertices of the ES
KKT polytope.

Thus an omitted rank-increasing row can always be switched on by **one edge pivot** in
the actual positive-stress polytope. The only obstruction to decreasing circuit
degeneracy is simultaneous loss of at least as many old circuit rows as the number of
entering quotient-circuit rows.

---

## 1. The omitted rows carry a strictly positive quotient dependence

C65 supplies a relative-interior full-support stress

```math
x^0_i>0\qquad(i\in E),
```

with

```math
\sum_{i\in E}x^0_i a_i=0.
\tag{1.1}
```

Let

```math
\pi:\operatorname{span}(E)\to\operatorname{span}(E)/W
```

be the quotient map and write

```math
\bar a_i:=\pi(a_i).
```

Every selected row in `S` maps to zero. Projecting (1.1) therefore gives

```math
\boxed{
\sum_{i\in E\setminus S}x^0_i\bar a_i=0,
\qquad x^0_i>0.
}
\tag{1.2}
```

The nonzero quotient rows span a space of dimension exactly `kappa`, because adjoining
all omitted rows to `S` restores the full row rank.

Fix an omitted row `f` with `bar a_f!=0`. Equation (1.2) gives a nonnegative quotient
dependence containing `f` with positive coefficient. Choose one with inclusion-minimal
support among such dependences and call that support `T`.

All coefficients on `T` are strictly positive. We next verify that `T` is an ordinary
vector-matroid circuit, not merely a support-minimal positive relation.

Suppose the quotient rows in `T` had dependency nullity at least two. Let
`lambda>0` be the chosen positive dependence. There would exist another quotient
relation `w` linearly independent from `lambda` and, after replacing it by a linear
combination with `lambda` if necessary, satisfying

```math
w_f=0.
```

For one of the two signs of `w`, increase the scalar from zero until some coordinate
other than `f` of

```math
\lambda+tw
```

first reaches zero. The vector stays nonnegative, its `f` coordinate stays positive,
and it is a nonzero quotient dependence on a proper subset of `T`, contradicting
minimality. Therefore the quotient dependency space on `T` is one-dimensional:

```math
\boxed{
\operatorname{rank}\{\bar a_t:t\in T\}=t-1.
}
\tag{1.3}
```

Since all `bar a_t` are nonzero, `t>=2`. Since the quotient dimension is `kappa`,

```math
t-1\le\kappa,
```

which proves the upper bound `t\le kappa+1`.

This also proves the stronger fact that **every nonzero omitted quotient row belongs to
a positive quotient circuit**.

---

## 2. Lift the quotient circuit to a second full stress direction

Choose positive coefficients

```math
\lambda_t>0\qquad(t\in T)
```

such that

```math
\sum_{t\in T}\lambda_t\bar a_t=0.
\tag{2.1}
```

Thus

```math
v_T:=\sum_{t\in T}\lambda_t a_t\in W.
\tag{2.2}
```

Because the rows indexed by `S` span `W`, choose real coefficients `mu_s` satisfying

```math
\sum_{s\in S}\mu_s a_s=-v_T.
\tag{2.3}
```

Define a dependence `d` on `U=S union T` by

```math
d_s=\mu_s\quad(s\in S),
\qquad
d_t=\lambda_t\quad(t\in T).
```

Then

```math
\sum_{u\in U}d_u a_u=0,
\tag{2.4}
```

and every `T` coordinate of `d` is strictly positive.

The circuit stress `c` is strictly positive on every coordinate of `S`. Hence for
sufficiently small `epsilon>0`,

```math
y:=c+\epsilon d
```

satisfies

```math
\boxed{y_u>0\quad\text{for every }u\in U.}
\tag{2.5}
```

Thus the nonnegative stress cone on `U` has a relative-interior full-support point.

---

## 3. The supported stress cone is exactly two-dimensional

Since `S` is a circuit,

```math
|S|=r_S+1.
\tag{3.1}
```

By (1.3), adjoining `T` raises row rank by exactly `t-1`:

```math
\operatorname{rank}R_U=r_S+t-1.
\tag{3.2}
```

Therefore the full signed dependency space on `U` has dimension

```math
\begin{aligned}
|U|-\operatorname{rank}R_U
&=(r_S+1+t)-(r_S+t-1)\\
&=2.
\end{aligned}
\tag{3.3}
```

Let

```math
\mathcal K_U
:=\{x\in\mathcal K:\operatorname{supp}x\subseteq U\}.
```

This is a coordinate face of the full nonnegative stress cone. It is pointed, because
no nonzero vector and its negative can both be coordinatewise nonnegative. Equations
(2.5) and (3.3) show that it is a full-dimensional pointed cone in a two-dimensional
linear space. Hence it has exactly two extreme rays.

One is the original ray `R_+ c`. Indeed, any decomposition of `c` into nonnegative
stresses has zero `T` coordinates term by term, so both summands are supported on
`S`; EC says the stress space on `S` is one-dimensional.

Call the other extreme ray `R_+ c'`.

Because the full-support vector `y` from (2.5) lies in the relative interior of this
2D cone,

```math
y=\alpha c+\beta c'
```

for some `alpha,beta>0`. For every `t\in T`, `c_t=0` while `y_t>0`, so

```math
\boxed{c'_t>0\quad(t\in T).}
\tag{3.4}
```

Thus `T subseteq supp(c')`.

The second ray cannot be positive on every coordinate of `S` as well: then it would
itself lie in the relative interior of `K_U`, not on an extreme ray. Therefore at least
one old coordinate vanishes. Define

```math
A:=S\setminus\operatorname{supp}c'.
```

Then `a=|A|>=1` and QP.3 follows.

Finally, because `K_U` is a face of the full cone, an extreme ray of `K_U` is also an
extreme ray of `K`: if `c'=u+v` with `u,v\in K`, every coordinate outside `U` is zero
in `c'` and hence separately zero in `u,v`, so the decomposition lies inside `K_U`.
Thus EC applies to `c'`: its support is another actual positive rigidity circuit.

---

## 4. Exact degeneracy update

Let

```math
S':=\operatorname{supp}c'=(S\setminus A)\cup T.
```

Since `c'` is a circuit,

```math
\operatorname{rank}R_{S'}=|S'|-1.
```

Using `|S|=r_S+1`,

```math
\begin{aligned}
\operatorname{rank}R_{S'}
&=(|S|-a+t)-1\\
&=r_S+t-a.
\end{aligned}
\tag{4.1}
```

Let

```math
\kappa':=\operatorname{rank}R-\operatorname{rank}R_{S'}.
```

Then

```math
\boxed{
\kappa'
=\kappa-t+a.
}
\tag{4.2}
```

This proves QP.4.

Hence:

- `a<t` strictly decreases the circuit rank gap;
- `a=t` preserves it;
- `a>t` increases it.

The entire failure of a monotone route to a low-degeneracy extreme is therefore
localized to **degenerate pivots that simultaneously turn off at least as many old
circuit rows as they turn on new quotient-circuit rows**.

---

## 5. Adjacency in the normalized KKT polytope

Every nonzero nonnegative KKT dependence has positive total diameter weight. Indeed the
standard virial identity gives

```math
\sum_C\alpha_e=D^2\sum_H\beta_h,
```

so a nonzero nonnegative stress cannot have `sum_H beta=0`.

Therefore each nonzero ray of `K_U` meets the normalization hyperplane

```math
\sum_H\beta_h=1
```

exactly once. The two-dimensional cone face `K_U` becomes a one-dimensional face of
the normalized polytope `P`. Its endpoints are the normalized versions of `c` and
`c'`.

Thus:

```math
\boxed{
\text{the QP pivot joins two adjacent vertices of }\mathcal P.
}
\tag{5.1}
```

This is useful because it turns the extreme-circuit ensemble from an arbitrary
Caratheodory decomposition into the actual one-skeleton of the KKT polytope.

---

## 6. Rank-preserving omitted rows

If an omitted row `f` already lies in `W`, then its quotient image is zero. Set
`T={f}`. Represent `-a_f` by rows of `S` and repeat Sections 2-5. The union
`S union {f}` again has dependency nullity two and yields an adjacent positive extreme
circuit containing `f`.

Here `t=1`, so

```math
\kappa'=\kappa-1+a\ge\kappa
```

because `a>=1`. Thus a row already in the selected span can be switched on by an
adjacent circuit, but such a pivot cannot improve the rank gap.

Combining this with QP gives:

### Corollary QP.1 — every omitted actual row is visible at an adjacent KKT extreme

For every `f\in E\setminus S`, there is a vertex of the normalized KKT polytope
adjacent to `c` whose positive circuit support contains `f`.

For rank-increasing `f`, all entering rows can be chosen as one positive quotient
circuit of size at most `kappa+1`.

---

## 7. Consequence for a minimum-degeneracy extreme

Choose an extreme positive circuit minimizing `kappa` over all vertices of `P`.
Then every QP pivot from it satisfies

```math
\kappa'\ge\kappa.
```

By QP.4,

```math
\boxed{a\ge t}
\tag{7.1}
```

for every positive quotient-circuit pivot.

Thus a minimum-degeneracy extreme has an exact local optimality property:

> every rank-increasing positive bundle of `t` omitted rows that can enter across one
> polytope edge forces at least `t` currently selected circuit rows to disappear at the
> opposite endpoint.

This is much sharper than the previous statement that the full stress is a convex
combination of many circuits. The remaining obstruction is now a simultaneous
zero-ratio degeneracy on actual adjacent pivots.

If one can prove a single QP pivot with `a<t`, then the chosen extreme was not
minimum-degeneracy. Iterating would eventually reach a circuit with smaller `kappa`.
In particular, any geometric theorem forcing `a<t` whenever `kappa` is linear would
produce the low-`kappa` extreme needed by EDB/LI/ENB.

---

## 8. Regressions and no-go information

- ESR does not contradict QP. A high-flex even-shell circuit can be one endpoint of a
  positive pivot once additional full actual rows are supplied; QP deliberately uses
  those omitted rows rather than the shell circuit alone.
- An abstract nonnegative kernel cone can have pivots with `a=t` everywhere, so QP by
  itself does not prove existence of a low-`kappa` extreme. The next theorem must use
  unit-contact/diameter geometry or the mixed rigidity structure.
- No generic-matroid connectivity theorem is used. QP works in the **actual realized
  row configuration**, so it is immune to specialization failures between generic and
  actual rigidity matroids.
- No individual stress-weight lower bound is used.

---

## 9. Exact next target

The high-degeneracy branch has become a finite pivot problem.

> **QP-degeneracy breaker.** Let `c` be a minimum-`kappa` extreme circuit of a C65
> survivor. If `kappa>=epsilon D`, prove that some positive quotient-circuit pivot has
> `a<t`.

A weaker useful statement is enough: find a pivot with

```math
a\le t-\eta t
```

for a fixed `eta>0` on a positive fraction of the rank-increasing quotient directions.
Repeated pivots would then reduce `kappa` to `o(D)` and activate the EDB/LI/ENB
low-degeneracy normal form.

The binding difficulty is now explicit: why should many entering omitted rows fail to
hit the same pivot ratio on at least as many old selected rows? The answer must come
from geometry/topology, not abstract polytope theory.

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let c be an extreme positive KKT circuit with support S and
    kappa=rank(R)-rank(R_S)=z_*-s_Z.
Quotient all omitted signed mixed rows by W=span(S). Full relative-interior positivity
projects to a strictly positive dependence of the omitted quotient rows.

For any omitted f with nonzero quotient image, choose a support-minimal positive
quotient dependence T containing f. Then T is a vector-matroid circuit,
    2 <= t=|T| <= kappa+1,
and rank(T mod W)=t-1.

Lift its positive quotient relation through S. Since c is strictly positive on S,
a small perturbation gives a stress positive on all U=S union T. Also
    nullity(R_U)=2.
Hence the nonnegative stress cone on U is a 2D pointed face with exactly two extreme
rays: c and another positive circuit c'. The second ray is positive on every T row and
drops a nonempty set A subset S. If a=|A|, then
    supp(c')=(S\A) union T,
    kappa'=kappa-t+a.
After beta normalization the two circuits are adjacent vertices of the KKT polytope.
Every omitted actual row is visible at some adjacent extreme; zero-quotient rows use
t=1.

For a minimum-kappa extreme, every rank-increasing pivot therefore obeys
    a >= t.
Next: use unit-contact/diameter geometry to force one pivot with a<t whenever
kappa=Omega(D).
```
