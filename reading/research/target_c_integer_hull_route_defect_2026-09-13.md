> Generated reading edition · [exact source](../../research/target_c_integer_hull_route_defect_2026-09-13.md) · source SHA-256 `1f3065ef1bc358745f8a8ebd2485d1a588531d0880d20bf51d9a9dc7b6796769`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "464723a7f120c05f14c4f916ad4ad119b52b5f13", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_integer_hull_route_defect_2026-09-13.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c6abcb36289b8f758680d936eb5aba6573b6ef306563535353de7c1482e3f943"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — integer hull-route defect and the hidden long-side payment

**Date:** 2026-09-13  
**Status:** proof-only finite Type-II reduction; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The loaded-hull ledger records `u_B` as an integer outer-walk slack, while the
diameter ledger uses the metric correction `b-per(F)`.  These are not the same
quantity.  The exact route/chord decomposition below separates the integer rounding
cost from the metric cost of long loaded-hull sides.

The useful implication chain is

```text
integer outer routes + convex loaded-hull sides
 -> exact rounding decomposition
 -> u_B pays every side-length excess above 2
 -> zero outer detour leaves a rounded long-side endpoint.
```

This is a source-level reduction.  It does not provide the missing contradiction.

## 1. Exact integer rounding decomposition

Use the canonical Type-II loaded-hull notation.  Let `b_i` be the loaded force-hull
vertices in cyclic order, put

```math
s_i:=|b_i-b_{i+1}|,
\qquad
\ell_i:=|W_i|,
```

where `W_i` is the distinguished outer-face unit-edge route from `b_i` to
`b_{i+1}`.  The canonical route facts are

```math
s_i\ge1,
\qquad
\ell_i\in\mathbb Z_{\ge1},
\qquad
\ell_i\ge s_i.
\tag{IR.1}
```

Therefore `\ell_i\ge\lceil s_i\rceil`.  Define

```math
r_i:=\ell_i-\lceil s_i\rceil\in\mathbb Z_{\ge0},
\qquad
\varphi_i:=\lceil s_i\rceil-s_i\in[0,1).
\tag{IR.2}
```

Since the routes partition the occurrence-counted outer walk,

```math
\boxed{
b-\operatorname{per}(F)
=\sum_i(\ell_i-s_i)
=\sum_i r_i+\sum_i\varphi_i.
}
\tag{IR.3}
```

Both terms on the right are nonnegative.  The first is an integer route surplus; the
second is the one-sided distance of each hull side from the next integer length.

For every `\epsilon\in(0,1)`, let

```math
N_{\epsilon}:=\#\{i:\varphi_i\ge\epsilon\}.
```

Equation (IR.3) gives the exact finite bound

```math
\boxed{
N_{\epsilon}\le {b-\operatorname{per}(F)\over\epsilon}.
}
\tag{IR.4}
```

Thus a sublinear outer detour forces all but `o(D)` loaded-hull side lengths to lie
within every fixed `\epsilon` below an integer.  This conclusion is one-sided: a side
length just above an integer is charged by the next integer, as it must be.

## 2. The integer slack pays metric side excess above two

Let `M=\{i:s_i>1\}` and `m=|M|`, as in Section 63.  Put

```math
L_{>2}:=\sum_{i\in M}(s_i-2)_+.
\tag{IR.5}
```

The canonical integer slack is

```math
u_B=\sum_{i\in M}(\ell_i-2)
      +\sum_{i\notin M}(\ell_i-1).
\tag{IR.6}
```

For `i\in M`, `\ell_i\ge2` and `\ell_i-2\ge(s_i-2)_+`; for `i\notin M`,
`\ell_i-1\ge0`.  Hence

```math
\boxed{u_B\ge L_{>2}.}
\tag{IR.7}
```

The difference is also controlled by the same metric detour.  Term by term, the
contribution to `u_B-L_{>2}` is `ell_i-s_i` when `s_i>2`, is at most `ell_i-s_i`
when `1<s_i\le2`, and equals `ell_i-s_i` when `s_i=1`.  Thus

```math
\boxed{
0\le u_B-L_{>2}
\le\sum_i(\ell_i-s_i)
=b-\operatorname{per}(F).
}
\tag{IR.7a}
```

The signed sum is also explicit:

```math
\sum_{i\in M}(s_i-2)
=\operatorname{per}(F)-q-m.
\tag{IR.8}
```

Taking positive parts in (IR.8) and using (IR.7) gives

```math
\boxed{
u_B\ge\bigl(\operatorname{per}(F)-q-m\bigr)_+.
}
\tag{IR.9}
```

This is stronger than the already-used `b\ge\operatorname{per}(F)` sign statement:
it identifies the payment when the nonunit hull sides have total length greater than
`2m`.

## 3. Zero outer detour is a tight long-side endpoint

Consider a Type-II subsequence for which the relevant limits exist, and write

```math
t={q-k\over D},
\qquad
r={m+k\over D},
\qquad
\lambda={b-\operatorname{per}(F)\over D}.
```

The exact identity `b=q+m+u_B` and `\operatorname{per}(F)/D\to\pi` imply

```math
\boxed{
{u_B\over D}=\pi+\lambda-t-r+o(1).
}
\tag{IR.10}
```

In particular, if `\lambda\to0`, then `t+r\le\pi+o(1)` and

```math
{u_B\over D}=\pi-t-r+o(1).
\tag{IR.11}
```

On the same subsequence, (IR.9) gives

```math
{u_B\over D}\ge[\pi-t-r]_+-o(1).
\tag{IR.12}
```

When `\lambda\to0`, (IR.7a) and (IR.11) give

```math
\boxed{
{u_B-L_{>2}\over D}\longrightarrow0,
\qquad
{L_{>2}\over D}\longrightarrow\pi-t-r.
}
\tag{IR.13}
```

The first equality says that asymptotically every unit of `u_B` is spent on metric
side length above two.  In particular, the zero-detour branch cannot hide a positive
linear `u_B` in arbitrary bridge excursions or in unused integer route length.

Combining (IR.3) and (IR.13), for every fixed `\epsilon>0` only `o(D)` sides can be
`\epsilon` away below their next integer, and the residual route excess
`\sum_i r_i` is `o(D)`.  This is an exact rounded-side endpoint, not an assumption that
the side lengths are literally integers.

## 4. Consequence on the Section-118 endpoint profile

On the proof-only common-cap profile, the strict aggregate/moment composition gives

```math
t\ge T_0-o(1),
\qquad
T_0=2.8406856729\ldots .
\tag{IR.14}
```

If a further zero-detour subsequence satisfies the low-sum condition

```math
t+r\le\pi-\eta+o(1),
\qquad
K_0:=\pi-T_0=0.3009069806\ldots,
\tag{IR.15}
```

then (IR.13) yields

```math
\boxed{
\liminf {u_B\over D}
\ge\eta.
}
\tag{IR.16}
```

On the Section-118 profile, the lower floor `t\ge T_0-o(1)` and
`K_0=\pi-T_0` show how this condition is approached: for example,
`t\le T_0+\eta/2` and `r\le K_0-3\eta/2` imply (IR.15).  The remaining
cases are the boundary layer `t+r\uparrow\pi` or the high-density case
`t>T_0+\eta/2`.

Together with (IR.7), (IR.15) forces at least `\eta D-o(D)` of total nonunit side
length above two.  The deficit is metric, not merely combinatorial.

## 5. Exact pure-tooth corollary

In the exact pure-tooth endpoint, Section 126 gives `m=q` and every distinguished
route has `\ell_i=2`. Hence `b=2q`. The audited endpoint train-capacity inequality
gives

```math
\liminf {q\over D}
\ge2\sqrt{\Delta_2},
\qquad
\Delta_2={\pi\over2\sqrt3}.
```

Using `\operatorname{per}(F)/D\to\pi`,

```math
\boxed{
\liminf {b-\operatorname{per}(F)\over D}
\ge4\sqrt{\Delta_2}-\pi
 =0.6676585738\ldots .
}
\tag{IR.17}
```

Thus the exact pure-tooth endpoint is automatically a positive-detour endpoint.  A
near-geodesic argument cannot close it; it must use the long-side/diameter geometry
or a source-preserving shear.

## 6. Scope and remaining obligation

- The finite statements use only the canonical Section-63 route/chord inequalities.
- The asymptotic statements use Type-II perimeter convergence and, in Section 4,
  the proof-only Section-118 floor.
- All outer routes and bridges are counted with occurrence multiplicity.
- Contact-isolated source points remain in the full source and never enter the affine
  kernel.
- No equality uniqueness, KKT coefficient floor, or global-minimizer construction is
  used.

The new closing target is precise: prove that a linear rounded-side endpoint of the
form (IR.13) is incompatible with the loaded diameter thrackle or with the inward
harmonic contact geometry. The present note does not prove that final incompatibility;
C-II remains open.
