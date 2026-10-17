> Generated reading edition · [exact source](../../../docs/reports/target_c_nm_fsdb_joint_defect_floor_2026-09-11.md) · source SHA-256 `499981fb0c56eda37fcc276daff0029dad08b009d4cdad17d5df2d344b143d10`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2B2895EE5D9D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — near-matching/force-hull joint defect floor

**Date:** 2026-09-11

**Target:** Target C, C-II

**Status:** unpromoted report-level theorem; route-map status unchanged

**Dependencies:** NM near-matching stability, full-source cell-slack/train capacity,
and the audited FSDB force-hull area inequality.

## Level-I status

`STILL OPEN`.

The near-matching theorem and the full-source train-capacity theorem constrain the
same currencies in opposite ways.  Combining them gives a stronger all-branch
defect floor than either theorem separately.

Write

```math
r_D=\frac{x_B+Q}{D},\qquad
\sigma_D=\frac{s_Z}{D},\qquad
r_H=\frac{2h-q}{D}=r_D+2\sigma_D.
```

The near-matching theorem gives

```math
\liminf r_H\ge c_*:=\frac{2\rho}{3}=0.4927234221\ldots,
\qquad \rho=\cos\rho.
\tag{1}
```

The joint consequence is

```math
\boxed{\liminf r_D\ge \varepsilon_* =0.0892450168\ldots.}
\tag{2}
```

More invariantly, $`\varepsilon_*`$ is the unique root in $`(0,c_*)`$ of

```math
\frac{\sqrt3}{8}\left(\frac\pi2+\frac52r\right)^2
 =
\frac{\pi/2+c_*/2+\sin(\pi/2+c_*/2)}4.
\tag{3}
```

The theorem applies to cyclic and forest diameter topology, arbitrary $`s_Z`$,
exceptional faces, and contact-isolated source points, subject only to the
report-level FSDB/FSCS inputs used by the earlier full-source area theorem.

It does not eliminate the linear-defect regime.

## Proof

Put

```math
r=\lim r_D,
\qquad
\sigma=\lim\sigma_D,
\qquad
k=\lim\frac{d_H+s_Z}{D}
```

along a subsequence, after passing to further subsequences when necessary.  The
exact post-ZF identities are

```math
q=x_B+Q+2(d_H+s_Z),
\qquad
h=x_B+Q+d_H+2s_Z.
\tag{4}
```

Since $`q\le\operatorname{per}F\le\pi D`$,

```math
k\le\frac{\pi-r}{2}.
\tag{5}
```

Also

```math
\frac hD=r+k+\frac{s_Z}{D}\ge r+k.
\tag{6}
```

The full-source cell-slack/train argument gives, with $`X=x_B/D`$,
$`Y=Q/D`$, and $`F_0=f/D`$,

```math
\frac{\operatorname{area}F}{D^2}
\le
\frac{a_0}{4}(r+k+2F_0)^2
 +
\frac{9X^2}{\pi}
 +
\frac{(Y-F_0)^2}{4\pi}+o(1),
\qquad a_0=\frac{\sqrt3}{2}.
\tag{7}
```

For fixed $`r,X,Y,F_0`$, subtract the force-hull lower bound
$`\Phi(\max\{2\rho,r+k+s_Z/D\})`$, where

```math
\Phi(t)=\frac{t+\sin t}{4}.
```

The resulting difference is increasing in $`k`$: below $`2\rho`$ only the
quadratic upper bound changes, and above $`2\rho`$ its derivative is at least
$`a_0\rho>1/2`$, whereas $`\Phi'(t)\le1/2`$.  Therefore feasibility at the
actual $`k`$ implies feasibility at the maximal value in (5).

At that value put

```math
z=r+k=\frac{\pi+r}{2}.
```

For fixed $`r`$, the right side of (7) is convex successively in $`F_0`$ and
in $`X`$.  Its maximum over $`0\le F_0\le Y`$, $`X+Y=r`$, occurs at a corner.
For $`0\le r\le0.1`$, the largest corner is

```math
X=0,qquad F_0=Y=r,
```

and hence

```math
\frac{\operatorname{area}F}{D^2}
\le
U(r)+o(1),
\qquad
U(r):=\frac{\sqrt3}{8}\left(\frac\pi2+\frac52r\right)^2.
\tag{8}
```

Now suppose $`r<c_*`$.  From (1) and the exact identity
$`r_H=r+2\sigma`$,

```math
\sigma\ge\frac{c_*-r}{2}.
\tag{9}
```

At maximal $`k`$, (6) and (9) give

```math
\frac hD
\ge z+\sigma
\ge \frac\pi2+\frac{c_*}{2}.
\tag{10}
```

Therefore FSDB gives the fixed lower area bound

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge
L_*:=
\frac{\pi/2+c_*/2+\sin(\pi/2+c_*/2)}4.
\tag{11}
```

The function $`U`$ is strictly increasing.  Direct rational bounds for $`\pi`$,
$`\sqrt3`$, and $`\rho`$ show

```math
U(0)<L_*<U(0.1).
```

For an explicit sign certificate, use
$`739/1000<\rho<37/50`$, $`3141/1000<\pi<22/7`$, and
$`1732/1000<\sqrt3<1733/1000`$.  The angle
$`\pi/2+c_*/2`$ lies in $`(1.81,1.83)`$, where the elementary sine bounds give
$`\sin t>0.97`$.  These estimates imply
$`U(0)<0.535<L_*`$ and $`L_*<0.705<U(0.1)`$.

Let $`\varepsilon_*`$ be the unique root of $`U(r)=L_*`$.  Equations
(8)--(11) contradict $`r<\varepsilon_*`$.  If instead $`r\ge c_*`$, then
the stronger bound $`r\ge c_*>\varepsilon_*`$ already holds.  Hence (2).
$`\square`$

## What remains

The coupling removes the regime in which both the actual diameter graph is nearly
matching and the outer/exceptional defect is small.  It still permits, for example,

```math
r_D\asymp 0.1,
\qquad
\sigma_D\asymp0.2,
\qquad
q/D\to\pi,
```

and the current area estimates do not contradict this allocation.  The live
obstructions remain:

* generic-transfer forests;
* cyclic high surplus with no upper tradeoff for $`e_{BB}+2s_C`$;
* positive mixed surplus without a support-to-motion theorem; and
* contact-isolated populations and giant exceptional faces.

The result is therefore a genuine branch coupling, not a Level-I settlement.
