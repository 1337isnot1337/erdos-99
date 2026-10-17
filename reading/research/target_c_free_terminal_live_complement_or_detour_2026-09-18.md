> Generated reading edition · [exact source](../../research/target_c_free_terminal_live_complement_or_detour_2026-09-18.md) · source SHA-256 `c4c5c65503b3d43f44d1a057da8f196337cfaf81ee9afedb7158c29c39accee6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "159dfc35623810ab952e17c86bd6d82994213ea4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_live_complement_or_detour_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a90a542d24222c39fa8c382dd5e709b1858b6ad6d8fa3621b701f5e735983b04"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — live terminal complement-train or near-maximal-detour split

**Date:** 2026-09-18  
**Status:** proof-only terminal refinement; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE subsequences in the live window immediately above the certified `t` floor  
**Depends on:** correlated exact-`t` stability; hostile-audited two-bin theorem; hostile-audited shared routewise retention; dominant outer directional-energy lower bound; live exact-flex diameter locking  
**Certificate:** `research/verify_target_c_free_terminal_live_complement_or_detour_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Fix

```math
\varepsilon_0:=0.00710
```

and suppose a terminal subsequence satisfies

```math
\limsup t_D\le\mu_*+\varepsilon_0
=1.960362849540479\ldots .
\tag{CD.1}
```

The correlated stability theorem gives, after a convergent subsequence,

```math
a+2(r+\delta)\le5\varepsilon_0=0.0355,
\tag{CD.2}
```

where

```math
r=\lim{Q-f\over D},
\qquad
\delta=\lim{b-P_F\over D},
\qquad
 a=\lim\left({\tau_D\over D}-{\pi\over2}-0.007707\right),
```

and all three variables are nonnegative.

Let `p` be the retained complement O--O pair mass supplied by shared routewise retention. Then one of two quantitatively different things must happen:

```math
\boxed{
p>0.01}
\tag{CD.3}
```

or

```math
\boxed{
\delta>0.01725,
\qquad
r\le0.0005,
\qquad
 a\le0.001.
}
\tag{CD.4}
```

Thus a terminal survivor in this narrow live interval either retains at least `0.01D-o(D)` complement outer-to-outer trains, or spends more than `97.18%` of the entire stability allowance for outer-walk detour and is forced extremely close to the pentagonal/matched-train endpoint in every other scalar defect.

In the first branch, the retained complement trains are a subset of the O--O trains. The exact O--O multishear and the live diameter-locking theorem therefore give an exact contact-flex product of dimension at least `(0.01-o(1))D`, a matching to the same number of pairwise distinct actual diameter bars, and at least `(0.02-o(1))D` signed flex/diameter derivative incidences.

The second branch has

```math
0.01725<\delta\le0.01775,
\tag{CD.5}
```

so its normalized exceptional-face counts are squeezed into

```math
0.761283045491165\ldots
\le\liminf {f\over D}
\le\limsup {f\over D}
\le0.761883045491166\ldots,
\tag{CD.6}
```

and the pentagon count obeys

```math
\boxed{
\liminf {P_5\over D}
\ge0.760783045491165\ldots .
}
\tag{CD.7}
```

Only at most `0.0005D+o(D)` bounded exceptional faces can have degree at least six.

---

## 1. Correlated residual envelope

Put

```math
\Delta_2={\pi\over2\sqrt3},
\qquad
s_2=\sqrt{\Delta_2},
\qquad
A_0=2s_2+0.007707.
```

The two-bin theorem gives residual exact-orbit mass

```math
R\le r_2(C),
\qquad
r_2(C):={C-\sqrt{8\Delta_2-C^2}\over2}.
```

Keeping the correlation in (CD.2) and dropping only `r>=0`,

```math
a\le5\varepsilon_0-2\delta.
```

Since `r_2` is increasing on the present interval,

```math
\boxed{
R\le\rho(\delta)
:=r_2(A_0+5\varepsilon_0-2\delta),
\qquad
0\le\delta\le{5\varepsilon_0\over2}=0.01775.
}
\tag{1.1}
```

---

## 2. Small complement mass forces detour

Shared routewise retention supplies retained dominant outer-occurrence mass `z` and retained complement O--O pair mass `p` satisfying

```math
z+p\ge{\pi\over2}-R-o(1).
\tag{2.1}
```

The dominant occurrences alone consume outer directional energy

```math
F(z):=z-6\sin(z/6),
```

and the disjoint-energy theorem gives in particular

```math
F(z)\le\delta.
\tag{2.2}
```

Assume

```math
p\le\eta:=0.01.
\tag{2.3}
```

Using (1.1) in the weakening direction in (2.1),

```math
z\ge {\pi\over2}-\rho(\delta)-\eta-o(1).
```

The function `F` is increasing for nonnegative arguments. Hence every limiting survivor with (2.3) must satisfy

```math
\boxed{
F\left({\pi\over2}-\rho(\delta)-0.01\right)\le\delta.
}
\tag{2.4}
```

The exact-rational certificate proves that the function

```math
\Phi(\delta)
:=F\left({\pi\over2}-\rho(\delta)-0.01\right)-\delta
```

is strictly decreasing throughout `[0,0.01775]` and that

```math
\boxed{
\Phi(0.01725)>1.39\times10^{-6}.
}
\tag{2.5}
```

Therefore (2.4) is impossible for `delta<=0.01725`, proving

```math
\boxed{\delta>0.01725.}
\tag{2.6}
```

No complement-rhombus incidence inequality is needed for this step. It uses only shared retention and the dominant outer-energy payment.

---

## 3. The remaining defect budget collapses

Insert (2.6) into (CD.2):

```math
a+2r
\le0.0355-2(0.01725)
=0.001.
\tag{3.1}
```

Since `a,r>=0`,

```math
\boxed{
a\le0.001,
\qquad
r\le0.0005.}
\tag{3.2}
```

This proves (CD.4). The upper detour bound in (CD.5) is the immediate stability consequence

```math
\delta\le{5\varepsilon_0\over2}=0.01775.
```

Thus the small-complement branch places the actual outer walk in the narrow normalized detour interval

```math
0.01725< {b-P_F\over D} < 0.01775+o(1),
```

while leaving at most `0.001D` of the correlated defect budget for train-slack excess and superpentagonal degree excess combined.

---

## 4. Exceptional faces become almost purely pentagonal

The exact terminal train ledger gives

```math
{f\over D}
={M_*+2a-\delta-r\over5}+o(1),
\qquad
M_*=4s_2+2(0.007707)
=3.824665227455829\ldots .
\tag{4.1}
```

Using

```math
0\le a\le0.001,
\quad
0\le r\le0.0005,
\quad
0.01725<\delta\le0.01775,
```

gives (CD.6).

Let `n_+` be the number of bounded exceptional faces of degree at least six. Degree excess gives

```math
n_+\le Q-f=rD+o(D),
```

so

```math
\boxed{n_+\le(0.0005+o(1))D.}
\tag{4.2}
```

Since `P_5=f-n_+`, the worst allowed lower endpoint gives

```math
\frac{P_5}{D}
\ge
\frac{M_*-0.01775-0.0005}{5}-0.0005-o(1),
```

which is (CD.7).

---

## 5. Consequence of the large-complement branch

If (CD.3) holds, shared retention has selected more than `0.01D-o(D)` distinct complement O--O trains. These are genuine complete outer-to-outer stopped trains.

The exact O--O multishear gives one independent exact contact-preserving angle coordinate per such train. Applying the live diameter-locking theorem to this product gives

```math
\operatorname{rank}G\ge(0.01-o(1))D,
```

a matching to at least `(0.01-o(1))D` pairwise distinct actual diameter edges, and

```math
I_++I_-\ge(0.02-o(1))D.
```

Thus the branch cannot hide behind singleton-train abundance: either a linear complement O--O flex reservoir exists anyway, or the outer detour is forced into the narrow near-maximal interval (CD.5) and all other scalar defect modes almost disappear.

---

## 6. Remaining obstruction

This refinement removes one ambiguity from the live `epsilon=0.00710` window.

A survivor cannot simultaneously have negligible retained complement O--O transport, moderate outer detour, and significant non-pentagonal/train-slack defects. If complement O--O mass is below `0.01D`, the actual outer-walk detour is essentially forced to the top of its allowed stability range and the bounded exceptional network is more than `0.7607D` pentagons with only `0.0005D` superpentagons.

The next closing step can therefore split cleanly:

1. exploit the linear O--O exact-flex/diameter-locking matching; or
2. exploit the near-maximal outer-detour plus almost-pure pentagon regime, where only `0.001D` total correlated defect budget remains outside the detour.

No theorem-state file is changed.

**Disposition:** proved a live complement-train/near-maximal-detour dichotomy and quantified the resulting pentagonal endpoint concentration; C-II remains open.
