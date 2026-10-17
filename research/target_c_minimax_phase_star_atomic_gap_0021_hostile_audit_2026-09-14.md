<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "1bd6580948d90d41a73cada0a2decd48e85ed5c0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_minimax_phase_star_atomic_gap_0021_hostile_audit_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d8d11c9bbd5050fbfcabb07c3ea86dd00c65a1c307b914bdba633c008369e2d3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit: minimax phase-star atomic gap 0.0021

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Object audited:** `target_c_minimax_phase_star_atomic_gap_0021_2026-09-14.md` (`30ce7661`)
**Disposition:** PASS as a proof-only theorem candidate; theorem-state authority unchanged
**LEVEL I STATUS:** `STILL OPEN`

This audit checks the new step in the `g=0.0021` atomic-gap theorem rather than merely
rerunning its arithmetic.  The points most capable of invalidating the claimed gain are:

1. the conversion of triangle-freeness into the weighted two-leaf deficit inequality;
2. the lower bound on the weighted best leaf;
3. the one-dimensional interval relaxation and its monotonicity directions;
4. the common-neighbor thresholds after pruning; and
5. the transfer from the all-train graph to the rhombic-only graph.

All five checks pass.  The exact companion scripts also pass unchanged.

## 1. Dominant-orbit deficit bookkeeping — PASS

Let the dominant orbit have total mass `W` and crossing mass `E`, and let the remaining
orbit mass be `R=A-W`.  With

\[
\delta={W^2\over4}-E,
\]

the note uses

\[
{A^2\over4}-\Delta_2-\delta
={A^2-W^2\over4}-\sum_{r\ne r_*}E_r.
\]

Since each other orbit obeys `E_r<=M_r^2/4` and
`sum M_r=R`,

\[
\sum_{r\ne r_*}E_r
\le {1\over4}\sum M_r^2
\le {R^2\over4}.
\]

Also `A^2-W^2=R(2W+R)`.  Therefore

\[
{A^2\over4}-\Delta_2-\delta
\ge {R(2W+R)-R^2\over4}={RW\over2}\ge0.
\]

Thus

\[
\delta\le {A^2\over4}-\Delta_2
\]

is in the correct direction.  No unproved additivity of Mantel deficits is used.

## 2. Weighted center-leaf inequality — PASS

Write the three dominant phase-window populations as

\[
C\ge U\ge V\ge0,
\]

and define the missing center-leaf pair masses

\[
x=CU-e(C,U),\qquad y=CV-e(C,V).
\]

Let `e_UV=e(U,V)`.  For every actual `UV` crossing, triangle-freeness says that the
center neighborhoods of its two endpoints are disjoint.  Hence

\[
\deg_C(u)+\deg_C(v)\le C.
\]

Summing over all `UV` edges gives

\[
C e_{UV}
\le \sum_{uv\in E(U,V)}
\bigl[(C-\deg_Cu)+(C-\deg_Cv)\bigr].
\]

Each missing-center count at a vertex of `U` is repeated at most `V` times, and each
such count at a vertex of `V` at most `U` times.  Therefore

\[
\boxed{C e_{UV}\le Vx+Uy.}
\]

With

\[
a=1-{V\over C},\qquad b=1-{U\over C},
\]

and

\[
h=C(U+V)-E=x+y-e_{UV},
\]

this yields exactly

\[
\boxed{ax+by\le h.}
\]

This is the theorem's key new correlation.  It is occurrence-safe because the crossing
graph vertices are complete stopped trains and strict rhombi are its simple edges.

## 3. Weighted best-leaf lower bound — PASS

For one leaf `L` with missing-pair mass `m`, the previously audited opposite-corner
mechanism uses

\[
F(C,L,m)=C+L-6\sqrt m.
\]

The theorem takes the positive weighted average with weights `a,b`.  Cauchy--Schwarz
and the previous section give

\[
{a\sqrt x+b\sqrt y\over a+b}
\le \sqrt{{h\over a+b}}.
\]

Put `L=U+V=W-C`.  Direct algebra gives

\[
{aU+bV\over a+b}
={CL-2UV\over2C-L}.
\]

Because `UV<=L^2/4`,

\[
{CL-2UV\over2C-L}
\ge {CL-L^2/2\over2C-L}={L\over2}.
\]

The denominator is positive on the certified domain: the atomic deficit gives
`C=W/2+z` with `|z|<0.045`, while `W>1.9025`, so `3C-W>0` by a wide margin.
Consequently

\[
\boxed{
\max(F_U,F_V)
\ge {W+C\over2}-6\sqrt{h\,{C\over3C-W}}.
}
\]

No simultaneous worst-case choice of the two leaf deficits is made.

## 4. Interval relaxation — PASS

Set `C=W/2+z`.  The lower bound becomes

\[
{3W\over4}+{z\over2}
-6\sqrt{(d_0-z^2){W+2z\over W+6z}}.
\]

The verifier covers `[-0.045,0.045]`; the actual domain is strictly smaller because
`0.045^2>d_0`.

For `z<0`,

\[
R(W,z)={W+2z\over W+6z}
\]

has

\[
\partial_W R={4z\over(W+6z)^2}<0,
\qquad
\partial_z R={-4W\over(W+6z)^2}<0.
\]

Thus replacing `W` by its lower bound and `z` by the left endpoint gives an **upper**
bound on the loss factor, exactly as the script does.  For `z>=0`, `R<=1`, also as
used by the script.  The raw term increases in both `W` and `z`, so its lower endpoint
choices are safe.

The exact-Fraction grid certifies

\[
\max(F_U,F_V)>1.15618192450409\ldots
>{2\over\sqrt3}+0.00148138\ldots .
\]

The worst interval is `[-0.00585,-0.00580]`. The square-root routine rounds upward,
so the sign is not floating-point dependent. The later hardening commit `17e08323`
also derives and checks the outward `sqrt(Delta_2)` bracket directly from certified
bounds on `pi` and `sqrt(3)`, removing the one non-self-contained numerical input in
the original verifier without changing the certified margin.

## 5. Common-neighbor pruning — PASS

For the selected center-leaf pair write `p=sqrt(m)`.  The certified effective degree
sum satisfies

\[
C+L-6p>{2\over\sqrt3}.
\]

The verifier separately proves `C<2/sqrt(3)`, hence `L>6p`.  It also bounds every
selected `p` by `(A-2/sqrt(3))/6` and proves the uniform lower bound `C>5p`.
After one `pD` phase-order deletion and one `pD` high-missing-degree deletion per
shore, the retained center and leaf populations remain above the triple-common-neighbor
thresholds used by the already-audited Section-163 globalization.  The theorem does
not silently assume an exact biclique.

## 6. Rhombic-only transfer — PASS, with inherited scope

The claim

\[
\liminf {T_R\over D}\ge2\sqrt{\Delta_2}+0.0021,
\qquad
\liminf {\sigma_R\over D}\ge0.0042
\]

is not obtained by deleting singleton trains from an already-selected all-train pair.
It uses the same argument on the strict-rhombus crossing graph itself.  This transfer
inherits the previously audited facts used in the explicit-rhombic-train theorem:

- vertices are non-singleton complete rhombic trains;
- the graph is simple and triangle-free;
- its edge count is exactly `R_4`;
- the limiting crossing relation is still supported at projective separation `pi/3`;
- the same finite `K_{2,2}`/order mechanism applies to selected rhombic train families.

Under that established transfer, the `g=0.0021` minimax proof applies verbatim.  This
audit does not promote those inherited rhombic-transfer premises beyond their existing
proof-only status.

## 7. Section-171 propagation — PASS

The companion exact-rational script checks the new endpoint

\[
t_0=C_{146}+0.0017279,
\qquad
\delta_0=0.002837775.
\]

At the endpoint it certifies the Section-171 feasibility function is negative by more
than `2.5e-5`, while its `delta` derivative stays above `142` throughout the feasible
interval.  Together with the inherited monotonicity in `t`, this safely excludes
`t<=t_0`.  The decimal is deliberately below the numerical root and is not presented
as endpoint-tight.

## 8. Audit conclusion

The new `0.0021` gain survives hostile algebraic review.  In particular, the
improvement is not an artifact of independently minimizing the center imbalance and
the missing-pair loss: the proof keeps their correlation through `h=delta-z^2`, then
uses both leaves through a weighted minimax bound.

The current proof-only consequences that may safely be propagated are therefore

\[
\liminf {T-q/2\over D}\ge2\sqrt{\Delta_2}+0.0021,
\]

\[
\liminf {\sigma_R\over D}\ge0.0042,
\]

and

\[
\liminf {q-k\over D}
\ge {4\over9}(\pi+\sqrt{\Delta_2})+0.0017279.
\]

This is a real quantitative advance, but it is not C-II closure.  The remaining task
is still a source-level incompatibility between the now very tight low-`t` endpoint
structures, not another scalar re-optimization of the same ledgers.
