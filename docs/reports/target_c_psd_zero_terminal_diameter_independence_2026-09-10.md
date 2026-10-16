<!-- theorem-state: {"artifact_id":"ART-5E5B85F3D33F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — zero-excess response terminals form a degree-two independent set in the diameter thrackle

**Date:** 2026-09-10  
**Repository state:** draft PR #178 after DC commit `47177b4337a6bb993e830d16d6c0e8d9d566fd81`; current `main` includes Woodall commit `1adc420e9227476135d6891b61f1a75193aa90ab`  
**Run type:** exact PSD-response / diameter-topology sharpening  
**Target:** Target C, C-II  
**Depends on:** C64 response cut domination and zero-row rigidity; C36 attachment size; C65 full actual diameter support; Hopf--Pannwitz `h<=q`; DC+Woodall in the low-surplus forest branch  
**External input:** none beyond already imported canonical diameter-thrackle facts  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

Let `B` be the `q` loaded diameter terminals and

\[
M=\Lambda-L_H\succeq0
\]

be the actual response defect.  Write

\[
d_b=\sum_{k\ne b}c_{bk},
\qquad
s_b=\sum_{k\ne b}\beta_{bk},
\]

and split

\[
Z:=\{b:d_b=s_b\},
\qquad
T:=B\setminus Z.
\]

C64 proved `|T|>=2q/5`.  Its own row-rigidity mechanism yields a stronger exact
statement:

\[
\boxed{
Z\text{ is an independent set of }H,
\qquad
\deg_H(b)\ge2\quad(b\in Z).
}
\tag{ZT.1}
\]

Consequently

\[
\boxed{|T|\ge q-\frac h2\ge\frac q2.}
\tag{ZT.2}
\]

Since C30 gives `2q>=ceil(D)+2`,

\[
\boxed{|T|\ge\frac{\lceil D\rceil+2}{4}.}
\tag{ZT.3}
\]

In the low-surplus range of DC, the actual diameter graph is a caterpillar forest and
Woodall gives `h=q-d_H`.  There the exact count improves to

\[
\boxed{|T|\ge\frac{q+d_H}{2}.}
\tag{ZT.4}
\]

Thus at least half of the full actual diameter boundary, and strictly more than half
when there are many diameter components, carries genuine positive PSD response defect.
This still does not produce a numerical lower bound on each defect diagonal.

---

## 1. C64 zero-row rigidity

C64 gives

\[
M_{bb}=d_b-s_b\ge0.
\]

If `b in Z`, then `M_bb=0`.  Positivity of every `2x2` principal minor of a PSD matrix
forces the entire row to vanish:

\[
M_{bk}=0\qquad(k\in B).
\]

Since

\[
M_{bk}=-(c_{bk}-\beta_{bk})
\quad(b\ne k),
\]

we have

\[
\boxed{c_{bk}=\beta_{bk}\quad\text{for every }k.}
\tag{1.1}
\]

C64 also observed two consequences used below:

1. a zero terminal has no loaded-loaded unit contact;
2. if a harmonic unloaded component `I_r` has `b in A_r`, then every
   `k in A_r\setminus\{b\}` is a diameter neighbor of `b`, because the component
   response has `c^{(r)}_{bk}>0`.

Every such attachment set has

\[
|A_r|\ge3.
\tag{1.2}
\]

---

## 2. Zero terminals have diameter degree at least two

### Lemma ZT.1

For every `b in Z`,

\[
\boxed{\deg_H(b)\ge2.}
\tag{2.1}
\]

### Proof

The full positive contact graph is connected.  By (1.1), `b` cannot have a direct
loaded-loaded unit contact: such a contact contributes positive response conductance
while `D>1` makes it a non-diameter pair.  Therefore `b` is incident to the contact
edges of at least one unloaded harmonic component `I_r`, so `b in A_r`.

By (1.2), choose distinct

\[
k,l\in A_r\setminus\{b\}.
\]

The strict harmonic component response gives

\[
c_{bk}>0,
\qquad
c_{bl}>0.
\]

Equation (1.1) forces

\[
\beta_{bk}=c_{bk}>0,
\qquad
\beta_{bl}=c_{bl}>0.
\]

Thus `bk,bl in H` and `deg_H(b)>=2`. `square`

In particular every diameter leaf belongs to `T`.

---

## 3. Zero terminals are independent in the diameter graph

### Lemma ZT.2

No diameter edge joins two zero terminals:

\[
\boxed{H[Z]\text{ has no edges}.}
\tag{3.1}
\]

### Proof

Suppose `bk in H` with `b,k in Z`.  Relative-interior full diameter support gives

\[
\beta_{bk}>0.
\]

By zero-row rigidity at `b`,

\[
c_{bk}=\beta_{bk}>0.
\tag{3.2}
\]

There is no direct loaded-loaded contact between `b` and `k` because `|b-k|=D>1`.
Hence the positive response conductance in (3.2) is contributed by at least one
unloaded harmonic component whose attachment set contains both `b` and `k`.

But C64.3 proves that every unloaded harmonic component contains at most one zero
terminal: if two zero terminals occur in the same attachment set, a third attachment
and zero-row rigidity create a diameter triangle.  Contradiction. `square`

Thus every diameter edge is incident to at most one zero terminal.

---

## 4. Half of all loaded terminals are strict

Sum diameter degrees over `Z`.  Lemma ZT.1 gives

\[
2|Z|\le\sum_{b\in Z}\deg_H(b).
\tag{4.1}
\]

By Lemma ZT.2, every diameter edge is counted at most once in the sum on the right.
Therefore

\[
\sum_{b\in Z}\deg_H(b)\le h.
\tag{4.2}
\]

Hence

\[
\boxed{2|Z|\le h.}
\tag{4.3}
\]

Since `q=|Z|+|T|`,

\[
|T|=q-|Z|\ge q-\frac h2.
\tag{4.4}
\]

The Hopf--Pannwitz diameter-thrackle bound gives `h<=q`, yielding

\[
\boxed{|T|\ge q/2.}
\]

C30's force-visible boundary count `2q>=ceil(D)+2` then gives ZT.3.

This improves C64's `2q/5` by using the actual diameter graph rather than only loaded
contact-degree incidence.

---

## 5. Forest specialization

DC proves that for every fixed

\[
\lambda_0<\lambda_{\rm disk}
\]

all sufficiently large post-ZF survivors with

\[
\frac{e_{BB}+2s_C}{D}\le\lambda_0
\]

have acyclic actual diameter graph.  The Woodall report now on `main` identifies this
as a caterpillar forest with exactly

\[
d_H=q-h
\]

components.  Therefore (4.4) becomes

\[
\boxed{
|T|
\ge q-\frac{q-d_H}{2}
=\frac{q+d_H}{2}.
}
\]

Every additional diameter component thus contributes half a forced strict terminal in
this exact counting sense.

In the `s_Z=0` circuit subcase, E597 simultaneously charges the same component count
by

\[
\frac{e_{BB}+2s_C}{D}
\ge0.597+\epsilon_{597}+3\frac{d_H}{D}.
\]

ZT and E597 therefore couple the electrical strict-set size and the diameter forest
topology to the same defect variable `d_H`.

---

## 6. Exact effect and remaining obstruction

The response defect cannot be confined to a sparse exceptional boundary set.  At
least half of all loaded terminals have

\[
d_b-s_b>0,
\]

and in the forest branch at least `(q+d_H)/2` do.

The remaining obstruction is purely quantitative.  Neither PSD nor unit-contact
geometry currently supplies a lower bound

\[
d_b-s_b\ge c/D
\]

on those strict terminals.  Near-star circular-planar networks can make individual
strict response conductances arbitrarily small, so a proof must use the actual
unit-contact embedding, FS almost-antipodal geometry, or global source capacity.

A useful next theorem would prove an aggregate estimate

\[
\sum_{b\in T}(d_b-s_b)\ge c
\quad\text{or stronger},
\]

with a scale that crosses one of the existing response/face thresholds.  Merely
counting `T` cannot do so.

---

## 7. Regression audit

- **Unit square:** its diameter graph is a matching and all four terminals are strict;
  ZT holds.
- **Regular odd shell:** compatible; the response defect is positive at every shell
  terminal in the explicit regression.
- **Near-star response network:** compatible; ZT counts strict rows but permits every
  positive diagonal to tend to zero.
- **Diameter star:** compatible.  A zero center of high degree is allowed, but all
  diameter leaves are strict, so ZT is stronger than C64 there.
- **Contact-isolated source points:** irrelevant to the terminal count; they remain
  outside the response network.

---

## 8. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| zero terminal degree at least two | proved | C64 row equality + one attached harmonic component with at least three terminals |
| zero terminals independent in `H` | proved | positive diameter edge would force a harmonic component containing two zero terminals |
| `2|Z|<=h` | proved | degree sum plus independence |
| `|T|>=q/2` | proved | Hopf--Pannwitz `h<=q` |
| forest `|T|>=(q+d_H)/2` | proved | `h=q-d_H` |
| positive aggregate trace floor | not proved | individual strict defects may vanish |
| Level I | still open | quantitative response / forest closure remains |
