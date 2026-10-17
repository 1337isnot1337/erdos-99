> Generated reading edition · [exact source](../../../docs/reports/target_c_chain_face_train_atom_2026-08-31.md) · source SHA-256 `3ee9edf20e147ea78debba90def88aaebd5a1b6a3d9d788f56a28a847ed15c00`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-0212E1586494","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C80: exact chain face creates a D-train atom

**Date:** 2026-08-31  
**Repository base:** `8cf163da` (main after C79 / PR #84)  
**Run type:** exact cross-route train-coordinate theorem  
**Target:** Target C Gate C-II / Target B pure-rhombic interface  
**Depends on:** C76 exact straight-chain KKT face; Target B Sections 26.6, 40--42 train coordinates, virtual-work identity, and diameter Hessian formulas  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C76 says an exact Target C star face is one diameter bar `h=za` of weight one and one
straight unit-contact chain of length `D`, every chain contact carrying stress `D`.
Target B supplies exact train coordinates for a simply connected pure rhombic disk.
C80 combines them.

If a pure-rhombic realization admits the C76 chain stress, then the `D` chain edges
belong to `D` **distinct** train tracks, all with exactly the chain direction. Those
are precisely the train tracks separating `z` and `a`. The chain diameter bar has zero
first derivative under every train-angle velocity, and its exact train-angle Hessian is

```math
\boxed{
H_h[v,v]
=-D\sum_{\tau\in P}(v_\tau-\bar v_P)^2,
}
```

where `P` is the `D`-track chain atom and

```math
\bar v_P=\frac1D\sum_{\tau\in P}v_\tau.
```

Thus one exact chain-face diameter bar contributes a rank-`D-1` negative-semidefinite
curvature operator on train-angle space. Equality means that all `D` chain tracks
co-rotate at one common angular rate.

This is the first exact operator-level bridge between Target C's one-dimensional KKT
limit and Target B's macroscopic train-angle neutral/equality spaces.

---

## 1. Train-coordinate conventions

Work in the pure simply connected strict-rhombic-disk setting of Target B Section 26.6.
There is one unit vector `u_tau` for every train track `tau` and one side label

```math
\epsilon_\tau(v)\in\{0,1\}
```

such that, up to translation,

```math
p_v=\sum_\tau \epsilon_\tau(v)u_\tau.
\tag{C80.1}
```

If `xy` is a unit contact edge, exactly one train coordinate changes between its
endpoints. Thus every contact edge has one train label `tau(xy)`, and after orienting
that train vector suitably,

```math
p_y-p_x=\pm u_{\tau(xy)}.
\tag{C80.2}
```

For an oriented diameter bar `h=za`, put

```math
r:=p_a-p_z,
\qquad |r|=D,
```

and

```math
d_\tau:=\epsilon_\tau(a)-\epsilon_\tau(z)\in\{-1,0,1\},
\qquad
a_\tau:=d_\tau u_\tau.
\tag{C80.3}
```

Then

```math
r=\sum_\tau a_\tau.
\tag{C80.4}
```

Target B Section 41 defines

```math
\lambda_\tau:=r\cdot a_\tau.
\tag{C80.5}
```

For any normalized KKT stress, if

```math
A_\tau:=\sum_{e\text{ a contact edge of }\tau}\alpha_e,
```

the exact train virtual-work identity is

```math
\boxed{
A_\tau=\sum_{k\in H}\beta_k\lambda_{k\tau}.
}
\tag{C80.6}
```

---

## 2. Insert the C76 chain stress

Assume the normalized stress is exactly the C76 face:

```math
H_s=\{h=za\},
\qquad
\beta_h=1,
\tag{C80.7}
```

and

```math
z=x_0,x_1,\ldots,x_D=a,
\qquad
p_{x_j}-p_{x_{j-1}}=u:=r/D,
\tag{C80.8}
```

with

```math
\alpha_{x_{j-1}x_j}=D
\qquad(1\le j\le D),
\tag{C80.9}
```

and all other contact stresses zero.

Let `m_tau` be the number of chain edges carrying train label `tau`. Then

```math
A_\tau=Dm_\tau.
\tag{C80.10}
```

Since there is only one positive diameter bar, C80.6 becomes

```math
A_\tau=\lambda_\tau.
\tag{C80.11}
```

But `|d_tau|<=1`, so

```math
\lambda_\tau=r\cdot(d_\tau u_\tau)\le D.
\tag{C80.12}
```

If `m_tau>=1`, equations C80.10-C80.12 give

```math
Dm_\tau\le D.
```

Hence:

### Lemma C80.1 — one chain edge per train

Every train track contains at most one positive chain edge. Since the chain contains
`D` edges, it uses exactly `D` distinct train tracks.

Call this set of tracks `P`.

For `tau in P`, equations C80.10-C80.12 give equality throughout:

```math
A_\tau=D,
\qquad
\lambda_\tau=D.
\tag{C80.13}
```

Equality in Cauchy--Schwarz forces

```math
d_\tau u_\tau=u=r/D.
\tag{C80.14}
```

Thus all tracks in `P` have one common projective direction, exactly the chain-contact
direction.

---

## 3. No other train separates the chain endpoints

Orient every train vector in `P` so that `u_tau=u`. Along the literal chain path

```math
x_0x_1\cdots x_D,
```

each train label in `P` occurs exactly once and no other label occurs.

The train side-label difference `d_tau` is path-independent: it is the net change of
the `tau` coordinate between `z` and `a`. Therefore the chain path gives

```math
\boxed{
 d_\tau=1\quad(\tau\in P),
\qquad
 d_\tau=0\quad(\tau\notin P).
}
\tag{C80.15}
```

Equivalently, `P` is exactly the set of train tracks separating the two chain
endpoints.

This also follows from C80.4 and C80.14, but the path argument rules out a hidden pair
of perpendicular zero-projection separating trains: a separating train must be crossed
by every primal path from `z` to `a`, while the straight chain path crosses only its
`D` labels.

Consequences:

```math
a_\tau=u\quad(\tau\in P),
\qquad
a_\tau=0\quad(\tau\notin P),
\tag{C80.16}
```

and hence

```math
\lambda_\tau=D\quad(\tau\in P),
\qquad
\lambda_\tau=0\quad(\tau\notin P).
\tag{C80.17}
```

---

## 4. The chain diameter gradient vanishes identically

Target B Section 41 gives the train-angle gradient

```math
(g_h)_\tau=r\cdot J a_\tau.
\tag{C80.18}
```

For `tau in P`, `a_tau=u` is parallel to `r`; for `tau notin P`, `a_tau=0`.
Therefore

### Lemma C80.2 — the exact chain bar is first-order invisible

```math
\boxed{g_h=0}
\tag{C80.19}
```

on the entire train-angle space.

Thus the C76 diameter bar contributes **no first-order train-angle row at all**. All
first-order train-angle locking in a pure-rhombic source must come from other active
diameter bars, even though the chain bar carries the entire beta mass of this KKT
stress.

This explains why the existence of the exact chain KKT face does not immediately
contradict Target B Section 40: the chain stress is maximally important mechanically
but first-order invisible to the rhombic train-angle coordinates.

---

## 5. Exact Hessian = negative variance on D chain tracks

Target B Section 41 gives, for a diameter bar,

```math
(H_h)_{\tau\tau}=d_\tau^2-\lambda_\tau,
\qquad
(H_h)_{\tau\sigma}=a_\tau\cdot a_\sigma
\quad(\tau\ne\sigma).
\tag{C80.20}
```

Using C80.15-C80.17:

- for `tau in P`, the diagonal entry is `1-D`;
- for distinct `tau,sigma in P`, the off-diagonal entry is `1`;
- every row/column outside `P` is zero.

Hence for every train-angle velocity `v`,

```math
\begin{aligned}
H_h[v,v]
&=(1-D)\sum_{\tau\in P}v_\tau^2
+2\sum_{\tau<\sigma\in P}v_\tau v_\sigma\\
&=\left(\sum_{\tau\in P}v_\tau\right)^2
-D\sum_{\tau\in P}v_\tau^2.
\end{aligned}
\tag{C80.21}
```

Put

```math
\bar v_P:=\frac1D\sum_{\tau\in P}v_\tau.
```

Then:

### Theorem C80 — exact chain-face train curvature

```math
\boxed{
H_h[v,v]
=-D\sum_{\tau\in P}(v_\tau-\bar v_P)^2
\le0.
}
\tag{C80.22}
```

Equality holds exactly when

```math
v_\tau=\bar v_P
\qquad\text{for every }\tau\in P.
\tag{C80.23}
```

Thus, modulo the global rotation direction, the chain bar contributes a negative
semidefinite operator of rank

```math
\boxed{D-1.}
\tag{C80.24}
```

Its nonzero eigenvalue is `-D` with multiplicity `D-1`, on the subspace of
zero-sum angular variations of the chain tracks.

The trace is therefore

```math
\boxed{\operatorname{tr}H_h=-D(D-1),}
\tag{C80.25}
```

matching Target B Section 41's general formula

```math
\operatorname{tr}H_h=k_h-D^2
```

because the chain endpoints are separated by exactly `k_h=D` train tracks.

---

## 6. Geometric meaning

The result has a simple interpretation. In train coordinates the chain endpoint vector
is

```math
r=\sum_{\tau\in P}u_\tau.
```

At the C76 face all `D` unit vectors `u_tau` are exactly aligned. Their sum has the
maximum possible length `D`. Rotating them independently while keeping their lengths
one cannot increase the endpoint distance; to second order it decreases by precisely
the angular variance C80.22. Only a common co-rotation leaves the chain diameter flat.

So the exact Target C chain face is not a higher-order blocker in the Target B train
system. It is a macroscopic **negative-curvature bar**.

---

## 7. Cross-route consequence for the Target B neutral space

Let

```math
V=\mathbb R^T/\langle\mathbf1\rangle
```

be the train-angle quotient and

```math
\mathcal L=\bigcap_{k\in H}\ker g_k
```

be Target B's first-order diameter-neutral space.

Because `g_h=0`, the chain bar does not lower `dim L`. Target B Section 40 still gives
in the pure-rhombic branch

```math
\dim\mathcal L\ge T-q
```

and asymptotically a positive multiple of `D`.

Define the chain-equality subspace

```math
E_P:=\{v\in V:v_\tau\text{ is constant on }P\}.
\tag{C80.26}
```

It has codimension `D-1` in `V`, and

```math
H_h[v,v]=0\iff v\in E_P.
```

Therefore every neutral train-angle direction

```math
v\in\mathcal L\setminus E_P
```

strictly shortens the chain diameter to second order. Any hypothetical locally
minimal source containing the exact chain KKT face must block every such direction by
**other** active diameter bars or by their higher-order equality/tangent mechanism.

This sharpens the open Target B shell-rank problem: the chain-face bar itself supplies
no positive curvature and no first-order rank; it contributes rank `D-1` of the wrong
sign.

A simple conditional corollary is worth recording. If `q<D`, then

```math
\dim\mathcal L\ge T-q>T-D=\dim E_P,
```

so

```math
\mathcal L\not\subset E_P.
```

Hence at least one first-order-neutral train direction strictly shortens the chain bar.
The global problem is that the actual near-round pure-rhombic regime need not satisfy
`q<D`, and the other diameter bars may still provide second/higher-order locking.

---

## 8. Why this matters for near-chain stresses

C80 is exact, not yet a uniform stability theorem. But it identifies the operator that
a C66 stress must approach if the normalized stress converges to the C76 face:

```text
D chain tracks with one common direction
chain diameter gradient = 0
chain Hessian = -D times variance on those D train angles
rank of negative curvature = D-1
```

This is the correct object to perturb. If one can prove a uniform spectral stability
statement saying that `S_z=1-o(1)` forces the KKT-weighted train Hessian to retain a
linear-dimensional negative subspace of size `Omega(D)`, then Target B Sections 42--43
would have to place all compensating higher-order blockers on diameter bars carrying
only the vanishing residual beta mass. That is a substantially sharper contradiction
target than counting active bars without weights.

The remaining difficulty is uniform stability of the exposed C76 face across growing
configurations: C76's compactness gap is configuration-dependent.

---

## 9. Regression audit

- A rectangular or oblique rhombic grid with a straight diameter row is consistent:
  it can contain the `D` parallel chain train tracks and many transverse tracks.
- C80 does **not** claim the exact chain face is impossible.
- Other active diameter bars may block train-angle directions even though they have
  zero beta weight in the chain stress.
- The theorem uses pure simply connected train coordinates. Extending it through the
  `O(D)` exceptional topology of general C-II remains a separate problem.
- No claim is made that a near-star stress already has one beta edge of weight
  `1-o(1)`; C66 only concentrates beta at one vertex.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C80 (pure rhombic disk + exact C76 chain face):
Let P be the train labels of the D positive chain contacts.
Target B virtual work gives A_tau=lambda_h,tau.
Since each chain contact has alpha=D and lambda<=D, every chain edge lies on a distinct
train and lambda=D there. Hence all D train directions equal the chain direction.
The literal chain path shows no other train separates z,a.
Therefore
  d_tau=1, lambda_tau=D for tau in P;
  d_tau=lambda_tau=0 outside P.
So
  g_h=0,
and for every train-angle velocity v,
  H_h[v,v]
    = -D sum_(tau in P)(v_tau-mean_P v)^2.
Thus H_h has negative rank D-1 and kernel exactly the modes co-rotating the D chain
tracks.

Next: prove a uniform near-face spectral stability theorem and combine it with Target B
Sections 42--43 higher-order blocker rank.
```
