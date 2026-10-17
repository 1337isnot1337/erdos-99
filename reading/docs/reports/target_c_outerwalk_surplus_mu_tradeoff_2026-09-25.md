> Generated reading edition · [exact source](../../../docs/reports/target_c_outerwalk_surplus_mu_tradeoff_2026-09-25.md) · source SHA-256 `c47988ba076f6d86e00382a6dfd938501727b928957f684990c9470bcd621b55`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9EF4A9B6AF4D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — a canonical-input full-core outer-walk/surplus tradeoff

**Date:** 2026-09-25
**Repository commit:** `15cd5d8a8346b42101b355afebd6da28ccd58886`
**State version:** `2026-09-14.audit.51`
**Run type:** source-ledger theorem candidate
**Target:** C-II full-core branch
**Starting status:** canonical Sections 61, 63, 75 and the full-core loaded-chord theorem
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** no external theorem used
**Computation:** decimal evaluation only; not load-bearing

## LEVEL I STATUS

STILL OPEN.

## 1. Exact starting endpoint and implication chain

The canonical full-core branch has the necessary floor

```math
\liminf\mu_D\ge\mu_{\rm TC}=1.6375621841815\ldots,
\qquad
\mu_DD=e_{BB}+2s_C-3k,
\quad k=d_H+s_Z.
```

The exact floor endpoint has been excluded, but larger surplus remains. The
candidate chain tested here is

```text
canonical good-train end capacity + loaded/pinned ledgers
    -> low mu forces linear extra global outer-walk surplus u_B
    -> source-level payment of u_B to aggregate cell detour, or strict sub-D motion
    -> exclusion of the remaining low-surplus full-core window.
```

The first arrow is proved below. The source-level payment arrow is open; this
report does not claim a Level I or C-II closure.

## 2. Strongest new result

**Classification:** proved candidate awaiting independent audit and promotion.

### Finite statement

Let `A` be a canonical contact-minimal, then diameter-pair-minimal,
triangle-free global-minimizer representative in the full-core near-disk
Type-II branch, with `D` large enough for the promoted loaded-chord theorem.
Use the actual force hull `F` and canonical notation:

- `q` loaded hull vertices, `b=q+x_B` occurrences on the positive-contact
  outer-face walk, `P_F=per(F)`;
- `m_B` nonunit sides of the loaded hull and `u_B=x_B-m_B>=0`;
- `Q=sum_(bounded faces)(deg f-4)`, and `f` bounded nonquadrilateral faces;
- `c_I` unloaded positive-contact components;
- `k=d_H+s_Z` and `mu_DD=e_BB+2s_C-3k`.

Then the **finite** inequality

```math
\boxed{\quad
5\mu_DD+2u_B-3m_B+10c_I+22\ \ge\ 3P_F.
\quad}
\tag{OW.1}
```

Consequently every canonical full-core survivor sequence satisfies

```math
\boxed{\quad
\liminf_{D\to\infty}
\left(5\mu_D+\frac{2u_B-3m_B}{D}\right)
\ge3\pi.
\quad}
\tag{OW.2}
```

In particular, if along a survivor sequence
`limsup mu_D <= mu_0 < 3pi/5`, then

```math
\boxed{\quad
\liminf\frac{u_B-\frac32m_B}{D}
\ge\frac{3\pi-5\mu_0}{2}>0.
\quad}
\tag{OW.3}
```

At the promoted floor value `mu_TC`, the right side is
`(3pi-5mu_TC)/2 = 0.6184835199...`; that endpoint itself is already
canonically excluded, so this number describes the limiting scale of nearby
scalar regimes, not an attainable equality case. If `u_B=o(D)`, (OW.2)
instead forces `liminf mu_D>=3pi/5=1.8849555921...`.

### Complete proof

Canonical Section 61 counts all train ends with occurrence multiplicity. Its
exact train count and good-end estimate are

```math
T=\frac{b+Q}{2}+2f,
\qquad
T-2\le2x_B+5f+g_F
       =2x_B+4f+Q,
```

where `Q=f+g_F`. Substitute `b=q+x_B`, multiply by two, and rearrange:

```math
q\le3x_B+4f+Q+4\le3x_B+5Q+4,
\tag{OW.4}
```

because every nonquadrilateral face contributes at least one to `Q`, so `f<=Q`.
Thus

```math
Q\ge\frac{q-3x_B-4}{5}.
\tag{OW.5}
```

Canonical Section 63 gives the exact outer-walk defect identity

```math
q-x_B=Q+2k.
\tag{OW.6}
```

In the full-core near-disk branch, the promoted loaded-chord theorem makes
every loaded-loaded unit contact a hull side. Hence `e_BB=q-m_B`.
The exact pinned ledger of Section 62 gives

```math
c_I+e_{BB}+s_C=q-2+k,
\qquad
s_C=m_B+k-c_I-2.
\tag{OW.7}
```

Substitute (OW.6)–(OW.7) into the definition of `mu_D`:

```math
\mu_DD
=q+m_B-k-2c_I-4
=\frac{q+x_B+Q}{2}+m_B-2c_I-4.
\tag{OW.8}
```

Apply (OW.5) in (OW.8):

```math
5\mu_DD
\ge3q+x_B+5m_B-10c_I-22.
\tag{OW.9}
```

As `q+x_B=b>=P_F`, we have `3q+x_B=3b-2x_B>=3P_F-2x_B`.
Insert this into (OW.9), then use `x_B=m_B+u_B`. The result is

```math
5\mu_DD+2u_B-3m_B+10c_I+22\ge3P_F,
```

which is (OW.1). No outer-walk occurrences have been identified or dropped.
In fact the proof has an exact nonnegative-slack decomposition. Define

```math
s_{\rm end}:=2x_B+4f+Q-(T-2)\ge0.
```

Substitution of the exact train count and (OW.8) gives

```math
\boxed{\quad
5\mu_DD+2u_B-3m_B+10c_I+22-3P_F
=s_{\rm end}+2(Q-f)+3(b-P_F).
\quad}
\tag{OW.10}
```

Thus every term discarded in (OW.1) is identified: good-train end capacity,
exceptional-face degree above five, and metric detour of the global contact
outer walk beyond the force-hull perimeter. Formula (OW.10) is an identity,
not a claim that its three slacks can vanish simultaneously in a canonical
survivor.

For (OW.2), canonical full-core near-disk convergence gives
`P_F/D->pi`, while canonical Section 75 gives `c_I=O(D^(2/3))=o(D)`.
Divide (OW.1) by `D` and take lower limits. Formula (OW.3) follows by
rearranging (OW.1) and using the stated upper bound on `mu_D`.

### Scope and dependencies

The theorem applies only to canonical Type-II full-core survivors. It is an
inequality for the actual positive-contact outer walk and actual loaded force
hull, not for a scaffold or one harmonic cell. All contact-isolated source
points remain in the global source; neither their population nor a full-source
affine-kernel assertion is used. The dependencies are:

| Input | Lifecycle | Exact use |
| --- | --- | --- |
| `C-LINEAR-NONMATCH`, Section 61 | canonical | train count and at-most-two good hull-to-hull trains |
| `C-LOADED-HULL`, Section 63 | canonical | `q-x_B=Q+2k`, `u_B=x_B-m_B` |
| `C-ATTACH-CURRENCY`, Section 62 | canonical | pinned ledger (OW.7) |
| `C-FULLCORE-LOADED-CHORD` | canonical | `e_BB=q-m_B` in near-disk full-core branch |
| `C-COMP-DEATOMIZATION`, Section 75 | canonical | `c_I=o(D)` only for asymptotic consequences |
| `C-FULLCORE-NEAR-DISK`, Sections 79–80 | canonical | `P_F/D->pi` only for asymptotic consequences |

No audited-working or unreviewed theorem is imported into the proof.

## 3. Exact frontier effect and remaining lemma

This is a new necessary tradeoff within the high-surplus full-core branch,
not a branch elimination. It splits that branch at `3pi/5`: below the split,
the extra global outer-walk surplus `u_B`, after a `3m_B/2` charge, is linear.
It does not identify that global outer walk with the local harmonic-cell walks
`L_r`, and it does not imply a strict diameter decrease.

A sufficient next bridge for this route must connect the **same** `u_B` to a
source-level gain. One precise version to test is: for fixed
`mu_0 in (mu_TC,3pi/5)`, every canonical full-core survivor with
`mu_D<=mu_0` and (OW.3)'s forced `u_B` admits a same-cardinality
unit-separated configuration of diameter strictly below `D`. This is a
source-preserving deformation/replacement theorem, not a consequence of
(OW.1), and remains open. The macroscopic-container branch and larger
`mu_D` full-core branch remain untouched.

## 4. Claim and regression audit

| Claim | Classification | Audit note |
| --- | --- | --- |
| (OW.1) finite source tradeoff | Proved candidate awaiting promotion | Exact algebra from named canonical modules; independent check requested |
| (OW.2)–(OW.3) asymptotic split | Proved candidate awaiting promotion | Uses only near-disk perimeter and `c_I=o(D)` |
| Global outer walk equals sum of cell outer walks | Rejected as an inference here | Cells can repeat loaded edges/vertices; no injective occurrence map is known |
| Linear `u_B` gives a strict competitor | Conditional, unproved | Requires source-preserving motion or replacement |

The proof retains bridges and repeated outer-walk occurrences through Section
61's exact count. It does not use an Euler path through diameter states,
extend ZR/ZF to isolates, infer a finite release from a zero multiplier, or
turn a scalar necessary inequality into global optimality. The separate
thin-cap partition regression shows why excess total cell diameter alone
cannot improve the area-weighted Section-122 floor; that geometric regression
is not a counterexample to (OW.1), which uses source-specific train and pinned
ledgers.

The audited-working proof-only Section 151 also bounds `u_B`, but uses the
audited-working Section-148 weighted diameter-moment payment and has a
different right-hand side. Equation (OW.1) uses only promoted inputs and
keeps `mu_D` and the nonunit-side count in the finite inequality. Neither
tradeoff supplies the missing source-preserving deformation.

## 5. Literature, computation, promotion, and handoff

No external theorem or computation is used in (OW.1)–(OW.3); the displayed
decimals are orientation values only. A focused
literature search on triangle-free disk packings supplied no load-bearing
claim. The arithmetic is symbolic and displayed in full.

**Promotion recommendation:** independent audit before any canonical change.
The theorem narrows a full-core subwindow but does not alter the exact Level I
or C-II status. An audit should verify the Section-61 endpoint count and the
normalization of `mu_D`, `m_B`, and `u_B`. If promoted, update the state
manifest/version, `docs/STATE.md`, Target C route/current frontier and prompt,
dependency edges, and regenerated views in one transaction.

The next agent should read Sections 61–63, 75, 79–80, 122–123 and the promoted
loaded-chord/train reports, then attack a source-preserving payment of the
forced global `u_B` in the `mu_TC<mu_D<3pi/5` window. Other mechanisms are
needed for `mu_D>=3pi/5` and the macroscopic-container branch.
