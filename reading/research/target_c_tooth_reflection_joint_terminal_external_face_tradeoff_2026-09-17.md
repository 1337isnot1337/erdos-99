> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_joint_terminal_external_face_tradeoff_2026-09-17.md) · source SHA-256 `a8e430a4ad50f85a9e922a3921f531f26b81ade8c7236a42ae4a6959c6fe6f46`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "259d98251b3c6399919cac7fb44ac097295f10fa", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_joint_terminal_external_face_tradeoff_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c8c53ca242f11a200f61fc63e4fb22374b71096b944bb8add23ab63d8d8642db"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — sharp joint terminal / external FREE face minimax

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only strengthening of the sharp universal FREE-face and terminal-deficit theorems  
**Scope:** all-inactive non-anchored FREE reflection ancestry  
**Dependencies:** sharp universal FREE-face theorem; block-optimized thin/thick upper-block theorem; terminal-deficit thin-matching budget; external-population upper-gate bound  
**Certificate:** `research/verify_target_c_tooth_reflection_joint_terminal_external_face_tradeoff_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The universal FREE-face theorem and the terminal-deficit theorem lower-bound the same
upper-block backtracking in two different ways.  Taking those bounds simultaneously,
before minimizing over the number of upper blocks, gives a stronger terminal law.  The
external population optionally places a further hard cap on the admissible block count.

Write

```math
T_D:=\pi D-q,
\qquad
Z_D:=|A\setminus F|,
\qquad
F=\operatorname{conv}B.
```

Assume first only

```math
\limsup_{D\to\infty}{T_D\over\sqrt D}\le t<\infty.
\tag{JE.1}
```

Put

```math
h_*={\sqrt{303}\over52},
\qquad
k_\infty={1\over2h_*}=1.493660973015707\ldots,
\tag{JE.2}
```

and let the sharp universal upper-block coefficient be

```math
K_\infty=0.188640613456314\ldots,
\qquad
c_{\rm univ}=2\sqrt{K_\infty}
=0.868655543829230\ldots .
\tag{JE.3}
```

For `b>0`, define

```math
\boxed{
Q_t(b):=
{1+\max\left\{K_\infty b^2,
\;k_\infty\left(b-{t\over2}\right)_+^2\right\}
\over b}.
}
\tag{JE.4}
```

Then every all-inactive FREE ancestry contains one consecutive all-lower run in the
original outer contact face with

```math
\boxed{
\operatorname{span}_N(R)
\ge (C_{\rm joint}(t)-o(1))\sqrt D,
\qquad
C_{\rm joint}(t):=\min_{b>0}Q_t(b).
}
\tag{JE.5}
```

This terminal-only conclusion does **not** require an external-population hypothesis.
If in addition

```math
\limsup_{D\to\infty}{Z_D\over\sqrt D}\le z<\infty,
\tag{JE.6}
```

then the exact stronger coefficient is

```math
\boxed{
L(z,t):=\min_{0<b\le z}Q_t(b),
}
\tag{JE.7}
```

with `L(0,t)=+infinity`, and

```math
\boxed{
\operatorname{span}_N(R)
\ge (L(z,t)-o(1))\sqrt D.
}
\tag{JE.8}
```

For every fixed `Lambda>1`, the selected run contains a vertex-disjoint matching of old
fully inactive outer-face source pairs of size

```math
\boxed{
\left({\Lambda-1\over2\Lambda}L(z,t)-o(1)\right)\sqrt D
}
\tag{JE.9}
```

with

```math
\boxed{
1<|x-y|
\le
1+\left({\Lambda h_*\over L(z,t)}+o(1)\right)D^{-1/2}.
}
\tag{JE.10}
```

When no external cap is used, the same statement holds with `L(z,t)` replaced by
`C_joint(t)`.

---

## 1. One block count pays both backtracking mechanisms

Let

- `B` be the number of maximal consecutive upper blocks;
- `m` be the number of thick upper gates at the exact threshold
  ```math
  \tau_D=D-\sqrt{D^2-1};
  
  ```
- `M` be the size of a maximum vertex-disjoint matching among the thin upper gates;
- `R` be the number of maximal all-lower runs.

The block theorem gives

```math
\boxed{B\le m+M,\qquad R\le B+1.}
\tag{JE.11}
```

The thick-edge exact first-hit identity and the activation-time budget give

```math
\boxed{
B_{\rm back}\ge k_Dm^2,
\qquad
k_D\longrightarrow k_\infty.
}
\tag{JE.12}
```

Independently, the sharp local angular-packing theorem over all upper blocks gives in
the square-root block regime

```math
\boxed{
B_{\rm back}
\ge (K_\infty-o(1))B^2-O(B).
}
\tag{JE.13}
```

These are lower bounds for the same nonnegative backtracking quantity, so whenever the
sharp block estimate applies,

```math
\boxed{
B_{\rm back}
\ge
\max\left\{(K_\infty-o(1))B^2-O(B),\;k_Dm^2\right\}.
}
\tag{JE.14}
```

The lower support ledger therefore gives

```math
G_{\rm low}
\ge
D+B_{\rm back}-O(\sqrt D).
\tag{JE.15}
```

---

## 2. Terminal deficit forces thick gates

The terminal-deficit theorem proves the exact hull-perimeter budget

```math
\boxed{2M\le T_D.}
\tag{JE.16}
```

Combining this with `B<=m+M`,

```math
\boxed{
m\ge\left(B-{T_D\over2}\right)_+.}
\tag{JE.17}
```

Thus a block count beyond `T_D/2` cannot be paid entirely by thin interruptions; the
excess blocks force thick-edge quadratic backtracking.

There is no hidden need for `Z_D=O(sqrt(D))` here.  Under (JE.1), if

```math
B/\sqrt D\to\infty,
```

then `M=O(sqrt(D))` by (JE.16), hence `m>=B-M=(1-o(1))B`.  Equations
(JE.12) and (JE.15), divided over at most `B+1` lower runs, give a run of span

```math
(k_\infty-o(1))B\gg\sqrt D.
```

Likewise `B=o(sqrt(D))` gives `G_low=D-o(D)` and only `o(sqrt(D))` lower runs, again
forcing super-square-root span.  Therefore only

```math
\boxed{B=\Theta(\sqrt D)}
\tag{JE.18}
```

can determine the finite square-root minimax constant.  This lies automatically inside
the `B<=D^(5/8)` sharp local-angular regime of (JE.13).

Take a subsequence with

```math
{B\over\sqrt D}\to b>0.
```

Equations (JE.1), (JE.14), (JE.15), and (JE.17) give

```math
\liminf
{\max_R\operatorname{span}_N(R)\over\sqrt D}
\ge
Q_t(b).
\tag{JE.19}
```

Minimizing over all `b>0` proves the terminal-only statement (JE.5).

---

## 3. External population simply truncates the block minimization

The external-population theorem gives a distinct old source point of `A\setminus F` for
every upper gate.  Every upper block contains at least one upper gate.  Hence

```math
\boxed{B\le U\le Z_D.}
\tag{JE.20}
```

Under (JE.6), every positive subsequential block coefficient satisfies `b<=z`.
Therefore (JE.19) minimizes only over `0<b<=z`, which proves (JE.7)--(JE.8).

If

```math
Z_D=o(\sqrt D),
```

then (JE.20) forces `B=o(sqrt(D))`, and the argument preceding (JE.18) gives the stronger
statement

```math
\boxed{
{\max_R\operatorname{span}_N(R)\over\sqrt D}\longrightarrow\infty.
}
\tag{JE.21}
```

---

## 4. Exact solution of the joint minimax

Set

```math
r:=\sqrt{K_\infty/k_\infty}
=0.355378854516177\ldots .
\tag{JE.22}
```

For `b>t/2`, the two quadratic terms in (JE.4) are equal exactly when

```math
\sqrt{K_\infty}\,b
=
\sqrt{k_\infty}\left(b-{t\over2}\right).
```

Thus the crossover is

```math
\boxed{b_0(t)={t\over2(1-r)}.}
\tag{JE.23}
```

For `0<b<=b_0(t)`,

```math
Q_t(b)={1\over b}+K_\infty b,
\tag{JE.24}
```

while for `b>=b_0(t)`,

```math
Q_t(b)
={1+k_\infty(b-t/2)^2\over b}.
\tag{JE.25}
```

The unconstrained minimizers of these two expressions are

```math
\boxed{b_E={1\over\sqrt{K_\infty}}
=2.302408606273952\ldots}
\tag{JE.26}
```

and

```math
\boxed{
b_H(t)=\sqrt{{t^2\over4}+{1\over k_\infty}}.}
\tag{JE.27}
```

There are two transition values:

```math
\boxed{
t_1
={2(1-r)\over\sqrt{k_\infty r(2-r)}}
=1.379843397554451\ldots,}
\tag{JE.28}
```

where `b_0(t_1)=b_H(t_1)`, and

```math
\boxed{
t_2
={2(1-r)\over\sqrt{K_\infty}}
=2.968362546296252\ldots,}
\tag{JE.29}
```

where `b_0(t_2)=b_E`.

Hence

```math
\boxed{
b_*(t)=
\begin{cases}
b_H(t),&0\le t\le t_1,\\
b_0(t),&t_1\le t\le t_2,\\
b_E,&t\ge t_2,
\end{cases}}
\tag{JE.30}
```

and `Q_t` decreases up to `b_*(t)` and is nondecreasing afterwards.  Therefore

```math
\boxed{
C_{\rm joint}(t)=Q_t(b_*(t)),
\qquad
L(z,t)=Q_t\bigl(\min\{z,b_*(t)\}\bigr).
}
\tag{JE.31}
```

---

## 5. Stronger terminal-only law

For `0<=t<=t_1`,

```math
\boxed{
C_{\rm joint}(t)
=g(t)
=k_\infty\left(\sqrt{t^2+{4\over k_\infty}}-t\right).
}
\tag{JE.32}
```

For `t_1<=t<=t_2`,

```math
\boxed{
C_{\rm joint}(t)
={2(1-r)\over t}
+{K_\infty t\over2(1-r)}.
}
\tag{JE.33}
```

For `t>=t_2`,

```math
\boxed{C_{\rm joint}(t)=c_{\rm univ}.}
\tag{JE.34}
```

The preceding terminal theorem took `max{g(t),c_univ}` after minimizing the two
mechanisms separately.  Equations (JE.32)--(JE.34) instead minimize their pointwise
maximum and are strictly stronger throughout

```math
\boxed{t_1<t<t_2.}
```

At

```math
T_D=(2+o(1))\sqrt D,
```

the old separate bound is

```math
\max\{g(2),c_{\rm univ}\}
=0.872566174277741\ldots,
```

while

```math
\boxed{
C_{\rm joint}(2)
=0.937259100006287\ldots .
}
\tag{JE.35}
```

Thus the terminal-sensitive improvement persists until

```math
T_D<(2.968362546296252\ldots-o(1))\sqrt D,
```

rather than disappearing at the previous separate-bound crossover near
`2.01163 sqrt(D)`.

---

## 6. Near-terminal and small-external specialization

When `T_D=o(sqrt(D))`,

```math
b_*(0)={1\over\sqrt{k_\infty}}
=\sqrt{2h_*}
=0.818227333125826\ldots .
\tag{JE.36}
```

Hence

```math
\boxed{
L(z,0)=
\begin{cases}
\displaystyle {1\over z}+k_\infty z,
&0<z<0.818227333125826\ldots,\\[2mm]
\displaystyle 2\sqrt{k_\infty}
=2.444308469089536\ldots,
&z\ge0.818227333125826\ldots .
\end{cases}}
\tag{JE.37}
```

For example, if also

```math
Z_D\le(0.5+o(1))\sqrt D,
```

then

```math
\boxed{
\operatorname{span}_N(R)
\ge(2.746830486507854\ldots-o(1))\sqrt D.
}
\tag{JE.38}
```

For `Lambda=2`, the same run contains a vertex-disjoint matching of

```math
\boxed{
(0.686707621626963\ldots-o(1))\sqrt D
}
\tag{JE.39}
```

old fully inactive pairs with

```math
\boxed{
1<|x-y|
\le1+(0.243733995222019\ldots+o(1))D^{-1/2}.
}
\tag{JE.40}
```

---

## 7. Matching extraction

For a selected all-lower run with support span

```math
S\ge(C-o(1))\sqrt D,
```

where `C` is either `C_joint(t)` or `L(z,t)`, write

```math
\sigma_e=|e|-1>0.
```

The activation-time ledger gives

```math
\sum_{e\in R}\sigma_e\le h_*+o(1).
\tag{JE.41}
```

Support progress per edge is at most `1+sigma_e`, so the run has at least
`(C-o(1))sqrt(D)` edges.  Markov keeps a fraction `1-1/Lambda` with

```math
\sigma_e
\le
\left({\Lambda h_*\over C}+o(1)\right)D^{-1/2}.
```

Parity thinning loses at most another factor two, proving (JE.9)--(JE.10) and their
terminal-only analogue.

---

## 8. Frontier effect

The scalar FREE obstruction now pays three coupled constraints:

1. projective-dispersion backtracking from the sharp universal theorem;
2. thick-edge backtracking once terminal perimeter cannot supply enough thin blocks;
3. an optional absolute block-count cap from the external source population.

The exact square-root minimax is `Q_t`, with the external cap acting only by truncating
its minimizing block coefficient.  In particular the stronger terminal-only middle
window is source-wide and does not depend on a small-external-population assumption.

This still does not close C-II.  A surviving FREE module must carry the resulting long
support-monotone run of old fully inactive vertices in the original outer contact face,
with the near-unit matching above.  The next target is geometric: combine several
ordered module normals, or couple one selected run to the canonical outer-walk / force-
hull currencies, rather than improve the one-dimensional upper-block ledger again.

C-II remains open.  No theorem-state authority is changed.

**Disposition:** combined the sharp universal block-backtracking and terminal-forced
thick-edge bounds before minimization, proved that large block counts are automatically
super-square-root under `T_D=O(sqrt(D))`, then imposed the external-population cap only
as an optional truncation.  This extends the terminal-sensitive improvement window
from about `2.01163 sqrt(D)` to `2.96836 sqrt(D)` and gives stronger coefficients
throughout the intermediate range.
