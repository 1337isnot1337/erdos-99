> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_p2_cyclic_isogeny_irreducibility_2026-09-10.md) · source SHA-256 `460a576696663222e05f26c1112e1842a49bb3192855d5eafd45f7a6265af1bd`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E71DB4E2EE1B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`, P2: cyclic-isogeny irreducibility for every primitive rank-two pullback

**Date:** 2026-09-10  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact torus-isogeny/Smith-normal-form theorem  
**Target:** rank-two obstruction in the Schinzel large-gap mechanism for P2  
**Depends on:** PK primitive-character Kummer rigidity; GC irreducibility of the base Gaussian curve  
**External literature:** standard Smith normal form and Capelli composition theorem  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

PK proves that every primitive torus character on the Gaussian P2 curve remains Kummer-primitive. This report converts that character statement into the exact rank-two monomial-pullback theorem needed by a Schinzel-type large-gap argument.

Let

```math
K:=\mathbb Q(i),
\qquad
f(X,Y):=X^2Y^2+i(4X^2-6X+4)Y-1.
```

Work first in the Laurent ring

```math
K[X^{\pm1},Y^{\pm1}].
```

For a full-rank integer matrix

```math
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},
```

let `phi_M` be the torus isogeny whose pullback on characters is the lattice map represented by `M`. Equivalently, after choosing the usual coordinate convention, `phi_M^*f` is obtained from `f` by a rank-two monomial substitution. Transposing `M` only changes the coordinate convention and does not affect the Smith invariants used below.

### Theorem CI — cyclic-isogeny irreducibility

Assume the first Smith invariant of `M` is one, equivalently

```math
\boxed{\gcd(a,b,c,d)=1.}
\tag{CI.1}
```

Then

```math
\boxed{\phi_M^*f\text{ is irreducible in }K[X^{\pm1},Y^{\pm1}].}
\tag{CI.2}
```

After multiplication by a monomial to clear negative exponents, the resulting ordinary polynomial has no nonmonomial factorization over `K`.

Equivalently, the inverse image of the irreducible curve

```math
C:f=0
```

under every finite torus isogeny with cyclic kernel is irreducible over `Q(i)`.

### Corollary CI-S — all rank-two Schinzel pullbacks are irreducible

Suppose a rank-two matrix `M` occurs in the Schinzel/Sawin large-gap reduction and its row lattice contains a primitive integer vector, in particular a vector of the form

```math
(1,N).
```

Then `M` satisfies CI.1, so the associated monomial pullback of `f` is irreducible over `Q(i)`.

Thus the P2 Gaussian curve has **no rank-two monomial-pullback obstruction at all** in the primitive-specialization regime.

---

## 1. Smith normal form and cyclic kernel

For any full-rank integer `2 x 2` matrix `M`, Smith normal form gives

```math
U M V
=\begin{pmatrix}d_1&0\\0&d_2\end{pmatrix},
\qquad
U,V\in GL_2(\mathbb Z),
\qquad
d_1\mid d_2.
\tag{1.1}
```

The first invariant is

```math
\boxed{d_1=\gcd(a,b,c,d).}
\tag{1.2}
```

Under CI.1,

```math
d_1=1.
```

Therefore

```math
\boxed{
U M V=\operatorname{diag}(1,k),
\qquad k=|\det M|.
}
\tag{1.3}
```

The finite cokernel is consequently cyclic of order `k`.

Matrices in `GL_2(Z)` act by Laurent-monomial automorphisms on the source or target torus. Such automorphisms preserve irreducibility in the Laurent polynomial ring. Hence it is enough to prove CI after reducing the monomial map to

```math
(S,T)\longmapsto(S,T^k),
\tag{1.4}
```

but with the target coordinates `(S,V)` replaced by a unimodular monomial coordinate system.

---

## 2. The powered target coordinate is a primitive character

A unimodular target monomial change has the form

```math
S=X^pY^q,
\qquad
V=X^rY^s,
```

with

```math
\begin{pmatrix}p&q\\r&s\end{pmatrix}\in GL_2(\mathbb Z).
```

In particular

```math
\boxed{\gcd(r,s)=1.}
\tag{2.1}
```

Thus the coordinate `V`, restricted to the original curve `C`, is exactly the primitive character

```math
\chi_{r,s}=X^rY^s.
```

PK proves for every prime `p_0`

```math
\chi_{r,s}\notin K(C)^{p_0},
```

and also excludes the exceptional `-4` fourth-power class.

Consequently

```math
\boxed{T^k-\chi_{r,s}\text{ is irreducible over }K(C).}
\tag{2.2}
```

---

## 3. Capelli composition proves the diagonal pullback irreducible

Let

```math
g(S,V)
```

be the Laurent polynomial obtained from `f(X,Y)` by the unimodular target coordinate change in Section 2. Since Laurent automorphisms preserve irreducibility and GC proves `f` irreducible,

```math
g
```

is irreducible.

Multiply by a Laurent monomial if necessary so that `g` is a primitive ordinary polynomial in `V` over `K[S^{\pm1}]`. Because no nontrivial primitive character is constant on `C` (already visible from PK's nonzero divisor vector), both coordinates in a unimodular system are nonconstant on the curve; in particular `g` has positive degree in `V`.

View

```math
g(S,V)
```

as an irreducible polynomial over the field

```math
K(S).
```

Let `alpha` be the class of `V` in the function field of its curve. Then

```math
K(S)(\alpha)\cong K(C),
```

and under this identification

```math
\alpha=\chi_{r,s}.
```

The Capelli composition theorem says that

```math
g(S,T^k)
```

is irreducible over `K(S)` if and only if

```math
T^k-\alpha
```

is irreducible over `K(S)(\alpha)`.

Equation (2.2) supplies exactly that condition. Hence

```math
\boxed{g(S,T^k)\text{ is irreducible over }K(S).}
\tag{3.1}
```

Gauss's lemma, followed by undoing the source and target Laurent automorphisms from the Smith decomposition, proves CI.2. `square`

---

## 4. Why the Schinzel row-lattice hypothesis forces `d_1=1`

The rank-two large-gap reductions used by Schinzel and by Sawin--Shusterman--Stoll produce a matrix `M` with the specialization exponent vector represented as an integral combination of the rows of `M`.

For the one-parameter specialization relevant here, that vector is primitive; after the harmless fixed degree shift in the standard formulation it has the form

```math
(1,N).
```

Suppose an integer

```math
e>1
```

divided every entry of `M`. Then every integer linear combination of its rows would have both coordinates divisible by `e`. It could not equal the primitive vector `(1,N)`.

Therefore

```math
\gcd(\text{entries of }M)=1.
```

By (1.2),

```math
d_1=1.
```

Thus every rank-two monomial map admitted by the primitive large-gap relation has cyclic cokernel and falls under CI.

This proves CI-S. `square`

---

## 5. Coordinate-free formulation

The transpose convention in the literature can be a source of pointless ambiguity, so the actual invariant statement is worth recording.

Let

```math
M_T\cong\mathbb Z^2
```

be the character lattice of the target torus and

```math
M_S\cong\mathbb Z^2
```

that of the source torus. A finite monomial map induces an injective lattice map

```math
\phi^*:M_T\hookrightarrow M_S.
```

The first Smith invariant equals one if and only if the finite quotient

```math
M_S/\phi^*M_T
```

is cyclic. In that case one may choose unimodular bases in which

```math
\phi^*=\operatorname{diag}(1,k).
```

The second target basis vector is primitive. Its restriction to `C` is therefore a primitive character, and PK says its `k`th-root Kummer cover is irreducible.

This is the entire mechanism. No choice of row-versus-column matrix convention affects it.

---

## 6. Relation to GC's `+t/-t` audit

GC proved irreducibility for the special two-parameter bivariate families required by Filaseta's printed integer-coefficient theorem. CI is stronger in a different direction.

GC:

```math
\text{special explicit matrices for all }t,\ell.
```

CI:

```math
\boxed{\text{every full-rank monomial matrix with first Smith invariant }1.}
```

The latter is precisely the structural class forced by a primitive exponent vector in the rank-two Schinzel reduction.

Thus the difficult algebraic part of the Gaussian coefficient-field bridge is no longer an unverified extrapolation from the integers: rank-two pullback irreducibility has been proved directly over `Q(i)` for the P2 curve.

What remains is to verify the scope of the **large-gap reduction theorem itself** over `Q(i)` (or reproduce that reduction over this number field). No special pullback factorization remains to be checked.

---

## 7. Regression audit

### `det M=±1`

Then `k=1`; the map is a torus automorphism and CI is immediate. The proof includes this case.

### Noncyclic finite kernel

Not covered. If `d_1>1`, the Smith form has two nontrivial power coordinates and PK for one primitive character alone does not automatically rule out splitting after the first extension. CI deliberately claims only `d_1=1`.

### Primitive row vector versus primitive column vector

The corollary only needs that the integer entries of `M` have gcd one. A primitive vector in either row lattice or column lattice forces that gcd condition. Smith invariants are unchanged by transpose.

### Monomial factors

Laurent irreducibility ignores units `cX^aY^b`. After clearing negative exponents, such Laurent units become monomial factors; CI excludes every nonmonomial factorization, which is the notion used in lacunary factorization theorems.

### Could a target coordinate become constant on `C`?

No primitive character `X^rY^s` is constant: PK's divisor table has zero divisor only when `r=s=0`, not for a primitive pair.

### Capelli exceptional case

Inherited exactly from PK; no binomial exception is omitted.

---

## 8. What this changes

The conditional GC-F handoff said:

> prove a Gaussian coefficient-field extension of Filaseta, then use the already checked bivariate families.

CI replaces the algebraic half of that request by a direct theorem:

```math
\boxed{
\text{every rank-two primitive Schinzel pullback of the P2 curve is irreducible over }\mathbb Q(i).
}
```

So the shortest remaining external/theorem-level question is now only:

> Does the Schinzel large-gap finite-matrix reduction used in Theorem 74 apply over the number field `Q(i)` with the same rank-two conclusion?

If yes, CI plus GC-R would give eventual irreducibility of `F_n^+`, hence eventual irreducibility of `H_{2n}`, and P2A would exclude every sufficiently large even-`m` P2 survivor.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.**

CI is self-contained downstream of PK and standard Smith/Capelli facts. It intentionally does not promote the final large-gap coefficient-field scope until the literature statement is verified.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let f define the Gaussian P2 curve C over Q(i). PK proves every primitive character
X^rY^s on C is not a pth power for any prime p; hence T^k-X^rY^s is irreducible in
Q(i)(C)[T] for every k.

For any full-rank monomial matrix M with gcd(entries M)=1, Smith normal form gives
  U M V = diag(1,k).
Unimodular source/target monomial changes preserve Laurent irreducibility. The powered
target coordinate after the target change is a primitive character X^rY^s. Capelli
composition then gives irreducibility of the diagonal pullback g(S,T^k), hence of the
original monomial pullback phi_M^*f.

If the row lattice of M contains a primitive vector such as (1,N), gcd(entries M)=1.
Therefore every rank-two matrix allowed by the primitive Schinzel large-gap relation
has irreducible P2 pullback over Q(i).

Remaining bridge: verify/reproduce the finite-matrix large-gap reduction itself over
Q(i). The rank-two pullback algebra is now closed.
```
