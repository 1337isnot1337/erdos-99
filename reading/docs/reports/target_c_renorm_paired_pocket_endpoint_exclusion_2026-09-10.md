> Generated reading edition · [exact source](../../../docs/reports/target_c_renorm_paired_pocket_endpoint_exclusion_2026-09-10.md) · source SHA-256 `1a82bb80be0e62cefb15b20ca525de300d40258322c9411ed8e3d084f3fcf473`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-771BE7CAFE2C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact remainder excludes the renormalized paired-pocket endpoint

**Date:** 2026-09-10  
**Repository branch:** `research/c2-renorm-paired-pocket-20260910`  
**Depends on:** RP, PC/TN, Cauchy perimeter-diameter bound  
**Target:** Target C, all post-ZF survivors  

## LEVEL I STATUS

`STILL OPEN`.

The preceding RP report proves

```math
\liminf \mu_D\ge \mu_{RP}
=\frac{\pi(2\sqrt{3\pi^2+1}-1)}{4\pi^2+1}
=0.7811638359065726\ldots,
```

where

```math
\mu_D=\frac{e_{BB}+2s_C-3(d_H+s_Z)}D.
```

This addendum proves that equality is impossible. Hence there is a uniform nonexplicit
positive gap above `mu_RP`.

## 1. Exact remainder in the RP pocket budget

Put

```math
k=d_H+s_Z,
\qquad X=d_P+Q.
```

PC gives exactly

```math
e_{BB}=X+2k+c_B.
\tag{1.1}
```

Therefore the definition of `mu_D` gives

```math
X=\mu_DD+k-c_B-2s_C.
\tag{1.2}
```

The exact PC/TN boundary identity is

```math
q=a+X+2k.
\tag{1.3}
```

Since `q=h+d_H`, this is

```math
X=h-d_H-2s_Z-a.
\tag{1.4}
```

Adding (1.2) and (1.4) cancels `d_H` exactly:

### Theorem RPE.1 — exact renormalized pocket remainder

```math
\boxed{
2(d_P+Q)
=
\mu_DD+h-s_Z-a-c_B-2s_C.
}
\tag{RPE.1}
```

Every subtracted quantity on the right is nonnegative.  RP.3 is therefore the
relaxation obtained by discarding the explicit remainder

```math
s_Z+a+c_B+2s_C.
```

This exact identity is stronger than the inequality recorded in the first RP report.

## 2. Equality in the RP scalar theorem forces the discarded remainder to vanish

Assume for contradiction that an unbounded post-ZF survivor sequence satisfies

```math
\mu_D\to\mu_{RP}.
\tag{2.1}
```

RP derives the necessary inequality

```math
\Phi(y)
\le
\frac\pi4\mu^2+
\frac{(\mu+y)^2}{16\pi},
\qquad
2\rho\le y\le\pi,
\tag{2.2}
```

for every subsequential limit `y=h/D`.  The function

```math
F_\mu(y)=\Phi(y)-\frac\pi4\mu^2-rac{(\mu+y)^2}{16\pi}
```

is strictly concave.  At `mu=mu_RP`, the endpoint `y=pi` is exactly zero, while the
`y=2rho` endpoint has a fixed positive margin.  Strict concavity therefore implies
that (2.1) forces

```math
\boxed{h/D\to\pi.}
\tag{2.3}
```

Now write

```math
\tau=d_P/D,
\qquad \nu=Q/D.
```

The RP cavity upper bound uses

```math
\tau^2+\nu^2
\le(\tau+\nu)^2
\le\left(\frac{\mu_D+h/D}{2}\right)^2,
\tag{2.4}
```

where the second inequality is RPE.1 after discarding

```math
\frac{s_Z+a+c_B+2s_C}{D}.
```

At the scalar endpoint all inequalities contributing to (2.2) must be asymptotically
sharp; otherwise a fixed positive loss would leave `F_{mu_RP}(pi)>0`.  Consequently

```math
\boxed{
\frac{s_Z}{D},\frac aD,\frac{c_B}{D},\frac{s_C}{D}\to0.
}
\tag{2.5}
```

In particular, (1.2) gives

```math
\frac XD
=
\mu_D+rac{d_H+s_Z}{D}-\frac{c_B+2s_C}{D}
=
\mu_{RP}+\frac{d_H}{D}+o(1).
\tag{2.6}
```

## 3. Maximal diameter-edge density kills `d_H`

Every positively loaded vertex is a force-hull vertex.  Consecutive loaded vertices
on `F` are distinct source points and hence have distance at least one.  Therefore

```math
q\le P_F.
\tag{3.1}
```

Cauchy's perimeter-diameter inequality gives

```math
P_F\le\pi D.
\tag{3.2}
```

Since `q=h+d_H`, equations (2.3), (3.1), and (3.2) yield

```math
0\le\frac{d_H}{D}
\le\pi-\frac hD
\to0.
\tag{3.3}
```

Thus (2.6) simplifies to

```math
\boxed{X/D\to\mu_{RP}.}
\tag{3.4}
```

On the other hand, the exact boundary identity (1.3), divided by `D`, gives

```math
\frac XD
=
\frac qD-\frac aD-2\frac{d_H+s_Z}{D}.
\tag{3.5}
```

Now `q/D=h/D+d_H/D->pi`, while (2.5) and (3.3) make the remaining terms vanish.
Hence

```math
\boxed{X/D\to\pi.}
\tag{3.6}
```

Equations (3.4) and (3.6) are incompatible because `mu_RP<0.8<pi`.

Therefore no endpoint sequence exists.

### Theorem RPE.2 — endpoint exclusion

There is no unbounded post-ZF survivor sequence with

```math
\mu_D\to\mu_{RP}.
\tag{RPE.2}
```

### Corollary RPE.3 — uniform positive gap

There exist absolute constants `epsilon_RP>0` and `D_0<infinity` such that every
post-ZF survivor with `D>=D_0` satisfies

```math
\boxed{
\mu_D\ge\mu_{RP}+\epsilon_{RP}.
}
\tag{RPE.3}
```

Indeed, otherwise choose a sequence with `D_j->infinity` and
`mu_{D_j}<mu_RP+1/j`; RP gives the matching lower limit and RPE.2 contradicts the
resulting convergence.

## 4. What the endpoint contradiction uses

The contradiction is not a new packing-density estimate.  It comes from the
incompatibility of two equality requirements:

1. RP cavity equality wants the pocket/face currency `X=d_P+Q` to be the average of
   the renormalized surplus and diameter-edge density;
2. when `h/D->pi`, convex perimeter forces `d_H=o(D)`, and the exact force-boundary
   ledger forces `X/D->pi` unless one of the discarded RP remainder terms is linear;
3. but linear remainder destroys RP equality.

Thus maximal projective diameter-edge density cannot be the scalar RP optimizer.

## 5. Remaining target

Level I remains open.  The next highest-value step is quantitative stability of this
contradiction.  One should retain

```math
2X=\mu_DD+h-s_Z-a-c_B-2s_C
```

and

```math
d_H/D\le\pi-h/D
```

inside the paired-pocket cavity optimization rather than discard them.  This should
push the explicit lower bound above `mu_RP`; the endpoint contradiction has a very
large structural gap (`pi-mu_RP>2.36`).

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Exact remainder:
  2(d_P+Q)=mu_D D+h-s_Z-a-c_B-2s_C.

RP gives mu_D>=mu_RP=0.7811638359... and equality would force h/D->pi.
At equality the discarded remainder must be o(D), so
  s_Z,a,c_B,s_C=o(D).
Since q=h+d_H<=P_F<=pi D,
  d_H=o(D).
Then PC gives
  (d_P+Q)/D -> mu_RP,
while the exact boundary identity
  q=a+d_P+Q+2(d_H+s_Z)
forces
  (d_P+Q)/D -> pi.
Contradiction.
Hence there is an absolute epsilon_RP>0 with
  mu_D>=mu_RP+epsilon_RP
for all sufficiently large post-ZF survivors.

Next: quantify this equality incompatibility to raise the explicit constant.
```
