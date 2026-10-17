> Generated reading edition · [exact source](../../../docs/reports/target_c_post_zf_missing_hull_side_equilibrium_2026-09-09.md) · source SHA-256 `17e50995b5e9361f655f4e2b65f56bdee44405e283b358efae78eb4f303421d9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-DA00642502F7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — missing hull sides force non-hull contact incidence

**Date:** 2026-09-09  
**Repository base:** PR #118 after primitive boundary normal form  
**Run type:** exact local equilibrium / primitive-endpoint exclusion  
**Target:** Target C, C-II after ZF  
**Depends on:** full-support relative-interior KKT stress in C-II, loaded force-hull geometry, LH/PN notation  
**External web search:** not used in the proof  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The primitive normal form left one non-cyclic endpoint at `m+k=2`:

```math
\text{PN-E1:}\qquad
m=1,\quad k=1,\quad C=P_q,
```

an all-loaded convex unit contact path with one nonunit closing hull side.

This report excludes PN-E1 exactly. The local reason is stronger and applies throughout the post-ZF branch:

> a loaded convex-hull vertex incident to a unit hull-side contact cannot have that side as its only contact.

Consequently, if `m` force-hull sides are nonunit and these missing sides occur in `r_m` cyclic runs, then

```math
\boxed{
e_{BI}+2c_B\ge m+r_m.}
\tag{ME.1}
```

Here `c_B` is the LH/PN count of loaded-loaded contacts beyond the unit force-hull sides. Equation ME.1 says every loaded vertex touched by a missing unit hull side consumes at least one non-hull contact incidence.

---

## 1. Local tangent-force obstruction

Let `b,c` be consecutive loaded vertices of the convex force hull `F`, and suppose

```math
|b-c|=1.
```

Then `bc` is a positive unit contact in the full-support C-II stress.

Let `n` be an inward normal to the supporting line through the hull side `bc`, chosen so

```math
n\cdot(x-b)>0
```

for every loaded hull vertex `x` other than `b,c`.

Such strictness holds because `B=Vert(F)` and `bc` is a side of the convex polygon `F`.

Assume for contradiction that `bc` is the only contact incident to `b`. KKT equilibrium at `b` is

```math
\alpha_{bc}(b-c)
=
\sum_{bk\in H}\beta_{bk}(b-k).
\tag{1.1}
```

Every coefficient in the relative-interior C-II stress is positive on every actual diameter edge. Since `D>1`, the contact neighbor `c` is not a diameter partner of `b`. Therefore every diameter partner `k` is a loaded hull vertex distinct from `b,c`, and

```math
n\cdot(k-b)>0.
```

Hence

```math
n\cdot(b-k)<0
\qquad(bk\in H).
\tag{1.2}
```

Taking the dot product of (1.1) with `n`, the left side is zero because `bc` lies on the supporting line, while the right side is strictly negative. Contradiction.

Thus:

### Lemma ME.1 — no sole hull-side contact at a loaded vertex

If a loaded vertex is incident to a unit force-hull side, then it has at least one additional unit contact.

No angle estimate, degree cap, response theorem, or asymptotic argument is used.

---

## 2. Missing-side run count

On the cyclic loaded force hull, mark the `m` sides whose Euclidean length is greater than one. These are exactly the hull sides that are not unit contacts.

Assume `0<m<q`, and let `r_m` be the number of cyclic connected runs of marked sides. The set of loaded vertices incident to at least one marked side has cardinality

```math
\boxed{|S_m|=m+r_m.}
\tag{2.1}
```

Indeed a run of `\ell` consecutive missing sides has `\ell+1` distinct incident vertices, and distinct runs have disjoint incident vertex sets.

For every `b in S_m`, at most one of its two force-hull sides is a unit contact if `b` lies inside a run, and exactly one is a unit contact if `b` is an endpoint of a run.

- If exactly one hull-side contact is present, Lemma ME.1 forces another contact not belonging to the unit hull-side cycle.
- If neither hull side is a contact, positive diameter loading and KKT equilibrium already force positive contact degree, so again at least one non-hull contact is incident to `b`.

Thus every vertex in `S_m` has at least one non-hull contact incidence.

The non-hull contacts incident to loaded vertices are precisely:

1. loaded-interior contacts, counted once by `e_BI` at their loaded endpoint;
2. extra loaded-loaded contacts beyond the unit hull sides, counted twice in loaded incidences by `c_B`.

Therefore

```math
\boxed{e_{BI}+2c_B\ge |S_m|=m+r_m.}
```

This proves ME.1. `square`

The case `m=q` cannot occur in the connected positive contact core without non-hull contacts; the same incidence conclusion may be written with `|S_m|=q`, but the run convention above is intended for the post-ZF regime where at least one unit hull side is present.

---

## 3. Primitive-normal-form consequence

PN gives

```math
c_I+s_C+c_B=m+k-2.
\tag{3.1}
```

It also gives the exact component boundary-contact count

```math
e_{BI}
=\sum_r\delta_r+3c_I+s_C+R_I,
\tag{3.2}
```

because each unloaded component satisfies

```math
t_r=\delta_r+3+s_r+r_r.
```

Insert (3.2) into ME.1:

```math
\sum_r\delta_r+3c_I+s_C+R_I+2c_B
\ge m+r_m.
\tag{3.3}
```

Use (3.1) once to isolate the run count:

```math
\boxed{
 r_m
\le
\sum_r\delta_r+R_I+(k-2)+2c_I+c_B.}
\tag{ME.2}
```

Thus many separated runs of missing unit hull sides require component diameter, internal Eppstein slack, mixed/diameter defect, or additional interior/chord structure. Missing sides cannot appear as mechanically isolated one-gap defects for free.

---

## 4. Exact exclusion of PN-E1

PN-E1 has

```math
m=1,
\qquad
k=1,
\qquad
c_I=s_C=c_B=0.
```

Its positive contact core is the convex path

```math
b_1b_2\cdots b_q
```

with every displayed edge a unit hull-side contact and the closing hull side `b_qb_1` nonunit.

The two path endpoints `b_1,b_q` each have exactly one contact, and that contact is a unit force-hull side. Lemma ME.1 excludes either endpoint immediately.

Equivalently, ME.1 has `m=r_m=1` and `e_BI=c_B=0`, giving

```math
0\ge2,
```

a contradiction.

Therefore:

### Theorem ME — one-gap primitive endpoint excluded

```math
\boxed{\text{PN-E1 does not occur in C-II for }D>1.}
\tag{ME.3}
```

Combined with PN, the exact primitive floor `m+k=2` now has only one surviving form:

```math
\boxed{
m=0,\quad k=2,\quad C=C_q.}
\tag{ME.4}
```

That survivor is the all-loaded unit convex contact cycle, including the regular odd-shell regression.

---

## 5. Strengthened primitive floor when a hull side is missing

PN proved `m+k>=2`. ME eliminates the only `m>0` equality case. Hence:

### Corollary ME.2

If at least one loaded force-hull side is nonunit, then

```math
\boxed{m+d_H+s_Z\ge3.}
\tag{ME.5}
```

At equality `m+k=3`, PN says exactly one of `c_I,s_C,c_B` equals one. ME.1 further removes some run patterns:

- if `m=1,k=2`, then `r_m=1` and the sole primitive defect on the left of PN.4 must provide enough non-hull incidence at both endpoints of the missing side;
- if `m=2,k=1`, two separated missing sides (`r_m=2`) demand four loaded non-hull incidences and are much more restrictive than one consecutive two-side run (`r_m=1`).

This turns the first stability layer above the cyclic endpoint into a finite mechanical case split.

---

## 6. Relation to the high-`x_B` branch

LH showed

```math
x_B=m+u_B.
```

ME separates two ways for outer-walk excess to be large:

1. `m` large: many actual force-hull sides are nonunit, and ME.1 forces a corresponding population of non-hull loaded contact incidences;
2. `u_B` large: the excess comes from deeper/repeated outer-face detours rather than additional missing unit hull sides.

Thus the high-`x_B` branch is no longer a single undifferentiated boundary phenomenon. A large `m` branch is mechanically coupled to `e_BI+2c_B`; a large `u_B` branch should be attacked by bridge/articulation and train-end stability.

---

## 7. Regression audit

### Regular odd shell

`m=0`; ME.1 is vacuous. The shell remains allowed.

### Unit square

Again `m=0`; no conflict.

### One-gap path

Excluded exactly, as intended.

### Two-edge detour through an unloaded vertex

One nonunit hull side can be replaced by two unit contacts through an unloaded vertex. Then `m=r_m=1` and the two loaded endpoints each already have one non-hull loaded-interior contact, so `e_BI>=2`; ME.1 is satisfied. The theorem does not falsely exclude this local geometry.

### Extra loaded chord

A loaded chord joining the two endpoints of distinct missing-side incidences contributes two units through `2c_B`, exactly matching the incidence count. No assumption that every extra contact enters the unloaded interior is made.

---

## 8. Next theorem

After ME, the primitive endpoint problem is reduced to the cyclic survivor

```math
m=0,\qquad k=2,\qquad C=C_q.
```

The high-`x_B` branch splits into:

- `m=Omega(D)`, which by ME.1 forces `e_BI+2c_B=Omega(D)`;
- `u_B=Omega(D)`, which represents deep outer detours / repeated outer-face topology.

The next useful exact result is a stability version of ME.1 that charges `u_B` to bridge or articulation structure, or a global exclusion of the all-loaded cyclic contact core for sufficiently large minimizers.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.**

The local equilibrium lemma is elementary; the post-ZF consequences depend on the report-level PN/LH/ZU normalization.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Local lemma:
At a loaded convex-hull vertex b, a unit hull-side contact bc cannot be the only
contact at b. Dot KKT equilibrium with the inward normal to side bc. The sole
contact force has zero normal component, while every positive diameter reaction
has the same strict nonzero normal sign. Contradiction.

Let m be the number of nonunit loaded hull sides and r_m their number of cyclic runs.
Exactly m+r_m loaded vertices touch a missing side. Every one needs a non-hull contact,
so
    e_BI+2c_B >= m+r_m.

Using PN component notation:
    r_m <= sum delta_r + R_I + (k-2) + 2c_I + c_B.

PN-E1 had m=1,k=1,c_I=s_C=c_B=0 and C=P_q. Its two endpoints have sole hull-side
contacts, so it is impossible.

Therefore the primitive equality m+k=2 has only
    m=0,k=2,C=C_q.
If m>0, then m+d_H+s_Z>=3.

Next: cyclic endpoint exclusion, or stability charging u_B=x_B-m to bridge/articulation
structure.
```
