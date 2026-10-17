> Generated reading edition · [exact source](../../../docs/reports/target_c_chain_track_interval_normal_form_2026-09-01.md) · source SHA-256 `7547404c04ce17085c4a568bc25717524d9d2d97c8ed2456933765183fd55764`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2F9724F373C1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: chain-track interval normal form

**Date:** 2026-09-01  
**Run type:** exact cross-route structural reduction  
**Target:** Target C C-II / C80–C82 chain-face branch  

## LEVEL I STATUS

`STILL OPEN`.

This report proves an exact normal form for how every active diameter bar acts on the
`D` parallel train tracks forced by C80. It does not yet prove the ordered shell-rank
contradiction, but it removes arbitrary coefficient patterns on the chain atom.

## 1. Starting point

Assume the pure simply connected strict-rhombic train-coordinate setting of Target B
and the exact C80 chain face. Thus one active diameter bar

```math
h_0=za,
\qquad |z-a|=D,
```

is the literal straight `D`-edge unit-contact chain

```math
z=x_0,x_1,\ldots,x_D=a.
```

Write

```math
u=\frac{a-z}{D}.
```

C80 gives `D` distinct train tracks

```math
P=\{\tau_1,\ldots,\tau_D\}
```

such that

- the chain edge `x_{j-1}x_j` belongs to `\tau_j`;
- every `\tau_j` has projective unit-edge direction `u`;
- the tracks are pairwise disjoint and occur in the order `\tau_1,\ldots,\tau_D`
  along the chain from `z` to `a`;
- these are exactly the train tracks separating `z` from `a`.

For any ordered vertex pair `h=xy`, retain Target B's train-coordinate notation

```math
r_h=p_x-p_y,
\qquad
 d_{h\tau}=\epsilon_\tau(x)-\epsilon_\tau(y)\in\{-1,0,1\},
```

and, for an active diameter bar, the gradient/Hessian formulas

```math
(g_h)_\tau=r_h\cdot J(d_{h\tau}u_\tau),
\tag{C83.1}
```

and

```math
(H_h)_{\tau\tau}=d_{h\tau}^2-r_h\cdot(d_{h\tau}u_\tau),
\qquad
(H_h)_{\tau\sigma}
=(d_{h\tau}u_\tau)\cdot(d_{h\sigma}u_\sigma)
\quad(\tau\ne\sigma).
\tag{C83.2}
```

## 2. Ordered separator lemma

### Lemma C83.1

After orienting every track in `P` so that `z` lies on its `0` side and `a` lies on
its `1` side, there is, for every source vertex `v`, an index

```math
k(v)\in\{0,1,\ldots,D\}
```

such that

```math
\epsilon_{\tau_j}(v)=
\begin{cases}
1,&j\le k(v),\\
0,&j>k(v),
\end{cases}
\tag{C83.3}
```

up to reversing all `0/1` conventions simultaneously.

Consequently, for every ordered pair `h=xy`, there are integers

```math
0\le a_h\le b_h\le D
```

and a sign `\sigma_h\in\{\pm1\}` such that

```math
\boxed{
 d_{h\tau_j}
 =\sigma_h\,\mathbf 1_{\{a_h<j\le b_h\}}.
}
\tag{C83.4}
```

The empty interval is allowed when no chain track separates `x` and `y`.

### Proof

Each train track in `P` is a properly embedded boundary-to-boundary arc in the
rhombic disk. Tracks of one projective direction do not cross. Every `\tau_j`
separates `z` from `a`, and the tracks meet the chain in the displayed order.

Let `Z_j` be the component of the disk cut by `\tau_j` that contains `z`. By the
Jordan separation theorem and pairwise disjointness, the `Z_j` are nested in chain
order: after choosing the indexing above,

```math
Z_1\subset Z_2\subset\cdots\subset Z_D.
```

Indeed, if two disjoint `z`–`a` separators were not nested, a path from `z` to the
first separator and a path from the second separator to `a` would force the two
proper arcs to cross. Equivalently, the components between consecutive tracks form a
linear sequence from `z` to `a`.

A fixed vertex `v` therefore lies on the `a` side of an initial segment of the
ordered tracks and on the `z` side of the rest. This proves (C83.3). Subtracting the
two threshold vectors for `x` and `y` gives one signed consecutive interval, proving
(C83.4). `\square`

## 3. Exact gradient and Hessian on the chain atom

For a nonempty interval

```math
I_h=\{a_h+1,\ldots,b_h\}
\subseteq\{1,\ldots,D\},
```

put

```math
c_h:=\sigma_h\,r_h\cdot u,
\qquad
\eta_h:=\sigma_h\,r_h\cdot Ju.
\tag{C83.5}
```

### Theorem C83.2 (interval normal form)

For every active diameter bar `h`, its restriction to the C80 chain tracks is

```math
\boxed{
 g_h|_P=\eta_h\,\mathbf 1_{I_h},
}
\tag{C83.6}
```

and

```math
\boxed{
 H_h[P,P]
 =\mathbf 1_{I_h}\mathbf 1_{I_h}^{\mathsf T}
  -c_h I_{I_h},
}
\tag{C83.7}
```

where `I_{I_h}` is the diagonal projector onto the interval coordinates.
Moreover, for every `\tau\in I_h`,

```math
\boxed{
\lambda_{h\tau}=r_h\cdot(d_{h\tau}u)=c_h.
}
\tag{C83.8}
```

Thus one active diameter bar is **uniformly forward, uniformly backward, or uniformly
tangent on its entire chain-track interval**. It cannot change sign from one chain
track to another.

### Proof

On `P`, all unit-edge direction vectors equal `u`, and Lemma C83.1 gives
`d_{h\tau}=\sigma_h` on `I_h` and zero off `I_h`. Equation (C83.1) immediately gives
(C83.6). For `\tau,\sigma\in I_h`, `\tau\ne\sigma`, equation (C83.2) gives

```math
(H_h)_{\tau\sigma}=\sigma_h^2(u\cdot u)=1,
```

while on the diagonal

```math
(H_h)_{\tau\tau}=1-\sigma_h r_h\cdot u=1-c_h.
```

All rows and columns off `I_h` vanish in the `P\times P` restriction. This is exactly
(C83.7), and (C83.8) is the definition of the Target B radial coefficient. `\square`

## 4. Prefix-variable form of every first-order diameter constraint

For a chain-track velocity `v\in\mathbb R^P`, define prefix variables

```math
X_0=0,
\qquad
X_k=\sum_{j=1}^k v_{\tau_j}
\quad(1\le k\le D).
\tag{C83.9}
```

Then (C83.6) gives

```math
\boxed{
 g_h\cdot v
 =\eta_h(X_{b_h}-X_{a_h}).
}
\tag{C83.10}
```

Hence every nonparallel active diameter bar imposes only one equality between two
prefix variables. The arbitrary `D`-coordinate gradient matrix collapses to an
interval-endpoint graph on the `D+1` prefix indices.

Let

```math
W_P=\left\{v\in\mathbb R^P:\sum_{\tau\in P}v_\tau=0\right\},
\tag{C83.11}
```

so `X_D=X_0=0`. The C80 chain bar has

```math
I_{h_0}=P,
\qquad c_{h_0}=D,
\qquad \eta_{h_0}=0,
```

and therefore

```math
\boxed{
H_{h_0}[v,v]=-D\|v\|^2
\qquad(v\in W_P).
}
\tag{C83.12}
```

This recovers C80 directly from the interval normal form.

## 5. Exact sign classification on chain-supported neutral motions

A diameter segment parallel to `u` has the same unoriented direction as `h_0`.
There cannot be a second distinct active diameter segment in that direction: if two
parallel length-`D` segments differ by a nonzero translation `s`, then the two cross
vectors are `r+s` and `r-s`, and

```math
|r+s|^2+|r-s|^2=2D^2+2|s|^2>2D^2,
```

so one source distance exceeds `D`.

Thus every active diameter bar `h\ne h_0` that meets `P` has `\eta_h\ne0`. For a
velocity supported on `P` and first-order neutral for all active diameter bars,
(C83.10) therefore gives

```math
X_{b_h}=X_{a_h}
\qquad(h\ne h_0).
\tag{C83.13}
```

Substituting into (C83.7) yields the exact scalar sign law

```math
\boxed{
H_h[v,v]
=-c_h\sum_{\tau\in I_h}v_\tau^2
\qquad
(h\ne h_0,\ v\text{ supported on }P,\ g_k\cdot v=0\ \forall k).
}
\tag{C83.14}
```

Therefore:

- `c_h>0` (forward) gives nonpositive quadratic curvature, strict when `v` is
  nonzero on `I_h`;
- `c_h=0` (tangent) gives zero quadratic curvature on every such neutral motion;
- `c_h<0` (backward) gives positive quadratic curvature whenever `v` is nonzero on
  `I_h`.

So, on the chain-supported first-order-neutral space, **every positive quadratic
blocker is a backward interval**. Forward bars can only help the chain bar shorten;
tangent bars are quadratically flat.

## 6. There is at most one tangent interval

### Corollary C83.3

Among all active diameter bars meeting `P`, at most one can be tangent on `P`.

### Proof

Tangency means `c_h=0`, hence `r_h\perp u`. All tangent bars therefore have the same
unoriented diameter direction `Ju`. As above, a diameter-`D` source contains at most
one segment in any prescribed unoriented direction. `\square`

Consequently the entire quadratic equality branch on chain-supported neutral motions
has at most one tangent diameter bar. If that bar is present, C43 remains relevant at
quartic order, but there is no family of different tangent directions on the C80
atom.

## 7. Terminal localization of backward intervals

Target B Section 42.3 proves that if a train `\tau` separates an active diameter bar
and `\lambda_{h\tau}\le0`, then both terminal boundary edges of `\tau` are non-hull
edges. Combining that theorem with (C83.8) gives:

### Corollary C83.4

If `c_h\le0`, then **every chain track in the entire interval `I_h` has two non-hull
terminal edges**.

Thus the only positive quadratic blockers on `W_P` are consecutive intervals made
entirely of doubly non-hull chain tracks. The unique possible tangent interval has the
same terminal localization.

## 8. Frontier effect

Before C83, the C80/C81 negative chain operator was opposed by an arbitrary family of
active diameter Hessians on `D` chain coordinates. C83 replaces that family by a much
smaller ordered object:

```text
chain tracks:       1,2,...,D
active diameter h:  one interval I_h=(a_h,b_h]
first variation:    eta_h * interval-sum
radial sign:        one scalar c_h on all of I_h
neutral Hessian:    -c_h * ||v on I_h||^2

forward interval    -> helps shortening
tangent interval    -> quadratic equality; at most one globally
backward interval   -> only possible positive quadratic blocker
backward/tangent    -> every track in interval has two non-hull terminals
```

Equivalently, in prefix variables every nonparallel diameter gradient is one edge
`a_h b_h` of a graph on `0,1,...,D`, while every positive quadratic obstruction is a
backward-labelled interval edge.

This is the promised interval-rank reduction from the C82 frontier. It does not yet
show that the backward interval graph has insufficient rank.

## 9. Exact next theorem

The next closing target is now substantially sharper than the general Target B
ordered shell-rank theorem:

> **Chain backward-interval rank theorem.** In the C80/C83 chain-face branch of a
> sufficiently large triangle-free pure-rhombic global minimizer, the family of
> backward interval edges on prefix vertices `0,...,D` cannot have rank `D-1` after
> imposing the full active-diameter first-order equalities; after deleting the unique
> possible tangent interval, there is a nonzero chain-supported neutral velocity that
> vanishes on every backward interval.

Any proof of this statement produces a nonzero `v\in W_P` for which `h_0` strictly
shortens, every forward bar is nonincreasing, every backward bar is flat, and the only
remaining higher-order obstruction is the single tangent interval. If the tangent
interval can also be avoided, all active diameters decrease or stay flat with
`h_0` strict, yielding the desired local diameter improvement.

The most concrete available inputs are C42.3's two non-hull terminals per backward
track, the linear family of degree-three reflex boundary vertices, the ordered
noncrossing same-phase train structure, and C82's prescribed chain-direction atom.
