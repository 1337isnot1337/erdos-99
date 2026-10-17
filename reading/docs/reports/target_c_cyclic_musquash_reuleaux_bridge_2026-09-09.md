> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_musquash_reuleaux_bridge_2026-09-09.md) · source SHA-256 `1f3bc0ecc8e9c9abefdd2798a2a254cf88b037ed967b7a03505adeaa1e23afb8`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C091D3289BA9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact Reuleaux leaf composition of the `d_H=0` shell

**Date:** 2026-09-09  
**Run type:** exact graph/geometric composition lemma  
**Target:** Target C cyclic `d_H=0` Reinhardt endpoint  
**Depends on:** PR #118 exact Reinhardt completion, connected odd-cycle-plus-leaves diameter graph, equal projective diameter spacing, and diameter/contact transition duality  
**External literature:** none beyond the Reinhardt completion already used in #118  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

PR #118 already proves that the exact `d_H=0` shell has a width-`D` Reuleaux completion `R`, that its full diameter graph is one odd cycle with direct leaves, and that every force-hull side is a unit chord of a radius-`D` boundary arc with central angle `pi/q`.

The missing local bookkeeping is exact.

Let

```math
v_0,\ldots,v_{r-1}
```

be the unique odd diameter-cycle vertices in cycle order. Let `p_i` be the number of pendant diameter leaves adjacent to `v_i`.

### Theorem LC — leaf composition

The Reuleaux boundary arc centered at `v_i` contains exactly the shell path

```math
P_i:v_{i-1}\leadsto v_{i+1}
```

whose internal vertices are the `p_i` pendant diameter leaves adjacent to `v_i`. Consequently

```math
\boxed{|E(P_i)|=p_i+1.}
\tag{LC.1}
```

If

```math
\ell_i:=p_i+1,
```

then

```math
\boxed{\ell_i\in\mathbb Z_{>0},\qquad \sum_{i=0}^{r-1}\ell_i=q,}
\tag{LC.2}
```

and the corresponding Reuleaux arc has angular length

```math
\boxed{\phi_i=\ell_i\frac\pi q.}
\tag{LC.3}
```

At the same cycle vertex,

```math
\boxed{\deg_H(v_i)=\ell_i+1.}
\tag{LC.4}
```

Every non-cycle diameter vertex is a leaf. Hence

```math
\boxed{\Delta(H)=1+\max_i\ell_i.}
\tag{LC.5}
```

Thus one positive odd-length composition `(ell_i)` simultaneously records the Reuleaux arc lengths, pendant diameter populations, and local diameter degrees.

---

## 1. The diameter star at a cycle vertex is one contiguous block

Fix `v_i`. Its diameter neighbors are

```math
v_{i-1},\quad v_{i+1},
```

plus exactly `p_i` leaves

```math
w_{i,1},\ldots,w_{i,p_i}.
```

The cyclic endpoint transition theorem says all diameter edges incident to one terminal occur consecutively in projective diameter-direction order.

The two cycle edges must be the endpoints of this block. A pendant edge cannot be a block endpoint on the leaf side because its leaf endpoint has diameter degree one; the neighboring direction transition must therefore continue through the common nonleaf endpoint `v_i`.

After reversing the local order if necessary, the block is

```math
v_iv_{i-1},
\quad
v_iw_{i,1},\ldots,v_iw_{i,p_i},
\quad
v_iv_{i+1}.
\tag{1.1}
```

It contains `p_i+2` diameter edges and therefore `p_i+1` internal consecutive-edge transitions.

---

## 2. The transitions are exactly one contact path

The diameter/contact transition duality says that two consecutive diameter edges sharing endpoint `v_i` have their two nonshared endpoints joined by one unit shell contact.

Applying this successively to (1.1) gives

```math
v_{i-1}w_{i,1},
\quad
w_{i,1}w_{i,2},
\ldots,
\quad
w_{i,p_i}v_{i+1},
```

with the direct contact `v_{i-1}v_{i+1}` when `p_i=0`.

These contacts form the path

```math
\boxed{
P_i=(v_{i-1},w_{i,1},\ldots,w_{i,p_i},v_{i+1}).
}
\tag{2.1}
```

Therefore `|E(P_i)|=p_i+1`, proving LC.1.

---

## 3. These paths partition the shell cycle

For a diameter terminal `x`, a contiguous star of degree `d_x` contributes exactly `d_x-1` internal direction transitions.

Summing over all `q` terminals and using `h=q`,

```math
\sum_x(d_x-1)
=2h-q
=q.
\tag{3.1}
```

There are exactly `q` cyclic direction transitions in total. Hence every direction transition is internal to one star block.

Only cycle vertices have degree greater than one; diameter leaves contribute zero. Therefore the paths `P_i` account for every transition. The transition/contact bijection then gives

```math
\boxed{E(C_q)=\bigsqcup_i E(P_i).}
\tag{3.2}
```

Their edge counts sum to

```math
\sum_i(p_i+1)=q.
```

With `ell_i=p_i+1`, this proves LC.2.

Contracting the internal leaves of each `P_i` leaves the contact edge `v_{i-1}v_{i+1}`. Since `r` is odd, these step-two edges form one cycle on the defining Reuleaux vertices.

---

## 4. Each path lies on one Reuleaux arc

The exact Reinhardt completion in #118 associates to each diameter-cycle vertex `v_i` a radius-`D` Reuleaux boundary arc centered at `v_i`, running between the cycle neighbors `v_{i-1}` and `v_{i+1}`.

Every internal vertex `w_{i,j}` of `P_i` is a diameter neighbor of `v_i`, so

```math
|w_{i,j}-v_i|=D.
```

The whole source lies in the disk `B(v_i,D)`. Therefore every point of `P_i` lies on the boundary circle of that disk and on the corresponding Reuleaux boundary arc.

Consecutive diameter directions in the exact equality shell differ by

```math
\frac\pi q.
```

Within one star block they use one common Euclidean lift. Thus consecutive vertices along `P_i` subtend exactly `pi/q` at the center `v_i`.

There are `ell_i=p_i+1` such subarcs, so the full arc angle is

```math
\phi_i=\ell_i\frac\pi q,
```

proving LC.3.

The graph degree identity

```math
\deg_H(v_i)=p_i+2=\ell_i+1
```

proves LC.4, and LC.5 follows because all off-cycle vertices have degree one.

`\square`

---

## 5. Why this is the correct discrete variable

The composition

```math
(\ell_0,\ldots,\ell_{r-1}),
\qquad
\sum\ell_i=q,
```

is the pointwise bridge between the exact Reinhardt geometry and the diameter graph:

```text
ell_i shell chords
    <-> one Reuleaux arc of angle ell_i*pi/q
    <-> p_i=ell_i-1 pendant diameter leaves
    <-> diameter degree ell_i+1 at its center.
```

The parent PR already controls the total completion area and the cycle length. A composition-sensitive area theorem can now control the largest local diameter star directly.

---

## 6. Regression audit

- No regularity of the Reinhardt polygon is used.
- The cycle vertices need not occur consecutively along the shell; each arc can contain an arbitrary positive number `ell_i` of unit shell chords.
- The exact cap-area identity in #118 is compatible: summing all `ell_i` gives exactly `q` equal small circular segments.
- The theorem is specific to `d_H=0`; the tree phases have missing diameter directions and do not have this exact Reuleaux composition.

---

## 7. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Unique diameter cycle vertices v_i have p_i direct diameter leaves.
Contiguous-star order at v_i is
  v_iv_{i-1}, leaves at v_i, v_iv_{i+1}.
The p_i+1 internal transitions are exactly the shell contact path
  P_i: v_{i-1} -- leaves(v_i) -- v_{i+1}.
These P_i partition all q shell contacts.

Set ell_i=p_i+1. Then
  ell_i>=1, sum ell_i=q.
In the exact Reinhardt completion, P_i lies on the radius-D Reuleaux arc centered at
v_i. Each unit shell chord subtends pi/q, hence
  phi_i=ell_i*pi/q.
Also
  deg_H(v_i)=ell_i+1,
  Delta(H)=1+max ell_i.

Next: apply a composition-sensitive Reuleaux area deficit to bound max ell_i.
```
