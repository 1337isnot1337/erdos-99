> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_reinhardt_sign_obstruction_2026-09-09.md) · source SHA-256 `1f1cf10680bba3f0c40c2ab9871053f4808f9d4c9bbfc77e703d4a77ebde7d38`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 6 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-840E4E5A55D7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic equality gives a Reinhardt sign equation

**Date:** 2026-09-09  
**Run type:** exact equality-class arithmetic reduction  
**Target:** Target C C-II cyclic primitive endpoint, `d_H=0`  
**Depends on:** CE exact cyclic difference-body equality in this stacked PR; elementary Minkowski polygon edge merge; elementary cyclotomic minimal polynomials  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

CE proves that the cyclic `d_H=0` endpoint has

```math
F-F=R_{2q},
```

where `R_{2q}` is the regular `2q`-gon of circumradius

```math
D=\frac1{2\sin(\pi/(2q))}
```

and side length one. The force hull `F` itself is a strictly convex equilateral `q`-gon with all side lengths one.

This report determines the exact side-direction freedom left by that equality.

After one global rotation there are signs

```math
\varepsilon_0,\ldots,\varepsilon_{q-1}\in\{+1,-1\}
```

such that the unordered side-vector set of `F` is

```math
\boxed{
\left\{
\varepsilon_j\zeta^j:0\le j<q
\right\},
\qquad
\zeta=e^{\pi i/q}.
}
\tag{RS.1}
```

Closure of the polygon is therefore exactly the Littlewood/cyclotomic equation

```math
\boxed{
P_q(\zeta)=0,
\qquad
P_q(x):=\sum_{j=0}^{q-1}\varepsilon_jx^j.
}
\tag{RS.2}
```

Two finite exclusions/classifications follow immediately.

1. If `q` is a power of two, RS.2 is impossible. Hence
   
   ```math
   \boxed{q\ne2^m.}
   \tag{RS.3}
   ```

2. If `q=p` is an odd prime, then
   
   ```math
   \boxed{P_p(x)=\pm\Phi_{2p}(x),}
   \tag{RS.4}
   ```

   the signs alternate, and the side-vector set is a rotated copy of all `p`-th roots of unity. Consequently
   
   ```math
   \boxed{F\text{ is the regular unit }p\text{-gon}.}
   \tag{RS.5}
   ```


Thus the exact cyclic endpoint has been reduced from arbitrary convex equilateral shells to the classical Reinhardt sign class, with complete rigidity at prime terminal counts and an exact arithmetic obstruction at power-of-two terminal counts.

---

## 1. Edge vectors of a planar Minkowski sum

Let

```math
v_0,\ldots,v_{q-1}
```

be the oriented side vectors of `F` in counterclockwise boundary order. Since `C=C_q`,

```math
|v_j|=1
\qquad(0\le j<q).
\tag{1.1}
```

The polygon `-F` has the side-vector multiset

```math
\{-v_0,\ldots,-v_{q-1}\}.
```

For two convex polygons, the edge-vector sequence of the Minkowski sum is obtained by merging the two cyclic edge-direction sequences. If two input edges are codirected, their vectors add and appear as one output edge; otherwise each input edge appears unchanged in the merged sequence.

For completeness, this is immediate from support-line motion. As the outer normal rotates, a Minkowski-sum vertex is the sum of the two supported vertices. At an angle where only one summand changes supported vertex, the sum boundary moves by that summand's edge vector. If both change at the same angle, the two codirected edge vectors add.

Apply this to

```math
F-F=F+(-F).
\tag{1.2}
```

Before any codirected merging, there are exactly `2q` unit input edge vectors:

```math
v_0,\ldots,v_{q-1},-v_0,\ldots,-v_{q-1}.
\tag{1.3}
```

CE says the output `F-F` is a regular polygon with exactly `2q` sides, each also of length one.

Therefore no merge can have occurred. In particular:

### Lemma RS.1 — no parallel-side collision

The `2q` vectors in (1.3) have pairwise distinct oriented directions, and they are exactly the `2q` side vectors of the regular polygon `F-F`.

`\square`

---

## 2. One choice from each antipodal pair

The side directions of a regular `2q`-gon are equally spaced by

```math
\frac\pi q.
```

After one common rotation, identify its unit side-vector set with

```math
\boxed{
\{\zeta^j:0\le j<2q\},
\qquad
\zeta=e^{\pi i/q}.
}
\tag{2.1}
```

The antipodal pairs are

```math
\{\zeta^j,-\zeta^j\}
=
\{\zeta^j,\zeta^{j+q}\},
\qquad0\le j<q.
\tag{2.2}
```

By Lemma RS.1,

```math
\{v_0,\ldots,v_{q-1},-v_0,\ldots,-v_{q-1}\}
=
\{\zeta^j:0\le j<2q\}
\tag{2.3}
```

as sets.

For each antipodal pair (2.2), `F` must contain exactly one member.

- It cannot contain neither, because then (2.3) would miss both directions.
- It cannot contain both, because negating the side-vector set would reproduce the same two directions, leaving some other antipodal pair absent from the `2q` distinct output directions.

Hence there are unique signs `epsilon_j in {+-1}` such that the side-vector set of `F` is

```math
\boxed{
\{\varepsilon_j\zeta^j:0\le j<q\}.
}
\tag{2.4}
```

This proves RS.1.

No claim is made about the order `j=0,...,q-1` along the boundary of `F`; the convex boundary order is obtained by sorting the selected oriented directions. Equation (2.4) is an unordered direction classification.

---

## 3. Polygon closure is a Littlewood equation

Every closed polygon has zero total side vector. Therefore

```math
\sum_{j=0}^{q-1}\varepsilon_j\zeta^j=0.
\tag{3.1}
```

Define

```math
P_q(x)=\sum_{j=0}^{q-1}\varepsilon_jx^j
\in\mathbb Z[x].
\tag{3.2}
```

Every coefficient is `+1` or `-1`, and (3.1) is exactly

```math
\boxed{P_q(\zeta)=0.}
```

This proves RS.2. `square`

Thus the remaining geometric freedom is discrete: it is encoded by a `+-1` polynomial of degree at most `q-1` vanishing at a primitive `2q`-th root of unity.

---

## 4. Power-of-two terminal counts are impossible

Assume

```math
q=2^m
```

for some `m>=1`. Then

```math
2q=2^{m+1},
```

and `zeta` is a primitive `2^{m+1}`-th root of unity.

Its minimal polynomial over `Q` is

```math
\boxed{
\Phi_{2q}(x)=x^q+1,
}
\tag{4.1}
```

which has degree `q`.

But `P_q` is a nonzero polynomial of degree at most `q-1`. A nonzero rational polynomial of degree below the minimal-polynomial degree cannot vanish at `zeta`.

This contradicts RS.2. Therefore:

### Theorem RS.2 — power-of-two exclusion

The cyclic `d_H=0` endpoint cannot have

```math
\boxed{q=2^m.}
```

`\square`

This is an exact finite exclusion. It is not asymptotic and uses no KKT coefficient lower bound.

---

## 5. Odd prime terminal counts force the regular polygon

Now let

```math
q=p
```

be an odd prime. Then `zeta` is a primitive `2p`-th root of unity, whose minimal polynomial is

```math
\boxed{
\Phi_{2p}(x)
=x^{p-1}-x^{p-2}+x^{p-3}-\cdots-x+1.
}
\tag{5.1}
```

Its degree is `p-1`.

RS.2 gives `P_p(zeta)=0`. Therefore

```math
\Phi_{2p}(x)\mid P_p(x)
```

in `Q[x]`. Both have degree at most `p-1`, and `P_p` has nonzero leading coefficient `+-1`. Hence their degrees are equal and

```math
\boxed{P_p(x)=\pm\Phi_{2p}(x).}
\tag{5.2}
```

Thus, after possibly reversing all signs,

```math
\varepsilon_j=(-1)^j.
\tag{5.3}
```

The selected side vectors are consequently

```math
\varepsilon_j\zeta^j
=(-\zeta)^j.
\tag{5.4}
```

Because `p` is odd,

```math
(-\zeta)^p
=(-1)^p\zeta^p
=(-1)(-1)=1,
```

and `-zeta` is a primitive `p`-th root of unity. Hence the side-vector set of `F` consists of the `p` equally spaced unit vectors

```math
1,\omega,\ldots,\omega^{p-1}
```

up to one global rotation, with `omega` primitive of order `p`.

Sorted by angle, these are the side vectors of the regular unit `p`-gon. A convex polygon is determined up to translation by its cyclic side-vector sequence. Therefore:

### Theorem RS.3 — prime rigidity

If the cyclic `d_H=0` endpoint has an odd prime number `p` of loaded terminals, then

```math
\boxed{F\text{ is the regular unit }p\text{-gon}.}
```

`\square`

This does not assert that the entire source is the regular polygon. CY already shows that the source contains a quadratic population of contact-isolated points outside the `O(D)` mechanical shell.

---

## 6. Relation to Reinhardt equality

The sign equation RS.2 is the natural discrete equality condition for an equilateral polygon whose difference body is the regular `2q`-gon. To avoid importing any external classification, this report uses **Reinhardt sign class** only as shorthand for the explicit condition

```math
\boxed{
\exists\varepsilon_j\in\{\pm1\}:
\sum_{j=0}^{q-1}\varepsilon_j e^{\pi i j/q}=0.
}
\tag{6.1}
```

Everything proved here follows from (6.1) directly.

For composite non-power-of-two `q`, non-alternating sign solutions are not excluded by the elementary minimal-polynomial argument. No claim of regularity is made in that case.

---

## 7. Regression audit

### Regular odd shell

For odd `q`, the alternating sign choice

```math
\varepsilon_j=(-1)^j
```

has

```math
\sum_j\varepsilon_j\zeta^j
=\sum_j(-\zeta)^j=0,
```

because `-zeta` is a nontrivial `q`-th root of unity. Thus the regular odd shell lies in RS exactly as required.

### Even non-power-of-two counts

Not excluded. The power-of-two proof uses the special degree identity

```math
\deg\Phi_{2q}=q.
```

For a general even `q` with an odd factor, the cyclotomic degree is smaller and a `+-1` multiple is not ruled out by degree alone.

### Prime endpoint

RS.3 classifies the force hull, not the isolated source population. The regular-shell mechanical geometry remains a valid local regression until a source-wide replacement/capacity theorem excludes its quadratic rattler cloud.

### Difference-body equality alone

The arithmetic step uses that `F` has exactly `q` unit sides. A generic convex body with the same regular difference body need not satisfy the sign equation.

---

## 8. What this changes

The cyclic `d_H=0` branch now has the exact chain

```text
CY cyclic endpoint
    -> CE: F-F is regular 2q-gon of side one
    -> RS: one side vector chosen from each antipodal regular direction
    -> P_q(exp(pi i/q))=0 with all coefficients +-1.
```

Hence:

- every power-of-two terminal count is excluded exactly;
- every odd-prime terminal count forces a regular mechanical shell;
- all other terminal counts are reduced to an explicit finite sign/cyclotomic class.

This is substantially narrower than the previous statement that the cyclic force hull is merely an arbitrary convex equilateral polygon.

---

## 9. Next theorem

There are two concrete next attacks.

1. **Arithmetic/combinatorial:** classify the allowed sign words further under the actual diameter-thrackle incidence and triangle-free unit-separation constraints, not only polygon closure.
2. **Source-wide:** in the prime case the shell is exactly regular. Combine that exact shell with CY's
   
   ```math
   n-q>\Delta D^2-\pi D
   ```

   contact-isolated population and the insertion/outer-shell machinery to seek a strict sub-`D` replacement or capacity contradiction.

A theorem excluding all nonregular sign words would reduce the entire `d_H=0` endpoint to the regular odd-shell regression.

---

## 10. Promotion recommendation

**Hold as a stacked report.**

RS depends on CE, which depends on the report-level CY endpoint in PR #118. No canonical file should be changed until that dependency chain is independently audited.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

CE gives in cyclic d_H=0:
    F-F = regular 2q-gon R_{2q}
with circumradius D and side length one.
F itself is a strict convex unit q-gon.

Minkowski edge merging for F+(-F) has 2q unit input edges and the output R_{2q}
has exactly 2q unit edges. Hence no codirected merge occurs. After rotation, if
    zeta=exp(pi i/q),
the q side vectors of F choose exactly one member of each antipodal pair:
    {epsilon_j zeta^j : 0<=j<q}, epsilon_j in {+-1}.
Polygon closure is therefore
    P_q(zeta)=0,
    P_q(x)=sum epsilon_j x^j.

Consequences:
- q=2^m is impossible because Phi_{2q}(x)=x^q+1 has degree q>deg P_q.
- if q=p is odd prime, Phi_{2p}|P_p and both have degree p-1, so
      P_p=+-Phi_{2p};
  the signs alternate and F is the regular unit p-gon.

Next: impose actual diameter-thrackle incidence and source-wide rattler geometry on
the remaining composite Reinhardt sign words.
```
