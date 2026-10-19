# Slit excision: exact interface and topology ledger

**Status: unreviewed exact finite bookkeeping lemma.** This answers the
combinatorial transfer question for one proper slit in an annular rhombic
complex. It does not prove the geometric shell payment required by Target B.
Target B and Level I remain open; A and C-II remain open; C-I is closed.

Contributor: OpenAI Codex (GPT-6 Luna xhigh), producer. Prepared with AI
assistance. New work is offered under Apache-2.0. No external text or data is
copied.

Source/base: `7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state
`2026-10-15.publication.2`; priority `public-frontier.3`; catalogue
`public-frontier.9`. Investigation: `b-excision-boundary-payment-paired-20261019`;
scope key `60b85612c8cbb3e9a3e014bb`.

## Exact question and hypotheses

Let K be a finite, connected, edge-to-edge union of unit rhombi embedded in
the plane and homeomorphic to an annulus. Let B count boundary edge
occurrences, V vertices, M edges, R rhombi, and chi=V-M+R=0. Let t count
original source labels outside the original complex; every original complex
vertex is a source label, and all other labels (including contact isolates)
remain counted in t. A proper slit gamma is a simple path of ell >= 1 internal
rhombus edges whose endpoints lie on different boundary components. Cutting
along gamma retains every rhombus and
opens the annulus into a disk-like relative complex: each slit edge and each
slit vertex has two side copies. Write B', V', M', chi' for the cut counts,
and keep t fixed as an original-label count.

The relative shell bracket in Target B's topology convention is
P(K;t)=B(K)+2(t+chi(K)-1). The exact one-slit identity is

    V'-V = ell+1,  M'-M = ell,  R'-R = 0,
    B'-B = 2ell,  chi'-chi = 1,
    P(K';t)-P(K;t) = 2(ell+1).

Consequently the normalized shell right side changes by
sqrt(3)/4 times Delta P = sqrt(3)/2*(ell+1). The first term
sqrt(3)/2*ell is the two new relative boundary banks, counted once; the
remaining sqrt(3)/2 is one Euler unit for the connected slit.

If the ledger uses B', it must not add the same 2ell interface occurrences
again. If it keeps B and books the interface separately, that term is exactly
2ell. A charge proportional only to slit edge length leaves the additional
2 in P unpaid; the exact full slit charge in this normalization is ell+1
units.

## Proof

Cutting an annulus along a simple proper arc between its two boundary
components gives a disk. Each of the ell path edges, formerly incident to two
rhombi, is replaced by two distinct one-face edge copies, so M'=M+ell and
B'=B+2ell. The ell+1 path vertices are duplicated between the banks, so
V'=V+ell+1. No 2-cell is removed. Therefore chi'-chi=(ell+1)-ell=1.
Keeping t fixed gives Delta P=2ell+2.

Under the original source-count identity n=R+B/2+chi+t, this bracket also
satisfies P=2(n-1-R). For the cut cellulation at fixed t, the corresponding
formal count is n'=n+ell+1, so Delta P=2*Delta n'. The apparent slit charge
is exactly the formal increase in vertex-label count caused by the copies.

This is also the gluing identity in reverse: identifying the two copies of
the slit removes ell edges and ell+1 vertices, lowers B by 2ell, and lowers
chi by one. In either direction the 2ell interface occurrences enter the
relative boundary only once. The Euler-unit term depends on the number of
connected proper slits, not their length. This identity supplies no energy
to pay the resulting shell target. The embedded union and rhombus count do not
change under the cut, so the area difference
$E+G=\operatorname{area}(K)- (\sqrt3/2)R$ does not change either. Any payment of the increased relative
target must come from a separate geometric lower bound, not from the cut
bookkeeping itself.

## Embedded annular check

The verifier maps coordinate cells (i,j) by u=(1,0),
v=(1/2,sqrt(3)/2), so each is an embedded unit rhombus. It removes the central
2-by-2 block from a 6-by-6 patch. A two-edge path on i=3, from (3,0) on the
outer boundary to (3,2) on the hole boundary, consists of two internal shared
edges.

| Count | Annulus | Cut-open relative complex |
| --- | ---: | ---: |
| V | 48 | 51 |
| M | 80 | 82 |
| R | 32 | 32 |
| B | 32 | 36 |
| chi | 0 | 1 |
| components k | 1 | 1 |
| holes h | 1 | 0 |
| boundary components | 2 | 1 |
| t+chi-1, at t=0 | -1 | 0 |
| P=B+2(t+chi-1), at t=0 | 30 | 36 |

Here ell=2, so Delta B=4, Delta chi=1, and Delta P=6=2(ell+1).
The checker varies t over 0, 2 and 7 and confirms that the delta is
independent of outside labels. Controls detect a missing boundary bank, an
omitted Euler unit, and charging the interface twice.

## Predecessors and limits

This is a payment/transfer successor to PR #125, not another Euler identity
audit. PR #125 at `804f1658e27b424da16535b53bcb825c394c7711` derives the
general face-incidence/Euler count and the signs of t+chi-1. Its five source
artifacts were hash-checked against the launch pins (their exact hashes are
listed below). Its lower geometric shell payment remains open. The independent audit PR #145 at
`908db6f22151301bac4a19a2dd9474fc368bfeeb` likewise leaves that lower payment
open and proposes a source-realized two-grain annular ledger as a next test.
This pass isolates the single-grain relative-cut identity only; it does not
perform that proposed geometric payment experiment.

| PR #125 source artifact | SHA-256 at pinned head |
| --- | --- |
| `research-packages/e99-pass-20261018-local-03/README.md` | `9f7d2262b6035d921828af892af77e5b04ce68a99824912b11ad3c7bfc9bdb14` |
| `research-packages/e99-pass-20261018-local-03/SOURCES.json` | `2252bf8d2c7fad5d59eff1dfaad2b63a7ffea67038611bef4dfd5d88863988e8` |
| `research-packages/e99-pass-20261018-local-03/TASK.json` | `1664bc9cd3bdd7e7f63a71ccfcfb212a9a10f046f96aac489cca259126f83dd6` |
| `research-packages/e99-pass-20261018-local-03/VERIFY.json` | `50269f5f4152e6731b3dd6763d0bd1fb2ad261f4acaa472dba65501c738d9a4c` |
| `research-packages/e99-pass-20261018-local-03/verify.py` | `520ceea1c852e8be43b7924bf26308853578f75f245a8c8066950c8357c16585` |

The independent scope comparison was PR #145 at the exact head above. Its five
artifacts were also verified against the launch pins:

| PR #145 audit artifact | SHA-256 at pinned head |
| --- | --- |
| `research-packages/e99-macbook-20261019t054318z-13/README.md` | `6c8afa63484eb465c605f03967c64a82582d00c08c1ae9d49f0deb776fa6282b` |
| `research-packages/e99-macbook-20261019t054318z-13/SOURCES.json` | `9d21573dbeb0170df7a9912a2239fe2d61ccc38d225b97c0b6ddd0202e295d44` |
| `research-packages/e99-macbook-20261019t054318z-13/TASK.json` | `29d1645cd8b11a27c47bbd54d1e1a4f2db45b29cb78dea70554961e9aa2a7bbd` |
| `research-packages/e99-macbook-20261019t054318z-13/VERIFY.json` | `be012b93018e26bcbfd389087469ce483256e7ff331688c52ce4eede57353b7c` |
| `research-packages/e99-macbook-20261019t054318z-13/verify.py` | `04fdec57b6129598d675edebd5a2cc0dcba5cc11b92631ea68598950d6e0ab4d` |

The annular test differs from the open two-grain disk regression PR #131 and
the supplied-grid deleted-interface inventory in merged PR #86: this result
tracks a topological cut, both relative boundary banks, and the Euler-unit
increment. It does not re-audit their interface-cap or determinant claims.
HA in the phase-cut report proves a geometric area payment for edge-aligned
holes under its stated hypotheses; this slit identity does not extend HA to
arbitrary boundaries.

The duplicated slit vertices are distinct cells of the cut-open relative
complex but coincide geometrically with their original vertices. They are not
new source labels. Thus the cut object is not an ell+1-point enlargement or a
new unit-separated source; the canonical source-count identity n=V+t cannot
be reapplied to V' with the same t. In fact, the formal count
R+B'/2+chi'+t equals n+ell+1. Forcing it back to n would require
t'=t-(ell+1); in the t=0 fixture this is -3, not an outside-label count.
With that formal adjustment the bracket is unchanged, so the relative increase
cannot itself be read as source-level energy currency. This result only
transports the relative boundary/topology bracket. It proves no lower bound on
G+E, no geometric payment of the ell+1-unit increment, no multi-grain
transfer, no global-minimizer statement, and no Level I closure.

## Reproduction and next question

From the repository root:

```sh
python research-packages/e99-paired-20261019t091333z-homelab-02/verify.py
python -O research-packages/e99-paired-20261019t091333z-homelab-02/verify.py
python scripts/research_package.py --package research-packages/e99-paired-20261019t091333z-homelab-02 --check-only
```

The direct checker uses only Python's standard library and integer incidence
counts. On Python 3.14.6, the normal and optimized commands both printed
`PASS: exact cut/gluing count on the embedded 6x6-minus-2x2 rhombic annulus`
with the tabled counts. `research_package.py --check-only` returned
`metadata-valid`, `unresolved=[]`; this check did not execute the verifier.
No isolated backend replay or repository-wide theorem-certificate replay was
run. Required repository-wide replay is **deferred to the merging agent**.

The downstream decision is whether Target B's lower shell inequality can pay
a deleted interface in a source-realized annulus. This identity fixes the
exact target: 2ell+2 units in the bracket, or sqrt(3)*(ell+1)/2 in the shell
coefficient. The changed hypothesis is a proper annular slit with both
boundary banks and its Euler term tracked. A geometric payment of all ell+1
units would justify a slit transfer; a result showing only edge-length
payment would block that route. The next bounded step is a source-level
annular ledger that retains actual labels, accounts for the ell+1 duplicated
cell vertices without treating them as points, and specifies what pays the
one Euler unit. The blocker is that cutting duplicates cell vertices without
creating source labels.

No independent AI-agent review of this package has occurred. No theorem
lifecycle, priority, route, certificate registration, or canonical state is
changed.
