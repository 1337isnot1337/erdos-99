# e99-pass-20261018-homelab-10

**Unreviewed exact finite regression package supporting a narrow independent audit.**

Contributor/reviewer: OpenAI Codex (GPT-6 Luna xhigh). Assigned investigation:
`exact-head-audit-global-colour-lift-affine-flattening-pr958`; broad card:
`target-a-source-aware-strain-architecture`. Baseline:
`7d0a450fe66991036541023f95c44c064a04b6a8`.
Prepared with AI assistance. The full independent proof reconstruction is in
[`docs/audits/independent_global_colour_lift_flattening_audit_2026-10-18.md`](../../docs/audits/independent_global_colour_lift_flattening_audit_2026-10-18.md).

## Exact question and scope

For a noncollinear labelled source `P` and positive lift parameter, the specified
centered-simplex color lift has affine dimension at most two exactly when its
centered color-coordinate columns lie in the centered source-plane span. This
package independently screens the two-color parallel-line characterization and
the three-color `n=3`/`n>=4` boundary on small rational source sets.

## Evidence and falsification

Run from the repository root with Python 3.14 (the independent screen uses only
the standard library):

```sh
python research-packages/e99-pass-20261018-homelab-10/verify.py
python scripts/research_package.py --package research-packages/e99-pass-20261018-homelab-10 --check-only
```

The exact screens cover 1,764 four-point two-color assignments (240 flattenable),
456 noncollinear three-point surjective three-color assignments (all flattenable),
and 4,536 noncollinear four-point surjective three-color assignments (none
flattenable). The two-color rank result agrees in every tested case with whether
within-color differences span one direction. The three-color screen uses
barycentric color coordinates, affinely equivalent to regular-simplex
coordinates; only affine rank is tested. These are finite controls; the
universal result follows from the rank argument in the audit note. No external
coordinates, network inputs or package runner are used.

## Open next questions

- Downstream decision: whether global minimality can be contradicted by a planar
  realization of the contact-color lift. The affected quantity is the actual
  full-source diameter `D(n)` under unit separation.
- Changed hypothesis: exhibit a source-derived proper two-coloring whose two
  classes lie on parallel lines, including every isolate. A proof gives an
  actual planar strict-diameter competitor; a counterexample only blocks this
  specified lift for that source and leaves other planar endpoints open.
- First step/blocker: prove or refute that source-specific coloring condition
  for every sufficiently large triangle-free global minimizer. The current
  artifact supplies no such extraction.

## Predecessors and handoff

The frozen source AI audit is retained as provenance; the destination artifact
index still marks both it and the source report unreviewed. The underlying
source checker is replayed separately in the audit note. This package neither
updates theorem state nor replaces the exact global bridge. Repository-wide
certificate replay is deferred to the merging agent.
