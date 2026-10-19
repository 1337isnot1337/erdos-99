# Branch-preserving `0.0071` Section 171 and outer-energy propagation

**Investigation:** `frontier-target-c-branch-aware-atomic-gap-20261018`. **Classification:** conditional, unreviewed research. This package changes no canonical claim lifecycle. **Baseline:** `7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state `2026-10-15.publication.2`; priority `public-frontier.3`; catalogue `public-frontier.9`.

## Exact question and result

Can the unreviewed branch-aware matched train gap `g=0.0071` be carried through the existing Section 171 endpoint and its two outer-energy alternatives without importing the separate `g=0.0050` numeric endpoint?

Assume the frozen `0.0071` report's full-core Type-II hypotheses and matched all-train floor, the existing Section 171 analytic reduction, and the physical propagation report's exact full-core low-`t` domain including `R_F=o(D)`, its outer-tooth/long-side dichotomy, tooth apex injectivity, and long-side directional-energy identity. Write

```text
s = sqrt(pi/(2 sqrt(3)))
C146 = 4/9 (pi+s)
epsilon = 0.0023374
t0 = C146+epsilon
C(g) = 2s+g
delta(g) = (9 epsilon/2-g)/2.
```

The Section 171 numeric certificate still closes at `g=0.0071`: `delta=0.00170915`, and a freshly derived cube-root upper endpoint `1.111` gives a positive outward-rational endpoint margin greater than `0.18`. This is conditional on the prior analytic reduction; it does not independently prove that reduction. The old `1.3025` cube-root bound, if copied unchanged, makes the margin negative by more than `0.0093`; the negative control is included in `verify.py`. The predecessor `g=0.0050` calculation had `delta=0.00275915` and margin greater than `0.000027`.

At the low-residual boundary `t=t0`, the physical outer-boundary quantity is

```text
B(g) = [5 pi + 2 C(g) - 10 t0]/3 > 0.4376350385.
```

The two source branches therefore give the following conditional endpoint floors:

- Shallow-tooth branch, with `eta=1/15`: distinct inward contacts `E_pen/D > 0.20599889-o(1)`.
- Shallow-tooth branch, with `eta=3/50`: `E_pen/D > 0.20457460-o(1)` and the aggregate inward projection exceeds `0.14698525-o(1)`.
- Long-side branch, with `beta=pi/6`: distinct near-tangent contacts `E_tan/D > 0.21243888-o(1)` and aggregate absolute tangent projection exceeds `0.18397747-o(1)`.

These branches are retained separately; under their stated endpoint hypotheses, at least `0.20599889 D-o(D)` distinct contacts lie in one of the two families. The predecessor branch floors were `0.19742389` for the tooth count and `0.20782023` for the long-side count. No KKT multiplier, stress floor, source-wide finite endpoint, or strict diameter decrease is derived.

For `x=t-t0>=0`, the imported low-`t` identities vary as `delta(x)=delta(0)+9x/4` and `B(x)=B(0)-10x/3`. The verifier records the corresponding branch functions. The displayed endpoint constants apply at `x=0`; the lower bound `t>=t0` alone gives no upper bound on `x`, so these constants are not claimed uniformly for every full-core source.

More explicitly, the two count floors are

```text
E_pen(eta,x)/D >= E_pen(eta,0)/D - (5/3 + 9/(8 eta)) x - o(1)
E_tan(x)/D      >= E_tan(0)/D      - (5/3 + 9/(8(1-sqrt(3)/2))) x - o(1).
```

The respective direction sums retain the tooth projection `Y_eta` and tangent projection `sqrt(3)/2` as in the source formulas.

For example, if a separate canonical low-`t` argument supplies `x<=0.01`, the same branch formulas give `E_pen(1/15)/D>0.0205-o(1)` and `E_tan/D>0.111-o(1)`. Thus either branch contains more than `0.0205D-o(D)` distinct contacts throughout that window. The current Section 171 lower bound does not itself supply this upper window; the verifier treats it as an explicit conditional input.

## Hypotheses and limits

The matched gap and the separate physical outer-energy propagation are both unreviewed, noncanonical inputs. The geometric assumptions retained from the physical report are the full-core Type-II branch with `R_F=o(D)`, its exact low-residual outer-tooth versus long-side dichotomy, shallow-tooth apex injectivity on the tooth side, and the directional-energy identity on the long-side route. The canonical prerequisites and source hashes are declared in `SOURCES.json`.

The calculation does not handle the macroscopic-container branch or propagate complement-rhombus incidence. It does not construct a finite configuration. All original source labels, including contact isolates, remain in scope as background hypotheses; no source point is deleted or moved. Since no endpoint is constructed, there is no claim that all lower or upper pair constraints have been checked.

**Stop condition:** without a canonical upper bound on `x`, report only the parameterized low-`t` branch floors and the explicit `x<=0.01` conditional. Do not turn the boundary values at `x=0` into a uniform source-wide contact or stress conclusion.

## Falsification and reproduction

`verify.py` uses exact `Fraction` arithmetic for every asserted bound, checks the new cube-root endpoint and positive Section 171 margin, reproduces the `g=0.0050` residual as a branch control, evaluates both outer-energy branches, and verifies that reusing the predecessor's coarse cube-root bound fails at `g=0.0071`.

```bash
python research-packages/e99-pass-20261018-local-07/verify.py
python scripts/research_package.py --package research-packages/e99-pass-20261018-local-07 --check-only
```

The package checker verifies metadata only. The arithmetic checker does not prove the imported analytic lemmas, asymptotic source extraction, or global minimality.

## Open next question

Can either directional contact family be converted, under the canonical full-core Type-II hypotheses, into a uniform positive lower bound on diameter-stress mass that includes contact-isolated labels and every active and inactive upper pair? That exact quantity could decide whether the outer-energy alternative reaches the current diameter-bracing gate. Keep the dependence on `x=t-t0` explicit; either a source-derived upper bound on `x` or a counterexample to a uniform branch floor would settle whether the endpoint constants can be used beyond `x=0`. First reconstruct the exact low-`t` interval from its source report; the current `0.0071` substitution supplies only the lower endpoint.

## Predecessors, overlap and credit

The package extends the frozen `0.0071` train-gap report and its verifier, and the separate `0.0050` Section 171 certificate plus physical boundary report. It recomputes the downstream endpoint rather than relabeling the predecessor. The private overlap refresh at `2026-10-19T04:52Z` covered all open PR titles/bodies, Issues and Discussion bodies/comments/replies; it found no matching live Target C handoff. Discussion #83's four requests concern other tasks. Its only open PR is #102 on an unrelated Target A Hall-overlap result. The catalogue's `existing_checks` is empty, so prior-check coverage remains unknown outside the exact pinned files and commands here.

Prepared with AI assistance by OpenAI Codex (GPT-6 Luna). The arithmetic composition and checker are new Apache-2.0-compatible work; prior reports retain their original attribution and lifecycle. An independent audit of this exact package has not occurred. Required repository-wide theorem-certificate replay is deferred to the merging agent.
