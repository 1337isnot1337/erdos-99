> Generated reading edition · [exact source](../../research/audit_target_c_section146_qk_corollary_endpoint_exclusion.md) · source SHA-256 `7dea1e5761de29f77345d9d908ba71b564eac6ad4a4a174e3e614ea8e06ae430`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a9405f889bc663bf1b6d9e6e46698c588a853b7c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/audit_target_c_section146_qk_corollary_endpoint_exclusion.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4e59a55fe9f3835116aa34599c0062b57402805b427167f54ad3df103ddd240c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Section-146 `q-k` corollary and endpoint exclusion

**Date:** 2026-09-12  
**Target:** `research/target_c_section146_qk_corollary_endpoint_exclusion.md`  
**Disposition:** PASS at proof-only / audited-working dependency scope  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Claims under audit

The source makes two claims downstream of the audited-working structural omnibus
§§142–146:

1. §146.5 already implies the stronger scalar floor
   
   ```math
   \liminf (q-k)/D\ge
   c_*={4\over9}(\pi+\sqrt{\pi/(2\sqrt3)});
   ```

2. no Type-II survivor sequence can attain equality at this floor.

The second claim uses the equality structure of §142 and a new outer-edge direction
measure argument. The theorem-state remains unchanged.

---

## 2. The `q-k` corollary from §146.5 — PASS

Audited-working §146.5 is

```math
\liminf {1\over D}
\left(h-{d_H\over9}-{10s_Z\over9}\right)\ge c_*.
```

The canonical definitions are

```math
d_H=q-h,
\qquad
k=d_H+s_Z.
```

Therefore exactly

```math
q-k=h-s_Z
=\left(h-{d_H\over9}-{10s_Z\over9}\right)+{k\over9}.
```

Since `k>=0`, the claimed `q-k` floor follows immediately. No limit-direction subtlety
is present because the comparison is pointwise before taking liminf.

This corollary was not stated in §146, whose displayed consequence emphasized `h/D`,
but it is logically stronger for the loaded-hull ledger because `q-k` is exactly the
currency in `b+Q=2(q-k)`.

**Verdict:** PASS.

---

## 3. Equality normal form — PASS

Assume `(q-k)/D -> c_*`. Since

```math
q-k=E_D+k/9,
\qquad
E_D:=h-d_H/9-10s_Z/9,
```

and `liminf E_D/D>=c_*`, nonnegativity of `k` forces

```math
k/D\to0.
```

Because `k=d_H+s_Z` with both terms nonnegative,

```math
d_H/D,s_Z/D\to0,
\qquad
h/D,q/D\to c_*.
```

Audited-working (146.2) then gives

```math
\liminf f/D\ge
s_*-c_*/4,
\qquad s_*:=\sqrt{\Delta_2}.
```

The algebra

```math
s_*-c_*/4=(8s_*-\pi)/9=2c_*-\pi=:\phi_*
```

was recomputed and is correct.

The exact ledger

```math
b=2h-Q-2s_Z
```

and Type-II `per(F)/D->pi`, `per(F)<=b`, yield

```math
\limsup Q/D\le2c_*-\pi=\phi_*.
```

Since `f<=Q`, both converge to `phi_*`; consequently `Q-f=o(D)` and
`b/D->pi`. Because `per(F)/D->pi` as well,

```math
b-per(F)=o(D).
```

No unproved equality classification is used.

**Verdict:** PASS.

---

## 4. Equality in the §142 phase inequalities — PASS

The exact stopped-train ledger from §142 is

```math
T=q+2f-k=(q-k)+2f.
```

Hence at the endpoint

```math
T/D\to x=c_*+2\phi_*,
\qquad
q/T\to y=c_*/x.
```

If `a` denotes the total atomic mass of a weak train-direction limit, §142 proves

```math
2s_*\le xa,
\qquad
y\le2(1-a).
```

The endpoint constants satisfy

```math
x(1-y/2)=x-c_*/2=2s_*.
```

Therefore

```math
2s_*\le xa\le x(1-y/2)=2s_*,
```

so both inequalities are equalities and

```math
1-a=y/2.
```

Thus the non-atomic train population has asymptotic size

```math
(1-a)T=(c_*/2+o(1))D.
```

This conclusion retains singleton trains because §142 defines `T` as the component
count of the full auxiliary graph on all positive contact edges, with contact edges
incident to no strict rhombus represented by singleton paths.

**Verdict:** PASS.

---

## 5. Uniform outer-edge direction measure — PASS

The source defines

```math
\nu_D=D^{-1}\sum_{e\in\partial_{out}}\delta_{\phi_e}.
```

Its total mass is `b/D->pi`.

All loaded force-hull vertices have distinguished exterior occurrences on the outer
contact walk, while every outer-walk vertex lies in the positive core and hence in
`F`. Thus the convex hull of the walk vertices is exactly `F`.

For the projected total variation

```math
V_D(\theta)=\sum_e|e\cdot n_\theta|,
```

a closed walk visiting both support extrema has

```math
V_D(\theta)\ge2w_F(\theta).
```

Occurrence repetitions do not affect this inequality. Integrating gives

```math
\int V_D=2b,
\qquad
\int 2w_F=2\operatorname{per}(F).
```

Therefore `b-per(F)=o(D)` and the Type-II uniform width convergence imply

```math
V_D/D\to2
```

in `L^1`.

The uniqueness step is also correct. For the `pi`-periodic kernel

```math
g(\theta)=|\cos\theta|,
```

one has distributionally

```math
g''+g=2\delta_{\pi/2\pmod\pi}.
```

Thus if a finite projective measure `nu` has constant cosine transform

```math
\int g(\theta-\phi)d\nu(\phi)=2,
```

applying `d^2/dtheta^2+1` gives a translate of `nu` equal to Lebesgue measure.
Hence `nu` itself is Lebesgue measure. This avoids any unproved regularity or Fourier
inversion assertion.

The weak-limit passage is safe because the masses are bounded and the cosine kernel
is jointly continuous and uniformly Lipschitz in `theta`.

**Verdict:** PASS.

---

## 6. Outer-occurrence capacity of non-atomic trains — PASS

This is the main multiplicity check.

In §142 every complete stopped train is an auxiliary path. A non-singleton path has
two terminal contact edges; each can contribute at most one outer-face occurrence. A
singleton path consists of one contact edge; if it is a bridge, its two face-side
occurrences may both be outer. Thus in every case

```math
\boxed{\text{one stopped train contributes at most two outer-face occurrences}.}
```

This is exactly the endpoint-count fact already used in the audited-working proof of
§142.6.

Choose finitely many atoms carrying train mass at least `a-epsilon`, and choose their
disjoint direction neighborhoods with boundaries carrying no limiting train measure.
Weak convergence gives at most

```math
(1-a+O(\epsilon)+o(1))T
```

trains outside those neighborhoods. They can supply at most twice that many outer
occurrences. At the equality endpoint this normalized capacity tends to

```math
2(1-a)x=c_*.
```

The entire outer walk has normalized length `pi`. Since `pi-c_*>0`, a positive
normalized mass of outer occurrences must lie in the shrinking atom neighborhoods.

But the preceding section proves `nu_D -> dphi`, so a finite union of arcs of total
length tending to zero has limiting outer-occurrence mass tending to zero. This is the
required contradiction.

The phase-to-edge identification is explicit: §142.1 assigns one projective contact
direction to each auxiliary stopped-train component, so every outer contact-edge
occurrence of a train in a selected phase neighborhood lies in the same projective
direction neighborhood. The argument does not assume that the outer walk is tangent
to the force hull.

The argument does not assume that an outer edge borders a rhombus. Singleton trains
are explicitly included, so bridges and defect-boundary contact edges are not lost.

**Verdict:** PASS.

---

## 7. Scope and authority

The proof depends essentially on audited-working, noncanonical §§142 and 146. It is
therefore downstream proof-only mathematics even though its convex-geometry part uses
canonical Type-II near-disk convergence.

The theorem does not:

- promote §§142–146;
- close the macroscopic inactive-container branch;
- prove a finite explicit positive gap above `c_*`;
- force an exact unit equilateral triangle;
- construct a strict sub-`D` competitor;
- delete contact-isolated source points; or
- extend the Section-57 affine-kernel theorem to them.

The safe conclusion is:

```math
\boxed{
\text{assuming audited-working §§142–146, no Type-II survivor sequence attains }
(q-k)/D\to c_*.
}
```

A uniform separation statement requires the usual sequence/diagonal formulation and
is not assigned a numerical constant here.

## 8. Final verdict

**PASS.** The `q-k` corollary and the endpoint exclusion are valid at proof-only scope.
This materially strengthens the full-core frontier, but C-II and Level I remain open.
