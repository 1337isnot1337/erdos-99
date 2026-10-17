> Generated reading edition · [exact source](../../../docs/reports/target_c_zf_boundary_surplus_collapse_2026-09-09.md) · source SHA-256 `61f9f2aad28eb581873a3ed0f9978cacfeb644f4098dba0012017c084425b924`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-952DC25D03A4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZF forces the linear boundary-surplus phase

**Date:** 2026-09-09  
**Repository state:** `4bc7c9baddb38d12cbadde8394992c0e9f708104` (`main` at start of run)  
**Run type:** closing-proof continuation / dependency synthesis  
**Target:** Target C, Gate C-II  
**Active prompt:** user-supplied Target C–Z full-settlement continuation prompt  
**External web search:** used only as a cross-check; no new theorem imported into the proof  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The report-level Z/ZC/ZR/ZF chain survives the September 9 consolidated audit. The new result below combines ZF with already-audited diameter-graph and terminal-path inputs. It does not prove the final face inequality and is not a Level I settlement.

## 1. Starting endpoint

The audited ZF conclusion for the nonisolated contact core is

$$
e+h\ge 2v-2,
\tag{1.1}
$$

and Eppstein's connected triangle-free penny-graph bound is

$$
e\le 2v-\delta-2.
\tag{1.2}
$$

Hence the campaign already records

$$
h\ge\delta\ge\lceil D\rceil.
\tag{1.3}
$$

The exact scalar closing theorem remains

$$
b+\sum_{F\text{ bounded}}(\deg F-4)>2h,
\tag{1.4}
$$

which is equivalent to `e+h<2v-2` and would contradict ZF.

Before this run, C33 split the loaded-boundary analysis according to

$$
\sigma_B:=2q-\delta-2,
\tag{1.5}
$$

where `q=|B_+|`. The modules C35–C45 develop a separate near-minimal branch under `sigma_B=o(D)`. The existing C34 estimate only gave `q>=(ceil(D)+2)/2`, so that branch was not excluded.

The implication attacked here is

```text
ZF row count + full diameter support
  -> h >= delta
  -> Hopf-Pannwitz h <= q
  -> q >= delta and sigma_B >= delta-2
  -> the C33 near-minimal boundary branch is impossible.
```

A second consequence combines the same stronger endpoint count with CR4, and a third combines ZF with C18 to show that no single diameter star can contain all active diameter edges.

## 2. Strongest genuinely new audited theorem

### Theorem ZS — ZF boundary-surplus collapse

Assume a sufficiently large triangle-free global minimizer has been chosen first to minimize the number of unit contacts and then to minimize the number of diameter pairs. Work in the fully force-visible C-II branch with the relative-interior stress and the audited ZR/ZF conclusions. Let

- `v` be the number of nonisolated contact-core vertices;
- `e` be the number of unit-contact edges in that core;
- `h` be the number of actual diameter pairs;
- `q=|B_+|` be the number of actual diameter endpoints;
- `delta` be the contact-graph diameter.

Define the two exact nonnegative slacks

$$
r_E:=2v-\delta-2-e\ge0
\tag{ZS.1}
$$

and

$$
s_Z:=e+h-(2v-2)\ge0.
\tag{ZS.2}
$$

Then

$$
\boxed{h=\delta+r_E+s_Z,}
\tag{ZS.3}
$$

$$
\boxed{q\ge h\ge\delta\ge\lceil D\rceil,}
\tag{ZS.4}
$$

and therefore

$$
\boxed{
\sigma_B=2q-\delta-2
\ge
\delta+2r_E+2s_Z-2
\ge
\lceil D\rceil-2.
}
\tag{ZS.5}
$$

In particular, along every unbounded hypothetical C-II sequence satisfying the audited ZF hypotheses,

$$
\liminf\frac{\sigma_B}{D}\ge1.
\tag{ZS.6}
$$

Thus the C33 near-minimal boundary phase `sigma_B=o(D)` cannot occur on the ZF route.

The connected terminal-path theorem CR4 consequently improves from the old C34-based count to

$$
\boxed{
\nu_{B_+}(C)
\ge
\left\lceil\frac{q-1}{4}\right\rceil
\ge
\left\lceil\frac{\lceil D\rceil-1}{4}\right\rceil,
}
\tag{ZS.7}
$$

and the positive circular-planar contact network contains at least

$$
\boxed{
\left\lfloor\frac{q-1}{8}\right\rfloor
\ge
\left\lfloor\frac{\lceil D\rceil-1}{8}\right\rfloor
}
\tag{ZS.8}
$$

pairwise terminal-disjoint strict size-two circular response minors. The previously recorded consequence from C34 was only `floor(ceil(D)/16)`.

### Proof

Eppstein's bound (1.2) gives `r_E>=0`. ZF gives `s_Z>=0`. Rearranging their definitions,

$$
\begin{aligned}
\delta+r_E+s_Z
&=\delta+(2v-\delta-2-e)+(e+h-2v+2)\\
&=h,
\end{aligned}
$$

which proves (ZS.3).

By the lexicographic restoration, the relative-interior diameter support is the full actual diameter graph. Its vertex set is exactly `B_+`, so it has `q` nonisolated vertices and `h` edges. The classical Hopf–Pannwitz planar diameter-graph bound, already used canonically in C66, gives

$$
h\le q.
\tag{ZS.9}
$$

Combining (ZS.3), `r_E,s_Z>=0`, and the contact-path comparison `delta>=ceil(D)` proves (ZS.4).

Now

$$
\begin{aligned}
\sigma_B
&=2q-\delta-2\\
&\ge2h-\delta-2\\
&=2(\delta+r_E+s_Z)-\delta-2\\
&=\delta+2r_E+2s_Z-2,
\end{aligned}
$$

which proves (ZS.5), and (ZS.6) follows because `D->infinity` on any unbounded-cardinality sequence.

Finally CR4 applies to the positive contact graph because C26/C35 give terminal degree at most three and nonterminal degree at most five. It gives `nu_{B_+}(C)>=ceil((q-1)/4)`. Pairing disjoint terminal paths gives at least `floor((q-1)/8)` terminal-disjoint circular two-connections, each with a strict size-two response minor. Substitute `q>=ceil(D)` from (ZS.4) to obtain (ZS.7)–(ZS.8). `square`

### Scope

ZS is conditional on the audited report-level ZR/ZF chain. It concerns the actual lexicographically normalized global source and its nonisolated contact core. It does not constrain contact-isolated source positions and does not produce a numerical lower bound on any strict circular minor.

### Dependencies

- `docs/targets/target-c/56-ci-restored-frontier.md`: promoted C-I finite integration and the contact/diameter lexicographic normal form.
- `docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md`: ZR and ZF.
- `docs/reports/campaign_zero_transfer_defect_review_2026-09-09.md`: independent consolidated audit that Z, ZC, ZR, ZF, and ZB survive under their stated dependencies.
- `docs/targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md`: definition and role of `sigma_B`.
- `docs/targets/target-c/22-diameter-matching-minor-frontier.md`: canonical use of the Hopf–Pannwitz bound `|H|<=|B|`.
- `docs/reports/target_c_terminal_path_packing_connected_refinement_2026-08-31.md`: CR4.

### Why it is new

The September 9 ZF report stops at `h>=delta>=ceil(D)`. The C33/C34 modules predate ZF and retain only `2q>=delta+2`. The campaign ledger uses `h<=q` inside the pure-rhombic ZB contradiction but does not feed it back into the general C33 phase split. The combination therefore removes a general C-II branch that remains live in the active pre-ZF boundary modules and doubles the certified linear family of terminal-disjoint strict response minors.

## 3. Diameter support cannot be a star

The same ZF edge-count lower bound interacts with the global C18 diameter-angle theorem.

Let

$$
\Theta(D)=
\frac{
D(5\pi/6-\sqrt3)+4\pi/3+\pi/(2D)
}{D+1},
\tag{3.1}
$$

and put

$$
a_D=2\arcsin\frac1{2D}.
\tag{3.2}
$$

For all sufficiently large `D`, `Theta(D)<pi/3`. At a diameter vertex `z`, C18 puts every pair of diameter-partner directions in angular separation `<Theta(D)`. Unit separation of two partners on the radius-`D` circle gives angular separation at least `a_D`. Ordering the `deg_H(z)` partner directions inside their common arc therefore gives

$$
(\deg_H(z)-1)a_D<\Theta(D),
$$

hence the safe integer bound

$$
\boxed{
\deg_H(z)\le
\left\lceil\frac{\Theta(D)}{a_D}\right\rceil.
}
\tag{3.3}
$$

Since `D a_D->1` and

$$
\Theta(D)\longrightarrow
\theta_\infty:=\frac{5\pi}{6}-\sqrt3
=0.8859430704\ldots<1,
$$

we obtain

$$
\boxed{
\limsup_{D\to\infty}\frac{\Delta(H)}D
\le\theta_\infty<1.
}
\tag{3.4}
$$

Together with ZF's `h>=ceil(D)`, for every diameter vertex `z`,

$$
\boxed{
\liminf_{D\to\infty}
\frac{h-\deg_H(z)}D
\ge
1-\theta_\infty
=0.1140569295\ldots.
}
\tag{3.5}
$$

Thus every proposed mechanical star center misses a linear number of actual active diameter edges. In particular the full diameter support is not a star for all sufficiently large survivors.

This does **not** contradict C66. C66 only says that in a near-zero response-defect sequence the normalized `beta` mass may concentrate on one star. Equation (3.5) says the remaining linear family of off-star edges is still present in the relative-interior support; their total positive weight may tend to zero. No uniform positive lower bound for their individual or aggregate weights is currently available.

For sufficiently large sources, C43 also excludes a diameter triangle. Hence the nonstar support has a matching of size at least two, but no linear matching bound follows from (3.4): a two-hub/caterpillar-type thrackle can still have linear edge count and bounded matching number under degree information of order `D`.

## 4. Exact target implication

The Z route no longer needs to analyze the asymptotic normal form in `04-near-minimal-response-frontier.md` as a possible survivor. Once ZF is accepted, every survivor satisfies the stronger exact phase condition

$$
\sigma_B\ge\lceil D\rceil-2.
\tag{4.1}
$$

The remaining C-II source is therefore a **linear boundary-surplus** source with

$$
q\ge h\ge\delta\ge\lceil D\rceil,
\tag{4.2}
$$

at least `floor((ceil(D)-1)/8)` terminal-disjoint strict circular minors, and a diameter support that has `Omega(D)` edges outside every one-star support.

This is a strict reduction of the pre-ZF branch ledger, but it does not change the exact scalar contradiction required by the campaign:

$$
\boxed{
 b+\sum_F(\deg F-4)>2h.
}
\tag{4.3}
$$

Equivalently, a closing proof must still force `e+h<=2v-3` for the same actual source.

## 5. Exact remaining lemma

### Boundary-surplus face theorem

There exists `D_0` such that every triangle-free lexicographically normalized global minimizer in the audited C-II/ZF class with `D>=D_0` satisfies

$$
\boxed{
 b+\sum_{F\text{ bounded}}(\deg F-4)>2h.
}
\tag{5.1}
$$

It is enough to prove this only under the now-derived restrictions

$$
q\ge h\ge\delta\ge\lceil D\rceil,
\qquad
\sigma_B\ge\lceil D\rceil-2,
\tag{5.2}
$$

plus the C18 off-star support bound (3.3).

A response-based substitute would also suffice if it converts the strengthened CR4 family into an **aggregate numerical** response defect that yields a strict sub-`D` competitor or the same face inequality. Strictness of linearly many minors without magnitude is still insufficient.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Theorem Z | proved and report-level promotable, subject to normal review | The September 9 consolidated audit finds the all-gap split argument, terminal coverage, and two-edge regression correct. |
| ZC | proved under stated C-II inputs | Z plus SEPq excludes C56-Z for `D>=9`. |
| ZR | proved under audited C56-G input | SVD and Schur elimination give `ker Omega=span(1,P_x,P_y)` on the nonisolated core. |
| ZF | proved under ZR and promoted finite integration | Mixed rigidity gives `e+h>=2v-2`; isolates are not included in `v`. |
| ZB | proved only for the pure strict-rhombic disk class | It uses the Target B exposed-hull theorem; it is not a general-topology closure. |
| `q>=h>=delta` | proved here under ZF | Hopf–Pannwitz is applied to the full actual diameter graph supplied by the lexicographic normal form. |
| `sigma_B>=ceil(D)-2` | proved here under ZF | Exact consequence of `q>=h>=delta`. |
| Near-minimal C33 phase survives ZF | false | It contradicts `sigma_B>=ceil(D)-2`. |
| Linear strict-minor count gives a trace gap | not proved | Positive circular minors can have arbitrarily small magnitude. |
| Linear off-star support gives positive off-star beta mass | not proved | Relative-interior positivity has no uniform quantitative floor. |

## 7. Regression tests and failed implications

### Regular odd shells

A regular unit odd `q`-gon has `v=e=h=q` and violates the desired face inequality. It also lies deeply in the boundary-surplus phase: its contact-graph diameter is about `q/2`, so `sigma_B` is linear. Thus

```text
linear boundary surplus -> face contradiction
```

is false without global-optimality information. The shell is excluded from the Level I hypotheses for large `q` because it is not globally diameter-minimal.

### Filled shell / strict interior approximation

Adding a near-triangular strict interior population can reproduce leading packing density while leaving the shell-like contact core. This continues to block any argument that uses only asymptotic density plus (4.1); exact global optimality must enter the closing theorem.

### Stress-star versus support-star

Equation (3.5) kills an exact support star but not an asymptotic **weight** star. The implication

```text
Omega(D) positive off-star edges -> Omega(1) off-star beta mass
```

has no proof and is precisely the kind of unsupported conductance floor rejected elsewhere in the repository.

### Same-hull saturation

The contact-minimal replacement argument that a source hull can be unit-covered is already present in Target A Section 125. It is not new and by itself does not control the outer-shell population.

### Rhombus-face rattler exclusion

The observation that a strict unit-rhombus face contains no additional source point is already the C49 rattler-localization report and active cavity frontier. It is not new.

## 8. Literature imported

No new literature theorem is imported by this report.

The only external graph fact used is the classical Hopf–Pannwitz planar diameter bound `|E(H)|<=|V(H)|`, already part of the active C66 frontier and therefore an existing project dependency. The run did not identify a stronger published edge/face theorem with the global-optimality hypothesis needed for (5.1).

## 9. Computation and reproducibility

No new computation was used. All new statements are exact algebraic or geometric consequences of existing audited theorems.

The September 9 campaign's exact verification scripts remain relevant to the Z/ZC/ZR/ZF dependency audit, but none is a logical dependency of the new deductions beyond the already-reviewed report-level inputs.

## 10. Canonical promotion recommendation

**Hold as report.**

The proof is short and exact, but its strongest input ZF is still report-level mathematics. Per the active prompt, do not modify canonical route maps merely because the consequence is useful. If ZR/ZF are explicitly promoted after review, then this theorem should be folded into:

- `docs/targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md` to retire the `sigma_B=o(D)` branch on the ZF route;
- the terminal-path/minor frontier to replace the `D/16` strict-minor count by the `D/8` count;
- the C66/C71 star frontier to record the distinction between a weight star and the necessarily nonstar full support;
- the active Target C continuation prompt.

## 11. Next run

Attack (5.1) only in the narrowed ZS class. Two concrete routes remain worth testing:

1. combine the linear boundary surplus and `q>=h>=delta` with DT's exact stopped-train currency, looking for a global-optimality estimate that pays the full `2 f_exc` loss rather than an `O(D)` remainder;
2. use the `Omega(D)` off-star active diameter support together with C66/C68/C70/C71 to prove an aggregate lower bound on off-star mechanical or response mass. A bound of the required magnitude must come from source geometry/global optimality, not positivity alone.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Strongest new theorem:
Assuming audited ZR/ZF, let r_E=2v-delta-2-e and
s_Z=e+h-(2v-2). Then
    h=delta+r_E+s_Z,
    q>=h>=delta>=ceil(D),
and
    sigma_B=2q-delta-2
           >=delta+2r_E+2s_Z-2
           >=ceil(D)-2.
Therefore the C33 sigma_B=o(D) near-minimal branch is impossible on the ZF route.
CR4 improves to at least floor((ceil(D)-1)/8) terminal-disjoint strict minors.

C18 + unit separation also gives
    deg_H(z) <= ceil(Theta(D)/(2 asin(1/(2D)))),
so limsup Delta(H)/D <= 5pi/6-sqrt(3)=0.885943... .
Since h>=D, every proposed star center misses at least
(0.114056...-o(1))D actual diameter edges. This kills support-star equality,
not weight-star concentration.

Exact endpoint now:
Prove b+sum_F(deg F-4)>2h for the narrowed linear-boundary-surplus ZF class.

Binding regressions/no-go results:
regular odd shells; filled shell approximants; no conductance floor from positivity;
same-hull saturation and rhombus-rattler localization are already canonical/report-level old results.

Highest-value next lemma:
Boundary-surplus face theorem (5.1), or a source-specific aggregate off-star
weight/response lower bound strong enough to imply it.

Authoritative dependencies:
docs/targets/target-c/56-ci-restored-frontier.md
docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md
docs/reports/campaign_zero_transfer_defect_review_2026-09-09.md
docs/targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md
docs/targets/target-c/22-diameter-matching-minor-frontier.md
docs/reports/target_c_terminal_path_packing_connected_refinement_2026-08-31.md
docs/reports/target_c_explicit_diameter_angle_gap_2026-08-31.md
```
