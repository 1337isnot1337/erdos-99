> Generated reading edition · [exact source](../../../docs/reports/target_c_half_depth_fan_forest_and_weight_budget_2026-10-08.md) · source SHA-256 `f0abd788773515a1afc80e841aadd74637bf4d4b29da2400edec85c1bc218a93`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "55c270a34f4c0c7b8f0cac272e8b7944bb85f84f", "source_branch_refs": ["refs/heads/research/level-i-closure-20261007"], "source_commit": "3d52e70f706100af0fee6bd730b4a21209181054", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_c_half_depth_fan_forest_and_weight_budget_2026-10-08.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "78c1d8c3860e2a60f4e75c29103e0818790bc9358ef22f640c2da7f7e7d8f37f"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Target C: half-depth blocker closure, fan forests and multiplier budgets

Date: 2026-10-08. Research base: `6e8dc144e2a0c268d261a43f298a47524c22b7f1`;
run start: `4de98db40dae7e3932d489f49c89960ecca77245`.
State: `2026-10-08.audit.155`, including the scoped Audit.158 entries.
Classification: **proved candidates awaiting independent audit**.
Registry status: unreviewed; canonical=false. C-II and Level I remain open.

The implication being attacked is

`actual loaded endpoint -> full-source shallow closed blocker set
-> finite same-cardinality translation -> canonical contradiction`.

The new circumcircle estimate makes “shallow” extend to depth
`D/2-o(D)` in a canonical large source. It does not extract that closed
set. A separate fan-forest observation strengthens the available
injective first-blocker matching from `ceil(2U/5)` to `ceil(U/2)`.
The KKT calculation below gives a multiplier budget, not an integer
bound on those blockers or their paths.

## 1. Inputs and scope

Use the full source `A`, all its contact-isolated labels, its actual
diameter `D` and an actual diameter pair `pa`. Write
`u=(p-a)/D` and `s(x)=u dot (p-x)`. Suppose
`A subset B(c,R)`, where `R>=D/2`. Put

```math
P=u\cdot(p-c),\qquad E=\sqrt{R^2-D^2/4}.
```

For a displacement length `delta>0` define

```math
A(E,\delta)=
\begin{cases}
E^2/\delta+\delta/2,&0\le E\le\delta/2,\\
E+\delta/4,&E\ge\delta/2,
\end{cases}
\qquad H=P-A(E,\delta).
\tag{1}
```

Assume `H>0` when applying the closure theorem.
The geometry lemma uses neither KKT equilibrium nor optimality.
The closure consequence uses the canonical contact-minimal, then
actual-diameter-pair-minimal triangle-free global source.

Load-bearing canonical inputs are:

- [C-I normalization](../targets/target-c/56-ci-restored-frontier.md);
- [full-source circumradius and midpoint bounds](../targets/target-c/58-full-source-geometry-audit.md), FS.1 and FS.6;
- [full-source centered fan reflection and blocker injection](target_c_centered_fan_simultaneous_reflections_2026-10-02.md);
- [Audit.152 blocker relation and finite closure](../audits/target_c_centered_fan_blocker_closure_independent_audit_2026-10-08.md).

The first-blocker improvement requires a fan leaf with a **unique actual
diameter partner**. Audit.152's broader centered-fan hypothesis does
not itself supply uniqueness.

## 2. Exact circumcircle upper safety

**Candidate lemma.** If `s(x)<H` and translating `x` to
`x'=x-delta u` increases its distance to a fixed source point `y`,
then `|x'-y|<D`.

Let `t=s(y)-s(x)=u dot (x-y)`. Distance increase means
`t<delta/2`. The old midpoint `m=(x+y)/2` has outward projection

```math
u\cdot(m-c)=P-s(x)-t/2>A(E,\delta)-t/2>0.
```

The last inequality uses `A>=delta/2` and `t<delta/2`.
Since both old points lie in the radius-`R` ball,

```math
|x-y|^2/4+|m-c|^2
=(|x-c|^2+|y-c|^2)/2\le R^2.
```

The exact translated squared distance is therefore strictly below

```math
F(t)=4R^2-4(A-t/2)^2-2\delta t+\delta^2.
\tag{2}
```

For `E<=delta/2` the first branch of (1) gives

```math
F(t)=D^2-(t-2E^2/\delta)^2\le D^2.
\tag{3}
```

For `E>=delta/2`,

```math
F(\delta/2)=D^2,\qquad
F'(t)=4E-\delta-2t\ge4E-2\delta\ge0
\quad(t\le\delta/2).
\tag{4}
```

Equations (2)--(4) prove strict upper safety. The calculation concerns
the old midpoint; it does not assume the translated point remains
in the circumcircle. No inactive upper pair is omitted.

### The half-depth coefficient and one sharp finite case

The diameter midpoint satisfies

```math
|(p+a)/2-c|^2+D^2/4
=(|p-c|^2+|a-c|^2)/2\le R^2.
```

Consequently `P>=D/2-E` and

```math
H\ge H_0:=D/2-E-A(E,\delta).
\tag{5}
```

In particular, when `R=D/2`, the midpoint is `c` and
`H=H_0=D/2-delta/2`. This finite correction is sharp for the
standalone geometry lemma. Set `c=0`, `p=(D/2,0)`,
`a=(-D/2,0)` and take

```math
x=(\epsilon,\sqrt{D^2/4-\epsilon^2}),\qquad
y=(\epsilon,-\sqrt{D^2/4-\epsilon^2}),
\quad 0<\epsilon<\delta/2.
```

The old four-point source has diameter `D`, while

```math
|x-\delta u-y|^2=D^2-4\epsilon^2+\delta^2>D^2.
\tag{6}
```

For any proposed threshold larger than `D/2-delta/2`, choose
`epsilon` above its corresponding outward margin and below `delta/2`.
Then `x` is strictly below the proposed depth threshold and (6)
violates upper safety. These sources are nonglobal for `D>=10`:
a four-site unit square is a strict same-cardinality competitor.
No sharp finite correction is asserted for `E>0`.

## 3. A full-source finite closure theorem

Use Audit.152's complete directed relation:
`x -> y` when translating `x` alone by `-delta u` changes an old
strict lower pair to distance at most one, or an old unit pair to
distance strictly below one.

Suppose `R_0 subset A` contains `p`, is closed under all these
arrows, and every member has depth less than `H` from (1).
Translate all of `R_0` by `-delta u` and fix every other source label.

Pairs inside either part are unchanged. On crossing pairs, closure
retains unit separation and keeps every old noncontact strict.
The new contact graph is a subgraph of the old triangle-free graph.
An increasing crossing distance is strictly below `D` by Section 2;
a nonincreasing one is at most its old value. There are no new
diameter pairs.

Here `A(E,delta)>=E` and `P<=R`, so
`H<=R-E<=D/2<D`. Thus the carrier `a` is outside `R_0`.
The old pair `pa` shortens strictly provided `0<delta<2D`.
Global minimality excludes diameter below `D`. At diameter `D`,
contact loss contradicts contact minimality; without contact loss,
the removed `pa` contradicts actual-diameter-pair minimality.
This is an actual finite move of all `n` source labels.

Therefore no such closed set exists. For `H>0` and `0<delta<2D`,
the closure from `p` must reach `H`. Parent arrows give a
distinct-vertex path to its first depth crossing, with

```math
1\le d_j\le1+\delta,\qquad
\Delta s_j>\delta/2,\qquad
d_j-1\le\delta\Delta s_j-\delta^2/2.
\tag{7}
```

Its length `L` and total edge excess satisfy

```math
L\ge H/(1+\delta),\qquad
\sum_j(d_j-1)
<\delta(H+1+\delta)-L\delta^2/2.
\tag{8}
```

This has the same finite endpoint as the previous
[diameter-ball cap estimate](target_c_sharp_cap_closure_and_unbounded_path_congestion_2026-10-08.md).
Additional full-source circumcircle information improves the depth.
No path disjointness is assumed.

### Canonical large-source specialization

Canonical FS.1 gives

```math
R_{\rm circ}\le D/2+\eta,\qquad
\eta=3^{1/4}\sqrt D.
```

Use the actual circumradius in (1). For `delta=1/D`, (5) gives
`H_0=D/2-o(D)`. A conservative explicit threshold follows by
using the larger radius `D/2+eta`, for which `E>delta/2`:

```math
\widehat H=D/2-2\sqrt{D\eta+\eta^2}-1/(4D).
\tag{9}
```

The canonical midpoint estimate has
`sqrt(D eta+eta^2)<D/8` for `D>=10000`, as verified in the
centered-fan source report. Thus (9) is positive there. The
closure must reach this uniform threshold, and along an unbounded
canonical source sequence

```math
\liminf L/D\ge1/2,\qquad
\limsup\sum_j(d_j-1)\le1/2.
\tag{10}
```

For a degree-two centered fan seed at `delta=1/D` its old two
contacts are preserved exactly. Its first arrow is a strict old
noncontact and retains Audit.152's
`s(x_1)>sqrt(3)/2-1/(4D)` estimate.
Neither its first blocker nor later vertices are assumed isolated.

## 4. Unique-partner fan leaves induce a forest

Assume `D>=5`. Let `F_fan` contain every actual degree-one diameter vertex `p`
having exactly two contacts `p_-,p_+` and satisfying the
common-carrier fan equations. Let `U=|F_fan|`.

**Candidate lemma.** The actual contact graph induced by `F_fan`
is a disjoint union of paths. It has an independent set of size
at least `ceil(U/2)`.

Each of a fan's two contacts is a complete side of the full source
hull, by the canonical unit-chord cap shield. Each fan is a strict
full-source hull vertex. Thus the induced fan graph is a subgraph
of the simple full-source hull cycle and has maximum degree two.

At least one hull vertex is not a fan: every fan's carrier is an
actual diameter endpoint incident to the three distinct pairs
`ap_-,ap,ap_+`, so it has diameter degree at least three. A cycle
in the induced fan graph would be the entire full-source hull
cycle, contradicting this nonfan carrier. All components are paths.

A component with `r` vertices contributes `ceil(r/2)` alternating
vertices to an independent set. Summing proves the bound.
No odd fan cycle incurs the former `2/5` loss.

Adjacent fans also have the same actual carrier: a fan's neighbor
has distance `D` to its carrier and has a unique actual diameter
partner. The carrier is therefore constant on each component.

### Stronger injective blocker matching

For the canonical `D>=10000` source, choose the independent
fan set above. The canonical full-source midpoint estimate
satisfies SR.6. Every solo reflection needs a strict-pair blocker,
and Lemma SR.2 makes these blockers distinct. None is an actual
diameter endpoint. Consequently

```math
\boxed{\text{disjoint loaded-to-diameter-inactive blocker pairs}
\ \ge\ \lceil U/2\rceil.}
\tag{11}
```

All leaves, blockers and carriers are original source labels.
A blocker is not asserted to be a contact isolate. Equation (11)
does not force `U` to be large and does not make the subsequent
half-depth paths disjoint.

## 5. What KKT equilibrium actually adds

For any normalized KKT stress, `sum_H beta=1` and

```math
\sum_C\alpha=D^2.
\tag{12}
```

At a fan leaf its only diameter reaction is `beta_pa(p-a)`.
The contact vectors `p-p_-` and `p-p_+` have outward radial
projection `1/(2D)` and opposite nonzero tangent projections.
Equilibrium gives

```math
\boxed{\alpha_{pp_-}=\alpha_{pp_+}=D^2\beta_{pa}.}
\tag{13}
```

For an independent fan set `S` its incident contact edges are
all distinct, so (12)--(13) imply

```math
2\sum_{p\in S}\beta_{pa}\le1.
\tag{14}
```

The bound is strict if any other contact has positive multiplier.
Every fan contact is loaded-loaded, so its weight is paid by
that part of the contact-stress budget.

On a full fan path with `r` vertices, (13) makes all diameter
multipliers equal, say `beta_r`. Its `r+1` incident contacts,
including both nonfan endpoint contacts, each have weight
`D^2 beta_r`. These contact sets are disjoint between components.
Therefore

```math
\sum_{\text{fan components}}(r+1)\beta_r\le1.
\tag{15}
```

This stress restriction is missing from an isolated loaded-carrier
geometric fixture. It has no integer population consequence
without an additional quantitative source theorem. Strict
positivity supplies no stated lower bound depending only on `D`.
Equations (14)--(15) do not bound `U`, path congestion or the
number of labels available to refill a deletion.

## 6. Verification and unresolved implication

The [exact checker](../../../research/verify_target_c_half_depth_fan_forest_2026_10_08.py)
checks rational quadratic identities, finite circumcircle cross-pair
samples, rational sharp half-depth fixtures, complete contact and
diameter graphs of circular-arc fan sources, their fan forests
and maximum independent sets, local fan equilibrium and explicit
same-cardinality square competitors.

The arc fixtures have an isolated loaded carrier and no normalized
global KKT stress. Local equilibrium checks are not full-source
stress certificates. Universal statements are proved analytically;
finite samples do not establish them.

The checker passed 966 exact quadratic identities and 261,916 valid
circumcircle cross-pair samples, including 102,148 increasing pairs
strictly below D. Nine sharp half-depth fixtures and six arc fixtures
passed 466 complete source-pair and 466 square-competitor checks.
The arc tests reconstructed the actual hulls and contact/diameter
graphs, found the exact maximum independent fan sets by enumeration,
and passed 150 local fan balance equations. Python compilation,
all seven local proof links and whitespace checks passed.

The remaining implication is still

`canonical global source -> shallow closed set or another
complete same-cardinality competitor`.

A half-depth path obstructs one proposed translation. Even an
injective first-blocker matching does not control later overlap.
The [forced-congestion regression](target_c_sharp_cap_closure_and_unbounded_path_congestion_2026-10-08.md)
remains relevant to unweighted counting. No stress floor,
canonical path-disjointness theorem, packet, strict global stability
inequality or Level I solution is claimed.
