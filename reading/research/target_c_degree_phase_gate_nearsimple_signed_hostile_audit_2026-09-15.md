> Generated reading edition · [exact source](../../research/target_c_degree_phase_gate_nearsimple_signed_hostile_audit_2026-09-15.md) · source SHA-256 `3c6cdbd5ad1f9196403d3de075f9efdf3e8d63696d1a22c5f9d8f92f36f3e9f2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b460435916c02ef0a45c214f227ca2013f63a7d3", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_degree_phase_gate_nearsimple_signed_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "3e6579fe4febd5292baedd80c931d17a99be0a2a6e20dc6b6cff11091c0c3b6d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — degree/phase-gate and near-simple signed composition

**Date:** 2026-09-15  
**Reviewed:**

- `research/target_c_global_straight_degree_phase_gate_2026-09-15.md`;
- `research/target_c_degree_phase_gate_nearsimple_signed_composition_2026-09-15.md`.

**Disposition:** **PASS at proof-only low-`t` full-core Type-II scope, after the explicit repeated-outer correction already incorporated in the reviewed theorem.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The first draft of the phase-gate note briefly conflated “at most one straight outer
occurrence” with “at most one outer occurrence.” That inference is false for unloaded
articulation vertices. The reviewed version no longer makes it: repeated-outer
vertices form a separate articulation branch, and the later near-simple theorem bounds
that branch by the full outer-walk repetition surplus. This audit checks the corrected
chain from scratch.

---

## 1. Straight sector geometry and degree collapse

At a `beta`-straight internal occurrence on a distinguished route `W_i`, the incoming
ray viewed from the vertex lies within `beta` of `-u_i`, while the outgoing ray lies
within `beta` of `+u_i`. Their smaller angular separation is therefore strictly larger
than

```math
\pi-2\beta.
```

The outer-face incidence is one of the two sectors between those rays, so its angle
`g` also satisfies

```math
g>\pi-2\beta.
```

All other contact rays lie in the complementary sector of angle `2pi-g`. If the
physical contact degree is `d`, that complement contains `d-1` consecutive contact-ray
gaps. Unit separation and triangle-freeness make every such gap strictly larger than
`pi/3`. Hence

```math
(d-1){\pi\over3}<2\pi-g<\pi+2\beta.
```

For `beta<=pi/6`, the right side is at most `4pi/3`, so the strict inequalities imply
`d<=4`. The loaded-route exclusion makes the internal vertex unloaded, and C26 gives
`d>=3`.

Thus every straight internal occurrence in this window has contact degree exactly
three or four.

**Verdict:** PASS.

---

## 2. The 15-degree straight-occurrence injection is correctly scoped

Suppose one physical vertex supported two `beta`-straight outer-face occurrences.
Those are two distinct outer angular sectors, each strictly larger than
`pi-2beta`. Since the vertex has degree at least three, there is at least one further
contact-ray gap, strictly larger than `pi/3`. Therefore

```math
2\pi>2(\pi-2\beta)+{\pi\over3}.
```

At `beta<=pi/12`, the right side is at least `2pi`, impossible.

This proves only that one physical vertex supports at most one **straight** occurrence.
It does not exclude an additional nonstraight occurrence of the same physical vertex
on the outer facial walk. The corrected theorem says exactly this.

Consequently `S_15` counts distinct physical straight vertices, but a separate
repeated-outer test is still required before treating all other angular sectors as
bounded faces.

**Verdict:** PASS after correction.

---

## 3. Repeated-outer straight vertices really are paid by `b-V_out`

For the occurrence-counted outer facial walk, let `m_x` be the number of occurrences
of physical outer vertex `x`. Then exactly

```math
b-V_{out}=\sum_x(m_x-1).
```

A straight vertex whose straight sector is not its only outer-face incidence has
`m_x>=2`, and therefore contributes at least one to this sum. Distinct repeated-outer
straight vertices contribute to distinct summands. Hence

```math
A_{15}\le b-V_{out}.
```

The main near-simple theorem gives at the current endpoint

```math
(b-V_{out})/D
\le0.0459365399110338116\ldots+o(1).
```

Subtracting this from the independently certified

```math
S_{15}/D
\ge1.1543116921171727469\ldots-o(1)
```

gives

```math
V_{simp,15}/D
\ge1.1083751522061389353\ldots-o(1).
```

No assumption that every repeated vertex has two straight occurrences is used here;
nonstraight repeats are fully included in `b-V_out`.

**Verdict:** PASS.

---

## 4. Positive equilibrium makes the straight outer sector strictly sub-semicircular

At an unloaded vertex there is no positive diameter row. Relative-interior positivity
therefore gives a positive contact-only equilibrium

```math
\sum_{xy}\alpha_{xy}(y-x)=0,
\qquad \alpha_{xy}>0.
```

If the contact rays lay in a closed semicircle, a supporting normal would have
nonnegative scalar product with every ray. Positivity of the coefficients forces every
ray onto the supporting line. With at least three distinct unit-contact rays this is
impossible. Thus every cyclic contact-ray gap is strictly less than `pi`.

For the straight outer sector,

```math
\pi-2\beta<g<\pi,
```

so

```math
\tau:=\pi-g
```

satisfies `0<tau<2beta`; at `beta=pi/12`, `0<tau<pi/6`.

**Verdict:** PASS.

---

## 5. Simple-outer face sectors are legitimate bounded-face incidences

A simple-outer straight vertex is defined occurrence-theoretically: its straight sector
is the only incidence of the unbounded face at that physical vertex. Every other
sector in the cyclic rotation is therefore a bounded-face incidence.

There is no hidden bridge exception. In the current full positive core, the proved
bridge-localization statement puts positive contact bridges on the unbounded face. A
bridge incident to the vertex would create additional outer-face incidence rather than
a bounded quadrilateral sector, placing the vertex in the repeated-outer branch.

The canonical bounded-face structure theorem makes every bounded degree-four face a
strict unit rhombus and every bounded face boundary a simple cycle in the scope used by
the phase-gate argument.

**Verdict:** PASS.

---

## 6. Cubic rhombus classification

At a cubic simple-outer straight vertex there are two bounded-face sectors. Their
angles satisfy

```math
\gamma_1+\gamma_2=\pi+\tau.
```

If either face is exceptional, the event is correctly assigned to the exceptional
branch. Otherwise both are strict unit rhombi. Writing the acute angle of a strict
rhombus as

```math
\pi/3+\delta,
\qquad0<\delta\le\pi/6,
```

the angle at the vertex is either `pi/3+delta` or `2pi/3-delta`.

Two acute/right angles sum to at most `pi`, so they cannot realize `pi+tau` with
`tau>0`. The only possibilities are:

- one acute/right and one obtuse, giving exactly
  ```math
  \tau=\delta_a-\delta_o>0;
  
  ```
- two obtuse, giving exactly
  ```math
  \delta_1+\delta_2=\pi/3-\tau>\pi/6.
  
  ```

No other all-rhombic cubic case exists.

**Verdict:** PASS.

---

## 7. Quartic all-rhombic fan classification

At a degree-four simple-outer straight vertex, the three bounded-sector angles satisfy

```math
\gamma_1+\gamma_2+\gamma_3=\pi+\tau<7\pi/6.
```

Each strict-rhombus angle is strictly greater than `pi/3`. If one were at least
`pi/2`, the total would be strictly greater than

```math
\pi/2+2\pi/3=7\pi/6,
```

contradiction. Hence all three rhombi are acute at the vertex, with

```math
\gamma_j=\pi/3+\delta_j.
```

Summation gives the exact identity

```math
\delta_1+\delta_2+\delta_3=\tau<\pi/6.
```

**Verdict:** PASS.

---

## 8. Exceptional-face and angular-defect charges do not undercount multiplicity

If `f` is the number of bounded exceptional faces and `Q` their total degree-above-four
excess, their total boundary-vertex incidence count is

```math
\sum_F|\partial F|=4f+Q.
```

Choosing one exceptional incidence for each simple straight vertex that touches an
exceptional face gives the safe injection

```math
X\le4f+Q.
```

For a cubic double-obtuse gate, the two incident rhombus defects have sum greater than
`pi/6`. Summing this local payment over all such gates can reuse the defect of one
rhombus at at most its four physical vertices. Therefore

```math
O{\pi\over6}<4\Delta_{train},
```

or

```math
O<{24\over\pi}\Delta_{train}.
```

No assumption that the gate rhombi are edge-disjoint is present; the factor four is
exactly the safe vertex-incidence multiplicity.

**Verdict:** PASS.

---

## 9. The phase-cut charge is occurrence-safe

Canonical Section 68 chooses a set of deleted strict-rhombus crossing relations with

```math
|F_{cut}|\le\left\lfloor{3\Delta_{train}\over\pi}\right\rfloor.
```

A strict rhombus has four vertices. Therefore one deleted rhombus relation can spoil
at most four transmission gates, regardless of how its train endpoints are reused
elsewhere. The number of transmission gates hit by the cut is at most

```math
4|F_{cut}|\le {12\Delta_{train}\over\pi}.
```

Combining with the double-obtuse payment gives the reviewed `36/pi` coefficient.
There is no double counting error: the `24/pi` term removes high-defect gates before
the phase cut, while the `12/pi` term removes surviving transmission gates incident to
a cut rhombus.

**Verdict:** PASS.

---

## 10. Signed injectivity extends from one representative to every extra incidence

At a straight occurrence on route `W_i`, every extra contact lies in the core-side
sector and satisfies the signed estimate

```math
(w-x)\cdot n_i>\sin(\pi/3-\beta).
```

At `beta=pi/12`, this is `>1/sqrt(2)`.

Suppose the same unit edge `xy` were an extra contact at straight occurrences at both
endpoints. With `e=y-x`,

```math
e\cdot n_i>1/\sqrt2,
\qquad
e\cdot n_j<-1/\sqrt2.
```

Thus the hull-side normals differ by more than `pi/2`. Type-II near-disk geometry
separates their side midpoints by at least `D/sqrt2-o(D)`. The hostile-audited signed
penetration proof's route-midpoint estimate then gives

```math
d_i+d_j\ge\sqrt2D-o(D).
```

This contradicts `d_i+d_j<=d_out<=0.002883975D+o(D)`.

The proof does not use how the extra incidence was selected. It therefore applies to
**all** extra incidences at every straight vertex. Since different extra incidences at
one physical endpoint are different contact edges, the whole incidence-to-edge map is
injective. Hence

```math
E_{all,15}=V_3+2V_4=S_{15}+V_4
```

and, in particular,

```math
E_{all,15}/D\ge1.1543116921171727469\ldots-o(1).
```

**Verdict:** PASS.

---

## 11. Numerical certificate

The Decimal certificate

```bash
python3 research/verify_target_c_degree_phase_gate_nearsimple_signed_composition.py
```

checks

```math
1.1543116921171727469
-0.0459365399110338116
=1.1083751522061389353
```

and the displayed half-split constants. The arithmetic is independent of the
geometric audit above.

**Verdict:** PASS.

---

## 12. Scope and unresolved gap

The reviewed chain proves a strong normal form, not a contradiction. In particular it
does not prove

- that exceptional-face incidence is scarce enough to leave a positive unconditional
  `P_ret` floor;
- that different retained phase gates lie on distinct stopped trains;
- that one Woodall diameter edge cannot brace many gates; or
- that the articulation/exceptional/phase-gate structure admits a simultaneous
  diameter-decreasing motion.

The next useful theorem must be an occupancy or reuse theorem linking these boundary
gates to the low-`t` pentagon/train network or to the near-extremal Woodall diameter
graph.

**Final verdict:** **PASS at proof-only low-`t` full-core Type-II scope. C-II remains
open.**
