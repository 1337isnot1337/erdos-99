# Balanced-triad obstruction to a rigid-support relay

**Classification:** unreviewed exact finite geometry and conditional source-interface lemma. This result does not change theorem state.

**Baseline:** `7d0a450fe66991036541023f95c44c064a04b6a8`  
**State / priority / catalogue:** `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`  
**Task:** `frontier-target-a-source-aware-strain-architecture-20261018`  
**Contributor:** OpenAI Codex, GPT-6 Luna. AI assistance produced the proof note and exact checker; no independent mathematical audit has occurred.  
**License:** Apache-2.0, subject to the repository contribution terms.

## Candidate question and downstream quantity

Can a nonlocal relay widen a small gap by translating one rigid support component
relative to a fixed exterior source interface, with every source label retained?
The exact test is a translated support component containing a boundary label `p`
that has three fixed exterior unit contacts whose contact normals are equally spaced
by `120` degrees. The motion is a common translation `t` of the whole component;
all three exterior labels stay fixed.

The quantity this architecture could change is the local support cost `W(d)` in
Sections 157 and 160, and hence the support term used toward the Target A source-to-
Schur endpoint. A positive feasible translation branch might supply a new gap step.
The falsification test is the exact first-order contact cone and a full pair audit
of the smallest source realizing this interface. The stop condition is failure of
the identity-branch motion at a retained source label; a local packing gain without
an embedding into a globally derived monomer domain cannot change the canonical
Schur or diameter endpoint.

## Exact interface lemma

Let `p` be a point of a rigid translated component, and let `q_0,q_1,q_2` be fixed
source labels with

\[
|p-q_i|=1,\qquad n_i:=p-q_i,\qquad
|n_i|=1,\quad \sum_i n_i=0,\quad n_i\cdot n_j=-\tfrac12\ (i\ne j).
\]

Then every feasible common translation `t` of length `0<|t|<1` violates at least
one of the three source lower bounds. In particular, the identity-branch feasible
translation cone at this exterior interface is `{0}`.

**Proof.** Put `r=|t|` and `u=t/r`. The three numbers `x_i=n_i·u` satisfy
`sum x_i=0`; the identity `sum_i n_i n_i^T=(3/2)I` for a unit 120-degree triad
gives `sum x_i^2=3/2`. Also `x_i in [-1,1]`. If every `x_i` were at
least `-1/2`, then `(x_i-1)(x_i+1/2)<=0`, so
`x_i^2<=x_i/2+1/2`. Summing gives `3/2<=3/2`; equality forces every `x_i` to be
either `1` or `-1/2`, and the zero-sum condition then forces the values
`(1,-1/2,-1/2)` up to permutation. Thus some `x_i<=-1/2`. For that fixed exterior
label,

\[
|p+t-q_i|^2-1=|t|^2+2n_i\cdot t
\le r^2-r<0,
\]

contradicting unit separation. This is an exact endpoint argument, not only a
first-order relaxation. `\square`

## Smallest full-source pair audit

Take the four labelled points

\[
p=(0,0),\quad q_0=(1,0),\quad
q_1=(-1/2,\sqrt3/2),\quad q_2=(-1/2,-\sqrt3/2).
\]

All six squared distances are recorded by the proof: `|p-q_i|^2=1`, and
`|q_i-q_j|^2=3`. Thus the unit-contact graph is the triangle-free star `K_{1,3}`;
the three leaf pairs are all actual diameter pairs, and the source diameter is
`D=sqrt(3)`. There are no omitted labels or contact isolates in this finite fixture.

The common-translation lemma already blocks every nonzero `|t|<1` using the lower
bounds. In the four-label fixture the complete endpoint ledger rules out larger
translations too. For `r=|t|>0`, `u=t/r` and `x_i=n_i dot u`, the three lower bounds
give `x_i>=-r/2` for every `i`. Since some `x_i<=-1/2`, this forces `r>=1`. The
upper bounds `|p+t-q_i|^2<=D^2=3` give `x_i<=1/r-r/2`; since some `x_i>=1/2`,
they force `r<=1`. Thus `r=1`, when the lower and upper bounds require
`|x_i|<=1/2` for all `i`, contradicting `sum x_i^2=3/2`. Hence the original `p`
is the only point satisfying its three source lower bounds and three diameter upper
bounds while the leaves remain fixed. The checker confirms the positive endpoint
`t=0`, a two-anchor control with a small feasible displacement after deleting one
exterior contact, and the boundary control `t=(-1,0)`, which satisfies every lower
bound but breaks the actual diameter bound (`|p+t-q_0|=2>D`). The controls distinguish
the balanced-triad obstruction from a claim based only on a numerical sample or on
lower bounds alone.

## Relation to the five-block results and limits

Sections 160-162 show that the free aligned-gap five-block translation has an
optimal quartic order, with a sharp symmetric leading coefficient. This package
does not repeat that optimization: it isolates one different source interface and
shows that a rigid component cannot pass through its balanced-triad boundary in the
small-strain regime. It gives no alternative gain and no support-radius improvement.
Open PR #102 proves a separate source-image Hall overlap formula and a full-shore
extension limitation; this package neither uses nor duplicates that result. The
assignment catalogue lists source proposal number `967`, but the current
`docs/research/proposals.json` has no matching entry, so no claim or data from it is
imported here.

The four-point fixture is not claimed to be a global minimizer, a Target A monomer
domain, or an embedding of the five-block template. The conditional interface lemma
applies only when all three anchors are actual retained source labels and are fixed
by the proposed motion. If the motion moves any anchor, the hypotheses change and
all new lower and upper pairs must be audited. A discontinuous endpoint with
`|t|>=1`, rotations, internal deformation, several moving support components,
contact-isolated labels, and global minimizer quantifiers are outside this result.
No bound on `d_sc`, `Delta_Lambda`, `j_*`, or `T_Z` follows; the canonical rank and
Section 175 surplus inequalities remain untouched.

## Reproduction

From the repository root, run the exact checker with Python 3.14 and the standard
library only:

```sh
python research-packages/e99-pass-20261018-local-02/verify.py
python -O research-packages/e99-pass-20261018-local-02/verify.py
```

The checker uses rational arithmetic plus the exact quadratic field
`Q(sqrt(3))`; it verifies the fixture and normal identities, and checks every pair
bound in the finite positive and negative controls. The analytic proof above covers
every translation direction, so the finite controls are not used as proof of the
universal direction bound. Repository-wide theorem-certificate replay is **deferred
to the merging agent**.

## Open next question

Can the actual Target A source be shown to have a gap-facing boundary label with a
fixed balanced exterior contact triad, or can a different multi-component motion
carry that triad while preserving every lower source pair and every active or
inactive diameter upper pair? A proof of the first alternative would exclude this
identity-branch rigid-relay architecture wherever that source motif occurs; a
counterexample or a feasible moving-anchor relay would reopen the architecture and
could affect `W(d)` only after a source embedding is proved. The next step is to
extract the complete contact incidence at an actual gap-facing source label from a
globally derived monomer domain. That source extraction and the full Schur/diameter
payment are the blockers.
