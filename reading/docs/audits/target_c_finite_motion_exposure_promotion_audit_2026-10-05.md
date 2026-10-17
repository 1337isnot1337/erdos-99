> Generated reading edition · [exact source](../../../docs/audits/target_c_finite_motion_exposure_promotion_audit_2026-10-05.md) · source SHA-256 `ddedf6ff9b0e9a3116f200625c2bd10a74bd851182362ce4cda631c9b0643253`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-354CE0B8BCDC","canonical":true,"claim_ids":["C-CENTERED-FAN-REFLECTIONS","C-TRANSLATION-LENS-EXPOSURE"],"claim_statuses":{"C-CENTERED-FAN-REFLECTIONS":"canonical","C-TRANSLATION-LENS-EXPOSURE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent promotion audit — finite fan reflections and translation-lens exposure

**Date:** 2026-10-05  
**Audit base:** \`3c94a1a93641a5f8fa24d43068d487594d3e38cd\`  
**Starting theorem state:** \`2026-10-05.audit.57\`  
**Target:** C-II / finite nonlocal source motions and blocker localization  
**Verdict:** **PASS for the two exact claims registered below.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit promotes:

1. \`C-CENTERED-FAN-REFLECTIONS\`;
2. \`C-TRANSLATION-LENS-EXPOSURE\`.

The promotion is intentionally finite and scoped. It does not promote any unreviewed fan-population extraction, exact-phase train extraction, slab swap, or reflection-repair theorem. The significance is that the current active-diameter obstruction can now be bypassed in two exact finite geometries: selected fan reflections and rigid packet translations. In both settings the surviving failure is localized to explicit lower blockers or uncovered physical anchors.

## 1. Simultaneous centered fan reflections

Audited source:
\`docs/reports/target_c_centered_fan_simultaneous_reflections_2026-10-02.md\`.

Let $`A`$ be a finite unit-separated planar source of diameter $`D\ge5`$. A selected fan leaf $`p`$ has:

- one actual diameter partner $`a_p`$;
- exactly two unit-contact neighbors $`p_-,p_+`$;
- the exact fan geometry
  
  ```math
  |p-a_p|
  =
  |p_--a_p|
  =
  |p_+-a_p|
  =
  D.
  ```


Let $`S`$ be an independent set of such leaves. Suppose their actual diameter midpoints
```math
m_p=\frac{p+a_p}{2}
```
satisfy
```math
|m_p-s|\le T,
\qquad
T<\frac{D-2}{2\sqrt2}.
```

Define
```math
F(p)=p-\frac{p-a_p}{D^2}
\quad(p\in S),
\qquad
F(x)=x
\quad(x\notin S).
```

For each selected leaf this is exactly the reflection of $`p`$ across the line through $`p_-,p_+`$. The displacement has length $`1/D`$.

### 1.1 The fan contact edges are actual full-source hull sides

Fix one selected $`p`$ and center coordinates at $`a_p`$. A unit chord of the circle of radius $`D`$ has endpoints
```math
\left(\sqrt{D^2-\frac14},\pm\frac12\right).
```

Every point in the closed minor cap beyond this chord lies at squared distance at most
```math
\left(D-\sqrt{D^2-\frac14}\right)^2+\frac14<1
```
from one chord endpoint.

Because the full source is unit-separated, no other source point lies in that cap or on the open chord. Since the endpoints are actual diameter endpoints, they are strict source-hull vertices. Hence the two fan contacts $`pp_-`$ and $`pp_+`$ are the two immediate full-source hull sides incident with $`p`$.

Contact-isolated source points cannot hide in the cap.

### 1.2 Exact separation of selected leaves

Let
```math
n_p=\frac{p-a_p}{D}.
```

For two selected leaves $`p,q`$,
```math
D(n_p-n_q)=2(p-q)-2(m_p-m_q).
```

If $`d=|p-q|<\sqrt2`$, the smaller angle $`\theta`$ between $`n_p,n_q`$ satisfies
```math
\sin(\theta/2)
\le
\frac{d+2T}{D}
<
\frac1{\sqrt2},
```
so $`\theta<\pi/2`$.

The short hull chain from $`p`$ to $`q`$ contains at least two full source-hull sides because $`q`$ is not either immediate fan neighbor of $`p`$. Every hull side has length at least one, including sides ending at contact isolates. Projection onto the bisector tangent gives
```math
d\ge2\cos(\theta/2)>\sqrt2,
```
a contradiction.

Therefore
```math
\boxed{|p-q|\ge\sqrt2.}
```

The same argument applies to a selected $`p`$ and any other actual diameter endpoint $`q\notin\{p,p_-,p_+\}`$ whose actual diameter midpoint is also within $`T`$ of $`s`$.

This uses ordinary support-normal order, not any incident-diameter Euler-path inference.

### 1.3 Every upper source constraint is protected simultaneously

Write
```math
r=p-a_p.
```

For any old source point $`y`$,
```math
2(p-y)\cdot r
=
|p-y|^2+D^2-|y-a_p|^2
\ge
|p-y|^2.
```

If $`d=|p-y|`$, then the exact reflected-distance identity gives
```math
|F(p)-y|^2-d^2
=
-\frac{2(p-y)\cdot r}{D^2}
+\frac1{D^2}
\le
-\frac{d^2-1}{D^2}
\le0.
```

Thus every moved-fixed distance is nonincreasing. For an old unit fan neighbor the equality geometry above shows the unit contact is preserved exactly. For $`d>1`$, the upper-distance inequality is strict.

For two selected leaves $`p,q`$, adding the two one-leaf changes gives
```math
|F(p)-F(q)|^2-|p-q|^2
\le
-\frac{2(|p-q|^2-2)}{D^2}
\le0
```
by the $`\sqrt2`$-separation theorem.

Therefore the simultaneous map is nonexpansive on **every pair of old source points**.

Moreover
```math
|F(p)-F(q)|
\ge
\sqrt2-\frac2D>1
```
for $`D\ge5`$, so a moving-moving pair cannot create a lower violation or a new contact.

All old contacts are preserved. Every selected old diameter edge $`pa_p`$ strictly shortens.

### 1.4 Lower-obstruction factorization

Let $`F_p`$ denote the solo map moving only $`p`$.

Every possible lower violation of the simultaneous map has the form
```math
|F(p)-y|\le1,
\qquad
p\in S,\quad
y\notin S.
```

That is exactly the same inequality as in the solo map $`F_p`$. A selected leaf $`q\ne p`$ cannot be a solo blocker because
```math
|F_p(p)-q|
\ge
\sqrt2-\frac1D>1.
```

Hence:
```math
\boxed{
\text{the simultaneous fan map is lower-feasible}
\iff
\text{every solo fan map is lower-feasible}.
}
```

The same equivalence holds with strict $`>1`$ required for old noncontacts.

For the canonical contact-minimal, then diameter-pair-minimal source, if one selected fan family had no such lower blocker, the endpoint would:

- preserve all old contacts;
- create no new contact;
- preserve unit separation;
- have diameter at most $`D`$;
- strictly shorten every selected old diameter;
- create no new diameter because all old source distances are nonincreasing.

If the new diameter were below $`D`$, global optimality would fail. If it remained $`D`$, the number of actual diameter pairs would drop, contradicting diameter-pair minimality.

Thus every selected solo fan map has an actual strict-pair lower blocker.

This does not contradict canonical \`C-CONTACT-DIAMETER-COORDINATES\`: that theorem is only local in a source-dependent contact-manifold chart. The finite reflection endpoint need not lie inside that unknown chart radius, and it may fail lower feasibility.

## 2. Canonical disjoint blocker matching from fan population

Now use the canonical full-source midpoint estimate from \`C-FS-GEOM\`: every actual diameter midpoint lies within
```math
T=\sqrt{D\eta+\eta^2}=O(D^{3/4}),
\qquad
\eta=3^{1/4}\sqrt D,
```
of the full-source circumcenter.

For every sufficiently large $`D`$ the report's explicit bound gives
```math
T\le D/6-2.
```

Let $`U`$ be the number of actual-diameter fan leaves of contact degree two.

Their induced contact graph has maximum degree two and is triangle-free. Each path or even cycle has an independent set containing at least half its vertices; each odd cycle has length at least five and has an independent set containing at least two-fifths. Therefore one may choose an independent fan family
```math
|S|\ge\left\lceil\frac{2U}{5}\right\rceil.
```

### 2.1 One old source point cannot strictly block two selected fan reflections

Suppose an old source point $`y`$ strictly blocks two selected leaves $`p,q`$:
```math
|p-y|>1,\quad |F_p(p)-y|\le1,
```
and similarly for $`q`$.

Then the reflected points $`p',q'`$ are at distance at most two, hence
```math
|p-q|\le2+\frac2D.
```

The midpoint concentration makes the smaller angle $`\theta`$ between the outward diameter normals satisfy
```math
\sin(\theta/2)<\frac13.
```

Three full hull sides on the short normal interval would force
```math
|p-q|>2\sqrt2>2+\frac2D
```
for the stated large-$`D`$ range. Therefore the chain has exactly two hull sides and its middle vertex $`r`$ is the common unit-contact neighbor of $`p,q`$.

Both reflections preserve
```math
|r-p'|=|r-q'|=1.
```

The angle bound also gives
```math
|p'-q'|>\frac74>\sqrt3.
```

The intersection of the two closed unit disks centered at $`p',q'`$ has diameter less than one. Both $`r`$ and $`y`$ lie in that lens, contradicting unit separation unless $`y=r`$. But $`r`$ is an old unit neighbor and therefore not a strict-pair blocker.

So strict-pair blockers are distinct across selected leaves.

A blocker cannot itself be an actual diameter endpoint: its old distance from its leaf is at most
```math
1+\frac1D<\sqrt2,
```
while the generalized selected-leaf separation theorem applies to every actual diameter endpoint because every diameter midpoint satisfies the canonical uniform midpoint bound.

Thus every blocker is diameter-inactive.

Consequently every sufficiently large canonical source satisfies the conditional exact matching theorem
```math
\boxed{
\#\{
\text{pairwise vertex-disjoint loaded-fan / diameter-inactive blocker pairs}
\}
\ge
\left\lceil\frac{2U}{5}\right\rceil,
}
```
and each matched pair obeys
```math
\boxed{
1<|p-y|\le1+\frac1D.
}
```

No claim that $`U`$ itself is large is promoted here.

The exact verifier was rerun independently and passed 166 old/joint pair certificates, simultaneous/solo factorization, distinct blocker labels, and the finite collision-transfer regression.

**Verdict:** canonical-ready.

## 3. Translation-lens protection for rigid packet motions

Audited source:
\`docs/reports/target_c_finite_translation_lens_exposure_2026-10-02.md\`.

The finite theorems below are independent of the unpromoted exact-phase/slab extraction ancestry mentioned in that source report.

### 3.1 Exact double-lens inclusion

Let $`r_1,r_2`$ be two vectors of length $`D`$, and write
```math
s=\frac{r_1+r_2}{2},
\qquad
w=\frac{r_1-r_2}{2}.
```
Then
```math
s\perp w,
\qquad
|s|^2+|w|^2=D^2.
```

Suppose
```math
|s+z|,\ |s-z|\le D.
```

Then every $`p`$ satisfying
```math
|p+w|,\ |p-w|\le D
```
also satisfies
```math
\boxed{|p+z|,\ |p-z|\le D.}
```

If $`s,w\ne0`$, $`z\ne\pm w`$, and one of the two old lengths $`|p\pm w|`$ is strictly below $`D`$, then both conclusions are strict.

The proof is a direct two-coordinate monotonicity argument. In orthogonal coordinates
```math
s=(a,0),\qquad w=(0,b),
```
write $`x=|z_x|`$, $`y=|z_y|`$. The premise gives
```math
(a+x)^2+y^2\le a^2+b^2=D^2,\qquad y\le b.
```
If $`t=|p_y|`$,
```math
|p_x|\le\sqrt{D^2-(t+b)^2},
```
and the resulting upper envelope
```math
F(t)=
\left(\sqrt{D^2-(t+b)^2}+x\right)^2+(t+y)^2
```
is nonincreasing.

### 3.2 Exposed crossing-diameter endpoints protect all cross upper pairs

Partition a diameter-$`D`$ source into nonempty packets $`S,T`$. Translate all points of $`S`$ by one vector and fix $`T`$.

Let $`H_{ST}`$ be the old actual diameter edges crossing the partition, and let
```math
E_S=\{x\in S:x\text{ is incident with }H_{ST}\},
\qquad
E_T=\{y\in T:y\text{ is incident with }H_{ST}\}.
```

If every edge of $`H_{ST}`$ remains at most $`D`$, then
```math
\boxed{
|x'-y'|\le D
\quad
\forall x\in E_S,\ y\in E_T.
}
```

If an exposed pair $`xy`$ was previously strict and either endpoint has an incident crossing diameter that strictly shortens, then $`xy`$ remains strictly below $`D`$.

The proof chooses incident crossing diameters $`xf`$ and $`my`$ and applies the double-lens theorem to the opposite cross pair $`xy`$. If $`xy`$ was not itself an old diameter, those two chosen diameter edges are vertex-disjoint.

Thus if
```math
\operatorname{conv}S=\operatorname{conv}E_S,
\qquad
\operatorname{conv}T=\operatorname{conv}E_T,
```
and all crossing diameters strictly shorten, **every** new cross distance is strictly below $`D`$. Internal packet distances are unchanged.

If the packet translation also preserves every old contact, then a canonical contact-minimal, diameter-pair-minimal source must have a previously strict lower pair reaching distance at most one. Otherwise the translated source is a strict global-diameter competitor or has fewer diameter pairs.

### 3.3 Positive equilibrium localizes uncovered upper witnesses to physical anchors

Let $`B`$ be the set of old actual diameter endpoints and $`Z`$ the actual contact-isolated source points.

For a packet $`S`$, let $`A_S`$ be the vertices incident with unit contacts crossing the packet boundary, and define
```math
Q_S=(B\cap S)\cup A_S\cup(Z\cap S).
```

Then
```math
\boxed{\operatorname{conv}S=\operatorname{conv}Q_S.}
```

Indeed, an unloaded nonisolated packet point with no crossing contact has all positive-contact neighbors inside $`S`$. Positive contact equilibrium expresses it as a strict positive convex combination of other source points, so it cannot be an extreme point of $`\operatorname{conv}S`$.

For an unloaded nonisolated packet point $`x`$, define the crossing-contact force
```math
g_x=
\sum_{y\notin S:\,xy\in C}
\alpha_{xy}(p_x-p_y).
```

If $`n`$ is any outward support normal of $`x`$ in $`\operatorname{conv}S`$, then
```math
\boxed{n\cdot g_x\le0.}
```

This follows by projecting positive equilibrium: every internal contact vector has nonnegative projection on $`n`$, so the crossing-contact force has nonpositive projection.

This restriction is invariant under rigid packet translation.

Therefore any new upper violation must have at least one endpoint in the uncovered anchor sets
```math
U_S=Q_S\setminus E_S,
\qquad
U_T=Q_T\setminus E_T.
```

The only possible uncovered anchor types are:

- an old diameter endpoint whose old diameters stay inside the packet;
- an unloaded crossing-contact endpoint satisfying the support-force inequality;
- a contact isolate.

### 3.4 One-vector exact cut sharpening

If every contact crossing the packet cut has the same oriented unit vector $`u`$ from $`T`$ to $`S`$, then an unloaded crossing-contact vertex in $`S`$ has boundary force a positive multiple of $`u`$, and one in $`T`$ has boundary force a negative multiple.

Hence a maximizing new upper witness with vector $`r`$ from $`T`$ to $`S`$ and
```math
r\cdot u>0
```
cannot use an unloaded crossing-contact endpoint. Both endpoints must lie in
```math
B\cup Z.
```

If contact isolates are absent, both endpoints are actual diameter endpoints; because exposed/exposed pairs are protected, at least one endpoint must carry an old diameter internal to its packet.

This is an exact upper-witness classification, not a claim that every exact-phase cut admits the needed rigid translation.

The exact verifier was rerun independently and passed:

- 105 actual four-point diameter sources against 93 exact lens endpoints;
- 19,530 cross-upper checks;
- 19,110 strictness checks;
- five uncovered-upper source packets with 93,954 exact old/new pair checks;
- 20 preserved cut contacts;
- the exact lower-collision regression.

**Verdict:** canonical-ready.

## 4. Scope and interaction with audit.56–57

The promoted theorems do **not** assert:

- that a large fan population $`U`$ exists;
- that every fan blocker can be repaired;
- that a packet translation satisfying the required contact geometry exists in every canonical source;
- that contact isolates are absent;
- that upper feasibility implies lower feasibility;
- that a finite contact-preserving move stays inside the source-dependent audit.56 local coordinate radius;
- that any selected pentagon wall gains positive audit.54 $`W_C`$ capacity.

The finite-move results instead refine the current obstruction.

- In the centered-fan geometry, all upper constraints and all moving-moving lower constraints are solved simultaneously. The complete remaining obstruction factorizes into fixed unary lower blockers.
- In rigid packet-translation geometry, crossing-diameter-exposed endpoint pairs are automatically upper-safe. Every remaining upper witness is forced onto a small explicit physical anchor set.

Thus the current C-II route may legitimately target blocker repair, blocker replacement, or exposure coverage rather than re-solving the entire diameter cage.

**Promotion recommendation:** advance theorem state to \`2026-10-05.audit.58\` and register both claims as canonical.
