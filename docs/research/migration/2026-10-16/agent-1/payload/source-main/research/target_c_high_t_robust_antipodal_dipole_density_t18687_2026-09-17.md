# Target C-II — the exact-antipodal branch has linear fixed-angle crossing dipoles

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the linear one-sided high-`t` obstruction shore for `t=(q-k)/D<=1.8687`  
**Dependencies:** linear exact-antipodal / strong-TB1 density fork; common one-sided switch half-plane; exact-antipodal opposite-transverse blocker pair; shrinking common row-phase window; canonical C67 projective diameter-direction separation; source-wide diameter degree bound  
**Certificate:** `research/verify_target_c_high_t_robust_antipodal_dipole_density_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current linear obstruction fork gives

\[
|E_D|+|S_D|>{7c_0\over8}D-o(D),
\qquad
c_0={113\over20{,}000{,}000},
\tag{RA.1}
\]

where `E_D` is the exact-antipodal good-interface set and `S_D` is the strong non-antipodal one-bar set.  The strong-TB1 bars already have a fixed angular margin

\[
\gamma:={c_0\over32}
={113\over640{,}000{,}000}
=1.765625\times10^{-7}.
\tag{RA.2}
\]

The exact-antipodal side previously only supplied two switching diameter bars of opposite transverse sign.  Their projective angle could, a priori, tend to zero.  This note rules out linear density of that near-parallel regression.

For every `i in E_D`, choose the two consistently inward blocker directions

\[
d_i^+,d_i^-\in S^1
\]

with opposite transverse signs relative to the row direction `u_i`, and define

\[
\eta_i:=d_{\mathbb{RP}^1}([d_i^+],[d_i^-])\in(0,\pi/2].
\tag{RA.3}
\]

Put

\[
E_D^{\rm wide}:=\{i\in E_D:\eta_i\ge\gamma\}.
\tag{RA.4}
\]

Then

\[
\boxed{
|E_D\setminus E_D^{\rm wide}|
\le 2\gamma D+o(D)
={c_0\over16}D+o(D).
}
\tag{RA.5}
\]

Consequently

\[
\boxed{
|E_D^{\rm wide}|+|S_D|
>{13c_0\over16}D-o(D)
=0.000004590625D-o(D).
}
\tag{RA.6}
\]

In particular one of the two robust mechanisms has density

\[
\boxed{
\max\{|E_D^{\rm wide}|,|S_D|\}
>{13c_0\over32}D-o(D)
=0.0000022953125D-o(D).
}
\tag{RA.7}
\]

Every interface in `E_D^{wide}` carries two actual diameter chords crossing at projective angle at least `gamma`.  For sufficiently large `D` the two chords cannot share an endpoint, so they are a genuine fixed-angle crossing dipole.

Thus the final linear fork is no longer

```text
exact antipodality with an arbitrarily degenerate opposite-sign pair
or
strong one-bar blocking.
```

It is

```text
linear density of fixed-angle crossing antipodal dipoles
or
linear density of fixed-interior-margin one-bar blockers.
```

Both sides now have the same absolute angular scale `gamma`.

---

## 1. One common open half-plane contains every oriented switching bar

Take the linear good shore strictly on one side of the common diameter-routing hub and orient the interface order toward the hub.  The global switch-caterpillar theorem supplies one linear functional `phi` such that every consistently inward switching diameter vector `n_h` satisfies

\[
\boxed{\phi(n_h)>0.}
\tag{RA.8}
\]

Represent `phi` by a nonzero vector `z`, so `phi(v)=z\cdot v`.  After normalization, every oriented unit switching direction

\[
d_h:={n_h\over D}
\]

lies in the same open semicircle

\[
\mathcal H_D:=\{d\in S^1:z\cdot d>0\}.
\tag{RA.9}
\]

Let the two endpoints of this angular semicircle be `L_D,U_D`, separated by `pi`.  Projectively they are the same line; write

\[
\kappa_D:=[L_D]=[U_D]=\ker\phi\in\mathbb{RP}^1.
\tag{RA.10}
\]

This common half-plane is the ingredient that prevents a near-projectively-parallel antipodal pair from rotating freely around the projective circle.

---

## 2. The exact-antipodal axial reaction places the row orientation in the same half-plane

Fix `i in E_D`.  Exact antipodality gives

\[
G_i=g_i u_i,
\qquad g_i\ne0,
\tag{RA.11}
\]

while the switching KKT identity and positivity give

\[
G_i=\sum_{h\in H_{sw,i}}\beta_h n_h,
\qquad \beta_h>0.
\tag{RA.12}
\]

Equation (RA.8) implies

\[
\phi(G_i)>0.
\tag{RA.13}
\]

Define

\[
w_i:=\operatorname{sgn}(g_i)u_i.
\tag{RA.14}
\]

Then `w_i` is a unit vector in `mathcal H_D`.  Replacing `u_i` by `-u_i` only swaps the labels `+` and `-` in the opposite-transverse blocker statement, so the chosen blocker directions still have opposite transverse signs relative to `w_i`.

Choose angular representatives inside the single open interval `mathcal H_D`:

\[
L_D<\theta_i^-<\omega_i<\theta_i^+<U_D,
\tag{RA.15}
\]

where `omega_i` is the angle of `w_i` and `theta_i^\pm` are the blocker angles after relabeling.  This ordering is legitimate because all three vectors lie in one open semicircle and the blocker transverse signs are opposite.

Put

\[
s_i:=\theta_i^+-\theta_i^-\in(0,\pi).
\tag{RA.16}
\]

The projective blocker gap is exactly

\[
\boxed{
\eta_i=\min\{s_i,\pi-s_i\}.
}
\tag{RA.17}
\]

---

## 3. A projectively narrow blocker pair has only two possible locations

Assume

\[
\eta_i<\gamma.
\tag{RA.18}
\]

There are two cases.

### Case A: `s_i<gamma`

Because `theta_i^-<omega_i<theta_i^+`,

\[
0<\omega_i-\theta_i^-<\gamma,
\qquad
0<\theta_i^+-\omega_i<\gamma.
\tag{RA.19}
\]

Hence both blocker projective directions lie within `gamma` of the row line `[u_i]=[w_i]`.

### Case B: `pi-s_i<gamma`

Using `U_D-L_D=pi`,

\[
(\theta_i^--L_D)+(U_D-\theta_i^+)
=\pi-s_i
<\gamma.
\tag{RA.20}
\]

Both summands are nonnegative, so

\[
\theta_i^--L_D<\gamma,
\qquad
U_D-\theta_i^+<\gamma.
\tag{RA.21}
\]

Since `L_D` and `U_D` represent the same projective line `kappa_D`, both blocker projective directions lie within `gamma` of `kappa_D`.

Therefore every narrow exact-antipodal pair satisfies the exact dichotomy

\[
\boxed{
\eta_i<\gamma
\Longrightarrow
\begin{cases}
[d_i^+],[d_i^-]\subset N_\gamma([u_i]),&\text{or}\\
[d_i^+],[d_i^-]\subset N_\gamma(\kappa_D).
\end{cases}
}
\tag{RA.22}
\]

The second alternative is the oriented-near-opposite regression that ordinary projective packing alone misses.  The common half-plane collapses all such regressions to the single boundary line `kappa_D`.

---

## 4. Two shrinking/common projective arcs have only `2 gamma D + o(D)` pair capacity

All high-`t` rectangle rows lie in one shrinking projective phase interval `W_D` of width

\[
\omega_D=o(1).
\tag{RA.23}
\]

Thus the Case-A directions from every narrow exact-antipodal interface lie in the `gamma`-neighborhood of `W_D`, an arc of length at most

\[
\omega_D+2\gamma.
\tag{RA.24}
\]

All Case-B directions lie in the projective `gamma`-ball around `kappa_D`, an arc of length `2gamma`.  The union of the two arcs therefore has total length at most

\[
\boxed{
\ell_D\le\omega_D+4\gamma.
}
\tag{RA.25}
\]

Different interfaces have disjoint switching supports, and the two blockers at one interface are distinct.  Hence `N_D` narrow interfaces contribute `2N_D` distinct actual diameter edges.

Canonical C67 separates distinct actual diameter directions by

\[
\delta_D=2\arcsin{1\over2D}\ge{1\over D}.
\tag{RA.26}
\]

A union of at most two projective arcs with total length `ell_D` contains at most

\[
2+{\ell_D\over\delta_D}
\]

`delta_D`-separated directions.  Therefore

\[
2N_D
\le2+{\omega_D+4\gamma\over\delta_D}
\le2+D\omega_D+4\gamma D.
\tag{RA.27}
\]

Divide by two:

\[
\boxed{
N_D\le2\gamma D+o(D).
}
\tag{RA.28}
\]

This is (RA.5).

The point is that a small projective gap has only two global hiding places: the shrinking row phase or the one common boundary direction of the switch half-plane.  Both have subcritical projective capacity.

---

## 5. The robust linear fork

The strong-TB1 theorem gives (RA.1) and uses exactly the same constant `gamma=c_0/32` as its fixed interior margin.  Subtract (RA.28):

\[
\begin{aligned}
|E_D^{\rm wide}|+|S_D|
&=|E_D|+|S_D|-N_D\\
&>{7c_0\over8}D-2\gamma D-o(D)\\
&={13c_0\over16}D-o(D).
\end{aligned}
\tag{RA.29}
\]

This proves (RA.6).  Taking the larger side gives (RA.7).

The constants are exact:

\[
{13c_0\over16}
={1469\over320{,}000{,}000}
=0.000004590625,
\tag{RA.30}
\]

and

\[
{13c_0\over32}
={1469\over640{,}000{,}000}
=0.0000022953125.
\tag{RA.31}
\]

So the high-`t` linear obstruction is forced into one of two fixed-angle regimes, both at positive linear density.

---

## 6. Wide antipodal pairs are genuine fixed-angle crossing dipoles

For `i in E_D^{wide}`,

\[
\eta_i\ge\gamma.
\tag{RA.32}
\]

The source-wide circumradius estimate used in the antipodal shared-endpoint theorem shows that if two actual diameter edges share one endpoint, their projective direction gap is at most

\[
\Theta_D
=2\arccos\left({D\over D+2\,3^{1/4}\sqrt D}\right)
=(4\,3^{1/8}+o(1))D^{-1/4}.
\tag{RA.33}
\]

Since `Theta_D->0` and `gamma>0` is fixed, for all sufficiently large `D`,

\[
\Theta_D<\gamma.
\tag{RA.34}
\]

Thus the two blockers of every wide antipodal interface have four distinct endpoints.  Two vertex-disjoint actual diameter edges cross in the convex diameter thrackle.  Their line-crossing angle is their projective direction gap, hence at least `gamma`.

Therefore

\[
\boxed{
 i\in E_D^{\rm wide}
 \Longrightarrow
 \text{a genuine two-chord crossing dipole of angle at least }\gamma.
}
\tag{RA.35}
\]

This is stronger than merely excluding shared-endpoint stars: the surviving linear antipodal obstruction cannot collapse into an asymptotically parallel crossing pair either.

---

## 7. If the wide-antipodal side wins, an unbounded globally disjoint fixed-angle braid survives

The source-wide degree estimate is

\[
\Delta(H)
\le(4\,3^{1/8}+o(1))D^{3/4}.
\tag{RA.36}
\]

Suppose the wide-antipodal side of (RA.7) occurs.  Treat each wide antipodal pair as a four-endpoint bundle.  Two bundles conflict when their endpoint sets meet.  A fixed bundle has four endpoints, each incident with at most `Delta(H)` diameter edges, so the bundle-conflict degree is at most `4Delta(H)`.

Greedy independent-set extraction therefore leaves at least

\[
\left(
{13c_0/32\over16\,3^{1/8}}-o(1)
\right)D^{1/4}
\tag{RA.37}
\]

bundles with pairwise disjoint endpoint sets.

All `2M_D` selected diameter edges are then vertex-disjoint; hence every pair of selected edges crosses.  Inside each original interface bundle the crossing angle remains at least `gamma`.  The interface tags, one-sided birth positions, and common train-cut order are all retained.

So the wide-EA alternative contains an unbounded paired braid

```text
M_D = Omega(D^(1/4)) interface bundles
2M_D globally vertex-disjoint actual diameter chords
all 2M_D chords pairwise crossing
within every tagged pair: crossing angle >= gamma
all pairs retain distinct ordered one-sided switch tags.
```

The fixed-angle condition is new; the previous matching extraction allowed each tagged pair to become projectively arbitrarily narrow.

---

## 8. Frontier effect

The previous final fork still allowed the exact-antipodal side to concentrate in tiny crossing angles, a potentially serious regular-shell regression.  The common switch half-plane plus C67 removes that escape at linear density.

The surviving high-`t` linear obstruction now has the robust form

```text
(A) fixed-angle antipodal dipoles:
    > 2.2953125e-6 D - o(D) interfaces in the winning subcase;
    each tagged pair consists of two crossing actual diameter chords;
    projective crossing angle >= 1.765625e-7;
    an Omega(D^(1/4)) globally endpoint-disjoint paired braid survives;

or

(B) strong one-bar blockers:
    > 2.2953125e-6 D - o(D) interfaces in the winning subcase;
    each chosen blocker is at least 1.765625e-7 radians inside both rays
    of its local dual cone;
    every local opening direction has first derivative >= D sin(gamma).
```

This does not close C-II.  It does remove asymptotically tangent/projectively narrow exact-antipodal dipoles from the positive-density frontier.  A closing argument can now assume a fixed absolute angular margin on whichever side of the final linear fork survives.

The next high-value target is to combine that fixed angular margin with the ordered common train-cut caterpillar and the near-triangular transverse rectangle.  On the antipodal side, the tagged pair order must now accommodate macroscopic angular separation at linearly many birth interfaces; on the TB1 side, one has the same fixed angular scale against the local opening cone.

No canonical promotion or C-II closure is claimed.

**Disposition:** proved that only `2 gamma D+o(D)` exact-antipodal interfaces can use projectively narrow blocker pairs, upgraded the final linear obstruction fork to fixed-angle positive-density alternatives, and obtained an `Omega(D^(1/4))` globally vertex-disjoint fixed-angle paired braid in the wide-antipodal winning branch. C-II and Level I remain open.
