> Generated reading edition · [exact source](../../../docs/reports/target_a_slot05_one_arm_source_sector_rank_cap_2026-10-10.md) · source SHA-256 `45b461442185dc86b8991175853e09d33d59c077865d83dab65eafe0e56a5813`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "3ac4fe9047a0e9471837782d37257e9beb58cfc8", "source_head": "7be6a6b746e9cf6ea18145248b652c7a0f206dc4", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_a_slot05_one_arm_source_sector_rank_cap_2026-10-10.md", "source_pr": 953, "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "af9a6a671e5d7cd97a8884dc6d711fe415752821baa39f2d5894dd3965e8291c"} -->

> **Imported unreviewed source research.** PR #953 is not a theorem promotion; current destination theorem state remains authoritative.

# Erdős Problem #99 — Slot 05 source-arm transfer and fan rank cap

**Date:** 2026-10-10
**Repository commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
**State version:** `2026-10-10.audit.234`
**Run type:** proof development and dependency audit
**Target:** A — source capacity / Schur response
**Starting status:** canonical through Section 177; Target A open
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_A_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used for a rejected strip-packing lead; no theorem imported
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting canonical endpoint

The preferred Target A endpoint is

$$
\operatorname{rank}S\le d_{\rm int}+|C^\partial|-\Delta_\Lambda,
$$

or equivalently $\zeta-s\ge0$, where
$\zeta=|C^\partial|-\operatorname{rank}S$ and
$s=\Delta_\Lambda-d_{\rm int}$. In the actual-response locked branch, Section 175
reduces the sufficient condition to

$$
|O_{\rm iso}|+Q_\Sigma\ge j_*+|T_Z|,
\qquad
Q_\Sigma=\sum_i(|O_i|-|C_i|)_+.
$$

In the zero-slack source branch, Sections 168 and 177 supply separate saturating
matchings from $C^\partial$ and $O$ into the same triangle-free source $A^0$.
The closure chain attacked here is

```text
zero-slack C/O source matchings
  -> classify common-source gates by their C-terminal sectors
  -> cap bad gates by the number of nonshield terminals
  -> a fan-size-independent source term in the rank bound
  -> Target A if the remaining tube/sector inequality holds.
```

The argument below does not identify the two source matchings.

## 2. Source-sector calculation and its regression

**Classification:** the one-arm crossing lemma, the inner-source defect bound, and
the source-boundary count below are unreviewed proved candidates requiring independent
audit. The gate/rank calculations are valid conditional algebra, but their
population-scale consequence is vacuous; they do not improve the canonical
Section-175 rank cut.

### Statement

Assume the Section-168 zero-slack endpoint. Let $A^0$ be its triangle-free
maximum-cardinality packing in the fixed source hull $H$, and let $X^*\subset K^*$
be the plateau-terminalized response optimum. Choose independently the canonical
matchings

$$
M_C:C^\partial\longrightarrow A^0,
\qquad M_O:O\longrightarrow A^0,
$$

where $M_C$ is restricted from a matching saturating $X^*$, and $M_O$ is
restricted from one saturating $Y_{\rm in}$. Let $\Sigma$ be a finite unit-contact
shield in $X^*$, and write $E=|E(\Sigma)|$, $d=\operatorname{diam}K^*$.
Use the Section-175 sets $T_\Sigma,T_O,C_i,O_i,O_{\rm iso}$, with

$$
b=|C^\partial\cap\widehat W_\Sigma|,
\quad
P_\Sigma=\sum_i(|C_i|-|O_i|)_+,
\quad
Q_\Sigma=\sum_i(|O_i|-|C_i|)_+.
$$

Let $e_\Sigma$ be the number of terminals
$c\in C^\partial\setminus\widehat W_\Sigma$ whose matched source label is
outside $K^*$ or whose source arm meets $|\Sigma|$. The common-source count
forces

$$
\boxed{\sum_i|O_i|+P_\Sigma\le 20d+25+e_\Sigma,}
\tag{S1}
$$

and the terminal population gives the fan-size-independent bound

$$
\boxed{e_\Sigma\le\sum_i|C_i|\le |C^\partial|\le8d+1.}
\tag{S2}
$$

Retaining the exact exception count gives

$$
\boxed{\operatorname{rank}S
\le |T_\Sigma|+20d+25+e_\Sigma-P_\Sigma-Q_\Sigma.}
\tag{S3}
$$

In particular, $e_\Sigma\le8d+1$ yields

$$
\boxed{\operatorname{rank}S
\le |T_\Sigma|+28d+26-P_\Sigma-Q_\Sigma.}
\tag{S4}
$$

The exact right-deficiency consequence is

$$
\boxed{h(G)\ge |O|-|T_\Sigma|-20d-25-e_\Sigma+P_\Sigma+Q_\Sigma.}
\tag{S5}
$$

In particular,
$$
h(G)\ge |O|-|T_\Sigma|-28d-26+P_\Sigma+Q_\Sigma.
\tag{S5a}
$$

For the Section-172 locked three-channel fan, $E=v=|V(\Sigma)|$. If the
prescribed-phase rotation is chosen as in the Voronoi tube lemma below, then

$$
|T_\Sigma|\le
\left\lfloor
\left(\frac4{\sqrt3}+\frac4\pi\right)v
+\frac{11}{2}+\frac{2\pi}{\sqrt3}-2\sqrt3-\frac6\pi
\right\rfloor .
\tag{S6}
$$

The exact phase-dependent condition from (S5) is

$$
|C^\partial|-s+P_\Sigma+Q_\Sigma
\ge |T_\Sigma|+20d+25+e_\Sigma.
$$

Since $e_\Sigma\le\sum_i|C_i|=|C^\partial|-b$, it is sufficient that

$$
\boxed{b-s+P_\Sigma+Q_\Sigma\ge |T_\Sigma|+20d+25.}
\tag{S7}
$$

For the fan, the simultaneous zero-slack / locked-fan subbranch therefore closes if

$$
\boxed{
 b-s+P_\Sigma+Q_\Sigma
\ge
\left\lfloor
\left(\frac4{\sqrt3}+\frac4\pi\right)v
+\frac{11}{2}+\frac{2\pi}{\sqrt3}-2\sqrt3-\frac6\pi
\right\rfloor
+20d+25.
}
\tag{S8}
$$

Neither (S7) nor (S8) can hold in the remaining $s\ge0$ branch: the left side of
(S7) is at most $16d+10$, while its right side is at least $20d+25$. This
population obstruction is proved explicitly in the audit below.

The linear coefficient of $v$ in (S8) is $4/\sqrt3+4/\pi$; the former
additive $v$-term from counting shield-crossing C-arms is absent. The coarser
threshold obtained from $e_\Sigma\le8d+1$ is unattainable when $s\ge0$; when
$s<0$, the nullity target is automatic. Indeed,
$$
|C^\partial|-s+P_\Sigma+Q_\Sigma
\le 2|C^\partial|+|O|
\le24d+11<28d+26,
$$
where $P_\Sigma+Q_\Sigma\le|C^\partial|+|O|$, and the one-sided boundary-layer
bounds proved below give $|C^\partial|\le8d+1$, $|O|\le8d+9$. Thus the useful sufficient
route is the shielded-terminal cancellation in (S7); neither (S7) nor (S8) is proved
for every canonical survivor.

### Scope

The source-arm lemma applies to any two unit-separated point sets $X^*,A^0$, any
strict matching between them, and any finite unit-contact shield in $X^*$. The rank
and deficiency corollaries additionally require the Section-168 zero-slack source
matchings, the Section-175 response sectors, and the actual-response locked fan. No
contact-isolated source point is deleted from $A^0$; all source labels remain in the
matching and packing counts. No global optimum is replaced by a scaffold or response
configuration.

### Proof

#### Lemma 1 — one matched source arm per crossed unit contact edge

Let $pq$ be a unit contact of $X^*$, let
$x\in X^*\setminus\{p,q\}$, and let $a\in A^0$ satisfy $|x-a|<1$. If the
closed segment $[x,a]$ meets $[p,q]$, then at most one arm from an injective
strict matching $x\mapsto a_x$ can meet this fixed contact edge.

An arm from an off-shield $x$ cannot meet a shield vertex: if $p\in[x,a]$, then
$|x-p|\le |x-a|<1$, contrary to unit separation of $X^*$. A nontrivial
collinear overlap is impossible for the same reason, since reaching the relative
interior of a unit edge from a distinct unit-separated point on its line takes length
at least one. Thus a meeting with the edge occurs at an interior point $z$, either
as a proper crossing or with $a=z$.

Put

$$
t=|p-z|\in(0,1),\qquad s_x=|x-z|,\qquad r_a=|a-z|.
$$

The segment condition gives $s_x+r_a=|x-a|<1$. Since $x$ is unit-separated
from both $p$ and $q$,

$$
1\le|x-p|\le s_x+t,
\qquad
1\le|x-q|\le s_x+1-t.
$$

Therefore $s_x\ge\max(t,1-t)$, and

$$
r_a<\min(t,1-t).
\tag{6}
$$

Suppose two distinct matching arms meet the same edge at $z_1,z_2$, with
$t_1=|p-z_1|\le t_2=|p-z_2|$. Their source labels are distinct. By (6) and the
triangle inequality along the contact edge,

$$
|a_1-a_2|
\le r_1+(t_2-t_1)+r_2
<\min(t_1,1-t_1)+(t_2-t_1)+\min(t_2,1-t_2)
\le1.
$$

For the last inequality: if $t_2\le1/2$, the right expression without its strict
sign is $2t_2$; if $t_1\ge1/2$, it is $2-2t_1$; and if
$t_1\le1/2\le t_2$, it is exactly one. The strict sign in the preceding line
then contradicts unit separation of $A^0$. This proves the lemma.

An off-shield source arm that meets $|\Sigma|$ must meet the relative interior of
at least one contact edge: meeting a shield vertex contradicts separation of $X^*$,
and collinear overlap is excluded above. Assign the arm to one such edge. Lemma 1 gives

$$
\boxed{
\#\{x\in X^*\setminus V(\Sigma):[x,a_x]\cap|\Sigma|\ne\varnothing\}
\le |E(\Sigma)|.
}
\tag{7}
$$

This improves the canonical Section-176.5 charge $5|V(\Sigma)|$ to
$|E(\Sigma)|$.

Together with Lemma 2, it gives the following replacement for the exception count in
Section 176.6:

$$
\boxed{
\#\{x\in X^*\setminus V(\Sigma):x\text{ is not sector-good}\}
\le |E(\Sigma)|+8d+1.
}
\tag{7a}
$$

Indeed, source labels outside $K^*$ account for at most $8d+1$ response
endpoints by Lemma 2. If the source label lies in $K^*$ but in another sector,
the segment joining it to $x$ must meet $|\Sigma|$, and (7) charges the endpoint
to one of at most $|E(\Sigma)|$ crossed contact edges. For the locked fan the
exception budget becomes $v+8d+1$, replacing the canonical $5v+12d+9$.

#### Lemma 2 — one-sided source-label exception

Let $K$ be convex with perimeter $P$, diameter $d$, and let $X\subset K$
be unit-separated. The number of points $x\in X$ with
$\operatorname{dist}(x,\partial K)\le1$ is at most $8P/\pi+1\le8d+1$.

Place disjoint open radius-$1/2$ disks around these points. They lie in the outer
parallel shell $(K+B_{1/2})\setminus K$ together with the inner boundary layer
$K\setminus K_{-3/2}$. Steiner's formula bounds the outer shell area by
$P/2+\pi/4$. Coarea and monotonicity of inner parallel perimeters bound the inner
layer area by $3P/2$, also when the inner parallel body disappears before distance
$3/2$. Thus the disks occupy area at most $2P+\pi/4$. Dividing by their area
$\pi/4$ proves the claim; Cauchy's perimeter inequality gives $P\le\pi d$.

If a matched source label $a_x$ lies outside $K^*$, the segment $[x,a_x]$
meets $\partial K^*$, and its length is below one. Hence
$\operatorname{dist}(x,\partial K^*)<1$. Applying Lemma 2 to the unit-separated
response points bounds the number of such $x$ by $8d+1$.

The corresponding exterior estimate is also useful. Let $O$ be a unit-separated
set outside $K$ with $\operatorname{dist}(o,K)<1$ for every $o\in O$. Disjoint
radius-$1/2$ disks centered at its points have their outside portions in
$(K+B_{3/2})\setminus K$ and their inside portions in $K\setminus K_{-1/2}$.
Steiner's formula bounds the first area by $3P/2+9\pi/4$; inner-parallel coarea
bounds the second by $P/2$. Dividing the total $2P+9\pi/4$ by $\pi/4$
gives
$$
|O|\le8P/\pi+9\le8d+9.
$$

#### Corollary 2A — sharper zero-slack inner-source defect

In the Section-168 zero-slack branch put
$$
k=|A^0\cap K^*|,\qquad r=m^*-k.
$$
Theorem 168.3 says every matching saturating $X^*$ into $A^0$ uses at least $r$
source labels outside $K^*$. Lemma 2 bounds the number of such labels in the same
matching by $8d+1$. Therefore
$$
\boxed{r\le8d+1,\qquad |A^0\cap K^*|\ge m^*-(8d+1).}
\tag{10}
$$
This sharpens the unreviewed 12d+9 bound in
docs/reports/target_a_inner_source_capacity_defect_bound_2026-09-05.md. It still
gives no comparison between $r$ and $s=\Delta_\Lambda-d_{\rm int}$.

The same one-sided estimate with $K=H$, whose diameter is $D$, gives
$|A^0_\partial|\le8D+1$ for the source-boundary set in (168.21). The Hall argument
of Corollary 168.2A then yields
$$
\boxed{|Z_\partial|\le8D+1,}
\tag{11}
$$
improving its displayed boundary exception $12D+9$. Neither improvement changes
the active theorem state.

#### Lemma 3 — sector classification of common-source gates

Write $S_C,S_O\subset A^0$ for the image sets of $M_C,M_O$, and
$L=|S_C\cap S_O|$. Since both image sets lie in the two-sided width-two boundary
band of $K^*$, Section 177.5A gives

$$
L\ge |C^\partial|+|O|-20d-25.
\tag{8}
$$

For each common source label $a$, its two matching partners form a gate
$c-a-o$, with $c\in C^\partial$, $o\in O$, and both arms shorter than one.
Partners are unique within each matching, so different labels give distinct
$c$- and $o$-endpoints.

Let $B_C=C^\partial\cap\widehat W_\Sigma$, $|B_C|=b$. For each sector, let
$e_i$ count the terminals $c\in C_i$ whose $M_C$-source is outside $K^*$
or whose source arm meets $|\Sigma|$, and put $e_\Sigma=\sum_i e_i$. Gates
with such a terminal are at most $e_\Sigma$, where
$e_\Sigma\le\sum_i|C_i|$. Gates with a shielded terminal or a sink in $T_O$ are
counted separately.

For every nonexceptional gate, $c\in C_i$ for a sector $D_i$, the source
$a\in K^*$ is in the same sector, and $o\notin T_O$. If $o$ is isolated it is
counted by $O_{\rm iso}$. Otherwise choose a surviving response neighbor
$x\in D_j$ of $o$. Both $a$ and $x$ lie in the open unit disk $B(o,1)$.
If they belonged to different sectors, the segment $[a,x]\subset B(o,1)$ would
cross $|\Sigma|$, forcing $o\in T_O$, a contradiction. Hence $j=i$, and
$o\in O_i$. The nonexceptional gates in sector $i$ use distinct endpoints on
both sides. Since at most $e_i$ terminals in sector $i$ were marked bad, their
number is at most $\min(|C_i|-e_i,|O_i|)$. Thus

$$
L\le b+e_\Sigma+|T_O|+|O_{\rm iso}|
+\sum_i\min(|C_i|-e_i,|O_i|).
\tag{9}
$$

Use $|C^\partial|=b+\sum_i|C_i|$ and
$|O|=|T_O|+|O_{\rm iso}|+\sum_i|O_i|$. Comparing (8) and (9), cancelling the
common $b,|T_O|,|O_{\rm iso}|$ terms, gives

$$
\sum_i\bigl(|C_i|+|O_i|-\min(|C_i|-e_i,|O_i|)\bigr)
\le 20d+25+e_\Sigma.
$$

Because $\min(|C_i|-e_i,|O_i|)\le\min(|C_i|,|O_i|)$, the left side is at least
$$
\sum_i\bigl(|C_i|+|O_i|-\min(|C_i|,|O_i|)\bigr)
=\sum_i|O_i|+P_\Sigma.
$$
This proves (S1). Also $e_\Sigma\le\sum_i|C_i|\le|C^\partial|\le8d+1$,
proving (S2).

#### Rank, deficiency, and fan consequences

By the canonical Section-175.3 cut bound,

$$
\operatorname{rank}S\le |T_\Sigma|+\sum_i\min(|C_i|,|O_i|)
\le |T_\Sigma|+\sum_i|O_i|.
$$

Equation (S1) is exactly
$$
\sum_i\min(|C_i|,|O_i|)+P_\Sigma+Q_\Sigma\le20d+25+e_\Sigma,
$$
because the left side equals $\sum_i|O_i|+P_\Sigma$. This proves (S3). Subtracting
the rank bound from $|O|$ gives (S5); using (S2) gives its coarser form.

For completeness, the fan tube estimate (S6) follows from one connected-graph
Voronoi-cell argument. Let $V_\phi$ be the centered Voronoi hexagon of a rotated
unit triangular lattice, and $K_\phi=V_\phi+B_1$. Then
$\operatorname{area}V_\phi=\sqrt3/2$,
$\operatorname{area}K_\phi=5\sqrt3/2+\pi$, and
$w_{K_\phi}(n)=w_{V_\phi}(n)+2$. If a lattice point is within one of $\Sigma$,
its full Voronoi cell is contained in $|\Sigma|+K_\phi$. For a connected graph,
adding an edge of length $\ell$ and normal $n$ to an already exposed endpoint
increases the area of this Minkowski sum by at most $\ell w_{K_\phi}(n)$: the
segment-plus-$K_\phi$ has area
$\operatorname{area}K_\phi+\ell w_{K_\phi}(n)$, and the endpoint copy was already
present. For the fan, start instead with its central unit triangle $P_0$, whose
Minkowski sum has area

$$
\operatorname{area}(P_0+K_\phi)
=\operatorname{area}P_0+\operatorname{area}K_\phi
+\frac12\sum_{e\subset P_0}w_{K_\phi}(n_e).
$$

Adding the other $v-3$ edges and averaging the weighted $V_\phi$-width sum over
one rotation period gives some orientation with weighted sum at most
$(2\sqrt3/\pi)(v-3/2)$, by Cauchy's mean-width formula. Divide the resulting
Minkowski-area bound by the Voronoi-cell area $\sqrt3/2$, and use that the tube
count is an integer. The result is exactly (S6), for every translation of the chosen
orientation. Section 154 permits this prescribed rotation and a generic translation.

Finally, the exact identity of Sections 113–115 and 175 is

$$
|O|-j_*=|C^\partial|-s.
$$

From (S5), $h(G)\ge j_*$ follows whenever
$$
|C^\partial|-s+P_\Sigma+Q_\Sigma
\ge |T_\Sigma|+20d+25+e_\Sigma.
$$
The fan tube estimate (S6) bounds the tube term in (A), but does not make (A) hold.
The population audit below shows that (S7) is impossible when $s\ge0$, and that
(S1)--(S5) do not improve the canonical sector cut.

### Population-scale audit

Write $C=|C^\partial|$ and $O=|O|$. The one-sided and exterior boundary-layer
bounds below give

$$
C+O\le (8d+1)+(8d+9)=16d+10.
$$

Consequently (S1) is automatic, even without the common-source matching: indeed
$$
\sum_i|O_i|+P_\Sigma
\le \sum_i(|O_i|+|C_i|)
\le O+C
\le16d+10<20d+25+e_\Sigma.
$$
The rank corollary (S3) is therefore no stronger than the existing sector cut
$\operatorname{rank}S\le |T_\Sigma|+\sum_i\min(|C_i|,|O_i|)$. Algebraically, its
additive term exceeds the existing one because
$$
20d+25+e_\Sigma-P_\Sigma-Q_\Sigma
\ge \sum_i|O_i|-Q_\Sigma
=\sum_i\min(|C_i|,|O_i|),
$$
where the inequality is just (S1). Thus the new source classification, as presently
bounded, supplies no Schur-rank information.

The proposed sufficient cancellation (S7) is impossible throughout the remaining
branch $s\ge0$. Since $b+\sum_i|C_i|=C$ and
$P_\Sigma+Q_\Sigma=\sum_i|C_i-O_i|$,
$$
b-s+P_\Sigma+Q_\Sigma
\le b-s+\sum_i(|C_i|+|O_i|)
\le C+O-s
\le16d+10,
$$
while the right side of (S7) is at least $20d+25$. Do not pursue (S7).

The actual sufficient condition before that cancellation remains
$$
C-s+P_\Sigma+Q_\Sigma
\ge |T_\Sigma|+20d+25+e_\Sigma.
\tag{A}
$$
The population bounds show that (A) can hold only if
$$
|T_\Sigma|+b+s+e_\Sigma\le4d-14.
\tag{B}
$$
This necessary condition follows from $P_\Sigma+Q_\Sigma\le C-b+O$ and is not
established by the current argument.

## 3. Exact frontier effect

This candidate improves the zero-slack source localization crossing charge from
$5|V(\Sigma)|$ (Section 176.5) to $|E(\Sigma)|$. The attempted source-to-sector
rank cap is a population-vacuous regression. This work does **not**
prove the right-sector surplus/coarse-Hall inequality for every canonical survivor,
does not construct a strict sub-$D$ competitor, and does not resolve Target A or
Level I.

The gate comparison uses only the lower bound
$L\ge |C^\partial|+|O|-20d-25$. That displayed floor can be zero under the
canonical one-sided endpoint packing estimates. The comparison remains valid because
$L\ge |C^\partial|+|O|-20d-25$ is true even when its right side is negative; no
positive gate guarantee is claimed. The population audit below shows that the
resulting source-sector cap is tautological at the available scale.

### Closure mechanisms tested

1. **Turn every source gate into a Schur edge.** This fails from the two arm lengths
   alone. Take $a=(0,0)$, $c=(-3/5,0)$, and $o=(3/5,0)$. Then
   $|c-a|=|a-o|=3/5<1$, but $|c-o|=6/5>1$. The point $o$ can be a site
   of a translated unit triangular lattice. The singleton endpoint shores are
   unit-separated, so the local length data do not make $c-o$ a response edge.
   This is only a regression to that local implication; it does not satisfy all
   Target A global-optimum and hull hypotheses and does not refute the canonical
   source-gate theorem. The canonical common-lattice-neighbor fact does not repair
   this implication either. Let
   $$
   y=(0,0),\quad o=(1,0),\quad v=(1/2,\sqrt3/2),\quad
   w=(-1/2,\sqrt3/2),
   $$
   be four vertices of a unit lattice lozenge, and set
   $$
   a=(1/10,1/10),\qquad c=(-4/5,1/10).
   $$
   The point $a$ lies in the interior of that lozenge since
   $a=t\,o+s\,w$ with $s=\sqrt3/15$ and
   $t=1/10+\sqrt3/30$, both strictly between zero and one. Its complete strict
   lattice neighborhood is exactly $\{y,o,v,w\}$: write a lattice site as
   $\lambda_{mn}=(m+n/2,\sqrt3 n/2)$; $|n|\ge2$ is excluded by the
   vertical coordinate, $n=-1$ has vertical squared distance
   $(76+10\sqrt3)/100>84/100$ and horizontal distance at least $2/5$,
   and for $n=0,1$ the only possibilities within distance one are respectively
   $m=0,1$ and $m=-1,0$. Moreover
   $$
   |a-y|=\sqrt2/10<1,\quad |a-o|=\sqrt{82}/10<1,\quad
   |a-v|^2=(92-10\sqrt3)/100<1,
   $$
   and $|a-w|^2=(112-10\sqrt3)/100<1$. Thus $y$ is a strict common
   lattice neighbor of $a$, while $o$ is another strict lattice neighbor
   available as the $O$-endpoint. Yet
   $$
   |c-a|=9/10<1,\quad |c-y|=\sqrt{13/20}<1,\quad
   |c-o|=\sqrt{13}/2>1.
   $$
   So even the Section-164 common-neighbor witness $y$, together with the full
   four-site source lozenge, does not force a direct $C^\partial\!\to O$ edge.
   This is still a local geometric regression, not a counterexample satisfying
   the global source-optimality and hull hypotheses.
2. **Replace a common source by both gate endpoints.** Here is a full-dimensional
   fixed-hull obstruction. Put
   $A^0=\{(-1,0),(0,0),(1,0),(-1,1)\}$ and $H=\operatorname{conv}A^0$.
   These four source points are unit-separated and triangle-free. The triangle
   $H$ has area $1$ and perimeter $3+\sqrt5$. The shared Oler inequality
   (Lemma 21.1) gives
   $$
   \alpha_1(H)\le 2/\sqrt3+(3+\sqrt5)/2+1<115/24<5,
   $$
   so $A^0$ is maximum, with $\alpha_1(H)=4$. Let
   $a=(0,0)$, $c=(-3/5,0)$, and $o=(3/5,0)$. Both arms have length
   $3/5$, while $|c-o|=6/5$, so the two endpoints are mutually compatible.
   However $c$ is blocked by $(-1,0)$, and $o$ by $(1,0)$, each at
   distance $2/5$. Removing only the common source $a$ cannot insert both
   endpoints; removing both blockers as well loses cardinality. This exact example
   shows why fixed-hull maximality alone does not turn a compatible gate into a
   two-for-one exchange. It does not model the response rank or the full canonical
   asymptotic hypotheses.
3. **Minimize the tube independently of the lattice phase.** This does not control
   $j_*(v)=N-|Y_0(v)|-m^*$, which changes with the same phase. The fan estimate
   (S6) is therefore stated for every translation after one orientation is chosen; it
   lowers the tube cost but does not supply the missing sector-surplus lower bound.

## 4. Exact remaining obligation

The source-arm lemma still improves the canonical localization exception count to
$|E(\Sigma)|+8d+1$. To turn it into a Target-A result, one must improve the
source-image overlap estimate enough to produce nontrivial sector information, or
use a different source-to-Schur bridge. The current $20d+25$ band threshold exceeds
the total available $C+O\le16d+10$.

If retaining the current common-source route, prove the actual condition (A) for at
least one admissible generic response phase,

$$
|C^\partial|-s+P_\Sigma+Q_\Sigma
\ge
|T_\Sigma|+20d+25+e_\Sigma,
$$

subject at minimum to the necessary budget (B), or construct an $N$-point
unit-separated configuration of diameter strictly below $D$. Condition (S7) is a
population-impossible sufficient condition, not a live lemma. The other canonical
branch, where the zero-slack source endpoint or the actual-response locked fan is
absent, also remains open.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Strict source arm crosses each fixed unit contact edge at most once | unreviewed candidate | proof above; unit separation of $X^*,A^0$ | Complete strict triangle-inequality proof; needs independent audit |
| One-sided width-one boundary-layer count $8d+1$ | proved candidate | Steiner formula, inner-parallel coarea | Exact area packing argument included above |
| Exterior width-one boundary-layer count $8d+9$ | proved candidate | Steiner formula, inner-parallel coarea | Outside and inside disk portions are both charged explicitly |
| Zero-slack inner-source defect $r\le8d+1$ | unreviewed candidate | Theorem 168.3 and Lemma 2 | Improves the unreviewed $12d+9$ bound; still gives no relation between $r$ and $s$ |
| Co-phased boundary-only response count $|Z_\partial|\le8D+1$ | unreviewed candidate | Corollary 168.2A and Lemma 2 applied to $H$ | Replaces the boundary packing constant $12D+9$ by $8D+1$ |
| Fan-size-independent source-sector rank cap (S1)–(S5) | regression | Sections 168, 175–177 and the boundary-layer bounds | (S1) is automatic from $C+O\le16d+10<20d+25$; (S3) is weaker than the canonical Section-175 sector cut |
| Rotated triangle-core Voronoi tube (S6) | conditional candidate | Section 154 prescribed phase; mixed-area and mean-width formulas | Analytic bound; no numerical certificate |
| Coarse 28d+26 closure threshold | regression | One-sided C/O boundary populations and $s\ge0$ | Its left side is at most $24d+11$, before the nonnegative tube cost |
| Shielded-terminal cancellation (S7) | rejected as a sufficient route | The one-sided source/exterior bounds and $s\ge0$ | Its left side is at most $16d+10$, but its right side is at least $20d+25$ |
| Actual common-source criterion (A) | unresolved | The source-sector gate comparison | It can hold only under the additional necessary budget (B), which is not proved |
| Section-177.5B displayed positive gate floor | regression | canonical endpoint bounds; `docs/reports/target_a_section177_gate_floor_vacuity_regression_2026-10-04.md` (unreviewed) | It is identically zero as a guarantee; actual gates are not ruled out |
| A common-source gate automatically gives a direct (C^\partial\to O) response edge, even with the Section-164 common-lattice witness | local regression | exact lozenge coordinates in Section 3 above | Both arms are below one and the full four-site source cell is present, yet the endpoint distance is $\sqrt{13}/2>1$; no full canonical source/hull claim is made |
| Fixed-hull maximality lets a common source be replaced by both compatible gate endpoints | local regression | exact four-point source hull in Section 3 above; shared Oler Lemma 21.1 | Two distinct remaining source labels block the endpoints; deleting all blockers loses cardinality |
| Zero-loss common-neighbor SDR | rejected | Section 166 | This report does not identify the two matchings or use an SDR upgrade |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Section 166 common-neighbor collision | respected | The source matchings $M_C,M_O$ remain independent; only common image labels are counted |
| Section 177.5B gate-floor vacuity (unreviewed report, salvaged in closed PR #650) | respected | The overlap inequality is used as a signed lower bound, not as a claim of positive gates |
| Common gate implies direct Schur edge, even after adding the Section-164 common-lattice witness | rejected as a data-only implication | The exact lozenge example refutes it; the full canonical source/hull bridge remains open |
| Fixed-hull maximality implies a two-for-one source exchange | rejected as a general implication | The full-dimensional four-point source hull has exact capacity four, but its two compatible gate endpoints are blocked by different remaining source points |
| Contact-isolated source labels | respected | All points of $A^0$ remain in the one-sided source packing and both source matchings |
| Shield-crossing multiplicity | improved candidate | One arm per contact edge is proved from endpoint separation, rather than charging five per shield vertex |
| Finite first-order versus finite motion | not used | No finite motion or endpoint is claimed |

## 7. Literature imports

No external theorem is imported. The literature search checked Z. Füredi,
“The densest packing of equal circles into a parallel strip,” *Discrete &
Computational Geometry* 6 (1991), 95–106,
[DOI 10.1007/BF02574677](https://doi.org/10.1007/BF02574677). The accessible abstract
addresses strip widths $\sqrt3/2<w\le\sqrt3$; it does not provide the width-four
strip estimate considered as a possible way to sharpen the source-band term, so that
lead was not used.

## 8. Computation

Not used. The proof is analytic. No finite verifier is load-bearing.

## 9. Corrections / supersessions

If independently audited, Lemma 1 would strengthen Section 176.5's source-arm crossing
budget. This report does not change canonical state, route maps, or prompts. A closed
noncanonical Target A branch (PR #645) contains an earlier version of the same
one-arm observation and a source-rank cap; it was treated only as a discovery lead and
rederived here against the current `ab6dd333` / `audit.234` authority. No claim from
that branch is a dependency.

## 10. Promotion recommendation

**Unreviewed.** The one-arm crossing lemma, boundary-layer counts, and their
inner-source consequences require independent audit. The common-source gate
classification is valid, but its rank corollary is population-vacuous. No canonical
promotion is recommended in this run.

## 11. Handoff

1. **Strongest result:** the one-arm lemma improves Section 176.5's shield-crossing
   exception charge to one source arm per contact edge. The same shell estimate gives
   $r\le8d+1$ and $|Z_\partial|\le8D+1$, but the attempted common-source rank cap
   is vacuous at the available population scale and is recorded as a regression.
2. **Canonical chain:** Sections 168.2, 175.3–175.4, 176, 177.5, and Section 154
   prescribed-phase freedom.
3. **Exact next theorem:** relate the boundary-order inner-source defect $r$ to the
   Schur demand $s$, or use the $m^*-r$ genuine source points inside $K^*$ to prove
   the canonical three-sector sink-surplus inequality. The common-source route first
   needs a nonvacuous source-overlap lower bound and the necessary budget (B);
   alternatively build a strict sub-$D$ competitor. The branches lacking the
   zero-slack / locked-fan intersection remain.
4. **Binding regressions:** Section 166 SDR collision; Section 177.5B gate-floor
   vacuity; no source-match identification.
5. **Read next:** the current Target A prompt and Sections 168–177; for a proposed
   independent audit, check every common-source endpoint, every source arm meeting a
   shield edge, and phase dependence of $s$ and $C^\partial$.
