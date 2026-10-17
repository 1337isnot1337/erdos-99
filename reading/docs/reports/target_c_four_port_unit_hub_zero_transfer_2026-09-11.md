> Generated reading edition · [exact source](../../../docs/reports/target_c_four_port_unit_hub_zero_transfer_2026-09-11.md) · source SHA-256 `3307599923aba5ce06a38bf3a46a6941ce97f2831e90b3a460635272f7a03aaa`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8167410A5BFC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_four_port_unit_hub_zero_transfer_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=e4180e89491de8f56979ec3bb7359e2004952653; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — a four-port unit-contact hub has zero cross-transfer

**Date:** 2026-09-11  
**Repository state:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** C-II closing attempt / exact local response lemma  
**Target:** Target C, post-C-I common-block phase  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used for this lemma  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

The September 10 transfer theorem removes a positive contact bridge from the common
intersection of all positive-diameter routes. The remaining common object is one
2-edge-connected contact block. The existing weighted four-cycle regression shows that
block topology alone gives no sign for a cross-transfer entry of

`K=Q^T Lambda^+ Q`.

The precise closing implication that would be useful is:

```text
common unit-contact block + KKT equilibrium
    -> a response restriction incompatible with the diameter-thrackle identities
    -> exclusion of the common-block phase.
```

The theorem below proves this implication only for a four-cycle with four straight
one-terminal ports. It is a local restriction, not the required general block theorem.

## 2. Strongest genuinely new audited theorem

### Theorem — four-port unit-contact hub has zero cross-transfer

Let a positive contact network contain a unit rhombus

`p_0 p_1 p_2 p_3 p_0`,

with all four contact edges of length one. At each `p_i`, attach a straight contact
port of positive length `ell_i>0` ending at one terminal `t_i`. Assume:

1. each port is the only contact connection from its terminal to the rhombus;
2. the four ports contain no diameter-reaction vertex and carry their positive contact
   stress constantly along the port;
3. at each `p_i`, the only positive contact edges are the two rhombus sides and the
   first edge of its port, and `p_i` has no positive diameter reaction;
4. the only positive diameter reactions at these four terminals are the two cross-port
   pairs `t_0t_2` and `t_1t_3`, both of length `D`;
5. the terminal equilibrium equations use positive contact and diameter coefficients.

Then the four rhombus contact stresses are equal. In the contact Dirichlet response
on the terminals, with

`e=(t_2,t_0)` and `f=(t_3,t_1)`,

the cross-transfer is

```math
\boxed{K_{ef}=0.}
```

The response conclusion remains true if arbitrary positive contact subnetworks are
inserted at the four rhombus vertices, provided each has one terminal, no diameter
reaction away from that terminal, and the equal cycle conductances in (2.5) are
retained. This response-only extension does not assert that arbitrary subnetworks
preserve the KKT equal-stress conclusion.

### Scope

This is an exact finite unit-contact/KKT response statement. It applies to a special
four-port local normal form inside a common block. It is not a statement about an
arbitrary 2-edge-connected contact block, an arbitrary port network, or a global
minimizer. It does not count contact-isolated source points and does not supply global
optimality.

### Proof

Write the unit rhombus as

```math
p_0=0,
\quad p_1=u,
\quad p_3=v,
\quad p_2=u+v,
\qquad |u|=|v|=1.
```

Put

```math
d_+=|u+v|,
\quad a={u+v\over d_+},
\qquad
d_-=|v-u|,
\quad b={v-u\over d_-}.
```

The positive terminal equilibrium at `t_0` for the diameter `t_0t_2` forces the
terminal contact port and the diameter chord to be collinear. The same holds at
`t_2`; likewise for `t_1,t_3`. Since the two endpoints of each port are joined by a
diameter chord, the port geometry has the form

```math
t_0=p_0-\ell_0a,
\quad t_2=p_2+\ell_2a,
\qquad
t_1=p_1-\ell_1b,
\quad t_3=p_3+\ell_3b.
\tag{2.1}
```

The signs in (2.1) are forced by positive equilibrium at the rhombus vertices: the
port force must lie in the positive cone of the two rhombus contact forces there.
The diameter lengths are then `d_++ell_0+ell_2` and `d_-+ell_1+ell_3`; their equality
is not needed below.

Let `alpha_01,alpha_12,alpha_23,alpha_30` be the positive contact stresses on the
rhombus sides, and let `tau_i` be the constant positive contact stress in port `i`.
At `p_0`, contact equilibrium is

```math
-\alpha_{01}u-\alpha_{30}v+\tau_0a=0.
```

Since `a=(u+v)/d_+` and `u,v` are linearly independent unless the rhombus is
degenerate, this gives

```math
\alpha_{01}=\alpha_{30}={\tau_0\over d_+}.
\tag{2.2}
```

At `p_1`, the equation is

```math
\alpha_{01}u-alpha_{12}v+\tau_1b=0,
```

so

```math
\alpha_{01}=\alpha_{12}={\tau_1\over d_-}.
\tag{2.3}
```

At `p_2` and `p_3` the same calculation gives

```math
\alpha_{12}=\alpha_{23}={\tau_2\over d_+},
\qquad
\alpha_{23}=\alpha_{30}={\tau_3\over d_-}.
\tag{2.4}
```

Equations (2.2)--(2.4) prove

```math
\boxed{\alpha_{01}=\alpha_{12}=\alpha_{23}=\alpha_{30}=:\alpha.}
\tag{2.5}
```

Now compute the contact response. In the unit-current problem with source `+1` at
`t_3` and sink `-1` at `t_1`, the ports at `t_0` and `t_2` carry zero current,
because each is a one-terminal tree attached to the rest of the network at one
vertex. Thus the voltage difference `V(t_2)-V(t_0)` is the same as
`V(p_2)-V(p_0)`.

By (2.5), every rhombus edge has resistance `r=1/alpha`. The current from `p_3` to
`p_1` splits equally between the two two-edge paths through `p_0` and `p_2`. Set
`V(p_1)=0`. Each path carries current `1/2`, so

```math
V(p_0)=r/2=V(p_2).
```

Therefore

```math
K_{ef}=V(t_2)-V(t_0)=V(p_2)-V(p_0)=0.
```

The response part of the conclusion also holds if one-terminal positive contact
subnetworks are attached at the four rhombus vertices, provided the equal cycle
conductances in (2.5) are retained. In the cross-transfer problem, the two unused
subnetworks carry zero current, and the source and sink subnetworks inject `+1` and
`-1` at their rhombus attachment vertices. This is only a response observation:
arbitrary subnetwork geometry does not by itself preserve the KKT equal-stress
conclusion, so it is not being asserted as a broader unit-contact theorem.
$`\square`$

## 3. Exact target implication

The arbitrary weighted four-cycle sign formula in
`target_c_common_hub_transfer_regression_2026-09-11.md` cannot be realized by this
special unit-contact/KKT four-port normal form: its four contact conductances are
forced equal, and the cross-transfer is zero rather than positive or negative.

This removes one local response degree of freedom, but `K_{ef}=0` is compatible with
the promoted C53 conclusion

`min_{e ne f} K_{ef} <= 0`.

It therefore does not produce a contradiction. The theorem says only that a proposed
strictly negative four-port transfer must use a more complicated block, a port with
additional reactions/branches, or a geometry outside this local normal form.

## 4. Exact remaining lemma

The needed global replacement is:

> **Common-block response lemma.** For the actual positive unit-contact KKT network,
> a common 2-edge-connected block carrying all positive-diameter route intersections
> must either contain a four-port substructure of the theorem in a way that controls
> all cross-transfers, or pay a quantitative `e_BB`, `s_C`, or `3d_H` surplus large
> enough to contradict the `s_Z=0`/`s_Z>0` ledgers.

The present theorem does not prove the required substructure or the surplus estimate.

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| A common positive bridge gives positive cross-transfer | already proved | The unique bridge carries one forced unit of current. |
| A common 2-edge-connected block gives positive cross-transfer | rejected | The weighted four-cycle has either sign. |
| Unit-contact four-port rhombus with straight ports gives zero cross-transfer | proved here | The stated incident-edge and KKT hypotheses force equal rhombus stresses, then the response calculation is exact. |
| This four-port lemma excludes every common block | rejected | General blocks can have more ports, branches, and internal reactions. |
| C-II is closed after the common-bridge exclusion | rejected | The general common block and isolated source points remain. |

## 6. Regression tests

| Regression | Result | Exact reason |
| --- | --- | --- |
| Weighted four-cycle `(a,b,c,d)=(2,1,2,1)` | survives as a general-network regression | It is outside the unit-contact/KKT four-port hypotheses. |
| Unit square | passes | It is the equal-stress case and has zero cross-transfer. |
| Non-square unit rhombus | passes | The port stresses change with `d_+` and `d_-`, but the four cycle stresses remain equal under the stated incident-edge hypotheses. |
| Contact-isolated source points | untouched | The theorem concerns only the local positive response network. |
| Regular odd shell | untouched | No global shell or optimality assertion is used. |

## 7. Failed routes and no-go result

The attempted route was

```text
common 2-connected block -> choose a negative cross-transfer -> C53 contradiction.
```

The existing weighted four-cycle kills this route for arbitrary response networks.
The new calculation shows that unit-contact/KKT geometry repairs the sign only in a
special four-port normal form, and repairs it to equality, not to the strict sign
needed for contradiction. The general multiport route remains open.

## 8. Literature imported

None.

## 9. Computation and reproducibility

No computation is required. The proof is an exact vector-equilibrium and two-path
Ohm-law calculation.

## 10. Canonical promotion recommendation

**Hold as report.** The lemma is proved, but its hypotheses are too narrow to change
the authoritative C-II route map. The report should not be promoted as a general
common-block theorem.

## 11. Next run

The highest-value next theorem is a port-count or internal-reaction inequality for a
general unit-contact block. It must retain the actual port geometry and prove either a
signed response restriction or a quantitative surplus charge. The four-port lemma is
only a base case for that classification.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New proved local lemma:
  A unit rhombic contact 4-cycle with four straight one-terminal positive ports and
  cross-port diameters forces all four cycle contact stresses equal. In the terminal
  response, K_(t2,t0),(t3,t1)=0. One-terminal positive trees along the ports do not
  change this cross-transfer.

Target effect:
  The arbitrary weighted 4-cycle sign regression cannot be realized in this special
  unit-contact/KKT normal form, but zero transfer is compatible with C53. The common
  2-connected hub with general ports/internal reactions remains open.

Binding regressions/no-go:
  General weighted 4-cycle permits either transfer sign; common-block topology alone
  cannot replace the single-bridge maximum-principle argument.

Highest-value next lemma:
  A general unit-contact common-block port-response or surplus inequality.

Authoritative files:
  docs/targets/target-c/56-ci-restored-frontier.md
  docs/reports/target_c_common_bridge_transfer_exclusion_2026-09-10.md
  docs/reports/target_c_common_hub_transfer_regression_2026-09-11.md
  docs/reports/target_c_woodall_diameter_topology_2026-09-10.md
```
