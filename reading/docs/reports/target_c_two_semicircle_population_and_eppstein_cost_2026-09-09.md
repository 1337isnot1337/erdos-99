> Generated reading edition · [exact source](../../../docs/reports/target_c_two_semicircle_population_and_eppstein_cost_2026-09-09.md) · source SHA-256 `ef0b99f25366586240bac36eac69a31ca7c49df87c06b3ab3a10148b3c07a3da`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DF4C8B5E2207","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cap-minimal full-core equality forces two half-density carriers and linear Eppstein slack

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** equality-regime classification / local penny-graph edge theorem  
**Target:** UF/TD full-core near-circle endpoint  
**Depends on:** TD, repaired LC/TR, C36/C44/C49, component Oler capacity, ZK, NBd; Eppstein's triangle-free penny-graph isoperimetric edge bound  
**External source:** David Eppstein, *Edge Bounds and Degeneracy of Triangle-Free Penny Graphs and Squaregraphs*, JGAA 22(3) (2018), 483--499, Theorem 4. This source is already indexed in the repository and stored as `papers/primary/463.pdf`.  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

TD proves that in the asymptotically full-core near-circle branch,

$$
S:=\sum_r\delta_r\ge(2-o(1))D.
$$

This report classifies the leading equality case

$$
\boxed{S/D\to2.}
\tag{TS.0}
$$

It proves that the two semicircle-scale cap-defining harmonic components are themselves asymptotically half of the entire two-dimensional core:

$$
\boxed{
\frac{n_1}{D^2}\to\frac\Delta2,
\qquad
\frac{n_2}{D^2}\to\frac\Delta2,
\qquad
\Delta=\frac\pi{2\sqrt3}.
}
\tag{TS.1}

$$

All other unloaded components together contain only `o(D^2)` vertices.

This makes Eppstein's general triangle-free penny-graph isoperimetric edge theorem effective on the two actual components. Each component then requires at least

$$
\boxed{
 t_i\ge
\left(\frac\pi{2\sqrt2}-o(1)\right)D
}
\tag{TS.2}
$$

physical contacts to loaded terminals, and its internal Eppstein slack obeys

$$
\boxed{
 r_i\ge
\left(\frac\pi{2\sqrt2}-1-o(1)\right)D.
}
\tag{TS.3}

$$

Therefore the global ZK slack satisfies

$$
\boxed{
R_I\ge
\left(\frac\pi{\sqrt2}-2-o(1)\right)D
= (0.2214414690\ldots-o(1))D.
}
\tag{TS.4}

$$

Inserted into NBd, the full-core cap-minimal endpoint leaves at most

$$
\boxed{
\left(\pi-\frac\pi{\sqrt2}+o(1)\right)D
=(0.9201511845\ldots+o(1))D
}
\tag{TS.5}

$$

for the combined currencies

$$
s_B+2E_{BB}+3c_I+s_C
$$

after the two harmonic graph diameters and their unavoidable internal penny-graph edge deficits are paid.

This is a genuine new boundary-order charge, but it does not yet close Level I.

---

## 1. Full-core and cap-minimal hypotheses

Work along a PR #119 near-circle subsequence with

$$
\frac{n-v}{D^2}\to0.
\tag{1.1}
$$

The global density asymptotic gives

$$
\frac n{D^2}\to\Delta,
$$

so

$$
\boxed{
\frac v{D^2}\to\Delta.
}
\tag{1.2}
$$

The loaded terminal count is only linear,

$$
q=O(D),
$$

hence the unloaded harmonic population satisfies

$$
\boxed{
\sum_r n_r=v-q=(\Delta+o(1))D^2.
}
\tag{1.3}
$$

Assume additionally the leading cap-cost equality TS.0:

$$
S/D\to2.
$$

TD's strict cap-efficiency optimization then gives two inclusion-maximal cap-defining components, call them `I_1,I_2`, such that

$$
\boxed{
\delta_1/D\to1,
\qquad
\delta_2/D\to1,
}
\tag{1.4}

$$

and their attachment arcs converge to complementary semicircles.

Since `S=delta_1+delta_2+sum_(r>=3) delta_r`, (1.4) and TS.0 imply

$$
\boxed{
S_{rest}:=\sum_{r\ge3}\delta_r=o(D).
}
\tag{1.5}

$$

---

## 2. The remaining components have subquadratic population

For every component `I_r`, C36 puts it inside its convex attachment cell `P_r`, and C44 gives

$$
\operatorname{diam}(P_r)\le\delta_r+2.
$$

Applying Oler to the `n_r` unit-separated vertices of `I_r` and then the isodiametric and perimeter-diameter bounds gives the finite component capacity already recorded in QP:

$$
\boxed{
 n_r
\le
1+\Delta(\delta_r+2)^2
+\frac\pi2(\delta_r+2).
}
\tag{2.1}

$$

Sum (2.1) over `r>=3`. Since

$$
\sum_{r\ge3}\delta_r^2
\le
\left(\sum_{r\ge3}\delta_r\right)^2
=S_{rest}^2=o(D^2),
$$

and the total number of components satisfies `c_I=O(D)`, all constant and linear terms contribute only `o(D^2)+O(D)`. Hence

$$
\boxed{
\sum_{r\ge3} n_r=o(D^2).
}
\tag{2.2}

$$

Combining with (1.3),

$$
\boxed{
 n_1+n_2=(\Delta+o(1))D^2.
}
\tag{2.3}

$$

Thus the two cap-defining components carry asymptotically the entire force-visible bulk.

---

## 3. Each semicircle cap has capacity at most `Delta/2`

The repaired LC/TR equality classification gives that `P_1/D` and `P_2/D` lie asymptotically in complementary semicircular caps of the radius-`1/2` disk. Each limiting cap has area

$$
\frac\pi8.
\tag{3.1}
$$

More precisely,

$$
\operatorname{area}(P_i)
\le
\left(\frac\pi8+o(1)\right)D^2,
\qquad i=1,2.
\tag{3.2}
$$

Also `per(P_i)=O(D)` because `diam(P_i)<=D+o(D)`.

Apply Oler to the `n_i` vertices of `I_i` inside `P_i`:

$$
a_0(n_i-1)
\le
\operatorname{area}(P_i)
+\frac{a_0}{2}\operatorname{per}(P_i),
\qquad a_0=\frac{\sqrt3}{2}.
$$

Divide by `D^2` and use (3.2):

$$
\limsup\frac{n_i}{D^2}
\le
\frac{\pi/8}{a_0}
=
\frac\pi{4\sqrt3}
=
\frac\Delta2.
\tag{3.3}
$$

Since (2.3) says the two limits sum to `Delta`, both upper bounds must be equalities. Therefore

$$
\boxed{
\frac{n_1}{D^2}\to\frac\Delta2,
\qquad
\frac{n_2}{D^2}\to\frac\Delta2.
}
$$

This proves TS.1.

The same squeeze also gives

$$
\boxed{
\operatorname{area}(P_i)/D^2\to\pi/8,
}
\tag{3.4}
$$

so each component asymptotically fills its semicircular attachment cap at the optimal planar packing density at leading order.

---

## 4. Eppstein's isoperimetric edge theorem

Eppstein's Theorem 4 states that an `m`-vertex triangle-free penny graph has at most

$$
\boxed{
2m-rac12\sqrt{2\pi\sqrt3\,m}+O(1)
}
\tag{4.1}
$$

edges.

Each internal graph `C[I_i]` is a triangle-free penny graph: it is an induced subgraph of the unit-contact graph on the source vertices `I_i`. Therefore

$$
e_i
\le
2n_i-rac12\sqrt{2\pi\sqrt3\,n_i}+O(1).
\tag{4.2}
$$

The component pinned-stress identity is

$$
s_i=e_i+t_i-2n_i-1\ge0,
$$

or

$$
t_i=2n_i+1+s_i-e_i.
\tag{4.3}
$$

Insert (4.2):

$$
\boxed{
 t_i
\ge
\frac12\sqrt{2\pi\sqrt3\,n_i}
+1+s_i-O(1).
}
\tag{4.4}

$$

Using TS.1,

$$
\sqrt{n_i}
=
\left(\sqrt{\frac\Delta2}+o(1)\right)D.
$$

The coefficient simplifies exactly:

$$
\frac12\sqrt{2\pi\sqrt3}\sqrt{\frac\Delta2}
=
\frac12\sqrt{2\pi\sqrt3}\sqrt{\frac\pi{4\sqrt3}}
=
\boxed{\frac\pi{2\sqrt2}}.
\tag{4.5}
$$

Therefore

$$
\boxed{
 t_i
\ge
\left(\frac\pi{2\sqrt2}-o(1)\right)D,
}
$$

proving TS.2.

Numerically,

$$
\frac\pi{2\sqrt2}=1.1107207345\ldots .
$$

So each diameter-scale component needs about `11.07%` more loaded attachment contacts than the bare C40 graph-diameter lower bound `t_i>=delta_i+3` detects.

---

## 5. Convert the edge deficit into exact ZK currency

ZK defines the internal Eppstein slack

$$
r_i:=2n_i-\delta_i-2-e_i\ge0.
\tag{5.1}
$$

Using (4.2),

$$
r_i
\ge
\frac12\sqrt{2\pi\sqrt3\,n_i}
-\delta_i-2-O(1).
\tag{5.2}
$$

Now TS.1 and (1.4) give

$$
\boxed{
 r_i
\ge
\left(\frac\pi{2\sqrt2}-1-o(1)\right)D.
}
\tag{5.3}
$$

Since

$$
R_I=\sum_r r_r,
$$

summing `i=1,2` yields

$$
R_I
\ge
\left(\frac\pi{\sqrt2}-2-o(1)\right)D.
\tag{5.4}
$$

This proves TS.4.

Numerically,

$$
\frac\pi{\sqrt2}-2
=0.221441469079\ldots .
$$

The charge is unweighted and belongs to an exact nonnegative currency already present in ZK/NBd. It is not an informal geometric inefficiency term.

---

## 6. Insert the exact near-circle boundary budget

NBd proves

$$
S+R_I+s_B+2E_{BB}+3c_I+s_C
=q+2x_B.
\tag{6.1}
$$

In the near-circle endpoint,

$$
q/D\to\pi,
\qquad
x_B=o(D).
$$

Under TS.0,

$$
S/D\to2.
$$

Together with TS.4, (6.1) gives

$$
\begin{aligned}
 s_B+2E_{BB}+3c_I+s_C
&\le
\left[\pi-2-\left(\frac\pi{\sqrt2}-2\right)+o(1)\right]D\\
&=
\boxed{
\left(\pi-\frac\pi{\sqrt2}+o(1)\right)D.
}
\end{aligned}
\tag{6.2}
$$

Numerically,

$$
\pi-\frac\pi{\sqrt2}
=0.920151184511\ldots .
$$

This proves TS.5.

---

## 7. Equality normal form after TS

A full-core near-circle survivor satisfying the minimum possible TD diameter cost now has all of the following simultaneously:

```text
force hull -> disk of diameter D
q = (pi+o(1))D loaded terminals
almost all consecutive loaded hull pairs are unit contacts
S = (2+o(1))D
exactly two macroscopic cap-defining harmonic components I1,I2
attachment cells -> complementary semicircles
n1,n2 = (Delta/2+o(1))D^2
area(P1),area(P2) = (pi/8+o(1))D^2
delta1,delta2 = (1+o(1))D
t1,t2 >= (pi/(2sqrt2)-o(1))D
R_I >= (pi/sqrt2-2-o(1))D
all other harmonic components carry o(D^2) population
remaining NBd currency <= (pi-pi/sqrt2+o(1))D.
```

This is substantially more rigid than the earlier “two dense half-meshes” heuristic: the half-density population and the linear internal edge deficit are now forced theorems in the cap-minimal branch.

---

## 8. What this does not prove

The theorem does **not** show that either `C[I_i]` is a squaregraph or a rhombic disk. Eppstein's Theorem 4 applies to every triangle-free penny graph and is deliberately weaker than the sharp squaregraph bound.

It also does not imply that the lower bound on `t_i` is attained. Extra pinned stress or additional internal edge deficit only makes the NBd budget more expensive, which is favorable for future work.

The remaining scalar allowance `0.92015...D` is still positive, so no Level I contradiction follows from TS alone.

---

## 9. Next target

The two components each have asymptotically optimal packing density inside a semicircular cap and are simultaneously close to the extremal edge-density regime if the NBd budget is to remain feasible.

The highest-value next theorem is therefore a **semicircle penny-graph stability theorem**:

> for a triangle-free penny graph with `(Delta/2+o(1))D^2` vertices embedded in a diameter-`D` semicircular cap and with graph diameter `(1+o(1))D`, improve Eppstein's generic edge deficit
> 

$$

> \frac\pi{2\sqrt2}D
> 
$$


> by exploiting the one-sided cap boundary and the positive pinned equilibrium.

A per-component improvement above

$$
\frac\pi{2\sqrt2}D
$$

feeds linearly into `R_I`. Any theorem pushing the combined `R_I` and unavoidable interface currencies beyond `pi-2` would close the cap-minimal full-core branch.
