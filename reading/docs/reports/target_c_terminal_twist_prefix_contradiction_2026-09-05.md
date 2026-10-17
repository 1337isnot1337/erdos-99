> Generated reading edition · [exact source](../../../docs/reports/target_c_terminal_twist_prefix_contradiction_2026-09-05.md) · source SHA-256 `ff9bf2ae92c6fe98adb4a73907bd5a809d1a2ee29e84c911c9dcb07f345a4cba`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C7A465A28DA7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C97: terminal-twist / full-span-prefix contradiction

**Date:** 2026-09-05  
**Run type:** exact branch closure / promoted audited theorem  
**Target:** canonical pure-rhombic C80-C96 chain-face survivor  
**Audit:** `docs/audits/target_c_c97_terminal_twist_audit_2026-09-05.md`  
**LEVEL I STATUS:** STILL OPEN globally

## Result

The exact pure simply connected strict-rhombic C80 chain-face branch is empty.

The proof combines three exact facts:

1. the C80 diameter chain has a forced terminal twist;
2. C88 equality forces the full-span simple prefix edge `{0,D}`;
3. C87.4 requires every simple prefix edge in both physical hull-arc orientations.

The terminal twist makes one of those two full-span orientations equal to the original chain diameter `za`, whose transverse coefficient is zero. It therefore cannot supply the required non-chain orientation. This is a contradiction.

## 1. Inputs

Use the exact C80 chain

`z=x_0,x_1,...,x_D=a`,

with ordered chain trains

`P={tau_1,...,tau_D}`,

where `x_(j-1)x_j` belongs to `tau_j` and the `tau_j` are exactly the tracks separating `z` from `a`.

C83 assigns every source vertex a prefix level

`k(v) in {0,...,D}`,

with `k(z)=0`, `k(a)=D`.

C87 splits the convex-hull boundary at `z,a` into two arcs `L,U`, each ordered from `z` to `a`. Along each arc, `k` is nondecreasing.

For a non-chain active diameter with interval `(a,b]`:

- positive transverse orientation is physically `L_a U_b`;
- negative transverse orientation is physically `U_a L_b`.

C87.4 says every simple prefix edge `{a,b}` occurs in both orientations, with positive relative-interior KKT flow in each.

C88 Section 1 gives `a_1=0`, `M_1=D`, and row 1 complete. Therefore

`{0,D} in E(G_P)`.

So C87.4 requires actual non-chain active diameter pairs in both physical orientations over `{0,D}`.

## 2. Internal chain degree four

For `1<=i<=D-1`, the chain vertex `x_i` lies in the relative interior of the diameter segment `za`, so it is not extreme. Canonical extremality therefore excludes every actual diameter pair incident to `x_i`. Under C65 full contact visibility, its equilibrium uses only positive unit-contact forces.

The chain contributes the two opposite contact rays `+u,-u`. Positive equilibrium requires at least one further contact ray in each open half-plane bounded by the chain line. Triangle-freeness implies every angular gap between consecutive unit-contact rays is strictly larger than `pi/3`; consequently each of the two open semicircles can contain at most one extra ray.

Thus every internal chain vertex has exactly four contacts: the two chain contacts and one off-chain contact on each side.

Write the upper unit neighbor as

`y_i=x_i+v_i`,

`v_i=(cos theta_i)u+(sin theta_i)Ju`,

with

`pi/3<theta_i<2pi/3`.

Write the lower unit neighbor as `w_i=x_i+r_i`, with oriented angle

`alpha_i in (-2pi/3,-pi/3)`.

## 3. Monotone off-chain rows

Unit separation of consecutive upper neighbors gives

`|u+v_(i+1)-v_i|>=1`.

Set

`m=(theta_i+theta_(i+1))/2`,

`delta=(theta_(i+1)-theta_i)/2`.

A direct expansion gives

`|u+v_(i+1)-v_i|^2-1 = 4 sin(delta)(sin(delta)-sin(m))`.

Because `m in (pi/3,2pi/3)` one has `sin(m)>sqrt(3)/2`, while `|delta|<pi/6` gives `|sin(delta)|<1/2`. Hence `delta>0` is impossible and

`theta_(i+1)<=theta_i`.

Equality holds exactly in the rhombic continuation case. The same calculation below the chain gives

`alpha_(i+1)>=alpha_i`,

again with equality exactly across a lower rhombus.

## 4. Two terminal rhombi on one side are impossible

Suppose the first and last chain edges both have a rhombus on the upper side. Then the upper row extends to

`y_0=x_0+v_0`, `y_D=x_D+v_D`

with the same monotonicity. Since the source diameter is `D`,

`|y_D-y_0|=|D u+v_D-v_0|<=D`.

Monotonicity gives

`u dot(v_D-v_0)=cos(theta_D)-cos(theta_0)>=0`.

Therefore

`|D u+v_D-v_0|^2 = D^2+2D u dot(v_D-v_0)+|v_D-v_0|^2 >= D^2`,

with equality only when `v_D=v_0`.

The diameter bound forces equality, so every upper vector is the same vector `v`. The source would then contain the two parallel length-`D` segments `x_0x_D` and `y_0y_D`. But

`|D u+v|^2+|D u-v|^2=2D^2+2`,

so one cross distance exceeds `D`, contradiction.

The same argument applies below the chain. Hence each side must have an outer-face incidence at one of the two terminal chain edges. A terminal edge cannot have the outer face on both sides in a rhombic disk. Therefore both terminal chain edges are outer-boundary edges, and their outer sides are opposite.

This is the forced terminal twist.

## 5. The two terminal edges lie on opposite outer-boundary paths

The pure rhombic disk has a simple outer boundary. Delete `z,a`; it consists of two boundary paths from `z` to `a`.

A fixed oriented boundary path has the disk interior locally on the same side at every traversed edge. Both terminal chain edges are traversed geometrically as `+u` on a `z`-to-`a` path. The terminal twist puts the disk interior on opposite sides of those two collinear `+u` edges. Hence the two terminal chain edges cannot lie on the same boundary path.

Call the path containing `x_0x_1` the `U` path and the path containing `x_(D-1)x_D` the `L` path, swapping the names if necessary. Every convex-hull vertex is an extreme source vertex and lies on the outer boundary; deleting non-hull boundary vertices gives exactly the two C87 hull arcs in the same cyclic order.

## 6. Two endpoint prefix fibers are singleton

The train `tau_1` is a proper crosscut separating `z` from `a`, and its `U`-side terminal is the first boundary edge

`x_0x_1`.

A proper crosscut has only two boundary terminals, one on each `z`-to-`a` boundary path. Thus the `U` path crosses `tau_1` in its first edge and never again. Every source vertex of that path after `z` lies on the `a` side of `tau_1`, so its prefix level is at least `1`.

Therefore

`U_0={z}`.

Similarly, `tau_D` terminates on the `L` path in the final boundary edge `x_(D-1)x_D`, and that path meets `tau_D` nowhere earlier. Every source vertex before `a` has prefix level at most `D-1`. Hence

`L_D={a}`.

No uniqueness is asserted for any intermediate prefix level.

## 7. Full-span prefix contradiction

C88 forces the simple full-span edge `{0,D}`.

C87.4 requires one actual non-chain diameter in each physical orientation over that edge. In particular it requires the orientation

`U_0 L_D`.

But Sections 5-6 give

`U_0={z}`, `L_D={a}`.

Therefore that required active diameter pair is exactly

`za`.

The chain bar has

`r_za=D u`

and therefore transverse coefficient

`eta_za=r_za dot Ju=0`.

C83 proves every non-chain active diameter meeting the chain atom has `eta!=0`. Hence `za` cannot supply the required reverse transverse orientation for `{0,D}`.

Contradiction.

### Theorem C97 — terminal-twist prefix contradiction

No C65 lexicographically normalized triangle-free global minimizer can simultaneously admit the exact C76/C80 straight-chain KKT face and the pure simply connected strict-rhombic train-coordinate realization.

Equivalently, the canonical exact pure chain-face branch C80-C96 is empty.

## 8. Scope

This does not yet settle Erdős #99.

C76 proves only

`S_z=1 => exact straight-chain stress`.

It does not prove that a finite C-II source has a stress with `S_z=1`; the star face can be empty. C66-C81 permit sequences whose KKT stresses approach the star degeneration without reaching it. C80 also assumes the pure simply connected rhombic train model.

Therefore the live Target C problem moves one level outward:

1. prove a uniform quantitative gap from the impossible exact star face;
2. or prove a near-chain stability theorem carrying C97 to `S_z=1-o(1)`;
3. or extend the terminal-prefix obstruction through the exceptional topology outside the pure-rhombic disk.

The exact C80-C96 branch should no longer be treated as a realizable equality model.
