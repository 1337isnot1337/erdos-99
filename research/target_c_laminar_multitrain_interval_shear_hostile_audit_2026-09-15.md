# Hostile audit — laminar multi-train interval shear

**Date:** 2026-09-15
**Reviewed:** `target_c_laminar_multitrain_interval_shear_2026-09-15.md`
**Disposition:** **PASS at proof-only dual-path O--O scope**
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This audit checks the new claim that a consecutive dual-tree block of non-singleton
outer-to-outer stopped trains admits an exact simultaneous finite shear and that every
source-pair displacement depends on a contiguous interval of the shear coordinates.
The dangerous points are topology, contact overlap, full-source handling, and whether
finite composition introduces cross terms in the contact constraints.

---

## 1. The theorem uses exactly the audited dual-path topology

The corrected small-leaf rectangle theorem does not assume that all same-phase O--O
trains form one global linear stack. It extracts a simple path in the complement dual
tree and then takes a consecutive block of edges on that path.

The candidate theorem uses only such a block. Deleting one path edge separates the
dual tree into two components. Choosing the component toward one fixed path endpoint
gives nested shores

\[
S_1\supseteq S_2\supseteq\cdots\supseteq S_m.
\]

No statement about off-path branches is needed: every branch is carried with the path
vertex to which it is attached.

The live rectangle trains are non-singleton automatically because each crosses a
linear family of center trains in strict rhombi. Thus the audited proper-crosscut and
cutset theorem applies directly; no singleton bridge extension is being smuggled in.

**Verdict:** PASS.

---

## 2. A contact can cross only its own selected cut

For each selected train `tau_i`, the audited O--O cutset lemma says the contacts with
endpoints on opposite shores are **exactly** the physical contact edges of `tau_i`.
The stopped-train decomposition partitions contact edges. Therefore if a contact
belongs to `tau_j`, then for every `i!=j` its endpoints lie on the same side of cut
`i`.

If a contact belongs to no selected train, its endpoints lie on the same side of every
selected cut.

This is the key point that makes simultaneous composition exact. It does not require
the selected train directions to be equal or approximately equal.

**Verdict:** PASS.

---

## 3. The finite multi-shear preserves every old contact exactly

For cut `i`, orient its train contacts from `T_i` to `S_i` with unit vector `u_i` and
put

\[
\Delta_i=R_{\theta_i}u_i-u_i.
\]

Move a source vertex by the sum of `Delta_i` over all selected shores containing it.
For a contact on `tau_j`, all `i!=j` contributions cancel between its endpoints, while
the `j`th contribution changes the contact vector from

\[
u_j
\]

to

\[
u_j+\Delta_j=R_{\theta_j}u_j.
\]

Its length is therefore exactly one. A nonselected contact receives equal endpoint
translations and is unchanged.

There is no Baker--Campbell--Hausdorff or rotation-composition issue: the vertices are
not successively rotated about different centers. Equation (IS.1) is one explicit
placement obtained by **adding translations**. The rotations appear only in the
chosen translation vectors `Delta_i`.

**Verdict:** PASS.

---

## 4. Full-source and inactive constraints are handled correctly

The motion is defined on all source vertices, not only on the positive-contact core.
The same Jordan-shore membership used by the audited one-train shear assigns every
contact-isolated source point to a side of every selected cut.

The source is finite. Every old noncontact has positive slack above one, and pair
distances are continuous functions of the finite parameter vector. Hence one common
neighborhood of the origin preserves all strict unit-separation inequalities.

The size of that neighborhood may depend on the finite source and may shrink with `D`.
The theorem needs no uniform radius.

**Verdict:** PASS.

---

## 5. Nested shores give exact interval support

Define

\[
\ell(v)=\#\{i:v\in S_i\}.
\]

Nestedness implies that the shore membership vector of every source vertex is a prefix:

\[
v\in S_i\iff i\le\ell(v).
\]

Thus if `ell(x)=a<ell(y)=b`, the cuts separating `x,y` are exactly

\[
a+1,a+2,\ldots,b.
\]

Subtracting the explicit placements gives

\[
p_y(\theta)-p_x(\theta)
=p_y-p_x+\sum_{i=a+1}^b\Delta_i.
\]

Hence every pair row has consecutive support. This includes actual diameter pairs,
and it is stronger than merely saying each diameter edge crosses a connected subset of
the dual path: it gives the exact finite displacement formula on that interval.

**Verdict:** PASS.

---

## 6. First and second variations are algebraically correct

For one interval row

\[
r(\theta)=r+\sum_i(R_{\theta_i}u_i-u_i),
\]

at the origin

\[
\partial_i r=Ju_i,
\qquad
\partial_{ii}r=-u_i,
\qquad
\partial_{ij}r=0\quad(i\ne j).
\]

For `L=|r|^2`, this gives

\[
\partial_iL=2r\cdot Ju_i,
\]

\[
\partial_{ii}L=2-2r\cdot u_i,
\]

\[
\partial_{ij}L=2u_i\cdot u_j.
\]

Along `theta_i=t c_i`, Taylor expansion yields

\[
r(t)=r+tA-{t^2\over2}B+O(t^3),
\]

\[
|r(t)|^2
=|r|^2+2t r\cdot A+t^2(|A|^2-r\cdot B)+O(t^3),
\]

with

\[
A=\sum c_iJu_i,
\qquad
B=\sum c_i^2u_i.
\]

These formulas are exact consequences of the rotation expansion. The companion
randomized regression script checks the same identities numerically but is not used as
proof.

**Verdict:** PASS.

---

## 7. No diameter conclusion is hidden

Section 157 proves that each individual O--O coordinate is blocked on both transverse
signs by actual diameter pairs. The present theorem does **not** infer that an
arbitrary combination of train shears is diameter-nonincreasing.

A single diameter edge may cross a long interval of selected cuts. Under the new
coordinates it then accumulates the entire interval sum. The active diameter max
function can still have full first-order rank on the selected coordinates.

The theorem therefore supplies a new exact coordinate reduction, not a C-II closure.
The next obligation is to exploit the consecutive-interval structure together with the
`O(D^{-1})` leaf phase width, positive KKT weights, or the explicit curvature term.

**Verdict:** PASS.

---

## Final disposition

The proof survives the topology, overlap, full-source, and finite-composition checks.
At the corrected rectangle scope it establishes a genuinely new fact:

```text
linear consecutive O-O dual-path block
    -> exact simultaneous finite contact shear
    -> every source-pair / diameter row has contiguous interval support
    -> explicit first and second variation on that interval.
```

**Final verdict:** PASS at proof-only dual-path O--O scope. C-II and Level I remain
open.
