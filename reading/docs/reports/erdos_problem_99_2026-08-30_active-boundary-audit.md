> Generated reading edition · [exact source](../../../docs/reports/erdos_problem_99_2026-08-30_active-boundary-audit.md) · source SHA-256 `864734f5a73be5dc69c2f210e926235249625baafe547536e98a30650cb25a0f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "393037b10bd69cb257b2c4fd12823eb4cc3721b9", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/erdos_problem_99_2026-08-30_active-boundary-audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f32e19f8a657f58aad8fa73d72bdd8d3e1c3418e5301397162e9a105103b5b0c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — active-boundary normal form audit

## New representative-level lemma

Assume that a triangle-free global minimizer exists for some cardinality (n), and
write its diameter as (D).  For a minimizer (A), define

```math
\mathfrak a(A)=|C(A)|+|H_D(A)|,
```

where (C(A)) is the unit-contact set and (H_D(A)) is the set of pairs at
distance (D).  Since (mathfrak a(A)) is an integer in a finite bounded range,
there is a triangle-free global minimizer maximizing it.

> **Lemma (active-boundary elimination).** A triangle-free global minimizer maximizing
> (mathfrak a) has no strict rattler: there is no (rin A) for which
> [
> 1<|r-p|<D\qquad(pin A\setminus\{r\}).
> ]

### Proof

Fix a strict rattler (r) and hold (A\setminus\{r\}) fixed.  Its strict feasible
region is

```math
U_r=\bigcap_{p\ne r}\{x:1<|x-p|<D\}.
```

The point (r) lies in (U_r).  Let (U_0) be its connected component.  It is a
nonempty bounded open set: it lies in the disk (|x-p_0|<D) for any fixed
(p_0\ne r).  Every point of (partial U_0) lies on at least one of the finitely
many circles

```math
|x-p|=1,
\qquad |x-p|=D.
```

The boundary of a nonempty bounded open planar set is infinite, whereas the
intersection points of distinct circles in this finite family form a finite set.
Consequently there is (x\in\partial U_0) lying on exactly one circle.  Approaching
(x) from (U_0) shows that replacing (r) by (x) preserves all inequalities as

```math
1\le |x-p|\le D.
```

No original diameter pair uses (r), so an old pair at distance (D) remains.  The
new configuration is therefore another global minimizer of diameter (D).

If the unique active circle has radius (D), the new point has no unit neighbor.  If
it has radius (1), the new point has exactly one unit neighbor.  In either case no
new unit equilateral triangle can appear: the old fixed set was triangle-free and a
new triangle would require two unit neighbors of the moved point.  Thus the new set
is triangle-free.  All old unit contacts and old diameter pairs remain, while the
new point contributes exactly one new active pair.  This gives

```math
\mathfrak a(A')=\mathfrak a(A)+1,
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
contradicting maximality.  Hence no strict rattler exists. \(square)
```



## Consequences

This gives the exact existence alternative

```math
\boxed{
\text{if a triangle-free global minimizer exists, one exists with no strict rattlers.}
}
```

It is useful because the canonical flexible-branch analysis also deliberately opens
forest edges and produces strict rattlers.  Those rattlers are valid probes of the
source-capacity problem, but they are not an invariant of the set of all
triangle-free minimizers.  A proof may choose either representative for a given
purpose, but a transition between the two must be proved rather than assumed.

The lemma does **not** prove Erdős Problem #99.  It does not imply first-order
jamming: a point with one or more contacts can still move through a feasible region,
and a re-termination may preserve the active-pair count by exchanging one active
pair for another.  It also does not transfer the source-specific Schur response or
the Target A Hall surplus.  The exact Target A endpoint remains

```math
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
```

The result should therefore be used as a normal-form audit, not as a closure of the
strict-rattler branch.
