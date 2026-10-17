# Target C-II — collapsed support-six blocks require global corridor interaction

**Date:** 2026-09-18  
**Status:** proved candidate; scoped global reduction, theorem-state authority unchanged  
**Scope:** the collapsed degree-pure support-six host, under the internally-disjoint corridor model  
**Certificate:** `research/verify_target_c_support6_collapsed_corridor_nonplanarity_2026_09_18.py`

The local collapsed certificate leaves six exceptional pentagons with host graph

\[
R=K_6\setminus\{03,14,25\},
\]

and one outside/activated train at each pentagon. If every stopped train could be
contracted to an internally disjoint corridor in one planar cellulation, the contracted
train-incidence graph would have the six pentagon hosts plus one outer/activated host,
with

\[
12+6=18
\]

distinct edges. A simple planar graph on seven vertices has at most

\[
3\cdot7-6=15
\]

edges. Therefore the internally-disjoint corridor model is impossible. In a general
position drawing of the contracted skeleton, deleting one edge at each crossing leaves
a simple planar graph, so at least three crossing events are required.

There is a sharper scoped subcase. If all six outside trains terminate at the same
outer host, their common projective direction makes them pairwise noncrossing. Their
six pentagon endpoints therefore inherit one cyclic boundary order. The twelve
internal trains are then chords on six boundary vertices. Exhausting all `6!` cyclic
orders gives a minimum of six alternating internal chord crossings. The verifier checks
this exact finite enumeration. This six-crossing statement is conditional on the
all-outer common-host model; it does not apply when the six anchors attach to several
activated faces.

The same enumeration is a hostile regression for the next tempting shortcut: every
minimum six-crossing order has a triangle-free crossing graph. Thus the already known
triangle-free train-crossing condition does not, by itself, eliminate the minimum
all-outer interaction pattern.

In every one of the 48 minimum orders, six internal trains have crossing degree two
and the other six are isolated; the nontrivial crossing graph is one `C_6`. For the
fixed collapsed `+++---` label word, 36 orders have two cyclic sign transitions and
12 have six. This is an exact classification of the minimum pattern, not an
impossibility result.

There is a further exact colour split. In the 36 two-transition orders, the six
crossings consist of two cross-sign/cross-sign pairs and four cross-sign/same-sign
pairs, with no same-sign/same-sign pair. In the 12 alternating six-transition
orders, all six crossings are between same-sign internal trains; there are no
cross-sign crossings. This is the finite interaction pattern that global corridor
integrability must still exclude or realize.

The dependency chain is:

```text
collapsed support-six incidence
  -> K6 minus a perfect matching plus six outside trains
  -> contracted skeleton has V=7, E=18
  -> E>3V-6
  -> at least three genuine corridor interactions
```

This is a global reduction, not an exclusion of the collapsed branch. The contraction
hypothesis is deliberately stronger than the current audited train formalism: distinct
complete trains can share rhombi or interact at crossing cells, and the local
certificate does not determine that global routing. The result therefore cannot be
used to claim that the collapsed branch is impossible.

## What it isolates

Any actual global collapsed realization must pay for at least three nontrivial train
interactions beyond the local six-pentagon closure equations. The next finite task is to
combine this lower bound with the fact that the complete-train crossing graph is
triangle-free and with the common parallel direction of the six outside anchors.
Possible outcomes are an exact crossing-pattern exclusion, a forced additional source
point/contact, or a diameter/KKT payment. None is asserted here.

The auxiliary genus-two side-pairing in the local realization is not used: it is only a
local quotient and is not identified with the physical plane. This note instead states
an explicit conditional obstruction for the stronger, physically interpretable
internally-disjoint corridor model.

**Disposition:** proved candidate at scoped reduction; positive-slack collapsed branch
and C-II remain open.
