> Generated reading edition · [exact source](../../research/target_c_high_t_full_nested_opposite_terminal_rail_t18687_2026-09-17.md) · source SHA-256 `ac80d1b2da742b9181d88a41af7bf2e7209f553888562e947c9cefcbfbf78eb6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "4e6d2da379dcd1d10f1339efa3858d4063e2a927", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_full_nested_opposite_terminal_rail_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "dc1854678c8ac6805fb3842350f563d114f199ee4a578db17b34c1f586f0cdfb"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — same-host exclusion turns the full blocker family into a nested rail

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** any positive-density one-bar obstruction family on one side of the common high-`t` routing hub through `t=(q-k)/D<=1.8687`  
**Dependencies:** same-host diameter exclusion; physical-piece boundary decomposition; convex diameter-thrackle order; one-sided common-hub interval support; unconditional exact-antipodal/strong-TB1 blocker fork  
**Certificate:** `research/verify_target_c_high_t_full_nested_opposite_terminal_rail_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The same-host exclusion does more than improve the three-piece pigeonhole constant. Once one birth host side is fixed, deleting the now-impossible same-host partner piece leaves a **single contiguous hubward boundary segment**:

$$
T_m\cup Q^{\rm opp},
$$

where `Q^opp` is the hubward part of the opposite physical host arc.

In the boundary orientation transported from increasing birth-interface order by the diameter-thrackle partner map, the path-region labels on this whole remaining segment are weakly decreasing:

$$
m,m,\ldots,m,m-1,m-2,\ldots,k.
$$

Therefore every selected bar in the fixed-birth-side family, without any second pigeonhole, has a support end `b_i` that is nonincreasing with its birth interface `i`. Since the support starts increase strictly, **all supports are strictly nested**.

This removes the support staircase from the high-`t` physical frontier. It also raises the unconditional nested-rail density from the previous physical-piece floor `s_0/6` to `s_0/2`.

---

## Theorem FN — full fixed-birth-side nesting

Let `Z_D` be a family of nonhub interfaces on one fixed side of the common routing hub, with one selected actual switching diameter bar `h_i in X_i` per interface and

$$
|Z_D|>zD-o(D),
\qquad z>0.
\tag{FN.1}
$$

Assume for notation that the selected interfaces are pre-hub, so `i<k`. After fixing one of the two physical birth host sides, there is a subfamily

$$
Z_D^\sigma\subset Z_D,
\qquad
|Z_D^\sigma|>{z\over2}D-o(D),
\tag{FN.2}
$$

whose birth endpoints are distinct and lie in increasing interface order on one fixed host arc.

For all sufficiently large `D`, write the selected bars in increasing interface order

$$
i_1<i_2<\cdots<i_M<k,
$$

and let the partner endpoint of the `s`-th bar lie in path region `R_{b_s}`. Then

$$
\boxed{
b_1\ge b_2\ge\cdots\ge b_M\ge k.}
\tag{FN.3}
$$

Consequently the exact selected-cut support intervals

$$
I_s=\{i_s+1,\ldots,b_s\}
\tag{FN.4}
$$

satisfy

$$
\boxed{
I_1\supsetneq I_2\supsetneq\cdots\supsetneq I_M.
}
\tag{FN.5}
$$

Every partner endpoint lies either on the opposite physical host arc or on the far terminal piece `T_m`. No selected bar has both endpoints on the birth host arc.

---

## 1. Boundary orientation after fixing the birth side

The proper O--O crosscuts `tau_1,...,tau_m` connect the same two disjoint host arcs and are pairwise noncrossing. Their terminal endpoints therefore occur in opposite cyclic orders on the two host arcs.

Fix one physical birth host `A`. Reverse the ambient cyclic orientation if necessary so the pre-hub layer subarcs on `A` occur in increasing interface order:

$$
C_{i_1}^A<C_{i_2}^A<\cdots<C_{i_M}^A.
\tag{FN.6}
$$

Let `B` be the opposite host arc. Because the crosscut endpoint orders on `A` and `B` are opposite, the hubward region labels on the relevant part of `B` run in the reverse path order when read in the same ambient cyclic orientation. At the far end sits the terminal boundary piece `T_m`, all of whose points belong to `R_m`.

Thus, starting at `T_m` and continuing along the hubward part of `B` in the orientation compatible with (FN.6), the region-label word is weakly decreasing:

$$
\boxed{
\underbrace{m,\ldots,m}_{T_m},
\ m-1,m-2,\ldots,k.
}
\tag{FN.7}
$$

Repeated labels inside one region and repeated partner vertices are allowed. The only property needed below is weak decrease.

The same statement holds with `A,B` interchanged. It is a topological property of the ordered crosscut rectangle, not of the exact-antipodal mechanism.

---

## 2. Same-host exclusion leaves exactly the monotone segment

By the same-host diameter-exclusion theorem, for sufficiently large `D` an actual diameter edge cannot have both endpoints on `A`.

Every selected support crosses the common hub cut. Hence its partner lies on the complementary hubward shore

$$
Q=Q^\uparrow\cup T_m\cup Q^\downarrow.
$$

Of the two host pieces `Q^uparrow,Q^downarrow`, exactly one belongs to `A` and exactly one belongs to `B`. The piece on `A` is now impossible. Therefore every retained partner lies in

$$
\boxed{T_m\cup Q^B,}
\tag{FN.8}
$$

the contiguous opposite-host-plus-terminal segment whose label order is (FN.7).

No partner-side pigeonhole is required.

---

## 3. Diameter-thrackle order forces decreasing support ends

Birth endpoints at distinct interface tags are distinct because they occupy occurrence-disjoint layer subarcs. Consider two selected bars

$$
e_s=x_sy_s,
\qquad
e_t=x_ty_t,
\qquad s<t.
$$

If `y_s=y_t`, their partner region labels tie.

If `y_s!=y_t`, the two actual diameter bars are vertex-disjoint. Diameter edges of a convex source form a geometric thrackle, so the two chords cross. For chords joining complementary boundary intervals, crossing is equivalent to preserving the ambient cyclic endpoint order from the birth shore to the partner shore. Hence the partner map is weakly order-preserving, with shared partner vertices represented as ties.

By (FN.6), increasing interface order is increasing birth-boundary order. The partner endpoints therefore occur weakly forward in the same boundary orientation on the segment (FN.8). But its region-label word is weakly decreasing by (FN.7). Thus

$$
b_1\ge b_2\ge\cdots\ge b_M,
$$

which proves (FN.3).

Since `i_s` increases strictly while `b_s` does not increase,

$$
\{i_{s+1}+1,\ldots,b_{s+1}\}
\subsetneq
\{i_s+1,\ldots,b_s\},
$$

proving the strict nesting (FN.5), including the case of partner collisions or constant death tags.

---

## 4. Unconditional high-`t` consequence

The corrected exact-antipodal/strong-TB1 fork supplies a winning one-bar mechanism on one hub side with density

$$
s_0={791\over320{,}000{,}000}.
\tag{FN.9}
$$

Apply Theorem FN with `z=s_0`. The only loss is the initial choice of birth host side. Therefore the unconditional high-`t` obstruction contains a strictly nested support rail of size

$$
\boxed{
M>
{s_0\over2}D-o(D)
=
{791\over640{,}000{,}000}D-o(D).
}
\tag{FN.10}
$$

Numerically,

$$
\boxed{
{s_0\over2}=1.2359375\times10^{-6}.
}
\tag{FN.11}
$$

Every rail bar runs from one fixed birth host side into the opposite-host-plus-terminal segment. The support staircase is no longer a surviving alternative.

If the winning mechanism is strong-TB1, every retained rail bar keeps its fixed order-`D` first-derivative blocking margin. If the winning mechanism is exact-antipodal, every retained birth interface still has its second force-pair bar and exact positive two-ray reaction certificate.

---

## 5. Endpoint-disjoint nested crossing extraction

The rail births are distinct. Partner collisions are the only endpoint collisions. Using

$$
\Delta(H_D)
\le
(4\,3^{1/8}+o(1))D^{3/4},
\tag{FN.12}
$$

a greedy partner-vertex thinning gives an endpoint-disjoint nested subrail with

$$
\boxed{
>
\left(
{s_0\over8\,3^{1/8}}-o(1)
\right)D^{1/4}.
}
\tag{FN.13}
$$

The numerical coefficient is

$$
\boxed{2.6933721266\times10^{-7}.}
\tag{FN.14}
$$

All retained bars are vertex-disjoint actual diameter edges and therefore cross pairwise.

This is a factor-three improvement over the earlier endpoint-disjoint coefficient attached to the `s_0/6` physical-piece normal form.

---

## 6. If a single physical destination is needed

The full rail in (FN.10) may use both the opposite host arc and `T_m`. Partitioning it between those two physical destinations gives, if needed, one of

$$
\boxed{
\text{opposite-host nested rail}
\quad\text{or}\quad
\text{far-terminal nested rail}
}
\tag{FN.15}
$$

with size

$$
\boxed{
>{s_0\over4}D-o(D)
={791\over1{,}280{,}000{,}000}D-o(D).
}
\tag{FN.16}
$$

Thus the earlier physical trichotomy has collapsed to a nested two-destination dichotomy. In particular, the opposite-host staircase is not a genuine survivor once same-host diameter edges are removed and the actual crosscut orientation is retained.

---

## 7. Deep exact-force branch

The parameterized deep exact-force theorem already proves a full nested lane of density

$$
\lambda=c_0-6\rho-\eta-2\delta.
\tag{FN.17}
$$

The present theorem supplies its missing physical localization: every bar in that lane ends either on the opposite host arc or on `T_m`; none ends on its birth host arc.

For the current ninety-percent choice

$$
\lambda=5.085\times10^{-6},
$$

the full physically localized nested rail therefore still has density `5.085e-6`, with no physical-piece loss. If one insists on one physical destination, one of the opposite-host or terminal subrails has density at least

$$
\boxed{2.5425\times10^{-6}.}
\tag{FN.18}
$$

The existing endpoint-disjoint coefficient for the full deep nested rail remains

$$
{\lambda\over4\,3^{1/8}}
\approx1.10813024638\times10^{-6},
\tag{FN.19}
$$

and the one-destination coefficient is half of this.

---

## 8. Frontier effect

The unconditional high-`t` obstruction is no longer merely an unordered positive-density blocker population with a three-way physical support form. After one birth-side choice it has a single global normal form:

```text
Theta(D) actual diameter bars
+ distinct ordered births on one fixed host arc
+ partners only on opposite host or T_m
+ weakly decreasing death tags
+ strictly nested selected-cut supports
+ exact common routing hub.
```

This holds whether the winning local mechanism is exact-antipodal or strong-TB1. The next closing argument can therefore work with a **linear nested rail unconditionally**, rather than branching first on staircase versus nesting. The remaining physical split is only whether a linear share of this rail ends on the opposite host arc or on `T_m`.

No C-II or Level-I closure is claimed.

**Disposition:** same-host exclusion plus oriented crosscut topology forces the entire fixed-birth-side blocker family into one strictly nested opposite-or-terminal rail, raising the unconditional nested density to `s_0/2`. C-II and Level I remain open.
