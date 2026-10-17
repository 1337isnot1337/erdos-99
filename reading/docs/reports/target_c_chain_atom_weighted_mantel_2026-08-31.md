> Generated reading edition · [exact source](../../../docs/reports/target_c_chain_atom_weighted_mantel_2026-08-31.md) · source SHA-256 `e98f2cb3261727c83becf3380115623940dd474dd72097afcdb8dbf7940f74b8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-ECB23883EA4C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C82: prescribed chain atom sharpens the pure-rhombic shell constants

**Date:** 2026-08-31  
**Repository base:** `a3c6f0bb` (main after C81 / PR #86)  
**Run type:** exact asymptotic cross-route extremal theorem  
**Target:** Target C C80 chain face + Target B Section 39 pure-rhombic exposed-hull theory  
**Depends on:** C80; Target B Section 39.1--39.4  
**Computation:** arithmetic only for displayed decimals

## LEVEL I STATUS

**STILL OPEN.**

C80 shows that an exact C76 chain face in a pure rhombic disk creates `D` distinct
train tracks with one common projective direction. Target B Section 39 already proves
that only the atomic part of the train-direction measure can carry positive-density
rhombus crossings, that its limiting crossing graph is triangle-free, and that exposed
hull chains force the total atomic train mass to satisfy

$$
s\le1-\frac y2,
\qquad
y:=\lim\frac qT.
$$

C82 inserts the **known atom of mass at least `D/T`** into the weighted Mantel step.
This gives a small but strict improvement of the pure-rhombic constants.

Put

$$
c:=\frac{2\sqrt3}{\pi},
\qquad
\Delta_2:=\frac1c=\frac\pi{2\sqrt3},
\qquad
A:=1+\Delta_2.
$$

Then every pure-rhombic asymptotic sequence admitting the exact C80 chain face obeys

$$
\boxed{
\frac TD
\ge
\frac{A}{1-y/2}+o(1).
}
$$

Consequently

$$
\boxed{
\liminf\frac TD
\ge
\frac43(1+\Delta_2)
=2.5425329094\ldots,
}
$$

improving Target B Section 39.7's `2.5395008183...`, and

$$
\boxed{
\liminf\frac{T-q}{D}
\ge
1+\Delta_2-\frac\pi2
=0.3361033553\ldots,
}
$$

improving Section 39.10's `0.3338292869...`.

The improvement is modest because the old weighted Mantel bound was already nearly
sharp. Its value is conceptual: the exact Target C chain face now has a quantitative
footprint in the mature Target B shell constants.

---

## 1. Limiting train notation

Use Target B Section 39 notation in a pure rhombic disk:

- `R` = number of rhombi;
- `T` = number of train tracks;
- `q` = number of convex-hull / diameter vertices;
- `mu_T` = empirical train-direction measure;
- `s` = total atomic mass of a weak limit `mu`;
- `y=q/T` asymptotically;
- `x=T/D` asymptotically.

Global minimum-diameter packing gives

$$
\frac{R}{D^2}\longrightarrow\Delta_2=\frac1c.
\tag{C82.1}
$$

Therefore

$$
\frac{R}{T^2}\longrightarrow\frac1{cx^2}.
\tag{C82.2}
$$

Target B Section 39 proves

$$
\boxed{s\le1-\frac y2}
\tag{C82.3}
$$

from exposed-hull chains.

---

## 2. C80 provides one prescribed atom

C80 gives `D` distinct train tracks in one exact projective direction. Therefore the
limiting train-direction measure has an atom of mass at least

$$
\boxed{a\ge\frac DT=\frac1x+o(1).}
\tag{C82.4}
$$

There may be additional trains with the same direction; only the lower bound is used.

Target B Section 39.1 shows that the limiting positive-density crossing graph lives on
the atomic directions and is triangle-free.

We need the weighted Mantel bound with one prescribed heavy atom.

---

## 3. Weighted Mantel with one prescribed atom

Let a finite triangle-free graph have nonnegative vertex weights of total mass `s`,
and suppose one distinguished vertex has weight `a`.

The ordinary weighted Mantel theorem gives edge weight at most `s^2/4`. If
`a<=s/2`, this remains the only needed bound.

If `a>s/2`, then

### Lemma C82.1 — heavy-vertex weighted Mantel

$$
\boxed{
\sum_{ij\in E}w_iw_j\le a(s-a).
}
\tag{C82.5}
$$

### Proof

Apply the standard Motzkin--Straus / Zykov symmetrization only to vertices other than
the distinguished one: if two residual vertices are nonadjacent, move all weight from
the one with smaller weighted degree to the one with larger weighted degree. This does
not decrease the weighted edge sum, preserves triangle-freeness, preserves the
specified weight `a`, and decreases the number of positive residual vertices unless
their weighted degrees agree. Iterating yields an extremizer whose positive residual
support is a clique, hence has size at most two.

If there is one residual vertex of weight `s-a`, the edge weight is at most
`a(s-a)`.

If there are two adjacent residual vertices of weights `b,c`, with
`b+c=s-a`, triangle-freeness prevents the distinguished vertex from being adjacent to
both. Assuming it is adjacent to `b`, the edge weight is at most

$$
ab+bc=b(a+c)=b(s-b).
$$

Since

$$
0\le b\le s-a<s/2,
$$

the function `b(s-b)` is increasing on this interval, and its maximum occurs at
`b=s-a`, giving `a(s-a)`. The case of no distinguished adjacency is smaller. `square`

The same statement passes to the atomic limiting crossing measure by finite
approximation, exactly as in Target B Section 39's weighted Mantel argument.

---

## 4. Insert the chain atom

Set

$$
S:=1-\frac y2.
$$

By C82.3, `s<=S`.

There are two cases.

### Case I: `1/x <= s/2`

Then

$$
x\ge\frac2s\ge\frac2S.
\tag{C82.6}
$$

Since

$$
A=1+\frac1c<2,
$$

this implies

$$
x\ge\frac AS.
\tag{C82.7}
$$

### Case II: `1/x > s/2`

The actual distinguished atom satisfies `a>=1/x>s/2`. Lemma C82.1 gives

$$
\frac1{cx^2}
\le a(s-a).
$$

For `a>s/2`, the function `a(s-a)` decreases as `a` increases. Therefore

$$
\frac1{cx^2}
\le
\frac1x\left(s-\frac1x\right)
\le
\frac1x\left(S-\frac1x\right).
$$

Multiplying by `x^2` gives

$$
\frac1c\le xS-1,
$$

hence again

$$
\boxed{
x\ge\frac{1+1/c}{S}=\frac A{1-y/2}.}
\tag{C82.8}
$$

Thus both cases yield the same universal chain-face refinement.

### Theorem C82 — chain-atom shell inequality

For every pure-rhombic asymptotic survivor admitting the exact C80 chain face,

$$
\boxed{
\frac TD
\ge
\frac{1+\Delta_2}{1-y/2}+o(1).
}
\tag{C82.9}
$$

Target B Section 39.6 has the same form with numerator

$$
\frac2{\sqrt c}=1.9046\ldots;
$$

C82 replaces it by

$$
1+\frac1c=1.9068996821\ldots .
$$

---

## 5. Improved train lower bound

Target B pinned rigidity gives

$$
y\ge\frac12+o(1).
$$

The right side of C82.9 increases with `y`, so

$$
\boxed{
\liminf\frac TD
\ge
\frac{4A}{3}
=
\frac43\left(1+\frac\pi{2\sqrt3}\right)
=2.5425329094\ldots .
}
\tag{C82.10}

This is a strict improvement of Section 39.7.

---

## 6. Improved exposed-hull ratio and neutral-space gap

Target B also gives

\[
q\le\pi D+o(D),
$$

or in `(x,y)` variables

$$
xy\le\pi+o(1).
\tag{C82.11}
$$

Combine with C82.9:

$$
\frac{Ay}{1-y/2}\le\pi.
$$

Therefore

$$
\boxed{
\limsup\frac qT
\le
\frac{\pi}{A+\pi/2}
=0.9033545903\ldots .
}
\tag{C82.12}
$$

This slightly improves Target B Section 39.9's `0.9039456812...`.

Finally,

$$
\frac{T-q}{D}=x(1-y).
$$

Using C82.9,

$$
\frac{T-q}{D}
\ge
A\frac{1-y}{1-y/2}+o(1).
$$

The function on the right decreases in `y`, so insert the largest allowed value from
C82.12. The algebra collapses exactly:

$$
\boxed{
\liminf\frac{T-q}{D}
\ge
A-\frac\pi2
=
1+\frac\pi{2\sqrt3}-\frac\pi2
=0.3361033553\ldots .
}
\tag{C82.13}

Since Target B Section 40 gives

\[
\dim\mathcal L\ge T-q,
$$

the same constant improves the macroscopic first-order-neutral train-space bound.

---

## 7. Interpretation

The improvement is intentionally small. A near-extremal triangle-free weighted
crossing graph can place the `D/T` chain atom on one side of an almost balanced
bipartition, so the ordinary weighted Mantel bound was already close to optimal.

C82 nevertheless records a genuine cross-route consequence:

```text
exact Target C chain face
    -> one train-direction atom of mass >=D/T
    -> prescribed-atom weighted Mantel loss
    -> larger T/D and (T-q)/D constants
    -> slightly larger Target B neutral train-angle space.
```

This increases, rather than decreases, the higher-order blocker burden identified by
C80-C81.

---

## 8. What remains

C82 does not make the neutral-space lower bound exceed the `D-1` chain-bending rank,
and it does not force `q<D`. Therefore dimension counting still cannot guarantee that
`mathcal L` bends the C80 chain atom.

The real next target remains one of:

1. prove one-edge beta concentration from C66's star-center concentration, unlocking
   C81; or
2. use the interval structure of diameter gradients on the ordered `D` chain tracks to
   bound the rank of their restrictions more sharply than the raw `q` count; or
3. combine the C80 negative variance with Target B's backward/tangent blocker map and
   the exposed-hull shortage of non-hull terminal train ends.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C80 gives a train-direction atom a>=D/T=1/x.
Target B gives total atomic mass s<=1-y/2 and crossing density R/T^2->1/(c x^2).
Weighted Mantel with one fixed atom:
  if 1/x<=s/2, x>=2/s;
  if 1/x>s/2, edge mass <=(1/x)(s-1/x), so x>= (1+1/c)/s.
Therefore always
  x=T/D >= (1+1/c)/(1-y/2)+o(1).
Consequences:
  liminf T/D >=2.5425329094...,
  limsup q/T <=0.9033545903...,
  liminf (T-q)/D >=0.3361033553....

Next: leaf selection, interval-rank on the D chain tracks, or blocker/end-budget coupling.
```
