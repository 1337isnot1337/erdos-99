> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_thin_partner_star_bandwidth_audit_t18687_2026-09-17.md) · source SHA-256 `d2fb5594b510a1a077dcfdc3d3751d0c078b7e81106c842303d1e062f50a0fb8`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2a2a8e522778948b65986ac424ad7b4fa9d967a2", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_thin_partner_star_bandwidth_audit_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "085f4a716a2ec8b5124afb52a584250ae70088a8d73221c0bded42894f7c3b44"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — fifteen-spaced THIN partner-star bandwidth

**Date:** 2026-09-17  
**Reviewed:** `research/target_c_high_t_tb1_thin_partner_star_bandwidth_t18687_2026-09-17.md`  
**Certificate:** `research/verify_target_c_high_t_tb1_thin_partner_star_bandwidth_t18687.py`  
**Verdict:** **PASS at proof-only high-`t` scope.**  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The candidate combines two independent controls on the extreme leaves of one repeated-partner THIN star:

1. fifteen-spaced owner tags plus the source-wide path-bandwidth lemma force the extreme owner endpoints to be `Omega(d)` apart when the star has multiplicity `d`;
2. the two extreme owner endpoints are both longer than `D-1/(4D)` from one common partner, and the canonical source circumradius is `D/2+O(sqrt D)`, forcing those leaves only `O(D^(3/4))` apart.

The combination gives

```math
d<\left({16\,3^{1/8}\over15}+o(1)\right)D^{3/4}.
```

The proof survives review. The important scope restrictions are recorded below.

---

## 1. The acute-triangle step is valid

Let the common partner be `q` and two leaves be `p,p'`. Put

```math
a=|qp|,
\qquad b=|qp'|,
\qquad c=|pp'|.
```

THIN gives

```math
a,b>D-{1\over4D}=:\ell_D,
```

while source separation and diameter give

```math
1\le c\le D.
```

At `q`,

```math
a^2+b^2>2\ell_D^2>D^2\ge c^2
```

for `D>1`. At either leaf,

```math
\ell_D^2+1-D^2
={1\over2}+{1\over16D^2}>0,
```

so

```math
a^2+c^2>b^2,
\qquad
b^2+c^2>a^2.
```

Thus the triangle is acute, and its minimum enclosing radius is its ordinary circumradius. Since the whole source lies in the canonical circumdisk, the triangle circumradius is at most that source circumradius.

**Verdict:** PASS.

---

## 2. The common-partner leaf upper bound has the correct factor

If `theta=angle pqp'`, then

```math
c^2=(a-b)^2+4ab\sin^2(\theta/2)
\ge4\ell_D^2\sin^2(\theta/2).
```

With

```math
R_\triangle={c\over2\sin\theta},
```

this yields

```math
R_\triangle\ge {\ell_D\over2\cos(\theta/2)}.
```

The canonical source bound

```math
R_\triangle\le R_D<{D\over2}+\eta_D
```

therefore gives

```math
\cos(\theta/2)>{\ell_D\over D+2\eta_D}.
```

Using `c=2R_triangle sin(theta)` and `sin(theta)<=2sin(theta/2)` gives exactly

```math
\boxed{
c<2\sqrt{(D+2\eta_D)^2-\ell_D^2}.
}
```

There is no missing factor of two. The regression certificate checks the expansion and a numerical grid of admissible acute triangles.

**Verdict:** PASS.

---

## 3. The asymptotic coefficient is correct

With

```math
\eta_D=3^{1/4}D^{1/2},
\qquad
\ell_D=D-{1\over4D},
```

one has

```math
(D+2\eta_D)^2-\ell_D^2
=4D\eta_D+4\eta_D^2+{1\over2}-{1\over16D^2}.
```

Hence

```math
\Xi_D
=2\,3^{1/8}D^{3/4}(1+o(1)).
```

The path-bandwidth inequality contributes the factor `4` in front of the leaf distance, so

```math
15(d-1)<8\Xi_D+2\pi\sqrt3
```

and therefore

```math
\boxed{
d<\left({16\,3^{1/8}\over15}+o(1)\right)D^{3/4}.}
```

The ratio against the generic inactive near-diameter coefficient `8*3^(1/8)` is exactly `15/2=7.5`.

**Verdict:** PASS.

---

## 4. The path-bandwidth theorem applies to the extreme owner segment

The bandwidth theorem is a statement about an arbitrary straight segment between source vertices in two selected path regions. It does not require that segment to be a blocker, contact, or diameter.

For a repeated-partner star, order the distinct owner coordinates

```math
i_1<\cdots<i_d.
```

They belong to the retained Horn coordinate set, so

```math
i_d-i_1\ge15(d-1).
```

The extreme owner vertices lie in `R_{i_1}` and `R_{i_d}`. A source vertex never lies on a selected train centerline, so the region labels are unambiguous. The extreme-owner segment crosses every separating selected O--O row, and the bandwidth theorem gives

```math
i_d-i_1<4|p_1-p_d|+2\pi\sqrt3.
```

No same-host hypothesis is needed for this star bound.

**Verdict:** PASS.

---

## 5. Endpoint-disjoint extraction requires the owner-shore split

Before choosing one edge per distinct partner, the full blocker-rich family may contain a source vertex as an owner of one edge and a partner of another. Merely making partner vertices distinct would then not guarantee a matching.

The candidate correctly first fixes the shore containing the owner endpoint. Every retained blocker crosses the same selected row `tau_*`, so after this split:

- every owner lies on one complementary source shore;
- every partner lies on the other shore;
- owners are distinct because their physical owner layers are distinct;
- choosing one edge per distinct partner makes partners distinct as well.

Selected train centerlines contain no source vertices, so no source vertex lies simultaneously on both shores. The chosen family is therefore genuinely vertex-disjoint.

**Verdict:** PASS.

---

## 6. The synchronized matching and rail constants are correct

The blocker-rich row contains

```math
|T_*|>({\gamma\over80}-o(1))D.
```

The owner-shore split retains `gamma/160` density. Dividing by the sharpened star coefficient gives

```math
\boxed{
{15\gamma\over2560\,3^{1/8}}
=4.20839394782\ldots\times10^{-10}
}
```

as the `D^(1/4)` matching coefficient.

Fixing one physical owner host and one monotone side of the one-turn partner-region word costs two further factors of two, giving

```math
\boxed{
{15\gamma\over10240\,3^{1/8}}
=1.05209848696\ldots\times10^{-10}
}
```

for the synchronized endpoint-disjoint staircase/nested rail.

The local regression certificate checks these constants directly.

**Verdict:** PASS.

---

## 7. What the theorem does not prove

The new star cap does **not** improve the exponent `D^(3/4)` in the common-partner degree bound. That exponent comes from the current canonical circumradius error

```math
R_D-{D\over2}=O(\sqrt D).
```

Consequently the endpoint-disjoint synchronized rail remains only `Omega(D^(1/4))`. The older unsynchronized superdiameter rail has a larger coefficient; the gain here is that the new matching/rail lives on the same blocker-rich row with inverse-`D` phase purification and common circumcenter flanks.

The theorem also does not show that a repeated-partner star is itself impossible. A closing continuation still needs either:

1. a stronger local circumradius/leaf-spread estimate on a phase-pure row, which would improve the `D^(3/4)` star exponent; or
2. a direct incompatibility between a single large common-partner superdiameter star and the dense near-equilateral train scaffold.

**Final verdict:** PASS. The latest THIN partner-repetition escape is quantitatively reduced, and an endpoint-disjoint ordered THIN rail can be recovered inside the same phase-pure dense-grid row, but C-II remains open.
