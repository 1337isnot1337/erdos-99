> Generated reading edition · [exact source](../../../docs/audits/target_c_lattice_population_reserve_independent_audit_2026-10-08.md) · source SHA-256 `7bb836f294fda77364119c144aa8d2efc0d1443247c03acbf7c6e22f8d86a502`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-555ECE44F892","canonical":true,"claim_ids":["C-GLOBAL-POPULATION-EXCESS-SQRT-RESERVE"],"claim_statuses":{"C-GLOBAL-POPULATION-EXCESS-SQRT-RESERVE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.165 — translated triangular-lattice population reserve

**Audit base:** `origin/main=e41da1278ed9c4d77110ec1616dbd83eecf53d22`, state `2026-10-08.audit.160`; C-II and Level I remain open. The proof uses no Target C theorem premise.

**Frozen research source:** `origin/research/level-i-closure-20261007` at `c981b6f818764765bcb99917a9d858599c425471`.

**Audited source artifacts:**

- `docs/reports/full_source_growing_lattice_population_reserve_2026-10-08.md`, SHA-256 `f166831af97d452701b9084ade15817df707d59e2d7e7299605928de37381c73`;
- `research/verify_growing_lattice_population_reserve_2026_10_08.py`, SHA-256 `47337264352ffa31bf9fe491c699f31843c2bf9b10d491cd52aec8914762a2cb`.

## Claim and verdict

**PASS — promote `C-GLOBAL-POPULATION-EXCESS-SQRT-RESERVE`.** For every finite planar unit-separated `n`-point global diameter minimizer with diameter `D>=3`, letting

```math
 g_A=n-1-\frac{\pi D^2}{2\sqrt3},
```

one has

```math
 g_A\ge \frac{3^{5/4}}{256\pi}\sqrt D>\frac{\sqrt D}{256}.
```

This statement applies to every global minimizer, including triangle-bearing ones. It has no triangle-free, contact-minimality, contact-isolate, KKT, stress, or source-subset hypothesis. It is a necessary population comparison and yields no source-preserving move, triangle conclusion, C-II closure, or Level I result.

## Independent proof reconstruction

Let `Lambda` be the triangular lattice with minimum spacing one and covolume `a0=sqrt(3)/2`; let `F` be a fundamental parallelogram. For `R=D/2`, define the periodic disk count

```math
 N_R(t)=\#((\Lambda-t)\cap B(0,R)),\qquad \mu_R=\pi R^2/a_0,
```

using the open disk. Unfolding the finite lattice sum gives mean `mu_R`. For every nonzero reciprocal vector `k`, its Fourier coefficient is

```math
 \widehat{N_R-\mu_R}(k)=\frac{R}{a_0|k|}J_1(2\pi R|k|).
```

This follows directly by polar integration: DLMF 10.9.1 gives the angular `J_0` integral and DLMF 10.22.1 at order zero gives `int_0^x t J_0(t)dt=xJ_1(x)`. No Fourier-series convergence or Poisson summation is used.

For almost every translation, no lattice point lies on the disk boundary. If such a disk contained `n` lattice points, those points would be unit-separated and strictly inside a disk of diameter `D`, hence would have diameter strictly below `D`; that contradicts global minimality. Therefore `N_R(t)<=n-1` almost everywhere. For the mean-zero function `f_R=N_R-mu_R`, this implies

```math
 g_A\ge \operatorname{ess\,sup} f_R.
```

Also, any nonzero Fourier coefficient satisfies

```math
 |\widehat f_R(k)|\le \int_F|f_R|=2\int_F(f_R)_+\le2\operatorname{ess\,sup}f_R,
```

where integration is normalized on `F`.

Take a shortest reciprocal vector with `|k|=2/sqrt(3)` and its double. Put `z=2*pi*R*|k|=2*pi*D/sqrt(3)`, `theta=z-3*pi/4`, and `A_R=3^(1/4)*sqrt(R)/(pi*sqrt(2))`. NIST DLMF 10.17(iii), with real order `nu=1` and one retained Hankel term, gives for every real `z>0`

```math
 \left|\sqrt{\frac{\pi z}{2}}J_1(z)-\cos(z-3\pi/4)\right|\le\frac{3}{8z}.
```

The first and doubled Fourier modes, divided by `A_R`, have leading terms `cos(theta)` and `2^(-3/2)cos(2theta+3pi/4)`. Their remainders are at most `3/(8z)` and `2^(-3/2)*3/(16z)`. The phase inequality

```math
 \max\{|\cos\theta|,2^{-3/2}|\cos(2\theta+3\pi/4)|\}\ge3/32
```

holds for every real `theta`: if `|cos(theta)|>=1/4`, the first term suffices; otherwise writing `c=cos(theta)`, `s=sin(theta)` makes the second term `|2c^2-1+2cs|/4>=3/32`.

For `z>=8`, both normalized remainder bounds are at most `3/64`. Hence one of the two Fourier coefficients has magnitude at least `(3/64)A_R`, so `ess sup f_R >=(3/128)A_R`. Since `D>=3` gives `z>8`, substituting `R=D/2` yields the stated constant. Finally `3^(5/4)>pi`, certified by `pi<22/7` and `(22/7)^4<243`.

## Hostile checks and scope

- The open disk and almost-everywhere boundary exclusion are essential to get a strict-diameter contradiction. Closed-disk counts alone could include diameter-`D` ties.
- The Fourier coefficients are individual integrals of a bounded periodic counting function; no pointwise Fourier-series assertion is needed.
- The two frequencies explicitly prevent phase cancellation; a single shortest frequency would not give a uniform lower bound.
- The theorem concerns all global minimizers. It does not claim that the comparison lattice is embedded in the source or that excess can be spent as an exchange.
- No assumption about triangle-freeness or contact population enters the proof.

## Verifier boundary

Inspected and reran the source verifier. Its exact rational phase arithmetic checks `3/32`, the `3/64` remainder margin at `z=8`, `pi<22/7`, and the final constant comparison. Its separate finite-patch routine enumerates 1,280 rational translations over radii `10,20,50,100,200`, certifies 192,306 lattice points across 878 rows, and proves strict containment, spacing after a common expansion, and a strict same-cardinality unexpanded competitor for those finite patches. These examples are nonglobal and do not prove the universal Fourier theorem or the global-minimizer inequality.

**Verdict:** PASS — promote the exact universal reserve only. C-II and Level I remain open.
