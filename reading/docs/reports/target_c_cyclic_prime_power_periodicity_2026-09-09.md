> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_prime_power_periodicity_2026-09-09.md) · source SHA-256 `28e7a1b32a5a2cf621f9e237ded37dae1a6896d407e1b9022d6dbc38ec4e9cda`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-2F2A6C35FFA6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — prime-power odd part forces periodic Reinhardt symmetry

**Date:** 2026-09-09  
**Run type:** exact cyclotomic classification  
**Target:** Target C cyclic `d_H=0` Reinhardt endpoint  
**Depends on:** RS sign-word closure in this PR  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

RS writes every exact `d_H=0` Reinhardt shell, after one rotation, with unit side vectors

```math
\epsilon_j\zeta^j,
\qquad
0\le j<q,
\qquad
\epsilon_j\in\{\pm1\},
\qquad
\zeta=e^{\pi i/q},
```

and closure

```math
\sum_{j=0}^{q-1}\epsilon_j\zeta^j=0.
\tag{PP.1}
```

RS already gives two endpoint classifications:

- if `q` is a power of two, no such sign word exists;
- if `q=p` is an odd prime, the signs alternate and the shell is regular.

The same field-basis argument classifies every `q` whose odd part is a prime power.

### Theorem PPW — block antiperiodicity

Let

```math
\boxed{q=2^a p^b}
\tag{PP.2}
```

with `a>=0`, `b>=1`, and `p` an odd prime. Put

```math
 m:=q/p=2^a p^{b-1}.
```

Then every Littlewood closure (PP.1) has the exact form

```math
\boxed{
(\epsilon_0,\ldots,\epsilon_{q-1})
=
(A,-A,A,-A,\ldots,A),
}
\tag{PP.3}
```

where

```math
A=(a_0,\ldots,a_{m-1})\in\{\pm1\}^m
```

is arbitrary and there are exactly `p` consecutive blocks.

Equivalently,

```math
\boxed{
\epsilon_{j+m}=-\epsilon_j
\qquad(0\le j<q-m).
}
\tag{PP.4}
```

Thus every such exact Reinhardt polygon is periodic rather than sporadic.

Geometrically the shell has exact `p`-fold rotational symmetry. In particular its unique odd diameter cycle is invariant under a free order-`p` action, so

```math
\boxed{p\mid r,}
\tag{PP.5}
```

where `r` is the diameter-cycle length.

The pendant-leaf/Reuleaux composition is repeated in `p` rotational copies.

---

## 1. Reduce to a primitive `2p`-th root

Put

```math
\eta:=\zeta^m.
```

Since `q=mp`,

```math
\eta^p=\zeta^q=-1,
```

and `eta` has exact order `2p`.

The field degrees are

```math
[\mathbb Q(\zeta):\mathbb Q]
=\varphi(2q)
=m(p-1),
```

and

```math
[\mathbb Q(\eta):\mathbb Q]
=\varphi(2p)=p-1.
```

Therefore

```math
\boxed{
[\mathbb Q(\zeta):\mathbb Q(\eta)]=m.
}
\tag{1.1}
```

But `zeta` satisfies

```math
X^m-\eta=0
```

over `Q(eta)`. Since the extension degree is exactly `m`, this polynomial is the minimal polynomial of `zeta` over `Q(eta)`. Hence

```math
\boxed{
1,\zeta,\ldots,\zeta^{m-1}
}
\tag{1.2}
```

is a basis of `Q(zeta)` over `Q(eta)`.

---

## 2. Every residue-class block vanishes separately

Group the closure sum (PP.1) by residues modulo `m`:

```math
\begin{aligned}
0
&=\sum_{j=0}^{mp-1}\epsilon_j\zeta^j\\
&=\sum_{r=0}^{m-1}
\zeta^r
\left(
\sum_{k=0}^{p-1}\epsilon_{r+km}\eta^k
\right).
\end{aligned}
\tag{2.1}
```

By the basis independence (1.2), every coefficient in parentheses must vanish:

```math
\boxed{
B_r(\eta)=0,
\qquad
B_r(X):=
\sum_{k=0}^{p-1}\epsilon_{r+km}X^k.
}
\tag{2.2}
```

Each `B_r` has degree exactly `p-1` and every coefficient is `+-1`.

The minimal polynomial of the primitive `2p`-th root `eta` is

```math
\Phi_{2p}(X)
=X^{p-1}-X^{p-2}+\cdots-X+1
=\sum_{k=0}^{p-1}(-1)^kX^k.
\tag{2.3}
```

Since `B_r(eta)=0` and both polynomials have degree `p-1`,

```math
B_r=\pm\Phi_{2p}.
```

Therefore for some sign `a_r in {+-1}`,

```math
\boxed{
\epsilon_{r+km}=a_r(-1)^k.
}
\tag{2.4}
```

Collecting the residue signs

```math
A=(a_0,\ldots,a_{m-1})
```

gives exactly the block form (PP.3). `square`

---

## 3. Converse

The classification is exact, not merely necessary.

Take any

```math
A=(a_0,\ldots,a_{m-1})\in\{\pm1\}^m
```

and define

```math
\epsilon_{r+km}=a_r(-1)^k.
```

Then

```math
\sum_{k=0}^{p-1}(-1)^k\eta^k
=\Phi_{2p}(\eta)=0,
```

so every residue block in (2.1) vanishes. Therefore

```math
\sum_j\epsilon_j\zeta^j=0.
```

Hence **every** `+-1` block `A` produces an algebraically closed Reinhardt side word in this prime-power-odd-part class.

The remaining convex polygon is obtained, as in RS, by sorting the selected unit directions in cyclic order.

---

## 4. Exact rotational symmetry

Let

```math
s_j:=\epsilon_j\zeta^j
```

be the directed unit side vectors.

For `j=r+km`, equation (2.4) gives

```math
\begin{aligned}
s_{r+km}
&=a_r(-1)^k\zeta^r\eta^k\\
&=a_r\zeta^r(-\eta)^k.
\end{aligned}
\tag{4.1}
```

Put

```math
\omega:=-\eta.
```

Since `p` is odd,

```math
\omega
=e^{2\pi i (p+1)/(2p)}
```

is a primitive `p`-th root of unity: `(p+1)/2` is coprime to `p`.

Thus for each fixed residue `r`, the `p` side vectors

```math
s_r,s_{r+m},\ldots,s_{r+(p-1)m}
```

form one complete rotation orbit

```math
s_r,\omega s_r,\ldots,\omega^{p-1}s_r.
```

Therefore the complete side-vector multiset is invariant under rotation by `omega`.

A convex polygon is determined up to translation by its cyclically ordered directed side vectors. Rotating the shell by `omega` produces the same side-vector multiset and hence a translate of the original shell. Translating to its centroid removes that translation.

### Corollary PPW.1 — shell symmetry

After centering,

```math
\boxed{\omega F=F.}
\tag{4.2}
```

So `F` has exact `p`-fold rotational symmetry.

---

## 5. Diameter graph and Reuleaux composition inherit the symmetry

The rotation `omega` is an isometry preserving `F` and its shell-vertex set. Therefore it preserves all pairwise distances among shell vertices and in particular the full shell diameter graph `H`.

In the `d_H=0` endpoint, `H` has one unique odd cycle. An automorphism of `H` must preserve that unique cycle setwise.

No nontrivial rotation about the polygon center fixes a shell vertex. Hence the order-`p` action is free on the cycle vertices. Therefore

```math
\boxed{p\mid r.}
```

The same rotation maps each cycle vertex together with all of its pendant diameter leaves to the corresponding rotated star. Hence the leaf counts and the LC arc composition repeat on `p` rotational orbits.

In particular, if the cycle vertices are indexed compatibly with the symmetry, then for

```math
r=p\tau
```

one may choose the indexing so that

```math
\boxed{
\ell_{i+\tau}=\ell_i
\qquad(0\le i<r-\tau).
}
\tag{5.1}
```

Thus the complete Reuleaux composition is `p` repeats of a positive integer composition of

```math
q/p=m.
```

---

## 6. Run-word interpretation

Extend the coefficient word antiperiodically to length `2q`:

```math
\widetilde\epsilon_{j+q}=-\widetilde\epsilon_j.
\tag{6.1}
```

The selected actual side directions are the positions where

```math
\widetilde\epsilon_j=+1
```

on the regular `2q` direction grid.

Inside a `+` run, consecutive selected directions differ by one grid step, so the intervening shell vertex has diameter degree one. Across a `-` run of length `L`, consecutive selected directions differ by `L+1` grid steps, and CD identifies the intervening cycle-vertex diameter degree as `L+1`. Therefore LC's composition part is exactly

```math
\ell=L.
```

So the positive integer Reuleaux composition is the cyclic list of negative-run lengths of the antiperiodic sign word; the positive-run lengths are the same list up to the half-turn shift.

For the block form `A,-A,A,-A,...`, the extended sign word has period `2m`. Hence its run-length composition is repeated `p` times, agreeing with the geometric symmetry argument above.

---

## 7. Special cases

### `q=p`

Here `m=1`, so `A` consists of one sign. PP.3 becomes the alternating word

```math
+,-,+,-,\ldots,+
```

up to global sign. This recovers RS's prime theorem and the regular unit `p`-gon.

### `q=2^a p`

Here `m=2^a`. Every exact equality sign word is obtained from an arbitrary length-`2^a` block `A` by alternating it through `p` blocks. Thus the whole nonregular family is still exactly `p`-fold rotationally symmetric.

### power of two

If the odd part is absent, RS already shows no sign word can close.

---

## 8. Interaction with the cubic composition energy

PR #125 AE gives

```math
\sum_{i=0}^{r-1}\ell_i^3
\le(48C_W+o(1))D^2.
```

In the prime-power-odd-part class, write

```math
r=p\tau,
\qquad
q=pm,
```

and let

```math
L_0,\ldots,L_{\tau-1}
```

be one fundamental composition block. Then

```math
\sum_i\ell_i^3
=p\sum_{j=0}^{\tau-1}L_j^3,
\qquad
\sum_jL_j=m.
\tag{8.1}
```

Hence

```math
\boxed{
\sum_{j=0}^{\tau-1}L_j^3
\le
\frac{48C_W+o(1)}{p}D^2.
}
\tag{8.2}
```

This is a finite arithmetic/geometry constraint on the arbitrary block `A`. It does not yet exclude the class because `A` can have many short sign runs.

---

## 9. What this changes

The exact equality branch now has the following arithmetic split:

```text
q = 2^a:
    impossible.

q = 2^a p^b, p odd prime:
    every sign word = A,-A,A,-A,... across p blocks;
    exact p-fold rotational symmetry;
    p divides odd diameter-cycle length r;
    Reuleaux leaf composition repeats p times.

q with at least two distinct odd prime factors:
    genuinely mixed/sporadic cyclotomic cancellation may remain.
```

Thus sporadic Reinhardt behavior is confined to terminal counts with at least two distinct odd prime factors.

---

## 10. Next theorem

Two arithmetic routes are now concrete:

1. classify the mixed cancellation when `q` has at least two distinct odd primes, retaining the run-length/cubic-energy data instead of only polynomial divisibility;
2. in the prime-power class, combine `p`-fold shell symmetry with the source-wide interior population/global descent to test whether a nonsymmetric rattler cloud can coexist with the lexicographically normalized shell.

The second route must not assume that interior rattlers inherit shell symmetry; only the mechanical shell does.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

RS: P(zeta)=sum_{j<q} epsilon_j zeta^j=0, epsilon_j=+-1,
zeta primitive 2q-th root.

If q=2^a p^b with p odd prime, put m=q/p and eta=zeta^m (primitive 2p-th root).
Field degrees give
  [Q(zeta):Q(eta)]=m,
so 1,zeta,...,zeta^(m-1) are a Q(eta)-basis.
Group P by residues mod m:
  P(zeta)=sum_r zeta^r B_r(eta).
Every B_r has p coefficients +-1 and must vanish at eta. Since deg B_r=p-1 and
Phi_{2p}=sum_{k=0}^{p-1}(-1)^k X^k is minimal,
  B_r=+-Phi_{2p}.
Hence
  epsilon_{r+km}=a_r(-1)^k.
The sign word is exactly
  A,-A,A,-A,...,A
across p blocks.

Side vectors satisfy
  s_{r+km}=a_r zeta^r(-eta)^k,
and -eta is a primitive p-th root. Therefore the side-vector multiset and centered
shell have exact p-fold rotational symmetry. The unique odd diameter cycle is invariant
and the action on its vertices is free, so
  p | r.
Its leaf/Reuleaux composition repeats in p rotational copies.

Thus genuinely sporadic sign cancellation can occur only when q has at least two
distinct odd prime factors.
```
