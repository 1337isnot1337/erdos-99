> Generated reading edition · [exact source](../../../docs/reports/target_c_post_pi_currency_coupling_2026-09-09.md) · source SHA-256 `98681181e71d770a92c0e4ed75301987bc4ae2fc3c983fc40fbf4bd3143329b5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DAF0D0123991","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — post-PI currency coupling excludes low pinned surplus

**Date:** 2026-09-09  
**Run type:** exact/asymptotic synthesis; cavity-capacity exclusion  
**Target:** Target C C-II after ZF/DB/PI  
**Depends on:** PI projective-circle force-hull area floor, GU attachment-cell bound and charging inequality, HB loaded-contact coupling, PC/OP convex outer-pocket decomposition, DB `q/D>=2rho`  
**Computation:** only evaluation of the final algebraic constant; not used in the proof

## LEVEL I STATUS

`STILL OPEN`

GU previously gave a dichotomy: if the pinned/contact currency

$$
L:=e_{BB}+2s_C
$$

is small compared with `D`, then the attachment-cell gap

$$
G:=area(F)-\sum_r area(conv A_r)
$$

is quadratic, but that gap could escape into the outer contact region or into bounded exceptional faces.

PI, HB, PC, and OP allow both escape regions to be bounded in terms of the **same** currency `L`. The resulting lower and upper bounds are incompatible below an absolute threshold.

The conclusion is the unconditional post-ZF lower bound

$$
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_0
=0.4198649147034757\ldots .
}
\tag{CC.1}
$$

Thus the entire branch `e_BB+2s_C=o(D)` and, more generally, every branch below `0.4198649D`, is excluded. No cavity or rattler alternative remains below that threshold.

---

## 1. PI gives the attachment-gap lower bound

Let

$$
A_{PI}:=\frac12\sin(2\rho)
=0.497856636324211\ldots,
\qquad
\rho=\cos\rho=0.7390851332151607\ldots .
\tag{CC.2}
$$

PI proves

$$
\liminf\frac{area(F)}{D^2}\ge A_{PI}.
$$

The GU component-diameter argument is unchanged, except that its old force-hull area constant is replaced by `A_PI`. Along any subsequence on which

$$
\frac{L}{D}	o\lambda
$$

(after passing to a further subsequence if needed), GU gives

$$
\boxed{
\liminf\frac G{D^2}
\ge
A_{PI}-\frac\pi4\lambda^2.
}
\tag{CC.3}
$$

The right side is positive throughout the range relevant below.

---

## 2. Exact excess-perimeter variable for the outer pockets

Let

- `a` be the number of missing force-hull sides, equivalently the number of OP convex outer pockets;
- `L_P` be the Euclidean perimeter of pocket `P`;
- `x_B=b-q` be the outer-walk excess;
- `P_F=per(F)`.

OP gives

$$
\sum_P L_P
=x_B+P_F-q+2a.
\tag{CC.4}
$$

Every pocket is a strict convex polygon. Its contact-boundary edges have length one and its added hull side joins two source points, so every side has length at least one. Therefore

$$
L_P\ge3.
\tag{CC.5}
$$

Define the total pocket-perimeter excess above this unavoidable triangular baseline:

$$
\boxed{
E_{out}:=\sum_P(L_P-3).
}
\tag{CC.6}
$$

Using CC.4,

$$
\boxed{
E_{out}=x_B+P_F-q-a.
}
\tag{CC.7}
$$

This is a useful exact scalar: unlike total pocket perimeter, its square can be used without paying the `Theta(D)` baseline pocket count at quadratic order.

---

## 3. HB and DB bound the outer-pocket perimeter excess

PC/HB gives

$$
a+e_{BB}\ge q,
\qquad	ext{so}\qquad
 a\ge q-e_{BB}.
\tag{CC.8}
$$

ZT gives `x_B<=q`, while the convex perimeter bound gives

$$
P_F\le\pi D.
$$

Insert these in CC.7:

$$
\begin{aligned}
E_{out}
&\le q+\pi D-q-(q-e_{BB})\\
&=\pi D-q+e_{BB}.
\end{aligned}
\tag{CC.9}
$$

DB gives

$$
\liminf q/D\ge\liminf h/D\ge2\rho.
\tag{CC.10}
$$

Write, along the chosen subsequence,

$$
\frac{e_{BB}}D\to t
$$

after a further extraction. Since `e_BB<=L`,

$$
0\le t\le\lambda.
\tag{CC.11}
$$

From CC.9-CC.11,

$$
\boxed{
\limsup\frac{E_{out}}D
\le c_0+t,
\qquad
c_0:=\pi-2\rho
=1.663422387159472\ldots .
}
\tag{CC.12}
$$

---

## 4. Outer-pocket area is controlled by excess perimeter, not total perimeter

For each pocket write

$$
L_P=3+u_P,
\qquad u_P\ge0.
$$

Then

$$
\sum_Pu_P=E_{out}.
$$

By the planar isoperimetric inequality for each convex pocket,

$$
area(P)\le\frac{L_P^2}{4\pi}.
$$

Since

$$
\sum_Pu_P^2\le\left(\sum_Pu_P\right)^2=E_{out}^2,
$$

we obtain

$$
\begin{aligned}
H_{out}:=\sum_Parea(P)
&\le
\frac1{4\pi}\sum_P(3+u_P)^2\\
&\le
\frac{E_{out}^2+6E_{out}+9a}{4\pi}.
\end{aligned}
\tag{CC.13}
$$

Here `a=O(D)` and `E_out=O(D)`, so the linear terms disappear after division by `D^2`. Therefore CC.12 gives

$$
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
\frac{(c_0+t)^2}{4\pi}.
}
\tag{CC.14}
$$

This is much sharper than squaring the total pocket perimeter, because the mandatory perimeter `3a=Theta(D)` does not create artificial quadratic area capacity.

---

## 5. HB also controls all bounded exceptional-face area

For every bounded nonquadrilateral face `F_i`, put

$$
r_i:=\deg F_i-4\ge1.
$$

Then

$$
Q=\sum_i r_i.
\tag{CC.15}
$$

Its perimeter is the integer

$$
k_i=r_i+4.
$$

C51 makes each bounded face convex, hence

$$
area(F_i)\le\frac{k_i^2}{4\pi}.
$$

Now

$$
\begin{aligned}
\sum_i k_i^2
&=\sum_i(r_i+4)^2\\
&=\sum_i r_i^2+8Q+16f\\
&\le Q^2+24Q,
\end{aligned}
\tag{CC.16}
$$

because `sum r_i^2<=Q^2` and `f<=Q`.

Thus the total exceptional-face area satisfies

$$
\boxed{
A_{exc}
\le
\frac{Q^2+24Q}{4\pi}.
}
\tag{CC.17}
$$

HB proves the stronger exact contact coupling

$$
e_{BB}\ge Q+2d_H+2s_Z,
$$

so in particular

$$
Q\le e_{BB}.
\tag{CC.18}
$$

Combining CC.17-CC.18 gives

$$
\boxed{
\limsup\frac{A_{exc}}{D^2}
\le
\frac{t^2}{4\pi}.
}
\tag{CC.19}
$$

This improves GU's earlier `5pi D` exceptional-perimeter localization by using the post-HB fact that exceptional-face degree itself must be paid by actual loaded-loaded contacts.

---

## 6. Upper-bound the full GU gap

ZG/GU gives the geometric charging inequality

$$
G\le H_{out}+A_{exc}+2q.
\tag{CC.20}
$$

Since `q=O(D)`, the final term is negligible on the `D^2` scale. Using CC.14 and CC.19,

$$
\boxed{
\limsup\frac G{D^2}
\le
\frac{(c_0+t)^2+t^2}{4\pi}.
}
\tag{CC.21}
$$

Together with the PI/GU lower bound CC.3, every post-ZF subsequential limit `(lambda,t)` must satisfy

$$
\boxed{
A_{PI}-\frac\pi4\lambda^2
\le
\frac{(c_0+t)^2+t^2}{4\pi},
\qquad
0\le t\le\lambda.
}
\tag{CC.22}
$$

This two-parameter inequality is the strongest form of the new currency coupling. It is strictly stronger when a substantial part of `L` comes from pinned stress `s_C` rather than direct loaded-loaded contacts.

---

## 7. Eliminate `t` and obtain a universal positive threshold

For fixed `lambda>=0`, the right side of CC.22 is increasing in `t`. Hence its largest possible value under `t<=lambda` is obtained at `t=lambda`. Therefore every survivor must satisfy

$$
A_{PI}-\frac\pi4\lambda^2
\le
\frac{(c_0+\lambda)^2+\lambda^2}{4\pi}.
\tag{CC.23}
$$

The left side decreases in `lambda` and the right side increases. Equality has one positive root

$$
\boxed{
\lambda_0
=0.4198649147034757\ldots .
}
\tag{CC.24}
$$

Equivalently, `lambda_0` is the positive root of

$$
(\pi^2+2)\lambda^2
+2c_0\lambda
+c_0^2-4\pi A_{PI}=0.
\tag{CC.25}
$$

Explicitly,

$$
\lambda_0
=
\frac{
-c_0+
\sqrt{c_0^2-(\pi^2+2)(c_0^2-4\pi A_{PI})}
}{\pi^2+2}.
\tag{CC.26}
$$

For every `lambda<lambda_0`, CC.23 is violated. Hence no unbounded post-ZF subsequence can have `(e_BB+2s_C)/D` tending below `lambda_0`.

This proves CC.1:

$$
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.4198649147034757\ldots .
}
$$

---

## 8. What this changes

Before CC, the small-`L` branch was reduced only to macroscopic cavity/shell geometry. CC closes that escape quantitatively.

Every sufficiently large post-ZF survivor must now carry **both** independent linear currencies:

$$
\boxed{
\frac{x_B+Q+2s_Z}{D}
\ge0.6099043189\ldots-o(1)
}
\tag{CC.27}
$$

from NB, and

$$
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge0.4198649147\ldots-o(1)
}
\tag{CC.28}
$$

from CC.

The first is total diameter branching/contact-topology defect; the second is loaded-contact/pinned-stress surplus. The previous GU request for a currency-coupling theorem is therefore partially fulfilled: neither currency may vanish or even fall below the displayed positive linear constants.

---

## 9. Regression audit

### Regular odd shell

The regular shell has both currencies linear, so it survives CC as it should. CC uses global post-ZF inputs but does not claim local shell geometry alone is impossible.

### Many tiny pockets

Their unavoidable perimeter `3a` contributes only `O(D)` to CC.13. They cannot fake `Theta(D^2)` area capacity merely by being numerous.

### One giant pocket

Allowed. Its perimeter excess is charged to `E_out`, and CC.14 permits it only within the global `pi D-q+e_BB` excess budget.

### One giant exceptional face

Allowed in principle. CC.17 shows that its quadratic area is paid by `Q^2`, and HB then transfers that cost to `e_BB`.

### Pinned-stress-dominated surplus

If `s_C` is large but `e_BB` is small, the stronger two-parameter inequality CC.22 applies. Replacing `t` by `lambda` is only the final worst-case relaxation.

---

## 10. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| exact pocket excess CC.7 | proved | OP perimeter identities |
| outer area bound CC.14 | proved | convex isoperimetry + baseline subtraction |
| exceptional area bound CC.19 | proved | degree decomposition + HB `Q<=e_BB` |
| two-parameter gap coupling CC.22 | proved | PI/GU lower + ZG charging upper |
| universal threshold `0.4198649...` | proved | one-variable monotone elimination |
| all macroscopic cavity branches excluded | only below threshold | high-surplus branch remains |
| Level I | still open | must now exploit coexistence of the two mandatory linear currencies |

---

## 11. Next target

The surviving post-ZF source satisfies simultaneously

$$
x_B+Q+2s_Z\ge(0.6099043-o(1))D
$$

and

$$
e_{BB}+2s_C\ge(0.4198649-o(1))D.
$$

The next closing attempt should use the exact boundary incidence identities to show that these two linear currencies cannot coexist at their required scales without forcing either

1. a large pure-rhombic/near-shell region covered by Target B stability, or
2. an area/perimeter loss incompatible with global minimum-diameter packing.
