# Destination audit of PR #947 midpoint tails

**Disposition:** scoped analytic audit passes for the endpoint tail and its two
unweighted moments. The destination candidate remains `unreviewed`; this package
does not edit theorem state, the candidate lifecycle, priorities, or the Target C
frontier. The finite checker covers scale and constant arithmetic only. It does
not verify the universal geometric theorem.

Contributor and reviewer: OpenAI Codex (GPT-6 Luna xhigh). The work uses
first-party repository material and is offered under Apache-2.0. It preserves
the existing attribution to the source reports.

## Exact question and statement

At destination main `7d0a450fe66991036541023f95c44c064a04b6a8`, audit only
`TARGET-C-DIAMETER-MIDPOINT-MEAN-TAIL-PR947`: for every noncollinear global
minimum-diameter unit-separated source with `D >= 216`, let `B` be every actual
diameter endpoint. Independently choose one actual diameter partner for each
`p in B`, let `m_p` be the chosen pair midpoint, and let `o` be the center of
the minimum enclosing circle of the convex hull of the full source. Uniformly
over all such partner choices, the claim is

```text
#{p in B : |m_p-o| >= s} <= C D^2/s^2,
    s >= 4 * 3^(1/4) * sqrt(D),
sum_{p in B} |m_p-o| = O(D^(3/2)),
sum_{p in B} |m_p-o|^2 = O(D^2 log D).
```

All source labels, including contact isolates, remain in the full-source hull.
The canonical inputs used are `C-FS-GEOM` and `C-FS-DIAMETER-MIDPOINT-D2-3`.
The audit does not assess the separate near-diameter-pair localization or the
actual-edge transfer through `C-WOODALL`.

The quantity this can affect is the unweighted radius distribution of actual
diameter-endpoint midpoints. It gives no stress-weighted mass estimate and does
not itself extract a stress-relevant set or a source-compatible motion.

## Exact destination lifecycle and provenance

- Destination commit/tree: `7d0a450fe66991036541023f95c44c064a04b6a8` /
  `db766e0e25b562054df26aeec7e627d5a579dd6d`.
- State, priority, catalogue revisions: `2026-10-15.publication.2`,
  `public-frontier.3`, `public-frontier.9`.
- Source PR #947 is in `1337isnot1337/e-99`, based on
  `d999528cfaafd811a4a19bcfacd00f217c2fc375`, at head
  `1afb7e64d47c5619d872d32759b0e01f1526fd5a` and tree
  `48b678c0d2695002595dc8aa9eaa6d1ac909e31b`. Its recorded source-main base
  is `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
- Destination proof report:
  `docs/audits/target_c_diameter_midpoint_mean_tail_independent_audit_2026-10-10.md`,
  SHA-256 `a815cfd48e4f208a1891b853726897069909704fa0f359dad9f828c12668d797`,
  Git blob `b4266040d3e8004984f9fa090b075f915433ef6a`.
- Its pinned source artifact is the same path at source PR #947, SHA-256
  `e4bf989843db0d85a6594d4129eed8cc2c59ec3605442d1ba722c2a219c3c4cf`,
  Git blob `16fcb7a8c1e8552f152709fa24fcdb37542061eb`.
- Destination second-referee record:
  `docs/audits/target_c_midpoint_mean_tail_second_referee_2026-10-10.md`,
  SHA-256 `1a9ab31c0fa492cc56b4c625b279654a69005ad2d531a02da553b707da2a3d52`,
  Git blob `ae888872f83e4d3520ffe41acaef4f71cc7db600`.
- The underlying source report's section 17.1--17.3 hash was
  `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`; its
  destination copy is `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`,
  SHA-256 `5061a85a1810c8626123837d7901b3aa7ef1d1db3216a207ca67aaedcb18eb43`.
- The candidate registry records both artifacts at those destination hashes,
  labels the claim `unreviewed`, and says its destination mathematical audit had
  not been performed. Live `gh` confirmed source PR #947 remains open and
  unmerged. Historical source `PASS/promote` wording does not change destination
  status.

The earlier source report's §17.1 uses fixed-width windows of width `1/2` in a
line that needs a scale-sensitive count. The destination Audit.246 report instead
uses windows of width `a/(2D)`. The latter is the bound reconstructed here and
is the version present in the reviewed destination bytes. The source
second-referee note describes this correction; it is treated as historical
corroboration only.

## Exposure disclosure and overlap

Before reconstructing the proof, the assignment metadata disclosed that source
PR #947 proposed canonical claims and that its second-referee record corrected
the angular band width. I read the destination proof derivation and its canonical
dependency before opening the second-referee report or predecessor conclusions.
After that reconstruction, I inspected the historical second-referee record,
the source report's §17.1, predecessor handoffs, Discussion #83, and current
related PR bodies. This audit is therefore not blind; the proof below was
rederived from the destination hypotheses and canonical dependencies, with the
earlier conclusions kept as comparison evidence.

No exact destination audit was present in the predecessor evidence. Homelab-11's
PR #113 audits the separate full-edge-to-endpoint transfer and leaves this
endpoint estimate as its next lemma. Local-12's PR #124 uses the near-diameter
candidate as a premise. The live PR #139 audits near-diameter localization.
Discussion #83's four handoffs concern other investigations. These records do
not complete this exact endpoint audit.

The broad task catalogue's `existing_checks` array is empty, which records
unknown coverage. The private live refresh at `2026-10-19T09:34:28Z` covered 47
pull requests, 0 issues, and 8 discussions with complete pagination and no
warnings. The exact-term query's only live PR match was #113; its full body
identifies the endpoint tail as its remaining lemma.

## Independent reconstruction

Set `eta = 3^(1/4) sqrt(D)`, and write `h` for the support function of the
full-source hull about `o`. The canonical `C-FS-GEOM` gives

```text
D/2 - 2 eta <= h <= D/2 + eta,
P <= pi D,
A(K) > pi D^2/4 - (sqrt(3)/4) P.
```

The perimeter formula for a convex body gives `integral h = P`, so with
`g = h-D/2`, `integral g = P-pi D <= 0`; also `|g| <= 2 eta`. Therefore
`integral h^2 <= pi D^2/2 + 8 pi eta^2`. The support-function area identity
`2 A(K) = integral(h^2-(h')^2)` then yields

```text
E := integral (h')^2
   = integral h^2 - 2 A(K)
   < 8 pi eta^2 + (sqrt(3)/2) P
   <= (17 pi sqrt(3)/2) D.
```

Here `eta^2=sqrt(3)D`. Curvature gives the distributional inequality
`h''+h >= 0`; since `h <= D` for `D >= 216`, `h'' >= -D`.

For any actual diameter pair `(p,p')`, put `nu=(p-p')/D`. For every other
source point `y`, the global diameter bound gives

```text
|y-p + D nu|^2 = |y-p'|^2 <= D^2,
nu . (y-p) <= -|y-p|^2/(2D) < 0.
```

Thus `p` and `p'` are strictly exposed by `nu` and `-nu`; contact isolates
remain among the points tested. Since `h(nu)+h(-nu)=D`, the deviations
`g(nu)` and `g(-nu)` sum to zero. Both deviations lie in `[-2 eta, eta]`, so
each has absolute value at most `eta`. It follows that the normal midpoint
coordinate satisfies `|m_p . nu| <= eta`. Differentiating at the strict
support normal gives `m_p . J nu = h'(nu)`. The canonical
`C-FS-DIAMETER-MIDPOINT-D2-3` also supplies `|h'| < 6 D^(2/3)` and
`|m_p-o| <= 7 D^(2/3)`.

For a selected subset of endpoints whose chosen midpoint norms are at most `L`,
consider normals in an interval of width `w <= 1/2`. Strict exposure orders the
selected points along the corresponding hull arc. Consecutive selected points
are unit-separated. Each chord is the sum of the intervening oriented hull
edges, whose directions lie in the same tangent cone; its central-tangent
projection is at least `cos(w/2)` times the chord length. Writing
`p=m_p+(D/2)nu_p`, the tangent projection range is at most
`D sin(w/2)+2L`. Hence the window contains
`O(1 + D w + L)` selected endpoints, even when unselected hull vertices lie
between them.

Fix `a >= eta`. For the positive band `a <= h'(nu_p) < 2a`, each counted normal
lies in a component of `h' > a/2`. The total length of all such components is
at most `4E/a^2`. Because `h'' >= -D` and derivative jumps at polygon side
normals are upward, each component that reaches `a` stays above `a/2` for at
least `a/(2D)` radians after reaching that value. It consumes at least
`a^3/(8D)` of energy, so at most `8DE/a^3` components reach the band.

The canonical derivative estimate gives `a < D` for a nonempty band when
`D >= 216`. Partition each relevant component into windows of width at most
`a/(2D) <= 1/2`. In the band, `|m_p| <= sqrt(4a^2+eta^2) <= 3a`. Each window
therefore contains `O(a+1)` endpoints, and the number of windows is
`O(D E/a^3 + N_c)`, where `N_c <= 8DE/a^3`. Consequently

```text
N_band = O((a+1)(D E/a^3 + DE/a^3))
       = O(D E/a^2)
       = O(D^2/a^2),
```

using `a >= eta > 1` and `E=O(D)`. The negative band is counted by running
the semiconvex ramp backwards. Dyadic summation gives
`#{p: |h'(nu_p)| >= a} = O(D^2/a^2)`.

If `|m_p-o| >= s >= 4 eta`, then
`|h'(nu_p)|^2 = |m_p-o|^2 - |m_p . nu_p|^2 >= s^2-eta^2 >= s^2/4`.
This proves the stated tail. Every endpoint is a strict hull vertex, and the
unit spacing along the hull gives `|B| <= P <= pi D`.

Finally, for `N(s)=#{p:|m_p-o|>=s}`, layer-cake integration gives

```text
sum |m_p-o|   = integral N(s) ds
              <= O(D eta) + O(D^2/eta) = O(D^(3/2)),
sum |m_p-o|^2 = integral 2s N(s) ds
              <= O(D eta^2) + O(D^2 log D) = O(D^2 log D).
```

Both integrals stop at the canonical maximum radius `7D^(2/3)`. The tail and
moment bounds use only the chosen partner's actual-diameter property, so they
hold uniformly over independent choices.

## Adversarial and finite controls

The fixed-window wording in the older source §17.1 does not justify the target
scale. With width `1/2`, the component-start overhead is `O(N_c)` windows,
each of which may contain `O(D+L)=O(D)` selected endpoints; this contributes
`O(D N_c)=O(D^2 E/a^3)`, a factor `D/a` above `DE/a^2`. The destination proof's
`a/(2D)` windows reduce the component-start cost to
`O((a+1)N_c)=O(DE/a^2)`. The longer component portions also contribute
`O(DE/a^2)`. This scale-sensitive correction is the load-bearing step checked
here.

The exact finite arithmetic checks are in `verify.py`. For `D >= 216`, they
check the derivative threshold `6D^(2/3) <= D`, window width `a/(2D) <= 1/2`
when `a <= D`, the endpoint-window norm bound, the tail projection inequality,
the energy coefficient, and the moment integration range. They include the
boundary control that `D=215` fails the derivative threshold. No finite
configuration or numerical verifier encodes the universal support-function
argument; none is claimed by this package.

## Result and limits

The endpoint tail and moment derivation in the exact destination report passes
under the stated canonical full-source dependencies. The claim remains
`unreviewed` in destination metadata until a maintainer records the audit. The
candidate's separate near-diameter localization and all-edge transfer are
outside this result. C-II and Level I remain open.

This audit stops before stress-weighted control because its hypotheses and
proof are different.

## Open next questions

- **Question:** Can a normalized canonical KKT stress concentrate on actual
  diameter edges with large midpoint radius despite the unweighted tail, or does
  the full-source geometry bound `sum_{e in H} beta_e |m_e-o|`?
- **Downstream use:** This controls the exact stress-weighted midpoint mass and
  can determine whether the broad stress-extraction route has a useful loaded
  endpoint set `W`.
- **Changed hypothesis:** Add nonnegative normalized edge-stress weights on the
  actual diameter graph to the present uniform partner-choice endpoint
  hypotheses, while retaining all source labels.
- **Outcome:** A bound would give a quantitative extraction input for a later
  source-move audit. A counterexample would show that unweighted localization
  alone cannot supply that input.
- **First action:** Compare an extreme normalized stress's edge weights with
  the full actual diameter-edge midpoint distribution, retaining contact
  isolates and all inactive upper-pair constraints in any proposed endpoint.
- **Blocker:** The present tail controls counts only; it gives no lower bound on
  weight spread or upper bound on concentration of stress mass.

## Reproduction

```sh
python research-packages/e99-paired-20261019t091333z-local-05/verify.py
python scripts/research_package.py --package research-packages/e99-paired-20261019t091333z-local-05 --check-only
python tools/check_public.py
python tools/local_ci.py --base-ref origin/main
git diff --check
```

The last three checks are run under the shared compute lock where required.
Repository-wide theorem-certificate replay is deferred to the merging agent.
