> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_kkt_exact_two_zero_extremes_2026-09-09.md) · source SHA-256 `ee46105e4b13b409f649552e444249bf1ab308df85db6fc85115a0afabd4e2dc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 5 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-2130377182C5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=0` KKT extremes delete exactly two cycle edges

**Date:** 2026-09-09  
**Run type:** exact KKT-polytope / convex-duality theorem  
**Target:** Target C C-II cyclic primitive endpoint, `d_H=0`  
**Depends on:** KL cycle localization; CE equal diameter-direction spacing; DC contiguous diameter stars; CY contact positivity; ES extreme-stress sparsification  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

KL proves that every proper face of the normalized KKT polytope is created only by vanishing diameter coefficients on the unique odd cycle of the full diameter graph. The remaining degeneracy question is exact:

> Can a nonzero stress have three cycle coefficients equal to zero?

The answer is no.

### Theorem EZ

For every nonzero signed equilibrium stress in the full three-dimensional unnormalized stress space,

```math
\boxed{
\text{at most two unique-cycle diameter coefficients vanish.}
}
\tag{EZ.1}
```

Hence every extreme normalized KKT stress has **exactly two** zero diameter coefficients, both on the unique odd diameter cycle:

```math
\boxed{
|\{h\in E(H):\beta_h=0\}|=2.
}
\tag{EZ.2}
```

All cycle contacts and all pendant diameter edges remain strictly positive.

Deleting two cycle edges from the connected unicyclic graph `H` leaves a forest on `q` vertices with `q-2` edges, hence exactly

```math
\boxed{2\text{ connected components}.}
\tag{EZ.3}
```

The selected mixed support has `2q-2` rows and one signed dependence, hence rigidity rank `2q-3`: every KKT extreme support is an actual-coordinate rigidity circuit.

---

## 1. Unique-cycle indexing and alternating signs

Index all `q` diameter edges by DC projective direction order

```math
h_0,\ldots,h_{q-1}.
```

KL gives that `H` is connected unicyclic. Let its unique odd cycle have length `r`, with direction-order positions

```math
0\le t_0<t_1<\cdots<t_{r-1}<q,
\qquad r\ge3\text{ odd}.
```

Extend

```math
t_{i+r}=t_i+q
```

and define positive gaps

```math
\ell_i=t_{i+1}-t_i,
\qquad
\sum_i\ell_i=q.
```

Put

```math
\theta=\frac\pi q,
\qquad
\nu_t=(\cos(\theta_0+t\theta),\sin(\theta_0+t\theta)).
```

Let `chi` be the signed cycle vector in the DC row orientation. The full planar diameter graph is a caterpillar with its unique cycle as spine; every edge off the cycle is pendant. DC says all diameter edges at one terminal form one contiguous projective-direction block. A pendant edge cannot be a block endpoint, because both neighboring direction-order edges must share its nonleaf endpoint. Therefore the two cycle edges at a cycle vertex are the two block endpoints.

Consecutive cycle edges in `(h_{t_i})` share one cycle vertex. Coherently orient the abstract cycle. In the DC traversal the shared endpoint has the same positive/negative endpoint role throughout its block, while the coherent cycle enters on one cycle edge and leaves on the other. Thus the two row-orientation conversion signs are opposite.

After one global sign choice,

```math
\boxed{
\chi_{t_i}=(-1)^i.
}
\tag{1.1}
```

Set

```math
r_t:=\chi_t\nu_t.
```

The cycle relation is

```math
\boxed{
\sum_{t=0}^{q-1}r_t=0.
}
\tag{1.2}
```

---

## 2. Three real coordinates for every signed stress

Use KL notation. Let `a_t` be the signed coefficient on the contact created by the transition `h_t -> h_{t+1}`, and let `b_t` be the signed coefficient on diameter edge `h_t`.

KL gives a vector parameter `c in R^2` such that

```math
\sin\theta\,(a_{t-1}-a_t)
=\frac1D c\cdot J r_t.
\tag{2.1}
```

CE gives

```math
D=\frac1{2\sin(\theta/2)},
\qquad
\lambda:=\frac1{D\sin\theta}=\sec\frac\theta2.
```

Define

```math
R_t=\sum_{s=0}^{t}r_s,
\qquad R_{-1}=0.
```

Integrating (2.1),

```math
\boxed{
a_t=A-\lambda c\cdot J R_t}
\tag{2.2}
```

for one scalar `A`.

The second KL equation is

```math
(1-\cos\theta)(a_{t-1}+a_t)-b_t
=\frac1D c\cdot r_t.
```

Since

```math
2(1-\cos\theta)=\frac1{D^2},
```

write

```math
M_t=\frac{R_{t-1}+R_t}{2}
```

and define

```math
\boxed{
K_t:=D r_t+\lambda J M_t.
}
\tag{2.3}
```

Then exactly

```math
\boxed{
D^2b_t=A-c\cdot K_t.
}
\tag{2.4}
```

Thus `(A,c_x,c_y)` are linear coordinates on the full signed equilibrium-stress space.

For cycle positions put

```math
K_i:=K_{t_i}.
```

If three cycle coefficients vanish, then

```math
A=c\cdot K_i=c\cdot K_j=c\cdot K_k.
```

A nonzero solution is therefore possible only if `K_i,K_j,K_k` are collinear. EZ reduces to proving that the `K_i` form a strictly convex polygon.

---

## 3. Exact step-two chord formula

Identify the plane with `C` and rotate globally so that

```math
\nu_t=e^{it\theta}.
```

Write

```math
\varepsilon_i=(-1)^i,
\qquad
r_{t_i}=\varepsilon_i e^{it_i\theta}.
```

Set

```math
a=\ell_i\theta,
\qquad b=\ell_{i+1}\theta,
```

```math
\delta=\frac{a+b}{2},
\qquad
\eta=\frac{a-b}{2},
\qquad
\mu=t_i\theta+\delta.
```

A direct substitution into (2.3) gives

```math
\boxed{
K_{i+2}-K_i
=
\frac{i\varepsilon_i e^{i\mu}}{\cos(\theta/2)}
\left(L_i-e^{i\eta}\right),
}
\tag{3.1}
```

where

```math
\boxed{
L_i=
\frac{\sin((\ell_i+\ell_{i+1}+1)\theta/2)}
{\sin(\theta/2)}.
}
\tag{3.2}
```

Because `ell_i,ell_{i+1}>=1` and at least one additional positive cycle gap remains,

```math
2\le\ell_i+\ell_{i+1}\le q-1.
```

Therefore the numerator angle in (3.2) lies in `[3theta/2,pi/2]`, so

```math
\boxed{L_i>1.}
\tag{3.3}
```

---

## 4. Strict convexity of the beta-functional polygon

Let

```math
\psi_i=\arg(L_i-e^{i\eta}).
```

Since `L_i>1`, the vector from `e^{i eta}` to the positive real point `L_i` has argument strictly between `0` and `-eta` when `eta!=0`, and equals zero when `eta=0`.

Hence

```math
\mu+\psi_i
```

lies strictly between

```math
\mu=t_i\theta+\frac{a+b}{2}
```

and

```math
\mu-\eta=t_i\theta+b.
```

Both lie strictly inside

```math
(t_i\theta,t_{i+2}\theta).
```

Consequently (3.1) gives a continuous argument lift satisfying

```math
\boxed{
\arg(K_{i+2}-K_i)
-\left(\frac\pi2+\arg\varepsilon_i\right)
\in(t_i\theta,t_{i+2}\theta).
}
\tag{4.1}
```

Because `r` is odd, step `i -> i+2` visits all indices modulo `r`. The parity of `i` is unchanged at each step, so the fixed term in (4.1) is unchanged between successive step-two chords. Their residual directions lie successively in disjoint intervals

```math
(t_i\theta,t_{i+2}\theta),
(t_{i+2}\theta,t_{i+4}\theta),\ldots
```

and therefore increase strictly. After `r` such steps, the lifted direction has increased by exactly `2pi` because

```math
t_{i+r}=t_i+q,
\qquad
\varepsilon_{i+r}=-\varepsilon_i.
```

The step-two chain closes. A closed chain whose edge directions increase strictly through one full turn cannot have a turn of `pi` or more; otherwise all edge vectors would lie in one closed half-plane and could not sum to zero.

Thus

```math
\boxed{
K_i,K_{i+2},K_{i+4},\ldots
}
```

is the boundary order of a strictly convex `r`-gon. In particular,

```math
\boxed{\text{no three }K_i\text{ are collinear}.}
\tag{4.2}
```

---

## 5. Exact two-zero theorem

Assume a signed equilibrium stress has three distinct zero unique-cycle coefficients:

```math
b_{t_i}=b_{t_j}=b_{t_k}=0.
```

By (2.4),

```math
A=c\cdot K_i=c\cdot K_j=c\cdot K_k.
```

Since the three points are noncollinear, `c` is orthogonal to two independent vectors and hence `c=0`. Then `A=0`, and (2.2), (2.4) give the zero stress.

Therefore every nonzero signed stress has at most two zero cycle coefficients. This proves EZ.1.

Now restrict to the normalized nonnegative KKT polytope. In this endpoint

```math
s_Z=2.
```

ES says every KKT extreme has at least two zero actual coordinates. CY/CG say contact coordinates never vanish, and KL says pendant diameter coordinates never vanish. Hence every extreme has at least two zero unique-cycle coordinates. EZ.1 gives at most two.

Therefore every extreme has exactly two, proving EZ.2.

---

## 6. Selected-support consequences

The full diameter graph is connected unicyclic on `q` vertices and `q` edges. Deleting exactly two cycle edges yields a forest with

```math
q\text{ vertices},
\qquad q-2\text{ edges}.
```

Hence its number of components is

```math
q-(q-2)=2.
```

Thus every KKT extreme selected diameter graph has exactly two tree components.

The selected mixed support contains

```math
q+(q-2)=2q-2
```

rows. An extreme normalized stress has no nonzero normalized tangent supported inside its support, so the signed dependence space on that support is one-dimensional. Therefore the selected rigidity-row rank is

```math
(2q-2)-1=2q-3.
```

Hence every extreme mixed support is an actual-coordinate planar rigidity circuit.

---

## 7. What remains

EZ completely removes stress-polytope degeneracy:

```text
full H:
    connected unicyclic;

KKT boundary:
    only unique-cycle beta coordinates can vanish;

KKT extreme:
    exactly two unique-cycle beta coordinates vanish;
    all contacts and all pendant diameter edges survive;
    selected H is a two-component forest with q-2 edges;
    selected mixed support is a rigidity circuit.
```

The remaining finite question is which two cycle edges vanish at each extreme.

The strict-convex `K` polygon strongly suggests a complete polar-duality description: the zero pair should be adjacent vertices of `conv{K_i}`. Since the convex order is the step-two order `i,i+2,i+4,...`, this predicts zero pairs separated by exactly one cycle edge in the ordinary unique-cycle order.

That stronger facet-attainability statement is the next target; it is not assumed here.

---

## 8. Regression audit

- The proof allows arbitrary positive gap composition `(ell_i)`; periodicity or regularity is not assumed.
- It proves noncollinearity in the entire signed stress space, not by numerical genericity.
- The unique cycle may have any odd length `r>=3` and may carry arbitrary pendant diameter leaves.
- The component count is two, not three: `q-(q-2)=2`.
- EZ does not yet prove that every unique-cycle beta inequality is attained by a KKT boundary stress.

---

## 9. Compact handoff

```text
In d_H=0, unique cycle positions t_i have alternating cycle signs. KL integrates the
signed stress space to (A,c in R^2):
    D^2 beta_{t_i}=A-c.K_i.
The exact step-two chord formula gives
    K_{i+2}-K_i
      =[i eps_i exp(i mu_i)/cos(theta/2)] [L_i-exp(i eta_i)],
with L_i>1 and residual chord direction strictly between t_i theta and t_{i+2} theta.
Since the cycle length is odd, step +2 visits every K_i and these directions turn
strictly through 2pi. Hence the K_i form a strictly convex polygon and no three are
collinear.

Therefore no nonzero signed stress can kill three cycle beta coordinates. ES gives
>=2 zeros at every normalized extreme, while CY and KL rule out contact and pendant
zeros. So every extreme kills exactly two unique-cycle edges. Its selected H has q-2
edges on q vertices and therefore exactly two components; the mixed selected support
has 2q-2 rows and rank 2q-3, hence is a rigidity circuit.
```
