# Hostile audit — parameterized collapsed mod-2 exclusion

**Audited source:** `research/target_c_support6_collapsed_mod2_parameter_box_2026-09-19.md`  
**Verifier:** `research/verify_target_c_support6_collapsed_mod2_parameter_box_2026_09_19.py`

The certificate imports the earlier exact fixed-parameter verifier only for its
rational constants and inverse matrix; it independently constructs the enlarged
interval box and all new interval bounds. The fixed parameters are widened by
`1/10000`, and every solved variable is widened by `1/1000`.

The contraction map is `T(x)=x-CF(x,p)`. The interval residual at the solved-angle
center gives `Y`, while the interval matrix `I-CJ` gives `Z0`; the additional
Lipschitz term is an overestimate of the solved-angle variation. The reported
`Z<1` and `Y+Z*R<R` therefore prove a self-map contraction for every parameter in
the parameter rectangle. This proves existence and uniqueness inside the solved
box, not uniqueness of arbitrary roots outside that box.

The geometry checks are interval checks. They verify strict order separation, all
positive turns, the upper one-turn bound, both adjacent-turn bounds, and the exact
face-order tuple. For each of the three selected edge-disjoint cycle pairs, every
train pair is enclosed on one side of the strict crossing threshold `|u.v|=1/2`;
the permitted pair set is exactly the one used by the earlier mod-2 certificate.
No numerical angle comparison is used in the logical tests.

The final contradiction is the audited plane mod-2 intersection identity. The note
does not identify the auxiliary closure surface with the physical plane and does not
assume any source embedding or diameter optimality.

Reproduction:

```text
python3 research/verify_target_c_support6_collapsed_mod2_parameter_box_2026_09_19.py
```

Expected final lines include:

```text
PASS: exact two-parameter collapsed mod-2 obstruction box
parameter_radius 0.0001 solved_radius 0.001
PASS: every closure point in the parameter box is globally excluded by XOR 0=1
```

**Audit disposition:** PASS for the stated local two-parameter exclusion. The
result is not a full collapsed-branch theorem and does not change canonical C-II
status.
