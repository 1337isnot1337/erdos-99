> Generated reading edition · [exact source](../../../../docs/targets/target-a/14-sharp-symmetric-five-block.md) · source SHA-256 `296af3860efef18e844eaada048e6709c29decedb7e070ced580b223d3e0ddd3`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target A — sharp symmetric five-block coefficient

This audited addendum follows Sections 160–161. Section 160 constructs a
reflection-symmetric toe-out translation of the fixed five Kuperberg blocks with
paper-normalized middle lift

```math
v_{\rm toe}(d)=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6).
```

Section 161 proves that arbitrary local rigid translations of those five blocks have
only quartic gain, but explicitly leaves the leading coefficient open. The theorem
below closes that coefficient question for the full reflection-symmetric translation
class: the Section 160 coefficient is sharp.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 162. Sharp leading coefficient for reflection-symmetric five-block translations

Work in the paper normalization of Sections 157, 160, and 161. Thus nearest-neighbor
center distance is two and the upper half triangular lattice has initial aligned gap
width `d>0`. Keep the exact same five rigid blocks and fix every exterior center.

Consider an arbitrary reflection-symmetric translation endpoint

```math
B_1=(-a,-b),\qquad
B_2=(-c,-e),\qquad
B_3=(0,v),\qquad
B_4=(c,-e),\qquad
B_5=(a,-b),
\tag{162.1}
```

with

```math
a,b,c,e,v\longrightarrow0
\qquad(d\downarrow0),
\qquad v\ge0,
\tag{162.2}
```

and suppose the final endpoint is feasible: every center distance is at least two.
No prescribed motion path or active-contact equality is assumed.

Section 160's complete nearest-neighbor enumeration implies in particular the
following necessary nonnegative margins:

```math
\begin{aligned}
M_1&=a^2-2a+b^2+2\sqrt3b,\\
M_2&=a^2-4a+b^2,\\
M_3&=a^2-2a+b^2-2bd-2\sqrt3b+d^2+2\sqrt3d,\\
M_5&=(a-c)^2+(b-e)^2+4(a-c),\\
M_7&=c^2+4c+(e+v)^2,\\
M_{10}&=c^2+2c+(e+v)^2-2\sqrt3(e+v),\\
M_{14}&=c^2-2c+e^2+2\sqrt3e.
\end{aligned}
\tag{162.3}
```

Only these seven inequalities are needed below.

## 162.1 First scaling: all variables are `O(d)`

> **Lemma 162.1.** Every feasible family satisfying (162.1)–(162.2) obeys
> ```math
> a,b,c,e,v=O(d).
> \tag{162.4}
> ```
> Moreover
> ```math
> \frac ad,\frac cd,\frac ed,\frac vd\longrightarrow0,
> \qquad
> 0\le\liminf\frac bd\le\limsup\frac bd\le1.
> \tag{162.5}
> ```

### Proof

Suppose first that (162.4) fails along a sequence `d_n->0`. Put

```math
r_n=\max\{|a|,|b|,|c|,|e|,v\}.
```

After passing to a subsequence we may assume `r_n/d_n->infinity` and

```math
(A,B,C,E,V)
=
\lim_{n\to\infty}
\frac{(a,b,c,e,v)}{r_n}
\tag{162.6}
```

exists, with at least one coordinate of absolute value one and `V>=0`. Because every
variable tends to zero, every quadratic term divided by `r_n` tends to zero; because
`d_n/r_n->0`, every explicit `d` term also vanishes.

Divide the inequalities in (162.3) by `r_n` and pass to the limit. From `M_2>=0`,
`M_7>=0`, and `M_5>=0` respectively,

```math
A\le0,\qquad C\ge0,\qquad A\ge C.
```

Hence `A=C=0`. Next `M_1>=0` and `M_3>=0` give `B>=0` and `B<=0`, so `B=0`.
Finally `M_{14}>=0` gives `E>=0`, while `M_{10}>=0` gives
`E+V<=0`. Since `V>=0`, this forces `E=V=0`, contradicting the normalization in
(162.6). Thus (162.4) holds.

Now divide by `d` along an arbitrary convergent subsequence. Quadratic terms divided by
`d` vanish. The same three inequalities `M_2,M_7,M_5` give

```math
A_1\le0,\qquad C_1\ge0,\qquad A_1\ge C_1,
```

so `A_1=C_1=0`. Then `M_1>=0` gives `B_1>=0`, while `M_3>=0`, now retaining its
linear `2\sqrt3d` term, gives `B_1<=1`. Finally `M_{14}` and `M_{10}` give
`E_1>=0` and `E_1+V_1<=0`, so `E_1=V_1=0`. Because every convergent subsequence has
these limits, (162.5) follows. $`\square`$

## 162.2 Second scaling: side translations are quadratic and the lift is quartic

Adding `M_{10}>=0` and `M_{14}>=0` cancels the linear `c` and `e` terms and gives the
exact inequality

```math
2\sqrt3\,v
\le
2c^2+2e^2+2ev+v^2.
\tag{162.7}
```

Since `e,v->0`, after shrinking `d` the terms `2ev+v^2` can be absorbed into the
left side. Hence

```math
\boxed{v=O(c^2+e^2).}
\tag{162.8}
```

> **Lemma 162.2.** One has
> ```math
> \boxed{a,c,e=O(d^2),\qquad v=O(d^4).}
> \tag{162.9}
> ```

### Proof

Suppose, along a sequence, that

```math
r_n=\max\{|a|,|c|,|e|\}
```

satisfies `r_n/d_n^2->infinity`. Lemma 162.1 gives `a,c,e=o(d)` and `b=O(d)`, while
(162.8) gives `v=O(r_n^2)`. Divide `M_2,M_5,M_7,M_{14},M_{10}` by `r_n`.
Because `r_n>>d_n^2`, the term `b^2/r_n` tends to zero; all other quadratic terms
divided by `r_n` also vanish, as does `v/r_n`. Passing to a normalized convergent
subsequence gives

```math
A\le0,\qquad A\ge C,\qquad C\ge0,\qquad E\ge0,\qquad E\le0.
```

Thus `A=C=E=0`, contradicting the definition of `r_n`. Hence `a,c,e=O(d^2)`.
Equation (162.8) then gives `v=O(d^4)`. $`\square`$

## 162.3 Exact leading optimization

Choose a sequence realizing

```math
V=\limsup_{d\downarrow0}\frac{v}{d^4}
```

and pass to a subsequence for which the bounded scaled variables converge:

```math
B=\lim\frac bd,\qquad
A=\lim\frac a{d^2},\qquad
C=\lim\frac c{d^2},\qquad
E=\lim\frac e{d^2},\qquad
V=\lim\frac v{d^4}.
\tag{162.10}
```

Lemma 162.1 gives `0<=B<=1`.

Divide `M_2>=0` by `d^2`. Since `a^2/d^2->0`,

```math
A\le\frac{B^2}{4}.
\tag{162.11}
```

Divide `M_5>=0` by `d^2`. The term `(a-c)^2/d^2` tends to zero and, because
`e/d->0`, `(b-e)^2/d^2->B^2`. Hence

```math
C\le A+\frac{B^2}{4}
\le\frac{B^2}{2}.
\tag{162.12}
```

Dividing `M_7>=0` by `d^2` gives `C>=0`. Dividing `M_{14}>=0` and
`M_{10}>=0` by `d^2` gives the opposite inequalities

```math
C\le\sqrt3E,
\qquad
C\ge\sqrt3E,
```

so

```math
E=\frac C{\sqrt3}.
\tag{162.13}
```

Finally divide (162.7) by `d^4`. Because `e=O(d^2)` and `v=O(d^4)`, the terms
`ev/d^4` and `v^2/d^4` vanish. Therefore

```math
\sqrt3V
\le C^2+E^2
=\frac43C^2.
\tag{162.14}
```

Using (162.12),

```math
V
\le\frac{4}{3\sqrt3}C^2
\le\frac{4}{3\sqrt3}\frac{B^4}{4}
=\frac{\sqrt3}{9}B^4
\le\frac{\sqrt3}{9}.
\tag{162.15}
```

This proves the sharp upper bound.

> **Theorem 162.3 (sharp symmetric five-block coefficient).** For every feasible
> reflection-symmetric local translation family (162.1)–(162.2),
> ```math
> \boxed{
> \limsup_{d\downarrow0}\frac{v(d)}{d^4}
> \le\frac{\sqrt3}{9}.
> }
> \tag{162.16}
> ```
> The analytic toe-out branch of Section 160 attains equality. Consequently its
> leading quartic coefficient is optimal over the entire reflection-symmetric
> rigid-translation class.

The equality case is also rigid at leading order. Equality in (162.15) forces equality
at every preceding bound, hence

```math
\boxed{
\frac bd\to1,
\qquad
\frac a{d^2}\to\frac14,
\qquad
\frac c{d^2}\to\frac12,
\qquad
\frac e{d^2}\to\frac{\sqrt3}{6},
\qquad
\frac v{d^4}\to\frac{\sqrt3}{9}.
}
\tag{162.17}
```

These are exactly the leading coefficients of Section 160's analytic solution.

## 162.4 Consequence for the proof search

Sections 160–162 now settle the natural local optimization hierarchy for the fixed
five rigid blocks:

1. Section 160 constructs an explicit quartic toe-out branch and gives the strongest
   current support constant;
2. Section 161 proves that arbitrary asymmetric/simultaneous local translations cannot
   improve the quartic exponent;
3. Section 162 proves that within the full reflection-symmetric translation class the
   Section 160 coefficient itself cannot be improved.

Thus coefficient tuning of the symmetric five-block model is exhausted. A better
support exponent requires a genuinely different block/contact architecture, rotations
or internal deformation, a nonlocal mechanism, or constructive use of the exterior
source/scaffold geometry. Alternatively, one must prove that the existing Section 160
quartic witness can be protected inside a globally derived monomer domain.

The exact Target A endpoint remains

```math
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}
}
```

or an explicit `N`-point unit-separated competitor of diameter strictly below `D(N)`.
Section 162 is an architecture-optimality theorem, not that final transport theorem.
