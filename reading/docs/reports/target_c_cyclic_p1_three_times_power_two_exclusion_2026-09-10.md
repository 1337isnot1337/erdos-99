> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_p1_three_times_power_two_exclusion_2026-09-10.md) · source SHA-256 `932407eb9d7a8d8939782bfcf06c9ed8832269210d9dd7828fb30bfdf804478b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-5D56035B9B92","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic P1: exclude `q-2 = 3*2^k`

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-p1-arithmetic-2026-09-10`  
**Run type:** exact 2-adic cluster / mod-2 reciprocal-factor argument  
**Target:** cyclic primitive `d_H=1`, P1 endpoint  
**Depends on:** P2 arithmetic reduction on this branch; PR #118 signed-closure theorem SC.1  
**Computation:** not used in the proof

## LEVEL I STATUS

`STILL OPEN`

P2 excludes the infinite P1 family `m=q-2=2^k`. The same arithmetic framework can be pushed through the first nontrivial odd part.

### Theorem P3

Let

```math
m:=q-2=3r,
\qquad
r=2^k,
\qquad
k\ge1.
```

Then the cyclic P1 endpoint is impossible.

Equivalently,

```math
\boxed{q-2=3\cdot2^k\quad\Longrightarrow\quad\text{no P1 survivor}.}
```

The proof does **not** require irreducibility of the Chebyshev trace polynomial. Indeed `G_m` has the elementary factor `T-1` throughout this family. Instead, two 2-adic Newton polygons separate the remaining cofactor into a large `T=1` cluster and a smaller `T=0` cluster. The P1 Littlewood reduction modulo two cannot accommodate the reciprocal lift of the smaller cluster.

---

## 1. Recall the P1 trace-degree upper bound

Use P2 notation:

```math
z=e^{i\delta},
\qquad
Y=z+z^{-1}=2\cos\delta,
```

and

```math
G_m(T):=C_m(T)+4T-6,
```

where

```math
C_n(2\cos\theta)=2\cos(n\theta).
```

The P1 angle equation gives

```math
G_m(Y)=0.
\tag{P3.1}
```

The P1 signed closure gives a Littlewood polynomial

```math
P(Z)=\sum_{j=0}^{m-1}\varepsilon_j Z^j,
\qquad \varepsilon_j\in\{\pm1\},
\qquad P(z)=0.
\tag{P3.2}
```

Exactly as in P2,

```math
[\mathbb Q(z):\mathbb Q(Y)]=2,
```

so if `h(T)` is the irreducible minimal polynomial of `Y` and `d=deg h`, then

```math
\boxed{d\le\frac{m-1}{2}.}
\tag{P3.3}
```

Also, because every coefficient of `P` is odd,

```math
\boxed{
P(Z)\equiv S_m(Z):=1+Z+\cdots+Z^{m-1}\pmod2.
}
\tag{P3.4}
```

---

## 2. Remove the unavoidable trace factor `T-1`

Let

```math
m=3r,
\qquad r=2^k.
```

For `k>=1`, `r` is congruent to `2` or `4` modulo `6`, so

```math
C_r(1)=2\cos(r\pi/3)=-1.
```

Using the composition identity

```math
C_{3r}(T)=C_3(C_r(T))=C_r(T)^3-3C_r(T),
```

we get

```math
G_m(1)=(-1)^3-3(-1)+4-6=0.
```

Thus

```math
\boxed{G_m(T)=(T-1)H_m(T)}
\tag{P3.5}
```

for a monic integer polynomial `H_m` of degree `m-1`.

The geometric P1 root satisfies `Y=2 cos delta ->2` in the large regime and in particular `Y!=1`. Hence its minimal polynomial `h` divides `H_m`, not the removed factor `T-1`.

---

## 3. The large 2-adic cluster at `T=1`

Put

```math
X=T-1,
\qquad
A(X):=C_r(1+X)+1.
```

Then `A(0)=0`. Since `r=2^k`, the doubling identity

```math
C_{2n}=C_n^2-2
```

shows modulo two that

```math
A(X)\equiv X^r\pmod2.
\tag{P3.6}
```

Write

```math
A=XB,
```

so

```math
B(X)\equiv X^{r-1}\pmod2.
\tag{P3.7}
```

Now set `U=C_r(1+X)=-1+A`. A direct expansion gives

```math
\begin{aligned}
G_{3r}(1+X)
&=U^3-3U+4(1+X)-6\\
&=A^3-3A^2+4X.
\end{aligned}
```

Since `G_{3r}(1+X)=X H_m(1+X)`, divide by `X`:

```math
\boxed{
H_m(1+X)=4+X B(X)^2(A(X)-3).
}
\tag{P3.8}
```

From P3.7,

```math
B(X)^2\equiv X^{2r-2}\pmod4.
```

Therefore every coefficient of degrees

```math
1,\ldots,2r-2
```

in `H_m(1+X)` is divisible by `4`, while the coefficient of

```math
X^{2r-1}
```

is odd because the constant term of `A-3` is `-3`.

The constant term of P3.8 is exactly `4`, and the polynomial is monic of degree `3r-1`. Hence its lower 2-adic Newton polygon begins with the single segment

```math
\boxed{(0,2)\longrightarrow(2r-1,0),}
\tag{P3.9}
```

followed by a horizontal segment to degree `3r-1`.

Because `2r-1` is odd, the first slope is

```math
-\frac2{2r-1}
```

in lowest terms. Therefore every `Q_2`-irreducible factor carrying a root with

```math
v_2(Y-1)>0
```

has degree divisible by `2r-1`, and in particular at least `2r-1`.

But

```math
2r-1>\frac{3r-1}{2}=\frac{m-1}{2}
\qquad(r\ge2).
```

By P3.3 the minimal polynomial `h` of the geometric P1 root is too small to contain such a local factor. Consequently **every** `Q_2` factor of `h` lies on the horizontal Newton segment.

Modulo two, P3.8 gives more precisely

```math
H_m(1+X)
\equiv X^{2r-1}(1+X^r)
=X^{2r-1}(X+1)^r
\pmod2,
\tag{P3.10}
```

where the last equality uses `r=2^k`.

The horizontal roots therefore reduce to `X=1`, i.e. to `T=0`. Since `h` is monic and all its 2-adic factors belong to this cluster,

```math
\boxed{h(T)\equiv T^d\pmod2.}
\tag{P3.11}
```

---

## 4. The `T=0` cluster gives a lower bound on `d`

For `k>=2`, put

```math
B_0(T):=C_r(T)-2.
```

Since `r=2^k>=4`, repeated use of `C_{2n}=C_n^2-2`, starting from

```math
C_4(T)-2=T^4-4T^2,
```

gives

```math
\boxed{B_0(T)\equiv T^r\pmod4.}
\tag{P3.12}
```

Write `C_r=2+B_0`. Then

```math
G_{3r}
=(2+B_0)^3-3(2+B_0)+4T-6
=B_0^3+6B_0^2+9B_0+4T-4.
\tag{P3.13}
```

Using P3.12, every coefficient of `G_{3r}` below degree `r` is divisible by `4`; since

```math
G_{3r}=(T-1)H_m,
```

the coefficient recursion from multiplication by `T-1` shows that every coefficient of `H_m` below degree `r` is divisible by `4`. Moreover P3.10 at `X=T-1`, or directly the mod-two trace identity, gives

```math
H_m(T)\equiv T^r(T+1)^{2r-1}\pmod2,
\tag{P3.14}
```

so the coefficient of `T^r` is odd.

Finally, because `m=3r` is divisible by four when `k>=2`,

```math
C_m(0)=2,
```

and therefore

```math
H_m(0)=-G_m(0)=4.
```

Hence the lower Newton polygon of `H_m(T)` begins with

```math
\boxed{(0,2)\longrightarrow(r,0).}
\tag{P3.15}
```

Its slope is

```math
-\frac2r=-\frac1{r/2}.
```

Every `Q_2`-irreducible factor whose roots reduce to `T=0` therefore has degree divisible by `r/2`. Since P3.11 puts all roots of `h` in this cluster,

```math
\boxed{d\ge r/2.}
\tag{P3.16}
```

For the remaining case `k=1`, so `r=2,m=6`, P3.11 alone is already enough below; no lower bound stronger than `d>=1` is needed.

---

## 5. Reciprocal lift conflicts with the Littlewood reduction

Because `h` is the minimal polynomial of

```math
Y=z+z^{-1}
```

and `[Q(z):Q(Y)]=2`, the minimal polynomial of `z` is exactly the reciprocal lift

```math
\boxed{
M(Z):=Z^d h(Z+Z^{-1}),
}
\tag{P3.17}
```

which is monic of degree `2d`.

Equation P3.11 gives modulo two

```math
M(Z)
\equiv
Z^d(Z+Z^{-1})^d
=(Z^2+1)^d
=(Z+1)^{2d}.
\tag{P3.18}
```

Since `M` is the minimal polynomial of the P1 Littlewood root `z`, it divides `P` in `Z[Z]`. Thus P3.4 implies

```math
(Z+1)^{2d}\mid S_m(Z)
\qquad\text{in }\mathbb F_2[Z].
\tag{P3.19}
```

But `m=3r`, `r=2^k`, so in characteristic two

```math
\begin{aligned}
S_m(Z)
&=\frac{Z^{3r}-1}{Z-1}\\
&=(Z-1)^{r-1}(Z^2+Z+1)^r.
\end{aligned}
\tag{P3.20}
```

Therefore the multiplicity of `Z+1=Z-1` in `S_m` is exactly

```math
r-1.
```

Equation P3.19 forces

```math
\boxed{2d\le r-1.}
\tag{P3.21}
```

For `k>=2`, P3.16 gives `2d>=r`, contradicting P3.21.

For `k=1`, P3.21 says `2d<=1`, impossible for every nonconstant minimal polynomial.

Thus no P1 source exists for any

```math
m=3\cdot2^k,\qquad k\ge1.
```

This proves Theorem P3. `square`

---

## 6. What the proof reveals

The useful point is not merely another congruence class. The argument gives a reusable template for arbitrary odd part `u` in

```math
m=2^k u.
```

The P1 Littlewood reduction remembers the exact multiplicities of the odd-order residue roots in

```math
S_m(Z)\pmod2,
```

while the trace polynomial `G_m` has 2-adic root clusters indexed by the corresponding trace residues. A low-degree rational trace factor must choose some of those clusters; its reciprocal lift consumes twice their trace degree in the Littlewood reduction.

For `u=3`, the two clusters are rigid enough to make the multiplicity budget impossible.

The next target is to formulate this cluster/multiplicity argument for general odd `u`. One does not need global irreducibility of `G_m`: it is enough to prove that every admissible union of 2-adic trace clusters either already has trace degree `>(m-1)/2` or consumes more multiplicity in `S_m mod 2` than is available.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `T-1` divides `G_(3*2^k)` | proved | trace composition at `T=1` |
| first Newton segment at `T=1` has length `2r-1` | proved | exact formula P3.8 + mod-4 square |
| low-degree P1 factor cannot use `T=1` cluster | proved | segment denominator/degree exceeds P1 trace upper bound |
| remaining factor reduces to `T^d` | proved | horizontal residual `(X+1)^r` |
| `T=0` cluster gives `d>=r/2` for `k>=2` | proved | second mod-4 Newton segment |
| reciprocal lift reduces to `(Z+1)^(2d)` | proved | trace-to-reciprocal transform |
| Littlewood reduction supplies only multiplicity `r-1` | proved | exact factorization of `S_(3r)` over `F_2` |
| P1 for `m=3*2^k` | excluded | incompatible inequalities `2d>=r` and `2d<=r-1` |
| arbitrary odd part | open | next cluster classification |
| Level I | still open | other P1/S1/D2/global branches remain |
