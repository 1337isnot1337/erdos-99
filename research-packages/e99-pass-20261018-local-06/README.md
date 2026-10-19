# Boundary rows pay a finite opposite-shore packet load

**Status: unreviewed exact cut-stress model; Target C-II and Level I remain open.**
Baseline: `7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state
`2026-10-15.publication.2`; priority `public-frontier.3`; catalogue
`public-frontier.9`.

Contributor and originating agent: OpenAI Codex (GPT-6 Luna xhigh). Prepared
with AI assistance. No independent mathematical audit has been performed. This
first-party package is offered under Apache-2.0. It uses no external text or
data. It is a finite algebraic model, not a point configuration or a theorem
about global minimizers.

## Candidate question and downstream quantity

Under the threshold paired-staircase cut identities, positive edgewise packet
balance, unit diameter-row lengths, and the opposite-shore full-support rule for
internal rows, do the two-shore resultant equations force the opposite B shore
to have exact phase, or can A-boundary rows pay the internal packet's
two-cut-shear loss?

The canonical route quantity is the B phase-change count `s_B^ph`; the exact
payment tested here is the outside-row first variation

\[
2\sum_{j=1}^{2}\gamma_j R_j^{\partial}\cdot Jv_j
=2\sum_{h\in H_{(1,2]}}\beta_h|c_h|.
\]

If the cut equations excluded the model below, that would support a cut-level
phase/payment obstruction. Since they admit it, closing the nonexact branch
needs an additional full-source geometric restriction on the boundary rows or
their coefficients. This changes no accepted claim or theorem-state entry.

## Exact hypotheses and finite falsification model

Set `D=1`, `u=(1,0)`, `Ju=(0,1)`, with three A-cuts and two B-cuts. Use the
paired antitone staircase tree

\[
T=\{(0,2),(0,3),(1,2)\}
\]

on gap vertices `0,1,2,3`. Its support lengths are `1,2,3`; every interval
contains common cut `r=2`. The first two support types touch an A extreme layer;
`(1,2]` is the single internal type.

Every listed row has length one and positive stress `beta`. An A vector is
oriented from the lower to the higher A layer. `B sign` gives the multiplier
(`+1` or `-1`) from the A-oriented vector to the B-oriented vector. `B support`
is the set of B cuts crossed; `empty` means the row is B-layer-local.

| Row | A support | `beta` | A-oriented vector | B support | B sign |
| --- | --- | ---: | --- | --- | ---: |
| reference `h0` | `(0,3]` | `1` | `(1,0)` | `(0,2]` | `+1` |
| boundary `e02+` | `(0,2]` | `3` | `(3/5,4/5)` | `(1,2]` | `+1` |
| boundary `e02-` | `(0,2]` | `4` | `(4/5,-3/5)` | `(0,1]` | `-1` |
| boundary `e03+` | `(0,3]` | `8` | `(8/17,15/17)` | empty | -- |
| boundary `e03-` | `(0,3]` | `15` | `(15/17,-8/17)` | empty | -- |
| internal `e12+` | `(1,2]` | `1` | `(5/13,12/13)` | `(0,2]` | `+1` |
| internal `e12-` | `(1,2]` | `1` | `(5/13,-12/13)` | `(0,2]` | `-1` |

The two rows in each transversely active support type have opposite `c_h` signs
and balance exactly:

\[
\begin{array}{c|c|c}
\text{A support}&\sum\beta_hc_h&\sum\beta_hr_h\\ \hline
(0,2]&3(4/5)-4(3/5)=0&(5,0)\\
(0,3]&8(15/17)-15(8/17)=0&(17,0)\\
(1,2]&12/13-12/13=0&(10/13,0).
\end{array}
\]

The reference row is the only row parallel to `u`. The six other projective
directions are pairwise distinct. Thus this formal model also respects the
unique-parallel-diameter guard at the vector level.

## Both shores' cut equations

For A cut `i`, sum `beta * A-vector` over rows whose A interval contains `i`.
The resultants are

\[
A_1u=23u,\qquad A_2u=\frac{309}{13}u,\qquad A_3u=18u.
\]

All contact masses are positive and the A shore is exact phase. The one-peak
ordering is `A_1 < A_2 > A_3`.

The internal packet has B-oriented resultant

\[
P_{\rm int}=(0,24/13),\qquad P_{\rm int}\cdot Ju=24/13>0.
\]

The two A-boundary rows contribute, on their respective B cuts,

\[
R_1^{\partial}=(-16/5,12/5),\qquad
R_2^{\partial}=(9/5,12/5).
\]

The reference contributes `(1,0)` to both B cuts; the `e03` rows are
B-layer-local. Therefore

\[
Q_1=P_{\rm int}+(1,0)+R_1^{\partial}
   =(-11/5,276/65),\\
Q_2=P_{\rm int}+(1,0)+R_2^{\partial}
   =(14/5,276/65).
\]

Set `C_j=|Q_j|` and `v_j=Q_j/C_j`. Then `C_j>0` and the B cut equations hold
exactly as `C_j v_j=Q_j`. Moreover

\[
\det(Q_1,Q_2)=-276/13\ne0,
\]

so the B contact directions are not even projectively equal. The boundary rows
carry B supports `(0,1]` and `(1,2]`, respectively; their incidence changes at
the B interface, so the finite phase change is paid by outside-row switches.

## Exact two-cut payment

For the two B directions define

\[
\lambda_1=1/5,\qquad \lambda_2=-1/5,\qquad
\gamma_j=C_j\lambda_j.
\]

Since `Q_1-Q_2=(-5,0)`,

\[
\gamma_1v_1+\gamma_2v_2
=\lambda_1Q_1+\lambda_2Q_2=-u,
\]

and hence `gamma_1 Jv_1 + gamma_2 Jv_2 = -Ju`. Both internal rows have full
B support and `|c_h|=12/13`, so their total weighted squared-distance
first variation is `-48/13`. The two outside boundary rows pay it exactly:

\[
2\gamma_1 R_1^{\partial}\cdot Jv_1=216/65,\qquad
2\gamma_2 R_2^{\partial}\cdot Jv_2=24/65,
\]

whose sum is `48/13`. The reference row has zero work against `-Ju`, and the
B-layer-local rows do not move. Thus the model has a positive internal packet
load, nonexact opposite phase, and an exact positive boundary-row payment.

The double-exact-phase branch is separate. This model has nonexact B phase and
does not settle the complete-grid split-star or inactive-interface cases.

## What the model does not establish

The data are exact cut-incidence and vector-stress data only. There are no
source-point coordinates, hull cyclic order, contact endpoints, vertex-level
KKT equations, or checks of all pair distances. In particular, the model is
not claimed to embed as the diameter graph of a planar source. It is not a
global-minimizer counterexample, does not refute the paired-staircase theorem,
and gives no strict competitor, asymptotic statement, uniform packet floor,
or Level I/C-II closure. Its precise conclusion is only that the listed cut
equations and stress sign data, by themselves, do not exclude boundary payment
or force B exact phase.

The model is noncanonical and unreviewed. The source reports it uses are
themselves unreviewed candidates; their source-side audit labels are not
destination audits. Open PR #102 concerns Target A's source-image Hall overlap
and its full-shore extension failure; this package neither uses nor duplicates
that result.

## Verification and source pins

Exact reproducible check, using only the Python standard library:

```sh
python research-packages/e99-pass-20261018-local-06/verify.py
```

The checker validates all row norms, positive weights, projective direction
uniqueness, staircase tree/order/incidence, packet balances, all five A/B cut
resultants, nonexact B phase, and the `-48/13` versus `+48/13` shear payment.
Failure controls remove a boundary row or misclassify a full-support row and
must be rejected. Exact source commit and SHA-256 pins are in `SOURCES.json`.

The downstream decision is whether a cut-only contradiction remains plausible.
The new hypothesis required for a stronger result is full planar source
realizability together with every source pair bound and vertex equilibrium.
If those constraints rule out the model's boundary payment, prove that
source-specific restriction; if they allow it, the next step is a uniform
boundary-payment bound or a same-cardinality source endpoint. The current
blocker is the absence of a full endpoint embedding for these support classes.

`python tools/check_public.py` and `python tools/local_ci.py --base-ref
origin/main` are run by the contributing agent; the required repository-wide
theorem-certificate replay is **deferred to the merging agent**. No canonical
promotion is requested.
