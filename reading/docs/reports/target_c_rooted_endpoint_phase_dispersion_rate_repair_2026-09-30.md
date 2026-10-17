> Generated reading edition · [exact source](../../../docs/reports/target_c_rooted_endpoint_phase_dispersion_rate_repair_2026-09-30.md) · source SHA-256 `333197e8789e5ae2fcfffe866ab2899dc8356ef68c919139f76e2f04be794063`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-532A034EEB45","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: rate-free repair for rooted endpoint phase dispersion

Base: ab76928fea0b4fb3ef30b4ac4bb819cfcffd1097.
Status: proof-only repair; C-II remains open.

The endpoint-exclusion argument in the parent commit should not rely on the
D-dependent window delta_D when transferring Hausdorff convergence to boundary
length. The following fixed-epsilon lemma removes that rate issue.

Let Z_w=L_w-per(P_w)=o(D). Let E_D be distinct outer-edge occurrences on
nonprincipal attachment routes whose projective directions lie in an eta_D-window
about one fixed direction u, with eta_D -> 0. Then |E_D|=o(D).

Proof. Fix epsilon>0 first, then take D large enough that eta_D<epsilon/4.
If a selected route has base-chord direction at projective distance at least epsilon
from u, each selected edge differs from that base direction by at least
3 epsilon/4. The exact projection identity

ell_i-b_i = sum_{e in R_i}(1-q_i dot z_e)

therefore charges at least c_epsilon=1-cos(3 epsilon/4)>0 per selected occurrence.
Their total number is at most Z_w/c_epsilon=o(D).

For the remaining routes, base directions lie within epsilon of u. At the endpoint,
the limiting nonprincipal attachment boundary is one radius-1/2 circular support arc
of angular length U<pi plus two isolated support points. The projective epsilon-window
has one oriented lift on that arc. Monotonicity of convex boundary directions implies
that the normalized total base length in the window is O(epsilon); isolated support
points contribute o(1) normalized base length after first fixing, then shrinking, an
angular neighborhood. Hence the corresponding route-edge count is at most

O(epsilon D)+o(D)+Z_w.

Thus limsup |E_D|/D <= C epsilon. Let epsilon -> 0. This proves |E_D|=o(D).

The order of limits is epsilon fixed, D -> infinity, epsilon -> 0. No rate of
Hausdorff or annular convergence is assumed.

Consequently the parent endpoint exclusion remains valid: canonical Section 90 gives
two linear inverse-phase train families separated by pi/3; Q_w=o(D) removes bounded
nonquadrilateral ends; the lemma removes nonprincipal outer ends; principal-corridor
geodesicity aligns each remaining phase with a corridor. The three corridor
separations for gap vector (theta,phi,phi) are theta/2, theta/2, pi-theta, none equal
to pi/3 because theta>2pi/3. Contradiction.

This note repairs only the route-phase dispersion step. It does not claim a uniform
gap above lambda1.
