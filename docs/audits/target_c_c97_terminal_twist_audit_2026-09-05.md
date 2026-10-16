<!-- theorem-state: {"artifact_id":"ART-8A38BA520995","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Audit — Target C C97 terminal-twist / prefix contradiction

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_c_terminal_twist_prefix_contradiction_2026-09-05.md`  
**Verdict:** PASS under the stated pure simply connected strict-rhombic C80 chain-face hypotheses.  
**Global LEVEL I status:** STILL OPEN.

## Checked implications

1. **Internal chain vertices have no diameter reaction.** For `1<=i<=D-1`, `x_i` lies in the relative interior of `za`, hence is not extreme. Canonical extremality therefore excludes every actual diameter pair at `x_i`. C65 then leaves only positive contact forces in equilibrium there.

2. **Exact degree four is valid.** The two chain rays are `+u,-u`. Positive equilibrium forces an off-chain ray in each open half-plane. Triangle-freeness makes every adjacent pair of unit-contact rays differ by strictly more than `pi/3`, so each semicircle from `+u` to `-u` contains at most one extra ray. Thus every internal chain vertex has exactly four contacts.

3. **Monotone-row calculation is exact.** For upper neighbors `y_i=x_i+v_i`, with `v_i` at angle `theta_i in (pi/3,2pi/3)`, unit separation of `y_i,y_(i+1)` gives

`|u+v_(i+1)-v_i|^2-1 = 4 sin(delta)(sin(delta)-sin(m)) >= 0`,

where `m=(theta_i+theta_(i+1))/2` and `delta=(theta_(i+1)-theta_i)/2`. Since `sin(m)>sqrt(3)/2` and `|sin(delta)|<1/2`, `delta>0` is impossible. Hence `theta_(i+1)<=theta_i`; equality is exactly rhombic continuation. The lower row is monotone in the opposite oriented sense.

4. **Two terminal rhombi on one side are impossible.** If both upper terminal rhombi exist, the monotone row supplies `y_0=x_0+v_0`, `y_D=x_D+v_D`. The diameter inequality `|D u+v_D-v_0|<=D`, together with monotonicity, forces `v_D=v_0` and hence a translated parallel length-`D` segment. The cross vectors `D u+v` and `D u-v` have squared-length sum `2D^2+2`, so one exceeds `D`. Contradiction. The same holds below. Therefore both terminal chain edges are boundary edges and their outer sides are opposite.

5. **The two terminal edges lie on opposite `z`-to-`a` outer-boundary paths.** The pure disk has a simple outer boundary. Along one oriented boundary path, the disk interior lies locally on one fixed side. Both terminal chain edges would be traversed geometrically as `+u` on the same `z`-to-`a` path, but terminal twist places the disk interior on opposite sides of them. Hence they cannot lie on the same path.

6. **Outer-boundary paths induce the C87 hull arcs.** Every convex-hull vertex is an extreme source vertex and therefore lies on the outer boundary of the planar contact disk. Extreme vertices occur there in the same cyclic order as on `conv A`; deleting non-hull boundary vertices from the two `z`-to-`a` paths gives the two C87 hull arcs, up to swapping `L,U`.

7. **The train endpoint convention is correct.** The canonical rhombic-train convention defines a train by crossing entry/exit contact edges at their midpoints; a maximal train terminates at a boundary contact edge. C80 labels `x_(j-1)x_j` by `tau_j`. Thus boundary edge `x_0x_1` is a terminal edge of `tau_1`, and `x_(D-1)x_D` is a terminal edge of `tau_D`.

8. **Only the needed endpoint prefix fibers become singletons.** Let the path containing `x_0x_1` be `U`. Since `tau_1` is a proper crosscut separating `z,a`, its other terminal lies on the opposite boundary path. Thus `U` crosses `tau_1` in its first edge and never again, so every later hull vertex has level at least `1`: `U_0={z}`. Similarly the opposite path `L` meets `tau_D` only in its final edge, so `L_D={a}`. No uniqueness is asserted for intermediate prefix levels.

9. **C88 forces `{0,D}` as a simple edge.** Its equality structure has `a_1=0`, `M_1=D`, and complete first row `B_1={m_1,...,D}`, so `D in B_1`.

10. **C87.4 requires two actual non-chain orientations.** For `{0,D}`, the two physical orientations are `L_0 U_D` and `U_0 L_D`. The latter is forced by item 8 to be `za`. But the chain bar has `eta_za=0`, while C83 proves every non-chain active diameter meeting the chain atom has nonzero `eta`. It cannot supply the required reverse orientation. Contradiction.

## Scope check

This is not yet a proof of Erdős #99. C76 proves only

`S_z=1 => exact straight-chain stress`.

It explicitly allows the star face `{s:S_z(s)=1}` to be empty. C66-C81 can approach the star degeneration without giving an exact `S_z=1` face on each finite configuration. C80 additionally assumes the pure simply connected strict-rhombic train-coordinate regime.

Therefore the audited statement is:

> **C97 — terminal-twist prefix contradiction.** A C65 lexicographically normalized triangle-free global minimizer cannot simultaneously admit an exact C76/C80 straight-chain KKT face and the pure simply connected strict-rhombic train-coordinate realization. The canonical pure C80-C96 exact-chain branch is empty.

The remaining target is a uniform exclusion neighborhood of this empty star face, or a defect-topology extension that prevents `S_z -> 1` sequences from escaping the exact contradiction.