<!-- theorem-state: {"artifact_id":"ART-4A455CFD8206","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — hostile audit of the sparse/directional full-core closure

**Date:** 2026-09-12  
**Audited artifact:** docs/reports/target_c_sparse_split_fullcore_closure_2026-09-12.md  
**Input module:** research/target_c_sparse_directional_signed_return_split.md  
**State version:** 2026-09-12.audit.44  
**Classification:** audited-working conditional result; theorem state unchanged

## Audit conclusion

The sparse/directional split is mathematically sound at its stated scope. It proves
the all-slack contradiction

\[
\lambda z\ge(2-\sqrt3)[J]_+
\quad\Longrightarrow\quad
\lambda z>\lambda z
\]

throughout the proof-only Section-118 window \(\sigma\le0.0088\), provided the
hostile-audited Section-117/118 signed-return theorem and its carrier hypotheses are
accepted. The strict rounded margin is greater than \(0.057\).

This is not a canonical theorem promotion and does not close C-II: the inactive
container branch is untouched, and the signed-return/sparse split remains a
proof-only dependency.

## 1. Area split

For a complete train \(\tau\), the rhombi met by \(\tau\) occur in transverse order.
The area of each unit rhombus is the transverse increment between its two parallel
train-edge lines. Telescoping therefore gives

\[
\sum_{R\ni\tau}\operatorname{area}(R)
\le\operatorname{width}_{\perp\tau}(P)
\le\operatorname{diam}(P)=d.
\]

Removing \(N_s\) sparse bad trains removes the union of their incident rhombi, so it
costs at most \(dN_s\), even when two sparse trains meet the same rhombus. In the
remaining rhombi, near-\(\pi/3\) crossings with a directional bad train are bounded
by \(2TM_d(\epsilon)\), and crossings with angular excess greater than \(\epsilon\)
are bounded by \(\Delta/\epsilon\). Every rhombus has area at most one. Hence

\[
A_{gg}\ge A_4-dN_s-2TM_d(\epsilon)-\Delta/\epsilon.
\]

This is a train union bound, not an endpoint multiplicity assertion. The later
signed-return step separately uses injective physical boundary occurrences. The audit
finds no reuse of a boundary occurrence.

## 2. Endpoint ledger

Classify a bad train through a selected non-tooth endpoint whenever one exists, and
leave only regular two-edge tooth trains in the directional class. The audited
Section-118 categories then give

\[
\frac{N_s}{D}
\le 5q+(z+C_{\rm tail})+(3z+6c)+\frac{20}{3}w+o(1).
\]

Since \(q+c\le z\), one has \(5q+6c\le6z\). With
\(C_{\rm tail}\le x/2+5w/3\),

\[
\boxed{\frac{N_s}{D}
\le10z+\frac{x}{2}+\frac{25}{3}w+o(1).}
\]

This is a total sparse-train count, not a directional supremum. The directional class
is only the regular tooth family, for which the audited tangent-window and bathtub
calculation gives

\[
\lim_{\epsilon\downarrow0}\limsup_D\frac{M_d(\epsilon)}D
\le Q_{\rm tooth}(y)+y+x+\frac{10}{3}w.
\]

Thus no \(z\) term is hidden inside the directional factor.

## 3. Return inequality and correlated maximization

With \(d/D\to\lambda\), \(T/D\le U-x-y+2z+o(1)\), and available principal-route
excess \(E/D\le z+o(1)\), the three-host signed-return theorem gives

\[
\lambda z\ge(2-\sqrt3)\left[
A_*(x,w)
\mathord{-}\lambda\left(10z+\frac{x}{2}+\frac{25w}{3}\right)
\mathord{-}2\left(U-x-y+2z\right)
\left(Q_{\rm tooth}(y)+y+x+\frac{10w}{3}\right)
\right]_+.
\]

The signs have the expected meaning: sparse trains remove area through
\(\lambda N_s/D\), directional trains through \(2(T/D)M_d\), and route excess is
on the left.

Put \(s_0=0.0088\), \(C=U_*-x-y+2z\), and
\(B=Q_{\rm tooth}(y)+y+x+10w/3\). After replacing
\(w\) by \(s_0-x-y-z\), the exact expression is

\[
B=Q_{\rm tooth}(y)+\frac{10s_0}{3}
\mathord{-}\frac{7x}{3}-\frac{7y}{3}-\frac{10z}{3}.
\]

The outward endpoint estimate \(Q_{\rm tooth}(s_0)<0.072\) gives \(B<0.1102\)
and \(C>1.8223\). Therefore
\(\partial_x(CB)=-B-7C/3<0\) and
\(\partial_z(CB)=2B-10C/3<0\). The maximum is at \(x=z=0\).

For \(P(y)=(U_*-y)(Q_{\rm tooth}(y)+10s_0/3-7y/3)\), implicit differentiation gives
\(Q_{\rm tooth}'(y)=1/(2F'(Q_{\rm tooth}(y)))>4.009\) on the interval. Hence
\(P'(y)>0\), so

\[
CB\le(1.8312-s_0)(0.072+s_0)<0.1473.
\]

This is the load-bearing correlated step. It follows from derivative signs on the
whole slack simplex, not from a sampled numerical search.

Finally, subtracting \(\lambda z/(2-\sqrt3)\) from the bracket and using
\(\lambda\le0.9763\), \(10+1/(2-\sqrt3)>25/3>1/2\), and
\(x+y+z+w\le s_0\), gives

\[
J-\frac{\lambda z}{2-\sqrt3}
>
0.4703
\mathord{-}0.9763\left(10+\frac1{2-\sqrt3}\right)0.0088
\mathord{-}2(0.1473)
>0.0577.
\]

Thus \(J>\lambda z/(2-\sqrt3)\ge0\), contradicting
\(\lambda z\ge(2-\sqrt3)J\). The companion verifier passes.

## 4. Scope and regressions

| Potential failure | Audit result |
| --- | --- |
| Sparse train counted once per incident rhombus | Pass: transverse-area union bound |
| Directional estimate applied to sparse interface trains | Pass: sparse trains are removed first |
| Reuse of one boundary occurrence | Pass: injective occurrence assignment is required |
| Full-source affine-kernel extension | Not used |
| Deletion of contact-isolated source points | Not used |
| Near-equilateral teeth promoted to exact triangles | Not used |
| Local carrier contradiction called global C-II closure | Explicitly rejected |
| Inactive-container branch | Not addressed |

## 5. Exact surviving obstruction and disposition

The audited result removes the full-core Type-II subwindow
\(\sigma\le0.0088\), under proof-only signed-return inputs. A complete C-II closure
still needs an all-regime full-core argument for \(\sigma>0.0088\), or an exact
contact/strict sub-\(D\) construction there, and an independent closure of the
macroscopic inactive-container branch.

**Audited-working, proof-only.** Keep the report and certificate, but do not update
docs/STATE.md, docs/state/theorem-state.yaml, or the Target C canonical route map
without the repository promotion transaction.
