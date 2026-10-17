> Generated reading edition · [exact source](../../../docs/reports/target_c_oler_gluing_train_surplus_identity_2026-09-14.md) · source SHA-256 `4eeafb7437ae82e9ffb7077a358c49645b52166c8228e9af05bc2079a27c3b31`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-EB8397EC4742","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact Oler gluing and the unavoidable train-surplus correction

**Date:** 2026-09-14
**Repository base:** `046784db`
**State version:** `2026-09-14.audit.51`
**Run type:** closing-proof reduction / exact Oler-gluing identity
**Target:** Target C-II, canonical full-core Type-II branch
**Claim class:** proof-only consequence awaiting independent audit
**External literature:** no new import
**Computation:** exact-rational regression only

## LEVEL I STATUS

`STILL OPEN`

The latest chamber bootstrap suggests cancelling inactive-chamber internal boundaries
against the positive-contact core. There is an exact finite identity governing that
operation. It shows that naive Oler gluing cannot compare the chamber slack directly
to the global Oler slack: the stopped-train surplus reappears as a mandatory positive
correction.

The identity also gives a stronger unconditional chamber-slack floor than the current
`2.1586 D` bootstrap.

Use

$$
a_0={\sqrt3\over2},\qquad c_0={a_0\over2}={\sqrt3\over4}.
$$

Let `K=conv(A)` be the full source hull and `F` the force hull. Retain the canonical
Section-77 notation:

- `N_F=|A\cap F|`, `Z_ext=n-N_F`;
- `R_4` strict rhombus faces and
  $A_4=a_0R_4+E_4$;
- `f,Q,q,k` the exceptional-face, loaded-hull, and mixed-defect currencies;
- `a` the number of convex outer pockets inside `F`;
- `T=q-k+2f` the complete stopped-train count;
- `A_ch,Z_ch,P_ch,s_ch=f+a` the total inactive-chamber area, isolate population,
  perimeter, and chamber count.

Define the force-hull Oler slack

$$
\Sigma_F:={\operatorname{area}(F)\over a_0}
+{P_F\over2}+1-N_F\ge0
\tag{G.1}
$$

and the canonical chamber slack

$$
\Sigma_{ch}:={A_{ch}\over a_0}+{P_{ch}\over2}+s_{ch}-Z_{ch}\ge0.
\tag{G.2}
$$

For the exterior caps of Section 77.2, let `A_i,P_i,z_i` have the same meaning there
and define their individual Oler slacks

$$
\sigma_i^{ext}:={A_i\over a_0}+{P_i\over2}-1-z_i\ge0,
\qquad
\Sigma_{ext}:=\sum_i\sigma_i^{ext}.
\tag{G.3}
$$

Finally define the full-source Oler slack

$$
\Sigma_K:={\operatorname{area}(K)\over a_0}
+{P_K\over2}+1-n,
\tag{G.4}
$$

and the punctured-packing slack

$$
\boxed{
\Omega_K:=\Sigma_K-{E_4\over a_0}\ge0.
}
\tag{G.5}
$$

The nonnegativity in (G.5) is exactly canonical Section 68.9 after dividing by `a_0`.

## 0. Provenance of the gluing ledger

A September 11 full-source cell-slack audit already records the dimensional
face/cap identity obtained after augmenting the force hull, and the September 12
chamber-residual theorem isolates the force-hull residual `R_F`. The formulas below
are a normalized, punctured specialization of that ledger to the Section-77 inactive
chambers and exterior caps. Their useful new role here is to expose exactly how the
current stopped-train surplus enters and then cancels against the mandatory chamber
boundary baseline. They should not be read as claiming first discovery of global
face/cap Oler additivity.

## 1. Exterior caps glue to the force hull exactly

Section 77.2 gives

$$
\sum_iA_i=\operatorname{area}(K)-\operatorname{area}(F),
$$

$$
\sum_iP_i=P_K+P_F-2P_{com},
$$

where `P_com` is the total length of force-hull sides already lying on `partial K`,
and the `r` nondegenerate caps contain exactly the `Z_ext` exterior source points.
Therefore

$$
\begin{aligned}
\Sigma_{ext}
&={\operatorname{area}(K)-\operatorname{area}(F)\over a_0}
 +{P_K+P_F\over2}-P_{com}-r-Z_{ext}.
\end{aligned}
\tag{G.6}
$$

Adding (G.1), using `n=N_F+Z_ext`, gives the finite identity

$$
\boxed{
\Sigma_F+\Sigma_{ext}
=\Sigma_K+P_F-P_{com}-r.
}
\tag{G.7}
$$

Every noncommon force-hull side is the closing chord of one nondegenerate exterior
cap. Its endpoints are distinct source points, so its length is at least one. Hence

$$
\boxed{
L_{cap}:=P_F-P_{com}-r\ge0.
}
\tag{G.8}
$$

## 2. Chamber slack differs from force-hull slack by an exact train term

The chamber tiling gives

$$
\operatorname{area}(F)=A_4+A_{ch},
\qquad
N_F=m+Z_{ch},
\tag{G.9}
$$

and canonical Section 77 gives

$$
m=R_4+f+q-k+1.
\tag{G.10}
$$

The exact chamber-perimeter decomposition is

$$
P_{ch}=(4f+Q)+(b+P_F-2q+2a).
\tag{G.11}
$$

Using the outer-walk identity

$$
b+Q=2(q-k),
\tag{G.12}
$$

we obtain

$$
\boxed{
P_{ch}-P_F=4f-2k+2a.
}
\tag{G.13}
$$

Subtract (G.1) from (G.2), then use (G.9)--(G.13) and
`A_4/a_0=R_4+E_4/a_0`:

$$
\begin{aligned}
\Sigma_{ch}-\Sigma_F
&=-{A_4\over a_0}+{P_{ch}-P_F\over2}+s_{ch}-1+m\\
&=q+4f-2k+2a-{E_4\over a_0}.
\end{aligned}
\tag{G.14}
$$

Since `T=q-k+2f`,

$$
q+4f-2k=2T-q=2\left(T-{q\over2}\right).
$$

Thus

$$
\boxed{
\Sigma_{ch}
=\Sigma_F
+2\left(T-{q\over2}\right)
+2a-{E_4\over a_0}.
}
\tag{G.15}
$$

No inequality has been used.

## 3. Exact all-region gluing identity

Add (G.7) to (G.15) and use (G.5):

$$
\boxed{
\Sigma_{ch}+\Sigma_{ext}
=\Omega_K
+2\left(T-{q\over2}\right)
+2a+L_{cap}.
}
\tag{G.16}
$$

Every term on the right is nonnegative. In particular,

$$
\boxed{
\Sigma_{ch}+\Sigma_{ext}
\ge2\left(T-{q\over2}\right).
}
\tag{G.17}
$$

This is the exact correction to the proposed additive Oler-gluing route. Internal
boundary cancellation does not leave only the global source slack. It necessarily
leaves twice the complete stopped-train surplus, together with outer-pocket and
exterior-cap chord corrections.

## 4. AG42 gives a `3.81009 D` combined local-slack floor

The audited-working AG42 theorem gives in Type II

$$
{T-q/2\over D}
\ge C_*-o(1),
\qquad
C_*:=2\sqrt{\Delta_2}+0.00042,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\tag{G.18}
$$

Therefore (G.17) yields

$$
\boxed{
\liminf {\Sigma_{ch}+\Sigma_{ext}\over D}
\ge2C_*
=4\sqrt{\Delta_2}+0.00084
=3.810091227455829\ldots .
}
\tag{G.19}
$$

This is not a contradiction: the local cap/chamber slacks are allowed to contain this
mandatory topological train correction.

## 5. Stronger chamber-only floor

Equation (G.15), `Sigma_F>=0`, and `a>=0` give

$$
\Sigma_{ch}
\ge2\left(T-{q\over2}\right)-{E_4\over a_0}.
\tag{G.20}
$$

Canonical Section 68 gives

$$
E_4<c_0P_K={a_0\over2}P_K,
$$

while Cauchy's perimeter-diameter inequality gives `P_K<=pi D`. Hence

$$
\boxed{
\Sigma_{ch}
>2\left(T-{q\over2}\right)-{\pi\over2}D.
}
\tag{G.21}
$$

Combining with AG42,

$$
\boxed{
\liminf {\Sigma_{ch}\over D}
\ge
4\sqrt{\Delta_2}+0.00084-{\pi\over2}
=2.239294900660933\ldots .
}
\tag{G.22}
$$

This improves the current bootstrap floor

$$
\Sigma_{ch}/D\ge2.158634412942893\ldots-o(1)
$$

by about `0.08066049`.

The proof of (G.22) does not use the §171 `q-k` bootstrap. It uses only the AG42
all-train floor, canonical chamber/cap bookkeeping, punctured packing, and convex
perimeter-diameter.

## 6. Frontier correction

The latest chamber report proposes an additive Oler-gluing inequality that cancels
internal chamber boundaries and leaves only the outer source-hull boundary. Equation
(G.16) shows the exact obstruction to that formulation.

Any valid gluing theorem must retain or separately cancel

$$
2(T-q/2)+2a+L_{cap}.
$$

The first term alone is at least `3.81009D-o(D)` in Type II. Therefore an upper bound
of the schematic form

```text
Sigma_ch <= global Oler slack + o(D)
```

cannot hold for the actual Section-77 chamber slack.

The revised closing target is one of the following:

1. prove a **signed** gluing inequality whose left side subtracts the mandatory
   `2(T-q/2)` topological correction before comparison with the global punctured slack;
2. convert the train correction itself into a strict source-level diameter decrease;
3. show that the exterior-cap/chamber decomposition forces an additional negative
   boundary-order term not present in (G.16); or
4. use the linearly many exceptional faces from the §171 bootstrap to force geometric
   width/area cost that cannot hide inside the exact correction.

Thus the gluing route remains live, but its correct invariant is

$$
\boxed{
\Sigma_{ch}+\Sigma_{ext}
-2(T-q/2)-2a-L_{cap}
=\Omega_K\ge0,
}
\tag{G.23}
$$

not `Sigma_ch` by itself.

## 7. Scope audit

- All source points are retained.
- `Sigma_ext` uses the exact Section-77 exterior-cap assignment; no cap point is
  deleted or duplicated.
- The cap chord credit `L_cap>=0` uses only unit separation of the two source endpoints
  of each noncommon force-hull side.
- `Omega_K>=0` is exactly the canonical Section-68 punctured-packing inequality.
- Occurrence multiplicity in `b,Q,f,T` is unchanged.
- The result is finite through (G.17) and asymptotic only when AG42 is inserted.
- No theorem-state authority is changed by this note.

**Disposition:** proof-only exact identity and frontier correction. C-II remains open.

---

**Recovery provenance:** copied from `research/c2-gluing-sol-20260914-r10` at exact tip `58950d925eaec5d281cddc0202a4ef3df4c1b0fd` during the 2026-10-04 Slot 2 branch audit. This recovered claim remains unreviewed and noncanonical.
