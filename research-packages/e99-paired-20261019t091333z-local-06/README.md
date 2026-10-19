# Destination audit of inverse-phase face-tail correction

This proof-only audit checks the corrected Audit.236 sequence exclusion at
destination main `7d0a450fe66991036541023f95c44c064a04b6a8`. Its conditional
claim passes under the two stated global hypotheses and canonical inputs. The
full reconstruction, pin list, scope, and limitations are in [AUDIT.md](AUDIT.md).

The finite script checks pinned source bytes and the displayed patch-exponent
ledger only. It does not verify the analytic theorem, extract the phase/tail
hypotheses, or prove C-II closure. The candidate remains `audited-working`; no
state promotion is proposed.

## Falsification target

The delicate implication is that a diagonal face cutoff can control both the
additive tail and the cubic routing constant, after which radius-`D^(3/4)`
patches force `q=o(D)`. A counterexample to the routing estimate, a failure of
one shared lattice translate within a patch, or a nonvanishing patch exponent
would falsify this implication.

## Open next question

The next theorem must extract both the global inverse-phase and vanishing
face-tail hypotheses from every sufficiently large canonical triangle-free
global minimizer, or construct a source-specific competitor without them. This
can change the actual diameter-endpoint count `q` by excluding the conditional
branch or bypassing it. The changed hypothesis is source extraction; either
outcome enables progress beyond this conditional sequence exclusion. First
action: derive a source-wide estimate for the actual-contact edge-direction
errors and the augmented-face tail from the canonical ZF data. The blocker is
that the current candidate assumes both globally and gives no source extraction.

OpenAI Codex (GPT-6 Luna, xhigh) produced this independent audit note and the
limited pin/exponent checker; it did not author the audited proof or its prior
checks. No third-party paper text was copied.
