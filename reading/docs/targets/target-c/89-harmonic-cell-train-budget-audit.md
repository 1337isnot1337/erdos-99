> Generated reading edition · [exact source](../../../../docs/targets/target-c/89-harmonic-cell-train-budget-audit.md) · source SHA-256 `93277145cc54828a36ca6fe5b0b66da48207b7f712bad2786e9b8556b6ea5c47`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — exact harmonic-cell train-budget sharpening

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 82 proves that every unloaded harmonic component is a boundary-order perturbation of a strict-rhombus quadrangulation. Its published local boundary estimate

$$
P_R\le 20a
$$

is deliberately coarse. The exact Section-82 face ledger retains enough information to improve that coefficient and, after summing the exact transverse train spans, to couple local rhombic area directly to the diameter and attachment count of the same harmonic cell.

No new compactness, packing theorem, KKT weight floor, or global-minimality assumption is used. The result is finite.

---

# 89. Exact local train budget and area–diameter inequality

Fix one unloaded positive-contact component `I_r` and retain the canonical Section-82 notation:

- `n=|I_r|`;
- `A=A_r subset B`, `a=|A|`, and `P=conv(A)`;
- `d=diam(P)`;
- `s=e+t-2n-1>=0`;
- `c` = number of loaded-loaded contacts with both endpoints in `A`;
- `c_partial` = number of those contacts that are sides of `P`;
- `L` = outer-face walk length of the induced contact graph `H` on `I_r union A`;
- `Q=sum_f(deg f-4)` over bounded faces;
- `mathcal R` = the full set of bounded strict-rhombus faces of `H`;
- `F_4=|mathcal R|`;
- `A_4=sum_{R in mathcal R} area(R)`;
- `P_R` = total physical boundary-edge occurrence count of the rhombus complex `mathcal R`, including every connected component and every hole boundary.

Canonical Section 82 gives the exact identity

$$
\boxed{L+Q=4a-6-2s-2c,}
\tag{89.1}
$$

and, from `L>=2a-c_partial`,

$$
\boxed{Q\le 2a-6-2s-2c+c_{partial}.}
\tag{89.2}
$$

Every nonquadrilateral bounded face has degree at least five, so if `f_exc` is their number,

$$
f_{exc}\le Q,
\qquad
\sum_{f\,nonquad}\deg f=4f_{exc}+Q\le5Q.
\tag{89.3}
$$

The same boundary classification used in Section 82 therefore gives

$$
P_R\le L+5Q.
\tag{89.4}
$$

## 89.1 Sharpen the local physical-boundary bound

Insert (89.1) into (89.4):

$$
P_R
\le (L+Q)+4Q
=4a-6-2s-2c+4Q.
$$

Now use (89.2). This yields the exact finite sharpening

$$
\boxed{
P_R
\le
12a-30-10s-10c+4c_{partial}.
}
\tag{89.5}
$$

Since `c_partial<=c`,

$$
\boxed{
P_R
\le
12a-30-10s-6c.
}
\tag{89.6}
$$

In particular the coefficient `20` in the coarse Section-82 estimate can be replaced by `12`, with explicit favorable corrections for pinned surplus and loaded-loaded attachment contacts.

This is not an asymptotic optimization: (89.5) is a direct finite consequence of the exact local face identity.

## 89.2 Exact local train count

Apply the canonical train decomposition separately to every edge-connected component of `mathcal R`. Every local train has exactly two physical boundary ends, including trains ending on hole boundaries. Summing over connected components gives

$$
\boxed{2T_R=P_R,}
\tag{89.7}
$$

where `T_R` is the total number of local train segments in the full harmonic-cell rhombus complex.

Combining (89.5) and (89.7),

$$
\boxed{
T_R
\le
6a-15-5s-5c+2c_{partial},
}
\tag{89.8}
$$

and hence

$$
\boxed{
T_R
\le
6a-15-5s-3c.
}
\tag{89.9}
$$

Thus every finite harmonic component has only `O(a)` local pseudolines, with an explicit constant six rather than the ten supplied by the coarse Section-82 boundary estimate.

## 89.3 Sum the exact transverse train spans inside the same cell

For each local train `tau`, orient its transverse coordinate as in the canonical train theorem. Let

$$
L_\tau:=\sum_{R\in\tau}\sin\theta_R,
\tag{89.10}
$$

where `theta_R in (pi/3,2pi/3)` is the unit-rhombus side angle in the chosen orientation. Crossing one rhombus advances the transverse coordinate of opposite-edge midpoints by exactly `sin theta_R`. Therefore `L_tau` is exactly the transverse distance between the two terminal edge midpoints of the train.

Both terminal edge midpoints belong to the convex cell `P`: every rhombus lies in `P` and every side midpoint of such a rhombus lies in `P`. Hence

$$
\boxed{L_\tau\le w_P(\nu_\tau)\le d,}
\tag{89.11}
$$

where `nu_tau` is the transverse unit normal and `w_P` is the directional width of `P`.

Each strict rhombus belongs to exactly two local trains, and its Euclidean area is `sin theta_R`. Consequently

$$
\sum_\tau L_\tau
=2\sum_{R\in\mathcal R}\sin\theta_R
=2A_4.
\tag{89.12}
$$

Sum (89.11) over all `T_R` trains:

$$
\boxed{2A_4\le T_R d.}
\tag{89.13}
$$

Combining with (89.8) gives the exact area–diameter–attachment inequality

$$
\boxed{
2A_4
\le
d\bigl(6a-15-5s-5c+2c_{partial}\bigr).
}
\tag{89.14}
$$

Using `c_partial<=c`,

$$
\boxed{
2A_4
\le
d\bigl(6a-15-5s-3c\bigr).
}
\tag{89.15}
$$

In particular,

$$
\boxed{A_4<3ad.}
\tag{89.16}
$$

Equivalently, whenever `A_4>0`,

$$
\boxed{
a>{A_4\over3d}.}
\tag{89.17}
$$

The useful content of (89.14) is the explicit simultaneous dependence on attachment count, local pinned surplus, loaded-loaded contacts, and the actual diameter of the same harmonic cell. It does not spend the ambient source diameter `D`.

## 89.4 Consequence for the canonical Type-II carrier

Now work in the canonical full-core near-disk Type-II branch and take the macroscopic locally rhombus-saturated cell supplied by `C-HARMONIC-WRAPPING`. Write its parameters as

$$
a_*,\quad d_*,\quad A_{4,*},\quad T_*,\quad s_*,\quad c_*,\quad c^\partial_*.
$$

Canonical Section 88 gives

$$
d_*\ge(\mu_0-o(1))D,
\qquad
\mu_0=0.889670810115\ldots,
\tag{89.18}
$$

and

$$
A_{4,*}=area(P_*)-o(D^2)=\Omega(D^2).
\tag{89.19}
$$

The finite inequalities above therefore hold on the exact same macroscopic carrier used by the localized complete-grid theorem:

$$
T_*
\le
6a_*-15-5s_*-5c_*+2c^\partial_*,
\tag{89.20}
$$

$$
2A_{4,*}\le T_*d_*.
\tag{89.21}
$$

Hence

$$
\boxed{
a_*=\Omega(D),\qquad T_*=\Omega(D),}
\tag{89.22}
$$

with the quantitative lower bounds

$$
T_*\ge {2A_{4,*}\over d_*},
\qquad
6a_*-15-5s_*-3c_*\ge {2A_{4,*}\over d_*}.
\tag{89.23}
$$

The first conclusion `a_*=Omega(D)` was already known from harmonic trapping. The new information is the exact finite train budget (89.20) and its simultaneous area constraint (89.21), which tie all local train pseudolines to the same attachment currency used by the harmonic response problem.

## 89.5 What this does and does not solve

Section 89 removes one avoidable constant loss from the Type-II local carrier. The next train-grid theorem may use

```text
local area A_4 = Theta(D^2)
+ local diameter d >= (0.8896708101-o(1))D
+ total local train count T <= 6a+O(1)
+ exact span budget 2A_4 <= Td
+ global/local angular-defect budget O(D)
```

instead of the previous `T<=10a+O(1)` consequence of `P_R<=20a`.

This still does **not** imply that one Fox--Pach complete grid covers a fixed fraction of the rhombi, nor that the train crossing graph is complete multipartite, Ferrers, or interval-convex. It also does not turn any physical contact into a positive KKT weight. C-II remains open.

## 89.6 Dependency audit

- **Canonical `C-HARMONIC-CARRIER-QUAD` / Section 82:** exact local face identity (89.1), outer-walk lower bound, strict-rhombus classification, and boundary classification (89.4).
- **Canonical train theorem / shared Theory 03:** a train is a chain of opposite-edge rhombi with two physical boundary ends and exact transverse advance `sin theta_R` per rhombus. The local proof of (89.11)--(89.13) uses only this elementary train geometry inside the convex cell `P`.
- **Canonical `C-HARMONIC-WRAPPING` / Section 88:** used only for the Type-II carrier consequence (89.18)--(89.23).
- **No use of canonical Sections 84 or 85.**

**Status:** canonical as `C-HARMONIC-TRAIN-BUDGET`; see `docs/state/theorem-state.yaml` for lifecycle authority. C-II remains open.
