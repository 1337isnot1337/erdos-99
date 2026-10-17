> Generated reading edition · [exact source](../../../docs/reports/target_c_coherent_strip_exact_restoration_capacity_slot07_2026-10-10.md) · source SHA-256 `2af4a903a40411961bd2baf9afd107ca8e0d7ba47ed7ca118c15c80fa6116524`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CD03CC52BC3E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: exact restoration capacity of a coherent rhombic strip

**Worker:** 07. **Date:** 2026-10-10.

**Authority:** main `ab6dd3336f9f8d440f2bada76edb32153391cddc`; state `2026-10-10.audit.234`. Level I and C-II remain open.

**Classification:** proved candidate awaiting independent audit. This is an actual-source conditional exclusion of a fixed-wall restoration mechanism, with explicit reduced-population endpoints. It is not a canonical promotion.

## 1. Exact advancement

The attempted bridge was

```text
vacancy transport along a coherent train
  -> jointly relocate every interior label along the whole train
  -> restore the deleted label within the fixed guarded strip
  -> same-cardinality contact-count or diameter contradiction.
```

The third arrow is impossible under the stated fixed-guard and confinement hypotheses, for every strip length and every strict rhombic angle. This includes overlapping hop cells; it does not assume a disjoint bank. The strict capacity is exactly one below the old population, so the missing label must be paid outside the strip or by changing guards. The strongest positive result is an explicit strict endpoint of that deficient cardinality, with every arbitrary exterior source label retained and every upper pair checked.

The companion proved candidate [rhombic vacancy hop and two-site capacity](target_c_rhombic_vacancy_hop_and_two_site_capacity_slot07_2026-10-10.md), Theorem C, supplies an internal geometric lemma below. Its complete all-parameter proof is in Section 4 there. Both reports are submitted together for audit; that lemma is not used as a canonical premise.

## 2. Actual strip and full-source accounting

Let `k>=2` be an integer. Let `u,v` be unit vectors with `v=c u+s n`, `0<=c<1/2`, `s=sqrt(1-c^2)`, and `n` perpendicular to `u`. Reversing `v` covers the obtuse representative as well. Define

```text
P_k={j u: 0<=j<=k-1},
W_k={-u,k u} union {j u-v,j u+v: 0<=j<=k-1},
F_k=conv(W_k).
```

Assume a finite unit-separated actual source `A` contains `P_k union W_k`. All additional labels may have arbitrary coordinates. In axial coordinates `x=a u+b v`,

```text
F_k={|b|<=1, -1<=a+b<=k, -1<=a-b<=k}.
```

The wall uses consecutive unit row edges and four end edges of squared length `2-2c` or `2+2c`. Its largest edge is shorter than `sqrt(3)`.

Triangulate each of the two rectangles between consecutive interior sites and the corresponding upper/lower row into two triangles, and each end cap into two triangles. This gives `4k` triangles, each with two unit sides and third side of squared length `2-2c` or `2+2c`. Their enclosing circle radii are at most `R_0=sqrt((1+c)/2)<1`, as proved by the exact circle/barycentric identity in companion Section 2.1. Hence every point of `F_k` is within `R_0` of an original wall or interior site, and

```text
A intersect F_k=P_k union W_k.
```

There is no uncounted interior source label or contact isolate.

For an interior point at least one from every wall guard, and an arbitrary original label outside `F_k`, the weighted wall-exit identity gives separation at least `sqrt(2-2c)>1`. Explicitly, at an exit on a side `ab`, `z=(1-t)a+tb`,

```text
|w-z|^2=(1-t)|w-a|^2+t|w-b|^2-t(1-t)|a-b|^2
        >=1-(2+2c)/4
```

for both the interior and exterior point `w`; their lengths add along the segment. Vertex exits give separation at least two. No nonvertex source label lies on a wall side, whose length is below two. This accounts for every exterior label, including isolates.

Every replacement point in `F_k` remains in `conv(A)`, so every upper pair has length at most `D=diam(A)`. Interior row sites are nonextreme points of that hull and cannot support actual diameter pairs, by strict convexity. All original diameter pairs are consequently retained when only the row is replaced.

## 3. Exact weak and strict capacity

Let `E_k` be the points of `F_k` at distance at least one from every guard in `W_k`, and let `E_k^>` use strict distance greater than one.

**Theorem S (proved candidate).** For every integer `k>=2` and every `0<=c<1/2`:

1. the largest cardinality of a unit-separated subset of `E_k` is `k`;
2. its unique cardinality-`k` point set is `P_k`;
3. the largest cardinality of a unit-separated subset of `E_k^>` is `k-1`.

These statements permit arbitrary continuous coordinates and simultaneous replacements of all row labels.

### 3.1 Longitudinal confinement

Write `X=u dot x`, `Y=n dot x`. For `x in E_k` with `X<=0`, the radius-`R_0` cover can only use the interior site `0`: every `j u` with `j>=1` is farther than or equal to one, and wall guards are at least one away. Set `r=|x|<=R_0`.

For `r>0`, write `x=a v+b w`, with `w=s u-c n`. Clearance from `v,-v` gives `|a|<=r^2/2`; clearance from `-u` gives `X>=-r^2/2`. If `b<=0`, then

```text
X<=c r^2/2-s r sqrt(1-r^2/4)<-r^2/2,
```

since `r^2<3/4<2(1-c)`, a contradiction. Thus `b>0`. Concavity in `a` gives

```text
X>=-c r^2/2+s r sqrt(1-r^2/4)>0,
```

where positivity follows from `r^2<4s^2`. Hence `X<=0` forces `x=0`. The symmetry `x -> (k-1)u-x` gives the other end. Therefore

```text
E_k subset {0<=X<=k-1},
E_k intersect {X=0}={0},
E_k intersect {X=k-1}={(k-1)u}.
```

### 3.2 Local interval disks without fixed interior guards

Fix `j in {0,...,k-2}` and translate so that `j u=0`. For a point of `E_k` with `0<=X<=1`, we have `|Y|<=s`. It must also lie in the two-site hexagon with vertices `-u,-v,u-v,2u,u+v,v`.

Indeed, within the rectangle `0<=X<=1`, `|Y|<=s`, only its upper-left and lower-right corner triangles lie outside that hexagon. The upper-left triangle has vertices

```text
(0,s/(1+c)), (0,s), (c,s)=v.
```

All its points are strictly inside the unit disk about `v`: the largest vertex squared distance is `2c^2/(1+c)<1`. The lower-right triangle is its central reflection and lies in the disk about `u-v`. Neither can contain a guard-clear point.

The four actual row guards `-v,v,u-v,u+v` are retained. The additional two guards `-u,2u` used in companion Theorem C need not be retained: their clearance follows automatically from `0<=X<=1`, since their horizontal distances are at least one. Thus Theorem C applies without keeping any neighboring interior label fixed. It yields

```text
E_k intersect {j<=X<=j+1}
 subset B_open((j+1/2)u,1/2) union {j u,(j+1)u}.
```

Each open interval contains at most one unit-separated point. A point in that interval has distance strictly below one from both endpoint sites. On each integer plane `X=j`, the only clear point is `j u`.

### 3.3 Counting arbitrary mixed placements

Suppose a unit-separated subset chooses nonnode points in `r` open intervals. Those intervals are edges of the path on the `k` original sites. If `r>0`, let `b>=1` be the number of connected blocks of chosen edges. The chosen intervals have exactly `r+b` distinct endpoint nodes. None of those nodes may be selected, by the preceding disk bound. The total population is at most

```text
r+(k-r-b)=k-b<=k-1.
```

If no interval is chosen, every point is an original node and population is at most `k`, with equality only for all `P_k`. The old row is feasible. This proves weak capacity and its equality classification. A strictly guarded placement cannot select a node, so it has at most one point per open interval, hence at most `k-1`.

### 3.4 Explicit strict endpoint achieving k-1

Set `delta=(1-2c)/100>0` and

```text
z_j=j u+delta w,  0<=j<=k-2.
```

The guards `j u+v,j u-v` are at squared distance `1+delta^2`. Every other row guard is originally at distance at least `d_min=sqrt(2-2c)>1`, and `d_min-1>(1-2c)/3>delta`, so it remains strictly farther than one. The left end guard opens at the first site; every other end-guard distance starts at least two. All `z_j` are strictly inside `F_k`, with axial displacement coefficients `delta/s,-c delta/s` of absolute sum below `1/50`.

Let `rho>0` be the minimum guard clearance of these finitely many sites, and `mu>0` their minimum distance to the wall boundary. Choose `0<epsilon<min(rho,mu)/2` and set

```text
q_j=z_j+(-1)^j epsilon n.
```

Every guard remains strictly farther than one and every site stays inside `F_k`. Adjacent points have squared distance `1+4epsilon^2>1`; points two or more indices apart have horizontal distance at least two. This is a strict packet of size `k-1`.

The shield in Section 2 separates it from every other retained source label. Hull containment checks every upper pair, including potentially newly active pairs; all original diameter pairs remain fixed, so the new diameter is exactly `D`. Assigning the row labels other than one deleted label to the packet gives an actual `|A|-1` endpoint. No continuous integration from the old deleted-row placement is asserted for this packet.

## 4. Consequences and limits

Any unit-separated equal-cardinality replacement confined to the strip with its wall fixed must reproduce every old row coordinate, even if all interior labels are moved jointly and permuted. Such a replacement cannot reduce diameter or contact count. Transporting a vacancy along this entire coherent train supplies no refill capacity in the same fixed strip.

**Corollary R (conditional source theorem, strict preparation after transversal deletion).** Suppose a nonempty set `U subset P_k` kills every normalized source KKT stress when deleted. Keep the whole wall and every exterior label fixed. There is a unit-separated endpoint of cardinality `|A|-|U|` at diameter exactly `D` in which every remaining row label has strict separation from every other retained label. That endpoint also admits a finite strict diameter descent.

Take any `k-|U|` sites from the strict packet in Section 3.4. The full retained-source ledger proves feasibility and unchanged diameter. All new row sites are contact-isolated and strictly inside `conv(W_k)`, so none supports a diameter pair. If the endpoint had a normalized KKT stress, it would be supported entirely on the fixed exterior and wall labels. Their contact and diameter pairs have not changed. Extending the stress by zero on every original row contact gives a normalized stress of `A` supported away from `U`, contradicting the deletion hypothesis. The canonical finite KKT strict-motion alternative therefore supplies a finite strict descent of this reduced endpoint. This argument uses all support faces, rather than one selected stress.

The deletion hypothesis is supplied, for example, by the companion forced-channel proposition when every normalized stress has positive weight on the row's common longitudinal channel. It is not supplied merely by one full positive stress. Corollary R preserves the exact deficit `|U|`; Theorem S prevents restoring that population strictly inside the unchanged strip.

### 4.1 Freeing both end guards does not restore capacity

There is a stronger obstruction when the two end labels may also be replaced. Let only the `2k` side-row guards

```text
W_k^side={j u-v,j u+v: 0<=j<=k-1}
```

stay fixed, and confine all `k+2` free labels to the original `F_k`. Their old sites are `P_k union {-u,k u}`.

**Lemma L (proved candidate, co-circular free-vertex guard).** Let `a,b,c` lie on the unit circle about `O=0`, with `b=-c`. In `T=conv{a,b,c}`, let `E_T` consist of points at distance at least one from both `b,c`. Then

```text
E_T subset B_open(a/2,1/2) union {0,a}.
```

To prove it, write `x=lambda a+mu b+nu c`, with nonnegative coefficients summing to one. The exact weighted-square identity is

```text
lambda|x-a|^2+mu|x-b|^2+nu|x-c|^2=1-|x|^2.
```

The two guard inequalities give `lambda|x-a|^2<=lambda-|x|^2`. If `lambda=0`, then `|x|=0`. If `lambda=1`, then `x=a`. Otherwise, for `x!=0`, substitution of `|x-a|^2=1+|x|^2-2a dot x` gives

```text
|x-a/2|^2-1/4
 =|x|^2-a dot x
 <=-(1-lambda)|x|^2/(2lambda)<0.
```

This proves the complete continuous-coordinate lemma. No angle bound was needed for it.

**Theorem E (proved candidate, movable-end capacity).** For every `k>=2` and `0<=c<1/2`, the weak capacity in `F_k` guarded only by `W_k^side` is `k+2`, with unique filling `P_k union {-u,k u}`. Strict capacity relative to the side-row guards is exactly `k+1`.

Decompose `F_k` in axial coordinates into the left triangle `conv{-u,-v,v}`, the middle parallelogram `conv{-v,v,(k-1)u-v,(k-1)u+v}`, and the right triangle `conv{k u,(k-1)u+v,(k-1)u-v}`. Lemma L confines each clear cap point to the open diameter disk of its end interval, apart from the two original endpoint sites.

For a clear point in the middle parallelogram with `X<=0`, the same radius-`R_0` triangulation cover can only use the site `0`. In axial coordinates the parallelogram has `a>=0`, so its component along `w=s u-c n` is `a s>=0`. It cannot be zero unless the point itself is zero: otherwise clearance from `v,-v` would require `|t|>=2` for `x=t v`, whereas `|x|<1`. Thus the positive projection estimate in Section 3.1 applies directly and gives `X>0` for every nonzero point. It does not need the freed end guard. Reflection gives `X<k-1` at the other end. The interval-disk proof of Section 3.2 applies unchanged in the middle, since the virtual end-guard clearances there follow from horizontal coordinates.

Consequently the entire clear set is partitioned by the `k+2` original nodes from `-u` to `k u`, with each intervening open interval contained in its open diameter disk. Each nonnode point blocks both adjacent nodes, and each interval contains at most one unit-separated point. The path-block count of Section 3.3 proves capacity `k+2` with equality only at all original nodes.

Strict clearance excludes the `k` interior nodes but permits the two end nodes, whose side-row guard distances are at least `sqrt(2-2c)>1`. Each end interval may supply either its outer end node or one nonnode point, never both. Each of the `k-1` middle intervals supplies at most one point. Strict capacity is therefore at most `k+1`. The two old end sites together with the `k-1` packet from Section 3.4 attain it: that packet was strictly separated from both end sites as well as all side guards. This proves the theorem.

The weak bound and equality classification remain valid with arbitrary original exterior labels and upper bounds imposed, since those only remove feasible placements and the old filling remains feasible. Strict capacity here means clearance from the side-row guards; an old end site may still have a unit contact with an exterior label. No claim is made that the two freed ends are strictly separated from every exterior point.

Thus even joint finite relocation of the full row and both end labels cannot change the equal-cardinality point set while confined to `F_k` and retaining the side-row guards. Moving a side-row guard or leaving the strip is necessary. This conclusion permits the end labels to be actual loaded endpoints and does not need a certificate of their loading.

### 4.2 Actual contact-star chambers without a lattice assumption

The same weighted identity applies to any finite guard set `G` on the unit circle about `p`, with one free vertex `q` at unit distance from `p`. In `F=conv(G union {q})`, for `x=lambda q+sum mu_g g`, translate `p=0` and use

```text
lambda|x-q|^2+sum mu_g|x-g|^2=1-|x|^2.
```

Guard clearance gives exactly the estimate from Lemma L. Thus the guard-clear set is contained in the open radius-`1/2` disk about `(p+q)/2`, apart from `p,q`. Antipodal guards are not required. To include both old free labels in the chamber, only `p in conv(G union {q})` is required; the retained guards need not surround `p` by themselves.

**Theorem J (proved candidate, actual contact-star rigidity).** Let `A` be any unit-separated triangle-free actual source, let `p,q` be a unit contact, and let `G` be the other unit-contact neighbors of `p`. Assume `G` is nonempty and `p in conv(G union {q})`. Keep all labels in `G` fixed and confine replacement positions for the two labels `p,q` to `F=conv(G union {q})`. The unique unit-separated two-site filling is `{p,q}`; strict capacity relative to `G` is exactly one. No other original non-guard label, including a contact isolate, lies in `F`.

The containing-disk bound gives capacity at most two, with equality only at the two diameter endpoints `p,q`. They are actually present and feasible, giving equality. Triangle-freeness says `|q-g|>1` for every `g in G`, so `q` itself is a strict site; `p` is not strict. Every pair containing a point strictly inside the diameter disk has distance below one from any other point in that disk or either endpoint, proving strict capacity one. An additional original source label in `F` would be a third unit-separated guard-clear point, impossible. Arbitrary exterior labels and upper constraints can only restrict possible replacements further; the old pair remains feasible.

At any unloaded vertex with a nonzero nonnegative contact equilibrium, the neighbor-hull hypothesis is automatic. Indeed,

```text
sum_{r in N(p)} alpha_{pr}(p-r)=0,
p=sum_{r in N(p)} [alpha_{pr}/sum_s alpha_{ps}] r.
```

There must be at least two distinct contact neighbors, since a single nonzero unit vector cannot balance. Thus `G` is nonempty for every choice of `q`, and `p` belongs to `F`, which is the hull of all original contact neighbors. No positivity at every incident edge or particular contact degree is needed. Canonical unloaded positive-contact core vertices have this equilibrium; contact isolates remain outside this claim and remain part of the full source.

If only `p` is freed and every neighbor is kept fixed, the same identity with no free-vertex term is even stronger: for `x in conv(N(p))`, weak clearance from all neighbors implies `1-|x-p|^2>=1`, hence `x=p`. The weak one-site filling is unique and strict capacity is zero.

Thus original-neighbor-hull restoration is rigid at every such unloaded source vertex, even when one arbitrary unit neighbor is also freed. This includes a loaded neighbor `q` when present. A changed equal-cardinality endpoint must move another retained neighbor or leave the chamber. The theorem does not obstruct either possibility or vertices for which there is no nonzero unloaded contact equilibrium. It is a finite actual-source statement and requires no lattice, pinned-stress model, Schur kernel, or integration assumption.

The result excludes this precise restoration mechanism in any actual source that contains the strip. It does not extract a strip from an arbitrary canonical source, prove forced-channel stress positivity, move a wall, or place the missing label elsewhere. Neither a reduced-cardinality strict packet nor a strict reduced-source KKT motion settles Level I.

The bare strip has `3k+2` points, `5k-1` contacts, no unit triangles, and diameter `k+1`. It is nonglobal for every `k>=2`. For `k=2,3,4`, square/rectangular grid competitors have squared diameters at most `8,13,18`, below `9,16,25`. For `k>=5`, put `3k+2` points in a square integer grid of side count `ceil(sqrt(3k+2))`: its squared diameter is below `2(3k+2)<(k+1)^2`. These are limiting/adversarial fixtures, not globally optimal counterexamples.

**Exact next obligation:** exhibit, in every relevant canonical survivor, a stress-killing vacancy path together with a finite replacement that either changes a side-row guard or puts at least one replacement label outside the corresponding strip, restores cardinality, and satisfies every source lower and upper pair. Theorems S and E say the extra population cannot be funded inside the strip even if both end labels are freed.

## 5. Certificates

Run the companion exact verifier:

```text
python3 research/verify_target_c_rhombic_vacancy_hop_slot07_2026_10_10.py
```

Its shared JSON certificate now includes 32 whole-strip fixtures (`k=2,3,5,9` at eight rational/algebraic angles): 5,000 old-source pairs, 4,512 endpoint pairs, and 2,120 strict inserted pairs. Every fixture certifies a `k-1` packet, unchanged diameter, old contact census, and a smaller grid competitor, in rational or `Q(sqrt(15))` arithmetic. The verifier chooses a positive rational `epsilon` by exact halving and then checks every pair; no floating-point tolerance is used.

The same run checks 5,000 exact barycentric cap identities and 906 clear-cap disk samples. Those samples were an adversarial check before the universal weighted-identity proof; they do not prove Lemma L or the contact-star theorem. Their universal proofs are analytic above, as is the unloaded-equilibrium implication.

The universal continuous-coordinate upper capacity and equality classification are analytic above; finite endpoint checks do not certify them. Arbitrary exterior labels are handled by the analytic wall shield, not by a finite fixture standing in for those labels. These results require independent audit before promotion.
