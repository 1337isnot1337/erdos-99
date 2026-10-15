# Target C — near-minimal loaded-boundary response frontier after C45

**LEVEL I STATUS: STILL OPEN.**

This module records C35-C45 in the phase where the C33 boundary surplus

`sigma_B=2|B_+|-delta-2`

is `o(D)`.

## Harmonic interior components

Let `I_1,...,I_{c_I}` be the connected components after deleting `B_+`. C33 gives

`c_I+e_BB <= sigma_B`,

so in the near-minimal phase

`c_I=o(D), e_BB=o(D)`.

C35 proves every loaded vertex has contact degree at most three, and every unpinned component has at least three contact edges to the loaded boundary.

For each component `I_r`, let `A_r` be its distinct loaded attachment vertices. C36 proves

`I_r subset conv(A_r)`

by the positive-KKT discrete maximum principle, and

`|A_r|>=3`.

Distinct attachment sets are noncrossing in cyclic force-hull order.

## Planar attachment incidence

Contract each `I_r` to one interior node and retain one edge to every distinct loaded attachment. Let `q_used` be the number of used loaded vertices and `s` the number of connected incidence components. C37 gives

`sum_r |A_r| <= q_used+2c_I-2s`.

Thus the number of used loaded vertices belonging to multiple attachment sets is at most

`2c_I-2s`.

C38 restores the loaded-loaded unit contacts and uses connectivity of the full contact core:

`e_BB >= s+(q-q_used)-1`.

Hence the number of loaded vertices that either do not touch the interior or belong to multiple attachment sets is at most

`2c_I+e_BB-3s+1 <= 2sigma_B`.

Therefore, when `sigma_B=o(D)`, all but `o(D)` of the `Theta(D)` loaded boundary vertices belong to exactly one of only `o(D)` noncrossing harmonic attachment components.

## Interior diameter cost

C40 quantifies each harmonic component. If `delta_r` is the graph diameter of `C[I_r]` and `t_r` its number of loaded-boundary contact edges, then

`t_r >= delta_r+3`,

`delta_r <= 3|A_r|-3`,

and globally

`sum_r delta_r + 3c_I + 2e_BB <= 3q`.

C44 adds the direct attachment-diameter transport

`diam A_r <= delta_r+2 <= 3|A_r|-1`.

Thus a harmonic component can connect loaded boundary points at a fixed positive fraction of the global diameter only if it consumes a linear number of loaded attachment vertices and has linear internal graph diameter.

## Strict response diameter defect

C41 gives the exact scalar response identity. If `c_bk=-Lambda_bk`, then

`sum_{b<k} c_bk |b-k|^2 = D^2`

and

`(D^2/2) tr(Lambda-L_H)
 = sum_{b<k} c_bk (D^2-|b-k|^2) > 0`.

Hence

`tr Lambda > 2 = tr L_H`,

while C11 still gives

`(Lambda-L_H)1=0`, `(Lambda-L_H)P_B=0`.

## Uniform anti-Reuleaux geometry

C43 gives absolute constants `eta_0>0,n_0` such that every triple of source points in every global minimizer with `n>=n_0` has one pair at distance at most

`rho_0D`, where `rho_0:=1-eta_0<1`.

Equivalently, the graph of pairs longer than `rho_0D` is triangle-free.

Set

`gamma_0:=1-rho_0^2>0`.

Every harmonic response clique contains a positive response pair paying at least `gamma_0D^2` geometric defect per unit conductance.

## C44 response-mass dichotomy

Define the short response mass

`S_short=sum_{|b-k|<=rho_0D} c_bk`.

Because `diam A_r<=3|A_r|-1` and `sum_r|A_r|<=3|B_+|<=3pi D`, only an absolute constant

`K_0=ceil(9pi/rho_0)`

of harmonic components can carry any response edge longer than `rho_0D`.

C41 gives total response conductance `sum c_bk>1`. Therefore exactly one of the following structural alternatives must hold.

### A. Absolute short-response mass

`S_short>=1/2`.

Then C41 gives the absolute trace gap

`tr(Lambda-L_H)>=gamma_0`.

### B. One macroscopic harmonic cell

Some component `I_r` has

`diam A_r>rho_0D`,

`delta_r>rho_0D-2`,

`|A_r|>(rho_0D+1)/3`,

`t_r>rho_0D+1`,

and total response conductance `>1/(2K_0)`.

In the near-minimal phase C37 improves the constant number of possible macroscopic cells from `9pi/rho_0` to asymptotically `3pi/rho_0`.

## C45 stress localization

C45 sharpens Branch B by keeping the long-response mass itself. One macroscopic component satisfies

`L_r=sum_{|s-t|>rho_0D} c_st^(r) > 1/(2K_0)`.

The componentwise C11 Dirichlet identity is

`sum_{e in E_r} alpha_e = sum_{s<t in A_r} c_st^(r)|s-t|^2`,

where `E_r` contains the internal contacts of `I_r` and its contacts to `B_+`.

Therefore

`sum_{e in E_r} alpha_e > [rho_0^2/(2K_0)] D^2`.

So Branch B contains one unloaded harmonic cell carrying a fixed positive fraction of the entire normalized contact-stress budget, simultaneously with linear attachment count, boundary incidence, and graph diameter.

## Current near-minimal normal form

```text
q = Theta(D) loaded boundary nodes
c_I = o(D) harmonic interior components
e_BB = o(D) loaded-loaded contacts
all but o(D) loaded nodes lie in exactly one A_r
A_r form a noncrossing boundary family
I_r subset conv(A_r)
sum delta_r = O(D)
incidence cyclomatic number = o(D)

response defect M=Lambda-L_H:
    M1=0
    MP_B=0
    tr M>0
    (D^2/2)tr M = sum c_bk(D^2-|b-k|^2)

quantitative dichotomy:
    A. S_short >= 1/2
       -> tr M >= gamma_0

    B. one harmonic component I_r has
       long response mass > 1/(2K_0)
       contact stress mass > [rho_0^2/(2K_0)]D^2
       diam A_r > rho_0D
       delta_r > rho_0D-2
       |A_r| > (rho_0D+1)/3
       t_r > rho_0D+1
```

The response problem is therefore no longer a diffuse small-weight problem. The two exact next targets are:

1. exclude the absolute trace-gap branch using the affine kernel, circular-planar minors, diameter-load support, or reciprocal geometry; or
2. exclude the single macroscopic positive-stress harmonic cell using its convex attachment hull, C42 rhombic bulk, reciprocal stress, or a finite-container/global-packing inequality.

No blanket PSD or Loewner comparison for `Lambda-L_H` is assumed.
