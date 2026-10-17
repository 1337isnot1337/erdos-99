> Generated reading edition · [exact source](../../../docs/reports/target_c_minimal_interface_annular_saturation_2026-09-09.md) · source SHA-256 `d9b6070dfdb0cdb9ef4c59d9e141a61a55b16216bda2d10476b5ca0aba3aefff`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 24 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-913A612A65DB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_minimal_interface_annular_saturation_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=83173ba967a45f3ec94617b3d80eac191a2a4073; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — minimal loaded-interface defect forces annular contact saturation

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** exact face-incidence equality classification  
**Target:** full-core near-circle endpoint with `Q_B/D->2`  
**Depends on:** GP/FS, NC, HBd, NBd, C35 loaded degree cap, C51 bounded-face simplicity/convexity  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

FS proves that the minimum possible loaded-interface defect is

```math
Q_B=(2+o(1))D.
```

At that minimum the interface incidence ledger itself saturates. Let `F_B` be the number of **all** bounded full-contact faces incident to at least one loaded terminal, including quadrilateral faces. Then

```math
\boxed{
F_B=(\pi+o(1))D,
}
\tag{AS.1}
```

```math
\boxed{
e_{BI}=(\pi+o(1))D,
\qquad s_B=o(D),
}
\tag{AS.2}
```

and

```math
\boxed{
\sum_r k_r=(\pi+2+o(1))D.
}
\tag{AS.3}
```

Consequently:

1. all but `o(D)` loaded hull vertices have exactly the two consecutive loaded-loaded hull contacts and exactly one loaded-to-interior contact;
2. all but `o(D)` bounded faces touching loaded terminals contain exactly two loaded vertices and exactly one loaded-loaded hull side;
3. those two loaded vertices are consecutive on the force hull;
4. across every such regular interface face, the unique interior neighbors of its two loaded endpoints belong to the same harmonic component;
5. therefore the harmonic-component label of the interior neighbor changes on only `o(D)` edges of the loaded hull cycle.

Thus the minimum-interface endpoint is an almost everywhere one-spoke-per-terminal annular strip. The two dominant half-disk harmonic carriers from FS/HG occupy long cyclic attachment blocks, and all serious topology is confined to `o(D)` transition locations. Those transition locations may still support macroscopic exceptional faces, so this is not yet a contradiction.

---

## 1. Exact full-versus-internal face count

Let

- `e_BB` be the loaded-loaded contact count;
- `e_BI` the loaded-to-unloaded contact count;
- `e_II=sum_r e_r` the contact edges internal to the unloaded components;
- `b` the full outer contact-face walk length;
- `F_int` the number of bounded faces containing no loaded terminal;
- `F_B` the number of bounded faces containing at least one loaded terminal;
- `Q_int=sum_r Q_r` the total internal bounded-face degree excess;
- `Q_B=Q-Q_int` the loaded-interface excess;
- `k_r` the outer-face walk length of `C[I_r]`.

For the full plane contact graph,

```math
2(e_{II}+e_{BI}+e_{BB})
=b+4(F_{int}+F_B)+Q_{int}+Q_B.
\tag{1.1}
```

Summing face incidence inside all unloaded components gives

```math
2e_{II}
=\sum_r k_r+4F_{int}+Q_{int}.
\tag{1.2}
```

Subtract (1.2) from (1.1):

```math
\boxed{
4F_B
=2(e_{BB}+e_{BI})-b-Q_B+\sum_rk_r.
}
\tag{AS.4}
```

This is an exact finite identity. It is the face-count counterpart of the stopped-train difference identity.

---

## 2. Loaded-face incidence upper bound

Call a loaded terminal `b in B` **regular** if both adjacent force-hull sides are actual direct loaded-loaded unit contacts. NC gives

```math
e_{BB}=q-o(D),
```

and the missing direct hull sides are `o(D)`. Hence all but `o(D)` loaded terminals are regular.

At a regular loaded terminal, C35 gives contact degree at most three. The two hull contacts are already present, so there is at most one loaded-to-interior contact.

In the cyclic order of edges around such a terminal:

- if there is no interior contact, there is exactly one bounded face sector between the two hull edges;
- if there is one interior contact, there are exactly two bounded face sectors, one on each side of that interior edge.

Thus a regular loaded terminal contributes exactly

```math
1+d_{BI}(b)
```

incidences to bounded faces. The `o(D)` irregular loaded terminals have bounded degree and contribute only `o(D)` incidences in total.

Let

```math
I_B:=\sum_{F\in\mathcal F_B}|V(F)\cap B|.
```

C51 makes every bounded face boundary a simple cycle, so this is ordinary vertex-face incidence without repeated boundary vertices. Summing over loaded terminals gives

```math
\boxed{
I_B=q+e_{BI}+o(D).
}
\tag{2.1}
```

Every bounded face containing a regular loaded terminal also contains one of that terminal's loaded hull neighbors, because every bounded sector at a regular terminal is incident to a hull edge. A face whose loaded vertices are all irregular uses at least one of only `o(D)` bounded-degree irregular terminals, so there are only `o(D)` such faces.

Therefore all but `o(D)` faces in `F_B` contain at least two loaded vertices, and

```math
I_B\ge2F_B-o(D).
```

Using (2.1),

```math
\boxed{
F_B\le\frac{q+e_{BI}}2+o(D).
}
\tag{AS.5}
```

---

## 3. Minimal interface defect forces equality

Assume now

```math
Q_B=(2+o(1))D.
\tag{3.1}
```

FS/GP gives the attachment-cell perimeter equality and hence

```math
\sum_rk_r\ge(\pi+2-o(1))D.
\tag{3.2}
```

NC and the near-circle endpoint give

```math
e_{BB}=q+o(D),
\qquad
b=q+o(D),
\qquad
q=(\pi+o(1))D.
\tag{3.3}
```

Insert (3.1)--(3.3) into the exact face-count identity AS.4:

```math
\begin{aligned}
4F_B
&=2(q+e_{BI})-q-2D+\sum_rk_r+o(D)\\
&\ge2(q+e_{BI})+o(D).
\end{aligned}
```

Hence

```math
F_B\ge\frac{q+e_{BI}}2-o(D).
\tag{3.4}
```

Together with AS.5,

```math
\boxed{
F_B=\frac{q+e_{BI}}2+o(D).
}
\tag{3.5}
```

Returning to AS.4, equality in (3.5) forces equality in (3.2):

```math
\boxed{
\sum_rk_r=q+Q_B+o(D)
=(\pi+2+o(1))D.
}
```

This proves AS.3.

It also forces

```math
\boxed{I_B=2F_B+o(D).}
\tag{3.6}
```

Thus the total loaded-vertex incidence excess above two per interface face is sublinear.

---

## 4. Almost every interface face contains one shell edge

A direct loaded-loaded hull side that is a contact bridge can be incident to the outer face on both sides. Each such bridge creates an additional occurrence in the outer contact-face walk, so the number of bridged hull contacts is at most `x_B=o(D)`.

Therefore

```math
q-o(D)
```

loaded-loaded hull sides are each incident to a bounded face in `F_B`.

For a bounded interface face `F`, let `m_F` be the number of those regular loaded-loaded hull sides on its boundary. Then

```math
\sum_{F\in\mathcal F_B}m_F=q-o(D).
\tag{4.1}
```

Every face with `m_F>0` contains all endpoints of its shell-edge blocks. Unless a face contains the whole hull cycle, which is impossible in the present full-core phase, `m_F` shell edges on a cycle use at least `m_F+1` distinct loaded vertices. Hence

```math
|V(F)\cap B|-2\ge m_F-1
\qquad(m_F>0).
\tag{4.2}
```

Faces with `m_F=0` can contain only irregular loaded terminals except for `o(D)` incidence errors from missing hull contacts. Since the irregular loaded set has total bounded-face incidence `o(D)`, the number of `m_F=0` interface faces is `o(D)`.

Sum (4.2) and use (3.6). The possible negative contribution from the `o(D)` one-loaded exceptional faces is itself `o(D)`. Thus

```math
\sum_{m_F>0}(m_F-1)=o(D).
\tag{4.3}
```

Equations (4.1) and (4.3) imply

```math
F_B=q+o(D).
\tag{4.4}
```

Combining this with (3.5),

```math
\boxed{e_{BI}=q+o(D)=(\pi+o(1))D.}
```

The loaded-degree identity

```math
s_B=3q-e_{BI}-2e_{BB}
```

and `e_BB=q+o(D)` therefore give

```math
\boxed{s_B=o(D).}
```

This proves AS.1-AS.2.

---

## 5. Terminal and face saturation

All but `o(D)` loaded terminals are regular, so they have at most one interior contact. Since

```math
e_{BI}=q+o(D),
```

all but `o(D)` regular loaded terminals must actually have one such contact.

Therefore all but `o(D)` loaded terminals have contact degree exactly three:

```math
\boxed{
\deg_C(b)=3,
}
```

with

- one unit contact to the previous loaded hull vertex;
- one unit contact to the next loaded hull vertex;
- one unit contact to a unique unloaded neighbor `u_b`.

Similarly, (3.6) implies that only `o(D)` interface faces have more than two loaded vertices, while Section 4 shows only `o(D)` have no regular shell edge or more than one regular shell edge.

Thus all but `o(D)` interface faces have exactly

```math
\boxed{
|V(F)\cap B|=2,
\qquad
m_F=1.
}
\tag{5.1}
```

The two loaded vertices must be the endpoints of that unique shell edge, hence are consecutive on the loaded force hull.

---

## 6. Regular interface face structure

Take a face satisfying (5.1) whose two loaded endpoints `b_i,b_{i+1}` are terminal-saturated as in Section 5. Let their unique unloaded neighbors be `u_i,u_{i+1}`.

At `b_i`, the bounded face on the interior side of the shell edge `b_i b_{i+1}` must leave along the unique interior contact `b_i u_i`. Likewise at `b_{i+1}` it enters along `u_{i+1}b_{i+1}`.

All other face vertices are unloaded. Therefore the remaining part of the simple face cycle is a contact path inside the unloaded graph from `u_i` to `u_{i+1}`. In particular those two vertices belong to the same component `I_r`.

If that internal path has `L_i` contact edges, then the full face degree is

```math
k_F=L_i+3.
\tag{6.1}
```

Triangle-freeness rules out `L_i=0`: if `u_i=u_{i+1}`, the three unit contacts to `b_i,b_{i+1}` form a unit triangle. Hence `L_i>=1`.

The face defect is therefore exactly

```math
\boxed{
Q_F=k_F-4=L_i-1.
}
\tag{6.2}
```

The quadrilateral case is precisely `L_i=1`; every exceptional regular annular face measures the excess length of its internal boundary path above the single-edge baseline.

---

## 7. Component labels change only at sublinearly many shell edges

For every terminal-saturated loaded vertex `b_i`, let `r(i)` be the harmonic component containing its unique unloaded neighbor `u_i`.

Section 6 shows that across every regular interface shell edge

```math
r(i)=r(i+1).
```

Only `o(D)` shell edges fail the regularity hypotheses. Therefore

```math
\boxed{
\#\{i:r(i)\ne r(i+1)\}=o(D).
}
\tag{7.1}
```

Thus the cyclic terminal attachment sequence consists of only `o(D)` component-label transition locations.

FS already proves that in the minimum-interface regime there are two individual harmonic components carrying `(Delta/2+o(1))D^2` vertices and attachment hulls converging to complementary semicircles. AS shows that these carriers are not attached through a diffuse alternating boundary pattern: away from `o(D)` transition locations, each occupies long consecutive terminal runs.

---

## 8. Exact stopped-train companion identity

Let `T` be the stopped-train count of the full contact graph and `T_r` that of `C[I_r]`. DT gives

```math
2T=b+Q+4f,
```

and componentwise

```math
2T_r=k_r+Q_r+4f_r.
```

Subtracting internal from global quantities gives

```math
\boxed{
T-\sum_rT_r
=\frac{b+Q_B-\sum_rk_r}{2}+2f_B,
}
\tag{8.1}
```

where `f_B` counts nonquadrilateral bounded faces touching loaded terminals.

Under the minimum-interface equalities

```math
b=q+o(D),
\quad
Q_B=2D+o(D),
\quad
\sum_rk_r=q+2D+o(D),
```

this collapses to

```math
\boxed{
T-\sum_rT_r=2f_B+o(D).
}
\tag{8.2}
```

Thus, after annular saturation, the only leading discrepancy between global and internal train systems is the number of exceptional loaded-interface faces themselves. Their degree excess has already been absorbed into the equality geometry.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| exact face-count identity AS.4 | proved | subtract full and component face incidence |
| loaded incidence upper bound AS.5 | proved asymptotically | all but `o(D)` terminals have two hull contacts and degree at most three |
| `sum k_r=(pi+2)D+o(D)` | proved under `Q_B/D->2` | AS.4 squeezed by AS.5 and GP lower bound |
| `F_B~q`, `e_BI~q`, `s_B=o(D)` | proved | shell-edge incidence equality |
| almost every interface face has two consecutive loaded endpoints and one shell side | proved | equality in loaded/shell incidence |
| component label changes only `o(D)` times | proved | regular face internal path connects unique interior neighbors |
| exactly two transition locations | not proved | sublinear transitions may remain |
| Level I | still open | defect may concentrate at transition faces or in long annular paths |

---

## 10. Next target

The minimum-interface endpoint is now much more rigid:

```text
outer loaded cycle: q=(pi+o(1))D unit contacts
almost every loaded vertex: exactly one interior spoke
almost every bounded loaded face: one shell side + two spokes + one internal component path
almost every shell edge preserves the harmonic-component label
sum component outer-walk length: (pi+2+o(1))D
Q_B=(2+o(1))D
only o(D) component-label transition locations
```

There are two remaining ways to place the `2D` interface defect:

1. spread it through the regular annular faces as excess internal path length `L_i-1`;
2. concentrate it at the `o(D)` transition faces, which MF shows become doubled near-geodesic segments if macroscopic.

A closing theorem should show that the two half-disk carrier outer boundaries already require the full additional `2D` length on the non-annular diameter sides. If so, the annular faces have only `o(D)` defect available and the complete `2D` obligation is forced into the transition region, reducing the equality endpoint to one or a few near-geodesic separator faces.
