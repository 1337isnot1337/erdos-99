<!-- theorem-state: {"artifact_id":"ART-BE818BB1C195","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — sparse full-core exclusion through `sigma=0.0105`

**Date:** 2026-09-12  
**Reviewed:** `docs/reports/target_c_sparse_split_fullcore_window_0105_2026-09-12.md`  
**Classification:** audited-working proof-only candidate; theorem state unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## Verdict

**PASS at the inherited proof-only signed-return/sparse-split scope.**

The extension from `sigma<=0.0088` to

\[
\boxed{\sigma\le0.0105}
\]

is not merely a scalar extrapolation. The geometric hypotheses used by the sharp
Section-118 sparse/directional argument remain valid with strict margins at the new
endpoint. The conservative final residual is above `0.0044`.

The result still does not close C-II. It leaves full-core slack above `0.0105` and the
Type-I inactive-container branch.

---

## 1. The largest-gap transfer does not have an `0.0088` ceiling

The transfer derivative is

\[
\partial_t h_\theta(t)
={1\over2}\cos{\phi+t\over2}
-{1\over2}\cos{\theta-t\over2},
\qquad
\phi=2\pi-2\theta.
\]

On the relevant rectangle `theta>=theta_8`, `0<=t<=0.1`, the hostile Section-117 audit
already checks that this derivative is increasing in `theta`, decreasing in `t`, and
has lower bound above `0.30` at the worst corner. Thus increasing `theta` from the old
Section-118 endpoint to the new value

\[
\theta_0=2.7051406245\ldots
\]

cannot weaken that derivative bound.

The same audit records a transfer cost above `0.0326` for `delta>=0.1`. Since
`w<=sigma<=0.0105`, that branch remains impossible. Therefore

\[
\delta\le {10\over3}w
\]

is valid throughout the enlarged interval.

This is the load-bearing geometry extension.

---

## 2. Tail and fourth-gap geometry have large remaining room

The exact complement-measure identity gives

\[
x_2+x_3+\tau=\delta+x.
\]

Since `x+w<=sigma`,

\[
x_2,x_3,\tau
\le x+{10\over3}w
\le {10\over3}\sigma
\le0.035.
\]

At `sigma=0.0105`, the residual principal gap is

\[
\phi_0=2\pi-2\theta_0
=0.8729040581\ldots .
\]

Thus the total perturbation available to create a fourth macroscopic gap or destroy
the two adjacent small-span conclusions is less than `0.041` of the principal-gap
scale. The same strict ordering used in Sections 104/113 survives. No limiting equality
is approached.

For a coarser independent check, the Section-113 mismatch quantity remains

\[
{\theta_8\over2}-{\pi\over3}-{73\over6}(0.0105)
=0.17650646\ldots>0.
\]

So the principal-corridor geometry stays uniformly separated.

---

## 3. The projective tangent lift remains single-valued

The directional-tooth theorem requires the relevant oriented support interval to have
angular variation strictly below `pi`. The sharp slack bookkeeping gives

\[
|S|+\tau
\le U(\theta)+{10\over3}\sigma.
\]

At the new endpoint,

\[
U_0+0.035
=1.8672365663\ldots<\pi.
\]

The gap to `pi` exceeds `1.27` radians. Hence there is no projective-lift ambiguity,
and the fixed-width tangent-window counting theorem applies exactly as in the audited
Section-117/118 proof.

---

## 4. Area transfer stays on the same exact identity

The Section-107 compact-support area formula is an exact identity without a small
`sigma` hypothesis. The only numerical inputs needed for its conservative lower bound
are the gap controls rechecked above.

With

\[
G(t)={t-\sin t\over8},
\]

the report uses

\[
A_0
={\pi\over4}
-G(\theta_0)
-2G\left(\phi_8+{10s_0\over3}\right)
-G\left({10s_0\over3}\right).
\]

All arguments are below `pi`, and direct recomputation gives

\[
A_0=0.469742134546628\ldots>0.4697.
\]

Thus the same local-rhombic-saturation transfer supplies the required finite carrier
area. No old `0.0088` decimal is embedded in this step.

---

## 5. Tooth inverse and correlated product maximization are analytic

At `s_0=0.0105`, the tooth inverse satisfies

\[
Q(s_0)=0.0784749319620981\ldots<0.0785<\pi/3.
\]

Hence the inverse remains in the monotone branch. Since

\[
F'(q)=\cos q+\sqrt3\sin q-1\le\sqrt3q,
\]

\[
Q'(y)>{1\over2\sqrt3(0.0785)}>3.677.
\]

After filling unused slack with `w`, the product upper bound is

\[
C B,
\]

with

\[
C=U_0-x-y+2z,
\]

\[
B=Q(y)+{10s_0\over3}-{7x\over3}-{7y\over3}-{10z\over3}.
\]

On the simplex,

\[
B<0.1135,
\qquad C>1.8217.
\]

Therefore

\[
\partial_x(CB)<0,
\qquad
\partial_z(CB)<0.
\]

The maximum lies on `x=z=0`. There

\[
P(y)=(U_0-y)(Q(y)+10s_0/3-7y/3).
\]

The lower derivative estimate is

\[
P'(y)>-0.1135+1.8217\left(3.677-{7\over3}\right)>2.3.
\]

Thus `P` is strictly increasing and the maximum is the endpoint `y=s_0`:

\[
CB\le0.1620888870\ldots<0.1622.
\]

This confirms the report's correlated maximization over the **whole** simplex. No
sampled interior point is being mistaken for a maximum.

---

## 6. Final contradiction has a conservative positive margin

Subtracting `lambda z/(2-sqrt(3))` from the return bracket produces coefficient

\[
10+{1\over2-\sqrt3}=13.7320508\ldots<13.733
\]

on the most expensive slack variable. The remaining coefficients are smaller.

Using outward bounds

\[
A_*>0.4697,
\quad
\lambda<0.977,
\quad
CB<0.1622,
\quad
\sigma\le0.0105,
\]

gives

\[
J-{\lambda z\over2-\sqrt3}
>
0.4697-0.977(13.733)(0.0105)-2(0.1622)
=0.0044200\ldots>0.
\]

Therefore the necessary signed-return inequality would imply

\[
\lambda z>(\lambda z),
\]

which is impossible.

The exact endpoint evaluation has still more room:

\[
J-{\lambda z\over2-\sqrt3}
\ge0.00479749\ldots
\]

under the extremal scalar allocation used in the report.

---

## 7. Regression checks

| Potential failure | Audit result |
| --- | --- |
| Reusing `0.0088` as a hidden geometric hypothesis | Pass: transfer/tangent conditions checked directly at `0.0105` |
| Coarse `delta>=0.1` branch reappears | Excluded: it costs `>0.0326>0.0105` |
| Fourth gap or adjacent-span order collapses | Excluded with `0.035` versus `phi_0>0.8729` |
| Projective tangent lift wraps | Excluded: extent `<1.8673<pi` |
| Tooth inverse changes branch | Excluded: `Q<0.0785<pi/3` |
| Correlated product has an interior maximum | Excluded by strict `x,z` derivatives and `P'(y)>2.3` |
| Decimal sensitivity | Excluded by outward-rounded residual `>0.0044` |
| Contact-isolated affine-kernel extension | Not used |
| Source deletion | Not used |
| Type-I inactive-container closure | Not claimed |

---

## 8. Exact frontier effect

The proof-only full-core excluded window is strengthened from `sigma<=0.0088` to

\[
\boxed{\sigma\le0.0105.}
\]

The exact scalar residual of the same argument vanishes only near

\[
0.01065455286\ldots,
\]

so further decimal optimization has little value. The live full-core obstruction is
now a genuinely larger-slack carrier with

\[
\sigma>0.0105,
\qquad
\operatorname{diam}(P_*)/D>0.9762830497\ldots
\]

in the associated Section-101 angular parametrization.

**Verdict:** PASS as an audited-working proof-only extension. Theorem-state authority
unchanged; C-II and Level I remain open.