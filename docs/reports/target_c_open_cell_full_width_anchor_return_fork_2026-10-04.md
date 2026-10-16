<!-- theorem-state: {"artifact_id":"ART-B3F063CAB89F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: full-width attachment separation and anchored return fork

Date: 2026-10-04
Source provenance: automation/target-c-open-cell-full-width-anchor-return-2026-10-04-v2; independently audited on current main 596445ac32ffd45e2cbb8df9dbeba15be3465cf5
Status: proof-only Target C-II candidate; theorem-state authority unchanged.
LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.

This note stays in the strong nonconstant open-witness-cell Type-II route and
starts only from current main.

Current main gives a harmonic attachment cell
\[
P_{\cap}=\operatorname{conv}A_{\cap},
\]
a coherent strict-rhombus component
\[
G_{\cap}\subset \operatorname{int}C_*\cap P_{\cap},
\qquad
A_G:=\operatorname{area}(G_{\cap})=\Omega_\epsilon(D^2),
\tag{1}
\]
and a same-host loaded attachment \(a_*\in A_{\cap}\cap\Gamma_*\).
Let \(\eta\) be the signed perpendicular distance from the host-cap chord line,
positive toward the cap, and put \(H_*=\eta(a_*)\).

The attachment-depth theorem on main gives \(H_*\ge A_G/D\). Attachments outside
\(\Gamma_*\) have nonpositive height, while \(a_*\) maximizes height on
\(\Gamma_*\). Thus \(a_*\) is a global height maximizer on \(A_{\cap}\), and
\[
P_{\cap}\subset\{\eta\le H_*\}.
\tag{2}
\]

## 1. Full-width second attachment

Put
\[
h_-=\min_{y\in G_{\cap}}\eta(y),\qquad
h_+=\max_{y\in G_{\cap}}\eta(y).
\]
Every line perpendicular to the height direction cuts \(G_{\cap}\) in
one-dimensional measure at most \(D\), because
\(G_{\cap}\subset P_{\cap}\) and \(\operatorname{diam}P_{\cap}\le D\).
Fubini gives
\[
A_G\le D(h_+-h_-).
\tag{3}
\]
Since \(h_+\le H_*\),
\[
H_*-h_-\ge {A_G\over D}.
\tag{4}
\]

Choose \(y_-\in G_{\cap}\) with \(\eta(y_-)=h_-\). Since
\(y_-\in\operatorname{conv}A_{\cap}\) and \(\eta\) is affine, some
\(b_*\in A_{\cap}\) satisfies \(\eta(b_*)\le h_-\). Hence
\[
\eta(a_*)-\eta(b_*)\ge {A_G\over D}.
\tag{5}
\]
Signed distance is 1-Lipschitz, so
\[
\boxed{
r_*:=|a_*-b_*|\ge {A_G\over D}=\Omega_\epsilon(D).
}
\tag{6}
\]
In particular \(b_*\ne a_*\). Both are loaded attachment vertices, hence actual
positive-diameter endpoints in the full-visibility source.

This uses the full height width of the quadratic grain. It improves the
half-area separation \(A_G/(2D)\) obtainable from a median-height cut and does
not require deleting crossing rhombi.

## 2. Canonical two-arc return at the loaded anchors

Attachment vertices are extreme vertices of their attachment polygon and occur
on the outer-face walk of the induced harmonic graph. Therefore canonical
Section 120 applies to \(a_*,b_*\).

Let \(d_{\cap}=\operatorname{diam}P_{\cap}\le D\), let \(L_{\cap}\) be the
occurrence-counted outer-walk length, let \(P_{{\rm exc},\cap}\) be the total
bounded nonquadrilateral perimeter, and let \(A_{4,\cap}\) be total strict
rhombus area in the cell. Section 120 gives
\[
d_{\cap}\bigl(L_{\cap}+P_{{\rm exc},\cap}-2r_*\bigr)
\ge (4-2\sqrt3)A_{4,\cap}.
\tag{7}
\]
Because \(G_{\cap}\) is a strict-rhombus subcomplex,
\(A_{4,\cap}\ge A_G\). Hence
\[
\boxed{
L_{\cap}+P_{{\rm exc},\cap}-2r_*
\ge (4-2\sqrt3){A_G\over D}.
}
\tag{8}
\]
Combining (6) and (8),
\[
\boxed{
L_{\cap}+P_{{\rm exc},\cap}
\ge (6-2\sqrt3){A_G\over D}.
}
\tag{9}
\]

## 3. Exact payment-versus-detour fork

Set \(\kappa=2-\sqrt3\). Equation (8) is
\[
(L_{\cap}-2r_*)+P_{{\rm exc},\cap}
\ge 2\kappa {A_G\over D}.
\tag{10}
\]
Therefore at least one of
\[
\boxed{
P_{{\rm exc},\cap}\ge\kappa {A_G\over D}
}
\tag{11}
\]
and
\[
\boxed{
L_{\cap}-2r_*\ge\kappa {A_G\over D}
}
\tag{12}
\]
must hold.

In the first branch canonical Section 123 gives
\[
\sum_rP_{{\rm exc},r}\le10(e_{BB}-k),
\]
so this one cell forces
\[
\boxed{
e_{BB}-k\ge {2-\sqrt3\over10}{A_G\over D}
=\Omega_\epsilon(D).
}
\tag{13}
\]

In the second branch, cut the outer walk at the chosen occurrences and let the
two complementary route lengths be \(\ell_1,\ell_2\). Both join \(a_*\) to
\(b_*\), so \(\ell_i\ge r_*\), and
\[
(\ell_1-r_*)+(\ell_2-r_*)=L_{\cap}-2r_*.
\]
Thus one actual outer route obeys
\[
\boxed{
\ell_i-r_*
\ge {2-\sqrt3\over2}{A_G\over D}
=\Omega_\epsilon(D).
}
\tag{14}
\]

So the strong Type-II cell has either a linear canonical loaded-hull payment
\(e_{BB}-k\), or a specific occurrence-counted outer route between two
macroscopically separated loaded actual-diameter endpoints whose excess over
their Euclidean chord is linear.

## 4. Host location and scope

The second attachment \(b_*\) may lie outside \(\Gamma_*\) or on the same host
arc. Equation (6) holds in both cases. If it lies on the same arc, the source
has two same-host loaded attachments with signed-height separation at least
\(A_G/D\). If it lies outside, the pair spans the two force-hull sides of the
host chord.

No claim is made that \(a_*b_*\) itself is a diameter edge. The theorem uses
only that both endpoints are loaded actual-diameter endpoints. It does not
identify the far-grid internal contact path with either outer route, and it
does not prove that the route in (14) is simple, bridge-free, or globally
injective across harmonic cells.

The exact remaining strong Type-II obligation is now to spend one of the two
canonical alternatives: upper-bound the linear \(e_{BB}-k\) payment strongly
enough to contradict the source ledger, or couple the anchored linear route
excess to the cap-local complete grid, diameter-thrackle geometry, or a
source-preserving contact-changing competitor.

The Type-I macroscopic-container branch and the non-strong inverse-\(D\)
inactive near-unit/near-diameter branch remain separate. C-II and Level I
remain open.

No computation, verifier, numerical experiment, or CI result is a proof
premise.

Disposition: proof-only Target C candidate.
