# Target C-II — a three-cut shear kernel sits inside the high-`t` macroscopic rectangle

**Date:** 2026-09-15  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** high-`t` complete rectangle and orientation extraction; high-`t` rectangle joint-cusp budgets; exact arbitrary O--O finite multishear; canonical mixed infinitesimal rigidity and full-support KKT stress  
**Certificate:** `research/verify_target_c_high_t_rectangle_three_cut_kernel_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current high-`t` rectangle gives a consecutive O--O row block

\[
A_*=(\tau_1,\ldots,\tau_m),
\qquad
m>0.0000226D-o(D),
\]

and, after the existing orientation extraction, a pairwise-noncrossing common column family

\[
B_+,
\qquad
|B_+|>0.1567D-o(D),
\]

such that every row crosses every column in one strict rhombus, with one common crossing order and one common real orientation branch.

The adjacent joint-cusp theorem spends the global switching, terminal, KKT-mass, and angular-defect currencies on one row interface.  Averaging the same currencies over **two consecutive interfaces simultaneously** gives a three-row object.  For some three consecutive rows

\[
\tau_i,\tau_{i+1},\tau_{i+2}
\]

whose two internal interfaces are nonhub, one has

\[
\boxed{
(C_i+C_{i+1})+(S_i+2S_{i+1}+S_{i+2})<2{,}216{,}000,
}
\tag{HK.1}
\]

where

\[
C_j:=N_j+L_j+D B_j
\]

uses the same notation as the joint-cusp theorem and

\[
S_j:=\sum_{b\in B_+}
\left(\theta(\tau_j,b)-{\pi\over3}\right).
\]

Consequently:

\[
\boxed{
N_i+N_{i+1}<2{,}216{,}000,
\qquad
L_i+L_{i+1}<2{,}216{,}000,
}
\tag{HK.2}
\]

\[
\boxed{
B_i+B_{i+1}<{2{,}216{,}000\over D},
}
\tag{HK.3}
\]

and the sum of the two oriented row-phase gaps obeys

\[
\boxed{
|\alpha_{i+1}-\alpha_i|+|\alpha_{i+2}-\alpha_{i+1}|
<{1.4142\times10^7\over D}+o(D^{-1}).
}
\tag{HK.4}
\]

Moreover there is a retained common column family

\[
B_0\subset B_+,
\qquad
\boxed{|B_0|>0.0783D-o(D),}
\tag{HK.5}
\]

such that every `b in B_0` crosses all three selected rows in the common order and

\[
\boxed{
0<\theta(\tau_j,b)-{\pi\over3}
<{2.8284\times10^7\over D}+o(D^{-1})
\quad(j=i,i+1,i+2).
}
\tag{HK.6}
\]

The three row directions have an exact nonzero planar dependence

\[
\boxed{
c_1u_i+c_2u_{i+1}+c_3u_{i+2}=0.}
\tag{HK.7}
\]

Using these coefficients in the audited arbitrary O--O multishear gives a non-Euclidean contact infinitesimal flex for which every actual diameter row outside

\[
H_{exc}:=H_{sw,i}\cup H_{sw,i+1}
\]

has zero first squared-length derivative **exactly**.  Thus

\[
\boxed{|H_{exc}|<2{,}216{,}000+o(1)}
\tag{HK.8}
\]

and canonical KKT stationarity gives

\[
\boxed{
\sum_{h\in H_{exc}}\beta_h\ell_h=0.
}
\tag{HK.9}
\]

The flex is non-Euclidean, so mixed infinitesimal rigidity and `beta_h>0` force both signs:

\[
\boxed{
\exists h_+,h_-\in H_{exc}:
\ell_{h_+}>0>\ell_{h_-}.
}
\tag{HK.10}
\]

If the three selected row directions span `R^2`, the kernel integrates by the implicit-function theorem to a nonconstant exact finite O--O multishear curve.  Along that curve every old unit contact is preserved exactly and every actual diameter row outside `H_exc` is unchanged exactly.  Hence the full nonlinear diameter obstruction is confined to the same bounded exceptional set while the macroscopic ordered transverse scaffold `B_0` remains present.

This is the high-`t` analogue of the earlier three-cut kernel cusp, but it is embedded in a linear-by-linear near-triangular rectangle rather than an isolated path triple.

---

## 1. Two-interface finite/KKT budget

For each internal rectangle interface let

\[
C_j=N_j+L_j+D B_j.
\]

The audited global budgets used by the adjacent joint-cusp theorem give, even after restriction to the rectangle block,

\[
\sum_j C_j
\le K_{glob}D+o(D),
\qquad
K_{glob}=10T-2\pi+2,
\quad T=1.8687.
\tag{HK.11}
\]

Numerically `K_glob=14.40381469...`, but the certificate uses an outward Machin enclosure for `pi`.

For a consecutive triple define the two-interface cost

\[
C_j+C_{j+1}.
\]

When this quantity is summed over all consecutive row triples, each interface cost occurs at most twice. Therefore

\[
\sum_{\text{triples}}(C_j+C_{j+1})
\le2K_{glob}D+o(D).
\tag{HK.12}
\]

Delete the `O(1)` triples meeting the unique diameter-routing hub or a block endpoint.  The number of eligible triples remains

\[
>0.0000226D-o(D).
\]

Both selected interfaces are then nonhub and retain the audited one-sided switching orientation toward the common hub.

---

## 2. Three-row angular budget

Use the consistent real orientation from the high-`t` rectangle phase theorem.  For row `tau_j` and common column `b in B_+`, put

\[
\delta_{jb}:=\theta(\tau_j,b)-{\pi\over3}>0,
\qquad
S_j:=\sum_{b\in B_+}\delta_{jb}.
\tag{HK.13}
\]

All these crossings are distinct strict rhombi, so the canonical angular-defect budget gives

\[
\sum_jS_j<C_{phase}D,
\qquad
C_{phase}={\pi^2\sqrt3(2+\sqrt3)\over12}.
\tag{HK.14}
\]

For a consecutive triple define

\[
W_j:=S_j+2S_{j+1}+S_{j+2}.
\tag{HK.15}
\]

Each row defect `S_j` occurs with total coefficient at most four when `W_j` is summed over all triples. Hence

\[
\sum_{\text{triples}}W_j<4C_{phase}D.
\tag{HK.16}
\]

Combining (HK.12) and (HK.16), some eligible triple satisfies

\[
(C_j+C_{j+1})+W_j
< {2K_{glob}+4C_{phase}\over0.0000226}+o(1).
\]

The exact certificate proves

\[
{2K_{glob}+4C_{phase}\over0.0000226}
=2{,}215{,}649.17\ldots
<2{,}216{,}000,
\]

which proves (HK.1)--(HK.3) and (HK.8).

---

## 3. The same triple is inverse-`D` phase-close

Let the real row phases be `alpha_j` and common column phases be `beta_b`, so on the selected oriented branch

\[
\delta_{jb}=\beta_b-\alpha_j-{\pi\over3}.
\]

For every `b in B_+`,

\[
|\alpha_{j+1}-\alpha_j|
\le\delta_{jb}+\delta_{j+1,b}.
\]

Summing over `B_+` gives

\[
|B_+|\left(
|\alpha_{i+1}-\alpha_i|+|\alpha_{i+2}-\alpha_{i+1}|
\right)
\le W_i.
\tag{HK.17}
\]

Using `|B_+|>0.1567D-o(D)` and (HK.1), the exact certificate proves

\[
{2{,}216{,}000\over0.1567}<1.4142\times10^7,
\]

which is (HK.4).

For each common column put

\[
x_b:=\delta_{ib}+\delta_{i+1,b}+\delta_{i+2,b}.
\]

Then

\[
\sum_{b\in B_+}x_b
=S_i+S_{i+1}+S_{i+2}
\le W_i
<2{,}216{,}000.
\]

Markov therefore leaves at least half of `B_+` with

\[
x_b\le{2(2{,}216{,}000)\over|B_+|}.
\]

The exact certificate verifies

\[
{2(2{,}216{,}000)\over0.1567}<2.8284\times10^7.
\]

Every summand of `x_b` is nonnegative, proving (HK.5)--(HK.6).  The common crossing order is inherited from the parent rectangle.

---

## 4. Exact three-cut infinitesimal kernel

Let the selected shore-oriented unit row vectors be

\[
u_1:=u_i,
\qquad
u_2:=u_{i+1},
\qquad
u_3:=u_{i+2}.
\]

Three planar vectors are linearly dependent, so choose nonzero `c=(c_1,c_2,c_3)` with

\[
\sum_{j=1}^3c_ju_j=0.
\tag{HK.18}
\]

Apply the exact arbitrary O--O multishear to these three trains and take the infinitesimal direction `theta_j=t c_j`.

For an actual diameter row `h`, let `sigma_hj` be its signed shore incidence.  Since the three cuts are consecutive on one laminar path, every incidence pattern is a contiguous signed interval.  If `h` belongs to neither internal switching set, then

\[
(\sigma_{h1},\sigma_{h2},\sigma_{h3})=(0,0,0)
\]

or, after one global orientation of `h`,

\[
(\sigma_{h1},\sigma_{h2},\sigma_{h3})=(1,1,1).
\]

The multishear first-variation vector is

\[
A_h(c)=\sum_{j=1}^3\sigma_{hj}c_jJu_j.
\]

Thus outside `H_exc`, either `A_h(c)=0` trivially or

\[
A_h(c)=J\sum_jc_ju_j=0
\]

by (HK.18).  Every nonexceptional actual diameter row therefore has zero first derivative exactly.

---

## 5. Positive KKT stress forces both exceptional derivative signs

The selected multishear infinitesimal motion preserves every old unit contact to first order.  It is not Euclidean: the common transverse family `B_+` is nonempty and none of its train coordinates is selected, while `c` is nonzero.  A global infinitesimal rotation would assign one common angular rate to every complete train, which is impossible here.

Canonical mixed infinitesimal rigidity therefore forbids all actual diameter derivatives from vanishing.  Since every nonexceptional diameter derivative is zero, at least one `ell_h` with `h in H_exc` is nonzero.

KKT stationarity on this contact flex gives

\[
\sum_h\beta_h\ell_h=0.
\]

All nonexceptional terms vanish and the relative-interior normalization has `beta_h>0` for every actual diameter row.  Hence the nonzero exceptional derivatives cannot have one sign.  This proves (HK.9)--(HK.10).

---

## 6. Rank-two case integrates to an exact finite kernel curve

Assume

\[
\operatorname{span}\{u_1,u_2,u_3\}=\mathbb R^2.
\]

For finite shear angles define

\[
\Phi(\theta_1,\theta_2,\theta_3)
:=\sum_{j=1}^3(R_{\theta_j}u_j-u_j).
\tag{HK.19}
\]

The derivative `D Phi(0)` has columns `Ju_j` and hence rank two.  Its kernel contains `c`.  By the implicit-function theorem, `Phi^{-1}(0)` contains a nonconstant smooth local curve through zero tangent to a nonzero kernel direction.

Along this curve the audited arbitrary O--O multishear preserves every old unit contact exactly.  A source pair whose selected-cut incidence is `(0,0,0)` is unchanged.  A pair whose incidence is `(1,1,1)` has total finite increment `Phi(theta)=0` and is also unchanged exactly.  Therefore every actual diameter row outside `H_exc` is unchanged exactly along the finite curve.

Strict old noncontact lower-distance inequalities and strict old nondiameter upper-distance inequalities remain strict for sufficiently small parameters by finiteness and continuity.  The only nonlinear diameter constraints left are the actual diameter rows in the bounded exceptional set `H_exc`.

The rank-one direction case is not promoted to a finite-curve claim here; it retains the exact infinitesimal kernel and exceptional-sign conclusion above.

---

## 7. Frontier effect

The live high-`t` normal form through `t<=1.8687` can now be sharpened to

```text
three consecutive O-O rectangle rows
+ >0.0783 D ordered common transverse columns
+ every retained row-column angle = pi/3 + O(1/D)
+ total two-row phase drift < 1.4142e7/D
+ exact nonzero three-cut shear kernel
+ <2,216,000 exceptional actual diameter rows
+ exceptional KKT mass <2,216,000/D
+ <2,216,000 terminal face-side occurrences across the two layers
+ positive-stress exceptional derivatives of both signs
+ both internal interfaces nonhub and one-sided toward the common diameter hub
+ in the rank-two case, an exact finite contact-preserving kernel curve on which
  every nonexceptional diameter row is unchanged exactly.
```

This is not a C-II closure.  It replaces the single-interface cusp by a finite nonlinear diameter problem embedded inside a macroscopic ordered near-triangular scaffold.  The remaining closing target is now finite: use the three-row scaffold and the one-sided ordered switching sets to rule out the residual exceptional diameter inequalities, or produce a small kernel-curve parameter that weakly shortens all of them and strictly shortens at least one.

**Disposition:** proved proof-only high-`t` three-cut kernel embedded in the complete rectangle through `t<=1.8687`. C-II and Level I remain open.
