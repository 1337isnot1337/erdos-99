> Generated reading edition · [exact source](../../research/target_c_all_bridge_transverse_interval_balance_2026-09-12.md) · source SHA-256 `a82af09058ea84ee8182f16d281eb5584e417a5a174331ad16a5c3845576b55a`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "780696671aec95f035ba65c297fa76735d1ac11e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_all_bridge_transverse_interval_balance_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1d99067f7cf79ae9dd710406979bae672d63e81aff619a18d4be1dd9f25d9684"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — all-bridge transverse bracing and straight-corridor interval balance

**Date:** 2026-09-12  
**Classification:** proved candidate awaiting hostile audit; proof-only.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Dependencies:** the C-II maximal-support normalization `C=C_*`, the positive KKT
stress, the exact bridge cut law, the parallel-diameter uniqueness lemma, and the
straight constant-stress bridge-corridor theorem in the canonical force-hull module.

This note strengthens the outer-to-outer train bracing statement.  The finite shore
shear does not use that the two train terminals are on the outer face; it only uses
that the cut contact is a bridge.  Consequently every positive-contact bridge has
diameter reactions on both transverse sides.  Along a straight chain of nested bridge
cuts, the transverse equations then become an exact interval telescoping identity.

The implication chain is

```text
positive bridge
  -> exact shore shear
  -> both transverse diameter signs
  -> straight bridge corridor gives signed interval balance
  -> long unchanged bracing profile or many interval endpoint events.
```

The last alternative has not yet been coupled to the canonical aggregate outer-walk
detour or to `e_BB-k`; no C-II closure is claimed.

## 1. Every positive bridge is two-sided braced

Work in the canonical C-II representative and choose a relative-interior normalized
KKT stress.  The `C=C_*` normalization identifies the positive-support contact graph
with the full actual unit-contact graph, and C65 identifies the positive diameter
support with the actual diameter graph.  Let `uv` be a bridge of this full contact
graph.  Orient it from the shore `T` to the shore `S` and write

```math
u_0:=p_v-p_u,
\qquad |u_0|=1.
```

Let `alpha>0` be the contact multiplier on `uv`.  Summing equilibrium over `S` gives
the exact bridge cut resultant

```math
\alpha u_0
 =\sum_{h=xy\in H,\ x\in T,\ y\in S}
       \beta_h(p_y-p_x).
\tag{1.1}
```

For a crossing diameter write `r_h=p_y-p_x`.  Taking the scalar product with `Ju_0`
gives

```math
\sum_{h\pitchfork uv}\beta_h(r_h\mathbin\cdot Ju_0)=0.
\tag{1.2}
```

We use the elementary fact that a finite set of diameter `D` has at most one
unordered diameter pair in a fixed projective direction.  Indeed, if
`b-a=d-c=Du` after orienting two parallel diameter pairs alike, then the two cross
distances `|Du-(c-a)|` and `|Du+(c-a)|` are both at most `D`; squaring and adding
forces `c=a`.

Assume the crossing transverse values in (1.2) do not contain both signs.  Positivity
of all `beta_h` forces every one of them to be zero.  All crossing diameter pairs are
therefore parallel to `u_0`, and the uniqueness fact leaves exactly one crossing pair.
Equation (1.1) then forces its shore-oriented vector to be `D u_0`.

Translate the entire shore `S` by

```math
\Delta_\theta=R_\theta u_0-u_0.
\tag{1.3}
```

The bridge remains a unit contact, every same-shore contact is unchanged, and all
other old noncontacts retain strict distance greater than one for sufficiently small
`theta`, by finiteness.  There is only one crossing diameter pair, and it changes to
`D u_0+\Delta_\theta`; exactly

```math
|D u_0+\Delta_\theta|^2
 =D^2-2(D-1)(1-\cos\theta)<D^2
\tag{1.4}
```

for `D>1` and nonzero sufficiently small `theta`.

If a same-shore diameter pair remains, (1.3) produces a same-diameter source with
strictly fewer actual diameter pairs, contradicting the secondary diameter-pair
normalization.  If none remains, the source diameter drops below `D`, contradicting
global minimality.  Hence every positive bridge has crossing diameter pairs `h_+`
and `h_-` with

```math
r_{h_+}\mathbin\cdot Ju_0>0,
\qquad
r_{h_-}\mathbin\cdot Ju_0<0.
\tag{1.5}
```

This is stronger in scope than the audited outer-to-outer train theorem: a bridge
whose two incident face occurrences are bounded is included.  No response-conductance
claim or individual KKT-weight lower bound is used.

## 2. Exact interval balance on a straight bridge corridor

Let

```math
x_0,x_1,\ldots,x_L
```

be a straight constant-stress bridge corridor, with consecutive bridge edges
`e_j=x_{j-1}x_j` and common oriented contact vector `u_0`, `1\le j\le L`.  Orient
the shore of the `e_j`-cut containing `x_0` as `S_j`.  These shores are nested.

For a positive diameter edge `h`, the path in the bridge-block tree intersects this
corridor in a (possibly empty) consecutive interval of cuts.  Write that interval as

```math
I_h=[\ell_h,r_h]\subseteq[1,L]
```

when it is nonempty, and orient its fixed diameter vector `r_h` from the endpoint on
the `S_j` side to the endpoint on the complementary side.  The orientation is
independent of `j\in I_h` because the cuts are nested.

Applying the bridge cut law to `e_j` gives

```math
\alpha_j u_0
 =\sum_{h:\,\ell_h\le j\le r_h}\beta_h r_h.
\tag{2.1}
```

Taking the transverse coordinate gives the exact zero-sum equations

```math
F_j:=
\sum_{h:\,\ell_h\le j\le r_h} y_h=0,
\qquad
y_h:=\beta_h(r_h\mathbin\cdot Ju_0),
\qquad 1\le j\le L.
\tag{2.2}
```

The finite difference of (2.2), with `F_0=F_{L+1}=0`, is

```math
\boxed{
\sum_{h:\,\ell_h=j}y_h
 =
\sum_{h:\,r_h=j-1}y_h,
\qquad 1\le j\le L+1.
}
\tag{2.3}
```

Thus the signed transverse mass entering a corridor level is exactly the signed mass
leaving the preceding level.  This is an equality of the actual positive KKT weights,
not merely an incidence or sign statement.  By (1.5), every occupied cut has both
positive and negative transverse contributors.

## 3. Profile/endpoint dichotomy

Let `Y_j` be the set of diameter edges whose intervals contain cut `j`.  The profile
`Y_j` changes only at a corridor interval endpoint.  If `E` is the number of distinct
levels at which at least one interval starts or ends, the corridor is partitioned
into at most `E+1` maximal blocks on which `Y_j` is constant.  Hence, for every
integer `M>=1`,

```math
\boxed{
\text{either some constant-profile block has length at least }M,
\quad\text{or }E\ge\left\lceil {L\over M}\right\rceil-1.
}
\tag{3.1}
```

On a constant-profile block, the same actual diameter paths cross every bridge cut and
their signed transverse KKT mass is zero at every level.  By (1.5) this fixed profile
contains both transverse signs.  Conversely, if no fixed profile persists for `M`
consecutive cuts, (3.1) forces at least `L/M-1` distinct endpoint levels.

The all-diameter common bridge profile is already excluded by the canonical common
bridge transfer theorem: the common intersection of all positive diameter paths is a
single bridge block.  A constant profile in (3.1) may still be a proper subset of the
diameter graph, so this note does not silently promote the exclusion to all subsets.

## 4. Exact status and next bridge

The new finite quantity is the signed endpoint balance (2.3).  Its intended use is

```math
\text{corridor endpoint events or a long common bracing profile}
longrightarrow
\text{Woodall/topological restriction or source-preserving descent}
longrightarrow
\text{upper control of }\sum_r(L_r-2d_r)\text{ or an exact unit triangle}.
```

What is proved here:

- every positive bridge is two-sided braced;
- every straight bridge corridor carries a zero transverse interval circulation;
- the circulation has the exact endpoint-bundle identity (2.3); and
- endpoint sparsity forces a long unchanged diameter-path profile.

What is not proved here:

- that a proper common profile is impossible;
- that corridor endpoint levels inject into the aggregate outer-walk detour;
- any uniform lower bound on a KKT weight; or
- a C-II or Level I conclusion.

**Disposition:** proved candidate awaiting hostile audit.  The theorem state and
canonical route map are unchanged.
