> Generated reading edition · [exact source](../../../docs/reports/full_source_growing_lattice_population_reserve_2026-10-08.md) · source SHA-256 `89ee0f2a1dba1dce57d055f15bd0c1b20a46935b2f347cca22cf24ccbaedd01c`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "cbc775b76361534ecc4238598ef0784680b68733", "source_branch_refs": ["refs/heads/research/level-i-closure-20261007"], "source_commit": "3d4d6024cb5892580103450162b07cdaf1b513c7", "source_lifecycle": "unreviewed", "source_path": "docs/reports/full_source_growing_lattice_population_reserve_2026-10-08.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f166831af97d452701b9084ade15817df707d59e2d7e7299605928de37381c73"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Full-source comparison: two lattice modes force a growing population reserve

Date: 2026-10-08. Research start: `4a2505e7adfef864f0fd572aa4ff3366b734bf55`.
Fixed main: `163010ca099dd6e21505ae574484fb8006a5a5de`.
State: `2026-10-08.audit.157`.
Classification: **proved candidate awaiting independent audit**.
Registry status: unreviewed; canonical=false. Level I remains open.

The attacked implication is

`global minimum diameter -> uniform growing translated-lattice reserve
-> exclude bounded/o(sqrt(D)) population-excess obstructions`.

This does not supply a source-preserving replacement for a general
C-II survivor whose population excess can be of boundary order.

## 1. Candidate global comparison

For every global unit-separated n-point planar diameter minimizer
with `D>=3`, put

```math
\Delta=\frac{\pi}{2\sqrt3},\qquad g_A=n-1-\Delta D^2.
```

The [canonical full-source comparison](../targets/target-c/58-full-source-geometry-audit.md)
gives `g_A>0`. The candidate strengthens it to

```math
\boxed{
g_A\ge \frac{3^{5/4}}{256\pi}\sqrt D
>\frac{\sqrt D}{256}.
} \tag{1}
```

This uses no triangle-free hypothesis, KKT stress, contact-core
identification or assumption about contact isolates. It concerns
every global minimizer. It asserts a necessary comparison bound,
not that the source is contained in the comparison lattice.

## 2. Translation counts and their individual Fourier coefficients

Let `Lambda` be the separation-one triangular lattice, with
covolume `a_0=sqrt(3)/2`. Let `F` be a fundamental parallelogram.
For disk radius `R` define

```math
N_R(t)=\#((\Lambda-t)\cap B(0,R)),\qquad
\mu_R=\frac{\pi R^2}{a_0}.
```

Use normalized integration on `F`. Unfolding the finite lattice
sum gives `int_F N_R=mu_R`. For nonzero `k in Lambda^*`,
the coefficient of `f_R=N_R-mu_R` is

```math
\widehat f_R(k)
=\frac1{a_0}\int_{B(0,R)}e^{2\pi i k\cdot x}\,dx
=\frac{R}{a_0|k|}J_1(2\pi R|k|).
\tag{2}
```

No convergence of a Poisson or Fourier series is invoked.
The angular identity for `J_0` is checked at
[NIST DLMF 10.9.1](https://dlmf.nist.gov/10.9.E1);
the radial antiderivative is
[NIST DLMF 10.22.1](https://dlmf.nist.gov/10.22.E1)
at order zero.

Since `f_R` has mean zero,

```math
|\widehat f_R(k)|\le\int_F|f_R|
=2\int_F(f_R)_+\le2\operatorname{ess\,sup}_F f_R.
\tag{3}
```

Thus one sufficiently large nonzero coefficient forces a positive
translation gain, even without selecting a maximizing translation.

## 3. Checked real-argument Bessel remainder

The primary source checked is
[NIST DLMF 10.17(i) and (iii)](https://dlmf.nist.gov/10.17).
For real `z>0`, order `nu=1`, and one retained Hankel term,
its real-argument first-neglected-term bound gives

```math
H_1^{(1)}(z)=\sqrt{\frac2{\pi z}},
e^{i(z-3\pi/4)}(1+\mathcal R(z)),\qquad
|\mathcal R(z)|\le\frac3{8z}.
```

The written conditions hold: `nu>-1/2` and the number of
retained terms `ell=1>=max(nu-1/2,1)`. Taking real parts gives

```math
\left|\sqrt{\frac{\pi z}{2}}J_1(z)
-\cos(z-3\pi/4)\right|\le\frac3{8z}.
\tag{4}
```

This is a checked error bound with a stated domain, not a
numerical asymptotic approximation.

## 4. A doubled mode prevents simultaneous phase cancellation

Choose a shortest dual vector, of length `s=2/sqrt(3)`, and
its double. Put

```math
z=2\pi Rs,\qquad \theta=z-3\pi/4,\qquad
A_R=\frac{3^{1/4}}{\pi\sqrt2}\sqrt R.
```

Equations (2) and (4) give

```math
\frac{\widehat f_R(k)}{A_R}=\cos\theta+e_1,
\qquad |e_1|\le\frac3{8z},
```
```math
\frac{\widehat f_R(2k)}{A_R}
=2^{-3/2}\cos(2\theta+3\pi/4)+e_2,
\qquad |e_2|\le2^{-3/2}\frac3{16z}.
\tag{5}
```

The two leading phases satisfy

```math
\max\{|\cos\theta|,
2^{-3/2}|\cos(2\theta+3\pi/4)|\}\ge3/32.
\tag{6}
```

Indeed, if `|cos theta|>=1/4`, the first term suffices.
Otherwise write `c=cos theta` and `s_\theta=sin theta`.
The second weighted term equals
`|2c^2-1+2c s_\theta|/4`.
Since `2c^2-1<=-7/8` and `2c s_\theta<=1/2`,
it is at least `3/32`.

For `z>=8`, the two remainder bounds in (5) are at most `3/64`.
Therefore

```math
\max\{|\widehat f_R(k)|,|\widehat f_R(2k)|\}
\ge(3/64)A_R,
```
```math
\operatorname{ess\,sup}(N_R-\mu_R)
\ge\frac3{128}A_R.
\tag{7}
```

The constant is conservative. No claim of optimality is made.

## 5. Apply the reserve to a global minimizer

Set `R=D/2` for the diameter of a global minimizer.
For almost every translation no lattice site lies on the disk
boundary. If such a translation contained `n` sites, all would
lie strictly inside the disk. Any `n` of them would have diameter
strictly less than `2R=D`, contradicting global minimality.
Thus `N_R(t)<=n-1` almost everywhere, and

```math
g_A=n-1-\mu_R
\ge\operatorname{ess\,sup}(N_R-\mu_R).
```

For `D>=3`, `z=2pi D/sqrt(3)>8`. Substituting (7) gives
the first inequality in (1). The second follows from
`3^{5/4}>pi`, for example by `pi<22/7` and `(22/7)^4<243`.
This completes the candidate proof.

## 6. Consequence for the source-wide ledgers

The [Voronoi ledger](target_c_full_source_voronoi_defect_spacing_debit_2026-10-08.md)
and [Delaunay ledger](target_c_full_source_delaunay_strain_and_branching_2026-10-08.md)
keep the term `a_0 g_A` exactly. Equation (1) supplies a growing
reserve in each. In particular, no unbounded family of global
minimizers can have `g_A=o(sqrt(D))`, and a putative bound
`g_A<=M` would force `D<(256M)^2`.

Neither source-wide ledger bounds `g_A` by a constant.
They still permit `g_A=Theta(D)`, total boundary-order strain,
exception seams, and a quadratic population of near-unit
contact isolates. No current C-II branch is closed by (1) alone.

## 7. Exact arithmetic and finite comparison patches

The [checker](../../../research/verify_growing_lattice_population_reserve_2026_10_08.py)
checks the rational two-phase interval bound, remainder threshold
and conservative constant. It searches a fixed rational translation
grid for several finite disk radii using exact integer row counts.
Every counted lattice point lies strictly inside the disk.
The finite comparisons demonstrate the normalization; they do not
prove the universal Fourier bound or certify global optimality.

Each selected patch also yields a triangle-free all-isolated
nonglobal source by an explicitly small common expansion that
keeps every point inside the same radius. An unexpanded patch
is a strict same-cardinality competitor. These examples pass a
positive growing population-excess lower test; they prevent
treating that necessary test alone as a triangle-forcing theorem.

The row certificate uses
`q^2 |i u+j v-t|^2=d^2+de+e^2`, where
`d=qi-a` and `e=qj-b`. Multiplying by four makes the row
inequality `(2e+d)^2<=4(q^2R^2-1)-3d^2`.
Integer square roots therefore count each strict-disk row exactly.
All lattice differences have positive integer squared norm
`i^2+ij+j^2`, hence at least one; an explicit unit pair is retained.
No quadratic enumeration of all patch pairs is claimed.

The final checker passed five radii (10, 20, 50, 100, 200) and
1,280 sampled translations. Its selected patches have 365, 1,456,
9,078, 36,290 and 145,117 points, for 192,306 certified points
in 878 integer rows. Rational pi bounds and the phase/remainder
constants passed. Every expanded patch passes the reserve test
and has a certified strict scaling competitor. Python compilation
passed. None of these counts certifies any patch globally optimal.

All claims in this report remain candidates awaiting independent
audit. The general compatible replacement and Level I steps are
unproved.
