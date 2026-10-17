> Generated reading edition · [exact source](../../../docs/reports/target_c_common_bridge_transfer_audit_2026-09-10.md) · source SHA-256 `1c1d6d4207590ab42d159bac71f670436f8552d43052cbe373851d8b404dc810`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-516D4ECA619E","canonical":true,"claim_ids":["C-COMMON-BLOCK"],"claim_statuses":{"C-COMMON-BLOCK":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — common-bridge transfer exclusion: dependency and sign audit

**Date:** 2026-09-10

**Repository base:** PR #190 after `target_c_common_bridge_transfer_exclusion_2026-09-10.md`

**Run type:** adversarial dependency audit

## LEVEL I STATUS

`STILL OPEN`.

This note audits the only potentially delicate dependency in the common-bridge
exclusion: the sign theorem

```math
\min_{e\ne f}K_{ef}\le0.
```

The branch-elimination report cited C56 for this fact.  The full C56 equality
classification is not needed.  The sign follows directly from the promoted C53
edge-space identities and is reproved below.  Therefore the new common-bridge theorem
does not depend on the unpromoted later C56-Z/C57-C61 equality machinery.

---

## 1. C53 data

Use exactly one C53 projective cut and common-half-plane orientation.  For positive
diameter edges `e_i`, write

```math
u_i=a_i(1,t_i),
\qquad a_i>0,
\qquad t_1<\cdots<t_m.
```

Let

```math
B=\operatorname{diag}(\beta_i),
\qquad
K=Q^T\Lambda^+Q,
\qquad
\gamma_i=a_i\beta_i,
\qquad
\Gamma=\operatorname{diag}(\gamma_i),
\qquad
G=\sum_i\gamma_i.
```

C53 proves

```math
N:=B-BKB\succeq0
```

after the positive diagonal congruence, equivalently

```math
M:=E N E=\Gamma(B^{-1}-K)\Gamma\succeq0,
```

and the affine response equations give

```math
M\mathbf1=0,
\qquad Mt=0.
\tag{1.1}
```

These are promoted inputs after the September 9 orientation audit.

---

## 2. Direct proof that the minimum off-diagonal transfer is nonpositive

Put

```math
c:=\min_{i\ne j}K_{ij}.
\tag{2.1}
```

Assume for contradiction that `c>0`.

Define the nonnegative off-diagonal similarity

```math
A_{ij}:=K_{ij}-c\ge0
\qquad(i\ne j),
\tag{2.2}
```

and let `L_A` be its `gamma`-weighted Laplacian:

```math
(L_A)_{ij}=-\gamma_i\gamma_jA_{ij}\quad(i\ne j),
\qquad L_A\mathbf1=0.
\tag{2.3}
```

Because all off-diagonal similarities are nonnegative,

```math
x^TL_Ax
=\sum_{i<j}\gamma_i\gamma_jA_{ij}(x_i-x_j)^2
\ge0.
\tag{2.4}
```

Thus `L_A` is positive semidefinite.

The off-diagonal entries of `M` are

```math
M_{ij}=-\gamma_i\gamma_jK_{ij}.
```

Subtracting the constant similarity `c` gives the exact Laplacian identity

```math
\boxed{
L_A=M-c(G\Gamma-\gamma\gamma^T).
}
\tag{2.5}
```

Center the strictly increasing slope vector in `gamma`-mean:

```math
t^0:=t-{\gamma^Tt\over G}\mathbf1.
\tag{2.6}
```

Then `gamma^Tt^0=0`, `t^0\ne0`, and (1.1), (2.5) give

```math
L_A t^0
=-cG\Gamma t^0.
\tag{2.7}
```

Take the Euclidean inner product with `t^0`:

```math
(t^0)^TL_A t^0
=-cG(t^0)^T\Gamma t^0.
\tag{2.8}
```

The left side is nonnegative by (2.4).  The factor
`G(t^0)^T\Gamma t^0` is strictly positive.  Hence

```math
-c\ge0,
```

contradicting `c>0`.  Therefore

```math
\boxed{c\le0.}
\tag{2.9}
```

No Robinson/Fiedler simplicity, C56 kernel classification, zero-transfer theorem, or
finite-integration theorem is used.

---

## 3. Electrical sign audit

The common-bridge theorem proves, in the same C53 orientation,

```math
K_{ef}\ge1/\alpha_{uv}>0
```

for every two selected diameter edges crossing the bridge cut.  The proof is invariant
under the additive constant ambiguity in `Lambda^+q_f` because `q_e^T\mathbf1=0`.

The maximum-principle signs are as follows when the bridge is `u in L`, `v in R` and
the current demand is `+1` at `r' in R`, `-1` at `l' in L`:

```math
V(v)-V(u)=1/\alpha_{uv},
```

```math
V(r)-V(v)\ge0\quad(r\in R),
```

```math
V(u)-V(l)\ge0\quad(l\in L).
```

Thus

```math
V(r)-V(l)
=[V(r)-V(v)]+[V(v)-V(u)]+[V(u)-V(l)]
\ge1/\alpha_{uv}.
```

This matches the incidence orientation `q_e=e_r-e_l` and therefore the C53 transfer
entry `K_{ef}` with no sign reversal.

---

## 4. Orientation audit

The September 5 C53 regression arose from changing the projective cut without changing
the edge orientations consistently.  The common-bridge proof avoids that failure.

C20 gives two complementary loaded cyclic intervals.  Choosing points in the two
transition boundary edges produces a separating chord line of the convex force hull.
Its normal `ell` satisfies

```math
ell(p_r-p_l)>0
\qquad(l\in B_L,r\in B_R).
```

Therefore every cut-oriented diameter vector `p_r-p_l` lies in the same open
half-plane.  One may choose the C53 projective cut corresponding to that half-plane;
then the projective orientation, the electrical current orientation, the columns of
`Q`, and the transfer signs above are all the same orientation.

---

## 5. Audit conclusion

The common-bridge contradiction uses only:

1. C20/C22 complementary loaded boundary intervals for a positive contact bridge;
2. C24: a bridge in `I_*` is crossed by every selected diameter pair;
3. elementary convex separation of two complementary vertex intervals;
4. elementary resistor-network cut conservation and maximum principle;
5. promoted C53 affine/PSD edge-space identities, from which (2.9) is proved directly;
6. at least two selected diameter edges, supplied in the sufficiently large post-ZF
   regime.

The conclusion

```math
I_*\text{ is one bridge block}
```

therefore survives the dependency audit without reopening any unpromoted C-I equality
chain.
