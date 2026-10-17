> Generated reading edition · [exact source](../../../docs/reports/target_c_tb1_exact_swap_fork_2026-10-01.md) · source SHA-256 `ced28064414306264ae1e94de3995cdf7edc2abfdfd3cf86b98006d60dd04c12`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CD9E9F215D06","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- exact TB1 contact-swap fork in an open witness cell

Date: 2026-10-01  
Base main: 41b6e09938c4d382289f72f3614efc7af35298cc  
Status: proof-only; C-II remains open.

## 1. Statement

Work in the fixed-star complete O--O rectangle on current main. Fix one retained shore
and one active adjacent interface whose two selected train directions are distinct.
By the witness-cell blocker theorem, this is a TB1 interface and both train directions
lie in one open cell between two consecutive global actual-diameter directions.

Choose the coherent real lift so that

```math
\arg u_i=0,\qquad \arg u_{i+1}=-\varepsilon,
\qquad 0<\varepsilon\le {4K\over D}.
\tag{1}
```

For the physical middle strip, orient the two outside-to-middle unit boundary-contact
vectors as

```math
a=u_i,\qquad b=-u_{i+1}.
\tag{2}
```

Define

```math
q:=|a+b|,\qquad
w:={a+b\over q},\qquad
v_{\rm sw}:=-(a+b)=-qw.
\tag{3}
```

Then

```math
q=2\sin{\varepsilon\over2}\le\varepsilon\le {4K\over D}.
\tag{4}
```

The finite translation of the whole middle strip by $`v_{\rm sw}`$ has the following
exact properties.

1. Both boundary contact families remain unit contacts:
   
   ```math
   a+v_{\rm sw}=-b,\qquad
   b+v_{\rm sw}=-a.
   \tag{5}
   ```

   All other old contacts are unchanged.

2. For every switching actual diameter, orient its diameter vector inward toward the
   translated strip and call it $`n_h`$, so $`|n_h|=D`$. Then
   
   ```math
   \boxed{|n_h\cdot w|>{Dq\over2}.}
   \tag{6}
   ```


3. The TB1 certificate has $`n_h\cdot w>0`$. Hence exactly one of the following holds.

   **TWO-SIGN:** some switching actual diameter satisfies $`n_h\cdot w<0`$.

   **ONE-SIGN:** every switching actual diameter satisfies $`n_h\cdot w>0`$.

4. In the ONE-SIGN case every moving old actual diameter strictly shortens under the
   exact finite swap. Consequently canonical global minimality and
   diameter-pair-minimality force a previously strict source pair $`xy`$ satisfying
   
   ```math
   \boxed{1<|xy|\le1+{4K\over D}}
   \tag{7}
   ```

   or
   
   ```math
   \boxed{D-{4K\over D}\le|xy|<D.}
   \tag{8}
   ```


Thus every phase-changing TB1 cusp on the current fixed-star rectangle admits the
finite source-level fork

```math
\boxed{
\text{opposite-sign moving diameter}
\quad\text{or}\quad
\text{previously strict }O(D^{-1})\text{-near-active pair}.
}
\tag{9}
```

Unlike the older high-$`t`$ contact-swap theorem, this endpoint statement needs no
host-transversality constant and no cone-collapse estimate beyond the current
witness-cell localization.

## 2. Exact contact swap

From (2)--(3),

```math
a+v_{\rm sw}
=a-(a+b)=-b,
\qquad
b+v_{\rm sw}
=b-(a+b)=-a.
```

This proves (5).

Also the angle between $`a`$ and $`b`$ is $`\pi-\varepsilon`$. Therefore

```math
q^2
=|a+b|^2
=2+2\cos(\pi-\varepsilon)
=2-2\cos\varepsilon
=4\sin^2{\varepsilon\over2},
```

which proves (4).

The adjacent-strip translation moves one physical source layer rigidly. Every old
source-pair distance whose endpoints lie on the same side of that layer is exactly
unchanged. The only old contacts crossing its boundary are the two train contact
families in (2), and (5) preserves those exactly. Hence every old unit contact is
preserved.

## 3. The open witness cell gives an exact non-grazing bound

Let $`m`$ be the projective midpoint of the two adjacent train directions. The vector
$`w`$ is the quarter-turn of that midpoint direction.

Let $`(d_-,d_+)`$ be the open witness cell containing both train directions. The
boundary directions $`d_-,d_+`$ are consecutive global actual-diameter directions.
Because both train directions are strictly inside the cell and are separated by
$`\varepsilon`$,

```math
d_{\mathbb{RP}^1}(m,\{d_-,d_+\})>{\varepsilon\over2}.
\tag{10}
```

Every switching diameter is an actual diameter direction. It cannot be one of the two
cell-boundary witness rows because those fixed rows have full support across the
retained shore and therefore do not switch. It also cannot have the same projective
direction as either witness row: parallel diameter segments are unique.

Since the cell contains no global diameter direction, every switching diameter line
lies outside the open cell. Hence (10) gives

```math
d_{\mathbb{RP}^1}([n_h],m)>{\varepsilon\over2}.
\tag{11}
```

Because $`w=Jm`$,

```math
|n_h\cdot w|
=
D\sin d_{\mathbb{RP}^1}([n_h],m)
>
D\sin{\varepsilon\over2}
={Dq\over2}.
```

This proves (6). In particular, no switching diameter is tangent to the swap axis.

The current blocker theorem supplies a one-bar TB1 tangent certificate. The midpoint
$`w`$ lies in the interior of the strip-opening tangent arc, so that certificate has
strict positive projection on $`w`$. The TWO-SIGN / ONE-SIGN fork is therefore
exhaustive.

## 4. ONE-SIGN strictly shortens every moving old diameter

For a switching diameter $`h`$, the middle-strip translation changes its oriented
vector by $`v_{\rm sw}`$ after choosing the inward orientation $`n_h`$. Thus

```math
|r_h(v_{\rm sw})|^2-D^2
=
2n_h\cdot v_{\rm sw}+|v_{\rm sw}|^2
=
-2q(n_h\cdot w)+q^2.
\tag{12}
```

In the ONE-SIGN case, (6) gives

```math
n_h\cdot w>{Dq\over2}.
```

Substituting into (12),

```math
|r_h(v_{\rm sw})|^2-D^2
<
-Dq^2+q^2
=-(D-1)q^2<0
\tag{13}
```

for $`D>1`$. Thus every switching old diameter becomes strict. Every nonswitching old
diameter is unchanged exactly.

This is a finite statement at the full swap amplitude $`q`$, not a first-order
argument.

## 5. Minimality forces a near-active inactive pair

Assume the interface is ONE-SIGN. Suppose that after the exact swap every previously
strict noncontact still has distance $`>1`$, and every previously strict nondiameter
pair still has distance $`<D`$.

All old contacts remain unit by Section 2. Hence the contact count is unchanged.

All moving old diameter pairs become strict by (13), while nonswitching old diameter
pairs are unchanged. If a nonswitching diameter remains, the moved source is another
diameter-$`D`$ global minimizer with the same number of contacts and strictly fewer
diameter pairs, contradicting the canonical diameter-pair-minimal choice after
contact minimization.

If no nonswitching diameter remains, then every old diameter is strict and by the
assumption no previously strict pair reaches $`D`$. The new source has diameter
strictly below $`D`$, contradicting global minimality.

Therefore some previously strict pair $`xy`$ becomes either non-unit-separated or a
new diameter pair by the endpoint of the swap. Such a pair must straddle the moved
middle strip; otherwise its distance is unchanged. Only one endpoint moves, by a
vector of norm $`q`$, so the distance changes by at most $`q`$. Hence either

```math
1<|xy|\le1+q
```

or

```math
D-q\le|xy|<D.
```

Equation (4) gives (7)--(8).

This does not claim that the full swap is feasible in the ONE-SIGN case. The first
inactive constraint that prevents feasibility is exactly the near-active witness
recorded above. Thus the argument respects the canonical inactive-slack caution.

## 6. Linear consequence

Let $`U_D`$ be any family of phase-changing TB1 adjacent interfaces on one retained
shore. Partition it into TWO-SIGN and ONE-SIGN interfaces.

If at least half are TWO-SIGN, there are at least $`|U_D|/2`$ interfaces carrying an
opposite-sign pair of moving actual diameters.

If at least half are ONE-SIGN, select a nonadjacent subfamily of at least
$`|U_D|/4`$ interfaces. Their physical middle layers are disjoint. A fixed source pair
can be changed by translations of at most two such disjoint layers, one for each
endpoint. Choosing one witness from (7)--(8) at each selected interface therefore
produces at least

```math
\boxed{|U_D|/8}
\tag{14}
```

distinct previously strict $`4K/D`$-near-active source pairs.

In particular, whenever the TB1 side of the current blocker dichotomy has

```math
|U_D|\ge\left({c_*\over4}-o(1)\right)D,
```

one obtains either

```math
\left({c_*\over8}-o(1)\right)D
```

TWO-SIGN interfaces or

```math
\boxed{
\left({c_*\over32}-o(1)\right)D
}
```

distinct inactive pairs within $`4K/D`$ of the unit or diameter constraint.

## 7. Frontier effect

The phase-changing TB1 branch is no longer only an infinitesimal tangent-obstruction
family. It has an exact finite source-level alternative:

- **TWO-SIGN:** actual moving diameter support occurs on both sides of the swap axis;
  or
- **NEAR-ACTIVE:** a linear TB1 population forces a linear population of distinct
  inactive pairs at the precise inverse-$`D`$ scale.

The next closure target is to combine TWO-SIGN with the one-arc switching order and
the common transverse complete O--O shore, or to promote the NEAR-ACTIVE population
to a controlled augmented active system. The exact-direction TB2, split-star O--O,
and inactive-interface branches remain separate.

No computation, verifier, numerical experiment, CI result, or unexecuted verifier
code is used.
