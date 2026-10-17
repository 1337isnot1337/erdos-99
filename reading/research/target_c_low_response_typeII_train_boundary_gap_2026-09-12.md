> Generated reading edition · [exact source](../../research/target_c_low_response_typeII_train_boundary_gap_2026-09-12.md) · source SHA-256 `66ea30aafe322054deb2a5deca4b34359933353b3de7a0136f4ee15473e83f36`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5191e008dacab36e023395675de60a72c4cde81e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_low_response_typeII_train_boundary_gap_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e5e30066919bc560e9a25f968c95483d7bf33faa01a1f795e2e49582275c3ce3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — local train boundary raises the Type-II low-response surplus floor to 1.63756

**Date:** 2026-09-12  
**Base branch:** `sol/2026-09-12-low-response-cell-closure`  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate pending independent hostile audit/promotion.

## 1. Result

Use the canonical post-ZF notation

```math
\varepsilon_D=\sum_{b<k}c_{bk}-1,
\qquad
\mu_D={e_{BB}+2s_C-3(d_H+s_Z)\over D},
```

and assume the canonical Section-80 Type-II branch together with

```math
\varepsilon_D\to0.
\tag{1.1}
```

The weaker assumption `epsilon_D->0`, rather than `D epsilon_D->0`, is sufficient for
this theorem.

Put

```math
a_0={\sqrt3\over2}
```

for the minimum area of a triangle-free strict unit rhombus, and define

```math
\boxed{
M_{tr}:={2\pi+\sqrt{2\pi/\sqrt3}\over5}
=1.6375621841\ldots .
}
\tag{1.2}
```

### Theorem LRII-T — local train-boundary gap

Every Type-II sequence satisfying (1.1) obeys

```math
\boxed{
\liminf_{D\to\infty}\mu_D\ge M_{tr}>1.6375.
}
\tag{LRII-T.1}
```

This strictly supersedes the previous low-response Type-II floors on the branch.
It does not close C-II and does not address Type I.

The proof uses four canonical ingredients:

1. C41 total response energy to select one `D-o(D)` attachment cell;
2. the exact Section-62 ZK component/slack budget;
3. Section-83 Type-II attachment-cell area tiling and local rhombus saturation; and
4. the finite train-boundary inequality `B_4>=4sqrt(R_4)` used canonically in
   Section 85.

The main new coupling is local: the same augmented internal graph that bounds the
cell perimeter also has to expose the boundary of its quadratic rhombus population.

## 2. Select the dominant near-diameter component

C41 gives

```math
\sum_{b<k}c_{bk}|b-k|^2=D^2,
\qquad
\sum_{b<k}c_{bk}=1+\varepsilon_D.
\tag{2.1}
```

Let `P_r=conv(A_r)` be the harmonic attachment cells and choose `P_*` with maximal
Euclidean diameter `d_*`. As in LRII-P,

```math
D^2\le d_*^2(1+\varepsilon_D),
```

so

```math
\boxed{{d_*\over D}\to1.}
\tag{2.2}
```

C40 gives

```math
{\delta_*\over D}\to1
\quad\text{from below in the sense}\quad
\delta_*\ge d_*-2.
\tag{2.3}
```

Let `r_*` be the Eppstein slack of `C[I_*]` and pass to a subsequence on which

```math
\mu_D\to\mu<\infty,
\qquad
{\delta_*+r_*\over D}\to\gamma,
\qquad
{1\over D}\sum_{r\ne *}\delta_r\to t.
\tag{2.4}
```

The exact ZK ledger

```math
\sum_r\delta_r+R_I+s_B=\mu_DD+6
\tag{2.5}
```

implies

```math
\boxed{
\gamma\ge1,
\qquad
t\ge0,
\qquad
\gamma+t\le\mu.
}
\tag{2.6}
```

All omitted `r_r` and `s_B` terms are nonnegative.

## 3. The augmented internal graph and its exact face budget

Choose `s,t in A_*` with `|s-t|=d_*`. Adjoin these two loaded vertices to
`C[I_*]`, retaining exactly one actual attachment contact from each into `I_*`.
Call the resulting connected plane triangle-free unit-distance graph `G'`.

Let

- `b'` be its outer-face walk length;
- `Q'=sum_F(deg F-4)` over its bounded faces;
- `f'` be its number of bounded nonquadrilateral faces.

Exactly as in LRII-P, Euler plus face incidence and the two degree-one leaves give

```math
\boxed{
b'+Q'=2(\delta_*+r_*)+4.}
\tag{3.1}
```

Hence

```math
{b'+Q'\over D}\to2\gamma.
\tag{3.2}
```

Let

```math
K_*:=conv(V(G')).
```

Every omitted attachment has a unit contact to `I_*`, while `I_* subset P_*`; thus

```math
K_*\subset P_*\subset K_*+B(0,1).
\tag{3.3}
```

Consequently

```math
d_H(K_*,P_*)\le1,
\qquad
\operatorname{per}(K_*)
\ge\operatorname{per}(P_*)-2\pi.
\tag{3.4}
```

Every convex-hull vertex of `G'` lies on its outer face, whose unit-edge walk has
length `b'`, so

```math
\boxed{
b'\ge\operatorname{per}(P_*)-2\pi.}
\tag{3.5}
```

### Lemma 3.1 — bounded four-faces of `G'` are exactly all-unloaded strict rhombi

Every bounded face of `G'` lies inside `K_*`. No omitted loaded attachment lies in
`K_*`: each loaded attachment is an extreme vertex of `P_*`, and a distinct extreme
vertex of `P_*` cannot belong to the convex hull of `I_*` together with only `s,t`.
Therefore deleting the other loaded attachments and their incident edges can open
faces only to the outer face of `G'`; it cannot place an omitted loaded vertex inside
a bounded face.

Every source vertex of `I_*` and every contact edge with both endpoints in `I_*` is
retained. Hence a bounded degree-four face of `G'` has a four-edge unit-contact boundary
with no omitted source vertex or contact edge in its interior. It is therefore a
bounded four-face of the original contact embedding. Canonical local face convexity
(Section 82) makes it a convex unit rhombus, and triangle-freeness makes it strict.
Conversely every original strict rhombus whose four vertices lie in `I_*` remains a
bounded four-face of `G'`.

Thus the bounded degree-four faces of `G'` are precisely the unloaded-only strict
rhombi assigned to `I_*` in canonical Section 83. `square`

Write their number as `R_*`.

## 4. Local train boundary forces `gamma` from cell area and perimeter

Let `B_*` be the number of edge occurrences incident to exactly one of the `R_*`
strict rhombi. The finite train-boundary theorem gives

```math
\boxed{B_*\ge4\sqrt{R_*}.}
\tag{4.1}
```

Every occurrence counted by `B_*` faces on its other side either the outer face of
`G'` or one bounded nonquadrilateral face. Hence

```math
B_*\le b'+4f'+Q'.
\tag{4.2}
```

Every bounded nonquadrilateral face has degree at least five, so `f'<=Q'`. Therefore

```math
\boxed{B_*\le b'+5Q'.}
\tag{4.3}
```

Use (3.1) to eliminate `Q'`:

```math
b'+5Q'
=5(b'+Q')-4b'
=10(\delta_*+r_*)+20-4b'.
\tag{4.4}
```

Let

```math
a:=\lim {\operatorname{area}(P_*)\over D^2},
\qquad
p:=\lim {\operatorname{per}(P_*)\over D}
```

after a further subsequence.

Canonical Section 83 gives

```math
\operatorname{area}(P_*)-A_{4,*}=o(D^2),
\tag{4.5}
```

because every local deficit is nonnegative and their global sum is `o(D^2)`.
Canonical Type II also gives globally

```math
A_4-a_0R_4=o(D^2).
\tag{4.6}
```

Each rhombus excess `area(R)-a_0` is nonnegative, so the same holds on the selected
subfamily:

```math
A_{4,*}-a_0R_*=o(D^2).
\tag{4.7}
```

Thus

```math
\boxed{{R_*\over D^2}\to {a\over a_0}.}
\tag{4.8}
```

Divide (4.1)--(4.4) by `D` and use (3.5), (4.8):

```math
4\sqrt{a/a_0}
\le10\gamma-4p.
\tag{4.9}
```

Planar isoperimetry gives

```math
p\ge2\sqrt{\pi a}.
\tag{4.10}
```

Substitute (4.10) into (4.9):

```math
\boxed{
\gamma
\ge
C_{tr}\sqrt a,
\qquad
C_{tr}:={4\over5}\sqrt\pi+{2\over5\sqrt{a_0}}.
}
\tag{4.11}
```

This is the new local train/perimeter coupling.

## 5. The remaining diameter budget bounds all remaining cell area

From (2.4), the total graph-diameter budget outside `I_*` is `tD+o(D)`. C40 and
ordinary isodiametry give, exactly as in LRII-P,

```math
\boxed{
\limsup {1\over D^2}
\sum_{r\ne *}\operatorname{area}(P_r)
\le {\pi\over4}t^2.
}
\tag{5.1}
```

Canonical Section 83 and Type II give total cell area

```math
\sum_r\operatorname{area}(P_r)
={\pi\over4}D^2-o(D^2).
\tag{5.2}
```

Therefore

```math
\boxed{
a\ge{\pi\over4}(1-t^2).}
\tag{5.3}
```

when `0<=t<=1`. If `t>1`, then (2.6) already gives `mu>2>M_tr`, so only `t<=1`
needs consideration.

Combine (4.11) and (5.3):

```math
\gamma
\ge
M_{tr}\sqrt{1-t^2},
\tag{5.4}
```

where

```math
C_{tr}{\sqrt\pi\over2}
={2\pi\over5}+{1\over5}\sqrt{\pi/a_0}
={2\pi+\sqrt{2\pi/\sqrt3}\over5}
=M_{tr}.
\tag{5.5}
```

We also retain `gamma>=1` from (2.6).

## 6. Optimize the honest split

By (2.6),

```math
\mu\ge\gamma+t.
\tag{6.1}
```

If

```math
t\ge M_{tr}-1,
```

then `gamma>=1` gives immediately

```math
\mu\ge1+t\ge M_{tr}.
\tag{6.2}
```

Now suppose

```math
0\le t\le M_{tr}-1.
```

Then (5.4) gives

```math
\mu\ge M_{tr}\sqrt{1-t^2}+t.
\tag{6.3}
```

The function on the right is concave on `[0,1]`, so on the present interval its
minimum occurs at an endpoint. At `t=0` it equals `M_tr`.

For the other endpoint, elementary bounds give

```math
{3\over2}<M_{tr}<{5\over3}.
\tag{6.4}
```

Hence `M_tr-1<2/3`, and

```math
M_{tr}\sqrt{1-(M_{tr}-1)^2}
>
{3\over2}\sqrt{1-{4\over9}}
={\sqrt5\over2}>1.
```

Therefore at `t=M_tr-1`,

```math
M_{tr}\sqrt{1-t^2}+t
>1+(M_{tr}-1)=M_{tr}.
```

So (6.3) is at least `M_tr` throughout the interval. Together with (6.2),

```math
\boxed{\mu\ge M_{tr}.}
```

This proves LRII-T.1.

For (6.4), for example, `pi>3` and `sqrt3<2` give the lower bound, while
`pi<22/7` and `sqrt3>5/3` give the upper bound by direct substitution into (1.2).
No decimal computation is needed.

## 7. Equality geometry and what remains

The minimizing split in this proof is

```math
t=0.
```

Thus any sequence approaching the LRII-T constant must put asymptotically all
macroscopic component-diameter budget into the single response-selected harmonic
component. It must also asymptotically saturate

1. Type-II cell area tiling, so `P_*` carries essentially the full disk area;
2. planar isoperimetry, so `P_*` has asymptotic circular perimeter;
3. the local train boundary `B_*=4sqrt(R_*)`;
4. the recipient bound `B_*=b'+5Q'`, forcing almost all non-rhombic recipients to be
   pentagonal at leading order; and
5. the augmented Euler identity, with the `Q'` currency taking the precise difference
   between the circular perimeter and the train-boundary requirement.

This is consistent with the canonical warning that near-degenerate pentagonal
corridors are the binding Type-II regression. The theorem therefore identifies, rather
than hides, the next obstruction: one near-disk harmonic component with a linear
pentagonal/interface budget and essentially no macroscopic competing cell.

## 8. Scope audit

- **Type II only.** Type I is untouched.
- The response assumption is only `epsilon_D->0`.
- Contact-isolated source points remain in the source and are not counted as harmonic
  components.
- The local train theorem is applied only after Lemma 3.1 identifies the bounded
  four-faces of the augmented internal graph with actual unloaded strict rhombi.
- The global Type-II equality `A_4-a_0R_4=o(D^2)` is used only through nonnegative
  subfamily excess.
- The microscopic `+2` attachment-diameter corrections contribute only `O(D)` after
  squaring and summing, as in the canonical ZK area estimates.
- No KKT coefficient floor, C66 star center, NLC, ESN, or HSR theorem is used.
- The result is not a Level-I closure: it is a stronger necessary lower bound on the
  renormalized component/slack currency.
