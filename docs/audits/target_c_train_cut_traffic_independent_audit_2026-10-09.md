<!-- theorem-state: {"artifact_id":"ART-F544D999283E","canonical":true,"claim_ids":["C-TRAIN-CUT-TRAFFIC-COMPRESSION"],"claim_statuses":{"C-TRAIN-CUT-TRAFFIC-COMPRESSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.198 — finite train-cut traffic compression

Date: 2026-10-09. Audit base: 8718243828106e1447657e557980ad0db41e589f,
state 2026-10-09.audit.191. Target C C-II and Level I remain open.

Frozen candidate: origin/research/sol/target-c-level1-gpt61-2026-10-04 at
9875cd6a77939bb6347353fc798ab8f9ab03ec3e. The source report
[target_c_multishear_traffic_domination_2026-10-05.md](../reports/target_c_multishear_traffic_domination_2026-10-05.md)
has SHA-256 450d2712b3f24bb25e842502636d61e61f93d56111b92e820f6973c9ad066644.
Its verifier at the same immutable commit has SHA-256
2260ca9e5fbf0b0cdc655f35afa9b2eb209fa840243eedff6c41bc0bd5226c11.

## Verdict

**PASS WITH NARROWED SCOPE — promote C-TRAIN-CUT-TRAFFIC-COMPRESSION.**
For the canonical positive semidefinite stress with its affine kernel on the
nonisolated positive-contact core, and for an explicitly admissible family of
disjoint actual contact cutsets with a tree of occupied regions, the cut
compression is positive semidefinite, has the stated exact kernel, and gives an
exact weighted sum-of-old-diameter-squares identity for the finite region
translations. The one-cut strictness threshold is valid.

This result does not extract such a family of cuts from every canonical source.
It controls the weighted mean of the old diameter pairs, not their maximum.
It gives no common upper-feasible endpoint, strict diameter improvement, or
frontier change.

## Exact statement promoted

Let P be a triangle-free global minimum-diameter source with D>=9, chosen to
minimize contacts and then actual diameter pairs. Let V be its connected,
two-dimensional nonisolated positive-contact core. Use the relative-interior
normalized stress from C-ZRF, restricted to V:

\[
\Omega_V=L_C^\alpha-L_H^\beta\succeq0,\qquad
\ker\Omega_V=\operatorname{span}\{\mathbf1,p_x,p_y\},\qquad
\sum_{h\in H}\beta_h=1.
\]

Here C is the full actual unit-contact set, H is the full actual diameter
pair set, all coefficients on these rows are positive, and every endpoint of
H lies in V. Contact-isolated points remain in the full source and are not
given stress or kernel coordinates.

Take a finite tree T of complementary regions from an admissible disjoint
family of actual contact cutsets. Every full-source label, including each
contact isolate, lies in one region. Each region has a core representative.
For each tree edge e, let S_e be its child shore and put
R_ve=1 when the region of core vertex v is in S_e, and zero otherwise.
Assume each contact either lies in one region or crosses exactly one selected
cut e; the crossing contacts are precisely the selected physical contacts
of train e, and when oriented from the other shore to S_e each has the
same unit vector u_e. These are the actual cutset hypotheses: no selected
stressed edge or virtual cut is substituted.

Set

\[
A_e=\sum_{c\in\tau_e}\alpha_c,\qquad
\varepsilon_{he}=R_{j_h e}-R_{i_h e},\qquad
\mathcal B_{ef}=\sum_{h\in H}\beta_h\varepsilon_{he}\varepsilon_{hf},
\qquad W=\operatorname{diag}(A)-\mathcal B.
\]

Then R has full column rank and

\[
\boxed{W=R^T\Omega_VR\succeq0,\qquad
\ker W=\{(\ell\cdot u_e)_e:
\ell\cdot w_c=0\text{ for every unselected contact }c\}.}
\]

Here w_c is the oriented unit vector of the unselected contact; its sign does
not affect the span. In particular,

\[
\dim\ker W=2-\dim\operatorname{span}\{w_c:c\text{ unselected}\},
\]

and W is positive definite exactly when those unselected directions span
\(\mathbb R^2\).

For any angles theta_e, set
\(\Delta_e=R_{\theta_e}u_e-u_e\) and translate every source label in region v
by its sum of \(\Delta_e\) along the root-to-v tree path. Every unit contact is
preserved exactly; for all sufficiently small angle vectors every other
full-source pair remains strictly more than one apart. If
\(\Delta^{(k)}=(\Delta_{e,k})_e\) is the vector of coordinate increments, then
the exact labelled-coordinate identity is

\[
\boxed{\sum_{h\in H}\beta_h|p'_{i_h}-p'_{j_h}|^2
=D^2-\sum_{k=1}^2(\Delta^{(k)})^TW\Delta^{(k)}.}
\]

Thus the weighted sum is nonincreasing for every angle vector, and is strictly
smaller whenever one coordinate increment vector is outside ker W. For one
selected cut, if |V|>2 floor(D)+2, then W_ee=A_e-\mathcal B_ee>0:
otherwise its binary shore indicator would be affine on V, forcing all core
points onto two parallel lines with at most floor(D)+1 unit-separated points
on each.

## Independent reconstruction

For each contact c, the vector of shore-indicator differences is zero when
the contact is unselected and is +e_e or -e_e for a selected contact in
train e. The stipulated cutset condition excludes a contact crossing two
selected cuts. Therefore its contact-Laplacian contribution to
R^TL_C^alpha R is either zero or alpha_c e_e e_e^T, giving diag(A). Each
actual diameter pair contributes beta_h epsilon_h epsilon_h^T to
R^TL_H^beta R. Subtraction gives W=R^T Omega_V R, hence positive
semidefiniteness.

The occupied-region representatives make R full rank: the root row is zero,
and the difference of representative rows in adjacent regions is the signed
coordinate vector of their tree edge. If Wx=0, semidefiniteness gives
Rx in ker(Omega_V), so Rx=b+ell dot p. Differences across unselected
contacts force ell orthogonal to their directions; differences across a
selected contact in train e give x_e=ell dot u_e. Conversely, for any such
ell, setting x_e=ell dot u_e makes Rx-ell dot p constant across every
contact edge. Connectedness of the core makes it constant on V, so
Rx in ker(Omega_V) and Wx=0. The map from ell to x is injective on
this orthogonal complement because the full set of core contact directions
spans the plane.

For the finite motion, a selected contact has relative translation increment
Delta_e, hence its old vector u_e becomes R_{theta_e}u_e; an unselected
contact's endpoints remain in the same region. The source is finite, so every
strict lower pair has positive slack and remains strict in a sufficiently small
common neighborhood, including pairs incident to contact isolates. Finally,
the core coordinates after motion are p'_k=p_k+R Delta^(k). Since the
coordinate vectors p_k are in ker(Omega_V),

\[
(\Delta^{(k)})^TW\Delta^{(k)}
=p_k'^T\Omega_Vp_k'-p_k^T\Omega_Vp_k.
\]

Summing over the two coordinates, all contact terms remain
sum_C alpha_c=D^2 by the original stress identity and sum_H beta_h=1;
rearranging gives the displayed exact diameter-square identity. This is an
energy statement on all actual diameter pairs, whose endpoints lie in V; it
does not extend the stress kernel to contact isolates.

If a one-cut diagonal were zero, positive semidefiniteness would put its basis
vector in ker W. The kernel formula makes the corresponding binary shore
indicator affine on V. Since both shores are nonempty, the affine functional
is nonconstant, so V lies on two parallel lines. Unit separation and
diam(V)<=D bound each line by floor(D)+1 points, proving the stated strict
threshold.

## Hostile checks and certificate boundary

- The stress is the canonical PSD stress and the affine kernel is only on V,
  as stated by C-ZRF. The proof does not infer PSD for a generic equilibrium
  stress or extend the kernel to source isolates.
- The tree-cut incidence is essential. If a contact crosses two selected cuts,
  its contact term has off-diagonal entries and the asserted diagonal contact
  compression need not hold. The theorem is only for the explicit cutset
  hypotheses above; no cut-family extraction is claimed.
- The weighted mean loss is not a maximum-diameter descent. It does not check
  every old or newly activated upper pair. The canonical finite positive-stress
  heptagon regression remains consistent because it refutes a stronger
  finite-competitor inference, not this exact energy identity.
- The source's one-cut pair formulas were expanded directly and are correct,
  but no separate claim is promoted here. Their inequalities still require
  checking every source pair and do not give a common feasible angle.

The frozen verifier was inspected and rerun at the source commit. It uses exact
Fraction arithmetic and passes 134 nonnegative principal-minor checks, the
four finite packet kernel/compression checks, exact contact preservation and
all lower-pair checks in those fixtures, and 480 sampled one-cut polynomial
identity checks. It does not certify the analytic theorem, source globality,
existence of a canonical cut family, or any upper-feasible endpoint. The
analytic proof above is the basis for promotion.

## Canonical disposition

Promote C-TRAIN-CUT-TRAFFIC-COMPRESSION, depending on C-ZRF, at precisely
the cutset scope stated above. There is no Target C frontier change: a common
upper-feasible finite endpoint, a strict sub-D competitor, and the
macroscopic-container branch remain open. Contact-isolated points are retained
and moved by their assigned region, but remain outside the stress kernel.
