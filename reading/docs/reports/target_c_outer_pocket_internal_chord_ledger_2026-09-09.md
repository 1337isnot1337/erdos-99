> Generated reading edition · [exact source](../../../docs/reports/target_c_outer_pocket_internal_chord_ledger_2026-09-09.md) · source SHA-256 `c2581470e23c540c780b75000d42e62af3a37a5e021f9fd9a16698d8492a70e1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7FB5DD765A26","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact outer-pocket / internal-loaded-chord ledger

**Date:** 2026-09-09  
**Repository base:** `6ed9d78ae146b68fd9b14c3c3486b048f3d59074`  
**Run type:** exact post-ZF cross-ledger reduction  
**Target:** Target C C-II after ZF / loaded-boundary capacity  
**Depends on:** OP outer-pocket augmentation, ZT terminal partition, ZU pinned-contact ledger  
**LEVEL I STATUS:** STILL OPEN

This note removes two pieces of slack left implicit in the post-ZF boundary bookkeeping.  It separates loaded-loaded contacts into actual force-hull sides and non-hull chords, and separates outer-walk excess into the number of convex outer pockets and the excess combinatorial size of those pockets.

The result is an exact four-currency ledger.  In particular, the earlier HB inequality

$$
e_{BB}\ge Q+2(d_H+s_Z)
$$

has an exact remainder:

$$
\boxed{
e_{BB}-Q-2(d_H+s_Z)
=d_P+c_B,
}
$$

where `d_P` is the total excess of outer-pocket degrees above triangles and `c_B` is the number of loaded-loaded unit contacts that are not force-hull sides.

No area lower bound per pocket is used or claimed.

---

## 1. Definitions

Use the post-ZF notation

- `q=|B_+|` for loaded force-hull vertices;
- `b` for the outer contact-face boundary-walk length;
- `x_B=b-q`;
- `Q=sum_F(deg F-4)=f+g_F` over bounded nonquadrilateral contact faces;
- `d_H=q-h`;
- `s_Z=e+h-(2v-2)`;
- `k:=d_H+s_Z`;
- `c_I` for the number of unloaded contact components;
- `e_BB` for all loaded-loaded unit contacts;
- `s_C` for the pinned-contact stress surplus.

OP augments the positive contact graph by every missing force-hull side.  Let

$$
\boxed{a:=\#\{\text{force-hull sides that are not unit-contact edges}\}.}
\tag{1.1}
$$

OP proves that the augmentation creates exactly `a` convex outer pockets.  Let their graph-boundary lengths be `k_P`.  Define

$$
\boxed{
d_P:=\sum_P(k_P-3)\ge0.}
\tag{1.2}
$$

Thus `d_P=0` iff every outer pocket is triangular.

There are exactly `q-a` force-hull sides that already are contact edges.  Each has both endpoints in `B_+`.  Define the remaining loaded-loaded contact count

$$
\boxed{
c_B:=e_{BB}-(q-a)\ge0.}
\tag{1.3}
$$

So `c_B` counts precisely the loaded-loaded unit contacts that are not force-hull sides.

---

## 2. OP resolves the outer-walk excess exactly

OP proves

$$
\sum_P k_P=b+2a-q.
\tag{2.1}
$$

Since the number of pockets is `a`,

$$
\begin{aligned}
d_P
&=\sum_P(k_P-3)\\
&=b+2a-q-3a\\
&=b-q-a\\
&=x_B-a.
\end{aligned}
$$

Hence

$$
\boxed{x_B=a+d_P.}
\tag{2.2}
$$

This is stronger than the earlier observation `a<=x_B`: every unit of outer-walk excess not creating a new pocket is exactly a unit of outer-pocket degree above three.

---

## 3. Exact terminal and loaded-contact formulas

ZT gives

$$
q=x_B+Q+2(d_H+s_Z)=x_B+Q+2k.
\tag{3.1}
$$

Insert (2.2):

### Theorem PC.1 — terminal partition by outer pockets

$$
\boxed{
q=a+d_P+Q+2k.
}
\tag{PC.1}
$$

Now (1.3) gives

$$
e_{BB}=q-a+c_B.
\tag{3.2}
$$

Use PC.1:

### Theorem PC.2 — exact HB remainder

$$
\boxed{
e_{BB}=d_P+Q+2k+c_B.
}
\tag{PC.2}
$$

Equivalently,

$$
\boxed{
e_{BB}-\bigl(Q+2d_H+2s_Z\bigr)=d_P+c_B.
}
\tag{PC.3}
$$

Thus the HB inequality

$$
e_{BB}\ge Q+2d_H+2s_Z
$$

is equality exactly when

1. every convex outer pocket is triangular (`d_P=0`), and
2. every loaded-loaded unit contact is a force-hull side (`c_B=0`).

There is no additional hidden slack.

---

## 4. Pockets versus unloaded/pinned structure

ZU gives

$$
c_I+e_{BB}+s_C=q-2+k.
\tag{4.1}
$$

Insert `e_BB=q-a+c_B` and cancel `q`:

### Theorem PC.3 — outer-pocket balance

$$
\boxed{
a+k=c_I+c_B+s_C+2.
}
\tag{PC.4}
$$

Equivalently,

$$
\boxed{
a=c_I+c_B+s_C+2-d_H-s_Z.
}
\tag{PC.5}
$$

and

$$
\boxed{
q-e_{BB}=a-c_B=c_I+s_C+2-k.
}
\tag{PC.6}
$$

This identity is useful because `a` is a genuine count of pairwise interior-disjoint convex outer pockets, whereas `x_B` was only a boundary-walk excess with repeated edge occurrences allowed.

A large pocket count is therefore not an independent escape: apart from the two Euler units, it is paid by unloaded components, non-hull loaded chords, pinned-contact stress surplus, and the opposite-sign mixed/diameter defect `k`.

---

## 5. Train count in the new currencies

DT and ZE give

$$
T=\frac{b+Q}{2}+2f=h-s_Z+2f=q-k+2f.
\tag{5.1}
$$

Use PC.1 and `Q=f+g_F`:

$$
\boxed{
T=a+d_P+3f+g_F+k.
}
\tag{PC.7}
$$

NM proves

$$
T-2\le2x_B+5f+g_F.
\tag{5.2}
$$

Substitute `x_B=a+d_P` and PC.7.  After cancellation,

$$
\boxed{
k\le a+d_P+2f+2.
}
\tag{PC.8}
$$

Combining with PC.4 gives the equivalent structural bound

$$
\boxed{
c_I+c_B+s_C\le2a+d_P+2f.
}
\tag{PC.9}
$$

This is only a repackaging of NM plus the exact new ledger, but it identifies which geometric boundary objects must pay for a large pinned/interior surplus.

---

## 6. Consequences and branch reductions

### 6.1 Loaded contacts and pocket count cannot both be small

From `e_BB=q-a+c_B`,

$$
\boxed{a+e_{BB}=q+c_B\ge q.}
\tag{6.1}
$$

Thus the old OP/HB dichotomy is exact up to the explicitly named non-hull chord count `c_B`.

DB gives asymptotically

$$
q\ge h\ge(2\rho-o(1))D,
\qquad \rho=0.7390851332\ldots,
$$

so every post-ZF survivor has either `a=Omega(D)` or `e_BB=Omega(D)`.

### 6.2 Low loaded-contact surplus forces many actual pockets

If along a sequence

$$
e_{BB}+2s_C\le\lambda D+o(D),
$$

then `e_BB<=lambda D+o(D)` and (6.1) gives

$$
\boxed{
a\ge(2\rho-\lambda-o(1))D.}
\tag{6.2}
$$

At the PI/GU area-gap threshold `lambda<0.796172...`, this lower bound is still a positive linear constant.  This localizes the low-surplus branch to linearly many **distinct convex outer pockets**, not merely a long repeated outer walk.

### 6.3 Exact equality geometry

If PC.3 is equality with zero remainder `d_P+c_B=0`, then all outer pockets are triangles and all loaded-loaded contacts lie on the force-hull cycle.  This is a concrete stability endpoint for any future pocket-incidence theorem.  It is not itself a contradiction: thin triangular pockets and shared unloaded components remain possible.

---

## 7. Regressions and limits

- **Non-hull loaded-loaded unit chords are possible.** No claim sets `c_B=0` without additional geometry.
- **Thin convex pockets are possible.** There is no uniform positive area lower bound per pocket.
- **One unloaded component may interact with several outer pockets.** PC does not inject pockets into unloaded components.
- **Repeated loaded vertices on the outer contact walk are allowed.** They are already accounted for by `d_P` through OP's exact face-incidence formula.
- **Regular odd shell.** Here `a=0`, `e_BB=q`; the ledger is compatible with the shell regression rather than falsely excluding it.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `x_B=a+d_P` | proved | OP exact pocket incidence |
| `q=a+d_P+Q+2k` | proved | ZT substitution |
| `e_BB=d_P+Q+2k+c_B` | proved | definition of `c_B` + preceding identity |
| `a+k=c_I+c_B+s_C+2` | proved | ZU substitution |
| `k<=a+d_P+2f+2` | proved | NM train-end bound |
| uniform area per pocket | rejected | thin convex pockets remain possible |
| one pocket per unloaded component | not proved | outer walk can revisit/share component structure |
| Level I | still open | global source-capacity / boundary-structure closure remains |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let
    a   = number of missing force-hull side contacts = number of OP outer pockets,
    d_P = sum_P(deg P-3),
    c_B = number of loaded-loaded contacts that are not hull sides,
    k   = d_H+s_Z.

OP gives exactly
    x_B=a+d_P.
ZT then gives
    q=a+d_P+Q+2k.
Since e_BB=(q-a)+c_B,
    e_BB=d_P+Q+2k+c_B.
Hence the HB slack is exact:
    e_BB-(Q+2d_H+2s_Z)=d_P+c_B.
ZU further gives
    a+k=c_I+c_B+s_C+2.

DT/NM become
    T=a+d_P+3f+g_F+k,
    k<=a+d_P+2f+2,
    c_I+c_B+s_C<=2a+d_P+2f.

Next target: exploit the geometry/topology of the equality-near branch
    d_P+c_B small,
where almost every outer pocket is triangular and almost every B-B contact is a hull side.
```
