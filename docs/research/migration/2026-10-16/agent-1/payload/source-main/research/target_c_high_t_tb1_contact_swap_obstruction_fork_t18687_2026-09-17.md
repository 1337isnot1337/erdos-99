# Target C-II — exact contact swap splits the strong-TB1 branch into wide bilateral pairs or inverse-`D` inactive slack

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the positive-density strong-TB1 side of the selected high-`t` O--O shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** adjacent-strip opening reduction; one-bar tangent certificate; TB1 inverse-`D` cone collapse; coupled host transverse margin; one-sided switching/host order; C67 diameter-direction separation; canonical contact-minimal then diameter-pair-minimal normalization  
**Certificate:** `research/verify_target_c_high_t_tb1_contact_swap_obstruction_fork_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The strong-TB1 branch has so far been treated infinitesimally: one switching diameter blocks the tiny local opening cone with an order-`D` derivative. The inverse-`D` cone-collapse theorem gives a finite displacement that is better adapted to this regime.

At a non-antipodal TB1 interface let `a,b` be the rooted unit boundary-contact vectors of the moving layer. Put

\[
q:=|a+b|>0,
\qquad
w:={a+b\over q},
\qquad
v_{\rm sw}:=-(a+b)=-qw.
\]

Then the two boundary contacts are not opened. They are **swapped exactly**:

\[
a+v_{\rm sw}=-b,
\qquad
b+v_{\rm sw}=-a.
\]

Hence both remain unit contacts. Because the strong-TB1 cone has width `O(D^-1)`, this exact swap has size

\[
q< {31.4\times10^6\over D}+o(D^{-1}).
\]

For a moving diameter edge with orientation-independent inward vector `n_h`, the exact change is

\[
|r_h(v_{\rm sw})|^2-D^2
=-2q(n_h\cdot w)+q^2.
\]

The selected TB1 blocker has positive projection at least `(c_H-o(1))D`, with

\[
c_H=0.453819885927\ldots .
\]

The host theorem gives the same absolute transverse floor to every switching diameter. Since `w` differs from the local transverse axis by `O(D^-1)`, every switching bar satisfies

\[
|n_h\cdot w|\ge(c_H-o(1))D.
\]

Therefore the local switching set has only two possible finite-swap behaviors:

1. some switching diameter has the **opposite** transverse sign from the selected TB1 blocker; or
2. every moving actual diameter strictly shortens under the exact contact swap.

In the second case, canonical minimality forces a previously strict source pair to become active or invalid during the swap. Since the displacement is `O(D^-1)`, that pair was already within `O(D^-1)` of either distance `1` or distance `D`.

Globally, one strict pair can be affected by at most two disjoint path-layer swaps. Thus a linear same-sign TB1 population forces a linear number of **distinct** inactive near-active pairs.

The opposite-sign branch also sharpens. Opposite-sign switching bars cannot share an endpoint for large `D`, and host order gives the same double-C67 narrow-pair capacity as in the exact-force setting. Consequently a linear opposite-sign TB1 population contains a linear fixed-angle family of genuine crossing diameter pairs.

For the current strong-TB1 density floor

\[
s_0={791\over320{,}000{,}000}=2.471875\times10^{-6},
\]

one obtains the explicit alternative

\[
\boxed{
\begin{array}{ll}
\text{WIDE-PAIR:}&
>(6.1796875\times10^{-7})D-o(D)
\text{ strong-TB1 interfaces carry}\cr
&\text{two vertex-disjoint crossing switching diameters with projective gap}\cr
&\eta\ge1.2359375\times10^{-6};\cr
\text{or}&\cr
\text{NEAR-ACTIVE:}&
>(6.1796875\times10^{-7})D-o(D)
\text{ distinct previously strict source pairs satisfy}\cr
&1<|xy|\le1+{31.4\times10^6\over D}+o(D^{-1})\cr
&\text{or}\cr
&D-{31.4\times10^6\over D}-o(D^{-1})\le|xy|<D.
\end{array}
}
\]

Thus the positive-density strong-TB1 branch is no longer only an infinitesimal blocker family. It either enters the same fixed-angle crossing-diameter geometry as the wide exact-antipodal branch, or it forces a new linear inactive-slack population at the precise `D^-1` scale of the residual contact cone.

---

## 1. The exact contact swap

Let `R_i` be the physical source layer between consecutive selected O--O cuts at a non-antipodal TB1 interface. Orient the two unit boundary-contact vectors from the fixed side into `R_i`:

\[
|a_i|=|b_i|=1,
\qquad
\theta_i:=\angle(a_i,b_i)\in(0,\pi).
\]

The adjacent-strip reduction translates every point of `R_i` by a common vector `v`. The boundary-contact vectors become

\[
a_i+v,
\qquad
b_i+v.
\]

Define

\[
\epsilon_i:=\pi-\theta_i>0,
\]

and

\[
q_i:=|a_i+b_i|,
\qquad
w_i:={a_i+b_i\over q_i},
\qquad
v_i:=-(a_i+b_i)=-q_iw_i.
\tag{CS.1}
\]

Because `theta_i<pi`, `q_i>0`. Directly,

\[
\boxed{
a_i+v_i=-b_i,
\qquad
b_i+v_i=-a_i.}
\tag{CS.2}
\]

Hence

\[
\boxed{|a_i+v_i|=|b_i+v_i|=1.}
\tag{CS.3}
\]

The boundary contacts survive exactly. Their vectors are exchanged with reversal.

Also

\[
q_i^2
=|a_i+b_i|^2
=2+2\cos\theta_i
=4\sin^2{\epsilon_i\over2},
\]

so

\[
\boxed{q_i=2\sin{\epsilon_i\over2}\le\epsilon_i.}
\tag{CS.4}
\]

The cone-collapse theorem gives

\[
\epsilon_i
<{31.4\times10^6\over D}+o(D^{-1}),
\]

therefore

\[
\boxed{
0<q_i
<{31.4\times10^6\over D}+o(D^{-1}).
}
\tag{CS.5}
\]

Finally `w_i` is exactly the midpoint direction of the local contact-opening cone. Indeed

\[
\boxed{
a_i\cdot w_i=b_i\cdot w_i={q_i\over2}>0.}
\tag{CS.6}
\]

Thus `w_i` is a unit opening tangent, even though the finite displacement `v_i=-q_iw_i` goes in the opposite direction and lands at the second unit-contact intersection.

---

## 2. Every switching diameter has a definite sign against the swap axis

For every switching actual diameter `h` at interface `i`, let

\[
n_h
\]

be the orientation-independent inward vector from the endpoint outside `R_i` to the endpoint inside `R_i`. Then `|n_h|=D`.

The coupled host theorem gives every switching diameter the projective transverse margin

\[
|n_h\cdot Ju_i|
\ge(c_H-o(1))D,
\qquad
c_H=0.453819885927\ldots,
\tag{CS.7}
\]

where `u_i` is the local row phase. The cone-collapse theorem puts the entire local opening cone, and hence its midpoint `w_i`, within `O(D^-1)` of the corresponding transverse direction. Therefore

\[
|n_h\cdot(w_i-Ju_i)|=O(1),
\]

and (CS.7) yields

\[
\boxed{
|n_h\cdot w_i|
\ge(c_H-o(1))D.
}
\tag{CS.8}

In particular no switching bar has asymptotically small projection on the swap axis.

Let `h_i^+` be the chosen strong-TB1 certificate bar. The strong-TB1 inequality applies to every unit opening tangent, so by (CS.6)

\[
\boxed{
n_{h_i^+}\cdot w_i
\ge(c_H-o(1))D.}
\tag{CS.9}

Call interface `i` **two-sign** if some other switching diameter satisfies

\[
n_h\cdot w_i<0.
\tag{CS.10}
\]

Otherwise call it **one-sign**. By (CS.8), on a one-sign interface every switching diameter satisfies

\[
\boxed{
n_h\cdot w_i\ge(c_H-o(1))D.}
\tag{CS.11}
\]

---

## 3. On a one-sign interface the exact swap strictly shortens every moving old diameter

For an oriented source pair `h=xy`, the adjacent-strip formula writes

\[
r_h(v)=r_h+\delta_hv,
\qquad
\delta_h\in\{-1,0,1\}.
\]

For a moving actual diameter, `delta_h!=0`, and by definition

\[
n_h=\delta_hr_h.
\]

Thus at `v_i=-q_iw_i`,

\[
\begin{aligned}
|r_h(v_i)|^2-D^2
&=2n_h\cdot v_i+|v_i|^2\\
&=-2q_i(n_h\cdot w_i)+q_i^2.
\end{aligned}
\tag{CS.12}
\]

On a one-sign interface, (CS.11) gives

\[
|r_h(v_i)|^2-D^2
\le
-2q_i(c_H-o(1))D+q_i^2.
\tag{CS.13}
\]

Because `q_i>0` and `q_i=O(D^-1)`, the right side is strictly negative for all sufficiently large sources. Hence

\[
\boxed{
|r_h(v_i)|<D
\quad\text{for every moving old actual diameter }h.
}
\tag{CS.14}

Every nonswitching old diameter is unchanged exactly by the layer translation.

This is a finite statement. It does not use a first-order limiting argument or a source-dependent infinitesimal step.

---

## 4. Canonical minimality forces an inactive near-active witness

Suppose `i` is one-sign. Assume, for contradiction, that after the exact swap `v_i`

1. every previously strict noncontact pair still has distance `>1`, and
2. every previously strict nondiameter pair still has distance `<D`.

All old contacts away from the two boundary trains are unchanged exactly; by (CS.3) the two boundary contact families also remain unit. Hence the number of unit contacts is unchanged.

By (CS.14), every moving old diameter is now strict. Every nonswitching old diameter is unchanged exactly. Therefore either:

- no nonswitching old diameter exists, in which case the new source has diameter `<D`, contradicting global minimality; or
- at least one nonswitching old diameter remains, in which case the new source is another diameter-`D` global minimizer with the same number of unit contacts but strictly fewer diameter pairs, contradicting the canonical contact-minimal then diameter-pair-minimal normalization.

Thus at least one previously strict pair `xy` must satisfy at the final swap

\[
|x(v_i)-y(v_i)|\le1
\quad\text{or}\quad
|x(v_i)-y(v_i)|\ge D.
\tag{CS.15}
\]

Such a pair necessarily straddles the translated layer; otherwise it would be unchanged. Let

\[
\ell=|x-y|.
\]

Since the displacement of the moving endpoint has norm `q_i`, the triangle inequality gives:

- if the first alternative in (CS.15) holds, then
  \[
  1<\ell\le1+q_i;
  \]
- if the second holds, then
  \[
  D-q_i\le\ell<D.
  \]

Using (CS.5), every one-sign strong-TB1 interface therefore has a previously strict witness satisfying

\[
\boxed{
1<|xy|
\le1+{31.4\times10^6\over D}+o(D^{-1})
}
\tag{CS.16}
\]

or

\[
\boxed{
D-{31.4\times10^6\over D}-o(D^{-1})
\le|xy|<D.
}
\tag{CS.17}
\]

The theorem does not claim that these near-active pairs are themselves contacts or diameters. They are exactly the finite-slack obstruction left after every old moving diameter has been shortened.

---

## 5. A strict pair can witness at most two layer swaps

The physical path layers `R_i` are pairwise disjoint. A source pair `xy` changes under the translation of `R_i` exactly when one endpoint lies in `R_i` and the other does not.

Each endpoint belongs to at most one path layer. Therefore the set of indices whose translations move the pair has cardinality at most two:

\[
\boxed{
\#\{i:\mathbf1_{R_i}(x)\ne\mathbf1_{R_i}(y)\}\le2.
}
\tag{CS.18}
\]

Consequently, if `M_D` is any family of one-sign strong-TB1 interfaces, choosing one witness from (CS.16)--(CS.17) at each interface yields at least

\[
\boxed{{|M_D|\over2}}
\tag{CS.19}

**distinct** previously strict near-active pairs.

This multiplicity-two fact is exact and independent of the slack size.

---

## 6. Two-sign TB1 interfaces give genuine two-host diameter pairs

Now let `i` be two-sign. Choose the positive strong-TB1 blocker `h_i^+` from (CS.9) and one negative switching bar `h_i^-` satisfying (CS.10).

The host transverse margin and connected host-normal order put the two signs on the two physical O--O host branches. Thus the two birth endpoints occupy opposite hosts. Their consistently inward diameter directions lie in the common one-sided switching semicircle, one below and one above the row line, each at projective distance at least

\[
\gamma_H-o(1),
\qquad
\gamma_H:=\arcsin c_H.
\tag{CS.20}
\]

The pair is also vertex-disjoint for all sufficiently large `D`. If the two diameter bars shared one endpoint, the source-wide diameter-degree geometry would bound their ordinary angle by

\[
\Theta_D
=2\arccos\left({D\over D+2\cdot3^{1/4}\sqrt D}\right)
=O(D^{-1/4}).
\tag{CS.21}
\]

But their transverse signs are opposite. Two directions less than `pi/2` apart on which the row-normal sine has opposite signs must straddle a row-direction zero, putting each within `Theta_D` of the row projective line. This contradicts (CS.20) once `Theta_D<gamma_H/2`, say.

Hence

\[
\boxed{h_i^+,h_i^-\text{ are vertex-disjoint and therefore cross properly}.}
\tag{CS.22}

No exact-antipodal reaction or positive KKT multiplier is used in this conclusion.

---

## 7. Generic two-host order gives the same double-C67 narrow capacity

Take any ordered family of two-sign TB1 interfaces on one fixed side of the common hub. At each interface use the pair `h_i^+,h_i^-` from Section 6.

Orient each diameter outward at its birth endpoint. By convex support-normal monotonicity, the diameter directions on one host move monotonically in one angular direction as the interface index increases, while the directions on the opposite host move monotonically in the other direction. Distinct selected interfaces have disjoint switching supports, so all chosen bars in each lane are distinct. C67 gives the projective separation

\[
\delta_D:=2\arcsin{1\over2D}
\tag{CS.23}
\]

between consecutive selected directions in either lane.

Choose a real angular lift of the common one-sided switching semicircle. Write the lower-host lane angle `a_j` and upper-host lane angle `b_j`. After reversing the interface order if necessary,

\[
a_{j+1}-a_j\ge\delta_D,
\qquad
b_j-b_{j+1}\ge\delta_D.
\tag{CS.24}
\]

Thus their ordinary opening

\[
\Delta_j:=b_j-a_j
\]

satisfies

\[
\boxed{
\Delta_j-\Delta_{j+1}\ge2\delta_D.
}
\tag{CS.25}
\]

By the two-host transverse margin,

\[
\Delta_j\ge2\gamma_H-o(1).
\tag{CS.26}
\]

Fix a constant

\[
0<\rho<\gamma_H.
\]

If the projective pair gap

\[
\eta_j:=\min\{\Delta_j,\pi-\Delta_j\}
\]

is below `rho`, the ordinary-small alternative is impossible by (CS.26). Hence every `rho`-narrow pair is near-antiparallel:

\[
\eta_j=\pi-\Delta_j.
\]

Equation (CS.25) shows that the narrow pairs form an initial segment and that their projective gaps increase by at least `2delta_D` per retained interface. Therefore

\[
\boxed{
N_D^{\rm narrow}(\rho)
\le {\rho\over2\delta_D}+1
\le {\rho D\over2}+1.
}
\tag{CS.27}
\]

This is the same double-C67 capacity as for the exact-force lanes, but the proof here uses only two-host switching geometry. It therefore applies to the two-sign TB1 branch.

After deleting the narrow initial segment, every surviving pair is vertex-disjoint by (CS.22) and has projective gap at least `rho`. The fixed-angle central-diamond theorem then applies mechanically to the two actual diameter chords.

---

## 8. Explicit consequence at the current strong-TB1 density floor

The current corrected high-`t` fork says that if the strong-TB1 mechanism wins, then

\[
|S_D|>
\left(s_0-o(1)\right)D,
\qquad
s_0:={791\over320{,}000{,}000}
=2.471875\times10^{-6}.
\tag{CS.28}
\]

Partition `S_D` into two-sign and one-sign interfaces.

### Case A: at least half are two-sign

Then the two-sign population has density at least

\[
\sigma:={s_0\over2}
={791\over640{,}000{,}000}
=1.2359375\times10^{-6}.
\tag{CS.29}
\]

Take

\[
\rho=\sigma.
\]

This is far below `gamma_H`. By (CS.27), the `rho`-narrow deletion costs at most `(sigma/2)D+o(D)`. Hence more than

\[
\boxed{
{s_0\over4}D-o(D)
=(6.1796875\times10^{-7})D-o(D)
}
\tag{CS.30}

interfaces retain a vertex-disjoint properly crossing diameter pair with

\[
\boxed{
\eta\ge {s_0\over2}
=1.2359375\times10^{-6}.
}
\tag{CS.31}

Each such pair has the fixed-angle central-diamond and central-crossing consequences already proved for any two vertex-disjoint actual diameter chords.

### Case B: at least half are one-sign

Then

\[
|M_D|>{s_0\over2}D-o(D).
\]

By (CS.19), the source contains more than

\[
\boxed{
{s_0\over4}D-o(D)
=(6.1796875\times10^{-7})D-o(D)
}
\tag{CS.32}

**distinct** previously strict source pairs satisfying (CS.16) or (CS.17).

Thus both sides of the final TB1 fork retain the same explicit linear coefficient `s_0/4`.

---

## 9. What this changes and what remains open

The positive-density strong-TB1 branch now has the finite source-level normal form

```text
EITHER
    linear density of genuine crossing two-host diameter pairs
    with a fixed projective angle floor,
    hence fixed-fraction central diamonds and central crossings;

OR
    linear density of distinct inactive source pairs
    within O(1/D) of the lower or upper distance constraint.
```

This removes the possibility that the TB1 branch survives solely because one robust blocker defeats an infinitesimal opening direction while no finite structure accumulates.

It does **not** close C-II.

- The WIDE-PAIR side still lacks the exact axial KKT force balance of the exact-antipodal branch. It now has the same crossing-diameter geometry, but not the same force coefficients.
- The NEAR-ACTIVE side is not contradictory by counting alone. Near-unit and near-diameter inactive pairs can exist in large numbers. A closing argument must use their layer incidence/order or obtain a collective source-preserving motion.
- The exact swap may cross an inactive constraint before its endpoint. Sections 4--5 record that event as the near-active witness rather than assuming a uniform inactive slack.

The next sharp target on the TB1 side is therefore to classify the linear near-active witnesses by their path-layer support. If they can be shown to have bounded crossing multiplicity against the common dense train rectangle, Case B dies; otherwise their ordered incidence should supply a new rigidity row comparable to the active diameter rail.

**Disposition:** converted the inverse-`D` strong-TB1 cone into an exact finite contact-swap fork. A positive-density TB1 survivor now forces either a linear fixed-angle family of genuine crossing bilateral diameter pairs or a linear family of distinct inactive pairs at `O(D^-1)` distance from the unit/diameter constraints. C-II and Level I remain open.
