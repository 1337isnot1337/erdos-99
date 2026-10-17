> Generated reading edition · [exact source](../../../docs/audits/target_c_section101_complement_gap_hostile_audit_2026-09-12.md) · source SHA-256 `f6b2e7951db46e0c28c23096e80c972ea9e23b5c8d43c23077230ee4be4dc2ca`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3AD031E7EF66","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C Section 101 complement-gap hostile audit

**Date:** 2026-09-12  
**Verdict:** PASS as a proof-only theorem; theorem-state promotion remains separate.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit independently checks Section 101's complement-gap/chord argument on top of
canonical audit.40 Section 100. The claimed wrapping threshold

```math
\mu_8=0.976040765267051982\ldots
```

is valid. The audit also supplies the equality-case argument that is only summarized
in Section 101: at the sharp scalar endpoint the limiting support is, up to rotation
and reflection, one closed circular arc plus two isolated support points.

## 1. Inputs and scope

Let `S` be a compact wrapping subset of the radius-`1/2` circle with pairwise minor
angular distance at most `theta<pi`. Put

```math
\phi=2\pi-2\theta,
\qquad
U=3\theta-2\pi.
```

Canonical Section 100 gives

```math
|S|\le U,
\qquad
2\alpha\le |S|,
```

for every wrapping Type-II attachment limit, where `alpha=lim a_D/D` after passing to
a subsequence. Canonical Section 94 gives three distinct support-free central arcs of
length `phi`.

The audit uses no Cauchy perimeter inequality, no Section-97/98 endpoint theorem, no
KKT coefficient floor, and no deletion of contact-isolated source points.

## 2. Complement-gap bookkeeping is correct

Write

```math
\mathbb T\setminus S=\bigsqcup_j G_j,
\qquad |G_j|=g_j.
```

Each complement component has endpoints in `S`. Wrapping excludes `g_j>=pi`: a gap
larger than `pi` puts `S` in an open semicircle, while a gap exactly `pi` has antipodal
endpoints in `S`, contradicting `theta<pi`. Therefore `0<g_j<pi`, and the pairwise
angular-diameter hypothesis gives

```math
g_j\le\theta.
```

The three Section-94 forbidden arcs lie in three distinct complement components because
the three wrapping anchors separating them lie in `S`. Hence at least three distinct
gaps satisfy `g_j>=phi`.

Section 100 gives

```math
\sum_j g_j=2\pi-|S|\ge 4\pi-3\theta
=\theta+2\phi.
```

No multiplicity or connected-component assumption is missing here.

## 3. The complement-chord majorization lemma passes

Set `f(x)=sin(x/2)` on `[0,theta]`. It is strictly increasing and strictly concave on
the positive interval.

First consider a finite feasible gap vector of total mass

```math
H=\theta+2\phi.
```

After sorting decreasingly, the largest entry is at most `theta`; because two other
entries must remain at least `phi`, the sum of the two largest entries is at most
`theta+phi`. Thus

```math
(\theta,\phi,\phi,0,\ldots)
```

majorizes every feasible vector of mass `H`. Karamata for concave `f` therefore gives

```math
\sum_j \sin(g_j/2)
\ge
\sin(\theta/2)+2\sin(\phi/2)
=
\sin(\theta/2)+2\sin\theta.
```

If the finite total mass is larger than `H`, decrease entries while preserving three
entries at least `phi` until the total is `H`; monotonicity of `f` can only decrease the
sum.

For a countable complement, choose finite subfamilies containing the three guaranteed
`phi`-gaps and carrying total mass at least `H-epsilon`. The same finite argument gives

```math
\sum_{j\in J_\epsilon}\sin(g_j/2)
\ge
\sin((\theta-\epsilon)/2)+2\sin(\phi/2)
```

for small `epsilon`. Letting `epsilon` decrease to zero proves the countable statement.
The series is harmless because `sin(g_j/2)<=g_j/2` and `sum g_j<=2pi`.

Therefore Section 101's chord floor

```math
\boxed{
\sum_j\sin(g_j/2)
\ge
\sin(\theta/2)+2\sin\theta
}
```

is valid.

## 4. The finite outer-walk transfer passes

Fix any finite family of complement components. Hausdorff convergence of the scaled
finite attachment sets to `S` has two consequences for every fixed small `eta>0` and
all sufficiently large `D`:

1. the central `eta`-trimmed subarc of each chosen complement gap contains no finite
   attachment;
2. distinct limit complement components produce distinct finite consecutive-attachment
   intervals, because the separating support contains a point of `S` and therefore a
   nearby finite attachment.

Thus a limit gap `g_j` produces a finite angular gap at least `g_j-2eta`. Type-II
annular convergence gives endpoint radii `(1/2+o(1))D`, so the corresponding endpoint
chord has length at least

```math
D\sin((g_j-2\eta)/2)-o(D).
```

The canonical Section-62 outer-face route between those consecutive attachments is a
unit-edge chain with the same endpoints, hence costs at least that chord length. The
selected routes are disjoint intervals of the outer-face walk in the same multiplicity
convention used by Section 62.

For `k` selected macroscopic intervals, all unselected consecutive-attachment
intervals cost at least two edges except the `c_D^partial` direct loaded-loaded
contacts. Hence

```math
L_D\ge
D\sum_{i=1}^k\sin((g_{j_i}-2\eta)/2)
+2(a_D-k)-c_D^\partial-o(D).
```

Insert the exact Section-82 identity

```math
L_D+Q_D=4a_D-6-2s_D-2c_D.
```

Using `c_D^partial<=c_D` and dropping only favorable nonnegative terms gives, after
dividing by `D`,

```math
2\alpha
\ge
\sum_{i=1}^k\sin((g_{j_i}-2\eta)/2).
```

Take `D` to infinity, then `eta` to zero, then increase the finite family. Monotone
convergence gives

```math
\boxed{
2\alpha\ge\sum_j\sin(g_j/2)
\ge\sin(\theta/2)+2\sin\theta.
}
```

The countable complement is therefore charged legitimately; Section 101 does not sum
infinitely many finite outer-walk intervals at a fixed `D`.

## 5. Scalar threshold and carrier transfer pass

Canonical Section 100 gives the opposite ceiling

```math
2\alpha\le3\theta-2\pi.
```

Thus every wrapping Type-II limit must satisfy

```math
F(\theta):=
3\theta-2\pi-\sin(\theta/2)-2\sin\theta\ge0.
```

On `[2pi/3,pi)`,

```math
F'(\theta)
=3-\frac12\cos(\theta/2)-2\cos\theta
\ge\frac{15}{4}>0.
```

Hence `F` has a unique zero. The repository certificate reproduces

```math
\theta_8=2.7029080296483676832\ldots,
\qquad
\mu_8=\sin(\theta_8/2)
=0.9760407652670519821\ldots .
```

Therefore

```math
\boxed{\lambda\ge\mu_8.}
```

The Section-88 cap-family propagation is unchanged: for each fixed `mu<mu_8`, a
macroscopic cell limit with normalized diameter at most `mu` cannot wrap and is cap
type. The cap-area gap stays strictly positive at `mu_8`, while Section 83 supplies the
summed local rhombic-deficit control. The actual-carrier conclusion in Section 101 is
therefore valid.

## 6. Equality case: the complement vector is exactly `(theta,phi,phi)`

The endpoint description deserves an explicit proof.

Suppose `theta=theta_8`. The scalar equality and the two density bounds force

```math
2\alpha=|S|=U_8:=3\theta_8-2\pi
```

and

```math
\sum_j\sin(g_j/2)
=
\sin(\theta_8/2)+2\sin\theta_8.
```

Therefore the complement has exactly the minimum allowed total mass

```math
\sum_jg_j=\theta_8+2\phi_8.
```

Any positive extra complement mass would strictly increase the chord sum because
`f` is increasing. With the total fixed, strict concavity makes Karamata equality
rigid: splitting any positive extremal gap or replacing `(theta_8,phi_8,phi_8)` by a
non-permutation feasible vector strictly raises the sum. Hence the positive complement
components are exactly three gaps, with lengths

```math
\boxed{(\theta_8,\phi_8,\phi_8)}
```

up to cyclic order.

## 7. Equality case: one support arc plus two isolated points is forced

This last step is stronger than merely exhibiting an extremizer.

Order the three complement gaps cyclically as `theta_8,phi_8,phi_8`. Their closed
complement consists of three closed support arcs of lengths `x,y,z>=0` with

```math
x+y+z=U_8.
```

Let `x` be the support arc immediately following the `theta_8` gap. If `x>0`, choose a
support point an angular distance `t` into that arc with

```math
0<t<\min\{x,\phi_8\}.
```

Together with the support endpoint at the other side of the `theta_8` gap, this gives
clockwise angular separation `theta_8+t`, which lies strictly in

```math
(\theta_8,\theta_8+\phi_8)
=(\theta_8,2\pi-\theta_8).
```

Its minor angular distance is therefore strictly larger than `theta_8`, a
contradiction. Thus `x=0`. The identical argument on the other side of the
`theta_8` gap gives `z=0`, so `y=U_8`.

Consequently, up to rotation and reflection,

```math
\boxed{
S=(\text{one closed arc of length }U_8)
\cup\{p,q\},
}
```

where `p,q` are the two isolated support points. This proves the endpoint concentration
asserted in Section 101 rather than merely supplying one example.

Numerically,

```math
\phi_8=0.877369247882851\ldots,
\qquad
U_8=1.825538781765516\ldots,
\qquad
\alpha_8=0.912769390882758\ldots .
```

## 8. Verdict and next theorem

**PASS.** Section 101's `0.976040765267052...` wrapping threshold, actual-carrier
transfer, and endpoint support concentration are valid conditional on canonical
Section 100. No theorem-state claim is changed by this audit.

The sharp endpoint now has a concrete finite-scale target. Equality in the outer-walk
ledger must force the three macroscopic complement-gap routes to be near-geodesic,
including one route of length approximately `mu_8 D`, while almost all attachments lie
at saturated unit-spacing density on the single surviving support arc. The natural
next theorem is to combine those two facts and extract the resulting two-edge
near-equilateral boundary teeth before coupling them to the canonical Section-91
ordered interior grid.
