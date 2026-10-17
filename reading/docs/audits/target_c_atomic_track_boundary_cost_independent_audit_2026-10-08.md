> Generated reading edition · [exact source](../../../docs/audits/target_c_atomic_track_boundary_cost_independent_audit_2026-10-08.md) · source SHA-256 `dc0f996227a196cba153366e667ac1bf0d900b587d4831cc4fa50db0ac1ee419`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 3 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-FD77BD4977EE","canonical":true,"claim_ids":["C-ATOMIC-TRACK-BOUNDARY-COST"],"claim_statuses":{"C-ATOMIC-TRACK-BOUNDARY-COST":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.129 — atomic track boundary cost

Date: 2026-10-08  
Audit base: `origin/main=0407f994f0a179e3274d74d42949e08f54c74239`, state `2026-10-08.audit.128`  
Source snapshot: `origin/research/target-c-atomic-boundary-audit-20261004` at `9d51e2120d36ba60161975d0de6e9c77786a1c53`  
Classification: independently reconstructed theorem; **PASS — promote**.  
Scope audited: Theorem A, Sections 1–5 only, of `docs/reports/target_c_atomic_boundary_capacity_audit_2026-10-04.md`. Theorem B is audited separately in Audit.130; Theorem C and the companion sharp-orbit report remain unreviewed.

Frozen source artifact hashes: report `e79dbcfcefcd7a65851e2f7e2307fede023f8860656f0b8979dec2d94b832b2f`; verifier `e4d1066e3cfd96e074a50f8780b3614ffb6da1bc3753401adb3f301251adee04`.

## Exact claim

Let a sequence range over canonical contact-minimal, then diameter-pair-minimal,
triangle-free global sources in the Type-II branch, with (D\to\infty). Retain
all source points, including contact isolates. Write

```math
p=\operatorname{per}(F),\quad q=|B|,\quad b=\text{occurrence-counted outer-walk length},
\quad Q=\sum_G(\deg G-4),\quad f=\#\{G:\deg G\ge5\},
```
```math
k=d_H+s_Z,\quad x_B=b-q,\quad m=\#\{\text{nonunit loaded-hull sides}\},
\quad g=p-q,\quad z=b-p,\quad u_B=x_B-m,
\quad s_2=\sqrt{\frac{\pi}{2\sqrt3}},\quad \Delta_2=s_2^2.
```

The claim is

```math
\liminf_{D\to\infty}\frac{Q+4f+x_B+m}{D}\ge4s_2. \tag{A}
```

Using the canonical Section 63 identities, this implies

```math
\liminf_{D\to\infty}\frac{10(q-k)+2g-3z-u_B}{D}\ge5\pi+4s_2. \tag{B}
```

If (t_D=(q-k)/D\le1.860+o(1)), then

```math
2g-3z-u_B\ge(5\pi+4s_2-18.6-o(1))D,
```
where (c=5\pi+4s_2-18.6\in(0.91721449540479,0.91721449540480)).
Consequently (g\ge(c/2-o(1))D) and

```math
\frac qD\le\pi-\frac c2+o(1)=2.6829854058874\ldots+o(1).
```
In particular, the joint hypotheses (x_B=O(\sqrt D)) and
(t_D\le1.860+o(1)) are impossible, since (0\le g\le x_B).

## Canonical dependencies

- `C-FULLCORE-NEAR-DISK`: full-source Type-II limits give (D^{-1}F\to)
  the radius-(1/2) disk, (p/D\to\pi), and (R_4/D^2\to\Delta_2).
- `C-LOADED-HULL`: actual loaded-hull order, occurrence-counted outer walk,
  (b+Q=2(q-k)), and (x_B=g+z, m=g+z-u_B).
- `C-RHOMBUS-POP`: each bounded quadrilateral is an actual strict unit rhombus.
- `C-PUNCTURED-PHASE`: total strict-rhombus area excess is (O(D)), with the
  full source retained.
- `C-TRAIN-INTERFACE-CURRENCY`, together with Theory 01, Theorem 10.6:
  complete tracks have two terminal occurrences; the finite actual crossing
  graph is simple and triangle-free, including holes and disconnected
  components.

All dependencies are canonical at the audit base. No audited-working atomic
Mantel result, proof-only report, scaffold, or source restriction is used.

## Independent proof reconstruction


**Source formatting excerpt (unbalanced inline math in the original):**

```text

Set (P_{\rm exc}=Q+4f\). It is enough to prove (A) along a subsequence on
which the normalized left side converges to a finite liminf; if it is infinite,
the claim is immediate. On this subsequence (P_{\rm exc}/D) and
((x_B+m)/D) are bounded. Since (q\le p), (b=q+x_B=O(D)). Thus the
normalized track, terminal, and boundary measures below have bounded mass.
Pass jointly to weak limits and to limits of the scalar budgets.
```



### Actual loaded sides are diffuse; repeated walk occurrences are charged

On the projective direction circle, put mass (1/D) at each actual unit side
direction of the loaded hull, giving measure (\rho_D). This is dominated by
the hull's perimeter-weighted tangent-direction measure. The rescaled convex
hulls converge to a disk, so the tangent measures converge weakly to uniform
measure of mass (\pi); this also follows from (S_F=h_F+h_F'') by testing
against smooth periodic functions and integrating by parts. Hence every weak
limit (\rho) is atomless.

There are exactly (q-m) unit loaded-hull sides. Select one exterior
occurrence of each in the contact outer walk, including only one occurrence
when the contact edge is a bridge. If (\omega_D) counts every outer-walk
occurrence, then

```math
\omega_D=\rho_D+\epsilon_D,\qquad
\epsilon_D\ge0,\qquad
\|\epsilon_D\|=\frac{b-(q-m)}D=\frac{x_B+m}D. \tag{1}
```

This counts all repeated vertices and bridge occurrences in the remainder;
none is identified away.

### Quadratic rhombus mass forces atomic track mass

Put mass (1/D) at each actual complete strict-rhombus track direction,
giving (\nu_D). Every track end borders either the outer face or a bounded
exceptional face, whose total terminal-occurrence count is at most
(P_{\rm exc}). Thus

```math
2\nu_D(\mathbb T)\le b/D+P_{\rm exc}/D=O(1).
```

Let (\xi_D) be the ordered crossing measure, with two ordered atoms for each
actual track crossing and scale (D^{-2}). Simplicity gives
(\xi_D\le\nu_D\otimes\nu_D). Each rhombus has acute angle at least
$`\pi/3`$, and the (O(D)) total rhombus area excess implies that, for every
fixed $`\eta>0`$, only (O_\eta(D)) crossings have acute angle at least
$`\pi/3+\eta`$. Thus any weak limit of $`\xi_D`$ is supported on

```math
E=\{(\theta,\phi):\phi=\theta\pm\pi/3\pmod\pi\}.
```

The product measure $`\nu\otimes\nu`$ charges (E) only at pairs of atoms:
for each first coordinate, the second coordinate has only two possible
values; the diffuse part gives zero mass to the countable translates of the
atomic set. Write (a) for the total atomic mass of this one fixed weak limit
$`\nu`$. The limiting crossing measure has total mass
$`2\Delta_2`$, so its unordered mass is $`\Delta_2`$, all on atom pairs.



**Source formatting excerpt (unbalanced inline math in the original):**

```text
To apply Mantel without collapsing phase labels, fix finitely many atoms and
disjoint neighborhoods with zero-mass boundaries that capture all but
arbitrary $`\eta>0`$ of this unordered crossing mass. Shrink their radii so
their total $`\nu`$-mass is at most (a+\eta\). The corresponding finite
source graphs are induced subgraphs of the actual simple triangle-free track
crossing graphs. They have at least
$`(\Delta_2-\eta)D^2-o(D^2)`$ edges and at most
$`(a+\eta)D+o(D)`$ vertices. Mantel's inequality gives
```


```math
\Delta_2-\eta\le\frac{(a+\eta)^2}{4}.
```
Letting $`\eta\downarrow0`$ yields
```math
a\ge2\sqrt{\Delta_2}=2s_2. \tag{2}
```

This is the fixed-limit finite-window argument. It does not take a second weak
limit of atomic masses and does not assume that the graph on three collapsed
phase labels is triangle-free.

### Pay for both ends of each atomic track

Let (o_D) and (j_D) be the outer and exceptional-face terminal occurrence
measures, both normalized by (D). Each track has two ends of its own
direction, so

```math
2\nu_D=o_D+j_D,\qquad o_D\le\omega_D,\qquad
\|j_D\|\le P_{\rm exc}/D. \tag{3}
```

Take atomic masses in these inequalities in the fixed joint weak limit. The
limit of (\rho_D) has no atoms; (1) bounds the atomic mass supplied by
$`\epsilon_D) by the limiting ( (x_B+m)/D`$ budget. The exceptional
terminal budget is at most the limit of (P_{\rm exc}/D). Therefore
```math
2a\le\lim\frac{x_B+m+P_{\rm exc}}D.
```
Together with (2) this proves (A). The subsequence was chosen at the finite
liminf, so the result holds for the original sequence.



**Source formatting excerpt (unbalanced inline math in the original):**

```text
Since (f\le Q), (5Q\ge Q+4f). Therefore (A) gives
$`\liminf(5Q+x_B+m)/D\ge4s_2`$. Substituting
$`Q=2(q-k)-b`$, (b=p+z), (x_B=g+z), and (m=g+z-u_B\) gives the
exact identity
```


```math
5Q+x_B+m=10(q-k)-5p+2g-3z-u_B.
```
Using (p/D\to\pi) proves (B). The stated low-(t_D) consequences follow
because (z,u_B\ge0); the (q/D) endpoint uses (g=p-q\ge(c/2-o(1))D).

## Hostile checks and verifier scope

- The atomic-mass step is checked against
  `research/target_c_atomic_mantel_gap_finite_diagonal_hostile_audit_2026-09-12.md`:
  the invalid second-weak-limit shortcut is avoided by freezing neighborhoods
  of atoms of one fixed limit and applying Mantel to finite source graphs.
- The source report's collapsed-phase triangle regression does not damage this
  proof: no phase-collapsed graph is used.
- The proof counts all source geometry used by canonical Type II and all
  occurrence-counted outer-walk terminals. Contact isolates are retained in
  the full-source dependencies; the positive-contact track complex is used
  only for its actual rhombi.
- Inspected and reran the frozen source script
  `research/verify_target_c_atomic_boundary_2026_10_04.py`. It passes 12
  rational budget checks, 1,677 exact full-source pair checks, and 462 exact
  convex-support checks. Its rational/Q(√3)/interval arithmetic is exact or
  outward-certified for those finite propositions; it does not verify the
  weak-limit proof, existence of canonical sources, global optimality, or
  C-II closure.
- The script's `q_hi=PI_HI-demand_lo` checks the 2.224378... endpoint from
  Theorem B in Section 7, not a consequence of Theorem A alone. Theorem A
  alone gives q/D<=pi-c/2+o(1)=2.682985...+o(1). Audit.129 did not audit
  Theorem B; its route-exposure proof is independently audited and promoted
  as C-ATOMIC-OUTER-ROUTE-EXPOSURE in Audit.130. The verifier's finite
  arithmetic is consistent with Theorem B but does not verify that analytic
  proof, so the script is not registered as a certificate.

## Verdict and frontier effect

**PASS — promote C-ATOMIC-TRACK-BOUNDARY-COST.** The independent proof
supports (A), (B), and the stated low-t_D consequences. The distinction
between q/D<=pi-c/2+o(1) from this theorem and q/D<=pi-c+o(1) from
Audit.130 is explicit; neither finite arithmetic check substitutes for the
analytic weak-limit proofs.

This makes the joint Type-II subcase (x_B=O(\sqrt D)),
$`t_D\le1.860+o(1)`$ empty and gives a linear perimeter-gap lower bound in
the low-(t_D) branch. It does not bound that gap from above, construct a
finite competitor, resolve other Type-II regimes, close C-II, or change Level
I. Theorem B was subsequently audited in Audit.130; Theorem C and the
companion sharp-orbit result from the source snapshot remain unreviewed.

Promotion transaction: PR #811 merged as 462456b7b34140ea2c88aec71ffe3e1d5a0a6e6d; protected check 37729047580 and post-main workflow 37729415565 passed.
