# Target C-II — a stricter energy slice forces a `>0.697D` common transverse ladder through `t<=1.8687`

**Date:** 2026-09-15  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** coupled paired-remainder path theorem through `1.8687`; finite-defect KKT-strip theorem; audited train-length/terminal-energy tradeoff; simple triangle-free stopped-train crossing graph  
**Certificate:** `research/verify_target_c_long_common_ladder_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current common-ladder theorem uses the broad adaptive terminal-energy cutoff from the path theorem.  That cutoff is designed to maximize path coverage, not to maximize the geometric length of the selected boundary trains.  The paired-remainder energy budget allows a much stricter selection while retaining a positive linear path.

Fix the constant cutoff

\[
\boxed{e_\tau<\lambda_0:=0.392.}
\tag{LL.1}
\]

Through `t<=1.8687`, this stricter slice still contains more than

\[
\boxed{0.0005D-o(D)}
\tag{LL.2}
\]

retained dominant O–O pair weight.  Hence one of at most three dominant phase windows contains more than

\[
\boxed{{D\over6000}-o(D)}
\tag{LL.3}
\]

actual selected O–O complete trains.  Every such train crosses more than

\[
\boxed{0.697D-o(D)}
\tag{LL.4}

other complete trains.

Re-running the finite-defect averaging on this stricter path gives two consecutive selected trains `tau_0,tau_1` bounding a nonhub region with total finite defect below `87000`.  In particular,

\[
|\Gamma(\tau_0)\triangle\Gamma(\tau_1)|\le86999.
\tag{LL.5}
\]

Combining (LL.4) and (LL.5) forces

\[
\boxed{
|\Gamma(\tau_0)\cap\Gamma(\tau_1)|
>0.697D-o(D).
}
\tag{LL.6}

The common family is pairwise noncrossing.  Thus the live high-`t` strip contains an ordered train-crossing

\[
\boxed{K_{2,M},\qquad M>0.697D-o(D),}
\tag{LL.7}

through the entire range `t<=1.8687`, while the same strip has only a fixed number of exceptional/terminal/diameter-switch defects.

---

## 1. Inherited coupled feasibility barrier

Use the endpoint notation from the coupled paired-remainder theorem at

\[
T=1.8687.
\]

That theorem supplies

\[
z_0=2.0477,
\qquad
d_0=F(z_0),
\qquad
F(s)=s-6\sin(s/6),
\]

and the exact coupled barrier

\[
\boxed{
z\ge z_0+1.36(\delta-d_0)-o(1),}
\tag{LL.8}
\]

for

\[
d_0-o(1)\le\delta<0.107+o(1).
\tag{LL.9}

The matched train floor gives the more precise endpoint ceiling

\[
\delta\le\delta_{max}+o(1),
\qquad
\delta_{max}=0.1068695395\ldots .
\tag{LL.10}

The hostile audit of the parent theorem already certifies the pair/remainder decomposition

\[
E_{pair}+F(z-2P)\le\delta+o(1),
\tag{LL.11}

with no energy double count.

---

## 2. A fixed `0.392` threshold still leaves a linear path

Let `P` be retained dominant O–O pair weight.  Weighted Markov applied to (LL.11) at the fixed threshold `lambda_0=0.392` gives

\[
P_{low}
\ge
P-{\delta-F(z-2P)\over\lambda_0}-o(1).
\tag{LL.12}

The endpoint-count floor is

\[
P\ge z-U_0(t)+2\delta+\kappa/2-o(1),
\qquad
U_0(t)={9t\over2}-2\pi.
\tag{LL.13}

As in the parent audit, the right side of (LL.12) increases with `P`, while the adverse source parameters are `t=T` and `kappa=0`.  Insert the coupled lower line (LL.8), and write

\[
z(\delta)=z_0+c(\delta-d_0),
\qquad c=1.36,
\]

\[
P(\delta)=z(\delta)-U_0(T)+2\delta,
\]

\[
r(\delta)=2U_0(T)-z(\delta)-4\delta.
\]

Then the lower-bound function is

\[
L(\delta)
=P(\delta)-{\delta-F(r(\delta))\over\lambda_0}.
\tag{LL.14}

Along the coupled line,

\[
P'=c+2=3.36,
\qquad
r'=-(c+4)=-5.36,
\]

so

\[
L'
=c+2-{1+(c+4)F'(r)\over\lambda_0}.
\tag{LL.15}

The exact certificate proves throughout the endpoint box

\[
0<r<2.047,
\qquad
F'(r)<0.0582.
\]

Therefore

\[
\boxed{L'>0.013.}
\tag{LL.16}

The adverse point is again the minimum-detour edge `delta=d_0`.  Exact outward arithmetic there gives

\[
P>0.0007750,
\qquad
r>2.0461498,
\qquad
F(r)>0.03943054,
\]

and hence

\[
\boxed{P_{low}>0.0005471D-o(D)>0.0005D-o(D).}
\tag{LL.17}

Pigeonholing among at most three phase windows yields (LL.3).  Since pair weight per train is at most one, this is also a lower bound for the number of actual selected O–O trains in that window.

---

## 3. The fixed cutoff gives a much longer boundary train

The exact complement-train incidence theorem gives every selected outer-to-outer train

\[
{r_\tau\over D}
\ge1-\delta-{e_\tau\over2}-o(1),
\tag{LL.18}

where `r_tau` is the number of strict-rhombus crossings along `tau`.

For the family (LL.1), use `e_tau<0.392` and (LL.10):

\[
{r_\tau\over D}
>1-0.10686954-{0.392\over2}-o(1)
>0.697D/D-o(1).
\]

Thus

\[
\boxed{r_\tau>0.697D-o(D).}
\tag{LL.19}

The stopped-train crossing graph is simple, so every traversed strict rhombus is a distinct crossing neighbor.  Hence

\[
\boxed{|\Gamma(\tau)|>0.697D-o(D)}
\tag{LL.20}

for every train in the stricter selected family.

The physical same-oriented terminal branch is uniformly impossible for this family: `lambda_0<1/2`, and at the adverse detour cap the exact certificate has a large positive margin in

\[
\left(1-\delta-{\lambda_0\over2}\right)^2
>\lambda_0-{\lambda_0^2\over4}.
\]

So the selected trains retain the opposite-terminal-arc path topology used in the parent theorem.

---

## 4. Re-run the finite-defect averaging on the stricter path

Use the one-phase path floor

\[
m>{D\over6000}-o(D).
\tag{LL.21}

For each eligible nonhub internal path region let

\[
C_i=N_i+L_i+D B_i
\]

with the same meanings as in the finite-defect theorem: actual diameter interval switches, assigned train-terminal occurrences, and switching KKT multiplier mass.

The exact global budgets remain

\[
\sum_iN_i\le2\pi D,
\]

\[
\sum_iL_i\le(10T-4\pi)D+o(D),
\]

\[
\sum_iDB_i\le2D.
\]

The exact certificate evaluates

\[
{10T-2\pi+2\over1/6000}<87000.
\tag{LL.22}

Deleting the hub and the `O(1)` end layers changes the denominator by only `o(D)`.  Thus for every sufficiently large source there is a nonhub region satisfying

\[
\boxed{C_i<87000.}
\tag{LL.23}

In particular,

\[
N_i\le86999,
\qquad
L_i\le86999,
\qquad
B_i<{87000\over D},
\tag{LL.24}

and there are at most `17399` bounded exceptional faces in the strip.

The crossing-neighborhood argument from the finite-defect theorem applies verbatim:

\[
\boxed{
|\Gamma(\tau_0)\triangle\Gamma(\tau_1)|
\le L_i\le86999.
}
\tag{LL.25}

The same strip also has one-sided diameter switching toward the common hub and a nonzero exact KKT layer reaction generated by one or two actual switching diameter bars.

---

## 5. More than `0.697D` trains cross both strip boundaries

Let

\[
A=\Gamma(\tau_0),
\qquad
B=\Gamma(\tau_1).
\]

Both boundary trains belong to the fixed-cutoff family, so (LL.20) applies to each.  Equation (LL.25) gives

\[
|A\cap B|
\ge\min(|A|,|B|)-|A\triangle B|.
\]

The subtracted term is an absolute constant, hence is `o(D)`.  Therefore

\[
\boxed{|A\cap B|>0.697D-o(D).}
\tag{LL.26}

Every common neighbor is a complete train crossing both boundaries exactly once, with its intervening midpoint subpath lying inside the selected strip.

Any two distinct common neighbors cannot cross one another: together with `tau_0` they would form a triangle in the simple train-crossing graph, which is triangle-free.  Thus the common family is pairwise noncrossing and consistently ordered across the strip.

This proves the macroscopic ordered ladder (LL.7).

---

## 6. Frontier effect

Through `t<=1.8687`, the full-core branch now contains one strip with the simultaneous structure

```text
boundary pair:
  two consecutive same-window O-O complete trains;
  each has terminal energy <0.392;
  each crosses >0.697 D distinct trains;

finite defect:
  N_i+L_i+D B_i <87000;
  <=86999 switching diameter rows;
  <=86999 train terminal occurrences;
  <=17399 bounded exceptional faces;
  crossing-neighborhood symmetric difference <=86999;
  switching KKT mass <87000/D;
  exact nonzero reaction generated by <=2 actual diameter bars;

bulk ladder:
  >0.697 D common transverse complete trains;
  every common train crosses both boundaries once;
  common trains are pairwise noncrossing and ordered.
```

This improves both parts of the previous common-ladder theorem: the endpoint moves from `1.8623` to `1.8687`, and the common ladder density rises from `0.6608` to `0.697`.

The remaining closing problem is no longer to create a large grid.  It is to use this `K_{2,Theta(D)}` grid against the fixed-complexity terminal/exceptional/diameter defect set to produce a source-preserving strict diameter descent or an impossible diameter-endpoint pattern.

**Disposition:** proved proof-only `>0.697D` common-transverse ladder inside a finite-defect nonhub strip through `t<=1.8687`.  C-II and Level I remain open.
