> Generated reading edition · [exact source](../../../docs/reports/target_c_post_zf_incidence_population_bridge_2026-09-09.md) · source SHA-256 `2fa596ac28baaaed261359ab8bb14051b45acede2ee8dfc7fa45df3e63229207`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C43761FA448C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — post-ZF incidence and isolate-population bridge

**Date:** 2026-09-09  
**Repository base:** `be9cbfb78cbda059fb4c2581118b236729cfad84`  
**Run type:** exact post-ZF synthesis / population reduction  
**Target:** Target C Gate C-II / Level I  
**LEVEL I STATUS:** STILL OPEN

This report combines the exact post-ZF ledger ZU with the older C37--C40 attachment
and component-diameter theorems. The linear `q` terms cancel. The result is an exact
identity controlling the entire graph-diameter content of the unloaded contact
components by the loaded-loaded contact count and the extra pinned-contact stress
nullity.

A second exact incidence identity resolves the gap between full mixed stress defect and
pinned-contact defect into planar attachment slacks. Finally, the component-diameter
identity gives a quantitative population theorem: if the loaded-loaded/pinned-stress
currency is sublinear in `D`, then the nonisolated contact core is `o(D^2)` and a
quadratic population of source points is necessarily contact-isolated.

This does not exclude that isolate-heavy branch. It identifies it exactly as the
population obstruction that must be supplied by global optimality / source capacity.

## 1. Inputs and notation

Use the post-ZF notation of
`target_c_zf_exact_defect_budget_addendum_2026-09-09.md`:

- `q=|B_+|` loaded diameter endpoints;
- `c_I` components `I_r` of `C[V(C)\setminus B_+]`;
- `e_BB` loaded-loaded unit contacts;
- `s_C>=0` extra pinned-contact left-nullity beyond one mandatory positive-stress
  relation per unloaded component;
- `d_H=q-h>=0` diameter-graph tree-component defect;
- `s_Z=e+h-(2v-2)>=0` extra mixed-framework row dependencies beyond the mandatory KKT
  relation.

Put

$$
\boxed{k:=d_H+s_Z.}
\tag{1.1}
$$

ZU gives the exact identity

$$
\boxed{c_I+e_{BB}+s_C=q-2+k.}
\tag{1.2}
$$

For each unloaded component let

- `delta_r` be the graph diameter of `C[I_r]`, with `delta_r=0` for a singleton;
- `t_r` be the number of contact edges from `I_r` to `B_+`.

C40 proves

$$
\boxed{t_r\ge\delta_r+3}
\tag{1.3}
$$

and

$$
\boxed{
\sum_r\delta_r+3c_I+2e_{BB}\le3q.
}
\tag{1.4}
$$

C35 gives loaded degree at most three.

## 2. Theorem ZI — exact component-diameter / boundary-degree ledger

Define the nonnegative component attachment surplus

$$
\boxed{
U:=\sum_r\bigl(t_r-\delta_r-3\bigr)\ge0
}
\tag{ZI.1}
$$

and the nonnegative loaded contact-degree slack

$$
\boxed{
s_B:=3q-e_{BI}-2e_{BB}\ge0,
}
\tag{ZI.2}
$$

where `e_BI=sum_r t_r`.

Then every post-ZF survivor satisfies the exact identity

$$
\boxed{
\sum_r\delta_r+U+s_B+3(d_H+s_Z)
=6+e_{BB}+3s_C.
}
\tag{ZI.3}
$$

In particular

$$
\boxed{
\sum_r\delta_r
\le 6-3(d_H+s_Z)+e_{BB}+3s_C
\le6+e_{BB}+3s_C.
}
\tag{ZI.4}
$$

and

$$
\boxed{
3(d_H+s_Z)\le6+e_{BB}+3s_C.
}
\tag{ZI.5}
$$

### Proof

By definition of `U`,

$$
e_{BI}=\sum_rt_r
=\sum_r\delta_r+3c_I+U.
$$

Insert this in ZI.2:

$$
s_B
=3q-\sum_r\delta_r-3c_I-U-2e_{BB}.
$$

ZU gives

$$
c_I=q-2+k-e_{BB}-s_C.
$$

Substitute and cancel `3q`:

$$
\begin{aligned}
s_B
&=3q-\sum_r\delta_r
 -3(q-2+k-e_{BB}-s_C)-U-2e_{BB}\\
&=6-3k+e_{BB}+3s_C-\sum_r\delta_r-U.
\end{aligned}
$$

Rearrangement is ZI.3. Nonnegativity gives ZI.4--ZI.5. `square`

### Why ZI is stronger than the pre-ZF C40 bound

C40 by itself says only `sum delta_r=O(q)=O(D)`. ZI cancels the full `q` term. If
`e_BB+s_C=o(D)`, then

$$
\sum_r\delta_r=o(D).
$$

Thus a source can have linearly many unloaded components while their **total** internal
graph diameter is sublinear.

## 3. Theorem ZJ — exact planar-incidence defect decomposition

Assume `c_I>0`. Use C37--C38 notation:

- `q_used`: loaded terminals belonging to at least one attachment set;
- `s>=1`: connected components of the attachment-incidence graph containing an
  unloaded-component node;
- `a=sum_r|A_r|`: distinct attachment incidences.

Define four exact nonnegative slacks:

$$
\boxed{u_A:=a-3c_I\ge0,}
\tag{ZJ.1}
$$

$$
\boxed{p_A:=q_{used}+2c_I-2s-a\ge0,}
\tag{ZJ.2}
$$

$$
\boxed{u_0:=q-q_{used}\ge0,}
\tag{ZJ.3}
$$

and, from C38,

$$
\boxed{
r_Q:=e_{BB}-\bigl(s+u_0-1\bigr)\ge0.}
\tag{ZJ.4}
$$

Then

$$
\boxed{
e_{BB}+s_C-k
=u_A+p_A+2(s-1)+u_0.
}
\tag{ZJ.5}
$$

Equivalently,

$$
\boxed{
s_C+r_Q
=k+u_A+p_A+(s-1).
}
\tag{ZJ.6}
$$

Consequently

$$
\boxed{k=d_H+s_Z\le s_C+r_Q\le s_C+e_{BB}.}
\tag{ZJ.7}
$$

### Proof

The definitions of `u_A,p_A` give

$$
q_{used}
=a-2c_I+2s+p_A
=c_I+u_A+p_A+2s.
$$

Adding `u_0=q-q_used` yields

$$
q=c_I+u_A+p_A+2s+u_0.
\tag{ZJ.8}
$$

ZU, written with `k`, is

$$
q=c_I+e_{BB}+s_C+2-k.
\tag{ZJ.9}
$$

Cancel `c_I` between ZJ.8 and ZJ.9 to obtain ZJ.5.

C38 and ZJ.4 give

$$
e_{BB}=s+u_0-1+r_Q.
$$

Insert this into ZJ.5 and cancel `u_0`; the result is ZJ.6. Since every term on
the right of ZJ.6 except `k` is nonnegative and `r_Q<=e_BB`, ZJ.7 follows. `square`

### Clean-incidence equality case

If `c_I>0` and

$$
e_{BB}=s_C=0,
$$

then C38 forces `s=1`, `u_0=0`, `r_Q=0`; ZJ.6 then forces

$$
\boxed{k=u_A=p_A=0.}
\tag{ZJ.10}
$$

ZU becomes

$$
\boxed{c_I=q-2.}
\tag{ZJ.11}
$$

Thus every unloaded component has exactly three distinct loaded attachments, every
loaded terminal is used, the attachment incidence graph is connected, and C37's
planar Euler bound is exact. ZI further gives

$$
\boxed{
\sum_r\delta_r+U+s_B=6.
}
\tag{ZJ.12}
$$

Hence only a constant total amount of internal graph diameter, excess boundary
attachment, or loaded-degree deficit survives in this exact zero-surplus phase.

This is a much more rigid object than the old generic noncrossing-attachment normal
form. It is combinatorially the equality regime of the bipartite planar incidence
bound, closely analogous to the vertex/face incidence graph of a triangulation of the
loaded polygon. No geometric triangulation classification is asserted here.

## 4. Theorem ZP — small boundary/stress surplus forces quadratic isolates

Let

$$
\boxed{
L:=6-3(d_H+s_Z)+e_{BB}+3s_C.
}
\tag{ZP.1}
$$

ZI shows `L>=0` and

$$
\sum_r\delta_r\le L.
\tag{ZP.2}
$$

C40's elementary packing estimate gives, for `n_r=|I_r|`,

$$
\boxed{n_r\le(2\delta_r+1)^2.}
\tag{ZP.3}
$$

Therefore the nonisolated contact-core population satisfies

$$
\boxed{
 v
 \le q+c_I+4L^2+4L
 \le2q+4L^2+4L
 \le2\pi D+4L^2+4L.
}
\tag{ZP.4}
$$

### Proof

Sum ZP.3:

$$
\sum_rn_r
\le c_I+4\sum_r\delta_r^2+4\sum_r\delta_r.
$$

The `delta_r` are nonnegative, so

$$
\sum_r\delta_r^2
\le\left(\sum_r\delta_r\right)^2
\le L^2.
$$

Hence

$$
\sum_rn_r\le c_I+4L^2+4L.
$$

The core consists of the `q` loaded terminals and the unloaded vertices. C37 gives
`c_I<=q` whenever `c_I>0`, while it is trivial if `c_I=0`. Thus

$$
v\le2q+4L^2+4L.
$$

Finally the convex diameter-endpoint polygon has unit-separated consecutive vertices
and perimeter at most `pi D`, so `q<=pi D`. This proves ZP.4. `square`

### Asymptotic isolate consequence

For global minimizers the canonical lattice/Oler bounds give

$$
\frac n{D^2}\longrightarrow
\Delta:=\frac\pi{2\sqrt3}.
\tag{ZP.5}
$$

If along a post-ZF sequence

$$
\lambda:=\limsup\frac{e_{BB}+3s_C}{D},
$$

then `L/D<=lambda+o(1)`, so ZP.4 gives

$$
\boxed{
\limsup\frac v{D^2}\le4\lambda^2.
}
\tag{ZP.6}
$$

and hence

$$
\boxed{
\liminf\frac{n-v}{D^2}
\ge
\Delta-4\lambda^2.
}
\tag{ZP.7}
$$

whenever the right side is positive.

In particular:

### Corollary ZP.1 — sublinear surplus is isolate-dominated

If

$$
e_{BB}+s_C=o(D),
$$

then

$$
\boxed{v=o(D^2)}
\tag{ZP.8}
$$

and

$$
\boxed{
\frac{n-v}{D^2}\longrightarrow
\frac\pi{2\sqrt3}.
}
\tag{ZP.9}
$$

Thus asymptotically **all quadratic source population is contact-isolated** in this
branch; the force-visible core contains only a negligible fraction on the `D^2`
scale.

More quantitatively, a positive quadratic isolate density is forced whenever

$$
\limsup\frac{e_{BB}+3s_C}{D}
<\frac12\sqrt{\frac\pi{2\sqrt3}}
=0.476\ldots .
\tag{ZP.10}
$$

No contradiction is claimed: the repository already identifies isolate control as a
missing global source-capacity theorem.

## 5. Effect on the post-ZF branch split

The old ZU trichotomy was

```text
at least one of c_I, e_BB, s_C is linear in D.
```

ZI/ZP sharpen it materially:

```text
small e_BB + s_C
    -> total unloaded-component graph diameter is sublinear
    -> nonisolated core population is o(D^2)
    -> quadratic source population is contact-isolated.

otherwise
    -> loaded-loaded contacts and/or extra pinned-contact stress nullity
       carry a genuine linear-scale currency.
```

So the many-`c_I` branch is no longer an independent diffuse possibility. If it is
not accompanied by a linear `e_BB` or `s_C`, it collapses into the explicit
isolate-heavy source branch.

This is a direct bridge between the Target C post-ZF ledger and the population
obstruction that previously appeared only as a warning in the defect-train campaign.

## 6. Binding regressions

- **Regular odd shell:** `c_I=s_C=0`, `e_BB=q`, so it lies in the linear `e_BB`
  branch and does not violate ZP.
- **Unit square:** likewise has linear-at-its-scale loaded-loaded contacts; it is below
  the large-source regime.
- **Many singleton harmonic cells:** allowed. ZJ shows the zero-surplus endpoint is
  exactly a maximal planar attachment-incidence regime; ZP says its core remains only
  `O(D)` plus constant-population defects.
- **Quadratic isolated fillings:** explicitly allowed. They are the obstruction exposed
  by ZP, not a counterexample to it.
- **Pentagonal exceptional faces:** untouched; no local area charge is used.

## 7. Exact remaining lemmas

ZP exposes two clean high-value targets.

### Population target

Prove that a sufficiently large triangle-free global minimizer in the lexicographic
C-II normalization cannot have

$$
n-v=\Theta(D^2)
$$

contact-isolated source points while the force-visible core has diameter `D`.

Any exact source-capacity or finite same-`D` replacement theorem that gives
`n-v=o(D^2)` would combine with ZP to force

$$
e_{BB}+s_C=\Omega(D).
$$

### Linear-surplus target

In the complementary branch, convert

$$
e_{BB}+3s_C=\Omega(D)
$$

into either the direct face inequality

$$
b+\sum_F(\deg F-4)>2h
$$

or a strict sub-`D` competitor. ZJ shows that `s_C` must also pay for the mixed defect
`d_H+s_Z` after the loaded-loaded contacts needed merely for quotient connectivity are
removed.

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| ZI exact diameter/degree identity | proved | ZU + definitions + C35/C40. |
| ZJ incidence decomposition | proved | Exact C37/C38 slacks + ZU. |
| `d_H+s_Z<=s_C+r_Q` for `c_I>0` | proved | Immediate from ZJ.6. |
| clean `e_BB=s_C=0` incidence normal form | proved | C38 + ZJ + ZU + ZI. |
| ZP core-population upper bound | proved | ZI + C40 packing + `q,c_I<=q`. |
| sublinear surplus -> quadratic isolates | proved | ZP + canonical `n/D^2->Delta`. |
| quadratic isolates impossible globally | **not proved** | This is the remaining source-capacity obstruction. |
| linear `e_BB` or `s_C` closes Level I | **not proved** | Still needs geometry/global optimality. |

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let k=d_H+s_Z. Post-ZF ZU says
    c_I+e_BB+s_C=q-2+k.

New exact cross-ledger:
    sum delta_r + U + s_B + 3k = 6+e_BB+3s_C,
where
    U=sum(t_r-delta_r-3)>=0,
    s_B=3q-e_BI-2e_BB>=0.

If c_I>0, exact incidence slacks give
    e_BB+s_C-k=u_A+p_A+2(s-1)+u_0,
    s_C+r_Q=k+u_A+p_A+s-1,
so
    k<=s_C+r_Q<=s_C+e_BB.

Population consequence: with
    L=6-3k+e_BB+3s_C,
    v<=2pi D+4L^2+4L.
Therefore if e_BB+s_C=o(D), then
    v=o(D^2),
    (n-v)/D^2 -> pi/(2sqrt(3)).

Remaining dichotomy:
1. quadratic contact-isolated population, requiring a source-capacity/global-optimality exclusion; or
2. linear loaded-loaded contacts / pinned-contact stress surplus, requiring a face or response contradiction.
```
