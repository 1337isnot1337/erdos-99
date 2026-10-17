> Generated reading edition · [exact source](../../research/target_c_section122_near_disk_loaded_contact_localization.md) · source SHA-256 `2d622ce5381a58519693e7b0ef746e688e86981769067244e612a322ba3f4b17`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c1972f8060983ed8b9e88febb89d0c08ec54c3a7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section122_near_disk_loaded_contact_localization.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "57cf588871ca56fe1798b3c0566414f65d0418d5d6cf58a5067be49bf6e3423c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — Section 122: near-disk geometry localizes loaded unit contacts to hull sides

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate.  
**Dependencies:** canonical Type-II near-disk conclusion of Section 80 and canonical Section 63 notation.

This section proves a source-level rigidity statement that is independent of the
carrier coefficient. In every sufficiently large Type-II survivor, a unit contact
between two loaded vertices must be a side of the loaded convex hull. Equivalently,
the Section-63 extra loaded-chord slack vanishes:

```math
\boxed{c_B=0.}
\tag{122.1}
```

Thus the loaded-loaded contact graph is eventually a subgraph of the cyclic hull graph.
No contact-isolated source point is removed or constrained by the Section-57 affine
kernel.

---

## 122.1 A finite convex near-disk lemma

Let `K` be a convex polygon and suppose for some center `o`, radius `R`, and
`0\le\delta<R` that

```math
d_H(K,B(o,R))\le\delta.
\tag{122.2}
```

Put

```math
r:=R-\delta,
\qquad
R_+:=R+\delta.
\tag{122.3}
```

For convex compact sets, Hausdorff distance equals the uniform distance of support
functions. Hence, after translating `o` to the origin,

```math
h_K(u)\ge r
\qquad(|u|=1).
```

Therefore

```math
\boxed{B(0,r)\subset K\subset B(0,R_+).}
\tag{122.4}
```

Define

```math
\beta:=\arccos{r\over R_+}.
\tag{122.5}
```

If `p` is a vertex of `K` and `u` is any outward unit normal in its normal cone, then

```math
u\cdot p=h_K(u)\ge r,
\qquad
|p|\le R_+.
```

Consequently the angle between `u` and the radial direction `p/|p|` is at most
`\beta`.

Now let `p,q` be distinct vertices with

```math
|p-q|=1.
\tag{122.6}
```

Because `|p|,|q|\ge r`, if `\gamma` is the smaller angle between their radial
directions, then

```math
1=|p-q|
\ge 2r\sin{\gamma\over2},
```

so

```math
\boxed{
\gamma\le 2\arcsin{1\over2r}.
}
\tag{122.7}
```

The normal cones of `p` and `q` are therefore contained in angular neighborhoods of
their radial directions of radius `\beta`. By monotonicity of the Gauss map around a
convex polygon, one of the two boundary arcs from `p` to `q` has all its oriented edge
directions in an angular interval of width at most

```math
\tau:=2\beta+\gamma
\le
2\arccos{r\over R_+}
+2\arcsin{1\over2r}.
\tag{122.8}
```

This is the boundary arc corresponding to the shorter normal sweep between the two
normal cones.

### Lemma 122.1 — short-turn unit chord lemma

Assume every side of `K` has length at least one and

```math
2\arccos{r\over R_+}
+2\arcsin{1\over2r}
< {2\pi\over3}.
\tag{122.9}
```

Then every pair of vertices `p,q` with `|p-q|=1` are consecutive vertices of `K`.

### Proof

Take the boundary arc supplied by (122.8). Suppose `p,q` are not consecutive. Then
both boundary arcs between them contain at least two polygon sides, so this selected
arc has edge vectors

```math
v_1,\ldots,v_j,
\qquad j\ge2.
```

Every `|v_i|\ge1`, and all their direction angles lie in an interval of width at most
`\tau<2\pi/3`. Let `w` be the unit vector in the midpoint direction of that interval.
Then

```math
w\cdot v_i
\ge |v_i|\cos{\tau\over2}
\ge \cos{\tau\over2}.
```

Since the arc joins `p` to `q`,

```math
\begin{aligned}
|q-p|
&\ge w\cdot(q-p)\\
&=\sum_{i=1}^j w\cdot v_i\\
&\ge j\cos{\tau\over2}\\
&\ge2\cos{\tau\over2}\\
&>1,
\end{aligned}
```

contradicting (122.6). Hence `p,q` are consecutive. `\square`

The constant `2\pi/3` is the exact elementary threshold for this projection proof:
two unit vectors can sum to a unit vector precisely when their angle is `2\pi/3`.

---

## 122.2 Apply the lemma to the Type-II force hull

Let `F_D` be the loaded force hull of a Type-II survivor with global diameter `D`.
Canonical Section 80 proves that, after choosing suitable centers `o_D`,

```math
\delta_D
:=d_H\!\left(F_D,B(o_D,D/2)\right)
=o(D).
\tag{122.10}
```

Set

```math
R_D={D\over2},
\qquad
r_D={D\over2}-\delta_D,
\qquad
R_{+,D}={D\over2}+\delta_D.
```

Then

```math
{r_D\over R_{+,D}}\longrightarrow1,
\qquad
r_D\longrightarrow\infty.
```

Therefore

```math
2\arccos{r_D\over R_{+,D}}
+2\arcsin{1\over2r_D}
\longrightarrow0.
\tag{122.11}
```

In particular (122.9) holds for all sufficiently large `D`.

Every side of `F_D` joins two source points, so unit separation gives side length at
least one. Lemma 122.1 now applies. Hence:

### Theorem 122.2 — loaded unit-contact localization

For every sufficiently large Type-II survivor,

```math
\boxed{
 b,b'\in B,\quad |b-b'|=1
 \Longrightarrow
 b,b'\text{ are consecutive vertices of }F.
}
\tag{122.12}
```

Thus there are no unit contact chords joining nonconsecutive loaded hull vertices.

---

## 122.3 Exact Section-63 consequences

Use the canonical Section-63 notation:

- `q=|B|`;
- `m` is the number of nonunit sides of the loaded convex hull;
- `x_B` is the outer-contact-walk excess;
- `u_B=x_B-m`;
- `e_{BB}` is the number of loaded-loaded unit contacts; and
- `c_B=e_{BB}-(q-m)` counts loaded-loaded unit contacts beyond the unit hull sides.

Theorem 122.2 gives immediately

```math
\boxed{c_B=0,}
\tag{122.13}
```

and therefore

```math
\boxed{e_{BB}=q-m.}
\tag{122.14}
```

All loaded-loaded unit contacts are exactly the unit sides of `F`.

Canonical Section 63 then specializes its exact ledgers to

```math
\boxed{
e_{BB}=Q+2k+u_B,
}
\tag{122.15}
```

and

```math
\boxed{
c_I+s_C=m+k-2,
\qquad k=d_H+s_Z.
}
\tag{122.16}
```

In particular the high-`e_{BB}` branch can no longer store contact currency in
nonconsecutive loaded chords. It must store it on the actual cyclic force-hull
boundary.

There is also a local consequence for every harmonic attachment cell `P_r`. Any
loaded-loaded unit contact whose two endpoints lie in `A_r` is a side of the global
force hull `F`; no induced harmonic graph contains an internal loaded-loaded unit
chord.

---

## 122.4 Scope and hostile checks

1. **Only Type II.** The proof uses the canonical Type-II Hausdorff convergence of
   `F_D/D` to the diameter-one disk. It says nothing about the macroscopic inactive-
   container branch.
2. **No rate assumption.** Only `delta_D/D->0` is used. The finite criterion (122.9)
   eventually holds even if `delta_D` itself tends to infinity.
3. **No smoothness.** `F_D` remains a polygon. The proof uses support normals and the
   monotone polygonal Gauss map; no differentiability of the boundary is assumed.
4. **Long boundary arc is irrelevant.** A unit chord can have one very long
   complementary boundary arc. The proof selects the arc corresponding to the shorter
   normal sweep. If the two endpoints were nonconsecutive, that selected arc would
   still contain at least two sides.
5. **Unit separation is used at the correct place.** It supplies `|v_i|>=1` for every
   hull side. No lower bound on arbitrary cell chords is needed.
6. **Contact-isolated source points are untouched.** The theorem concerns only loaded
   vertices of the positive-contact force hull and does not extend Section 57 to
   isolated coordinates.
7. **No theorem-state mutation.** This is a proof-only structural candidate. C-II
   remains open.

## 122.5 Handoff

Combining Sections 120--122 leaves a sharper full-core problem. Section 120 forces
linear aggregate local detour. Section 121 pays every bounded defect-face contribution
from one global loaded-contact surplus. Section 122 shows that the loaded-contact
surplus cannot hide in interior loaded chords: every loaded-loaded unit contact lies on
`partial F`.

The next useful target is therefore a global payment theorem for

```math
\sum_r(L_r-2d_r)
```

using the cyclic unit/nonunit side pattern of `partial F`, or an incompatibility
between that pattern and the Woodall diameter graph/common bridge block.
