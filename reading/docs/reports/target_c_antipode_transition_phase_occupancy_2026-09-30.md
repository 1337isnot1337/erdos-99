> Generated reading edition · [exact source](../../../docs/reports/target_c_antipode_transition_phase_occupancy_2026-09-30.md) · source SHA-256 `c297ba2a8321b0c95016ea5886c88fc9ca169dd90febf38c946bd92e9ee04c67`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F424B7A54A11","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: exact antipode transitions and inverse-phase hull occupancy

**Date:** 2026-09-30<br>
**Base main:** `c2f1850d0f168bbe1914976738eac179d5e916aa`<br>
**State version:** `2026-09-14.audit.51`<br>
**Classification:** proved candidate awaiting promotion; noncanonical.<br>
**Level I:** open. C-II remains open.

## 1. Finite statements

Let the entire source be a finite unit-separated planar set of diameter
$`D`$. Let $`F`$ be the two-dimensional hull of its loaded diameter
vertices, and assume its full diameter graph is not a star. Put
$`q=|B|`$, $`h=|E_H|`$, $`d_H=q-h`$, and
$`\delta_D=2\arcsin(1/(2D))`$.
Call a hull side covered when its endpoints have a common diameter partner.
The exact V-cover candidate from this run leaves at most $`U=2d_H`$
sides uncovered. No near-disk limit is assumed.

**Opposite support and width.** If the covered side $`xy`$ has length
$`s`$, common diameter partner $`v`$, and inward unit normal $`n`$,
then $`v`$ uniquely maximizes projection onto $`n`$, even over the
entire source. On the loaded hull,
```math
\boxed{w_F(n)=\sqrt{D^2-s^2/4}.}
\tag{1.1}
```
No opposite hull side is parallel to a covered side.

**Antipode transition.** Let consecutive covered sides $`xy,yz`$, in
counterclockwise order, have lengths $`s,t`$, common diameter partners
$`v,w`$, and exterior turn $`\psi`$. Then exactly
```math
\boxed{\psi=\arcsin\frac{s}{2D}+\arcsin\frac{t}{2D}
                 +2\arcsin\frac{|v-w|}{2D}.}
\tag{1.2}
```
Thus $`\psi\ge\delta_D`$, and $`\psi\ge2\delta_D`$ if
$`v\ne w`$. The repeated-partner case has exactly the first two terms.

**Direction occupancy.** For $`r`$ disjoint projective tangent intervals
of widths $`\omega_j<\pi`$, the total number of loaded hull sides in
them is at most
```math
\boxed{4d_H+2r+2\sum_j\omega_j/\delta_D.}
\tag{1.3}
```
For widths $`\omega_j=W_j/D`$, this is at most
$`4d_H+2r+2\sum_jW_j`$, because $`D\delta_D>1`$.

## 2. Support and signed transition proofs

Place a covered side at $`x=(-s/2,0),y=(s/2,0)`$, with the loaded
hull above its supporting line. Its partner is $`v=(0,H)`$, where
$`H=\sqrt{D^2-s^2/4}`$. Every source point $`p=(a,b)`$ belongs
to both radius-$`D`$ disks about $`x,y`$, hence
```math
b^2+(|a|+s/2)^2\le D^2.
```
Therefore $`b\le H`$, with equality only at $`p=v`$. The loaded
side supports at height zero. This proves (1.1), unique opposite support,
and the absence of an opposite parallel side.

For (1.2), put $`y=0`$, with incoming side direction $`\alpha`$ and
outgoing direction $`\beta=\alpha+\psi`$. Set
$`a=\arcsin(s/(2D))`$, $`b=\arcsin(t/(2D))`$. The inward circle
intersection formulas give
```math
\arg(v-y)=\alpha+\pi/2+a,\qquad
\arg(w-y)=\beta+\pi/2-b.
\tag{2.1}
```
The sign of their difference must be checked. The cross diameter constraint
$`|x-w|\le D`$ implies $`\sin(\psi-b)\ge\sin a`$.
If $`\psi<a+b`$, then $`-\pi/6<\psi-b<a\le\pi/6`$, where
sine is strictly increasing, a contradiction. Thus
$`\theta=\psi-a-b\ge0`$. Also $`\theta<\pi`$, since a strict
hull turn is less than $`\pi`$. The two radius vectors have length
$`D`$, so
```math
|v-w|=2D\sin(\theta/2),\qquad
\theta=2\arcsin(|v-w|/(2D)).
```
This proves the law, including $`v=w`$. Source separation gives
$`s,t\ge1`$, and $`|v-w|\ge1`$ when the partners differ.

When all sides are covered, summation yields
```math
2\pi=2\sum_i\arcsin\frac{s_i}{2D}
       +2\sum_i\arcsin\frac{|v_i-v_{i+1}|}{2D}.
\tag{2.2}
```
The regular-Reuleaux shell realizes this identity. It is not a winding
contradiction by itself.

## 3. Occupancy proof, including every uncovered side

One oriented tangent interval of width $`\omega`$ selects one consecutive
side chain. If it contains $`c`$ covered and $`u`$ uncovered sides,
there are at most $`u+1`$ covered runs. Each within-run turn is at least
$`\delta_D`$. Consequently
```math
(c-u-1)\delta_D\le\omega,
\qquad c+u\le2u+1+\omega/\delta_D.
```
The $`r`$ disjoint projective intervals lift to $`2r`$ oriented chains.
Their uncovered counts total at most $`U\le2d_H`$. Sum the last bound
to prove (1.3). Empty chains improve the bound. Cuts are placed outside each
chain, so wraparound never duplicates a side.

## 4. Original global train ends

Use canonical Section 61's global stopped trains. A good hull end is an
occurrence on a distinguished one-edge outer route, as defined there.
Each physical hull side supplies at most one good occurrence. This retains
bridge multiplicities and singleton trains.

Suppose $`M_j`$ distinct original trains have directions in the $`r`$
disjoint intervals of widths $`W_j/D`$. They have $`2\sum_jM_j`$
original terminal incidences. At least
```math
\boxed{2\sum_jM_j-4d_H-2r-2\sum_jW_j}
\tag{4.1}
```
are nongood. Canonical Section 61 bounds their capacity by
$`2x_B+5f+g_F`$. Hence
```math
\boxed{2\sum_jM_j\le4d_H+2r+2\sum_jW_j+2x_B+5f+g_F.}
\tag{4.2}
```
Here $`Q=f+g_F`$ is the **global** contact-face currency, not the sum
of the harmonic-cell $`Q_P`$'s in the rooted local ledger.

For fixed $`r,W_j`$, linear family size and $`d_H=o(D)`$ force almost
all of the families' **two** ends into the nongood budget. This improves
one-bad-end-per-train counting. Hull occupancy also bounds local physical
train ends, but (4.2) requires actual global trains or an explicit transfer
theorem for local ends.

## 5. Dependencies, audit, and remaining implication

The geometric identities use only coordinates and source diameter. Occupancy
also uses this run's exact V-cover candidate. The global end charge is
canonical Section 61. The finite integer/Fraction audit
`docs/research/migration/2026-10-16/shards/01/support/research/verify_antipode_transition.py` checks unique opposite support,
radius-vector order, and turning bounds by sign-aware rational squaring.
It certifies examples, not universality or global optimality; its rational
examples contain no odd diameter cycle.

The analytic proof covers repeated and distinct partners, unequal lengths,
long star runs, and projective cuts. Degenerate hulls are excluded explicitly.
No asymptotic convergence rate, incidence transfer, or artificial train end
is used. The closing chain is

`inverse-phase terminal mass -> (4.2) -> impossible global defect payment
or a full-source strict competitor`.

The last implication remains open: the current global ledger permits a linear
nongood-end budget. No source point has been removed and no C-II closure is
claimed.
