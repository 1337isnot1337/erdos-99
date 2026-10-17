> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_p1_common_path_run_equation_2026-09-09.md) · source SHA-256 `1012e72535f11cfb0baf32cdd1ecdc244fe01c504991891433812c982553af26`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 13 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-8FA27B905DC4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — P1 common path: exact star-run equation and exclusion of 2/3-edge cores

**Date:** 2026-09-09  
**Repository branch:** `research/cyclic-run-word-audit-2026-09-09`  
**Run type:** exact run-composition reduction + finite subcase closure  
**Target:** primitive cyclic `d_H=1,s_Z=1`, P1  
**Depends on:** JP common-path theorem and SC sign/cycle interpretation on PR #118; SR star-run saturation on this branch; C18 diameter-star angle bound  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`, but P1 common paths with 2 or 3 diameter edges are excluded for all sufficiently large sources.

P1 has the exact rectangle with diameter diagonals `ac,bd`, unit sides `ab,cd`, and long sides `ad,bc` of length `sqrt(D^2-1)`. JP defines the common twin-cycle path

```math
J=P_H(x,y),
```

where `x` and `y` are the nonleaf endpoints of `ac` and `bd`. JP proves

```math
|x-y|\in\{1,\sqrt{D^2-1}\}
```

and `|E(J)|>=2`.

The recent SR correction says the full diameter tree need not be a path: star runs are allowed. The correct path variable is therefore the actual graph path `J`, with each interior turn carrying the full multiplicity of the corresponding diameter star.

### Theorem PRE — exact P1 path-run equation

Write

```math
J:v_0=x,v_1,\ldots,v_L=y,
\qquad L=|E(J)|\ge2.
```

For each interior vertex put

```math
\boxed{r_i:=\deg_H(v_i)-1\ge1\qquad(1\le i\le L-1).}
\tag{PRE.1}
```

Then, after orienting the projective diameter order consistently along either twin maximal completion:

1. the two `J`-edges incident to `v_i` are the two extreme edges of the contiguous H-star at `v_i`;
2. their projective direction gap is exactly
   ```math
   \boxed{r_i\delta,
   \qquad
   \delta=2\arcsin\frac1{2D};}
   \tag{PRE.2}
   
   ```
3. if
   ```math
   R_0=0,
   \qquad
   R_j=r_1+\cdots+r_j,
   
   ```
   then for some `theta`
   ```math
   \boxed{
   \frac{y-x}{D}
   =e^{i\theta}
   \sum_{j=0}^{L-1}(-1)^j e^{iR_j\delta};
   }
   \tag{PRE.3}
   
   ```
4. the parity and endpoint metric are linked exactly:
   ```math
   \boxed{
   L\text{ odd}\iff |x-y|=1,
   }
   \tag{PRE.4}
   
   ```
   ```math
   \boxed{
   L\text{ even}\iff |x-y|=\sqrt{D^2-1};
   }
   \tag{PRE.5}
   
   ```
5. therefore the sparse run polynomial
   ```math
   P_J(z)=\sum_{j=0}^{L-1}(-1)^j z^{R_j},
   \qquad z=e^{i\delta},
   
   ```
   satisfies
   ```math
   \boxed{|P_J(z)|=2\sin(\delta/2)}
   \quad(L\text{ odd}),
   \tag{PRE.6}
   
   ```
   and
   ```math
   \boxed{|P_J(z)|=\sqrt{1-4\sin^2(\delta/2)}}
   \quad(L\text{ even}).
   \tag{PRE.7}
   
   ```

Moreover the interior run exponent obeys

```math
\boxed{R_{L-1}\le q-4.}
\tag{PRE.8}
```

For sufficiently large `D`, neither `L=2` nor `L=3` is possible. Hence every surviving P1 common path has

```math
\boxed{|E(J)|\ge4.}
\tag{PRE.9}
```

This is the first P1 reduction that incorporates all pendant/star multiplicities explicitly and does not use the invalid Euler-trail shortcut.

---

## 1. `H` is `J` plus direct leaves

PR/JP prove that every full-H edge outside the common twin-cycle path `J` is a direct leaf edge. Therefore if `ell_i` denotes the number of leaf edges attached to `v_i`, then

```math
\deg_H(v_i)=
\begin{cases}
1+\ell_i,&i=0,L,\\
2+\ell_i,&1\le i\le L-1.
\end{cases}
\tag{1.1}
```

In particular

```math
r_i=1+\ell_i
\quad(1\le i\le L-1).
\tag{1.2}
```

The number of vertices outside `J` is `q-(L+1)`, so

```math
\sum_{i=0}^L\ell_i=q-L-1.
\tag{1.3}
```

The rectangle diagonals `ac,bd` each have one leaf endpoint and one nonleaf endpoint by JP. Since `x,y` are the nonleaf endpoints, each is incident to the corresponding diagonal leaf edge. Hence

```math
\ell_0\ge1,
\qquad
\ell_L\ge1.
\tag{1.4}
```

Using (1.2)-(1.4),

```math
R_{L-1}
=\sum_{i=1}^{L-1}(1+\ell_i)
=(L-1)+q-L-1-\ell_0-\ell_L
\le q-4.
```

This proves PRE.8.

---

## 2. The two path edges are the extremes of each interior star run

SR applies to P1 after breaking the projective diameter order at the unique doubled Minkowski edge. Thus all H-edges incident to any terminal occur in one contiguous projective run.

Fix an interior path vertex `v_i`. The two J-edges incident to `v_i` lie on the odd cycle of **both** twin maximal antipodal completions. Every other H-edge incident to `v_i` is a direct leaf edge in both completions.

SC's local support-event description identifies cycle states as the boundary states of a fixed-endpoint star run: through the interior of the run the same support endpoint is fixed, while the two transitions at the run boundaries change that fixed endpoint. Equivalently, the two cycle edges incident to a cycle vertex are the two extreme projective edges of its star, and the pendant edges lie between them.

Therefore the two J-edges at `v_i` are the extremes of a block containing

```math
\deg_H(v_i)
```

actual diameter states. Every internal projective gap in the block is the ordinary gap `delta`. The extreme-to-extreme separation is therefore

```math
(\deg_H(v_i)-1)\delta=r_i\delta,
```

proving PRE.2.

---

## 3. Projective directions along `J` are monotone

Compress each terminal star run in the projective support order to its two boundary cycle states. SC's sign-change/cycle construction then gives the odd cycle of either maximal completion in its cyclic projective order.

The common path `J` is a path segment of that odd cycle. Hence, after choosing one of the two cycle orientations, its edge directions are monotone in one lift of projective angle.

Let the `J` edge vectors along graph-path traversal be

```math
p_j:=v_j-v_{j-1},
\qquad |p_j|=D,
\qquad 1\le j\le L.
```

At `v_i`, the line directions of `p_i,p_{i+1}` differ by `r_i delta`. C18 puts all diameter partners at one vertex in an angular cone of width strictly below `pi/3+o(1)`; in particular `r_i delta<2pi/3` for all sufficiently large `D`.

The oriented traversal vectors cannot make the small angle `r_i delta`, because then

```math
|v_{i+1}-v_{i-1}|
=|p_i+p_{i+1}|
=2D\cos(r_i\delta/2)>D,
```

contradicting the source diameter.

Thus the traversal turn is the supplementary angle. With the monotone projective lift,

```math
\boxed{
p_{i+1}=-e^{ir_i\delta}p_i.}
\tag{3.1}
```

Iterating gives

```math
p_{j+1}=(-1)^j e^{iR_j\delta}p_1.
```

Write `p_1=D e^{itheta}` and sum over the path. This proves PRE.3.

---

## 4. Twin-cycle parity fixes the endpoint metric

There are four possibilities for which endpoint of each rectangle diagonal is the H-leaf.

If the leaf endpoints are `a,b`, then `x=c,y=d`, so `|x-y|=|cd|=1`. The `H+ad` odd cycle is

```math
ac\cup J\cup ad,
```

of length `L+2`, so `L` is odd. The `H+bc` cycle gives the same parity.

If the leaf endpoints are `c,d`, then `x=a,y=b`, again `|x-y|=1`, and the same `L+2` parity applies.

If the leaf endpoints are `a,d`, then `x=c,y=b`, so

```math
|x-y|=|bc|=\sqrt{D^2-1}.
```

Here `H+bc` has cycle `J+bc` of length `L+1`, while the other completion cycle has length `L+3`. Both are odd exactly when `L` is even.

The remaining leaf pattern `c,b` is symmetric and gives `|x-y|=|ad|=sqrt(D^2-1)` with `L` even.

This proves PRE.4-PRE.5.

Divide PRE.3 by `D` and use

```math
D^{-1}=2\sin(\delta/2)
```

to obtain PRE.6. For the long endpoint,

```math
\frac{\sqrt{D^2-1}}{D}
=\sqrt{1-D^{-2}}
=\sqrt{1-4\sin^2(\delta/2)},
```

which gives PRE.7.

---

## 5. Exclude `L=2`

If `L=2`, PRE.5 applies. There is one interior run parameter `r=r_1`, and PRE.3 reduces to two diameter vectors. Their endpoint span is

```math
|x-y|=2D\sin(r\delta/2).
```

PRE.5 requires

```math
2D\sin(r\delta/2)=\sqrt{D^2-1}.
```

Hence

```math
\boxed{
r\delta
=2\arcsin\left(\frac12\sqrt{1-D^{-2}}\right).
}
\tag{5.1}
```

As `D->infinity`, the right side tends to

```math
\frac\pi3.
```

But C18 gives the source-wide incident-diameter angle bound

```math
r\delta
\le
\frac{D(5\pi/6-\sqrt3)+4\pi/3+\pi/(2D)}{D+1},
```

whose limit is

```math
\theta_\infty=\frac{5\pi}{6}-\sqrt3
=0.885943\ldots
<\frac\pi3.
```

Therefore (5.1) contradicts C18 for all sufficiently large `D`. Thus

```math
\boxed{L\ne2.}
```

---

## 6. Exclude `L=3`

If `L=3`, PRE.4 applies and the normalized endpoint length is `1/D->0`.

Put

```math
a=r_1\delta,
\qquad
b=r_2\delta.
```

After rotation, PRE.3 gives

```math
\frac{x-y}{D}
=1-e^{ia}+e^{i(a+b)}
```

up to complex conjugation. Hence

```math
\left|1-e^{ia}+e^{i(a+b)}\right|
=\frac1D.
\tag{6.1}
```

Choose any fixed

```math
\theta_\infty<\theta_*<\frac\pi3.
```

By C18, for all sufficiently large `D`,

```math
0<a,b\le\theta_*.
\tag{6.2}
```

The continuous function

```math
f(a,b)=|1-e^{ia}+e^{i(a+b)}|
```

has no zero on the compact square `[0,theta_*]^2`. Indeed, if it vanished then

```math
e^{ia}=1+e^{i(a+b)}.
```

Taking moduli gives

```math
1=2\cos((a+b)/2),
```

because `0<=a+b<2pi/3`. Thus

```math
a+b=\frac{2\pi}{3},
```

contradicting `a+b<=2theta_*<2pi/3`.

Therefore

```math
\min_{[0,\theta_*]^2}f=:c_*>0.
```

But the right side of (6.1) tends to zero. For `D>1/c_*`, (6.1) is impossible.

Hence

```math
\boxed{L\ne3}
```

for all sufficiently large sources.

Together with JP's `L>=2`, this proves PRE.9.

---

## 7. Algebraic form

PRE.6-PRE.7 can be squared to eliminate the endpoint phase. Since `|z|=1`,

```math
P_J(z)P_J(z^{-1})
=
\begin{cases}
2-z-z^{-1},&L\text{ odd},\\
z+z^{-1}-1,&L\text{ even}.
\end{cases}
\tag{7.1}
```

The exponent bound `R_{L-1}<=q-4` makes this a lower-degree reciprocal algebraic relation at the same P1 angle `z=e^{idelta}` that satisfies SC's Chebyshev equation

```math
T_{q-2}(\cos\delta)+4\cos\delta-3=0.
\tag{7.2}
```

Thus any algebraic-degree proof for the physical P1 root can now use the mechanically relevant common path rather than the full shell Littlewood word. This is potentially stronger because the run relation has exponent span at most `q-4`.

---

## 8. Next target

There are two concrete continuations.

1. **Arithmetic:** prove that the physical root `z=e^{idelta}` of the P1 Chebyshev equation has algebraic degree larger than the reciprocal relation (7.1) permits. Experiments show the Chebyshev factor is irreducible except for the irrelevant `cos(delta)=1/2` factor when `6|(q-2)`, but a proof is still required.
2. **Geometric:** use C18 together with PRE.3 to exclude `L=4` or force a quantitative lower bound on `L`. The path-run variables satisfy the extra integer budget `R_{L-1}<=q-4`, so this is a finite constrained polygonal-sum problem rather than an arbitrary Littlewood sum.

No claim beyond `L>=4` is made here.

---

## Audit classification

| Claim | Status | Reason |
| --- | --- |
| every interior J turn is an integer star-run multiple of `delta` | proved | SR + SC cycle-edge extremality |
| exact path-run equation PRE.3 | proved | monotone projective cycle order + diameter bound |
| parity/endpoint metric PRE.4-PRE.5 | proved | four leaf-pattern enumeration |
| exponent budget `R<=q-4` | proved | all off-J edges are leaves + two mandatory diagonal leaves |
| `L=2` excluded | proved asymptotically | required 60-degree star angle vs C18 50.76-degree cap |
| `L=3` excluded | proved asymptotically | compact three-vector zero obstruction + C18 |
| all P1 excluded | open | `L>=4` remains |
