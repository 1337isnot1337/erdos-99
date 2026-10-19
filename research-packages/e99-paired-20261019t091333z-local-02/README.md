# PC3 cannot pay PR147 cross-component virtual mass

**Status:** unreviewed conditional arithmetic and sharp failure of a proposed
scalar payment. This is not a Target B theorem or a global-minimizer example.
Level I and Targets A, B and C-II remain open; C-I remains closed.

**Base/source:** 7d0a450fe66991036541023f95c44c064a04b6a8.
**State / priority / catalogue:** 2026-10-15.publication.2 /
public-frontier.3 / public-frontier.9.
**Investigation:** b-true-deep-payment-hypothesis-paired-20261019.
**Scope key:** 615c0aab2ac81ddf21b90cd8.
**Contributor:** OpenAI Codex, GPT-6 Luna xhigh; derivation, checker and report.

## Exact question and result

PR103 gives a conditional quadratic lower bound on noncrossing determinant mass
between separated, linear-size direction subsets in distinct Section-50
components. PR147's pinned, unreviewed candidate gives a displayed scalable
pure-disk ledger with two retained K_(m,m) components, positive PC1 trim depth,
one deleted interface crossing, and V12 = 2(1+c)m^2 - 1. The downstream
quantity is the cross-component
subsum V12 of the canonical missing-crossing determinant M and its possible
contribution to the Target B endpoint

G + E >= (sqrt(3)/4) B + (sqrt(3)/2)(t + chi - 1).

The added hypothesis tested here is the existing canonical PC3 deep-diagonal
condition, including its deleted-interface charge, applied to every possible
trim of either PR147 grid. It yields no positive PC3 reserve on this family.
The reason is a linear diameter mismatch, not lack of positive trim depth:

* Each component has grid shore sizes m,m, so every trimmed sum M' + b' is
  at most 2m.
* The PR147 trim k = l = m/4 has depth d = m/4 - 2 > 0, while its PC1
  diameter excess (|U+V|-D)_+ is zero.
* The PR147 hull vertices (1-c,-s)m and (-s,1+c)m differ by
  (1-c+s,-1-c-s)m. Since c^2+s^2=1, their distance is
  2m sqrt(1+s). Hence D >= 2m sqrt(1+s) > 2m and
  2D/sqrt(3) > 4m/sqrt(3) > 2m.
* Thus M' + b' - 2D/sqrt(3) is bounded above by a negative constant times m.
  The canonical PC3 positive part is zero for all sufficiently large m,
  uniformly over trims. Its nonnegative deleted-edge penalty only decreases
  the term. The o(D) coherence error cannot remove a fixed linear deficit.

The exact support-corrected scalar payment proposed in PR147 also fails even
after adding the standard PC3 reserve as a unit-for-unit allowance. Its
residual is

Q(m) = V12 - [P12 + (2E + H - J) + (sqrt(3)/2)B]
     = 2(c - 2s + sqrt(3))m^2 - 4sqrt(3)m + sqrt(3) - 2.

For every integer m >= 12 in the family (in particular every allowed multiple
of four), Q(m) > 0 and Q(m) = m^2 + O(m). The exact checker certifies the
algebra and an all-m lower bound. Since PC3 contributes zero, the gap remains
Q(m), of quadratic order. This is a sharp failure of this scalar payment rule
under the PR147 geometry and the existing PC3 hypotheses. It does not refute
the canonical endpoint.

## Reconstructed ledger and precise added condition

Write a0 = sqrt(3)/2. PR147's exact ledger gives

With Section-50 parameters eta = 1/2 and lambda = 1/4, PR147 gives internal
angle defect delta < 2/m^2 < D^(-1/2), while the square interface has defect
pi/6 and is deleted. Since D < 4m, each train's internal degree m is at least
lambda D, so vertex pruning deletes nothing. The interface is the only deleted
crossing: total E_del = E_del,12 = 1, and its determinant is P12 = 1. The two
components have m^2 retained physical crossings each. The complete
cross-component determinant sum is Q12 = 2(1+c)m^2, so the
noncrossing cross mass is V12 = Q12 - P12 = 2(1+c)m^2 - 1. In this
construction all other missing nonzero determinant pairs are precisely these
cross-component pairs, hence global M = V12. The physical determinant mass is
S = 2s m^2 + 1 and S + M = 2(s+1+c)m^2, with total rhombi R = 2m^2 + 1.

The support/boundary ledger is

J = 2(1+c)m^2 = V12 + 1,  B = 8m,  G = m^2 - 1,
E = 2m^2(s - a0) + 1 - a0,  H = (4+2c)m^2 - 2.

Therefore H - J = 2G and

2E + H - J = 2(G + E)
            = 2(1 + 2s - sqrt(3))m^2 - sqrt(3).

The support-turning subtraction removes the quadratic J term exactly. Raw H
cannot be counted again as independent credit. Substitution gives Q(m) above.
The checker uses exact rational arithmetic for c,s and exact signs in
Q(sqrt(3)); its all-m proof uses
1/sqrt(3) < t < 1/sqrt(3)+1/m^2 < 0.585, monotonicity of c(t),s(t), and
1.732 < sqrt(3) < 1.733. It obtains

2(c - 2s + sqrt(3)) > 6425087/6711125,
Q(m) > g(m) = (6425087/6711125)m^2 - (1733/1000)(4m-1) - 2.

Here g(12) = 584259897/10737800 > 0 and
g(m+1)-g(m) >= 228211313/13422250 > 0 for m >= 12.
The negative control verifies that replacing H-J by raw H makes the
candidate ledger appear to pay V12, exposing precisely the spurious quadratic
credit removed by J.

For a component j, the established PC3 term has the form

P3(j) = [ d_j(M'_j + b'_j - 2D/sqrt(3) - o(D))
          - (2/sqrt(3)-1) E_del(H_j) ]_+.

A nonzero quadratic PC3 reserve would require both a linear positive margin
M'_j + b'_j >= 2D/sqrt(3) + kappa D for some fixed kappa > 0 and enough
deleted-edge budget control. PR147 violates the first condition for every
trim, so the two-component sum of the canonical PC3 reserves is also zero
eventually. Even if another source met that threshold, PC3 is a lower bound on
physical rhombus counts; a separate theorem would still have to transfer its
reserve to V12 after support turning is subtracted. No such transfer is proved
here. In precise terms, any PC3-funded repair of this scalar ledger must prove
a source-valid inequality of the form

V12 <= P12 + (2E + H - J) + (sqrt(3)/2)B + T_PC3_to_V12,
0 <= T_PC3_to_V12 <= sum_j P3(j).

The residual forces T_PC3_to_V12 >= Q(m). On PR147 the rightmost PC3 budget is
zero, so this proposed repair is impossible for every allowed m. These lines
state the exact missing transfer and its necessary size; they do not assert
that such a transfer inequality follows from the current route.

There is a different source-level alternative. The canonical pure-disk
global-minimizer shell window gives G + E < (sqrt(3)/4)B = 2sqrt(3)m.
Thus, for this family, requiring membership in the canonical pure-disk
global-minimizer class is enough to exclude the PR147 candidate.
But PR147 has

G + E = (1 + 2s - sqrt(3))m^2 - sqrt(3)/2
      > m^2 - sqrt(3)/2 > 2sqrt(3)m   (m >= 12).

So this family is excluded from the global-minimizer class. This is a
globality-specific exclusion, not a payment of V12 and not a proof that every
source with positive PC1 depth is excluded.

## Falsification, inputs, and limits

The falsification controls are: a trim cannot increase M' + b' above 2m; the
diameter lower bound must be computed from actual listed source points; the
PC3 interface penalty must be retained; and the support term must use H-J,
not H alone. If any exact source value violates these checks, or if the
all-m residual bound fails, the claimed obstruction fails.

**Stop condition:** this pass stops at the proved zero-PC3-reserve and positive
payment-gap conclusions for the pinned family. Reopen only with a changed
source hypothesis that yields an endpoint-ready deep-crossing transfer, or a
global-source theorem that excludes the family while retaining every source
label. Do not rerun the earlier PC1-only enumeration.

The geometry and its full pair-distance/topology ledger remain the unreviewed
PR147 candidate's hypotheses here. This checker does not replay PR147's
geometric verifier, certify unit separation, or prove a canonical-source
extraction. PR103's local virtual-mass implication was reconstructed directly
before reading PR134's audit; that later audit reports the same conditional
implication and does not cover this PC3 threshold. PR86 is the audited abstract
interface inventory and does not supply a train-geometric or virtual-area
transfer. No PC1-only counterexample enumeration is repeated.

Pinned predecessor artifacts:

* PR103 head 4b708e27e9e26f8c163685dfe8b033b6d6369177:
  docs/reports/target_b_two_component_virtual_determinant_payment_2026-10-18.md,
  SHA-256 c755e9508fc28ae6765eef4e704367deef73ff692e4b397f685b011705967882.
* PR134 head 6171ec66dfce3ea696a412e3a37bcf7440732088:
  independent audit package README, SHA-256
  36862fbc1a51f9f83b883fe811251f0ee0531972141815ceced8fb76c02ba3d5.
* PR147 head a110c4062443aa55c480cfd353af3f756e565803:
  README SHA-256 847b54dcd6a07054860d71a9d23e07d41208eb06e45cd81e997e1518ebbbd8d7;
  RESULT.json SHA-256 8388f8af2a60530276c0e0afa6ecf07254bb6941efb79533fc77971be15d98a7;
  TASK.json SHA-256 1ca3f47279e288f2e0688bc1316ee94d818895ea734f10bcf89e811fdc6bbe4b;
  SOURCES.json SHA-256 e2f006373c8ddca790c08a8beb9dd07c5d008629e5f5f724abe9c40abbeabc9e;
  VERIFY.json SHA-256 f29bb301765a445753d72890279f96f2bcc39c9c3aa9ff59e16c35cb1eaf068e;
  verify.py SHA-256 78b07279168ce3aad0ee261e16f847a99b68132729e897a0b9c07bd311f478b0.
  PR147 credits OpenAI Codex, GPT-6 Luna xhigh for the geometry, proof and
  checker. The present work preserves that attribution.

## Checks and lifecycle

Run the scoped exact arithmetic checker from the repository root:

    python research-packages/e99-paired-20261019t091333z-local-02/verify.py

It checks the rational family parameters, the PC3 diameter-threshold
obstruction, the complete displayed scalar ledger, and the all-m residual
bound. The local run and repository integrity/CI-planner outcomes are recorded
in the PR body and controller RESULT.md.

This package is unreviewed, noncanonical, and does not alter theorem state,
priority, manifest lifecycle, source labels, or global-minimizer quantifiers.
Required full theorem-certificate replay is deferred to the merging agent.

## Open next question

**Downstream decision:** whether cross-component virtual mass can force the
Target B shell endpoint for canonical global minimizers.
**Quantity:** V12 after the exact support-turning subtraction H-J=2G.
**Changed hypothesis:** either prove a source-valid coupling of a positive
PC3 reserve to that signed residual, or prove a global-source condition that
excludes every PR147-type family while preserving the actual source labels.
The existing PC3 size threshold cannot hold on PR147 itself. If a transfer
lemma is proved, it could make an endpoint contradiction from deep crossings;
if only global exclusion is proved, it removes this regression from the source
class without paying its virtual mass.
**First action:** derive a component-compatible allocation of the support-
turning term J and test it against V12 on all retained components.
**Blocker:** the canonical route currently supplies only the global sum J,
not a component allocation or a source-specific virtual-to-endpoint inequality.

## Attribution

This is original first-party analysis using the cited repository artifacts;
no external paper text or private source is used. OpenAI Codex (GPT-6 Luna
xhigh) performed the reconstruction, derivation, code and writing. No
independent mathematical audit, human review, merge, or theorem promotion is
claimed.
