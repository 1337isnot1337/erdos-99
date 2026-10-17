> Generated reading edition · [exact source](../../../docs/reports/target_c_regular_odd_shell_stress_polygon_2026-09-09.md) · source SHA-256 `33d5c13049de6961a39710276418bf9974afd416b050f64241767bd354e3ef9e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 20 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-B40CECD68F90","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — regular odd shell: exact normalized KKT stress polygon and zero patterns

**Date:** 2026-09-09  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact Fourier classification / binding-regression analysis  
**Target:** cyclic `d_H=0,1,2` shell degeneration  
**Depends on:** elementary regular-polygon geometry; consistent with US/CY  
**Computation:** none in the proof

## LEVEL I STATUS

`STILL OPEN`

The exact `d_H=0` Reinhardt family contains the regular odd shell as its most symmetric regression. US gives one uniform interior KKT stress but does not classify the whole two-dimensional normalized stress polytope.

For a regular odd unit `q`-gon, that polytope is explicit.

### Theorem RSP — exact regular-shell stress polygon

Let

```math
q=2k+1\ge5,
\qquad
x=\frac\pi q,
\qquad
D=\frac1{2\sin(x/2)}.
```

Number the polygon vertices `j in Z/qZ`. Let

```math
C_j=\{j,j+1\}
```

be the unit shell contacts and

```math
H_j=\{j,j+k\}
```

be the `q` diameter edges.

For any real equilibrium stress write `alpha_j` on `C_j`, `beta_j` on `H_j`, and put

```math
a_j:=\alpha_j/D^2.
```

Then the complete real equilibrium-stress space has dimension three. Its diameter coordinates are exactly

```math
\boxed{
\beta_j=b_0+b_c\cos\frac{2\pi j}{q}+b_s\sin\frac{2\pi j}{q}.
}
\tag{RSP.1}
```

Conversely every sequence of the form RSP.1 has a unique matching contact-stress sequence `a_j`, and the contact sequence has the same Fourier support `0,plus/minus1`.

After normalized KKT scaling

```math
\sum_j\beta_j=1,
```

we have

```math
\boxed{b_0=1/q.}
\tag{RSP.2}
```

Moreover, for every nonnegative normalized diameter sequence `beta_j>=0`, the corresponding contact coefficients are automatically **strictly positive** for `q>=5`. Hence the normalized KKT stress polytope is exactly

```math
\boxed{
\mathcal S_q=
\left\{(b_c,b_s):
\frac1q+b_c\cos\frac{2\pi j}{q}+b_s\sin\frac{2\pi j}{q}\ge0
\quad\forall j
\right\}.
}
\tag{RSP.3}
```

This is a regular `q`-gon in the `(b_c,b_s)` plane.

Its boundary zero patterns are exact:

1. a relative-interior point has every `beta_j>0`;
2. a relative-interior point of a polytope edge has exactly one zero diameter coefficient;
3. a polytope vertex has exactly two zero diameter coefficients, and they are consecutive in the **vertex index**:
   
   ```math
   \boxed{\beta_j=\beta_{j+1}=0.}
   \tag{RSP.4}
   ```

4. no nonzero normalized nonnegative stress has three zero diameter coefficients.

In projective diameter-direction order, `H_j` and `H_{j+1}` are separated by exactly one diameter edge. Therefore deleting the two zero edges at a stress-polytope vertex splits the regular diameter cycle into

```math
\boxed{
K_2\ \sqcup\ P_{q-2},
}
\tag{RSP.5}
```

one single-edge tree and one long path.

Thus the regular-shell KKT degeneration predicts a unique topological `d_H=2` boundary model. It does **not** give an arbitrary pair of nontrivial diameter trees.

---

## 1. Regular-shell equilibrium equations

Put

```math
\zeta=e^{2ix}=e^{2\pi i/q}
```

and represent the polygon vertices by complex numbers

```math
p_j=R\zeta^j,
\qquad
R=\frac1{2\sin x}.
```

The longest chord of the odd regular polygon joins `j` to `j+k`, with

```math
k=\frac{q-1}{2}
```

and length

```math
D=\frac1{2\sin(x/2)}.
```

At vertex `j`, equilibrium is

```math
\alpha_{j-1}(p_j-p_{j-1})
+
\alpha_j(p_j-p_{j+1})
=
\beta_j(p_j-p_{j+k})
+
\beta_{j-k}(p_j-p_{j-k}).
\tag{1.1}
```

Divide by `R zeta^j` and use

```math
1-\zeta= -2i e^{ix}\sin x,
\qquad
1-\zeta^{-1}=2i e^{-ix}\sin x,
```

```math
\zeta^k=-e^{-ix},
\qquad
1-\zeta^k=2e^{-ix/2}\cos(x/2),
```

```math
1-\zeta^{-k}=2e^{ix/2}\cos(x/2).
```

Separating real and imaginary parts gives the equivalent scalar pair

```math
\boxed{
\beta_j+\beta_{j-k}=a_{j-1}+a_j,
}
\tag{1.2}
```

```math
\boxed{
\beta_{j-k}-\beta_j
=c_x(a_{j-1}-a_j),
\qquad
c_x:=\frac{\cos x}{1-\cos x}.
}
\tag{1.3}
```

The normalization by `D^2` in `a_j=alpha_j/D^2` uses

```math
D^{-2}=4\sin^2(x/2).
```

---

## 2. Fourier diagonalization leaves only modes `0,plus/minus1`

Take one Fourier mode

```math
a_j=A\lambda^j,
\qquad
\beta_j=B\lambda^j,
\qquad
\lambda=e^{2imx},
\qquad
m\in\mathbb Z/q\mathbb Z.
```

Equations (1.2)-(1.3) become

```math
B(1+\lambda^{-k})=A(1+\lambda^{-1}),
\tag{2.1}
```

```math
B(\lambda^{-k}-1)=c_xA(\lambda^{-1}-1).
\tag{2.2}
```

Because `q` is odd, none of the factors `1+lambda^{-k}` or `1+lambda^{-1}` vanishes. Eliminating `A/B` yields

```math
\boxed{
\tan(mkx)=c_x\tan(mx).
}
\tag{2.3}
```

We solve this exactly.

### Odd mode `m=2r+1`

Put

```math
y=mx/2.
```

Since

```math
mkx=m\frac{\pi-x}{2}
\equiv\frac\pi2-y\pmod\pi,
```

(2.3) is

```math
\cot y=c_x\tan(2y).
```

With `t=tan y`,

```math
\frac1t=c_x\frac{2t}{1-t^2},
```

so

```math
t^2=\frac1{1+2c_x}
=\tan^2(x/2).
```

For `1<=m<=q-2` odd, `0<y<pi/2`, hence `t>0` and therefore

```math
y=x/2.
```

Thus

```math
\boxed{m=1.}
```

### Even mode `m=2r`

For nonzero even `m`,

```math
mkx=r(\pi-x)
\equiv-rx\pmod\pi,
```

so (2.3) becomes

```math
-\tan(rx)=c_x\tan(2rx).
```

Writing `t=tan(rx)` and cancelling `t` gives

```math
t^2=1+2c_x
=\cot^2(x/2).
```

For `1<=r<=k`, the only solution is

```math
rx=\frac\pi2-\frac x2,
```

namely

```math
r=k,
\qquad
m=q-1.
```

Finally `m=0` plainly solves the equations. Therefore the only Fourier modes in the real stress space are

```math
\boxed{m=0,1,q-1.}
\tag{2.4}
```

This proves the three-dimensionality and RSP.1.

---

## 3. The matching contact harmonic is smaller

For `m=0`, equations (2.1)-(2.2) give simply

```math
A=B.
\tag{3.1}
```

For `m=1`, (2.1) gives

```math
\frac BA
=
\frac{1+e^{-2ix}}{1+e^{-2ikx}}
=
 i\,\frac{\cos x}{\sin(x/2)}e^{-3ix/2}.
\tag{3.2}
```

Hence

```math
\boxed{
\left|\frac AB\right|
=
\frac{\sin(x/2)}{\cos x}.
}
\tag{3.3}
```

The `m=q-1` relation is its complex conjugate.

Thus if the diameter harmonic has amplitude `rho`, the normalized contact harmonic in `a_j` has amplitude

```math
\rho\frac{\sin(x/2)}{\cos x}.
\tag{3.4}
```

---

## 4. Nonnegative beta automatically gives positive contact stress

Write the normalized diameter stress as

```math
\beta_j=\frac1q+\rho\cos(2jx-\phi).
\tag{4.1}
```

Among the `q` equally spaced sample angles `2jx`, some point lies within angular distance `x=pi/q` of the antipode of `phi`. Therefore

```math
\min_j\cos(2jx-\phi)\le-\cos x.
```

If every `beta_j>=0`, (4.1) gives

```math
\boxed{
\rho\le\frac1{q\cos x}.
}
\tag{4.2}
```

By (3.3), the contact sequence has mean `1/q` and harmonic amplitude at most

```math
\frac1q
\frac{\sin(x/2)}{\cos^2x}.
```

For `q>=5`, `0<x<=pi/5` and

```math
\sin(x/2)<\cos^2x.
```

Hence the contact harmonic amplitude is strictly less than its positive mean. Therefore

```math
\boxed{a_j>0\quad\forall j,}
```

and thus

```math
\boxed{\alpha_j>0\quad\forall j.}
\tag{4.3}
```

So no additional contact-sign inequality cuts down the beta-nonnegative polygon. This proves RSP.3.

---

## 5. Exact zero patterns of the regular stress polygon

The normalized feasible beta sequences are

```math
\beta_j=\frac1q+u\cos(2jx)+v\sin(2jx)\ge0.
```

Each inequality is one supporting half-plane in the `(u,v)` plane, with outward normal at angle `2jx`. These normals are the vertices of a regular `q`-gon, so their intersection is itself a regular `q`-gon up to scaling and rotation.

Equivalently, write

```math
\beta_j=\frac1q+\rho\cos(2jx-\phi).
```

A zero coefficient must occur at a sample point minimizing the cosine. On an odd equally spaced sample set, the closest sample(s) to the antipodal angle `phi+pi` are either

1. one unique sample; or
2. exactly two neighboring samples when the antipode lies at their midpoint.

There can be no third minimizer.

Therefore an edge-interior boundary stress has one zero, while a polytope vertex has exactly two neighboring zeros in `j`-order:

```math
\boxed{\beta_j=\beta_{j+1}=0.}
```

This proves RSP.4 and excludes three beta zeros.

---

## 6. Convert `j`-adjacency to diameter-cycle/projective order

The diameter edge is

```math
H_j=\{j,j+k\}.
```

Its projective direction is

```math
\arg(p_{j+k}-p_j)
\equiv\theta_0+2jx\pmod\pi.
```

One minimum projective step is `x`. Hence projectively consecutive diameter edges have index difference `d` satisfying

```math
2d\equiv1\pmod q.
```

Since `q=2k+1`,

```math
d=k+1\equiv-k\pmod q.
\tag{6.1}
```

This is also exactly diameter-cycle adjacency: `H_j` and `H_{j-k}` share the endpoint `j`.

Two projective steps change the index by

```math
2(k+1)=q+1\equiv1\pmod q.
\tag{6.2}
```

Therefore the two zero edges `H_j,H_{j+1}` at a stress-polytope vertex have exactly one diameter edge between them in projective/graph-cycle order.

Deleting two edges at cyclic positions separated by one surviving edge splits a `q`-cycle into

- that one surviving edge, a `K_2` tree on two vertices;
- the complementary path on `q-2` vertices.

Thus

```math
\boxed{H\setminus\{H_j,H_{j+1}\}=K_2\sqcup P_{q-2}.}
```

This proves RSP.5.

---

## 7. Interpretation for the cyclic tree phases

The regular exact Reinhardt shell therefore has a completely explicit degeneration hierarchy:

```text
interior of normalized stress polygon:
    d_H=0 full diameter q-cycle;

relative interior of one stress-polygon edge:
    one beta zero;
    diameter support is one spanning path (d_H=1 topology);

vertex of stress polygon:
    two beta zeros;
    zeros are two projective steps apart;
    diameter support is K2 disjoint union P_(q-2) (d_H=2 topology).
```

This is exactly compatible with CY's polytope dimensions `2,1,0` but is much more specific about the boundary support.

It also explains why an attempted claim that two beta zeros must be graph-adjacent would be false: the binding regular model has one surviving diameter edge between them.

---

## 8. Relation to D2S/D2R

D2S/D2R reduce an arbitrary cyclic `d_H=2` survivor to two exact `D,D,1` triangle-chain bodies and four shell transition defects. RSP identifies the symmetric limiting support pattern those bodies can approach:

```math
\boxed{
\text{one diameter component of size 2 and one component of size }q-2.
}
```

A theorem extending RSP's beta-coordinate description from the regular shell to the full exact Reinhardt sign-code family would therefore be decisive for the D2 topology. If the two-zero support remains `K_2 sqcup P_{q-2}`, then D2's arbitrary two-caterpillar endpoint collapses to one single-edge tree plus one long tree.

The next target is precisely that extension, not a generic stress-rank argument.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| equilibrium Fourier support is `0,plus/minus1` | proved | exact circulant equations and trigonometric mode solve |
| normalized beta formula RSP.1-RSP.2 | proved | Fourier classification + sum normalization |
| beta-nonnegative implies all contact alphas positive | proved for odd `q>=5` | exact harmonic-amplitude ratio |
| normalized KKT polytope is a regular q-gon | proved | q equally spaced beta half-planes |
| edge stress has one beta zero | proved | regular polygon facet |
| vertex stress has two neighboring beta zeros in j-order | proved | two adjacent active half-planes / cosine minima |
| no three beta zeros | proved | same |
| two-zero support is `K2 sqcup P_(q-2)` | proved | projective/graph-cycle reindexing |
| same zero pattern for every nonregular Reinhardt shell | open | sign-code dependence not yet classified |
| arbitrary cyclic d_H=2 excluded | open | D2R may approach nonregular Reinhardt limits |

---

## 10. Next target

Derive the normalized stress space for an arbitrary exact `d_H=0` Reinhardt shell directly from its regular difference body and sign word.

The hoped-for formula is a sign-code conjugate of RSP.1 in which the beta coordinates are evaluations of one affine/trigonometric function on the uniformly spaced diameter-direction states. The exact issue is whether a nonnegative normalized stress can vanish at two diameter states whose deletion leaves two macroscopic tree components.

If two-zero stresses always isolate one single diameter edge, the cyclic `d_H=2` phase is reduced to a one-small-tree degeneration; if the pattern is even more rigid, the phase may close outright.
