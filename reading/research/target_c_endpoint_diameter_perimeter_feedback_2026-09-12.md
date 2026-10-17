> Generated reading edition · [exact source](../../research/target_c_endpoint_diameter_perimeter_feedback_2026-09-12.md) · source SHA-256 `f4ae2132b582e74bd247a8d6ea6b91a5b6f33271f7aa3cfd3bcdf289677c6ec5`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6b21856f505f76f5af1c09cc5c918cf8fe16c69e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_endpoint_diameter_perimeter_feedback_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "970eda3855fe7d019fa44a9df6cb8d7091463517fdbdd41f51490d5d82f1929e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — endpoint diameter-edge/perimeter feedback

**Date:** 2026-09-12  
**Status:** proof-only endpoint reduction; theorem-state authority unchanged.  
**Classification:** proved candidate awaiting hostile audit.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note composes the audited Type-II endpoint floor from the outer-detour
diameter moment with the canonical difference-body perimeter inequality.  It gives a
small but exact feedback loop: a countersequence on the scoped Section-118 endpoint
has not only many `q-k` units, but also almost the maximal possible actual diameter
edge count and force-hull perimeter.

The implication chain is

```text
outer-walk nonnegativity
  -> q-k >= S_* D
  -> h >= q-k
  -> difference-body perimeter bound
  -> per(F) >= P_* D
```

The final numerical gap is positive, so this is not a contradiction.  Its value is
to remove a broad low-perimeter forest/cyclic regime from the current endpoint
search and to state the remaining slack in an exact reusable form.

## 1. Inputs and notation

Use the canonical post-ZF notation

```math
q=|B|,\qquad h=|H|,\qquad d_H=q-h,\qquad
k=d_H+s_Z.
```

For the Type-II endpoint covered by the proof-only outer-detour floor, put

```math
t_D={q-k\over D}.
```

The audited endpoint result gives

```math
\liminf t_D\ge S_*:=2.798596312209462\ldots .
\tag{EP.1}
```

The exact defect identity is

```math
q-k=h-s_Z.
\tag{EP.2}
```

Since `s_Z\ge0`, (EP.1)--(EP.2) imply

```math
\boxed{\liminf {h\over D}\ge S_*.}
\tag{EP.3}
```

No assumption that `s_Z=o(D)` is made.

## 2. Finite difference-body perimeter inequality

Let

```math
a_D:=\arcsin {1\over2D}.
```

The audited difference-body theorem applies to the full actual diameter graph.  Its
projective diameter directions are pairwise separated by at least `2a_D`.  If `h`
directions are placed in cyclic order, concavity of `sin(g/2)` gives

```math
\operatorname{per}(F)
\ge h-1+2D\cos((h-1)a_D).
\tag{EP.4}
```

The finite right side need not be asserted monotone at the last lattice step near
`h=\pi D`; the asymptotic argument below avoids that unnecessary claim.  The bound
`h\le\pi D` follows from `h\le q\le\operatorname{per}(F)\le\pi D`.  On any
subsequence, pass to `h/D\to y\in[S_*,\pi]`.  Since
`a_D=1/(2D)+O(D^{-3})`, (EP.4) gives

```math
\liminf {\operatorname{per}(F)\over D}
\ge y+2\cos(y/2).
```

The function `y+2\cos(y/2)` is increasing on `[S_*,\pi]` (strictly before `\pi`),
so

```math
\boxed{
\liminf {\operatorname{per}(F)\over D}
\ge S_*+2\cos(S_*/2)
=:P_*=3.139913777927318\ldots .
}
\tag{EP.5}
```

The universal diameter-perimeter inequality is `\operatorname{per}(F)\le\pi D`.
Consequently the endpoint has the explicit remaining slack

```math
\boxed{
0\le {\pi D-\operatorname{per}(F)\over D}
\le \pi-P_*+o(1)
=0.001678875662475\ldots+o(1).
}
\tag{EP.6}
```

## 3. Equivalent area feedback

The same audited difference-body module gives, for a subsequence with `h/D\to y`,

```math
\liminf {\operatorname{area}(F)\over D^2}
\ge {y+\sin y\over4}.
\tag{EP.7}
```

The function on the right is increasing on `[0,\pi]`.  Therefore (EP.3) also gives

```math
\boxed{
\liminf {\operatorname{area}(F)\over D^2}
\ge {S_*+\sin S_*\over4}
=0.783726679476622\ldots .
}
\tag{EP.8}
```

This leaves only

```math
{\pi\over4}-{S_*+\sin S_*\over4}
=0.001671483920826\ldots
\tag{EP.9}
```

of the isodiametric area budget at the endpoint.  In the full Type-II branch the
canonical harmonic-cell area saturation is stronger and gives `area(F)/D^2\to\pi/4`;
(EP.9) is recorded because it uses only the diameter-edge feedback and remains
available whenever the endpoint composition is invoked without importing the full
near-disk conclusion.

## 4. What this removes, and what it does not

This reduction excludes any scoped endpoint subsequence with a fixed perimeter deficit
larger than `0.0016788757D` (and, through (EP.8), any corresponding fixed area deficit
larger than `0.0016714839D^2`).  It applies in both Woodall branches; no cyclic/forest
classification is used.

It does **not** close the remaining endpoint.  The positive gap in (EP.7) is real, and
the regular odd-shell geometry shows that perimeter saturation alone is compatible
with a cyclic diameter support.  In the forest branch, `d_H/D` can still be positive
but bounded by the existing `k/D<0.3444+o(1)` band; (EP.6) does not turn that band
into a contradiction.  Nor does near-maximal force-hull area provide a
source-preserving finite deformation.

The exact remaining implication is therefore

```math
\text{endpoint diameter moment}
\to\text{near-maximal diameter-edge/perimeter profile}
\to
\begin{cases}
\text{a quantitative forest stability theorem},\\
\text{a common-block/unit-contact response contradiction},\\
\text{or a finite strict-diameter descent}.
\end{cases}
```

Contact-isolated source points remain retained throughout; no full-source affine
kernel or unproved response sign is used.

**Classification:** proved candidate awaiting hostile audit; proof-only; no canonical
state mutation.
