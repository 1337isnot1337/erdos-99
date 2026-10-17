> Generated reading edition · [exact source](../../../docs/reports/target_c_slope_one_hemmi_exclusion_2026-09-09.md) · source SHA-256 `d4d84d15b0943bba68f466f95d0b2ca8a2df2db0ef95f86a8afc4329aec98526`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-280B255D8CB1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — SHX: sharp Hemmi geometry excludes the RCC slope-one endpoint

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-nearzero-physical-carrier`  
**Run type:** exact asymptotic branch exclusion / convex perimeter-area synthesis  
**Target:** Target C C-II, C66 phase `D epsilon -> 0` at RCC slope one  
**Depends on:** RCC/S1E/SCC/SAC/SOD on this branch; PI and JC; HKS/HKI sharp Hemmi input from PR #130  
**New external literature:** none beyond the already-audited Hemmi input in HKS/HKI  
**Computation:** only conservative scalar evaluations with fixed margins

## LEVEL I STATUS

**STILL OPEN.**

This report closes one complete endpoint of the near-zero response phase.

Let

$$
\varepsilon:=\sum_{b<k}c_{bk}-1
=\tfrac12\operatorname{tr}(\Lambda-L_H),
$$

and

$$
L:=e_{BB}+2s_C.
$$

RCC proves that `epsilon -> 0` forces `liminf L/D >= 1`. The remaining equality endpoint was

$$
D\varepsilon\to0,
\qquad
\frac{L}{D}\to1.
\tag{SHX.1}
$$

SAC and SOD reduce any such sequence to

$$
\frac hD=\frac qD+o(1)=:y+o(1),
\qquad
1.5336\le y\le1.6349643789\ldots,
\tag{SHX.2}
$$

and, crucially,

$$
\sum_r\operatorname{area}(\operatorname{conv}A_r)=o(D^2).
\tag{SHX.3}
$$

The sharp Hemmi perimeter-area theorem now contradicts the JC cavity capacity everywhere in the interval SHX.2.

### Theorem SHX — slope-one exclusion

There is no unbounded sequence of post-ZF Target C survivors satisfying SHX.1.

Equivalently,

$$
\boxed{
D\varepsilon\to0
\quad\Longrightarrow\quad
\liminf\frac{e_{BB}+2s_C}{D}>1
\text{ in the sense that slope-one approach is impossible.}
}
\tag{SHX.4}
$$

More precisely, no subsequence can have `(e_BB+2s_C)/D -> 1`.

This statement does **not** yet provide an explicit uniform gap `1+eta`; obtaining such a quantitative stability version requires extending the SCC/SAC estimates off exact slope one.

---

## 1. Reduce the attachment gap to the full force-hull area

Under SHX.1, SAC proves SHX.3. Hence the C49 attachment gap

$$
G:=\operatorname{area}(F)
-
\sum_r\operatorname{area}(\operatorname{conv}A_r)
$$

satisfies

$$
\boxed{
G=\operatorname{area}(F)-o(D^2).
}
\tag{SHX.5}
$$

Pass to a subsequence along which

$$
y:=\lim h/D,
\qquad
p:=\lim P_F/D,
\qquad
P_F:=\operatorname{per}(F),
$$

and

$$
t:=\lim e_{BB}/D
$$

exist. Since `L/D -> 1` and `s_C>=0`,

$$
0\le t\le1.
\tag{1.1}
$$

S1E gives `q-h=o(D)`, so `q/D -> y`. Consecutive force-hull vertices are unit-separated, hence `q<=P_F`; therefore

$$
p\ge y.
\tag{1.2}
$$

ZT gives

$$
b=2h-Q-2s_Z\le2h,
$$

and the outer contact walk has `P_F<=b`. Thus

$$
p\le2y.
\tag{1.3}
$$

Consequently

$$
\min\{y,p-y\}=p-y.
\tag{1.4}
$$

---

## 2. PI plus JC forces a minimum perimeter

PI gives the force-hull area lower bound

$$
A_{PI}(y)
:=
\begin{cases}
\frac12\sin y,&y\le\pi/2,\\[3pt]
\frac12,&y\ge\pi/2.
\end{cases}
\tag{2.1}
$$

so

$$
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge A_{PI}(y).
\tag{2.2}
$$

The actual-perimeter JC capacity gives

$$
\limsup\frac G{D^2}
\le
\frac{(t+\min\{y,p-y\})^2}{4\pi}.
\tag{2.3}
$$

Use SHX.5, (1.1), and (1.4):

$$
\boxed{
A_{PI}(y)
\le
\frac{(1+p-y)^2}{4\pi}.
}
\tag{SHX.6}
$$

All quantities are positive. Therefore every hypothetical slope-one survivor must satisfy

$$
\boxed{
p\ge p_{req}(y):=y-1+\sqrt{4\pi A_{PI}(y)}.}
\tag{SHX.7}
$$

SOD gives `y>=1.5336`. On the entire SOD interval, `p_req` is increasing. Indeed:

- for `y<=pi/2`,
  $$
  p_{req}'(y)
  =1+\frac{\pi\cos y}{\sqrt{2\pi\sin y}}>1;
  $$
- for `y>=pi/2`, `A_PI=1/2`, so `p_req'(y)=1`.

Thus

$$
p\ge p_{req}(1.5336).
$$

A conservative direct evaluation gives

$$
\boxed{p>3.039.}
\tag{SHX.8}
$$

(The actual value is about `3.0393612`.)

Hence the full hypothetical slope-one interval lies inside the perimeter range where Hemmi's sharp fixed-diameter area theorem applies.

---

## 3. Hemmi first branch already exceeds JC at the forced perimeter

Put

$$
p_2:=12\sin\frac\pi{12}
=3.1058285412\ldots .
\tag{3.1}
$$

On the sharp first Hemmi branch

$$
3<p\le p_2,
$$

HKS records

$$
\boxed{
A_H(p)
=3\left(\frac p{p_2}\right)^2
-\frac{3+\sqrt3}{2}.
}
\tag{SHX.9}
$$

Therefore every diameter-one normalized force hull with perimeter `p` in this interval satisfies

$$
\operatorname{area}(F)/D^2\ge A_H(p).
\tag{3.2}
$$

Fix `y` in the SOD interval and suppose first that

$$
p_{req}(y)\le p\le p_2.
$$

Consider

$$
\Phi_y(p)
:=A_H(p)-\frac{(1+p-y)^2}{4\pi}.
\tag{3.3}
$$

Its derivative is

$$
\Phi_y'(p)
=
\frac{6p}{p_2^2}
-
\frac{1+p-y}{2\pi}.
\tag{3.4}
$$

On

$$
p\ge3.039,
\qquad
y\ge1.5336,
\qquad p\le p_2,
$$

we have the crude bounds

$$
\frac{6p}{p_2^2}>1.89,
$$

while

$$
\frac{1+p-y}{2\pi}<0.41.
$$

Hence

$$
\boxed{\Phi_y'(p)>1.48>0.}
\tag{SHX.10}
$$

So it is enough to test the smallest allowed perimeter `p=p_req(y)`.

By definition of `p_req`,

$$
\frac{(1+p_{req}(y)-y)^2}{4\pi}=A_{PI}(y).
$$

Thus

$$
\Phi_y(p_{req}(y))
=A_H(p_{req}(y))-A_{PI}(y).
\tag{3.5}
$$

Define

$$
R(y):=A_H(p_{req}(y))-A_{PI}(y).
$$

For `y<=pi/2`, `p_req'(y)>1` and

$$
A_{PI}'(y)=\tfrac12\cos y<0.019
$$

throughout `y>=1.5336`. Also `A_H'(p)>1.89`. Hence

$$
R'(y)>1.89-0.019>0.
$$

For `y>=pi/2`, `A_PI` is constant and `p_req'(y)=1`, so again `R'(y)>0`.

Therefore the smallest value occurs at `y=1.5336`. A conservative evaluation gives

$$
\boxed{
R(1.5336)>0.007.
}
\tag{SHX.11}
$$

(The actual margin is about `0.00729`.)

Consequently, for every

$$
1.5336\le y\le1.634964\ldots,
\qquad
p_{req}(y)\le p\le p_2,
$$

we have

$$
A_H(p)
>
\frac{(1+p-y)^2}{4\pi},
$$

contradicting the JC upper capacity SHX.6.

---

## 4. Perimeters above the first Hemmi branch are even easier

It remains to exclude

$$
p\ge p_2.
$$

HKI records the simple `n=2` Hemmi lower bound, valid for

$$
p\in[p_2,\pi],
$$

$$
\boxed{
A(F)/D^2
\ge
\frac p2\cos\frac\pi{12}
-rac{\sqrt3}{2}.
}
\tag{SHX.12}
$$

The right side is increasing in `p`, so at `p=p_2` it already equals

$$
\frac{3-\sqrt3}{2}
=0.6339745962\ldots .
\tag{4.1}
$$

By contrast, throughout the entire SOD interval and with `p<=pi`, the JC capacity is at most

$$
\frac{(1+\pi-1.5336)^2}{4\pi}
<0.542.
\tag{4.2}
$$

Thus SHX.12 and JC are separated by more than `0.09`; no `p>=p_2` case is possible.

---

## 5. Conclusion

Every hypothetical slope-one sequence must, by PI+JC, have `p>=p_req(y)>3.039`.

- If `p<=p_2`, sharp first-branch Hemmi exceeds the maximum JC cavity capacity by at least the positive margin established in SHX.11 and monotonicity SHX.10.
- If `p>=p_2`, the coarse Hemmi lower bound exceeds JC by more than `0.09`.

Both alternatives are impossible.

Therefore there is no sequence satisfying SHX.1. This proves SHX.

---

## 6. What this changes in the near-zero response frontier

RCC previously gave only

$$
D\varepsilon\to0
\Longrightarrow
\liminf L/D\ge1.
$$

S1E/SCC classified the equality endpoint. SOC/SAC/SOD made that endpoint progressively more rigid. SHX now deletes it completely.

The surviving C66 branch must therefore stay **strictly above slope one** in the asymptotic sense that no subsequence can converge to one.

What is not yet proved is a numerical constant `eta>0` such that

$$
L\ge(1+\eta)D
$$

for all sufficiently large near-zero survivors. Compactness of scalar variables alone is insufficient because SCC/SAC used equality-scale geometric conclusions. A quantitative off-slope stability theorem is required.

---

## 7. Regression audit

- SHX uses Hemmi only after PI+JC forces `p>3.039`, inside the audited Hemmi range.
- The first-branch contradiction is monotone in `p`; no unproved optimizer statement is used.
- The second branch uses the weaker HKI `n=2` Hemmi inequality, so no higher-branch formula is needed.
- `t=e_BB/D` is replaced by the larger value one, which only enlarges the JC capacity and makes the contradiction harder.
- `min{y,p-y}=p-y` follows from `q<=P_F<=b<=2h` and `q/h->1`; no near-circle assumption is used.
- The proof depends essentially on SAC's attachment-area collapse, hence on exact slope-one S1E/SCC geometry. It is not claimed for arbitrary `L/D>1`.
- No conclusion about the sign of Erdős #99 is claimed from SHX alone.

---

## 8. Next target

The natural next theorem is a **quantitative off-slope stability version of SCC/SAC**.

Write

$$
\eta_D:=L/D-1\ge-o(1).
$$

RCC and the response-energy concentration imply one harmonic component still has an attachment pair at distance `D-o(D)` and graph diameter at least `D-o(D)`. ZK leaves at most approximately `eta_D D` graph-diameter budget outside that carrier.

A useful quantitative target is to prove

$$
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le C\sqrt{\eta_D}\,D^2+O(\eta_D^2D^2)+o(D^2)
$$

for an absolute `C`, while retaining the PI/JC/Hemmi lower-vs-upper comparison above. Since SHX has a fixed area margin at slope one, any such continuous estimate would produce an explicit `eta_*>0` and upgrade RCC to

$$
L/D\ge1+\eta_*.
$$

That is now the shortest response-side quantitative target.

## 9. Compact handoff

```text
SHX closes exact RCC slope one.
Assume D epsilon->0 and L=(e_BB+2s_C)=D+o(D).
SAC gives total attachment-cell area=o(D^2), hence G=area(F)-o(D^2).
SOD gives y=h/D=q/D+o(1) in [1.5336,1.634964...].
Let p=per(F)/D, t=e_BB/D<=1. Since q<=per(F)<=b<=2h, y<=p<=2y and
min(y,p-y)=p-y.
PI + actual-perimeter JC:
    A_PI(y) <= (1+p-y)^2/(4pi),
so
    p >= p_req(y)=y-1+sqrt(4pi A_PI(y)) >3.039.
For p<=p2=12sin(pi/12), sharp Hemmi
    A_H(p)=3(p/p2)^2-(3+sqrt3)/2
has p-derivative >1.89 while JC capacity derivative <0.41.
At p=p_req(y), JC capacity=A_PI(y), and
    A_H(p_req(y))-A_PI(y)
 increases with y and is >0.007 already at y=1.5336.
Contradiction.
For p>=p2, the coarse Hemmi n=2 bound is >=(3-sqrt3)/2>0.633,
while JC capacity is <0.542. Contradiction.
Therefore no near-zero survivor can have L/D->1.
Next: quantitative SCC/SAC off slope one to obtain an explicit L/D>=1+eta.
```
