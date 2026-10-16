<!-- theorem-state: {"artifact_id":"ART-CD09D493C2BD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_hemmi_kubota_perimeter_area_import_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=952233844e5aceedb671cb7f0a20f8e6c83d2c0a; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — HKI: Hemmi–Kubota perimeter/diameter area bound raises the post-ZF surplus floor

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Run type:** external convex-geometry theorem import + exact Target C consequence  
**Target:** Target C C-II after ZF/PI/JC  
**Depends on:** PDG/DJC fixed-perimeter PI/JC optimization; Hemmi's perimeter-diameter area inequality (5.5) as reproduced and discussed by Anita Kripfganz  
**Computation:** decimal evaluation only  
**New external literature:** yes; scope and source are explicit below

## LEVEL I STATUS

**STILL OPEN.**

The PDG run isolated the force-hull perimeter `L=per(F)` and diameter `D` as the decisive convex variables. A literature audit then found a directly relevant classical result that is substantially stronger than the Groemer-to-Blaschke transfer used in current main.

Kripfganz's 2003 habilitation, Chapter 5, Section 5.1, reproduces Hemmi's 1953 perimeter-diameter area inequalities. In the notation `F=area(K)`, `L=per(K)`, `D=diam(K)`, equation (5.5) states that for every integer `n>=1` and

\[
L\in\left[6nD\sin\frac{\pi}{6n},\ \pi D\right],
\]

one has

\[
\boxed{
F\ge
\left(
\frac{L}{2D}\cos\frac{\pi}{6n}
-\frac{\sqrt3}{2}
\right)D^2.
}
\tag{HKI.1}

The source states that these bounds are attained by regular `3n`-sided Hemmi polyhedra at the corresponding special perimeters and that for `n>=2` they improve the older Kubota bound.

Only the `n=2` case is needed here. It creates a sharp enough barrier at the perimeter

\[
\boxed{
p_2:=12\sin\frac\pi{12}
=3.1058285412302491481\ldots .
}
\tag{HKI.2}

Combining this single imported inequality with the existing PI/JC machinery raises the unconditional post-ZF pinned/contact floor to

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{HKI}
=0.4707353395403166318\ldots .
}
\tag{HKI.3}

This is a significant improvement over PDG's `0.4668176044...`.

---

## 1. External theorem and source audit

### Source checked

Anita Kripfganz, *Hemmi–Polyeder*, Habilitationsschrift, Universität Leipzig, 2003, Chapter 5, especially Section 5.1.

The PDF was text-checked and visually checked at the displayed equation (5.5). The surrounding text attributes the inequality to Hemmi's 1953 work and gives the precise range

\[
L\in[6nD\sin(\pi/(6n)),\pi D].
\]

The bibliography identifies the relevant original papers as

- D. Hemmi, *On a Minimum Problem in the Theory of Ovals*, Bull. Yamagata Univ. (Nat. Sci.) 3 (1953) 1, 1–11;
- D. Hemmi, *The Minimum Area of Convex Curves for Given Perimeter and Diameter*, Bull. Yamagata Univ. (Nat. Sci.) 3 (1954) 2, 55–76.

### Exact imported statement

For each `n>=1`, if a planar convex body has diameter `D` and perimeter `L` in the range above, equation (5.5) gives HKI.1.

No claim from the later detailed classification of all Hemmi polyhedra is needed in the proof below.

### Applicability to Target C

The force hull `F=conv(B)` is a planar convex body. Its Euclidean diameter is exactly the source diameter `D`, since it contains the positively loaded endpoints of actual diameter pairs and lies inside the source convex hull. Its perimeter is the same `per(F)` already used in PI, JC, and GS. Therefore the imported inequality applies directly, with no network or combinatorial reinterpretation.

---

## 2. The `n=2` perimeter threshold

Set

\[
p:=\frac{\operatorname{per}(F)}D.
\]

For `n=2`, HKI.1 applies whenever

\[
p\ge p_2:=12\sin\frac\pi{12}.
\]

It gives

\[
\frac{\operatorname{area}(F)}{D^2}
\ge
\frac p2\cos\frac\pi{12}
-\frac{\sqrt3}{2}.
\tag{2.1}

The right side is increasing in `p`. At the threshold,

\[
\begin{aligned}
\frac{p_2}{2}\cos\frac\pi{12}
-\frac{\sqrt3}{2}
&=
6\sin\frac\pi{12}\cos\frac\pi{12}
-\frac{\sqrt3}{2}\\
&=
3\sin\frac\pi6-rac{\sqrt3}{2}\\
&=
\boxed{\frac{3-\sqrt3}{2}}.
\end{aligned}
\tag{HKI.4}

Thus every Target C force hull with `p>=p_2` satisfies

\[
\boxed{
\frac{\operatorname{area}(F)}{D^2}
\ge
\frac{3-\sqrt3}{2}
=0.63397459621556\ldots .
}
\tag{HKI.5}

This is already far above the approximately `0.5 D^2` PI/Groemer floor governing PDG.

---

## 3. High-perimeter survivors have a much larger surplus

Let

\[
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
t:=\lim\frac{e_{BB}}D
\]

along a convergent post-ZF subsequence.

GU subtracts at most

\[
\frac\pi4\lambda^2D^2+o(D^2)
\]

for the attachment cells. JC gives the joint cavity capacity

\[
\limsup\frac GD^2
\le
\frac{(t+m)^2}{4\pi}
\]

with

\[
m=\min\{y,p-y\}\le\frac p2\le\frac\pi2.
\]

Since `t<=lambda`, any `p>=p_2` survivor must satisfy the deliberately weakened inequality

\[
\frac{3-\sqrt3}{2}
-\frac\pi4\lambda^2
\le
\frac{(\lambda+\pi/2)^2}{4\pi}.
\tag{3.1}

Its positive root is

\[
\boxed{
\lambda_{high}
=0.5813130664918103722\ldots .
}
\tag{HKI.6}

Therefore

\[
\boxed{
p\ge p_2\quad\Longrightarrow\quad\lambda\ge0.5813130664\ldots .}
\tag{HKI.7}

The exact value of this high-perimeter root is not important for the universal minimum; only the large separation from the low-perimeter branch matters.

---

## 4. Below the Hemmi threshold, PI/JC is monotone in perimeter

Now suppose

\[
p<p_2.
\]

Use no Hemmi inequality at all. PDG proved that, after optimizing the diameter density `y` for fixed perimeter `p`, the PI/JC required-surplus function `L_PI(p)` is decreasing on the entire allowed interval.

Hence

\[
\lambda\ge L_{PI}(p)>\lim_{u\uparrow p_2}L_{PI}(u).
\tag{4.1}

Because

\[
p_2>4\rho,
\]

the fixed-perimeter PI optimizer near `p_2` is

\[
y=p/2.
\]

Therefore the limiting low-perimeter constant is the positive root of

\[
\frac12\sin\frac{p_2}{2}
-\frac\pi4\lambda^2
=
\frac{(\lambda+p_2/2)^2}{4\pi}.
\tag{HKI.8}

Define this root by

\[
\boxed{\lambda_{HKI}:=R\left(\frac12\sin(p_2/2),\frac{p_2}{2}\right),}
\tag{HKI.9}

where `R(A,m)` is the explicit positive-root function from PDG.

Numerically,

\[
\frac{p_2}{2}
=1.5529142706151245741\ldots,
\]

\[
\frac12\sin\frac{p_2}{2}
=0.4999200601469133947\ldots,
\]

and

\[
\boxed{
\lambda_{HKI}
=0.4707353395403166317719720558\ldots .
}
\tag{HKI.10}

Thus

\[
\boxed{
p<p_2\quad\Longrightarrow\quad\lambda>\lambda_{HKI}.}
\tag{HKI.11}

---

## 5. Universal consequence

The two perimeter regimes are now separated by a large quantitative jump:

```text
p < p_2:
    lambda > 0.470735339540316...

p >= p_2:
    lambda >= 0.581313066491810...
```

Therefore every unbounded post-ZF survivor sequence satisfies

\[
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge
0.4707353395403166317\ldots .
}
\tag{HKI.12}

The worst regime allowed by this coarse Hemmi import approaches the threshold `p_2` from **below**. At `p_2` itself the `n=2` Hemmi inequality activates and produces a much stronger area floor.

This discontinuity is a discontinuity only in the **coarse family of lower bounds being used**: the full Hemmi solution contains sharper inequalities that fill the perimeter ranges continuously. HKI deliberately uses only the simple displayed inequality (5.5), so no continuity claim about the true minimum-area function is made.

---

## 6. Improvement over the current frontier

The explicit floors developed in this campaign are

\[
\lambda_{GS}=0.4647922504\ldots,
\]

\[
\lambda_{DJC}=0.4653518454\ldots,
\]

\[
\lambda_{PDG}=0.4668176044\ldots,
\]

and now

\[
\boxed{\lambda_{HKI}=0.4707353395\ldots .}
\]

The improvement over PDG is approximately

\[
\boxed{0.0039177351.}
\]

Unlike the small numerical GS refinement, this gain comes from importing a theorem tailored exactly to fixed perimeter and diameter.

---

## 7. Stronger literature route exposed

Kripfganz's Section 5.4 states that the full isoperimetric-isodiametric problem is quantitatively solved by Hemmi polyhedra and gives a piecewise sharp complex of inequalities for every

\[
2D\le L\le\pi D.
\]

Equation (5.5) is only a convenient coarse member of that complex. Therefore the natural next literature task is now concrete:

> Extract and verify the sharp Hemmi lower-area function on the interval immediately below `p_2=12 sin(pi/12)`, then substitute it into the PI/JC cavity optimization.

Because HKI's universal minimum is currently attained only as `p approaches p_2 from below`, any sharp lower-area improvement on that left neighborhood immediately raises the global Target C surplus floor again.

The full Hemmi function may remove the artificial threshold jump entirely and substantially strengthen HKI.

---

## 8. Regression audit

### Applicability to a polygonal force hull

The imported theorem is for arbitrary planar convex figures, so polygons are included.

### Diameter normalization

The force hull contains endpoints of actual diameter pairs and all its points lie in the source convex hull, so its diameter is exactly `D`.

### Perimeter range

The `n=2` theorem is used only for `p>=p_2`, precisely its stated range.

### No use of the sharp classification

The proof does not assume the force hull is a Hemmi polyhedron. It uses only the lower-area inequality valid for every convex figure in the range.

### Apparent threshold jump

Not interpreted as geometry. It is only a feature of switching from PI to the coarse `n=2` inequality (5.5). The true sharp lower envelope is continuous and is the next target for extraction.

---

## 9. Literature record

**Checked source:** Anita Kripfganz, *Hemmi–Polyeder*, Habilitationsschrift, Universität Leipzig, 2003, Chapter 5, pp. 85–108 in the thesis pagination. Equation (5.5) and its range were visually inspected in the PDF.

**Original works identified by that source:**

- D. Hemmi, *On a Minimum Problem in the Theory of Ovals*, Bull. Yamagata Univ. (Nat. Sci.) 3 (1953) 1, 1–11.
- D. Hemmi, *The Minimum Area of Convex Curves for Given Perimeter and Diameter*, Bull. Yamagata Univ. (Nat. Sci.) 3 (1954) 2, 55–76.

**Original-paper audit status:** not yet independently fetched. The theorem statement is imported from Kripfganz's detailed mathematical synthesis, not from a secondary popular summary.

---

## 10. Classification

**Status:** proved Target C consequence conditional on the imported Hemmi inequality HKI.1; source statement and hypotheses visually verified in Kripfganz's full mathematical treatment.  
**Level I:** still open.  
**New literature:** yes.  
**Original-source provenance:** follow-up desirable before canonical promotion.

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

External Hemmi inequality (Kripfganz thesis eq. 5.5):
For every n>=1 and convex planar K with diameter D and perimeter
    L in [6n D sin(pi/(6n)), pi D],
    area(K) >= [L/(2D) cos(pi/(6n)) - sqrt(3)/2] D^2.

Use n=2. The threshold is
    p_2=L/D=12 sin(pi/12)=3.105828541230249....
At p=p_2 the imported area floor is
    (3-sqrt(3))/2=0.6339745962....
Thus every p>=p_2 post-ZF survivor has lambda=(e_BB+2s_C)/D >=0.5813...
by the existing GU/JC cavity argument.

For p<p_2, use PI/JC only. PDG proves the optimized PI-only required surplus decreases
with p, so its infimum below p_2 is the left limit at p_2:
    0.5 sin(p_2/2) - pi lambda^2/4
      = (lambda+p_2/2)^2/(4pi).
The positive root is
    lambda_HKI=0.4707353395403166318....
Hence universally
    liminf (e_BB+2s_C)/D >= lambda_HKI.

The new bottleneck is exactly the interval immediately below p_2. Kripfganz records
the full sharp Hemmi-polyhedron area function there; extracting it is the next step.
```
