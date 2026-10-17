# Target C-II — upgrade shallow-tooth apex injectivity to internal-edge injectivity

**Date:** 2026-09-14  
**Base comparison:** main commit `2bb7078aa8ea9c84c0acca24b6598da87c218f6a`  
**Status:** proof-only Type-II strengthening; theorem-state authority unchanged  
**LEVEL I STATUS:** `STILL OPEN`

Main now proves that, for

\[
\alpha_\eta<\pi/12,
\]

`eta`-shallow two-edge outer teeth have pairwise distinct unloaded apexes.  Its edge
count still loses a factor two because the chosen extra contact at one shallow apex
could a priori be chosen from the other endpoint as well:

\[
E_{pen}(\eta)\ge {1\over2}N_{sh}(\eta).
\]

The fixed-scale Type-II local-flatness argument in
`target_c_shallow_tooth_internal_penetration_2026-09-14.md` closes exactly this gap.
It proves two additional facts.

1. A two-edge tooth apex has no loaded unit-contact neighbor except its two base
   endpoints.  Therefore every mandatory third contact is an internal
   unloaded-to-unloaded contact of the same harmonic component.
2. For an `eta`-shallow tooth, every such extra contact ends more than `sqrt(3)/2`
   inside the tooth-base support line.  A second shallow tooth apex is within
   `sin(alpha_eta)<sin(pi/12)` of its own nearby loaded-hull support line.  Type-II
   fixed-scale flatness makes nearby support lines differ by `o(1)`, so the deep
   endpoint cannot itself be a shallow tooth apex.

Consequently a contact edge selected at one shallow apex cannot be selected at another
shallow apex.  The selection is edge-injective, not merely apex-injective:

\[
\boxed{
E_{int}(\eta)
\ge N_{sh}(\eta)
\ge N_2-{d_{out}\over\eta}.
}
\tag{IU.1}
\]

Every counted edge is internal to one unloaded positive-contact component.

## Current low-`t` count

Use main's exact convenient choice

\[
\eta={1\over15}.
\]

At the current AG42/§171 floor,

\[
{N_2\over D}
\ge0.4363893718701161781\ldots-o(1),
\]

and

\[
{d_{out}\over D}\le0.002883975+o(1).
\]

Therefore

\[
\boxed{
{E_{int}(1/15)\over D}
\ge
0.4363893718701161781\ldots
-15(0.002883975)
-o(1)
=0.3931297468701161781\ldots-o(1).
}
\tag{IU.2}
\]

The corresponding edge normal component is the main-certified value

\[
\boxed{
Y_{1/15}
={29\sqrt3-\sqrt{59}\over60}
=0.7091387945271472222\ldots .
}
\tag{IU.3}
\]

Thus this same explicit cohort has total local-normal penetration at least

\[
\boxed{
0.2787835547882367\ldots D-o(D).
}
\tag{IU.4}
\]

If the objective is local-normal flux rather than edge count, the slightly smaller
choice `eta=0.06` from the parent note gives the marginally stronger certified flux

\[
0.2790071278755881\ldots D-o(D)
\]

with `0.3883231218701161...D` distinct internal edges.  The count supremum as
`eta` tends to `2(1-cos(pi/12))` from below is

\[
0.3940702972468222\ldots D-o(D).
\]

## What is genuinely new relative to main

The main apex-injectivity theorem proves

\[
E_{pen}(1/15)/D\ge0.1965648734350580\ldots-o(1)
\]

for physical penetration contacts whose loaded/unloaded classification is not used in
its counting argument.  Equation (IU.2) doubles that floor and places every counted
edge inside an unloaded component:

\[
0.1965648734\ldots
\quad\longrightarrow\quad
0.3931297468\ldots .
\]

This is the useful form for the component ledger.  Future compositions may charge the
cohort directly to the internal edge variables `e_r`, Eppstein slacks `r_r`, pinned
surpluses `s_r`, attachment-cell geometry, or componentwise source-preserving
perturbations.

No KKT weight floor is asserted, and C-II remains open.
