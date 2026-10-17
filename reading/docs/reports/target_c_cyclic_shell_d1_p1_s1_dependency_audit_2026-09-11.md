> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_shell_d1_p1_s1_dependency_audit_2026-09-11.md) · source SHA-256 `ca2289ce7e0699b63b2ec821b8a0c5ddb56b4711178453af6a3da9ca93a08157`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 12 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-471FEEE8C6FA","canonical":true,"claim_ids":["C-P1-PRX","C-S1-Q13","C-S1-RSQ"],"claim_statuses":{"C-P1-PRX":"canonical","C-S1-Q13":"regression","C-S1-RSQ":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Erdős Problem #99 — independent audit of the primitive cyclic-shell `d_H=1` P1/S1 chain

**Date:** 2026-09-11  
**Target:** Target C, exact primitive endpoint `m=0`, `d_H+s_Z=2`, `C=C_q`, then the `d_H=1,s_Z=1` subcase  
**Audited families:** PN/ME/CY, AD/D1/AC/SC, P1 RL/O3/FRM/PRX, S1 RSQ, and the `q=13` S1 KKT/PSD regression  
**Disposition:** complete P1 exclusion is valid in its stated primitive-shell scope; the S1 reciprocal-square reduction is valid but does not close S1; the `q=13` S1 shell is a genuine numerical regression and not a global-minimizer theorem  

## LEVEL I STATUS

`STILL OPEN`.

The main purpose of this audit is scope discipline. Historical reports often call this the “cyclic `d_H=1`” branch. It is **not** the general Woodall `d_H=1` forest topology. It is the much narrower primitive all-loaded unit-shell normal form obtained when

```math
m+d_H+s_Z=2.
```

Within that exact normal form, the P1 arithmetic closure is valid and complete. S1 remains open.

---

## 1. Primitive endpoint provenance

PN rewrites the post-ZF exact ledgers using

- `m`: number of nonunit force-hull sides;
- `k=d_H+s_Z`;
- `c_I,s_C,c_B`: interior-component, pinned-stress, and extra loaded-chord currencies.

It proves exactly

```math
 c_I+s_C+c_B=m+k-2.
\tag{1.1}
```

Thus `m+k>=2`. At equality all three currencies vanish, so the positive contact core is a connected subgraph of the loaded hull cycle containing exactly `q-m` hull edges. Connectivity leaves only

```math
(m,k)=(0,2)
\quad\text{or}\quad
(m,k)=(1,1).
```

ME excludes the one-gap path `(m,k)=(1,1)` by a direct KKT tangent-force argument: a loaded vertex incident to a unit hull-side contact cannot have that side as its only positive contact. Hence the exact primitive equality reduces to

```math
\boxed{m=0,\qquad d_H+s_Z=2,\qquad C=C_q.}
\tag{1.2}
```

This reduction is finite and exact.

CY then shows that every normalized selected KKT stress keeps all cycle contacts positive. The normalized KKT polytope has dimension `s_Z=2-d_H`, so the primitive shell has the three bookkeeping cases

```math
(d_H,s_Z)=(0,2),(1,1),(2,0).
```

The present audit concerns only

```math
\boxed{d_H=1,\qquad s_Z=1.}
\tag{1.3}
```

By the current Woodall theorem, the full diameter graph in this case is a connected caterpillar tree. The older shell reports do not contradict that topology.

---

## 2. Difference-body one-defect split

Let `F` be the strictly convex equilateral force hull and `K=F-F` its difference body. In the primitive `d_H=1` shell, the exact difference-body counting argument is valid.

If `r_parallel` is the number of antipodal pairs of parallel primal hull sides, Minkowski edge merging gives exactly

```math
|V(K)|=2q-2r_{parallel}.
```

Every actual diameter vector is a circular vertex of `K` at radius `D`, and every circular vertex of `K` is a vertex difference of length `D`, hence an actual diameter vector. Since the full diameter graph has `h=q-d_H=q-1` edges, there are exactly `2h` circular vertices. Therefore the number of off-circle antipodal vertex pairs is

```math
a_{short}=d_H-r_{parallel}.
```

For `d_H=1` there are exactly two possibilities:

- **P1:** `r_parallel=1`, `a_short=0`;
- **S1:** `r_parallel=0`, `a_short=1`.

No third one-defect difference-body geometry is omitted.

D1's angle formulas follow directly from the cyclic half-boundary of `K`. In P1 there is one antipodal pair of length-two difference-body edges; in S1 there is one antipodal short vertex pair.

---

## 3. Endpoint-switch / signed closure audit

AC's local endpoint-switch argument is valid. In S1, if the two diameter chords adjacent to the unique short difference-body state changed the same support endpoint, the middle shell vertex would have to be non-diametral. But any diameter chord from that vertex is disjoint from both adjacent diameter chords and, by the convex diameter-thrackle property, would have to cross both. The two required partner arcs are disjoint, so this is impossible.

Thus the two defect-adjacent primal signs are opposite. In P1 the same cancellation is also visible directly from the length-two Minkowski merged edge: the corresponding parallel primal unit sides are oppositely directed and cancel in primal closure.

For P1, after removing this cancelling pair and putting

```math
m=q-2,\qquad z=e^{i\delta},
```

the remaining shell closure gives a genuine length-`m` Littlewood annihilator

```math
P(Z)=\sum_{j=0}^{m-1}\varepsilon_jZ^j,
\qquad \varepsilon_j\in\{\pm1\},
\qquad P(z)=0.
\tag{3.1}
```

The P1 metric equation is

```math
\cos(m\delta/2)=2\sin(\delta/2).
```

Squaring and eliminating the half-angle gives the exact reciprocal geometric equation

```math
\boxed{
F_m(z)=0,
\qquad
F_m(Z)=(Z^m+1)^2+4Z^{m-1}(Z-1)^2.
}
\tag{3.2}
```

Equivalently, for `T=z+z^{-1}` and trace Chebyshev `C_m`,

```math
G_m(T)=C_m(T)+4T-6=0.
```

No irreducibility assertion about `F_m` or `G_m` is needed.

---

## 4. P1 odd-`m` ramification exclusion

Let `M(Z)` be the monic minimal polynomial of the physical P1 root `z`. Since `M|P` over `Q[Z]` and both are primitive, Gauss's lemma gives `M|P` over `Z[Z]`. Modulo two,

```math
\bar M\mid S_m(Z):=1+Z+\cdots+Z^{m-1}.
\tag{4.1}
```

If `m` is odd, `S_m` is squarefree over `F_2`; hence `\bar M` is squarefree and the polynomial discriminant of `M` is odd. Therefore the number field `K=Q(z)` is unramified above two.

But (3.2) gives

```math
\iota=
\frac{z^m+1}{2z^{(m-1)/2}(z-1)}\in K,
\qquad
\iota^2=-1.
```

Thus `Q(i) subset K`. Since two is ramified in `Q(i)/Q`, ramification-index multiplicativity forces every prime of `K` above the Gaussian prime over two to have even ramification index, contradicting the odd discriminant.

Therefore every odd `m` P1 state is impossible.

---

## 5. RL zero-residue and O3 order-three audits

Write

```math
m=ru,
\qquad r=2^k,
\qquad u\text{ odd}.
```

RL studies the physical irreducible trace factor `h(T)` of `G_m`.

At trace residue zero, the local Newton polygon has a factor-degree lower bound incompatible with the Littlewood residue multiplicity at `Z=1`:

- for `r>=4`, the relevant segment has slope `-2/r`, forcing local degree divisible by `r/2`, while the reciprocal Littlewood cap gives trace multiplicity at most `(r-1)/2`;
- for `r=2`, the segment `(0,3)->(2,0)` forces even local degree while the cap is below one;
- for `r=1`, the cap is zero.

Thus the physical trace factor has no residue `T=0`, equivalently no reciprocal residue root `z=1`.

O3 handles trace residue one, equivalently primitive third reciprocal roots. When `3|u`, the lifted trace `t_0=-1` is a double root of `C_u(T)-2`. The local Newton polygon has one exact rational root `T=1` plus a remaining segment of slope `-2/(2r-1)`. The physical factor cannot contain the rational factor `T-1`, so any physical order-three trace factor requires multiplicity exceeding the Littlewood cap `r`. For `r=1`, the analogous segment forces degree two against cap one.

Thus primitive-third reciprocal residues are also absent.

---

## 6. FRM nonexceptional Newton segment

The strongest arithmetic subtlety is FRM's local slope. It is correct.

Let `\bar t=\bar\omega+\bar\omega^{-1}` be a nonzero, non-order-three trace residue with `\bar\omega^u=1`. Let `\omega` be its odd-order Teichmuller lift and

```math
t_0=\omega+\omega^{-1}.
```

Then exactly

```math
C_u(t_0)=2.
```

Moreover `t_0` is an exact double root of `C_u(T)-2`, because

```math
C_u(z+z^{-1})-2={ (z^u-1)^2\over z^u}
```

and the trace map is unramified at `\omega\ne\omega^{-1}`. Hence

```math
\boxed{C_u(t_0+X)-2=X^2V(X),\qquad V(0)\in\mathcal O^\times.}
\tag{6.1}
```

This resolves the apparent degree issue in the power-of-two composition. For `r=2^k`, put

```math
H_r(Y)=C_r(2+Y)-2.
```

The doubling identity gives

```math
H_r(Y)\equiv Y^r\pmod4.
```

Substituting (6.1) into `C_m=C_r\circ C_u` yields

```math
G_m(t_0+X)
=H_r(X^2V(X))+4(t_0-1)+4X.
```

Because `t_0-1` is a unit outside the order-three residue, the lower Newton polygon begins with the single segment

```math
\boxed{(0,2)\to(2r,0)}
```

of slope `-1/r`. Thus every physical local trace root above `\bar t` satisfies

```math
v_2(t-t_0)=1/r.
\tag{6.2}
```

The Littlewood reduction gives the opposite multiplicity cap. FRM's conclusion that every present nonexceptional trace factor occurs with full exponent exactly `r` is valid.

---

## 7. P1 even-`m` ramification doubling

For even `m`, (3.2) gives the element

```math
s={z^m+1\over2z^{(m-2)/2}(z-1)}\in Q(z),
\qquad
s^2=-z.
\tag{7.1}
```

Choose a local factor of the minimal polynomial over `Q_2`, with residue `\omega`. RL and O3 ensure

```math
\omega\ne1,
\qquad
\omega\text{ is not of order }3.
```

FRM gives the trace depth `1/r`. Writing

```math
z=\widehat\omega(1+x)
```

and using `\omega+\omega^{-1}\ne0`, the trace map is locally unramified, so

```math
v_2(x)=1/r.
\tag{7.2}
```

Let `\eta` be the Teichmuller lift of the unique residue square root of `\omega`. Then `\eta^2=\widehat\omega`. Put `s/\eta=1+y`. Equation (7.1) becomes

```math
y^2+2y+2+x=0.
```

Since `1/r<1`, nonarchimedean valuation comparison forces

```math
\boxed{v_2(y)=1/(2r).}
\tag{7.3}
```

Therefore the local ramification index `e` is divisible by `2r`.

If `\mu` is the irreducible local factor with reduction `\bar\mu=g^a`, and `f_0=deg g`, then for the local field `L=Q_2(z)`

```math
\deg\mu=e f_L=a f_0,
\qquad
f_0\mid f_L.
```

Hence

```math
a=e{f_L\over f_0}\ge e\ge2r.
```

But `\bar M|S_m`, and every nontrivial `u`-th residue root occurs in `S_m` with multiplicity exactly `r`. Thus `a<=r`, contradiction.

This closes every even `m` P1 state. Combined with Section 4:

### Theorem P1-AUDIT

Within the exact primitive shell normal form (1.2)-(1.3), the P1 parallel-side endpoint is impossible for all relevant `m=q-2`. The complete PRX ramification proof is valid.

---

## 8. S1 reciprocal-square reduction

S1 has no parallel primal-side pair and one short antipodal difference-body vertex pair. Normalize the two defect-adjacent signs to `+,-`, and put

```math
Q(Z)=\sum_{k=0}^{m-1}a_kZ^k,
\qquad a_k\in\{\pm1\}.
```

The signed shell directions give exact centered closure

```math
\boxed{
e^{-i(m-1)\delta/2}Q(z)=2\sin(\tau/2)>0.}
\tag{8.1}
```

Therefore the centered value is real and

```math
\boxed{Q(z)=Q^*(z),\qquad Q^*(Z)=Z^{m-1}Q(Z^{-1}).}
\tag{8.2}
```

The S1 metric geometry gives

```math
4\sin^2(\tau/2)=-{G_m(t)\over2-t},
\qquad t=z+z^{-1}.
```

Using

```math
2-t=-{(z-1)^2\over z}
```

and (8.1)-(8.2) yields exactly

```math
\boxed{F_m(z)=(z-1)^2Q(z)^2.}
\tag{8.3}
```

Thus every primitive S1 state solves the exact pair

```math
\boxed{
Q(z)=Q^*(z),
\qquad
F_m(z)=(z-1)^2Q(z)^2.
}
\tag{8.4}
```

The reduction is valid. It does not exclude S1.

If `Q` is nonpalindromic, the physical root also annihilates

```math
B_Q={Q-Q^*\over2(Z-1)},
\qquad \deg B_Q\le m-2.
```

If `Q` is palindromic, the phase condition is automatic and S1 becomes a signed one-variable cosine equation. These are genuine reductions, not closures.

---

## 9. Independent `q=13` S1 regression reproduction

The stored `q=13` regression was independently reconstructed from the displayed trace polynomial and sign word.

The physical trace root reproduces

```math
\delta\approx0.24143000751205,
\qquad
D\approx4.15206390869924,
```

strictly inside the S1 interval. The reconstructed equilateral polygon has closure residual about `3.2e-11` at ordinary double precision.

Direct distance classification reproduces exactly 13 cycle unit contacts and the 12 diameter pairs listed in the report. The smallest inactive contact slack is about `0.7713`; the smallest inactive diameter slack is about `0.07242`, so the active-set classification is not tolerance-sensitive.

The mixed rigidity matrix has rank `23=2q-3`, leaving a two-dimensional self-stress space. Linear programming with `sum beta=1` reproduces a full positive KKT stress with minimum coefficient

```math
0.0528311855\ldots
```

and equilibrium residual about `1.4e-15`.

The associated stress matrix has three numerical affine zero modes and first positive eigenvalue

```math
1.1039011469\ldots .
```

The report additionally claims both endpoints of the normalized one-dimensional stress segment remain PSD. The original reproduction script did not check this. The independent endpoint calculation does:

- negative endpoint `t≈-0.469050100806` kills exactly diameter `(1,7)`;
- positive endpoint `t≈+0.469050100792` kills exactly diameter `(4,11)`;
- both endpoint stress matrices have first positive eigenvalue `≈1.050855613` and only the three affine numerical zero modes.

The companion script `research/verify_s1_q13_kkt_endpoints.py` records this endpoint reproduction.

This remains a **numerical regression**, not an interval-certified algebraic theorem and not a global minimizer. Its margins are large enough to make the intended lesson reliable: shell closure + full-support KKT + maximal-rank PSD + endpoint PSD is not by itself an S1 contradiction.

---

## 10. Correct theorem-state disposition

| Object | Independent disposition |
| --- | --- |
| PN/ME primitive shell reduction | valid in stated post-ZF scope |
| AD/D1 P1/S1 one-defect split | valid in primitive equilateral-shell scope |
| AC endpoint switch / defect-sign rule | valid |
| SC P1 Littlewood closure | valid |
| RL zero-residue exclusion | valid |
| O3 order-three exclusion | valid |
| FRM nonexceptional slope `-1/r` and full multiplicity | valid |
| PRX complete P1 exclusion | **certified valid, scoped to primitive shell `d_H=1,s_Z=1`** |
| RSQ S1 reciprocal-square reduction | **certified valid, scoped to primitive S1** |
| S1 excluded | not proved |
| `q=13` S1 closure/KKT/PSD package | independently reproduced numerical regression |
| `q=13` source is a global Erdős-99 minimizer | not claimed / not proved |
| general Woodall `d_H=1` forest branch excluded | not proved; P1/S1 are a narrower primitive-shell normal form |

The correct remaining primitive-shell obligation is S1 with a genuinely global-source ingredient. A shell-only algebraic/KKT/PSD contradiction is blocked by the `q=13` regression.
