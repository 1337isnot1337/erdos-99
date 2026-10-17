> Generated reading edition · [exact source](../../../docs/reports/target_c_one_vacancy_side_pin_restoration_slot07_2026-10-10.md) · source SHA-256 `81fd50d508489c9454379be11eeb01e7efd4ffdb01ec7c1921a4150e929e755f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2755DC266ACB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: one vacancy releases a coherent row and selected side pins

**Worker slot:** 07. **Date:** 2026-10-10.

**Base:** main `ab6dd3336f9f8d440f2bada76edb32153391cddc`, theorem state `2026-10-10.audit.234`. This continues branch `research/sol61-slot07-20261010-stress-transversal` after `a8916cfc`.

**Classification:** proved candidate awaiting independent audit; conditional stress-transversal corollary; finite confinement regression. No canonical promotion or Level I resolution.

## 1. Closure chain and new bridge

```text
actual coherent one-row strip + one literal end vacancy
  -> finite interior-row strictification with the whole wall fixed
  -> simultaneous inward release of selected side-row pins
  -> every moved label has strict lower and upper slack against the full source
  -> if the released set meets every normalized stress, strict diameter descent
     after deleting just one label, regardless of the size of that released set.
```

This compresses a potentially large virtual stress-transversal deletion to one actual population deficit in this geometry. It does not restore the last label. In the smallest three-label release cell, an exact capacity argument below shows that one deficit is sharp while the other five guards stay fixed and targets stay in the old hexagon.

The main new source ingredient is the inward-normal lemma. It checks all actual exterior unit contacts of each released pin. Inactive lower pairs are then covered by a finite source-dependent margin. Hull containment checks all upper pairs, including newly active ones. No isolate is discarded.

## 2. Source hypotheses and endpoint theorem

Let `k>=2`, let `u,n` be perpendicular unit vectors, and let

```text
v=c u+s n,  0<=c<1/2,  s=sqrt(1-c^2).
P={j u: 0<=j<=k-1},
W={-u,k u} union {j u+v,j u-v: 0<=j<=k-1},
F=conv(W).
```

Assume a finite unit-separated actual source `A` contains `P union W`. Every other source label is arbitrary. Let `S` be any subset of the `2k` side-row pins `j u+v,j u-v`; keep the two end guards and every label outside `P union S` fixed.

**Theorem P (proved candidate).** Delete only the source label at `(k-1)u`. There is a continuous finite motion of every other retained label such that:

- every distance between retained distinct labels stays at least one;
- diameter never exceeds `D=diam(A)`;
- all moved labels, namely the `k-1` retained interior-row labels and the pins in `S`, have strict separation from every other retained label at the endpoint;
- every endpoint pair involving a moved label is strictly below `D`;
- all other source labels, including all original contact isolates, remain at their original coordinates.

Thus `k+|S|` potentially stress-bearing labels are replaced by `k+|S|-1` strictly released labels using one actual vacancy. The source need not be globally optimal or triangle-free for this theorem.

The original source contains no further label inside `F`. Indeed its `4k` unit-basis triangle decomposition covers `F` by disks about the displayed old sites of radius `sqrt((1+c)/2)<1`; an additional label would violate unit separation. Every wall side has length at most `sqrt(2+2c)<sqrt(3)`. The weighted wall-exit identity therefore separates any weakly wall-clear interior point from every original exterior label by at least `sqrt(2-2c)>1`. Both statements are proved in the companion strip report, Section 2, and are internal candidate lemmas submitted with this proof.

## 3. Inward-normal lemma for an actual side pin

**Lemma N (proved candidate).** Suppose unit vectors `a,b` make an angle `theta in (pi/3,2*pi/3)`, and an actual unit-separated source contains

```text
p, p-a, p+b, p+b+a.
```

Put `z=p+b`, and choose the unit normal `n_b` perpendicular to `a` with `b dot n_b>0`. If an original source label `y!=p` has `|y-z|=1`, then

```text
(y-z) dot n_b>=0.
```

Consequently moving `z` a positive distance in direction `-n_b` strictly opens every such unit pair. The sole exceptional lower unit contact is with `p`, whose replacement must be paid separately.

### Proof

Translate `p=0`, take `a=(1,0)`, `b=(cos(theta),sin(theta))`, and write the unit vector `w=y-z`. Source separation from `p`, `p-a`, and `z+a` gives

```text
b dot w >= -1/2,
(a+b) dot w >= -(1+cos(theta)),
a dot w <= 1/2.
```

The inequalities involving a coincident source label are unnecessary: if `y=p-a` then `|y-z|=|a+b|>1`, and if `y=z+a` then `w=a` has zero normal component. Thus every nonexceptional unit neighbor satisfies the displayed inequalities, or is already handled directly.

Suppose the argument `psi` of `w` lies in `(pi,2*pi)`. The last inequality restricts it to `(pi,5*pi/3]`. Since `a+b` has argument `theta/2` and length `2cos(theta/2)`, the middle inequality excludes `(pi,pi+theta)`; hence `psi>=pi+theta`. The first inequality then forces `psi>=theta+4*pi/3`, because `psi-theta` is in `[pi,2*pi)` and must have cosine at least `-1/2`. But `theta>pi/3` makes this greater than `5*pi/3`, a contradiction. Therefore `w` has nonnegative normal component.

For a depth `t>0`, the new squared distance is exactly

```text
|y-(z-t n_b)|^2=1+2t(w dot n_b)+t^2>1.
```

The lemma needs neither KKT stress nor triangle-freeness.

### Application to every selected pin

For a top pin `z=j u+v` with `j<=k-2`, use `p=j u`, `a=u`, `b=v`: the required opposite interior neighbor `p-a` is an old row point or the left end guard, and `z+a` is the next top-row pin. At the last top pin use `a=-u`; the right end guard supplies `p-a`. Both angles remain strictly between `pi/3` and `2*pi/3`, and `n_b=n`.

For bottom pins use `b=-v`, and the same right/left choice of `a`; now `n_b=-n`. Hence top pins move vertically downward and bottom pins vertically upward. All original unit contacts except their own vertical row contact open strictly. This includes every possible exterior unit neighbor, not just modeled lattice points.

## 4. Explicit three-stage finite motion

Let `w=s u-c n`, so `v dot w=0` and `u dot w=s>0`. Choose `delta=(1-2c)/100`.

### Stage I: translate the punctured row

For `0<=j<=k-2`, move `j u` to `j u+t delta w`, `0<=t<=1`, with the whole wall and every exterior label fixed.

Interior-row mutual distances remain their old integer multiples of one. Distances to `j u+v,j u-v` have squared value `1+t^2 delta^2`. Every other side-row guard starts at distance at least `d_min=sqrt(2-2c)>1`, and

```text
d_min-1=(1-2c)/(d_min+1)>(1-2c)/3>delta.
```

Thus those nonunit pairs stay strictly above one. The left end pair has squared distance `1+2t delta s+t^2 delta^2`; all other end-guard pairs start at least two away. Axial displacement coefficients are `t delta/s,-t c delta/s`, whose absolute sum is below `1/50`, so all moving row points stay strictly inside `F`.

Weak clearance from the full original wall, including every pin later selected for release, supplies exterior separation through the wall-exit lemma. All positions remain in the original source hull, so no upper pair exceeds `D`.

### Stage II: separate the row internally

Let `z_j=j u+delta w`. Their guard clearance and their distance to the boundary of `F` have positive minima. Choose a positive `epsilon` less than half of both minima, and move

```text
z_j -> z_j+t(-1)^j epsilon n,  0<=t<=1.
```

Adjacent row points have squared distance `1+4t^2 epsilon^2`; nonadjacent points have horizontal distance at least two. The finite positive guard margin keeps every row-wall distance above one throughout. The wall-exit shield covers every exterior label. The endpoint row packet `Q` is strictly separated internally and from every original wall vertex, including pins in `S`.

### Stage III: move all selected pins inward together

Assign distinct positive depths `d_z in [1,2]` to pins in each side row. Put `n_z=n` for top pins and `n_z=-n` for bottom pins. Move

```text
z -> z-t d_z n_z,  0<=t<=tau.
```

Choose `tau>0` sufficiently small as follows. The packet `Q` has positive clearance from every original pin in `S`. Every original nonunit pair involving `S` and a fixed label, or two labels in `S`, has a finite positive margin. Select `tau` smaller than one eighth of these margins and smaller than `s/100`; omit empty families. These bounds preserve all such lower pairs and keep every selected pin strictly inside `F` for `t>0`.

For an original unit pair between a pin and a fixed label, Lemma N gives exact strict opening; the exceptional old interior label is absent from its old coordinate and has already been replaced by a strictly clear packet site. For two selected pins, the only original unit pairs are adjacent pins in the same side row. Their squared distance is

```text
1+t^2(d_z-d_{z'})^2,
```

which is strictly above one for `t>0`. Opposite-row pin pairs are nonunit and covered by the finite margin. All packet-pin pairs remain strict by the first margin. Therefore every pair involving a moved label is strictly above one at the endpoint, and every lower pair remains feasible along the whole stage.

The inward pin displacements lie strictly inside `F`: for a top pin their axial coefficients are `a=j+c t d_z/s`, `b=1-t d_z/s`, and for a bottom pin `a=j-c t d_z/s`, `b=-1+t d_z/s`. Substituting in `|b|<1` and `-1<a+b,a-b<k` proves the claimed containment for the chosen small depth. All endpoint moved sites are consequently interior points of `conv(A)`. Strict convexity gives distance strictly below `D` from every point in that hull, including other moved sites. This proves every upper pair and completes Theorem P.

No step requires a uniform source margin. Finiteness supplies the positive inactive-pair minima after the exact unit-pair cases have been proved.

## 5. Stress-transversal compression

**Corollary K (conditional source theorem).** Suppose `T=P union S` meets the positive support of every normalized nonnegative source KKT stress: equivalently, no such stress is supported entirely on labels in `A\T`. Then deleting the single label `(k-1)u` permits a finite retained-source motion with endpoint diameter strictly below `D`.

Apply Theorem P. At its endpoint every moved label is contact-isolated and has no diameter pair at distance `D`. All old fixed-label contact and diameter rows are unchanged, and no new `D` pair involves a moved label. Any normalized endpoint KKT stress would therefore be supported on the fixed labels. Extending it by zero on all original rows incident to `T` gives a normalized source stress supported away from `T`, contrary to the hypothesis. If endpoint diameter already lies below `D`, the conclusion is immediate. Otherwise canonical `C-FINITE-KKT-STRICT-MOTION-ALTERNATIVE` (Audit.87) gives one sufficiently small strict step, with every inactive retained-source pair checked by its finite margin.

The support hypothesis is on every normalized stress, including proper support faces. Positivity of one relative-interior stress does not imply it. This is a compression from a virtual deletion of `|T|` labels to one actual vacancy, not a same-cardinality competitor.

## 6. Sharp three-label confinement regression

For `k=2`, free the two interior sites `0,u` and the side pin `v`, retaining the other five guards `-u,-v,u-v,2u,u+v`. Confine all targets to the old hexagon `F`.

**Theorem C3 (proved candidate / finite regression).** The unique weakly guarded unit-separated three-point filling is `{0,u,v}`. Strict capacity relative to the five guards is exactly two. Thus even freeing this side pin leaves one population deficit if all three free labels must be strictly released in that compartment.

Let `H_0=conv{-u,-v,u,v}` and `H_1=conv{0,u-v,2u,u+v}`. Their union covers `F` apart from two triangles: the upper triangle with vertices `v,u+v,(u+v)/2`, and the lower triangle with vertices `-v,u-v,(u-v)/2`. Each is inside a fixed guard's unit disk, except for a vertex already in `H_0 union H_1`. Use guard `u+v` for the upper triangle and `-v` for the lower one; the midpoint distance is `sqrt((1+c)/2)<1`. Hence every clear point lies in `H_0 union H_1`.

In `H_1`, the co-circular free-vertex identity about center `u` puts every clear point in the open diameter disk of `[0,u]`, apart from `0,u`. In `H_0`, only `u,v` are free unit-circle vertices about zero. Write their barycentric weights as `lambda,eta`, let `Lambda=lambda+eta`, and use the two fixed guards `-u,-v`. The weighted identity gives

```text
(1+Lambda)|x|^2 <= 2x dot (lambda u+eta v).
```

For `0<Lambda<1` and `x!=0`, at least one of `x dot u,x dot v` is strictly greater than `|x|^2`. Thus `x` lies strictly inside one of the two diameter disks of `[0,u]` or `[0,v]`. For `Lambda=0`, the point is zero. For `Lambda=1`, the point lies on the chord `[u,v]`; each nonendpoint chord point has distance strictly below one from the retained guard `u+v`, since

```text
|(1-t)u+t v-(u+v)|^2=1-2t(1-t)(1-c)<1.
```

Therefore the whole clear set lies in those two open diameter disks, apart from `0,u,v`. Assign each nonendpoint point to a disk whose interior contains it, assign `u,v` to their own disks, and assign zero arbitrarily. In a three-point subset, two points are assigned to one closed disk. Neither can be an interior point, since its distance from every point of that closed disk is below one. Thus the assigned pair consists of `0,u` or `0,v`. Once zero is present, any point in either open disk is less than one from it. Hence the only three-point filling is `{0,u,v}`. None of those three points is strictly clear from the five guards, so strict capacity is at most two. Theorem P with `k=2,S={v}` constructs two strict sites, proving equality.

This regression needs no global optimality. Its actual-source upper capacity survives the addition of arbitrary exterior constraints; strict attainment against the full exterior source is established by the inward-normal construction, not assumed from the finite picture.

## 7. Scope and next obligation

The finite motion retains all source labels other than the one explicit vacancy. It handles arbitrary exterior labels, all contact isolates, every unit lower pair, every old diameter pair, and every potentially newly active upper pair. The row and pin hypotheses are actual geometric containment hypotheses. Neither a lattice competitor nor artificial pins supply them.

The theorem does not extract such a strip from every canonical survivor, establish its stress-support hypothesis, or restore the last label. The exact next obligation is a source-realized capacity payment for that remaining vacancy after this finite release, or a theorem extracting strips whose release admits a different equal-cardinality endpoint outside the blocked fixed hexagon. C-II and Level I remain open.

The numerical discovery check optimized the three-site five-guard cell at `c=0,1/5,2/5` and found only the old point set up to permutation and numerical error. That did not establish an upper capacity bound; Theorem C3's analytic proof does. Exact verification files are recorded separately with their finite scope.

## 8. Exact certificates and a nontrivial surviving-stress diagnostic

Run

```text
python3 research/verify_target_c_one_vacancy_side_pin_release_slot07_2026_10_10.py
```

The script deliberately reruns the companion exact verifier, then checks 68 additional source/endpoint fixtures at eight rational/algebraic angles, lengths `k=2,5`, and one-pin/all-pin releases. The cases include off-lattice exterior unit neighbors, horizontal exterior unit neighbors, 32 retained contact-isolate instances, and 16 sources whose first top pin is an actual diameter endpoint. All arithmetic is rational or `Q(sqrt(15))`; stage amplitudes are selected by exact rational halving.

Two square sources give a diagnostic that is not vacuous. Add the four missing corners to the strip to form the complete square grid `{-1,...,k} times {-1,0,1}`, with `k=2` or `5`. Its two opposite-corner diameter rows have squared length `(k+1)^2+4`. There is a normalized equilibrium stress with `beta=1/2` on each diagonal, contact weight `(k+1)/2` on the top/bottom boundary chains, weight one on the two left/right vertical chains, and zero contact weight on every interior edge. Direct force balance verifies it. Its contact mass is exactly the squared diameter.

Deleting the interior point `(k-1,0)` removes only zero-weight rows, so this normalized stress survives the literal vacancy. Thus there is no strict first-order direction opening all remaining contacts and shortening all old diameter pairs at the initial punctured source. The finite three-stage construction nevertheless releases the row and top pin and then admits strict descent.

For completeness, every normalized stress of this full square chart is the displayed one. At each unloaded noncorner boundary point, equilibrium forces the contact weight normal to that side to vanish. Interior straight-cross equilibrium propagates those zero row/column weights. The four surviving boundary chains have constant weights; the two left-corner balances force their diagonal weights equal, and normalization gives `beta=1/2`. The exact verifier independently checks that the complete contact/diameter row matrix has left nullity one, verifies the displayed stress, and verifies that it survives the literal deletion and meets the released set.

At the released endpoint the active row matrix has full row rank. The verifier solves exactly for radial row values `+1` on all unit contacts and `-1` on all old-diameter pairs, then selects one positive rational step by halving until every retained pair is strictly above one and strictly below the old diameter. It records the velocity and step in the JSON certificate. This supplies four explicit strict-descent endpoints, not just a solver status or a first-order direction.

These two square sources are nonglobal: for the 12-point case a triangular-lattice competitor has squared diameter at most 12 rather than 13; for the 21-point case a square-grid competitor has squared diameter 32 rather than 40. The selected positive-contact core is only the boundary, with `2k+6` vertices and `2k+8` contact/diameter rows, below the canonical required mixed rank `4k+9`. Thus the diagnostic does not satisfy `C-ZRF` and is not a canonical C-II counterexample.

The finite counts and amplitudes are in `research/target_c_one_vacancy_side_pin_release_slot07_certificate_2026_10_10.json`. Path samples do not prove whole-segment feasibility, the general normal lemma, arbitrary-exterior safety, or canonical strip/transversal extraction. The analytic proof carries those steps. The stress and strict fourth steps are certified only for the stated finite square diagnostics.
