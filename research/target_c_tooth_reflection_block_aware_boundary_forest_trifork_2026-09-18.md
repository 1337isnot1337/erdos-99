<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8efbe6625b227bc32c983aee245d206a16b3a658", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_block_aware_boundary_forest_trifork_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "121ca293efa7fa24e4efdb155655f9a8d1dbb6448b25216d48316b1ad7d97f0b"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — upper blocks sharpen the fixed-pair boundary/forest obstruction

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion; proof-only sharpening of the fixed-pair boundary/forest route  
**Scope:** the `PAIR-REUSE` branch for the two extreme all-inactive FREE modules  
**Dependencies:** fixed-pair lossless common runs; all-run forest-union identity; two-boundary slack tradeoff; two-sided outer-face localization; common-trunk two-normal cone theorem; short-edge planarity  
**Certificate:** `research/verify_target_c_tooth_reflection_block_aware_boundary_forest_trifork_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding fixed-pair boundary/forest theorem charged the Euler correction to the
**number of upper gates**. That loses a constant for no geometric reason. A consecutive
block of upper gates interrupts the lower forest only once. The same block also contains
an upper edge that can be selected without conflicting with representatives of any
other upper block.

Replacing upper-gate count by upper-block count improves the finite minimax

\[
\max\left\{\frac Es-T,\frac T4\right\}
\]

to

\[
\max\left\{\frac Es-B,\frac B2\right\},
\]

and therefore replaces the factor `1/5` by `1/3`. No new external-population
hypothesis is introduced.

Fix

\[
h_*:=\frac{\sqrt{303}}{52},\qquad
c_*:=0.129220199818177\ldots,\qquad
b_*:=\sin(c_*/2),
\]

and a fixed `K>h_*`. Put

\[
\alpha_K:=1-\frac{h_*}{K}>0.
\tag{BA.1}
\]

On the `PAIR-REUSE` side of the fixed extreme-pair theorem, the two FREE ancestries
share a set `E_*` of distinct original lower-gate edges with

\[
E:=|E_*|\ge\left(\frac{\alpha_K}{2}-o(1)\right)D,
\tag{BA.2}
\]

and

\[
1<|e|\le1+\frac KD
\qquad(e\in E_*).
\tag{BA.3}
\]

Their canonical support normals satisfy

\[
c_*-o(1)\le\theta_D\le\frac\pi2+o(1).
\tag{BA.4}
\]

The complementary fixed-pair branch already yields the linear inverse-`D` matching.
Everything below concerns `PAIR-REUSE`.

## 1. Upper blocks are the exact lower-forest separators

For ancestry `i`, let `B_i` be the number of maximal nonempty consecutive blocks of
upper gates. Put

\[
B:=B_1+B_2.
\tag{BA.5}
\]

Deleting those upper blocks leaves at most `B_i+1` maximal all-lower runs. Keep only
lower runs containing at least one edge of `E_*`, and call the resulting path forests
`\mathcal P,\mathcal Q`. If their component counts are `p,q`, then

\[
\boxed{
p\le B_1+1,\qquad q\le B_2+1,
\qquad p+q\le B+2.
}
\tag{BA.6}
\]

Let

\[
H:=\mathcal P\cup\mathcal Q,
\qquad I:=\mathcal P\cap\mathcal Q.
\]

All lower edges lie in the common plane graph `P_{<sqrt(2)}(A)`. The exact two-forest
Euler identity is

\[
\beta(H)=c_H-p-q+c_I.
\]

Since `E_*>0`, the union has at least one component, so `c_H>=1`. Hence

\[
\boxed{
\beta(H)\ge c_I-B-1.
}
\tag{BA.7}

This is strictly stronger than charging `c_I` by the total number of upper gates when
an ancestry contains a nontrivial upper block.

## 2. One representative from every upper block is already a matching

Consider one ancestry with upper blocks

\[
[a_1,b_1],\ldots,[a_r,b_r]
\]

in ancestry-edge index order. Distinct maximal upper blocks are separated by at least
one lower edge, so

\[
a_{j+1}\ge b_j+2.
\tag{BA.8}
\]

Choose the **first upper edge** of every block. Its edge index is `a_j`. Equation
(BA.8) implies

\[
a_{j+1}\ge a_j+2,
\]

so no two chosen path edges share an ancestry vertex. Thus the block representatives
form a vertex-disjoint source matching of size exactly `B_i`.

Every representative is an original strict subdiameter pair. The two-boundary slack
ledger gives, for each ancestry separately,

\[
\boxed{
\sum_{e\in M_i^{\rm blk}}(D-|e|)
\le
\sum_{e\in E_{{\rm up},i}}(D-|e|)
\le t_D
<h_*+D^{-1/3}.
}
\tag{BA.9}
\]

The child of every inactive upper gate lies outside the force hull `F`. Because the
chosen first edges are disjoint, their children are distinct. Consequently

\[
\boxed{Z_D:=|A\setminus F|\ge B_i}
\tag{BA.10}
\]

for each ancestry, although no bound on `Z_D` is assumed in the theorem.

Choose the ancestry with more upper blocks. Its representative matching
`M_{\rm up}^{\rm blk}` satisfies

\[
\boxed{
|M_{\rm up}^{\rm blk}|
=\max(B_1,B_2)
\ge\frac B2,
}
\tag{BA.11}
\]

\[
\boxed{
\sum_{e\in M_{\rm up}^{\rm blk}}(D-|e|)
<t_D<h_*+D^{-1/3}.
}
\tag{BA.12}

This is the constant improvement missing from the gate-count argument: no parity
thinning is required after passing to maximal upper blocks.

## 3. Block-aware finite minimax

Fix a real threshold `s>1`.

If one component `C` of `I` contains at least `s` selected edges of `E_*`, the
componentwise two-normal cone theorem gives endpoint displacement `X_C` along its
appropriate normalized two-normal axis `U_C` with

\[
\boxed{
X_C\cdot U_C\ge(b_*-o(1))s.
}
\tag{BA.13}
\]

If no component contains `s` selected edges, then

\[
c_I>\frac Es,
\]

and (BA.7) gives

\[
\boxed{
\beta(H)>\frac Es-B-1.
}
\tag{BA.14}
\]

At the same time (BA.11) gives an upper block-representative matching of size at least
`B/2`. For every `B>=0`,

\[
\boxed{
\max\left\{\frac Es-B,\frac B2\right\}
\ge\frac{E}{3s}.
}
\tag{BA.15}
\]

Indeed, if `B>=2E/(3s)` the second term is at least `E/(3s)`; otherwise the first
term is greater than `E/(3s)`.

Therefore for every `s>1`, `PAIR-REUSE` forces at least one of

\[
\boxed{
\beta(H)\ge\frac{E}{3s}-O(1),
}
\tag{BA.16}
\]

\[
\boxed{
X_C\cdot U_C\ge(b_*-o(1))s,
}
\tag{BA.17}
\]

or

\[
\boxed{
|M_{\rm up}^{\rm blk}|\ge\frac{E}{3s}-O(1),
\qquad
\sum_{e\in M_{\rm up}^{\rm blk}}(D-|e|)<h_*+D^{-1/3}.
}
\tag{BA.18}
\]

Choose

\[
s=\sqrt{\frac{E}{3b_*}}
\tag{BA.19}
\]

up to integer rounding. The two principal terms become

\[
\sqrt{\frac{b_*E}{3}}.
\]

Hence

\[
\boxed{
\text{PAIR-REUSE}\Longrightarrow
\max\{\beta(H),\ \text{compatible trunk drift},\ |M_{\rm up}^{\rm blk}|\}
\ge
\sqrt{\frac{b_*E}{3}}-o(\sqrt D).
}
\tag{BA.20}
\]

The upper-matching alternative retains the complete bounded aggregate diameter-defect
ledger (BA.12) and has at least the same number of distinct external child vertices.

## 4. Explicit square-root constant

Using (BA.2), define

\[
\boxed{
C_K^{\rm blk}:=\sqrt{\frac{\alpha_Kb_*}{6}}.
}
\tag{BA.21}
\]

Then `PAIR-REUSE` forces at least one of

1. **BLOCK-FACE:**
   \[
   \beta(H)\ge(C_K^{\rm blk}-o(1))\sqrt D;
   \]
2. **BLOCK-TRUNK:** one compatible common component has actual two-normal endpoint
   displacement at least
   \[
   (C_K^{\rm blk}-o(1))\sqrt D;
   \]
3. **BLOCK-UPPER:** there is a vertex-disjoint matching of old fully inactive
   outer-face source pairs with
   \[
   |M_{\rm up}^{\rm blk}|\ge(C_K^{\rm blk}-o(1))\sqrt D,
   \]
   \[
   \sum_{xy\in M_{\rm up}^{\rm blk}}(D-|x-y|)<h_*+o(1),
   \]
   and at least the same number of distinct children in `A\setminus F`.

Compared with the preceding gate-count coefficient

\[
C_K=\sqrt{\frac{\alpha_Kb_*}{10}},
\]

the new coefficient is larger by the exact factor

\[
\boxed{\sqrt{5/3}=1.2909944487358\ldots .}
\tag{BA.22}
\]

For `K=1`,

\[
\alpha_1=0.6652520156628998\ldots,
\]

and

\[
\boxed{
C_1^{\rm blk}
=0.0846090036211229\ldots .
}
\tag{BA.23}
\]

Thus the fixed-pair FREE route now forces `0.084609... sqrt(D)` bounded faces, actual
two-normal drift, or block-separated near-diameter pairs, unless the complementary
linear inverse-`D` matching branch already occurs.

## 5. Uniform near-diameter submatching and the supercritical regime

The BLOCK-UPPER alternative is stronger than a uniform inverse-square-root shell.
For every fixed `Lambda>1`, Markov applied to (BA.12) leaves a submatching of size

\[
\boxed{
\left((1-\Lambda^{-1})C_K^{\rm blk}-o(1)\right)\sqrt D
}
\tag{BA.24}
\]

whose every edge satisfies

\[
\boxed{
0<D-|x-y|
\le
\left(\frac{\Lambda h_*}{C_K^{\rm blk}}+o(1)\right)D^{-1/2}.
}
\tag{BA.25}
\]

For `K=1` and `Lambda=2`, this is

\[
\boxed{
(0.0423045018105614\ldots-o(1))\sqrt D
}
\tag{BA.26}
\]

edges with individual diameter deficit at most

\[
\boxed{
(7.91282180407404\ldots+o(1))D^{-1/2}.
}
\tag{BA.27}
\]

There is also a qualitative gain above the critical square-root scale. If the block
count on the larger-block ancestry satisfies

\[
|M_{\rm up}^{\rm blk}|/\sqrt D\to\infty,
\]

then half of its representatives have deficit `O(1/|M_{\rm up}^{\rm blk}|)`. Applying
the existing long-matching crossing extraction to that half gives a pairwise-properly-
crossing submatching of size

\[
\boxed{
\Omega\left(
\frac{|M_{\rm up}^{\rm blk}|^2}{D+|M_{\rm up}^{\rm blk}|}
\right)\to\infty.
}
\tag{BA.28}
\]

Thus only the genuine `Theta(sqrt(D))` block scale can keep the upper alternative from
already producing a growing crossing braid.

## 6. Frontier effect

Combining the fixed extreme FREE pair with block-aware forest accounting gives the
proof-only source-wide fork

```text
EXACT-BRAID
or
LINEAR-LOWER: Theta(D) inverse-D inactive lower matching
or, in PAIR-REUSE,
    BLOCK-FACE:  >= (C_K^blk-o(1)) sqrt(D) bounded faces
    BLOCK-TRUNK: >= (C_K^blk-o(1)) sqrt(D) actual two-normal drift
    BLOCK-UPPER: >= (C_K^blk-o(1)) sqrt(D) block-separated upper pairs
                 with O(1) total diameter deficit and as many external children.
```

This still does not close C-II. The improvement is not another free numerical tuning:
it identifies the correct combinatorial quantity in the Euler correction. A whole
consecutive upper block costs one lower-run separator and simultaneously supplies one
nonadjacent upper representative. The remaining critical obstruction is therefore a
`Theta(sqrt(D))` family of distinct external upper children tied to an `O(1)` aggregate
near-diameter defect, unless the planar lower network already pays square-root face or
spatial-drift currency.

**Disposition:** replaced upper-gate count by maximal upper-block count in the all-run
forest identity, selected one first upper edge per block without parity loss, and
re-optimized the finite boundary/forest minimax. C-II and Level I remain open; no
canonical theorem-state authority is changed.
