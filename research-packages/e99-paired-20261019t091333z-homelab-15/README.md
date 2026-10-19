# Independent audit of PR #138: Oler remainder and envelope obstruction

**Verdict: conditional pass for the published implication.** At the exact
published head `d17d45aebb04811c920d03f46c50a2337fe19a98`, I reconstructed the
signed-remainder identity, its implication from PR #117's phase inequality (1),
and the strict obstruction to verifying the separate-envelope condition. I found
no algebraic or finite-control defect. The source-specific joint remainder for an
actual global source remains unbounded, so this does not prove the locked branch,
Target A, or Level I. This audit is evidence for a maintainer; it changes no claim
lifecycle or theorem state.

## Exact question, hypotheses, and affected quantity

The audited candidate asks whether PR #117's phase-integrated sink inequality can
be written as an exact signed source-area remainder and whether separate Oler
envelopes can certify that remainder. Its hypotheses retain the triangle-free
global source `A subset H=conv(A)`, every one of its `N` labels, the actual
Section-165 plateau response `X*` with hull `K*`, `d=diam(K*)`,
`t=(D-d)/2>1`, the Section-155 common placement, the actual locked three-channel
unit-contact fan `Sigma`, and a Section-102 admissible basis at each generic phase.

The exact downstream quantity is

```text
Xi_Sigma - j_* - |T_Z|.
```

A positive source remainder is a sufficient condition for this integer residual
to be nonnegative at some generic phase, which closes the actual-response locked
branch through Section 175. Failure of the sufficient test is inconclusive.

**Candidate lemma before search.** Under the hypotheses above, set
`L=K*+tB`, `B0=E[d_int+t_Sigma]`,
`A_Sigma=area(N_1(|Sigma|))`,
`Delta_H=area(H)-area(L)`, and
`Omega_H=area(H)+(a0/2)per(H)-a0(N-1)`, where `a0=sqrt(3)/2`.
Reconstruct the exact identity for the phase threshold and prove that its
separately bounded version is impossible using only the stated Oler envelopes.
The falsification experiment is an independent exact replay of every pinned
finite control plus a same-cardinality strict-diameter competitor for each
triangle-free deleted-color source. Stop if the argument does not control the
joint signed remainder on an actual Section-165 source/response pair.

## Proof reconstruction

PR #117 states, for the same phase-dependent integer residual,

```text
E[Xi_Sigma - j_* - |T_Z|]
  >= (area(L)-A_Sigma)/a0 - N + E[d_int+t_Sigma].       (1)
```

The implication from (1) is an integer argument: if the right side is greater than
`-1`, the expectation of the integer residual is greater than `-1`; it cannot be
at most `-1` at every generic phase. Thus some generic phase has residual at least
zero. Multiplying that strict test by `a0` gives

```text
area(L) + a0*B0 > a0*(N-1) + A_Sigma.
```

Substituting the definitions into the candidate's signed remainder gives exactly

```text
R_exact
 = Omega_H - Delta_H - (a0/2)*per(H) + a0*B0 - A_Sigma
 = area(L) + a0*B0 - a0*(N-1) - A_Sigma.
```

The cancellation is exact: the `area(H)` and source-perimeter terms disappear.
Therefore `R_exact>0` is exactly the sufficient test derived from (1), with the
actual fan-neighborhood area retained. For a connected graph of `e` unit edges,
start with one unit disk and add edges along a spanning tree. Each new unit segment
adds at most its capsule area minus the already-covered endpoint disk, namely `2`.
Extra edges cannot increase this bound. Hence `A_Sigma<=pi+2e`, and the candidate's
condition

```text
Omega_H + a0*B0 > Delta_H + (a0/2)*per(H) + pi + 2e            (B)
```

is a stronger sufficient condition than `R_exact>0`.

Under Section 155, both `H` and `L` have diameter `D`,
`area(H)<=pi D^2/4`, and
`area(L)>pi D^2/4-(sqrt(3)*pi/4)D`. Thus
`Delta_H<sqrt(3)*pi D/4`. Also `per(H)<=pi D`, so (B) is implied by

```text
Omega_H + a0*B0 > (sqrt(3)*pi/2)D + pi + 2e.                  (C)
```

I checked the cited [Klain paper](https://faculty.uml.edu/dklain/Klain-Isoperimetric.pdf),
Section 4, equation (6): it states the Bonnesen bound for compact convex planar
sets, which covers the convex bodies `H` and `L` used in Section 155.

The candidate's coarser two-sided estimate is also valid: the Hausdorff bound
`d_H(H,L)<=3eta(D)` gives `H subset L+3eta B` and
`L subset H+3eta B`. Steiner's formula and
`per(H),per(L)<=pi D` bound either positive area difference by
`3pi D eta(D)+9pi eta(D)^2`. The signed one-sided estimate above is the relevant
bound for (B).

For a global optimum, Section 114.2 gives
`N-1>D^2/c`, `c=2sqrt(3)/pi`; multiplying by `a0` yields
`a0(N-1)>pi D^2/4`. Combining this strict bound with the isodiametric and
Cauchy perimeter bounds gives

```text
0 <= Omega_H < (sqrt(3)*pi/4)D.
```

For each Section-102 admissible basis, `d_int<=m*-|Z|`; the fan is unicyclic, so
`t_Sigma<=|V(Sigma)|=e`. Phase integration gives
`E|Z|=area(K*)/a0`. Oler on `X*` then gives

```text
B0 <= m* - area(K*)/a0 + e
   <= per(K*)/2 + 1 + e
   <= pi*d/2 + 1 + e
   <= pi*D/2 + 1 + e.
```

Consequently

```text
Omega_H + a0*B0
 < (sqrt(3)*pi/2)D + a0*(1+e)
 < (sqrt(3)*pi/2)D + pi + 2e.
```

The final gap is `pi+2e-a0(1+e)>2+e>0`, using `pi>3` and
`a0=sqrt(3)/2<1`. This proves that (C) cannot be verified from those independent
upper bounds. It does **not** prove `R_exact<=0` for any actual source.
The correlation among `Omega_H`, `Delta_H`, `B0`, and `A_Sigma` remains available
to a stronger joint argument.

## Adversarial replay and finite controls

All five reviewed files were read from exact Git head
`d17d45aebb04811c920d03f46c50a2337fe19a98`; their SHA-256 and Git blob IDs matched
the assignment's immutable `source-pins.json`. The source `verify.py` passed.
The reviewed package SHA-256 values were README `f96ef081c91c7c3779c3b8ec99109bb7722a6d3460d39b64509d632974b3ac52`,
SOURCES `e34176a31310b6ccc0a427300b8e1048ceb378a4fb7352bb0560ae534ca2e6c6`,
TASK `61c6300f349854d15a60801e51478747809391cfa3c28f71d33fc1dd1a9afaff`,
VERIFY `2d660ad3f669f863bef079fb65d3494d29726a10cf0972441e0b9ed09167b271`,
and verifier `dbb68cf395cd7562dbaf5fb3761e5abb451aad39d7cd2582520a4c5103610774`.
This independent `verify.py` uses only the Python standard library and separately:

- Reconstructs the triangular-lattice patches as sets, computes their hulls in an
  exact integer affine coordinate system, checks pair distances, counts, exact
  hull area/perimeter and the full-patch Oler slack for radii 1 through 6.
- Certifies the retained two-residue sources for radii 3 and 6 are triangle-free:
  every unit contact switches between their two retained residues, so the contact
  graph is bipartite. It checks the exact populations 25 and 85 and slacks
  `6sqrt(3)` and `21sqrt(3)`.
- Independently checks the `M=6`, `k=3` Steiner expansion
  `Delta_H=-54+(81/2)sqrt(3)-9pi`. This signed gap is strictly negative because
  `sqrt(3)<2` and `pi>3`; the control correctly tests the signed expression.
- Supplies same-cardinality triangle-free square-grid competitors, confirming
  both deleted-color controls are not global diameter optima. For 25 labels, the
  `5x5` square grid has diameter squared `32<36`. The integer disk
  `x^2+y^2<=26` contains 89 labels; any 85 have pairwise separation at least one,
  no unit triangle (the unit-contact graph is bipartite by parity), and diameter
  squared at most `104<144`.
- Checks the signed-remainder cancellation and the strict `2+e` lower bound for
  `e=0,...,100`; the proof above establishes the bound for every integer `e>=0`.

The finite controls do not satisfy the large-cardinality Section-155 hypothesis
`D>16sqrt(3)` (`D=6` or `12`), and the inner triangular patch is not a
triangle-free optimum. They provide source-side arithmetic controls only. No fan,
Section-102 basis, or actual plateau response is represented.

## Reproduction

With the repository's provisioned Python 3.14 environment:

```sh
git show d17d45aebb04811c920d03f46c50a2337fe19a98:research-packages/e99-macbook-20261019t054318z-01/verify.py > /tmp/pr138-pinned-verify.py
sha256sum /tmp/pr138-pinned-verify.py
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python /tmp/pr138-pinned-verify.py
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python research-packages/e99-paired-20261019t091333z-homelab-15/verify.py
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python scripts/research_package.py --package research-packages/e99-paired-20261019t091333z-homelab-15 --check-only
```

The first hash must be `dbb68cf395cd7562dbaf5fb3761e5abb451aad39d7cd2582520a4c5103610774`.
The package metadata command checks hashes and declarations only; it executes no
proof or certificate command.

## Predecessors, live status, and limits

The inspected route remains `docs/targets/target-a/README.md`; theorem state is
`2026-10-15.publication.2`, priority is `public-frontier.3`, and catalogue is
`public-frontier.9`. Target A and Level I remain open; C-I is closed and C-II open.
The published PR #138 is still open at the pinned head and had no live comments or
reviews at audit time. Discussion #83 handoffs concern the distinct PR #87 and #89
fan-ledger scopes. The current open PR #141 audits PR #117's phase inequality at
its exact head and records a conditional pass with a measurability clarification
for the Section-113 matching. It is a separate artifact and does not promote the
phase inequality's canonical lifecycle. This audit uses PR #117 equation (1) as
the explicit premise of PR #138's implication; it does not duplicate PR #141's
proof/checker audit.

PR #87's seed-63 all-basis full-tube ledger and PR #89's seed-66 fixed-phase
control are regression predecessors. PR #117 adds the actual-source phase
criterion. PR #138's distinct contribution is the signed source-area remainder
and the obstruction to its separate-envelope route. None supplies a source-specific
lower bound for `R_exact`.

One source-inventory gap is nonmathematical: PR #138's `SOURCES.json` does not
list `docs/targets/target-a/03-source-response.md`, which contains Section 114.2,
the strict translated-lattice bound used in the `a0(N-1)>pi D^2/4` step. Its
baseline commit is exact and the canonical statement is present there, so I could
check the implication; this audit pins that file in its own `SOURCES.json`. Adding
the missing source pin would make PR #138's declared input list match its proof
dependencies more completely.

The remaining lemma is to prove `R_exact>0` for an actual Section-165 source and
response, or to prove a source-specific obstruction to that joint lower bound. The
changed hypothesis must retain the actual source `A,H,N`, plateau response `X*`,
fan, and basis counts; a failed sufficient test alone is inconclusive. Either a
successful lower bound or a precise obstruction changes only the actual-response
locked-branch decision through `Xi_Sigma-j_*-|T_Z|`. No result here closes the
zero-slack branch or the universal global-minimizer quantifiers.

No external text or private dependency was used. This audit and its independent
checker are offered under Apache-2.0. Reviewer: OpenAI Codex, GPT-6 Luna xhigh;
the reviewer reconstructed and checked the published result independently and
did not edit the pinned PR #138 bytes. Required full theorem-certificate replay
is deferred to the merging agent.
