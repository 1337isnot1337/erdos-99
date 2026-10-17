> Generated reading edition · [exact source](../../../../docs/targets/target-c/63-loaded-hull-slack-audit.md) · source SHA-256 `1cd190adfdc04aa454ac42c25e6ba85214342617e55f1e57dc793fd420342480`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — loaded-hull slack audit

This module upgrades the loaded-loaded contact bound after Sections 61–62. The proof is
an exact outer-walk argument on the actual force hull; it does not use the rejected
cyclic cap theorem, a KKT weight floor, or any removal of contact-isolated source
points.

**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

---

# 63. Exact loaded-hull slack and primitive boundary split

Retain the canonical post-ZF notation:

- `B={b_1,...,b_q}` is the loaded force-hull vertex set in cyclic order;
- `e_BB` is the number of unit contacts with both endpoints in `B`;
- `b` is the outer contact-face boundary-walk length, with multiplicity;
- `x_B=b-q`;
- `Q` is the bounded nonquadrilateral face excess;
- `d_H=q-h`;
- `s_Z=e+h-(2v-2)`;
- `k=d_H+s_Z`;
- `c_I` is the number of unloaded positive-contact components; and
- `s_C` is their total extra pinned-contact left-nullity.

Section 61 gives the exact defect identity

```math
2h-q=x_B+Q+2s_Z,
```

which is equivalent to

```math
\boxed{q-x_B=Q+2k.}
\tag{63.1}
```

The main theorem below strengthens Section 62's `e_BB>=k` to

```math
\boxed{e_{BB}\ge Q+2k.}
\tag{63.2}
```

More precisely, there are explicit nonnegative integer slacks `u_B,c_B` such that

```math
\boxed{e_{BB}=Q+2k+u_B+c_B.}
\tag{63.3}
```

## 63.1 Outer-walk intervals between loaded hull vertices

Write

```math
s_i:=|b_i-b_{i+1}|
```

with cyclic indices. Since the source is unit-separated,

```math
s_i\ge1.
\tag{63.4}
```

Choose the distinguished exterior occurrences of the loaded vertices on one cyclic
pass of the outer contact-face boundary walk. They occur in force-hull cyclic order.
Let

```math
W_i:b_i\leadsto b_{i+1}
```

be the corresponding outer-walk subpath, and let `ell_i` be its number of unit-contact
edge occurrences. The subpaths partition that cyclic outer walk, so

```math
\sum_i\ell_i=b=q+x_B.
\tag{63.5}
```

Each `W_i` is a polygonal path of unit edges joining endpoints at Euclidean distance
`s_i`. Therefore

```math
\ell_i\ge s_i,
\qquad
\ell_i\in\mathbb Z_{\ge1}.
\tag{63.6}
```

Subtracting `q` from (63.5) gives the exact integer identity

```math
\boxed{x_B=\sum_i(\ell_i-1).}
\tag{63.7}
```

This argument permits bridge excursions and repeated articulation vertices: they are
already counted with multiplicity in the outer walk.

## 63.2 Nonunit hull sides versus direct loaded contacts

Let

```math
m:=|\{i:s_i>1\}|.
\tag{63.8}
```

If `s_i>1`, (63.6) and integrality imply `ell_i>=2`, so each such interval contributes
at least one to (63.7). Hence

```math
\boxed{m\le x_B.}
\tag{63.9}
```

For every other index, `s_i=1`. Thus the two consecutive loaded hull vertices
`b_i,b_{i+1}` are themselves at unit distance, so their hull side is an actual
loaded-loaded contact. The `q-m` such sides are distinct. Therefore

```math
\boxed{e_{BB}\ge q-m\ge q-x_B.}
\tag{63.10}
```

Using (63.1) proves (63.2).

Define the two exact nonnegative integer slacks

```math
\boxed{u_B:=x_B-m\ge0,}
\qquad
\boxed{c_B:=e_{BB}-(q-m)\ge0.}
\tag{63.11}
```

Here `u_B` measures outer-walk excess beyond the one mandatory excess occurrence for
each nonunit hull side. The count `c_B` consists of loaded-loaded contacts beyond the
unit sides of the loaded convex polygon; geometrically these are additional straight
contact chords between nonconsecutive loaded vertices.

Now

```math
\begin{aligned}
e_{BB}
&=q-m+c_B\\
&=(q-x_B)+(x_B-m)+c_B\\
&=Q+2k+u_B+c_B.
\end{aligned}
```

This proves (63.3).

## 63.3 Exact primitive boundary dichotomy

Equation (63.10) gives

```math
\boxed{e_{BB}+x_B\ge q.}
\tag{63.12}
```

Hence

```math
\boxed{\max\{e_{BB},x_B\}\ge q/2.}
\tag{63.13}
```

The canonical difference-body theorem gives

```math
\liminf {h\over D}\ge2\rho,
\qquad
\rho=\cos\rho=0.739085\ldots,
```

and `q>=h`. Therefore every unbounded post-ZF survivor sequence satisfies

```math
\boxed{
\liminf {1\over D}\max\{e_{BB},x_B\}\ge\rho.
}
\tag{63.14}
```

This is a split between two directly geometric currencies: either linearly many unit
contacts join loaded convex-hull vertices, or the outer contact-face walk has linearly
many excess unit-edge occurrences beyond the loaded hull population.

## 63.4 Exact metric decomposition of `x_B`

Let

```math
P_F:=\operatorname{per}(F)=\sum_i s_i.
```

Because `s_i>=1`,

```math
P_F-q\ge0.
```

Because every outer-walk subpath has length `ell_i` and chord length `s_i`,

```math
b-P_F=\sum_i(\ell_i-s_i)\ge0.
```

Thus

```math
\boxed{x_B=(P_F-q)+(b-P_F),}
\tag{63.15}
```

with both terms nonnegative. No assertion that either term is `o(D)` is made; those
are precisely among the cyclic cap consequences rejected by the independent audit.

## 63.5 Outerplanar cap on loaded-loaded contacts

The straight-line graph on the `q` loaded convex vertices whose edges are the
`e_BB` unit contacts is planar and triangle-free. Add the `m` missing convex-hull
sides. The augmented graph contains the full convex `q`-cycle, so it is 2-connected,
with

```math
E'=e_{BB}+m
```

edges and outer-face length `q`.

Let `t` be the number of bounded triangular faces. Every such triangle must use at
least one added hull side: otherwise all three edges were original unit contacts and
would form a forbidden unit equilateral triangle. Each added hull side borders at
most one bounded face, hence

```math
t\le m.
\tag{63.16}
```

Euler gives `F_b=E'-q+1` bounded faces. Face incidence yields

```math
\begin{aligned}
2E'
&=q+\sum_{G\text{ bounded}}\deg G\\
&\ge q+3t+4(F_b-t)\\
&=q+4F_b-t\\
&\ge q+4(E'-q+1)-m.
\end{aligned}
```

Therefore

```math
\boxed{2e_{BB}+m\le3q-4.}
\tag{63.17}
```

In terms of the extra loaded chord count,

```math
\boxed{2c_B\le q+m-4.}
\tag{63.18}
```

This does not close either primitive branch, but it constrains how the loaded-contact
slack in (63.3) can be stored.

## 63.6 Exact coupling to the pinned ledger

The canonical post-ZF pinned ledger is

```math
\boxed{c_I+e_{BB}+s_C=q-2+k.}
\tag{63.19}
```

Using

```math
q=m+u_B+Q+2k,
\qquad
e_{BB}=u_B+Q+2k+c_B,
```

all `u_B` and `Q` terms cancel from (63.19), giving the exact integer identity

```math
\boxed{c_I+s_C+c_B=m+k-2.}
\tag{63.20}
```

Thus a large topology defect cannot coexist with few nonunit hull sides, little pinned
stress, few unloaded components, and few extra loaded chords simultaneously.

More importantly, eliminate `e_BB` directly from the canonical renormalized surplus:

```math
\begin{aligned}
e_{BB}+2s_C-3k
&=(q-2+k-c_I-s_C)+2s_C-3k\\
&=q-2-2k+s_C-c_I\\
&=x_B+Q+s_C-c_I-2,
\end{aligned}
```

where the last line uses (63.1). Hence

```math
\boxed{
e_{BB}+2s_C-3(d_H+s_Z)
=x_B+Q+s_C-c_I-2.
}
\tag{63.21}
```

This identity is exact, finite, and branch-independent.

The canonical all-phase theorem `C-MU-09604` therefore has the equivalent geometric
form

```math
\boxed{
\liminf_{D\to\infty}
{x_B+Q+s_C-c_I\over D}
\ge z_*>0.9604.
}
\tag{63.22}
```

The endpoint `z_*` is already excluded by the canonical theorem. Section 63 does not
need a new transcendental certificate; it only identifies the exact currency on which
that theorem acts.

## 63.7 Strengthening Section 62's retained-contact payment

Section 62 proved only `e_BB>=k`. Equation (63.3) gives the sharper exact payment

```math
\boxed{e_{BB}\ge Q+2k.}
\tag{63.23}
```

Combining this with

```math
e_{BB}+2s_C\ge3k+\mu_DD
```

gives

```math
2(e_{BB}+s_C)
=(e_{BB}+2s_C)+e_{BB}
\ge Q+5k+\mu_DD.
```

Consequently

```math
\boxed{
\liminf
{e_{BB}+s_C-\frac52(d_H+s_Z)-\frac12Q\over D}
\ge {z_*\over2}>0.4802.
}
\tag{63.24}
```

The main value of (63.23), however, is structural rather than the numerical half-factor:
exceptional-face defect and Woodall/mixed defect are already paid by actual unit
contacts among loaded hull vertices before any pinned-stress currency is invoked.

## 63.8 Equality and near-equality structure

Equality in (63.12) means `u_B=c_B=0`. Then

1. every nonunit loaded hull side has an outer-walk replacement of exactly two unit
   contact-edge occurrences;
2. every unit loaded hull side is the corresponding direct loaded-loaded contact; and
3. there are no additional loaded-loaded contact chords.

Thus the outer contact boundary is obtained from the loaded convex polygon by replacing
exactly `x_B` nonunit sides by two-edge unit detours and leaving every other side as a
unit contact.

Any simple intermediate vertex in one of those two-edge detours is unloaded. In the
fully visible C-II core, canonical C26 forbids such a vertex from having total contact
degree one or two, so it must participate in additional contact structure. Bridge and
articulation repetitions instead increase `u_B`. This gives a concrete stability
problem in the high-`x_B` branch.

## 63.9 Scope and regressions

- **Regular odd shell:** `m=x_B=u_B=c_B=0` and `e_BB=q`; all exact identities hold.
- **Unit square:** likewise `e_BB=q=4`, `x_B=0`.
- **A shallow two-edge detour:** allowed. A nonunit hull side can be replaced by two
  unit edges with arbitrarily small geometric area; Section 63 charges one integer unit
  of `x_B` but asserts no uniform area gap.
- **Bridge excursions:** retained. Repeated outer-walk occurrences increase `u_B`.
- **Positive `s_Z`:** retained through `k=d_H+s_Z`.
- **Contact-isolated source points:** retained; the theorem concerns the force-visible
  contact core and never identifies `q` or `v` with the full source population `n`.
- **Rejected cyclic cap consequences:** not used. In particular (63.15) does not set
  either `P_F-q` or `b-P_F` to `o(D)`.
- **KKT coefficient floors:** not used.

## 63.10 Remaining obstruction

Sections 61–63 now force three simultaneous facts in every large post-ZF survivor:

1. `2h-q >= (c_*-o(1))D`, with `c_*>0.6099`;
2. `e_BB >= Q+2(d_H+s_Z)` exactly; and
3. `max(e_BB,x_B) >= (rho-o(1))D`, with `rho=cos rho`.

The renormalized surplus is exactly the outer/face/pinned-component currency
`x_B+Q+s_C-c_I-2`, not an opaque loaded-contact expression.

The remaining proof should therefore split geometrically:

- **high `e_BB`:** couple a linear family of unit contacts on loaded convex-hull
  vertices to the Woodall diameter thrackle and the unique common 2-edge-connected
  contact block;
- **high `x_B`:** convert linearly many outer-walk excess occurrences into either
  linearly many forced interior attachments/contact-degree events or a bridge/articulation
  structure incompatible with the common-block/negative-transfer theorem.

Pure scalar ledger optimization has little left to extract from these currencies.
