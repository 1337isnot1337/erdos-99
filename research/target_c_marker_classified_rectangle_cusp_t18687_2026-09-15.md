<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c51bd46b1d21a2ed84e0042a1751f1d41ec60548", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_marker_classified_rectangle_cusp_t18687_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7956e8dd8d693bd7c78a254dc41bcf7445e2acc128d9f5d95a027ae72ff454ab"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the high-`t` rectangle cusp is marker-classified and contains a clean transverse corridor

**Date:** 2026-09-15  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** high-`t` complete rectangle and joint-cusp theorem; phase-zero marker path/interval-isolation theorem; diameter-path Helly hub; stopped-train terminal decomposition  
**Certificates:** `research/verify_target_c_high_t_rectangle_joint_cusp_t18687.py`, `research/verify_target_c_marker_rectangle_cusp_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The merged high-`t` rectangle theorem supplies a consecutive O--O row block `A_*` of linear size and a macroscopic ordered common column family. The phase-zero marker theorem deletes only `o(D)` rows from the same shrinking dominant phase window. Restricting the joint-cusp average to interfaces whose two boundary rows survive that deletion costs only `o(D)` interfaces, so the parent finite-cusp constant is unchanged.

Thus the finite KKT cusp can be chosen on the **fixed-marker path** itself.

There are adjacent selected O--O rows

\[
\tau_0,\tau_1
\]

bounding one nonhub path region `R`, and a pairwise-noncrossing common column family

\[
B_0,
\qquad
|B_0|>0.0783D-o(D),
\tag{MC.1}
\]

such that all parent joint-cusp conclusions hold:

\[
\boxed{
N_R+L_R+D B_R+S_0+S_1<1{,}109{,}000,
}
\tag{MC.2}
\]

\[
N_R,L_R\le1{,}108{,}999,
\qquad
B_R<{1{,}109{,}000\over D},
\tag{MC.3}
\]

\[
d_{\mathbb{RP}^1}(\nu_0,\nu_1)
<{7.08\times10^6\over D}+o(D^{-1}),
\tag{MC.4}
\]

and every `b in B_0` crosses both rows in one common order with

\[
0<\theta(\tau_r,b)-{\pi\over3}
<{1.416\times10^7\over D}+o(D^{-1})
\qquad(r=0,1).
\tag{MC.5}
\]

The new marker information gives the exact local blocker dichotomy:

\[
\boxed{
\begin{array}{ll}
\nu_0\ne\nu_1
&\Longrightarrow\text{a minimal translation certificate is strict-interior TB1};\\[2mm]
\nu_0=\nu_1
&\Longrightarrow\text{TB1 is impossible and minimal TB2 has opposite transverse signs.}
\end{array}}
\tag{MC.6}
\]

In the second case there is no phase-parallel switching diameter. In both cases the zero rigid translation of `R` is locally isolated for the fixed finite source.

Because `R` is nonhub, every actual diameter edge with an endpoint in `R` is a switching edge at this interface. Hence `R` contains at most `N_R` distinct actual-diameter endpoints. Combining this with the terminal bound and the ordered common columns gives a further geometric consequence: between the two rows there is a run of more than

\[
\boxed{3.5\times10^{-8}D-o(D)}
\tag{MC.7}

consecutive common-column slabs whose interior contains

- no endpoint of an actual diameter edge;
- no complete-stopped-train terminal face-side occurrence;
- no bounded nonquadrilateral contact face.

This is a defect-free **contact/routing corridor**, not a source-free corridor: contact-isolated source points are retained and are not controlled by (MC.7).

---

## 1. The rectangle survives phase-marker deletion

The complete-rectangle theorem starts with one shrinking dominant phase window and extracts a consecutive row block

\[
A_*=(\tau_1,\ldots,\tau_m),
\qquad
m>0.0000226D-o(D).
\tag{MC.8}
\]

Every row belongs to the same adaptively selected retained O--O family used by the coupled paired-remainder theorem.

Apply the phase-zero marker deletion to that same phase window. Its selected endpoint measure is a retained pair submeasure, so the two shrinking marker neighborhoods delete only `o(D)` pair weight and therefore only `o(D)` rows from the entire window. In particular they delete only `o(D)` rows from `A_*`.

Let `A_M` be the surviving rows of `A_*`. Then

\[
|A_M|>0.0000226D-o(D).
\tag{MC.9}
\]

An internal adjacent interface of the original consecutive block is **marker-good** if both of its boundary rows lie in `A_M`. One deleted row destroys at most two such interfaces. Therefore the number of marker-good interfaces is still

\[
>0.0000226D-o(D).
\tag{MC.10}
\]

Delete also the unique hub region and the `O(1)` end interfaces. The same density remains.

The oriented common-column family `B_+` from the rectangle theorem crossed every row of `A_*`, so it still crosses every marker-good boundary row. Its consistent oriented crossing branch is unchanged by deleting rows.

---

## 2. Restrict the parent joint-cusp average to marker-good interfaces

For an internal rectangle interface let

\[
J_i=N_i+L_i+D B_i+S_i+S_{i+1}
\]

with the notation of the parent joint-cusp theorem.

All terms are nonnegative. The parent proof gives the global restricted-block bound

\[
\sum_{i\in A_*}J_i
<\left(10T-2\pi+2+2C_{phase}\right)D+o(D).
\tag{MC.11}
\]

Discarding marker-bad interfaces can only decrease the left side. By (MC.10), the denominator in the averaging step is unchanged at first order. The same exact arithmetic certificate therefore gives one marker-good nonhub interface satisfying

\[
J_i<1{,}109{,}000.
\]

This is (MC.2). Every scalar consequence (MC.3)--(MC.5) from the parent theorem applies to the same pair without modification.

Because the two rows are both marker survivors and were adjacent in the original path, the region between them is also one region of the cleaned fixed-marker path. Thus the marker theorem applies directly rather than through a coarsened block.

---

## 3. Marker geometry classifies the same finite cusp

Choose coherent oriented row directions `nu_0,nu_1` by putting the fixed marker `theta_+` on the same named shore. Orient the two physical strip contact vectors from the fixed exterior into `R`:

\[
a=\nu_0,
\qquad
b=-\nu_1.
\tag{MC.12}
\]

The loaded-hull boundary pieces belonging to `R` lie between consecutive surviving marker-path terminals. Hence their oriented normal angles avoid the two deleted marker neighborhoods.

Every switching diameter has exactly one endpoint in `R`; orient its length-`D` vector from the outside endpoint into `R` and call it `n_h`. Uniform Type-II diameter-normal convergence identifies `n_h/D`, up to `o(\rho_D)`, with the outward loaded-hull normal at its endpoint in `R`.

The phase-zero blocker theorem now applies verbatim.

### Distinct row directions

If `nu_0!=nu_1`, a minimal TB2 pair would force each blocker direction to lie projectively within the shrinking row phase gap of `nu_0`. Its endpoint normal would then lie in a deleted marker neighborhood, impossible. Hence TB1 occurs. A TB1 vector on a boundary ray is excluded by the same argument, so

\[
\boxed{
n_h\in\operatorname{int}\operatorname{cone}\{a,b\}.
}
\tag{MC.13}
\]

This strict interiority gives a positive sourcewise tangent margin and locally isolates the zero finite layer translation.

### Equal row directions

If `nu_0=nu_1=nu`, any switching diameter with

\[
n_h\cdot J\nu=0
\]

would be phase-parallel and therefore marker-forbidden. A one-bar certificate for the two antipodal opening directions would require exactly such zero transverse projection. Thus TB1 is impossible and a minimal certificate is exactly two bars with

\[
\boxed{
(n_{h_+}\cdot J\nu)(n_{h_-}\cdot J\nu)<0.
}
\tag{MC.14}
\]

Again the strict signs locally isolate the zero finite layer translation.

This proves (MC.6).

---

## 4. Every actual diameter endpoint in the nonhub region is counted by `N_R`

The diameter-path Helly theorem says every actual diameter support interval contains one common hub region `R_*`. The selected region `R` is nonhub.

Take an actual diameter edge with an endpoint in `R`. Its other endpoint cannot also lie in `R`: otherwise its path support would be the singleton `{R}`, which would not contain `R_*`. Thus the diameter support interval has `R` as one endpoint region and extends from `R` toward the hub.

Consequently its cut-incidence row starts or stops exactly at the interface between `tau_0` and `tau_1`. It is one of the switching rows counted by `N_R`.

Therefore

\[
\boxed{
\#\{\text{distinct actual-diameter endpoints in }R\}
\le N_R.
}
\tag{MC.15}
\]

This is stronger than merely bounding the number of block-crossing diameter bars: in a nonhub single path region there are no hidden actual-diameter endpoints belonging to an internally supported diameter edge.

---

## 5. The common columns cut the region into ordered slabs

The columns in `B_0` are pairwise noncrossing and every one crosses both boundary rows exactly once. Restrict each column midpoint path to the segment between those two crossing rhombi. These are pairwise-disjoint proper crosscuts of the topological strip region `R`.

By the common-order theorem they occur in one order along both boundary rows. Thus if

\[
M:=|B_0|,
\]

they cut `R` into `M+1` slabs, with `M-1` internal slabs between consecutive common columns.

Call the following objects **finite defects** in `R`:

1. distinct actual-diameter endpoints;
2. complete-stopped-train terminal face-side occurrences assigned to `R`.

By (MC.2) and (MC.15), their total number is at most

\[
N_R+L_R\le1{,}108{,}999.
\tag{MC.16}
\]

Assign a defect in the interior of one slab to that slab. If a defect lies on a common-column segment, mark both adjacent internal slabs; at the two extreme columns mark the one adjacent internal slab. Hence one defect marks at most two internal slabs.

The number of marked internal slabs is therefore at most

\[
2(1{,}108{,}999)=2{,}217{,}998.
\tag{MC.17}
\]

Deleting those marked slabs leaves at most `2,217,999` consecutive runs of unmarked internal slabs.

Since

\[
M>0.0783D-o(D),
\]

pigeonhole gives one unmarked run of length

\[
>{0.0783\over2{,}217{,}999}D-o(D).
\]

The companion exact checker verifies

\[
{0.0783\over2{,}217{,}999}>3.5\times10^{-8},
\]

proving (MC.7).

---

## 6. An unmarked run has no bounded exceptional contact face

Every bounded nonquadrilateral face is a terminal face for each stopped train edge arriving at it; in particular it contributes terminal face-side occurrences to `L_R`. A through-going common column cannot pass through such a face, since a stopped train terminates there rather than traversing it.

Therefore a bounded nonquadrilateral face lies inside one column slab (or meets a slab boundary only at ordinary contact boundary data), and any slab containing such a face contains a terminal occurrence. An unmarked slab contains none.

Hence the interior of the clean run contains no bounded nonquadrilateral contact face. In the stopped-train contact complex its bounded faces are strict rhombi.

The same run contains no actual-diameter endpoint by construction. This proves the three bullets following (MC.7).

Contact-isolated source points are a different issue. They do not appear in the stopped-train terminal or contact-face ledgers and are not bounded by ZR/ZF. They remain part of the full source. No claim that the corridor is empty of such points is made.

---

## 7. Frontier effect

The current high-`t` obstruction can now be placed in one source-level picture:

```text
fixed antipodal phase markers
+ one nonhub adjacent O-O row pair inside the complete high-t rectangle
+ >0.0783 D ordered common transverse columns
+ row-row and row-column phase errors O(1/D)
+ N,L <=1,108,999 and D B<1,109,000
+ every actual diameter endpoint in the region belongs to this finite switching set
+ strict-interior TB1 if the row phases differ exactly
  OR opposite-transverse TB2 if they agree exactly
+ the rigid region translation is locally isolated
+ a >3.5e-8 D run of transverse slabs with no diameter endpoint,
  no stopped-train terminal occurrence, and no bounded exceptional contact face.
```

The missing closure theorem is correspondingly precise. One must use the clean ordered rhombic corridor to build a full-source deformation that is not a rigid translation of the entire region, or prove that the finite TB1/TB2 diameter blocker cannot attach consistently to such a corridor. Contact-isolated source points must be handled explicitly in either route.

No such final deformation is claimed here.

**Disposition:** proved proof-only marker classification of the high-`t` rectangle cusp and a linear defect-free contact/routing corridor through `t<=1.8687`. C-II and Level I remain open.
