> Generated reading edition · [exact source](../../../docs/reports/target_c_oblique_lattice_pick_comparison_2026-09-14.md) · source SHA-256 `e78b307c7ea57a4172834861344a75a60107ed8cc9bbb7c01ba88c1fd2e2db5e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 4 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-5C73D01BA7E7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — exact lattice-point comparison for one oblique affine source

**Date:** 2026-09-14  
**Repository HEAD when written:** `f174a9eb5d8de320ce9929223d71f5d6efbcb5af`  
**Status:** proof-only, independently checked; not promoted  
**Scope:** one exact two-direction unit oblique lattice; source-cardinality exact

## Result

Let (u,v) be unit vectors with

```math
  \frac{\pi}{3}<\theta:=\angle(u,v)\le\frac{\pi}{2},
  \qquad \Lambda_\theta=\mathbb Zu+\mathbb Zv,
  \qquad s=\sin\theta,
  \qquad a_0=\frac{\sqrt3}{2}.
```

Let (A\subset\Lambda_\theta) be finite and put

```math
  n=|A|,
  \qquad K=\operatorname{conv}(A),
  \qquad D=\operatorname{diam}(A).
```

Assume $`K`$ is two-dimensional. If

```math
\boxed{
  \frac{\pi D^2}{4}\left(\frac1{a_0}-\frac1s\right)
  > \frac{\pi D}{2}+1,
}
\tag{PL.1}
```

then there is an (n)-point subset (B) of a unit triangular lattice with

```math
  \operatorname{diam}(B)<D.
\tag{PL.2}
```

Consequently (A) cannot be a global minimum-diameter (n)-point
unit-separated configuration. The comparison keeps all (n) source points; it
does not delete contact-isolated points or replace the source by a scaffold.



**Source formatting excerpt (unbalanced inline math in the original):**

```text
The reflected statement holds for a basis angle in
\([\pi/2,2\pi/3)), after replacing (v) by (-v). The endpoint
\(\theta=\pi/3) is excluded: the full lattice then contains unit
equilateral triangles and the density difference in (PL.1) vanishes.
```



The source-specific form is slightly stronger. If (b_\Lambda(K)) denotes the
number of lattice points on the boundary of the lattice polygon (K), then it
suffices that

```math
  \frac{\operatorname{area}(K)}s+\frac{b_\Lambda(K)}2+1
  < \frac{\pi D^2}{4a_0}.
\tag{PL.3}
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
Condition (PL.1) is the uniform consequence of (PL.3), using
\(\operatorname{area}(K)\le\pi D^2/4\) and
$`b_\Lambda(K)\le\operatorname{per}(K)\le\pi D`$.
```



## Proof

### 1. The oblique lattice is feasible and triangle-free


**Source formatting excerpt (unbalanced inline math in the original):**

```text

For (z=iu+jv\ne0), if (ij\ge0), then, since
\(\cos\theta\ge0),
```



```math
  |z|^2=i^2+j^2+2ij\cos\theta\ge i^2+j^2\ge1.
```

If (ij<0), write (i=a), (j=-b) after changing signs if necessary,
where (a,b\ge1). Then

```math
  |z|^2=(a-b)^2+2ab(1-\cos\theta)>1,
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
because (2(1-\cos\theta)>1) in the open range
\(\theta>\pi/3\). Thus every finite subset of $`\Lambda_\theta`$ is
unit-separated. The only unit lattice differences are
$`\pm u,\pm v`$.
```



In particular, a unit equilateral triangle cannot occur in the full oblique
lattice in this open range: from one vertex the two other vertices would have
to be two distinct members of $`\{\pm u,\pm v\}`$, while their difference
has length either $`|u-v|>1`$ or $`|u+v|>1`$. This triangle-free observation
is a regression check, not an input to the diameter comparison.

### 2. Exact population bound from the lattice polygon

Every vertex of (K) belongs to $`\Lambda_\theta`$, so (K) is a lattice
polygon for the lattice $`\Lambda_\theta`$. Affinely map $`\Lambda_\theta)
to \(\mathbb Z^2`$. Pick's theorem, transformed back to Euclidean area,
states that the number (N_\Lambda(K)) of all lattice points in (K) is

```math
  N_\Lambda(K)
  =\frac{\operatorname{area}(K)}s
    +\frac{b_\Lambda(K)}2+1.
\tag{PL.4}
```

Since (A\subseteq K\cap\Lambda_\theta),

```math
  n\le N_\Lambda(K).
\tag{PL.5}
```

To obtain a uniform version, subdivide every boundary edge of (K) at the
successive lattice points on that edge. Consecutive points in this subdivision
differ by a nonzero lattice vector, hence are at Euclidean distance at least
one by Step 1. Therefore

```math
  b_\Lambda(K)\le\operatorname{per}(K)\le\pi D,
\tag{PL.6}
```

where the final inequality is Cauchy's perimeter-diameter bound. The
isodiametric inequality gives
$`\operatorname{area}(K)\le\pi D^2/4`$. Combining (PL.4)--(PL.6),

```math
  n
  \le \frac{\pi D^2}{4s}+\frac{\pi D}{2}+1.
\tag{PL.7}
```

### 3. An exact-cardinality triangular competitor

Let $`\Lambda_\triangle`$ be any unit triangular lattice. For a translate
$`\Lambda_\triangle+t`$, let

```math
  M(t)=\bigl|(\Lambda_\triangle+t)\cap B^\circ(0,D/2)\bigr|,
```

where the disk is open. Averaging over one fundamental parallelogram of the
triangular lattice gives the exact identity

```math
  \frac1{a_0}\int_{Q_\triangle}M(t)\,dt
  =\frac{\pi D^2}{4a_0}.
\tag{PL.8}
```

This is just translation averaging of the indicator of the disk; the open
boundary has measure zero. If (PL.3) holds, then (PL.5) and (PL.8) imply
that the average of (M(t)) is strictly greater than (n). Hence some
translate has at least (n+1) sites in the open disk. Select any (n) of
them and call the result (B). Each pair of selected sites is at distance at
least one, because they lie in a unit triangular lattice, while every pair is
at distance strictly less than (D), because both sites lie in the open disk
of radius (D/2). Thus (B) has exactly (n) points and
$`\operatorname{diam}(B)<D`$.

Finally, (PL.1), (PL.7), and (s>a_0) give

```math
  n
  \le \frac{\pi D^2}{4s}+\frac{\pi D}{2}+1
  < \frac{\pi D^2}{4a_0},
```

so the uniform condition also implies (PL.3). This proves the theorem.

If (K) is a segment, unit separation gives (n\le D+1). For all
sufficiently large (D),
$`D+1<\pi D^2/(4a_0)`$, and the same open-disk averaging gives a strict
smaller-diameter triangular competitor. Thus the lower-dimensional case is
also harmless asymptotically.

## Quantitative consequence and exact limitation

Failure of (PL.1) is necessary for an exact oblique-lattice global minimizer:

```math
  s-a_0
  \le \frac{2a_0s}{D}+\frac{4a_0s}{\pi D^2}.
\tag{PL.9}
```

Near the triangular endpoint, (s-a_0=\tfrac12(\theta-\pi/3)+O((\theta-
\pi/3)^2)), so the critical angular scale remains (O(D^{-1})). A safe
uniform form for $`\theta\in(\pi/3,\pi/2]`$ is

```math
  0<\theta-\frac\pi3
  \le \frac8D+\frac{16}{\pi D^2}
\quad\text{whenever }D\text{ is large enough that the right side is }<\frac\pi6.
\tag{PL.10}
```

The coefficient in (PL.10) is intentionally not optimized. The exact useful
statement is (PL.1), or better the source-specific condition (PL.3). The
improvement over a fundamental-cell thickening estimate is that the boundary
cost is the actual lattice boundary count (b_\Lambda(K)/2), not an added
two-dimensional boundary layer. It therefore sharpens the affine-lattice
subroute but does not remove inverse-diameter shear.

No inference is made from this theorem to a general C-II source. Canonical
coherent grains need not be one exact affine lattice, and their source may have
holes, phase interfaces, exceptional faces, or contact-isolated points. The
macroscopic-container branch is untouched.

## Proof-obligation ledger

- **Proved here:** (PL.1)--(PL.10), under the exact lattice and convex-hull
  hypotheses above.
- **Trusted standard input:** the affine form of Pick's theorem, the
  isodiametric inequality, Cauchy's perimeter-diameter inequality, and the
  elementary translation-average identity (PL.8).
- **Exact regression:** a vanishing-shear lattice with
  $`\theta-\pi/3=O(D^{-2})`$ fails (PL.1), so the theorem does not falsely
  exclude the known critical-scale model.
- **Not proved:** an affine chart for arbitrary full-core minimizers; a
  source-preserving deformation of a non-affine rhombic grain; any closure of
  the aggregate detour or macroscopic-container branch.

**Level-I status:** STILL OPEN. This artifact is a restricted, source-level
comparison only.
