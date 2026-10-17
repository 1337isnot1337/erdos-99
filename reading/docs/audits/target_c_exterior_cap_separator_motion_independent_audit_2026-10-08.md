> Generated reading edition · [exact source](../../../docs/audits/target_c_exterior_cap_separator_motion_independent_audit_2026-10-08.md) · source SHA-256 `da7630d9c6728a86ef1441f0c4db9e58baa8617d3777731e594747f3ea9994ee`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BEA8A9DED869","canonical":true,"claim_ids":["C-EXTERIOR-CAP-CORE-CONTACT-CUT","C-EXTERIOR-CAP-DIAMETER-SEPARATOR","C-EXTERIOR-CAP-FULL-SOURCE-STRIP-DESCENT"],"claim_statuses":{"C-EXTERIOR-CAP-CORE-CONTACT-CUT":"canonical","C-EXTERIOR-CAP-DIAMETER-SEPARATOR":"canonical","C-EXTERIOR-CAP-FULL-SOURCE-STRIP-DESCENT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: exterior-cap diameter separator and reduced-source motions

**Date:** 2026-10-08  
**Audit base:** `origin/main=fc22be030d803ff4a304f827cdd3a16bd247b27c`, state `2026-10-08.audit.138`  
**Frozen source:** `research/sol/target-c-exterior-cap-closure-20261006` at `f4a362727779f6afc0f01738015112c04fdb73d5`  
**Source report:** `docs/reports/target_c_exterior_cap_separator_motion_and_interior_refill_2026-10-06.md`, SHA-256 `0192a54ab219b0a6bdfd4ea012138d82c59a219e59b13ad4b6a395a3081abfce`

## Verdicts

- **PASS — promote `C-EXTERIOR-CAP-DIAMETER-SEPARATOR`.** Under the stated finite circumradius and diameter-midpoint hypotheses, an actual loaded-hull cap side places every actual diameter endpoint a distance at least `g` from its line through the full-source circumcenter, and every actual diameter pair crosses that line. For a fixed positive-area cap, `g` is linear in `D`; the full diameter graph is then bipartite and lies in the Woodall caterpillar-forest branch, while `q <= pi D - A_C + 1` excludes `q/D -> pi`.
- **PASS WITH REPAIRED PROOF — promote `C-EXTERIOR-CAP-CORE-CONTACT-CUT`.** The stated `O(D)` core deletion and strict-diameter reduced source are valid with every contact isolate retained. The source proof's phrase “the connected core” is not needed: canonical connectivity is for the mixed contact-plus-diameter graph, and does not itself assert contact-graph connectivity. If the contact cut were empty, the same two-shore motion with no deletions would preserve every contact and strictly shorten every actual diameter, contradicting global minimality. This proves the needed nonemptiness.
- **PASS — promote `C-EXTERIOR-CAP-FULL-SOURCE-STRIP-DESCENT`.** The fixed-width full-source strip deletion and uniform finite translation preserve unit separation, strictly shorten every cross-shore pair, retain every actual diameter endpoint, and give diameter `<D` after deleting at most the stated `O(D)` labels.
- **No C-II or Level I closure.** Both motions reduce cardinality and supply no forced refill packet. The source's stress-transversal extension, explicit refill construction, and stronger packet obligation are outside this audit and remain unpromoted.

## Exact geometry for the cap separator

Translate the full-source circumcenter to `0`. Let `R` be the circumradius of the full source hull, and assume every actual diameter midpoint `m=(b+k)/2` satisfies `|m|<=L`. Let `F=conv(B)` be the actual loaded endpoint hull. For one actual exterior cap, let its base be a side of `F`, with outward unit normal `u`, so `F` lies in `u dot x <= c`, `c>=0`. Put `w=Ju`, `r=D-R`, and assume

$$
c+2L<r,\qquad g=\sqrt{r^2-(c+2L)^2}>L.
$$

For any loaded endpoint `b`, choose its actual diameter partner `k`. Since `|k|<=R` and `|b-k|=D`, `|b|>=D-R=r`. The loaded endpoints both lie in `F`, and the midpoint bound gives `|u dot (b+k)|<=2L`. Hence

$$
-c-2L\le u\cdot b\le c,
\qquad |u\cdot b|\le c+2L,
\qquad |w\cdot b|^2=|b|^2-|u\cdot b|^2\ge g^2.
$$

The same estimate holds for `k`. If `b` and `k` had the same sign of `w`-projection, then `|w dot (b+k)|>=2g>2L`, contradicting `|b+k|<=2L`. Thus every full actual diameter edge crosses `w dot x=0`, and every loaded endpoint is at signed distance at least `g` from it.

### Macroscopic cap consequence

For a canonical source, `C-FS-GEOM` gives

$$
D/2\le R<D/2+3^{1/4}\sqrt D,
\qquad L=\sqrt{D\eta+\eta^2}=O(D^{3/4}),
\quad \eta=3^{1/4}\sqrt D.
$$

`C-DB-DENSITY` places the full-source circumcenter inside the loaded force hull, so the chosen side has `c>=0`. If the actual cap has area at least `alpha D^2` for fixed `alpha>0`, it is contained in the circumdisk's segment `u dot x>=c`; the normalized circular-segment area tends to zero if `c/R` tends to one. Therefore `c/D` stays below `1/2` by a positive amount depending on `alpha`. Since `R/D -> 1/2` and `L/D -> 0`, the two finite inequalities hold for all sufficiently large `D` and give `g>=gamma_alpha D` for some `gamma_alpha>0`.

All actual diameter edges cross the line, so the full actual diameter graph is bipartite. `C-WOODALL` then excludes its `d_H=0` odd-unicyclic alternative; the graph is in the `d_H>0` caterpillar-forest branch. Let `A_C` be the full-source boundary arc forming the cap and containing no other loaded endpoint. The cap perimeter is `A_C+|ab|<=2A_C`; the isoperimetric inequality gives `area(C)<=A_C^2/pi`, hence `A_C>=sqrt(pi alpha)D`. The other `q-1` consecutive loaded boundary arcs each have length at least one, so

$$
q\le \operatorname{per}(\operatorname{conv}A)-A_C+1
 \le \pi D-\sqrt{\pi\alpha}\,D+1.
$$

This excludes the terminal `q/D -> pi` subcase whenever an actual exterior cap has area at least `alpha D^2`. It does not force `d_H` to be linear or exclude the nonmatching forest branch.

## The core contact cut and finite motion

Use the canonical nonisolated positive-contact core `V`, all actual contacts `C`, and all actual diameter edges `H`. The canonical incidence theorem places every loaded endpoint in `V`; all contact-isolated source labels remain outside the motion argument and are kept fixed. Define

$$
V_- = \{p\in V:w\cdot p\le0\},\qquad V_+=\{p\in V:w\cdot p>0\},
$$

and let `R_-` be the negative-shore endpoints of contact edges crossing this cut. Each `p in R_-` satisfies `-1<w dot p<=0`. Since `g>1`, no loaded endpoint is in `R_-`.

The strip containing `R_-` has width one and tangential span at most `D`. Oler's finite inequality, with unit-separated centers, and the perimeter bound `per(conv R_-)<=2D+2` give

$$
|R_-|\le (2/\sqrt3)D+D+2=(1/a_0+1)D+2,
\qquad a_0=\sqrt3/2.
$$

For nonemptiness, suppose `R_-` were empty. Then no old contact crosses the cut. Translate every point of `V_-` by `+epsilon w` and every point of `V_+` by `-epsilon w`, retaining every source isolate fixed. All contacts stay unit, and every actual diameter pair crosses the cut and strictly shortens. Every other full-source pair has strict lower and upper margins; since the source is finite, one sufficiently small positive `epsilon` preserves all of them. This would give an `n`-point source of diameter `<D`, contradicting global minimality. Thus `R_-` is nonempty. This proof does not assume that the contact graph is connected.

Now delete `R_-`, and perform the same shore translations. Every surviving old contact has both ends on one shore, so it remains exactly unit. Every old actual diameter endpoint remains because it is more than one from the cut, and every old diameter edge has projection span `d>=2g`. Its new squared length is

$$
D^2-4\epsilon d+4\epsilon^2<D^2
\qquad(0<\epsilon<g).
$$

For every retained pair that was neither a contact nor an actual diameter, the original distances lie strictly between `1` and `D`. The minimum of the finitely many positive lower and upper margins is positive. Taking `epsilon` smaller than one quarter of this minimum and than `g` preserves all such constraints, including pairs between moving core labels and fixed contact isolates. Therefore the reduced source has `n-|R_-|` unit-separated points and diameter `<D`. No uniform positive lower bound on this `epsilon` is claimed.

## Uniform full-source strip descent

For any `1/2<a<g`, remove all source labels `R_a={p in A:|w dot p|<a}` and move the remaining negative and positive shores by `+epsilon w` and `-epsilon w`, respectively, where `0<epsilon<a-1/2`. Within-shore distances stay fixed. Across shores, the new normal separation is at least `2(a-epsilon)>1`, and for an old cross-shore vector with normal component `d>=2a`,

$$
|x-y-2\epsilon w|^2-|x-y|^2=-4\epsilon d+4\epsilon^2<0.
$$

All old diameter pairs cross the line, so every same-shore pair was already strictly below `D`, while every cross-shore pair strictly decreases. This proves the new diameter is strictly below `D`. The strip has width `2a`, tangential span at most `D`, area at most `2aD`, and perimeter at most `2D+4a`; Oler gives

$$
|R_a|\le(2a/a_0+1)D+2a+1.
$$

All actual diameter endpoints are retained because their cut distance is at least `g>a`. The parameter `epsilon` is a uniform permitted finite translation for the given `a`; this says nothing about the resulting full-source diameter gap, since same-shore pairs remain unchanged.

## Dependencies, regressions, and excluded claims

The canonical loaded-endpoint and full-source geometry inputs are `C-FS-GEOM`, `C-DB-DENSITY`, `C-LOADED-HULL-CAP-BUDGET`, and `C-DIAMETER-LEAF-CONTACT-INCIDENCE`. The forest conclusion uses `C-WOODALL`. The exact cut proof uses no KKT weight lower bound and no selected-stress-only diameter graph. It retains every isolate; the core cut fixes isolates, while the strip cut removes all labels in its strip.

The existing paired-cap nonglobal regression (Audit.94) is consistent with these results: it lacks the canonical mixed-rigidity and loaded-density hypotheses. It blocks using paired caps and local KKT features alone to infer globality; this audit supplies no refill or same-cardinality competitor.

The source report's S.3-L localized stress-transversal theorem is not promoted: its reduction to strict source descent cites the separate E.5 signed-row-separation argument, which is not needed by the claims proved here. The explicit Section 5 refill construction is also not audited here; its verifier, if used, would certify only its listed finite packets, not the all-`M` analytic argument. The global macroscopic-cap extraction and the forced packet/refill step remain open.

## Claim ledger

| Claim | Verdict | Disposition |
| --- | --- | --- |
| Loaded diameter endpoints avoid an actual cap base line and each diameter crosses it | PASS | Canonical `C-EXTERIOR-CAP-DIAMETER-SEPARATOR` |
| A macroscopic actual cap forces bipartite Woodall forest topology and a linear gap below `q/D=pi` | PASS | Included in `C-EXTERIOR-CAP-DIAMETER-SEPARATOR` at fixed-`alpha` asymptotic scope |
| The core cut deletes at most `(1/a_0+1)D+2` unloaded labels and admits a finite strict-`D` reduced-source motion with all isolates fixed | PASS WITH REPAIRED PROOF | Canonical `C-EXTERIOR-CAP-CORE-CONTACT-CUT` |
| A full-source width-`2a` strip can be deleted at `O(D)` cost with a uniform finite translation and strict reduced diameter | PASS | Canonical `C-EXTERIOR-CAP-FULL-SOURCE-STRIP-DESCENT` |
| Localized S.3-L stress transversals, explicit Section 5 refill, or canonical macroscopic-cap extraction | NOT AUDITED / NOT PROMOTED | Separate proofs are required; the refill premise remains the C-II gap |
| C-II or Level I closure | NOT CLAIMED | No forced refill or same-cardinality competitor is supplied |

## Frontier effect

An actual macroscopic exterior cap is incompatible with the terminal `q/D -> pi` branch. In the macroscopic-cap branch, the full diameter graph lies in the Woodall forest branch and the cap induces an `O(D)` source deletion with a strict sub-`D` reduced configuration. To restore cardinality, one still needs a forced packet of exactly the deleted size at the translated endpoint that passes every full-source lower and upper check. No such packet is established. The active C-II finite-move/payment obligation is unchanged.
