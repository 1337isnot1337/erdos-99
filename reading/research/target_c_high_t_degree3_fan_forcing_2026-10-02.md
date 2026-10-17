> Generated reading edition · [exact source](../../research/target_c_high_t_degree3_fan_forcing_2026-10-02.md) · source SHA-256 `8d05ca776d97f6047192f9b0942363a520d7f17c867ca3b4538046376b2caae9`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "0e242106a89e7ade4c2665d1e39179ae470584d8", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_degree3_fan_forcing_2026-10-02.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "35600be9440487d1e8762d977ac7e0be54d4e0c7268512c5acc36b36270194fb"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: high-t face capacity forces a massive degree-three fan population

**Date:** 2026-10-02  
**Base main:** \`9b8edd43260d6921babf9d9b2293ce8c4b7410b1\`  
**Status:** proof-only composition in the canonical full-core/no-macroscopic-container Type-II branch. C-II and Level I remain open.

## 1. Result

Work in the modern full-core Type-II staircase with

```math
t_D:={q-k\over D},
\qquad k=d_H+s_Z,
```

and also in the low-outer-walk, square-root-diameter-matching regime

```math
\nu(H)=O(\sqrt D),
\qquad
x_B=O(\sqrt D).
\tag{1}
```

Let $`I`$ be the internal good-fan population from the current leaf-fan theorem, split as

```math
I=U+T,
```

where $`U`$ counts contact-degree-two internal fan vertices and $`T`$ counts
contact-degree-three internal fan vertices.

The current exact fan-face theorem gives

```math
U\le 2x_B+Q+4.
\tag{2}
```

The high-$`t`$ outer-face identity and near-disk perimeter bound give

```math
Q\le 2t_DD-\operatorname{per}(F).
\tag{3}
```

The new conclusion is the finite inequality

```math
\boxed{
T
\ge
2\operatorname{per}(F)-2t_DD-5\nu(H)-5x_B-4.
}
\tag{4}
```

Since Type II gives

```math
{\operatorname{per}(F)\over D}\to\pi,
```

(4) yields

```math
\boxed{
T\ge\bigl(2\pi-2t_D-o(1)\bigr)D.
}
\tag{5}
```

Therefore for every fixed $`T_0<\pi`$,

```math
t_D\le T_0+o(1)
\quad\Longrightarrow\quad
\boxed{
T\ge\bigl(2(\pi-T_0)-o(1)\bigr)D.
}
\tag{6}
```

At the widest current high-$`t`$ endpoint $`T_0=1.860`$,

```math
\boxed{
T>
(2.5631853071\ldots-o(1))D.
}
\tag{7}
```

Thus the modern high-$`t`$ low-$`x_B`$ square-root branch is not genuinely a
degree-two/degree-three fork.  More than $`2.56D`$ internal exact
$`(D,D,1)`$-fan vertices are forced to use a third positive unit contact.

## 2. Proof of the finite inequality

The current global good-fan theorem gives

```math
I\ge h-4\nu(H)-2x_B.
\tag{8}
```

The matching/currency theorem gives

```math
d_H=q-h\le\nu(H),
```

so

```math
h\ge q-\nu(H).
\tag{9}
```

Section 63 gives the nonnegative outer-walk split

```math
x_B=(\operatorname{per}(F)-q)
+(b_{\rm out}-\operatorname{per}(F)).
```

Hence

```math
q\ge\operatorname{per}(F)-x_B.
\tag{10}
```

Combining (8)--(10),

```math
\boxed{
I\ge
\operatorname{per}(F)-5\nu(H)-3x_B.
}
\tag{11}
```

Now use the exact loaded-hull face identity

```math
b_{\rm out}+Q=2(q-k)=2t_DD.
\tag{12}
```

Since

```math
b_{\rm out}\ge\operatorname{per}(F),
```

we obtain (3):

```math
Q\le2t_DD-\operatorname{per}(F).
```

Insert this into the current exact face payment (2):

```math
U
\le
2x_B+2t_DD-\operatorname{per}(F)+4.
\tag{13}
```

Finally $`T=I-U`$.  Subtract (13) from (11):

```math
T
\ge
2\operatorname{per}(F)-2t_DD
-5\nu(H)-5x_B-4.
\tag{14}
```

Thus (4) is the exact finite estimate needed here.

Under (1), divide by $`D`$ and use
$`\operatorname{per}(F)/D\to\pi`$ to obtain (5)--(7).

## 3. Deep diameter-inactive third-contact ports

Every degree-three fan vertex $`p`$ has a third positive unit contact $`pz(p)`$.
The current inward-spoke theorem and inactivity theorem give

```math
\deg_H(z(p))=0.
```

The global unit-contact degree bound implies that one source vertex can be the
third neighbor of at most five such fan vertices.  Therefore the number $`Z`$ of
distinct third-contact ports satisfies

```math
\boxed{
Z\ge {T\over5}.
}
\tag{16}
```

The current deep-layer theorem proves that fewer than $`15x_B`$ source points of

```math
A\cap(F\setminus B)
```

lie at loaded-hull depth $`<\sqrt3/2`$.  All the ports in (16) lie in this set.
Hence

```math
\boxed{
Z_{\rm deep}
\ge {T\over5}-15x_B.
}
\tag{17}
```

Combining (5) with $`x_B=O(\sqrt D)`$,

```math
\boxed{
Z_{\rm deep}
\ge
\left({2(\pi-t_D)\over5}-o(1)\right)D.
}
\tag{18}
```

Every such deep port satisfies the full-source diameter margin

```math
|z-y|\le D-{\sqrt3\over2}
\qquad(y\in A).
\tag{19}
```

At $`t_D\le1.860+o(1)`$,

```math
\boxed{
Z_{\rm deep}
>
(0.5126370614\ldots-o(1))D.
}
\tag{20}
```

So more than half a diameter unit of distinct source vertices is simultaneously

- nonisolated in the positive contact graph;
- inactive in the full actual-diameter graph;
- at depth at least $`\sqrt3/2`$ inside the loaded hull; and
- protected from every global diameter constraint by the same fixed margin.

## 4. Loaded-to-unloaded attachment incidence

For every degree-three fan vertex $`p`$, its third contact enters one unloaded
positive-contact component.  Different fan vertices give distinct
loaded-to-unloaded contact edges.  Thus

```math
\boxed{
e_{BI}\ge T.
}
\tag{21}
```

Consequently,

```math
\boxed{
e_{BI}
\ge
\bigl(2\pi-2t_D-o(1)\bigr)D.
}
\tag{22}
```

At $`t_D\le1.860+o(1)`$,

```math
\boxed{
e_{BI}>
(2.5631853071\ldots-o(1))D.
}
\tag{23}
```

This consumes more than $`81\%`$ of the asymptotic loaded-terminal population
$`q\sim\pi D`$ as distinct third-contact incidences.

## 5. Consequence for the extra loaded-loaded / loaded-degree slack

Retain the exact near-circle currencies

```math
E_{BB}:=e_{BB}-(q-x_B)\ge0,
```

and

```math
s_B:=3q-e_{BI}-2e_{BB}\ge0.
```

Then

```math
e_{BI}
=
q+2x_B-2E_{BB}-s_B.
\tag{24}
```

Low $`x_B`$ and Type II give $`q=(\pi+o(1))D`$.  Combine (22) and (24):

```math
\boxed{
2E_{BB}+s_B
\le
\bigl(2t_D-\pi+o(1)\bigr)D.
}
\tag{25}
```

At $`t_D\le1.860+o(1)`$,

```math
2E_{BB}+s_B
<
(0.5784073464\ldots+o(1))D.
\tag{26}
```

Thus the same small scalar that caps the global exceptional-face defect also caps
the combined extra loaded-loaded contact population and unused loaded degree.

This is a fan-driven consequence; it is not obtained by simply reusing the
high-$`t`$ $`Q`$-bound.

## 6. Pinned-stress concentration

Canonical full-core component deatomization gives

```math
c_I=O(D^{2/3})=o(D).
\tag{27}
```

Loaded-chord elimination gives, with $`m_B\le x_B`$,

```math
c_I+s_C=m_B+k-2.
\tag{28}
```

Since $`x_B=o(D)`$, (27)--(28) give

```math
s_C=k+o(D).
\tag{29}
```

Also $`q/D\to\pi`$, so from $`t_D=(q-k)/D`$,

```math
{k\over D}=\pi-t_D+o(1).
```

Therefore

```math
\boxed{
s_C=(\pi-t_D+o(1))D.
}
\tag{30}
```

At $`t_D\le1.860+o(1)`$,

```math
\boxed{
s_C>
(1.2815926535\ldots-o(1))D.
}
\tag{31}
```

Equation (30) is a known full-core ledger consequence; the new information is that
the same branch now simultaneously forces (7), (20), and (23).  Thus the large
pinned-stress surplus cannot live on a sparse or diffuse boundary model: it coexists
with a $`2.56D`$-scale family of exact degree-three fan terminals and a
$`0.51D`$-scale family of deep diameter-inactive ports.

## 7. Unconditional component concentration

The $`T`$ degree-three fan leaves are $`T`$ distinct loaded attachment incidences
distributed among the $`c_I`$ unloaded components.  Since $`T>0`$, here $`c_I>0`$.
Canonical component deatomization gives

```math
c_I=O(D^{2/3}).
```

Therefore some unloaded component $`I_*`$ has at least

```math
\boxed{
\Omega(D^{1/3})
}
\tag{32}
```

distinct degree-three fan leaves in its loaded attachment set $`A_*`$.  This
concentration is unconditional; it does not depend on the off-carrier/large-cell
fork below.

There is a geometric consequence.  Every loaded actual-diameter endpoint is a strict
extreme point of the force hull.  Hence every selected subset of $`A_*\subseteq B`$
remains in convex position.  If $`r_*`$ of the attachments are the distinct fan
leaves above, the polygon $`\operatorname{conv}(A_*)`$ has at least $`r_*`$ sides
between source vertices, each of length at least one.  Thus

```math
\operatorname{per}(\operatorname{conv}(A_*))\ge r_*.
```

Cauchy's diameter-perimeter inequality gives

```math
\operatorname{per}(\operatorname{conv}(A_*))
\le
\pi\,\operatorname{diam}(\operatorname{conv}(A_*)).
```

Consequently

```math
\boxed{
\operatorname{diam}(\operatorname{conv}(A_*))
\ge {r_*\over\pi}
=
\Omega(D^{1/3}).
}
\tag{33}
```

So every high-$`t`$ hard sequence contains one actual harmonic attachment cell that
simultaneously has an unbounded fan-port population and unbounded Euclidean diameter.

## 8. Harmonic-return fork with explicit high-t constants

Apply the current fan-port harmonic-return theorem to the $`T`$ degree-three fan
attachments.

For one such fan leaf $`p`$, let $`a`$ be its diameter carrier and $`I_r`$ the
unloaded component reached by the third contact.  The theorem supplies another
loaded attachment $`b\in A_r\setminus\{p\}`$ satisfying

```math
u_p\cdot(p-b)\ge c_D,
\qquad
c_D\to{\sqrt3\over2}.
\tag{34}
```

Put

```math
L_D:=\sqrt{2Dc_D}
=(3^{1/4}+o(1))\sqrt D.
\tag{35}
```

For each incidence, either $`b`$ is off the carrier circle of $`a`$, or the
attachment cell has diameter at least $`L_D-2`$.

Hence either at least half of the $`T`$ incidences are off-carrier returns,

```math
\boxed{
N_{\rm off}
\ge
(\pi-t_D-o(1))D,
}
\tag{36}
```

or at least $`T/2`$ incidences lie in $`L_D`$-large harmonic cells.

The canonical attachment-perimeter budget bounds the number of such large cells by

```math
{2\pi D\over L_D-2}.
```

Therefore in the second case one harmonic cell carries at least

```math
{T(L_D-2)\over4\pi D}
```

degree-three fan attachments.  Using (5),

```math
\boxed{
N_{\rm one\ cell}
\ge
\left(
{(\pi-t_D)3^{1/4}\over2\pi}
-o(1)
\right)\sqrt D.
}
\tag{37}
```

At $`t_D\le1.860+o(1)`$, the fork becomes

```math
\boxed{
N_{\rm off}>
(1.2815926535\ldots-o(1))D,
}
\tag{38}
```

or one harmonic cell carries

```math
\boxed{
N_{\rm one\ cell}>
(0.2684419930\ldots-o(1))\sqrt D
}
\tag{39}
```

degree-three fan attachments.

## 9. Frontier effect

The live modern high-$`t`$ low-$`x_B`$, square-root-matching branch now has the
simultaneous normal form

```math
\boxed{
\begin{array}{rl}
I &= (\pi-o(1))D,\\
T &\ge (2\pi-2t_D-o(1))D,\\
Z_{\rm deep} &\ge {2(\pi-t_D)\over5}D-o(D),\\
e_{BI} &\ge (2\pi-2t_D-o(1))D,\\
s_C &= (\pi-t_D+o(1))D.
\end{array}
}
\tag{40}
```

At $`t_D\le1.860`$, this forces

- $`>2.56318D-o(D)`$ degree-three exact fan terminals;
- $`>0.51263D-o(D)`$ distinct deep diameter-inactive positive-contact ports;
- $`>2.56318D-o(D)`$ loaded-to-unloaded contact incidences;
- $`>1.28159D-o(D)`$ pinned-contact stress surplus;
- and the explicit harmonic-return fork (38)--(39).

This removes the possibility that the high-$`t`$ low-$`x_B`$ hard branch is
predominantly stress-flat degree-two fan geometry.

## 10. Remaining bottleneck

No contradiction is claimed.

The remaining branch is now specifically an attachment-system problem.  A closing
argument must show that the noncrossing harmonic attachment family cannot support
both

```math
e_{BI}\ge(2\pi-2t_D-o(1))D
```

and

```math
s_C=(\pi-t_D+o(1))D
```

while more than

```math
{2(\pi-t_D)\over5}D-o(D)
```

distinct unloaded ports lie a fixed positive depth inside $`F`$.

Two concrete next targets are now sharper:

1. **off-carrier branch:** charge the linear family (36) of nonlocal returns to the
   cyclic noncrossing attachment-perimeter ledger;
2. **large-cell branch:** combine the $`\Omega(\sqrt D)`$ fan population in one
   $`L_D`$-large harmonic cell with the current component graph-diameter and
   pinned-stress identities.

The macroscopic inactive-container and Type-I branches are unchanged.

**Disposition:** proof-only composition and structural strengthening.  No numerical
search, verifier execution, CI result, or unexecuted certificate code is used.
