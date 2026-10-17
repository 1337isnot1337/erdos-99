> Generated reading edition · [exact source](../../../docs/audits/target_c_pure_tooth_train_coordinate_reconstruction_hostile_audit_2026-09-12.md) · source SHA-256 `a159dae5a42b0f0258b9447078112879f1321c187c0db81bff892a39798f68f8`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2090D9D077E1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: hostile audit of exact pure-tooth train coordinates

Date: 2026-09-12  
Reviewed: proof-only `target_c_pure_tooth_train_coordinate_reconstruction_2026-09-12.md`.  
Disposition: PASS at exact pure-tooth, proof-only scope.  
Authority: audit.46 remains canonical; C-II remains open.

## 1. Scope

The claim assumes the exact Section-126 endpoint: one unloaded component, full
attachment set A=B, T_triangle=q, Qplus=0, and the audited train normal form with q
outer-to-outer stopped trains. Canonical C65 is also required when the statement is
applied to actual diameter pairs, because it identifies H with the full actual
diameter graph and excludes contact-isolated diameter endpoints.

No full-source affine-kernel statement is used. The coordinate identity is on the
nonisolated positive-contact core; source isolates are retained but have no active
contact or diameter row in this core calculation.

## 2. Independent derivation of the displacement identity

For a train τ choose a shore orientation and a unit contact vector u_τ so that its
exact one-train shear has velocity Ju_τ on one shore and zero velocity on the other.
For core vertices x,y define ε_xy(τ) as +1, -1, or 0 according to the signed shore
separation. The finite train-cut theorem says every contact edge of τ is exactly a
cut edge and every cut edge has the same oriented unit vector.

The exact shear therefore has relative velocity

  v_x^(τ) - v_y^(τ) = ε_xy(τ) J u_τ.

Summing these q one-train shears gives train-angle vector 1. The exact train-angle
normal form identifies this sum, modulo a common translation, with global rotation
v_x=Jp_x. Subtracting the two vertex equations and applying -J gives

  p_x - p_y = Σ_τ ε_xy(τ) u_τ.

This does not depend on a chosen contact path; the path-free statement comes from the
shore indicators, while the train-angle normal form supplies the equality with the
realized coordinates.

## 3. Metric and diameter consequences

Each nonzero coefficient has absolute value one and each u_τ is a unit vector, so

  |p_x-p_y| <= #{τ : τ separates x and y}.

For an actual diameter pair this gives an exact integer bound

  #{τ : τ separates x and y} >= ceil(D).

By C65 every actual diameter endpoint is in the core in this normalization. Since the
pure endpoint has h=q actual diameter edges, summation gives

  total diameter/train cut incidences >= q ceil(D).

The result counts distinct train cuts, not repeated edges of an arbitrary contact
path. Repeated crossings cancel in the shore indicator, so no path-length assumption
is hidden in the inequality.

The longitudinal and transverse projections are also correct: after orienting the
diameter vector r_h, the signed unit train vectors sum to r_h, so their normalized
longitudinal sum is D and the transverse sum is zero. The latter is the corresponding
diameter-derivative row relation.

## 4. Local and full-source scope checks

- The two-edge tooth check is consistent: a boundary contact route crosses the two
  train cuts belonging to its two contact edges, with the signs fixed by traversal.
- Reversing a shore orientation reverses both ε and u, leaving their product unchanged.
- Contact-isolated points are never inserted into the train coordinate map or moved by
  the algebraic reconstruction. They are handled only by C65’s full-source visibility
  statement.
- No claim is made that every Boolean train word is realized or that graph distance
  equals the number of separating trains.
- No response coefficient floor, support-only matrix argument, or global-minimality
  conclusion is smuggled into the metric bound.

## 5. What remains open

The incidence lower bound is strong but not contradictory: q may be a constant
multiple of D larger than one, and the exact vector sums can still have cancellation.
The separate support-only regression confirms that circular incidence, rank q-1, and a
positive left kernel do not suffice. A closure must combine the metric vector sums with
the actual odd-unicyclic diameter thrackle, train crossing angles, or a finite
diameter-decreasing motion.

Final disposition: exact train-cut reconstruction and its diameter-incidence
corollary pass at proof-only scope. No theorem-state change; C-II remains open.
