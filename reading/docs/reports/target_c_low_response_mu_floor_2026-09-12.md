> Generated reading edition · [exact source](../../../docs/reports/target_c_low_response_mu_floor_2026-09-12.md) · source SHA-256 `4d7ab946aae05678753dda8dc4ee6d5cc5ee0409a2b74380b2dbc5a6db0603cf`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CA5C87DD9A82","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — response defect localizes contact stress into near-diameter cells

**Date:** 2026-09-12  
**Repository commit at start:** `9cdc955468f0ecbc23f9b095eb06947b8f8550eb`  
**State version:** `2026-09-12.audit.44`  
**Target:** full-source Target C-II  
**Classification:** proved candidate awaiting promotion; this report is unreviewed and noncanonical  
**Level I status:** STILL OPEN; C-II is not resolved here

## 1. Statement and exact novelty

Use the canonical contact-minimal, then diameter-pair-minimal C-II normal form. Keep
all source points, including contact-isolated points. Let `D` be the source diameter,
and let `I_r` be the unloaded positive-contact components with loaded attachment sets
`A_r`. Write

```math
 L_r:=\operatorname{diam}(A_r),\qquad
 S_r:=\sum_{e\in E_r}\alpha_e,
```

where `E_r` consists of the internal contacts of `I_r` and its contacts to loaded
vertices. Let `S_BB` be the stress on direct loaded-loaded contacts. Define the C41
response defect

```math
 \varepsilon_D:=\sum_{b<k}c_{bk}-1>0,
```

where `c_bk` are the full Kron response conductances on the loaded hull. Define the
canonical renormalized surplus

```math
 \mu_D:=\frac{e_{BB}+2s_C-3k}{D},
 \qquad k=d_H+s_Z.
```

The already recorded RCC report proves the stronger scalar bound

```math
 \mu_D\ge(1+\varepsilon_D)^{-1/2}-\frac8D.
```

The scalar inequality below is therefore not claimed as a new frontier. The new
candidate content here is the stress localization that follows from the component
Dirichlet energy identity: it does not assume C66/C70, a star center, or a unique
long component.

Every sufficiently large source with `0<=epsilon_D<=1` satisfies the finite
candidate inequality

```math
\boxed{\mu_D\ge \sqrt{1-\varepsilon_D}-\frac8D.}
\tag{LR.1}
```

Consequently, along every C-II sequence with `D epsilon_D -> 0`,

```math
\boxed{\liminf \mu_D\ge1.}
\tag{LR.2}
```

The theorem is a stress-localization branch reduction only. It does not exclude the
remaining `mu_D>=1` low-response branch, and it does not prove C-II.

## 2. Exact inputs

The proof uses the following statements, with their current dispositions.

1. The canonical C41 response identity decomposes the unscaled response defect as

   ```math
   D^2\varepsilon_D
   =(D^2-1)S_{BB}+\sum_r E_r,
   \qquad
   E_r:=\sum_{s<t\in A_r}c^{(r)}_{st}(D^2-|s-t|^2)\ge0.
   \tag{LR.3}
   
   ```

   Here `c^(r)` is the Kron response of `I_r`. Direct loaded-loaded contacts have
   unit length and give the first term.

2. The component harmonic-coordinate energy identity is exact:

   ```math
   S_r=\sum_{s<t\in A_r}c^{(r)}_{st}|s-t|^2.
   \tag{LR.4}
   
   ```

   This is the HSR candidate report
   `target_c_component_stress_response_diameter_2026-09-09.md`; no lower bound on an
   individual KKT coefficient is used.

3. Canonical C40 gives

   ```math
   L_r\le\delta_r+2,
   \tag{LR.5}
   
   ```

   where `delta_r` is the contact-graph diameter of `I_r`.

4. Canonical Section 62 gives the exact nonnegative ledger

   ```math
   \sum_r\delta_r+R_I+s_B+3k=6+e_{BB}+2s_C.
   \tag{LR.6}
   
   ```

   Hence

   ```math
   \sum_r\delta_r\le \mu_DD+6.
   \tag{LR.7}
   
   ```

5. The full-source virial normalization is

   ```math
   S_{BB}+\sum_r S_r=D^2.
   \tag{LR.8}
   
   ```

   Contact-isolated source points have no positive contact stress and are not removed
   from the source; they simply do not occur in (LR.8)'s contact-edge partition.

## 3. HSR aggregate bound

For each component, (LR.4) and the definition of `L_r` give

```math
 S_r\le L_r^2 C_r,
 \qquad C_r:=\sum_{s<t\in A_r}c^{(r)}_{st}.
```

Since `E_r=D^2C_r-S_r`, whenever `L_r<D`,

```math
 E_r\ge S_r\left(\frac{D^2}{L_r^2}-1\right),
 \qquad
 S_r\le \frac{L_r^2}{D^2-L_r^2}E_r.
\tag{LR.9}
```

Let `L_*:=max_r L_r`. If `L_*<D`, summing (LR.9) and using (LR.3) gives

```math
 T:=\sum_rS_r
 \le \frac{L_*^2}{D^2-L_*^2}D^2\varepsilon_D.
\tag{LR.10}
```

The same decomposition also gives

```math
 S_{BB}\le \frac{D^2}{D^2-1}\varepsilon_D.
\tag{LR.11}
```

If there were no unloaded component, then (LR.8) and (LR.11) would contradict
`epsilon_D<=1` for all sufficiently large `D`. Thus `L_*` is defined in the range
under consideration. If `L_*=D`, the conclusion below is immediate. Otherwise,
using `T=D^2-S_BB`, rearrange (LR.10):

```math
 \frac{L_*^2}{D^2}
 \ge
 \frac{T}{T+D^2\varepsilon_D}.
\tag{LR.12}
```

Put `t:=T/D^2`. From (LR.11), for `D>=2`,

```math
 {S_{BB}\over D^2}\le {\varepsilon_D\over D^2-1}\le\varepsilon_D,
```

so the virial identity gives

```math
 t=1-{S_{BB}\over D^2}\ge1-\varepsilon_D.
```

The function `t -> t/(t+epsilon_D)` is increasing for `t>=0`. Therefore (LR.12)
gives

```math
 {L_*^2\over D^2}
 \ge {t\over t+\varepsilon_D}
 \ge {1-\varepsilon_D\over(1-\varepsilon_D)+\varepsilon_D}
 =1-\varepsilon_D.
\tag{LR.13}
```

This is the required argument. The earlier draft's statement that a lower bound on
the denominator of (LR.12) implied (LR.13) had the inequality direction backwards;
the theorem survives because the normalized numerator `t` has the displayed lower
bound and the ratio is monotone in `t`.

For `epsilon_D<=1`, (LR.13) gives

```math
 L_*\ge D\sqrt{1-\varepsilon_D}.
\tag{LR.14}
```

The case `L_*=D` also satisfies (LR.14).

## 4. Convert attachment diameter to canonical surplus

Choose a component attaining `L_*`. By (LR.5),

```math
 \delta_*\ge L_*-2\ge D\sqrt{1-\varepsilon_D}-2.
```

Combine this with (LR.7):

```math
 \mu_DD+6\ge\sum_r\delta_r\ge\delta_*,
```

which proves (LR.1):

```math
 \mu_D\ge\sqrt{1-\varepsilon_D}-\frac8D.
```

If `D epsilon_D -> 0`, then `epsilon_D ->0` and the right side tends to one. This
proves (LR.2).

The proof also gives a more operational version of the branch reduction. For every
fixed `eta>0`, the total stress of components with
`L_r <= (1-eta)D` is at most

```math
 \frac{(1-\eta)^2}{1-(1-\eta)^2}D^2\varepsilon_D.
\tag{LR.15}
```

Thus `D epsilon_D ->0` forces almost all `D^2` contact stress into components whose
attachment diameters are `D-o(D)`, while direct loaded-loaded stress is `o(1/D)`.
The cutoff can be sharpened. Put

```math
 \eta_D:=\sqrt{\varepsilon_D/D}.
```

For all sufficiently large `D`, the stress on components with
`L_r <= (1-eta_D)D` is at most

```math
 D^2\frac{\varepsilon_D}{\eta_D}
 =D^2\sqrt{D\varepsilon_D}=o(D^2).
\tag{LR.16}
```

Their attachment diameters are at most
`D-D eta_D=D-sqrt(D epsilon_D)=D-o(1)`. Thus, in the `D epsilon_D -> 0` branch,
all but `o(D^2)` contact stress lies in components with attachment diameter
`D-o(1)`. This is a stress statement; it does not say that one component alone
carries all of that stress.

The canonical all-phase diameter budget also bounds the number of such cells. Since
Section 75 gives `sum_r delta_r <= 2+2*pi*D`, every component in the high-stress
family has

```math
 \delta_r\ge D-\sqrt{D\varepsilon_D}-2.
```

Hence their number is at most

```math
 \frac{2+2\pi D}{D-\sqrt{D\varepsilon_D}-2}<7
```

for all sufficiently large `D`; it is therefore at most six. This is weaker than
the C66/C70 at-most-three star bound, but it does not use a star center.

## 5. What this changes

The existing canonical all-phase Section-75 inequality is

```math
\liminf\left(\mu_D+\frac{2k}{D}\right)\ge2\rho=1.478170\ldots.
```

The RCC report already gives the stronger scalar implication

```math
\mu_D\ge(1+\varepsilon_D)^{-1/2}-8/D,
```

so (LR.1) should not be promoted as a better scalar floor. The independent addition
is the stress statement:

```text
D epsilon_D -> 0  ->  mu_D >= 1-o(1)
mu_D <= 1-eta    ->  epsilon_D is bounded below by a positive eta-dependent constant
```

The second line follows directly from (LR.10) and (LR.7), not from a converse to
C41. It is a response-defect alternative, not a closure: the high-defect branch is
still allowed by the current ledger.

The low-response branch is now reduced to one or more near-diameter attachment cells
with total contact stress `D^2-o(D^2)`, without invoking C66/C70's star localization.
The remaining problem is to exclude those cells using the canonical common-bridge,
radial-train, or source-preserving diameter-decrease machinery. C66/NLC can further
reduce this family to at most three cells, and its slope-one endpoint can reduce it to
one, but those are separate unpromoted hypotheses.

## 6. Regression and scope audit

- No global optimality conclusion is inferred from the response identity alone.
- Contact-isolated source points are retained and are not counted as harmonic
  components.
- No full-source affine-kernel statement is used.
- No universal PSD conclusion, KKT coefficient floor, or simultaneous exchange is
  assumed.
- The argument does not identify a unique component, a unique star center, or a finite
  motion. It only forces near-diameter attachment geometry and stress concentration
  in the low-response branch.
- If `epsilon_D` is not small, (LR.1) may be weaker than the existing canonical
  surplus floor. That is expected; the theorem is aimed at the `D epsilon_D ->0`
  branch.

## 7. Candidate classification and next exact target

## 7.1 Canonical all-phase currency cross-check

The current canonical Section-75 ledger gives an additional exact asymptotic
constraint that is independent of the low-response hypothesis. Its identities are

```math
e_{BB}+s_C=q+k+O(D^{2/3}),
\qquad
\mu_DD=e_{BB}+2s_C-3k,
```

with `k=d_H+s_Z`. Therefore, writing

```math
\lambda_D:={e_{BB}+2s_C\over D},
\qquad
\kappa_D:={k\over D},
```

we have `lambda_D=mu_D+3 kappa_D+o(1)`. The canonical all-phase bound (75.24)
then reads

```math
\boxed{
\liminf(\lambda_D-\kappa_D)\ge2\rho,
\qquad
\lambda_D\ge2\rho+\kappa_D-o(1),
}
\tag{LR.17}
```

along every common subsequence, where `rho=cos rho` and
`2 rho=1.478170...`. This is only an algebraic restatement of the canonical
Section-75 inequality; it is not a new promotion.

The same ledger rewrites the canonical Section-123 payment in a form useful for
the live detour target:

```math
e_{BB}-k=q-s_C+O(D^{2/3}),
```

and therefore

```math
\boxed{
\sum_rP_{{\rm exc},r}
\le10\bigl(q-s_C\bigr)+O(D^{2/3}).
}
\tag{LR.18}
```

Any proposed upper bound on `\sum_r(L_r-2d_r)` must be coupled to this current
currency, not to an older ordinary-surplus scalar. This cross-check does not close
C-II, but it rules out stale slope-one substitutions in the remaining aggregate
detour argument.

## 7.2 A canonical Type-II loaded-hull half-perimeter floor

There is one further finite-to-asymptotic consequence that is useful when splitting
the remaining detour by `q` and `x_B`. Section 63 gives

```math
b=q+x_B,
\qquad
q-x_B=Q+2k\ge2k,
```

and the force-hull outer-walk bound gives `\operatorname{per}(F)\le b`. In the
canonical full-core Type-II branch, Section 80 gives
`\operatorname{per}(F)/D\to\pi`. Consequently

```math
\pi D-o(D)
\le q+x_B
\le2q-2k,
```

so

```math
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge{\pi\over2}.
}
\tag{LR.19}
```

This is a canonical hull/ledger floor, not a claim that `q/D\to\pi` or that
`x_B=o(D)`. It supplies a second live split: a low-`q` Type-II subsequence must
carry linear outer-walk excess, while a near-circle subsequence must pay that
perimeter through the loaded hull itself. Neither side is yet converted into a
strict diameter decrease.

**Classification:** proved candidate awaiting promotion. The algebra and the HSR
energy identity are self-contained, but the HSR report itself is still unreviewed,
and the scalar floor is already dominated by RCC. This report does not enter the
canonical theorem-state manifest.

The proved low-response normal form is a family of at most six harmonic components
`I_{r_1},...,I_{r_m}` (`m<=6`) such that

```math
 L_{r_j}=D-o(1)\quad(1\le j\le m),
```

while collectively

```math
 \sum_{j=1}^m S_{r_j}=D^2-o(D^2),
 \qquad
 \sum_{j=1}^m E_{r_j}=o(D).
```

The last estimate follows from `sum_r E_r<=D^2 epsilon_D=o(D)`. No theorem here
upgrades this collective concentration to one component with stress `D^2-o(D^2)`,
let alone `D^2-o(D)`.

The next exact target is therefore a contradiction for this bounded family of
near-diameter cells, or an additional independently proved localization theorem that
reduces the family to one cell before a one-cell closing argument is invoked. A theorem
that forces a fixed response defect or a strict same-cardinality diameter decrease
from the bounded-family normal form would close the low-response branch. The
high-response branch remains separate.
