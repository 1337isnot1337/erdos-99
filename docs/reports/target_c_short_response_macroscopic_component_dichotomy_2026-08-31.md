<!-- theorem-state: {"artifact_id":"ART-558224CEC489","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C44: short-response mass or one macroscopic harmonic component

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C35-C41, C43, force-hull perimeter bound `|B_+|<=pi D`  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C43 gives a uniform geometric deficit but does not lower-bound the effective conductance carried by the forced short response pair. C44 converts that weakness into a sharp structural dichotomy.

Let

\[
\rho_0:=1-\eta_0\in(0,1),
\qquad
\gamma_0:=1-\rho_0^2>0,
\tag{C44.1}
\]

where `eta_0` is the C43 anti-Reuleaux constant. For the C11 response conductances

\[
c_{bk}:=-\Lambda_{bk}\ge0,
\]

define the total uniformly short response mass

\[
\boxed{
S_{short}:=
\sum_{\substack{b<k\\|b-k|\le\rho_0D}}c_{bk}.
}
\tag{C44.2}
\]

Then there is an absolute integer `K_0<infty`, depending only on `eta_0`, such that every sufficiently large fully force-visible C-II survivor satisfies at least one of the following.

### Branch A — absolute short-response mass

\[
\boxed{S_{short}\ge\frac12.}
\tag{C44.3}
\]

Consequently C41 gives the absolute trace gap

\[
\boxed{
\operatorname{tr}(\Lambda-L_H)\ge\gamma_0.
}
\tag{C44.4}
\]

### Branch B — one macroscopic harmonic response component

There is an unpinned component `I_r` with attachment set `A_r`, graph diameter `delta_r`, boundary-contact count `t_r`, and component response total conductance

\[
C_r:=\sum_{s<t\in A_r}c^{(r)}_{st}
\tag{C44.5}
\]

such that

\[
\boxed{
C_r>\frac1{2K_0},
}
\tag{C44.6}
\]

and

\[
\boxed{
\operatorname{diam}A_r>\rho_0D,
\qquad
\delta_r>\rho_0D-2,
\qquad
|A_r|>\frac{\rho_0D+1}{3},
\qquad
t_r>\rho_0D+1.
}
\tag{C44.7}
\]

Thus failure of an absolute short-response mass cannot be spread through many tiny-conductance components. It forces a **single** harmonic component carrying nonvanishing response conductance, linear graph diameter, and a linear fraction of the loaded boundary incidence.

This is the first quantitative C-II response dichotomy that remains valid despite the absence of any lower bound on individual KKT weights.

---

## 1. Every attachment set has diameter at most `delta_r+2`

Fix an unpinned component `I_r` and two distinct attachments `s,t in A_r`. By definition there are contact edges

\[
sx\in C,
\qquad
ty\in C
\]

with `x,y in I_r`.

Since the induced contact graph on `I_r` is connected and has graph diameter `delta_r`, there is an internal contact path from `x` to `y` using at most `delta_r` edges. Adding the two boundary contact edges gives a contact path from `s` to `t` of length at most

\[
\delta_r+2.
\]

Every contact edge has Euclidean length one, so the triangle inequality gives

\[
|s-t|\le\delta_r+2.
\tag{C44.8}
\]

Taking the maximum over attachments proves

\[
\boxed{
\operatorname{diam}A_r\le\delta_r+2.
}
\tag{C44.9}
\]

C40 gives

\[
\delta_r\le3|A_r|-3,
\]

therefore

\[
\boxed{
\operatorname{diam}A_r\le3|A_r|-1.
}
\tag{C44.10}
\]

This elementary transport from graph diameter to attachment geometry was not used in C40.

---

## 2. Only constantly many components can carry a near-diameter response edge

Call `I_r` **macroscopic** if

\[
\operatorname{diam}A_r>\rho_0D.
\tag{C44.11}
\]

By C44.10, every macroscopic component satisfies

\[
3|A_r|-1>\rho_0D,
\]

hence

\[
\boxed{
|A_r|>\frac{\rho_0D+1}{3}.
}
\tag{C44.12}
\]

C36 gives the global distinct-attachment incidence bound

\[
\sum_r|A_r|\le3|B_+|.
\tag{C44.13}
\]

The force-hull perimeter bound gives

\[
|B_+|\le\operatorname{per}(F)\le\pi D.
\tag{C44.14}
\]

If `M` is the number of macroscopic components, C44.12-C44.14 imply

\[
M\frac{\rho_0D+1}{3}
<
3\pi D,
\]

so

\[
M
<
\frac{9\pi D}{\rho_0D+1}
<
\frac{9\pi}{\rho_0}.
\tag{C44.15}
\]

Fix once and for all

\[
\boxed{
K_0:=\left\lceil\frac{9\pi}{\rho_0}\right\rceil.
}
\tag{C44.16}
\]

Then every sufficiently large C-II survivor has at most `K_0` macroscopic harmonic components.

Every response edge contributed by a nonmacroscopic component has length at most `rho_0D`, because its endpoints both lie in `A_r`. Therefore **all nonshort component response conductance is carried by at most `K_0` macroscopic components.**

Direct loaded-loaded contact response edges have length one, hence are short for sufficiently large `D`.

---

## 3. The full response has total conductance greater than one

Let

\[
C_{resp}:=\sum_{b<k}c_{bk}.
\tag{C44.17}
\]

C41 proves

\[
\boxed{C_{resp}>1.}
\tag{C44.18}
\]

The response decomposes into direct loaded-loaded contacts and the component Schur responses:

\[
C_{resp}
=
C_{BB}^{dir}+\sum_r C_r.
\tag{C44.19}
\]

All terms are nonnegative.

---

## 4. Proof of the dichotomy

If

\[
S_{short}\ge\frac12,
\]

then every term counted in `S_short` has

\[
D^2-|b-k|^2
\ge
(1-\rho_0^2)D^2
=
\gamma_0D^2.
\tag{C44.20}
\]

C41 therefore gives

\[
\frac{D^2}{2}\operatorname{tr}(\Lambda-L_H)
=
\sum_{b<k}c_{bk}(D^2-|b-k|^2)
\ge
\gamma_0D^2S_{short}
\ge
\frac{\gamma_0D^2}{2}.
\]

Cancel `D^2/2` to obtain C44.4. This is Branch A.

Now assume instead

\[
S_{short}<\frac12.
\tag{C44.21}
\]

The total nonshort response mass is

\[
C_{long}:=
\sum_{\substack{b<k\\|b-k|>\rho_0D}}c_{bk}
=
C_{resp}-S_{short}.
\tag{C44.22}
\]

By C44.18 and C44.21,

\[
\boxed{C_{long}>\frac12.}
\tag{C44.23}
\]

No direct loaded-loaded contact contributes to `C_long`, and no nonmacroscopic component contributes to it. Hence all of `C_long` lies in the at most `K_0` macroscopic component responses. Therefore one macroscopic component satisfies

\[
C_r
\ge
\frac{C_{long}}{K_0}
>
\frac1{2K_0},
\]

which proves C44.6.

Because this component is macroscopic,

\[
\operatorname{diam}A_r>\rho_0D.
\]

C44.9 then gives

\[
\delta_r+2>\rho_0D,
\]

so

\[
\boxed{\delta_r>\rho_0D-2.}
\tag{C44.24}
\]

C44.12 gives the attachment-count bound in C44.7. Finally C40 proves

\[
t_r\ge\delta_r+3,
\]

hence C44.24 yields

\[
\boxed{t_r>\rho_0D+1.}
\tag{C44.25}
\]

This is Branch B. `square`

---

## 5. Near-minimal boundary sharpening

In the C33 near-minimal phase `sigma_B=o(D)`, C37 improves C36's crude incidence count to

\[
\sum_r|A_r|
\le
q_{used}+2c_I-2s
\le
|B_+|+o(D).
\tag{C44.26}
\]

Since `|B_+|<=pi D`, the number of macroscopic components is then asymptotically at most

\[
\frac{3\pi}{\rho_0}+o(1),
\tag{C44.27}
\]

rather than `9pi/rho_0`. Thus Branch B in the actual near-minimal response frontier can be taken to involve one of only an absolute bounded number of macroscopic cells, with a better constant.

The exact constant is not important; the structural conclusion is.

---

## 6. Exact effect on the C-II response frontier

C44 changes the response-side target from a diffuse network problem to the following explicit binary obstruction:

```text
C-II response:
    either
        short response mass >= 1/2
        -> tr(Lambda-L_H) >= gamma_0 > 0
    or
        one harmonic component I_r has
            response conductance >= 1/(2K_0)
            attachment diameter > rho_0 D
            graph diameter > rho_0 D-2
            |A_r| > (rho_0 D+1)/3
            boundary contact count > rho_0 D+1
```

Branch A supplies the absolute trace gap that C41 alone could not prove.

Branch B supplies a single macroscopic object with both **geometric scale** and **nonvanishing response weight**. This is substantially stronger than merely knowing that some attachment set is large.

The next response-side lemma can therefore be split cleanly:

1. exclude an absolute trace gap using the affine-kernel/circular-planar/diameter-load structure; or
2. exclude one macroscopic harmonic component with the C44.6-C44.7 parameters using its convex attachment hull, C42 rhombic bulk, or a container/area inequality.

Either route would remove one half of the C44 dichotomy.

---

## 7. Regression audit

- **Tiny individual response edges:** allowed. Branch B aggregates long response mass over only constantly many components, so no individual-edge lower bound is used.
- **Many small harmonic components:** they can exist, but all of their response conductance is uniformly short and therefore feeds Branch A.
- **One huge component:** allowed precisely as Branch B; it is now quantified by attachment count, graph diameter, boundary contacts, and total response conductance.
- **Direct loaded-loaded contacts:** always short for large `D`; they help Branch A and cannot hide Branch B mass.
- **Near-minimal phase:** only improves the constant number of macroscopic components; the main dichotomy does not require `sigma_B=o(D)`.
- **C-I:** outside scope because C35-C41 are C-II inputs.

```text
C44:
For every harmonic component, any two attachments are joined by a contact path of
length <=delta_r+2, so
    diam A_r <= delta_r+2 <= 3|A_r|-1.
With rho_0=1-eta_0 from C43, a component carrying any response pair longer than
rho_0 D must therefore have |A_r|>(rho_0 D+1)/3. Since sum|A_r|<=3|B_+|<=3pi D,
only K_0=ceil(9pi/rho_0) such components exist.

C41 gives total response conductance >1. If short response mass is >=1/2, C41+C43 give
    tr(Lambda-L_H)>=gamma_0.
Otherwise long response mass >1/2, all carried by <=K_0 macroscopic components, so one
has total response conductance >1/(2K_0), attachment diameter >rho_0D, graph diameter
>rho_0D-2, |A_r|>(rho_0D+1)/3, and t_r>rho_0D+1.
```
