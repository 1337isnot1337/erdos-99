> Generated reading edition · [exact source](../../../../docs/targets/target-c/101-complement-gap-chord-threshold-audit.md) · source SHA-256 `4d6303fc2e1dbae15889af2a77312938fdbf939ddf4df6adc30115081b9aa0f6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 4 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — complement-gap chord threshold audit

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** canonical after independent promotion audit and theorem-state audit.41 promotion.

Canonical Section 100 halves the Section-88 angular-support ceiling for a wrapping
circle limit:

```math
|S|\le 3\theta-2\pi,
\qquad
\alpha:=\lim {|A_D|\over D}\le {|S|\over2}.
```

That theorem leaves another first-order resource unused.  The complement of `S` is a
union of support-free angular gaps.  Each macroscopic gap forces the corresponding
outer-face unit-contact route to have at least the Euclidean chord length of the gap.
The exact Section-82 face ledger can charge all such gaps simultaneously.

Combining the Section-100 support ceiling with the resulting complement-chord floor
gives the necessary scalar inequality

```math
\boxed{
\sin(\theta/2)+2\sin\theta\le 3\theta-2\pi.
}
```

Its unique root is

```math
\boxed{
\theta_8=2.7029080296483676832\ldots,
\qquad
\mu_8:=\sin(\theta_8/2)=0.9760407652670519821\ldots .
}
```

Thus, using canonical Section 100, every wrapping Type-II harmonic-cell limit has
normalized diameter at least `mu_8`.  This
strictly improves Section 100's `0.9642670742...` candidate threshold.

No Cauchy perimeter inequality, Section-97/98 endpoint theorem, KKT coefficient floor,
or deletion of contact-isolated source points is used.

---

# 101. The full support complement forces additional outer-walk chord currency

## 101.1 Circle notation and the support-complement budget

Let `S` be a compact wrapping subset of the radius-`1/2` circle with pairwise minor
angular distance at most

```math
\theta<\pi.
\tag{101.1}
```

Put

```math
\phi:=2\pi-2\theta,
\qquad
U:=3\theta-2\pi.
\tag{101.2}
```

Write the open complement as the disjoint union of its connected angular gaps,

```math
\mathbb T\setminus S=\bigsqcup_{j\in J}G_j,
\qquad
|G_j|=g_j>0.
\tag{101.3}
```

Because `S` is compact and proper, every `G_j` has endpoints in `S`.  Wrapping forbids
a complementary gap of angular length at least `pi`: a gap longer than `pi` puts `S`
in an open semicircle, while a gap exactly `pi` would have antipodal endpoints in `S`,
contrary to `theta<pi`.  Therefore

```math
0<g_j<\pi.
\tag{101.4}
```

The two endpoints of `G_j` are points of `S`; since their minor angular separation is
`g_j`, (101.1) gives

```math
\boxed{g_j\le\theta.}
\tag{101.5}
```

Canonical Section 94 supplies three support-free central arcs, one in each of three
distinct anchor gaps, each of length

```math
\phi.
```

The three anchor points of `S` separate those arcs, so they lie in three distinct
components of `mathbb T\setminus S`.  Hence there are three distinct indices
`j_1,j_2,j_3` with

```math
\boxed{g_{j_i}\ge\phi\qquad(i=1,2,3).}
\tag{101.6}
```

Now use canonical Section 100.  Its sharp support-measure theorem gives

```math
|S|\le U.
\tag{101.7}
```

Therefore the total complementary angular measure obeys

```math
\boxed{
\sum_j g_j
=2\pi-|S|
\ge2\pi-U
=4\pi-3\theta.
}
\tag{101.8}
```

The right side has the useful exact decomposition

```math
4\pi-3\theta
=\theta+2\phi.
\tag{101.9}
```

Thus the complement has at least the angular mass of one `theta`-gap and two
`phi`-gaps.

## 101.2 Concavity minimizes the complement chord sum at `(theta,phi,phi)`

Let

```math
f(x):=\sin(x/2),
\qquad 0\le x\le\theta<\pi.
\tag{101.10}
```

Then `f` is increasing and concave and `f(0)=0`.

### Lemma 101.1 — complement chord minimum

Under (101.5), (101.6), and (101.8),

```math
\boxed{
\sum_j f(g_j)
\ge f(\theta)+2f(\phi)
=\sin(\theta/2)+2\sin\theta.
}
\tag{101.11}
```

### Proof

It is enough first to prove the assertion for a finite collection whose total mass is
exactly

```math
H:=\theta+2\phi.
```

Sort its entries decreasingly.  Because at least three entries are at least `phi`, the
largest entry is at most

```math
H-2\phi=\theta,
```

and the sum of the two largest is at most

```math
H-\phi=\theta+\phi.
```

Consequently the vector

```math
(\theta,\phi,\phi,0,0,\ldots)
```

majorizes every feasible vector of total mass `H`.  Concavity of `f` therefore gives

```math
\sum_jf(g_j)\ge f(\theta)+2f(\phi).
```

If the total mass is larger than `H`, decrease entries while preserving three entries
at least `phi` until the total becomes `H`; this can only decrease the sum because `f`
is increasing.  This proves the finite statement.

For the countable complement, fix `epsilon>0`.  Choose finitely many complementary
components, including the three components from (101.6), whose total angular measure
is at least `H-epsilon`.  The same majorization argument, now with total
`H-epsilon`, gives

```math
\sum_{j\in J_\epsilon} f(g_j)
\ge
f(\theta-\epsilon)+2f(\phi)
```

for `epsilon` small enough that `theta-epsilon>=phi`.  Let `epsilon` tend to zero.
This proves (101.11).  `square`

Since

```math
\phi/2=\pi-\theta,
```

we used

```math
f(\phi)=\sin(\phi/2)=\sin\theta.
\tag{101.12}
```

The extremal gap vector `(theta,phi,phi)` is not artificial.  The sharp Section-100
circle construction can degenerate two of its three support arcs to points and leave
one support arc of angular length `U`; its complement then has exactly these three gap
lengths.  Thus (101.11) is the correct sharp chord consequence of the one-dimensional
support theorem alone.

## 101.3 Every macroscopic complement gap costs an outer unit-contact route

Return to a wrapping Type-II harmonic-cell sequence

```math
P_D=\operatorname{conv}(A_D),
\qquad D\to\infty,
\tag{101.13}
```

such that, after scaling by `D` and passing to a subsequence,

```math
A_D/D\to S
```

in Hausdorff distance and

```math
{\operatorname{diam}(P_D)\over D}\to
\lambda=\sin(\theta/2)<1.
\tag{101.14}
```

Use the canonical local notation

- `a_D=|A_D|`;
- `L_D` for the outer-face walk length of the induced harmonic contact graph;
- `s_D>=0` for the local pinned-contact surplus;
- `c_D` for loaded-loaded contacts with both endpoints in `A_D`;
- `c_D^partial` for those which are polygon sides; and
- `Q_D>=0` for bounded-face degree excess.

Canonical Section 82 gives the exact identity

```math
\boxed{
L_D+Q_D=4a_D-6-2s_D-2c_D.
}
\tag{101.15}
```

Let `G_{j_1},...,G_{j_k}` be any fixed finite family of complementary components of
`S`.  Write the endpoints of `G_{j_i}` as `u_i,v_i`; both lie in the compact support
`S`. Hausdorff convergence supplies attachment angles converging to `u_i` and `v_i`,
while every fixed compact subarc strictly inside `G_{j_i}` contains no attachment for
all sufficiently large `D`.  Therefore the last attachment before `G_{j_i}` and the
first attachment after it converge to the two endpoints.  The corresponding cyclic
attachment gaps are distinct for large `D` and satisfy the stronger relation

```math
\boxed{h_{i,D}=g_{j_i}+o(1)<\pi.}
\tag{101.16}
```

The strict upper bound follows from `g_{j_i}<pi`.  This two-sided Hausdorff transfer is
important: a one-sided lower bound on `h_{i,D}` alone would not justify monotonicity of
the chord function across `pi`.

Type-II annular convergence puts every attachment radius at

```math
\left({1\over2}+o(1)\right)D.
```

Hence the Euclidean chord between the endpoints of the corresponding finite gap is at
least

```math
D\sin(g_{j_i}/2)-o(D).
\tag{101.17}
```

The Section-62 outer-face route between those consecutive attachments is a polygonal
chain of unit contact edges with the same endpoints.  Its edge count is at least the
Euclidean endpoint distance.  The `k` selected macroscopic routes are distinct pieces
of the outer-face walk.  They are not one-edge loaded-loaded contacts for large `D`.

Every other consecutive-attachment interval contributes one edge exactly when it is a
`c_D^partial` direct contact and at least two edges otherwise.  Consequently

```math
L_D
\ge
D\sum_{i=1}^k
\sin(g_{j_i}/2)
+2(a_D-k)-c_D^partial-o(D).
\tag{101.18}
```

Insert (101.18) in (101.15).  Since `c_D^partial<=c_D`, all local correction terms have
the favorable sign, and after division by `D` and passage to a subsequence with

```math
{a_D\over D}\to\alpha
\tag{101.19}
```

we obtain

```math
2\alpha
\ge
\sum_{i=1}^k
\sin(g_{j_i}/2).
\tag{101.20}
```

Because the finite family of complement components was arbitrary, monotone convergence
over larger finite subfamilies gives

```math
\boxed{
2\alpha
\ge
\sum_j\sin(g_j/2).
}
\tag{101.21}
```

A useful stronger form keeps the support measure `m:=|S|` rather than immediately
replacing it by its Section-100 ceiling.  Since `m<=U=3theta-2pi`, we have
`theta-m>=phi`.  For fixed `m`, the vector

```math
(\theta,\theta-m,\phi,0,0,\ldots)
```

majorizes every feasible complement-gap vector of total mass `2pi-m`: the largest gap
is at most `theta`, and the two largest leave at least one required `phi`-gap.  Concavity
of `sin(x/2)` therefore strengthens (101.21) to

```math
\boxed{
2\alpha\ge
\sin(\theta/2)+\sin((\theta-m)/2)+\sin\theta.
}
\tag{101.22a}
```

In particular, setting only `m<=U` aside for the moment recovers the report's uniform
floor

```math
\boxed{
2\alpha
\ge
\sin(\theta/2)+2\sin\theta.
}
\tag{101.22}
```

Equation (101.22) is the new local attachment-density floor.  Section 96 used only
three guaranteed `phi`-gaps and therefore retained only `3 sin(theta)` on the right of
its doubled-density inequality.  The full complement budget forces one additional
amount of angular mass and raises that chord currency to
`sin(theta/2)+2 sin(theta)`.

## 101.4 Section 100 supplies the opposite density ceiling

Canonical Section 100 gives

```math
\boxed{
2\alpha\le3\theta-2\pi.
}
\tag{101.23}
```

Combining (101.22a) with `2alpha<=m` gives

```math
m\ge\sin(\theta/2)+\sin((\theta-m)/2)+\sin\theta.
\tag{101.23a}
```

For fixed `theta`, the left-minus-right side has derivative

```math
1+{1\over2}\cos((\theta-m)/2)>0.
```

Thus the easiest admissible case is the largest allowed support measure
`m=U=3theta-2pi`.  Since `theta-U=phi` and `sin(phi/2)=sin(theta)`, every wrapping
limit must satisfy

```math
\boxed{
\sin(\theta/2)+2\sin\theta
\le3\theta-2\pi.
}
\tag{101.24}
```

Define

```math
F(\theta)
:=3\theta-2\pi-\sin(\theta/2)-2\sin\theta,
\qquad 2\pi/3\le\theta<\pi.
\tag{101.25}
```

Then

```math
F'(\theta)
=3-{1\over2}\cos(\theta/2)-2\cos\theta.
\tag{101.26}
```

On `[2pi/3,pi)`, `cos(theta)<=-1/2` and `0<cos(theta/2)<=1/2`, so

```math
F'(\theta)
\ge3-{1\over4}+1
={15\over4}>0.
\tag{101.27}
```

Also

```math
F(2\pi/3)<0,
\qquad
\lim_{\theta\uparrow\pi}F(\theta)=\pi-1>0.
```

Hence there is a unique root `theta_8` in `(2pi/3,pi)`, and (101.24) forces

```math
\theta\ge\theta_8.
\tag{101.28}
```

The scalar certificate gives

```math
\boxed{
\theta_8
=2.7029080296483676832\ldots,
\qquad
\mu_8:=\sin(\theta_8/2)
=0.9760407652670519821\ldots .
}
\tag{101.29}
```

Therefore every wrapping Type-II harmonic-cell limit satisfies

```math
\boxed{
\lambda\ge\mu_8=0.976040765267052\ldots .
}
\tag{101.30}
```

## 101.5 Propagation to an actual macroscopic carrier

Fix any `mu<mu_8`.  Assuming the Section-100 circle theorem, (101.30) shows that a
macroscopic harmonic-cell limit of normalized diameter at most `mu` cannot be wrapping.
It is therefore cap type.  Canonical Section 88's cap-family capacity theorem applies:

```math
\limsup {1\over D^2}
\sum_{\operatorname{diam}(P_r)\le\mu D}
\operatorname{area}(P_r)
\le\mathcal C(\mu)<{\pi\over4}.
\tag{101.31}
```

The canonical total harmonic-cell perimeter bound leaves only uniformly many cells
longer than `mu D`, and canonical Section 83 gives summed local rhombic deficit
`o(D^2)`.  Hence one long cell is macroscopic and locally rhombus-saturated.

At `mu_8`, with `theta_8=2 asin(mu_8)`, the Section-88 cap function has

```math
\mathcal C(\mu_8)=0.5830784079\ldots,
\qquad
{\pi\over4}-\mathcal C(\mu_8)
=0.2023197554\ldots>0.
\tag{101.32}
```

Thus a diagonal choice `mu upward mu_8` yields actual cells `P_*` with

```math
\boxed{
\operatorname{diam}(P_*)
\ge(\mu_8-o(1))D,
\qquad
\operatorname{area}(P_*)\ge c_8D^2,
\qquad
{A_{4,*}\over\operatorname{area}(P_*)}\to1
}
\tag{101.33}
```

for one absolute `c_8>0`.

## 101.6 Endpoint structure

A sequence approaching `theta_8` must make both (101.22) and (101.23) asymptotically
tight.  In particular:

1. `|S|=3theta_8-2pi` in the Section-100 support theorem;
2. `2alpha=3theta_8-2pi` and boundary unit-spacing capacity is saturated;
3. the complement-chord minimization is sharp, so after discarding zero-measure
   splitting the complement-gap vector is `(theta_8,phi_8,phi_8)`;
4. the exact Section-82 correction currency satisfies
   ```math
   s_D/D\to0,
   \qquad c_D/D\to0,
   \qquad Q_D/D\to0;
   
   ```
5. the three macroscopic outer contact routes across those complement gaps are
   asymptotically Euclidean geodesics.

The sharp circle model is explicit: one support arc has angular length

```math
U_8=3\theta_8-2\pi,
```

while the other two wrapping clusters degenerate to isolated support points.  The
three complementary gaps then have lengths `(theta_8,phi_8,phi_8)`.  This model
saturates the one-dimensional support and chord inequalities simultaneously.

Thus the next obstruction is no longer a diffuse six-cluster problem.  A live endpoint
would force almost every attachment into one dense force-circle arc, with only two
macroscopic anchor clusters carrying zero angular measure, while the same cell contains
a quadratic near-rhombic interior and an explicit linear-by-linear ordered train grid.
That concentration/grid coexistence is the natural next target.

## 101.7 Dependency and regression audit

- **Canonical Section 100 / `C-WRAP-ANGULAR-MEASURE`:** sharp wrapping support measure
  `|S|<=3theta-2pi` and attachment-density ceiling
  `2alpha<=3theta-2pi`.
- **Canonical Section 94:** three distinct support-free arcs of length
  `phi=2pi-2theta`, hence three distinct complement components of at least that length.
- **Canonical Sections 62 and 82:** consecutive-attachment outer-face routes and exact
  local identity `L+Q=4a-6-2s-2c`.
- **Canonical Type-II near-disk geometry / Section 93:** force-hull radii
  `(1/2+o(1))D`, used to convert angular gaps into Euclidean chord lower bounds.
- **Canonical Sections 83 and 88:** cap-family propagation and local-rhombic-deficit
  summability for the actual-carrier conclusion.
- **Countably many complement gaps:** handled by finite subfamilies followed by
  monotone convergence; no unjustified infinite outer-walk summation is used.
- **Bridges and repeated outer-face edge occurrences:** harmless because all selected
  consecutive-attachment routes are disjoint intervals of the outer-face walk in the
  same multiplicity convention as Section 62.
- **Contact-isolated source points:** untouched.
- **No Cauchy perimeter bound, no Section-97/98 endpoint claim, no rejected cyclic-cap
  theorem, and no KKT coefficient floor.**

**Theorem state:** canonical as `C-WRAP-COMPLEMENT-CHORD` in audit.41 after the
independent promotion audit and finite-gap Hausdorff repair above. C-II remains open.
