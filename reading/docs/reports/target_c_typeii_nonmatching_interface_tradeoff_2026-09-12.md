> Generated reading edition · [exact source](../../../docs/reports/target_c_typeii_nonmatching_interface_tradeoff_2026-09-12.md) · source SHA-256 `11748658ed884ae53d847c78d603057fd1e560e0c45768fde58b1a575d3f54f3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0596A5326EBD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — corrected Type-II nonmatching/interface tradeoff

**Date:** 2026-09-12  
**Classification:** corrected proved candidate awaiting promotion; unreviewed and noncanonical  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This note repairs an invalid use of the withdrawn `1.9046256...` unconditional loaded-hull floor. The exact first-order scalar coupling survives, but the claimed `0.6676585...D` Type-II nonmatching floor does not.

Put

$$
t_D={q-k\over D},\qquad
r_D={2h-q\over D},\qquad
x_D={x_B\over D},\qquad
Q_D={Q\over D},
$$

where `k=d_H+s_Z`.

## 1. Correct loaded-hull input

Canonical Sections 63 and 85 give

$$
Q=2(q-k)-b\le2(q-k)-\operatorname{per}(F),
\tag{NT.1}
$$

$$
q-k+2f\ge2\sqrt{R_4},
\qquad f\le Q.
\tag{NT.2}
$$

In Type II,

$$
{\operatorname{per}(F)\over D}\to\pi,
\qquad
{R_4\over D^2}\to\Delta_2:={\pi\over2\sqrt3}.
$$

The corrected loaded-hull/train argument therefore gives only

$$
\boxed{
\liminf t_D
\ge
t_*:={2\over5}\left(\pi+\sqrt{\Delta_2}\right)
=1.6375621841815\ldots .
}
\tag{NT.3}
$$

The previously used unconditional value

$$
2\sqrt{\Delta_2}=1.9046256137\ldots
$$

is rejected. That value is available only under additional defect-small hypotheses such as the separately audited `J_aug=o(D)` interface/augmented-defect branch; it is not a general Type-II floor for `q-k`.

## 2. Exact nonmatching identity

Canonical Sections 61 and 63 give

$$
2h-q=x_B+Q+2s_Z,
\tag{NT.4}
$$

and

$$
b+Q=2(q-k),
\qquad x_B=b-q.
\tag{NT.5}
$$

Hence

$$
x_B+Q=2(q-k)-q
\tag{NT.6}
$$

and equivalently

$$
2h-q=2(q-k)-q+2s_Z.
\tag{NT.7}
$$

If one uses only `q/D<=pi`, (NT.3), and `s_Z>=0`, then (NT.7) yields merely

$$
\liminf r_D\ge2t_*-\pi
=0.1335317147732\ldots .
\tag{NT.8}
$$

This is far weaker than canonical Section 61 and is not useful.

## 3. The train-end ledger gives the real surviving tradeoff

Section 61's finite train-end inequality is

$$
h-2\le2x_B+3f+(Q-f)+s_Z.
\tag{NT.9}
$$

Since

$$
h=(q-k)+s_Z,
$$

the `s_Z` terms cancel. Along any subsequence on which the normalized variables converge,

$$
\boxed{
t\le2x+2f+Q.
}
\tag{NT.10}
$$

Let

$$
s:=x+Q=2t-q_*.
\tag{NT.11}
$$

Because `0<=f<=Q`,

$$
2x+2f+Q\le2x+3Q\le3(x+Q)=3s.
$$

Therefore

$$
\boxed{s\ge t/3.}
\tag{NT.12}
$$

Using (NT.4),

$$
{2h-q\over D}=s+2{s_Z\over D},
$$

so the corrected Type-II consequence of this particular ledger is

$$
\boxed{
\liminf {2h-q\over D}
\ge {t_*\over3}
=0.5458540613938\ldots .
}
\tag{NT.13}
$$

Canonical Section 61 already proves the stronger branch-independent lower floor

$$
\liminf {2h-q\over D}\ge c_*,
\qquad c_*=0.609904\ldots .
$$

Thus this Type-II coupling does **not** improve the canonical nonmatching floor.

The old claim

$$
{2h-q\over D}\ge0.6676585\ldots
$$

is rejected.

## 4. What remains useful: exceptional-face forcing near small interface currency

Equation (NT.10) can be rearranged without any false hull floor:

$$
\boxed{
2f-Q\ge t-2s,
\qquad s=x+Q.
}
\tag{NT.14}
$$

Therefore whenever the nonmatching/interface currency `s` is less than `t/2`, a positive linear exceptional-face contribution is forced. More explicitly,

$$
f\ge {t-2s\over2}
\tag{NT.15}
$$

whenever the right-hand side is positive.

Feasibility itself requires `s>=t/3`: since `2f-Q<=Q<=s`, equations (NT.14) imply

$$
t-2s\le s.
$$

At the formal scalar endpoint `s=t/3`, equality is forced throughout the simple bounds:

$$
x=0,
\qquad Q=f=s=t/3.
\tag{NT.16}
$$

Thus a sequence trying to minimize this interface currency cannot be close to a pure rhombic disk; it must carry a linear exceptional-face population. This is the valid structural content of the tradeoff.

## 5. Relation to the audited augmented-defect dichotomy

The separately audited interface/augmented-defect theorem gives

$$
(q-k)+J_{aug}\ge2\sqrt{R_4}.
\tag{NT.17}
$$

Consequently the larger value `2sqrt(Delta_2)=1.9046256...` for `(q-k)/D` is valid on the additional subbranch

$$
J_{aug}=o(D).
$$

Nothing in the present report proves that defect-small hypothesis. The previous version silently treated the conditional high-density branch as universal; that was the core error.

## 6. Withdrawn endpoint addendum

The previous report also attached a boundary-degree saturation discussion to the false `0.6676585...` endpoint. That discussion is not needed for the exact scalar theorem and is withdrawn from this report pending a separate audit against a correctly specified endpoint branch.

## 7. Final disposition

The exact scalar relation

$$
t\le2x+2f+Q,
\qquad x+Q=2t-q_*
$$

is valid. It forces `x+Q>=t/3` and linear exceptional-face currency near equality.

It does **not** improve the canonical Section-61 nonmatching lower bound. The previously advertised Type-II floor `0.6676585...` is invalid and superseded by this correction.

C-II and Level I remain open.