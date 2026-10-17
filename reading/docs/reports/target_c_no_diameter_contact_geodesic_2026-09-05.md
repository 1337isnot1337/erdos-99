> Generated reading edition · [exact source](../../../docs/reports/target_c_no_diameter_contact_geodesic_2026-09-05.md) · source SHA-256 `a3697e9b28597af5e8c82b6b495b8dbbdf403404392ac4b5d4dd76ecaf04fc92`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E6F8475EEABA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: no exact diameter contact geodesic in the pure-rhombic C65 source

**Date:** 2026-09-05  
**Run type:** exact branch strengthening / dependency audit  
**Target:** C97 extension to C99-C100 near-chain geometry  
**LEVEL I STATUS:** STILL OPEN

## Result

In the C65 lexicographically normalized, fully force-visible, pure simply connected strict-rhombic branch, no active diameter pair `za` can satisfy

`d_C(z,a)=D`.

Equivalently, if `k_(za)` is the number of train tracks separating the endpoints, then

`k_(za)>D`.

Since `k_(za)` is an integer,

`k_(za)>=floor(D)+1`.

When `D` is an integer this is the strict improvement

`k_(za)>=D+1`.

## 1. Equality in graph distance creates the exact geometric chain

C99 identifies contact distance with train-separator count:

`d_C(z,a)=k_(za)`.

Assume for contradiction that `k_(za)=D`.

Orient every separator-train vector from the `z` side to the `a` side and denote it by `a_tau`. Train coordinates give

`p_a-p_z=sum_(tau in P)a_tau=D u`,

where `|u|=1` and every `|a_tau|=1`.

C99's exact identity is

`sum_(tau in P)|a_tau-u|^2=2(k-D)`.

Thus `k=D` forces

`a_tau=u`

for every separator train.

A shortest contact path from `z` to `a` crosses every separator train exactly once and no other train. Along the oriented `z`-to-`a` path, crossing train `tau` changes the corresponding train coordinate from the `z` side to the `a` side, so the unit contact edge vector is `+a_tau=u`.

Hence the source contains the literal straight chain

`z=x_0,x_1,...,x_D=a`,

with

`x_j-x_(j-1)=u`

for all `j`. In particular `D` is an integer in the equality case, the chain uses `D` distinct parallel trains, and those trains are exactly the tracks separating `z` from `a`.

These are precisely the geometric chain-atom properties used from C80 onward. No assertion about a β=1 exposed stress has been made.

## 2. C83 interval normal form requires only the geometric chain atom

C83's ordered-separator proof uses:

1. the `D` pairwise disjoint parallel train crosscuts separating `z,a`;
2. their linear order along the straight chain;
3. the pure simply connected train-coordinate model.

Those hypotheses have just been recovered. Therefore every active diameter pair has one signed interval on the chain tracks and, for every non-chain active diameter meeting the chain atom,

`g_h|P=eta_h 1_(a_h,b_h]`,

with `eta_h!=0`.

The chain diameter `za` itself has zero train-angle gradient because every separator direction is parallel to `u`.

## 3. C84 circulation does not use a β=1 chain stress

Choose the C65 relative-interior normalized KKT stress. It is positive on every actual active diameter pair:

`beta_h>0`.

Train-angle stationarity gives

`sum_h beta_h g_h=0`.

The chain bar has zero restriction to `P`, so C84's derivation applies verbatim:

`sum_(h!=za) beta_h eta_h 1_(a_h,b_h]=0`.

After the discrete prefix derivative, the non-chain interval multigraph carries the nowhere-zero signed circulation

`w_h=beta_h eta_h`.

Thus C84 requires no exposed β=1 face once the exact geometric chain atom is present.

## 4. C86 connectivity also requires only the literal chain

C86.2 is a general theorem of the C65 lexicographic source: every fixed-diameter critical velocity integrates locally while preserving every active contact and diameter pair exactly.

Apply it to the literal chain above. Along any such integrated motion, the `D` chain contacts remain unit and their endpoints remain distance `D`. Equality in the triangle inequality therefore forces all `D` chain edges to remain collinear with one common direction.

Consequently every critical train-angle velocity has one common angular rate on all chain tracks. Modulo global rotation, there is no nonconstant chain-supported neutral mode. C84's rank formula then forces the simple prefix graph to be connected on all `D+1` levels.

Again, no β=1 hypothesis is used.

## 5. C87-C88 and the terminal-twist contradiction rerun

C87 uses exactly:

- the connected prefix graph;
- the nowhere-zero KKT circulation;
- physical hull-arc orientation of the interval bars;
- planar diameter-thrackle order.

Therefore its positive-prefix collapse applies. Every simple interval occurs in both physical hull-arc orientations, the simple prefix graph has exactly `D` edges, and C88's equality analysis gives the staircase normal form. In particular

`{0,D}`

is a simple prefix edge.

The C97 terminal-twist argument itself uses the literal straight chain, full contact visibility, triangle-freeness, and the pure rhombic disk. At every internal chain vertex, absence of diameter reaction and positive contact equilibrium force exactly one off-chain contact on each side. The monotone-row argument forces the two terminal chain edges onto opposite outer-boundary paths. Hence, after naming the paths as in C97,

`U_0={z}`, `L_D={a}`.

But C87 requires both physical orientations of the full-span prefix edge `{0,D}`. One is

`U_0 L_D=za`.

The chain bar has zero transverse coefficient, whereas every non-chain interval representative has nonzero transverse coefficient. It cannot supply the required reverse non-chain orientation. Contradiction.

## Theorem — strict contact-distance gap

No active diameter pair in the C65-normalized pure simply connected strict-rhombic branch is joined by a contact geodesic of Euclidean-optimal length.

For every diameter pair `za`,

`d_C(z,a)=k_(za)>D`.

## 6. Interface with C98-C100

For a dominant diameter edge of KKT weight `b>1/2`, C99 gives

`k_(za)<=D/(2b-1)`.

The theorem here supplies the strict lower endpoint

`floor(D)+1 <= k_(za)`.

Thus

`b <= (1 + D/(floor(D)+1))/2`.

If `D` happens to be an integer, this becomes

`b <= 1 - 1/[2(D+1)]`.

C100 can give a stronger bound when the integer gap is quantitatively separated from zero, but no uniform fractional-part bound for `D` is presently known.

## 7. Scope

This theorem is restricted to the pure simply connected strict-rhombic branch because C83/C87 and the terminal-twist step use the train disk. It does not exclude exact contact geodesics in arbitrary non-rhombic C-II topology.

It also does not by itself contradict C98: the strict gap above `D` can be only `o(D)`.

## Handoff

```text
New exact strengthening:
In the C65 pure-rhombic branch, every active diameter pair satisfies

  d_C(z,a)=# separating trains > D.

Reason:
If equality held, C99 forces every separator train exactly parallel to za and a shortest contact path becomes a literal straight D-edge chain. From that point C83, C84, C86, C87, C88 and the C97 terminal-twist contradiction rerun without needing a beta=1 exposed stress.

For dominant beta b>1/2:
  floor(D)+1 <= k <= D/(2b-1).

Next target:
Quantify the strict contact-distance gap uniformly, or convert even one extra separator / angular defect into a shell or response cost that is incompatible with C98-C101.
```
