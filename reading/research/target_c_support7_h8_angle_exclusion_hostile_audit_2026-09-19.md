> Generated reading edition · [exact source](../../research/target_c_support7_h8_angle_exclusion_hostile_audit_2026-09-19.md) · source SHA-256 `a473701b81b548c14a26708ee12dd5108033405965b6a80d27026a90a322bc61`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "090d53476455340fa037f20583c00c5831ebd2e3", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h8_angle_exclusion_hostile_audit_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "645081cf263949863937a24efd049e02a4f49df726329c5114603ea75581384a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — support-seven `H8` exact turn-angle exclusion

**Date:** 2026-09-19  
**Audited source:** `research/target_c_support7_h8_angle_exclusion_2026-09-19.md`  
**Certificate:** `research/verify_target_c_support7_h8_angle_exclusion_2026_09_19.py`  
**Verdict:** PASS at the stated scope  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

## 1. Claim and scope

The source claims only that eight of the 20 fully convex support-seven `H8` reflection orbits left by the preceding endpoint reduction are impossible. It leaves 12 convex orbits and all nonconvex `H6/H7` cases open. It does not claim a support-seven exclusion or improve the global one-anchor coefficient from `1/7` to `1/8`.

Verdict: scope is correctly limited.

---

## 2. Force-cycle reconstruction: PASS

In a fully convex reciprocal octagon, the present raw rays at a hull vertex lie in one open cone of width `<pi`. The raw cyclic order is inherited from the hull order after deleting missing neighbors.

For an edge sign `+`, the unit force ray is the raw ray; for sign `-`, it is reversed by `pi`. Since the two raw cones are disjoint, all positive force rays occur as one ordered block and all negative force rays as the other ordered block. The verifier's cycle construction

```text
positive raw rays in raw order, then negative raw rays in raw order
```

is therefore a valid counterclockwise force cycle up to cyclic rotation. All gap identities are invariant under that arbitrary starting point once the certificate fixes the same cycle convention throughout.

At non-ground vertices there are exactly five present edges; at the ground there are seven.

Verdict: PASS.

---

## 3. Raw-angle affine conversion: PASS

The verifier reimplements the already-audited support-six conversion. For an ordered pair of incident edges it computes the counterclockwise force arc `R`; it separately knows:

- whether the two edge signs agree; and
- the exact raw orientation `chi` from the convex hull order.

The raw angle is then exactly one of `R`, `2-R`, `R-1`, or `1-R`. The conversion uses only integer coefficients and integer constants in units of `pi`.

Every triangle named in the eight identities is checked to use three present reciprocal edges before its affine angle sum is constructed.

Verdict: PASS.

---

## 4. Equalities used: PASS

For each vertex, the force-ray gaps make one full turn, so `F_i=2` exactly. For every nondegenerate reciprocal triangle, ordinary Euclidean interior-angle sum gives `T_abc=1` exactly.

The fully convex `H8` assumption guarantees all eight reciprocal points are distinct hull vertices, hence no triangle is collinear. The triangle equations do not use the reciprocal stress or signed trace identity.

Verdict: PASS.

---

## 5. Strict inequalities used: PASS

For every physical non-ground pentagon, prior audited work proves

$$
0<x_{i,k}<2/3,
\qquad
2/3<x_{i,k}+x_{i,k+1}<1.
$$

The source uses only these bounds and, in two cases, strict positivity of a ground force gap. In convex `H8`, the seven raw ground rays are distinct; reversing a subset by `pi` cannot create coincident force rays because all raw rays lie in an open cone of width `<pi`. Hence every ground force gap is strictly positive.

No inequality is weakened in the wrong direction. Each certificate sums strict inequalities, so the resulting comparison `C<B` is strict.

Verdict: PASS.

---

## 6. Exact certificate structure: PASS

Each case is encoded by a labelled missing-edge set and a labelled positive-edge set. The verifier first reconstructs the exact 20-orbit input from the preceding support-seven certificate and asserts each of the eight `(type,M,P)` triples occurs in that input.

For each case it then:

1. converts every listed strict turn bound to a rational affine inequality `row*x < bound`;
2. sums them to obtain `C(x)<B`;
3. constructs the claimed affine combination of `F_i` and `T_abc`;
4. compares the complete coefficient dictionaries and affine constants exactly;
5. substitutes only the exact values `F_i=2`, `T_abc=1` and verifies the same functional is forced to `C(x)=B`.

All arithmetic is `fractions.Fraction` or integer dictionary arithmetic. There is no tolerance, LP solver, or floating-point branch in the committed certificate.

Verdict: PASS.

---

## 7. Case-by-case boundary values: PASS

The verifier reproduces:

```text
A: C7 exact identity forces C=-1, but strict turn inequalities force C<B; EXCLUDED
B: C7 exact identity forces C=1, but strict turn inequalities force C<B; EXCLUDED
C: C7 exact identity forces C=1, but strict turn inequalities force C<B; EXCLUDED
D: C3+C4 exact identity forces C=1, but strict turn inequalities force C<B; EXCLUDED
E: C3+C4 exact identity forces C=-2, but strict turn inequalities force C<B; EXCLUDED
F: C3+C4 exact identity forces C=-2, but strict turn inequalities force C<B; EXCLUDED
G: C3+C4 exact identity forces C=1, but strict turn inequalities force C<B; EXCLUDED
H: C3+C4 exact identity forces C=1, but strict turn inequalities force C<B; EXCLUDED
```

The two affine shifts in cases F and H are load-bearing and are included in the exact coefficient comparison, not added only after evaluation.

Verdict: PASS.

---

## 8. Orbit accounting: PASS

The preceding reduction has 20 convex reflection orbits: 12 of missing type `C7` and 8 of type `C3+C4`. The present certificate removes exactly eight distinct keys: three `C7` and five `C3+C4`.

It then asserts exactly

$$
9+3=12
$$

keys remain.

Global sign complement need not be checked separately: it gives the same raw reciprocal configuration with every force vector reversed and preserves the existence/nonexistence of the pentagon gap solution. Reflection was already quotiented in the input census.

Verdict: PASS.

---

## 9. Surviving linear feasibility is not overclaimed

A separate discovery LP was useful for finding the sparse identities, but no numerical LP result is used as proof. The committed theorem only excludes the eight cases with exact identities.

The source states that the other 12 pass the tested affine turn system with positive margin. That statement is diagnostic only and is not used to assert geometric realizability. Exact equilateral-pentagon closure, reciprocal metric realization, signed trace/tensor equilibrium, and global source/train geometry can still remove those cases.

Verdict: PASS.

---

## 10. Reproducibility

The verifier was run with Python 3 and `python3 -m py_compile`. Its final output is:

```text
A: C7 exact identity forces C=-1, but strict turn inequalities force C<B; EXCLUDED
B: C7 exact identity forces C=1, but strict turn inequalities force C<B; EXCLUDED
C: C7 exact identity forces C=1, but strict turn inequalities force C<B; EXCLUDED
D: C3+C4 exact identity forces C=1, but strict turn inequalities force C<B; EXCLUDED
E: C3+C4 exact identity forces C=-2, but strict turn inequalities force C<B; EXCLUDED
F: C3+C4 exact identity forces C=-2, but strict turn inequalities force C<B; EXCLUDED
G: C3+C4 exact identity forces C=1, but strict turn inequalities force C<B; EXCLUDED
H: C3+C4 exact identity forces C=1, but strict turn inequalities force C<B; EXCLUDED
PASS
eight additional fully-convex H8 reflection orbits excluded exactly
remaining H8 reflection orbits: 12 = 9 C7 + 3 C3+C4
```

Final verdict: **PASS at the stated scope.** Eight additional convex support-seven cases are rigorously removed; 12 convex `H8` cases and the nonconvex `H6/H7` branches remain. C-II remains open.
