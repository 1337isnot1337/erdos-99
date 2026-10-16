<!-- theorem-state: {"artifact_id":"ART-17B0E5196E8F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — outer-pocket area from chain–chord detour

**Date:** 2026-09-09  
**Repository base:** `3be19652b84a3097b513af7fa55366a1690ad7b7`  
**Run type:** exact geometric stability theorem  
**Target:** Target C C-II / post-JC outer-cavity capacity  
**Depends on:** OP hull augmentation and PC pocket notation  
**External input:** none  
**LEVEL I STATUS:** STILL OPEN

JC bounds the total outer-pocket area from the total available excess perimeter.  This note proves a different estimate that detects **detour**: if the unit-contact outer walk is close in length to the true convex force-hull perimeter, then the entire outer-pocket area is small even when the walk and hull perimeter are both `Theta(D)`.

Let

- `F` be the force hull;
- `P_F=per(F)`;
- `b` be the unit-contact outer-face boundary-walk length;
- `q=|B_+|`;
- `a` be the number of missing force-hull side contacts, equivalently the number of OP outer pockets;
- `x_B=b-q`.

For each OP outer pocket `P`, let

- `s_P` be the Euclidean length of its unique force-hull side;
- `ell_P` be the length of the complementary old-contact boundary chain.

Every edge of that contact chain is a unit edge, so `ell_P` is also its number of edges.

The main bound is

\[
\boxed{
H_{out}
:=\sum_P area(P)
\le
\frac{\pi}{4\sqrt2}
(x_B+a)^{3/2}
\sqrt{b-P_F}.
}
\tag{OD.1}
\]

The square root is real because OP already proves `P_F<=b`.

This is exact at finite `D`; no asymptotic error occurs in OD.1.

---

## 1. One added hull side per outer pocket

OP forms the hull-augmented graph

\[
\widehat G=C\cup\partial F
\]

by adding every missing force-hull side.  It proves that

1. `\widehat G` is 2-connected;
2. every new bounded face is a simple strict convex polygon;
3. the number of new bounded faces equals the number `a` of added hull sides.

Every added hull side lies on `partial F`.  It is incident to the unbounded face on its exterior side and to exactly one bounded face on its interior side.  Conversely every new bounded face must contain an added hull side, because the old bounded faces of `C` remain unchanged and only added edges can cut a new face from the old outer face.

There are `a` added sides and `a` new bounded faces.  Hence:

### Lemma OD.1

Every OP outer pocket contains exactly one added force-hull side.

Its remaining boundary is therefore a simple subchain of the old unit-contact outer walk joining the endpoints of that hull side.

---

## 2. Exact total chain length and exact total detour

Let the graph-boundary degree of pocket `P` be `k_P`.  By Lemma OD.1,

\[
\ell_P=k_P-1.
\tag{OD.2}
\]

OP proves the exact incidence identity

\[
\sum_P k_P=b+2a-q.
\tag{OD.3}
\]

Therefore

\[
\boxed{
L_{chain}:=\sum_P\ell_P
=b+a-q
=x_B+a.
}
\tag{OD.4}
\]

There are `q-a` force-hull sides that were already unit-contact edges.  Their total length is exactly `q-a`.  The remaining hull sides are precisely the unique added sides of the outer pockets. Hence

\[
\boxed{
\sum_Ps_P=P_F-(q-a).
}
\tag{OD.5}
\]

Subtract OD.5 from OD.4:

### Lemma OD.2 — exact chain–chord detour

\[
\boxed{
U_{det}:=\sum_P(\ell_P-s_P)=b-P_F.
}
\tag{OD.6}
\]

Each term is nonnegative by the triangle inequality, so OD.6 also recovers `P_F<=b`.

Thus `b-P_F` is not an abstract perimeter slack.  It is exactly the total excess length paid by the old contact chains over the straight force-hull chords that replace them.

---

## 3. One pocket lies in a focal ellipse

Fix one outer pocket `P`.  Write its hull-side endpoints as `A,B`, its contact-chain length as

\[
\ell:=\ell_P,
\]

and its hull-side length as

\[
s:=s_P=|A-B|.
\]

For any point `x` on the polygonal contact chain, let `ell_1,ell_2` be the two subchain lengths from `A` to `x` and from `x` to `B`.  Then

\[
\ell_1+\ell_2=\ell.
\]

Euclidean distance is at most polygonal path length, so

\[
|A-x|+|x-B|
\le\ell_1+\ell_2
=\ell.
\tag{OD.7}
\]

Hence the whole contact chain lies in the closed ellipse

\[
E(A,B;\ell)
:=\{x:|A-x|+|x-B|\le\ell\}.
\]

The ellipse is convex.  OP proves `P` is convex, and `P` is the convex polygon bounded by the contact chain together with chord `AB`.  Therefore

\[
P\subseteq E(A,B;\ell).
\tag{OD.8}
\]

Moreover `P` lies in one closed half-plane bounded by the line `AB`, while the ellipse is symmetric across that line. Thus `P` occupies at most half the ellipse area.

The ellipse has semimajor axis

\[
a_E=\ell/2
\]

and focal distance

\[
c_E=s/2.
\]

Its semiminor axis is

\[
b_E=\frac12\sqrt{\ell^2-s^2}.
\]

Therefore:

### Lemma OD.3 — one-pocket ellipse bound

\[
\boxed{
area(P)
\le
\frac\pi8\ell\sqrt{\ell^2-s^2}.
}
\tag{OD.9}
\]

Since

\[
\ell^2-s^2=(\ell-s)(\ell+s)\le2\ell(\ell-s),
\]

we also have

\[
\boxed{
area(P)
\le
\frac\pi{4\sqrt2}
\ell^{3/2}\sqrt{\ell-s}.
}
\tag{OD.10}
\]

No smoothness or Dido/isoperimetric theorem is used; the polygonal chain itself supplies the ellipse containment.

---

## 4. Sum the pocket bounds

Put

\[
u_P:=\ell_P-s_P\ge0.
\]

By OD.10,

\[
H_{out}
\le
\frac\pi{4\sqrt2}
\sum_P\ell_P^{3/2}\sqrt{u_P}.
\tag{OD.11}
\]

Cauchy–Schwarz gives

\[
\sum_P\ell_P^{3/2}\sqrt{u_P}
\le
\left(\sum_P\ell_P^3\right)^{1/2}
\left(\sum_Pu_P\right)^{1/2}.
\tag{OD.12}
\]

For nonnegative `ell_P`,

\[
\sum_P\ell_P^3
\le
\left(\sum_P\ell_P\right)^3.
\tag{OD.13}
\]

Use OD.4 and OD.6:

\[
\sum_P\ell_P=x_B+a,
\qquad
\sum_Pu_P=b-P_F.
\]

Substitution into OD.11–OD.13 proves OD.1.

---

## 5. Post-ZF exact-coordinate form

The PC/ZT variables give more explicit formulas.  Put

\[
k=d_H+s_Z,
\]

and let `c_B` be the number of loaded-loaded contacts that are not hull sides. PC proves

\[
e_{BB}=d_P+Q+2k+c_B,
\]

\[
a=q-e_{BB}+c_B.
\]

Also ZT gives

\[
b=2h-Q-2s_Z.
\tag{OD.14}
\]

From OD.4,

\[
\boxed{
L_{chain}
=x_B+a
=2h-Q-2s_Z-e_{BB}+c_B.
}
\tag{OD.15}
\]

From OD.6,

\[
\boxed{
U_{det}
=2h-Q-2s_Z-P_F.
}
\tag{OD.16}
\]

Therefore OD.1 becomes

\[
\boxed{
H_{out}
\le
\frac\pi{4\sqrt2}
\bigl(2h-Q-2s_Z-e_{BB}+c_B\bigr)^{3/2}
\sqrt{2h-Q-2s_Z-P_F}.
}
\tag{OD.17}
\]

All quantities under the roots are nonnegative by their geometric definitions.

This form is useful together with JC/JN/GS because those theorems already constrain `h`, `e_BB`, and `P_F` on the `D` scale.

---

## 6. Stability consequences

### Corollary OD.4 — near-perimeter outer walk has subquadratic pocket area

Suppose along an unbounded post-ZF sequence

\[
b-P_F=o(D).
\tag{OD.18}
\]

Since `b=O(D)` and `a=O(D)`, OD.4 gives `L_chain=O(D)`.  Therefore OD.1 yields

\[
\boxed{H_{out}=o(D^2).}
\tag{OD.19}
\]

More quantitatively, if

\[
b-P_F=O(D^{1-\eta})
\]

for some `eta>0`, then

\[
\boxed{H_{out}=O(D^{2-\eta/2}).}
\tag{OD.20}
\]

### Corollary OD.5 — quadratic outer-pocket area forces linear detour

Conversely, if

\[
H_{out}\ge\gamma D^2
\]

and

\[
L_{chain}\le LD
\]

for fixed positive `gamma,L`, then OD.1 implies

\[
\boxed{
\frac{b-P_F}{D}
\ge
\frac{32\gamma^2}{\pi^2L^3}.
}
\tag{OD.21}
\]

Thus a macroscopically large outer cavity must pay a positive linear chain–chord detour.  It cannot coexist with asymptotic equality `b=P_F+o(D)`.

---

## 7. Relation to JC/JN/GS

JC bounds the **joint** outer-pocket and exceptional-face area using an isoperimetric square in the total excess-perimeter currency. OD is complementary:

- JC is strongest when only the total perimeter budget is known;
- OD becomes much stronger when `b-P_F` is small, because it remembers that every outer pocket is trapped between a unit contact chain and its straight hull chord.

JN showed that attempting to attain the old scalar JC threshold forces `P_F/D->pi` and several other defect currencies to vanish.  OD identifies an additional geometric quantity that must then be checked: the contact-walk detour `b-P_F`.  If the same extremal regime forces `b-P_F=o(D)`, OD makes the entire outer-pocket contribution subquadratic, so the equality geometry must move into bounded exceptional faces alone.

No claim of an improved numerical pinned-surplus constant is made in this report.  That optimization should be performed separately against the full JC/GS feasible region rather than folded into the geometric lemma.

---

## 8. Regressions and limits

- A single long semicircular-like contact chain can enclose `Theta(D^2)` area, but then its length exceeds its chord by `Theta(D)`; OD allows this.
- Many thin triangular pockets may have `a=Theta(D)` while total area is only `O(D)`; OD also allows this.
- `P_F` close to `pi D` alone does not imply small detour; `b` may still exceed `P_F` by a positive linear amount.
- OD controls only OP outer pockets, not bounded exceptional contact faces. Those remain governed by the `Q`/JC bounds.
- The ellipse constant is not claimed optimal. A Dido circular-arc bound would improve it, but no such external input is needed for OD.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| one added hull side per OP pocket | proved | edge/face incidence + `p=a` |
| `sum ell_P=x_B+a` | proved | OP exact face-incidence identity |
| `sum(ell_P-s_P)=b-P_F` | proved | exact hull-side length partition |
| one-pocket ellipse bound | proved | focal-distance inequality + convexity |
| OD.1 global detour-area bound | proved | Cauchy–Schwarz |
| `b-P_F=o(D) => H_out=o(D^2)` | proved | OD.1 and `L_chain=O(D)` |
| improved universal surplus constant | not claimed here | requires joint optimization with JC/GS |
| Level I | still open | exceptional faces / high-surplus geometry remain |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For each OP outer pocket P:
    ell_P = length of its old unit-contact chain,
    s_P   = length of its unique added force-hull side.
Exactly
    sum ell_P = b+a-q = x_B+a,
    sum s_P   = per(F)-(q-a),
so
    sum(ell_P-s_P)=b-per(F).

Every point x on the contact chain has
    |A-x|+|x-B| <= ell_P,
so the convex pocket lies in one half of the ellipse with foci A,B and major-axis
length ell_P. Therefore
    area(P) <= (pi/8) ell_P sqrt(ell_P^2-s_P^2)
            <= (pi/(4sqrt2)) ell_P^(3/2) sqrt(ell_P-s_P).
Summing by Cauchy gives
    H_out <= (pi/(4sqrt2))
             (x_B+a)^(3/2) sqrt(b-per(F)).

Post-ZF:
    x_B+a = 2h-Q-2s_Z-e_BB+c_B,
    b-per(F)=2h-Q-2s_Z-per(F).

Hence near equality of outer-walk length and convex perimeter forces subquadratic
outer-pocket area. Next: optimize this together with JC/GS and the exceptional-face
Q budget.
```
