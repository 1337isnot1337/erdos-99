# Target C-II — `g=0.0021` internal/transverse physical normal form

**Date:** 2026-09-15  
**Status:** proof-only synthesis; theorem-state authority unchanged  
**Scope:** no-container full-core Type-II branch at the independently audited minimax atomic gap `g=0.0021`  
**LEVEL I STATUS:** `STILL OPEN`

Two independently audited geometric upgrades substantially strengthen the physical
normal form at the current low-`t` endpoint:

1. on the tooth branch, shallow-tooth **internal edge injectivity** places one distinct
   strongly inward unit contact entirely inside an unloaded harmonic component for
   every sufficiently shallow tooth;
2. on the rounded long-side branch, the outer-face angular-sector multiplicity theorem
   replaces the old straight-event factor `10` by `4`.

Propagating the audited `g=0.0021` scalar checkpoint gives the following branch
alternative.

### Tooth branch

\[
\boxed{
{E_{int}\over D}
\ge0.3937667468701161781\ldots-o(1),
}
\tag{NF.1}
\]

where every counted edge

- is an actual unit contact;
- has both endpoints unloaded;
- lies inside one unloaded positive-contact component; and
- has inward component greater than
  \[
  \boxed{
  Y_{1/15}
  ={29\sqrt3-\sqrt{59}\over60}
  =0.7091387945271472\ldots .
  }
  \tag{NF.2}
  \]

The resulting unweighted inward-flux sum is greater than

\[
0.2792352762\ldots D-o(D).
\tag{NF.3}

### Rounded long-side branch

\[
\boxed{
{E_\perp(\pi/6)\over D}
\ge0.0977831787370802\ldots-o(1),
}
\tag{NF.4}

where every counted edge is an actual unit contact with transverse component greater
than `1/2` relative to its associated long loaded-hull side direction.  Hence the
unweighted transverse-flux sum is greater than

\[
0.0488915893\ldots D-o(D).
\tag{NF.5}

The weaker physical normal form with floors `0.2128D` and `0.0391D` remains valid but
is numerically superseded by (NF.1) and (NF.4).

## 1. Shared audited scalar checkpoint

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
C_0=2\sqrt{\Delta_2}+0.0021,
\]

and

\[
t_{21}={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0017279.
\]

The §171 squeeze gives

\[
R(t_{21})=0.00567555,
\qquad
\delta:={d_{out}\over D}\le0.002837775+o(1).
\tag{NF.6}

The tooth/long-side scalar split gives the same branch floor

\[
\boxed{
F_{21}=0.4363333718701161781\ldots .
}
\tag{NF.7}

Thus either

\[
N_2/D\ge F_{21}-o(1)
\]

or

\[
L_{>2}/D\ge F_{21}-o(1).
\]

## 2. Tooth branch: internal-edge injectivity at `eta=1/15`

The hostile-audited shallow-tooth internal-penetration theorem states that for

\[
\eta={1\over15}
\]

every `eta`-shallow two-edge tooth supplies one **distinct** internal unloaded-to-
unloaded contact.  The only teeth discarded are those with base deficit exceeding
`eta`, and the metric Markov bound gives

\[
N_{sh}(1/15)
\ge N_2-{d_{out}\over1/15}.
\tag{NF.8}

Therefore on the tooth branch,

\[
\begin{aligned}
\liminf {E_{int}\over D}
&\ge
F_{21}-15(0.002837775)\\
&=0.3937667468701161781\ldots .
\end{aligned}
\tag{NF.9}

This proves (NF.1).

The internal-penetration theorem gives exactly

\[
Y_{1/15}
={29\sqrt3-\sqrt{59}\over60},
\]

which proves (NF.2).  Multiplying the two safe lower bounds gives (NF.3).

The important classification is not merely directional.  Every selected edge lies
inside one unloaded harmonic component, so (NF.1) can be charged directly to the
component variables `e_r`, component geometry, or componentwise deformations.

## 3. Long-side branch: sector multiplicity and bridge suppression

The angular-sector multiplicity theorem gives for every

\[
0<\beta\le\pi/6
\]

\[
\liminf {4E_\perp(\beta)\over D}
\ge
\liminf {L_{>2}\over D}
-\delta\left(1+{2\over1-\cos\beta}\right).
\tag{NF.10}

This already includes the audited bridge suppression of loaded degree-two repeated
outer-route events.

Set

\[
\beta={\pi\over6}.
\]

Then (NF.6)--(NF.7) give

\[
\begin{aligned}
\liminf {E_\perp(\pi/6)\over D}
&\ge {1\over4}
\left[
F_{21}
-0.002837775
\left(1+{2\over1-\sqrt3/2}\right)
\right]\\
&=0.0977831787370802\ldots .
\end{aligned}
\tag{NF.11}

Every selected edge has transverse component greater than

\[
\sin(\pi/6)=1/2,
\]

which proves (NF.4)--(NF.5).

## 4. Current endpoint in physical terms

The low-`t` full-core survivor must now realize one of

```text
TOOTH / HARMONIC-INTERNAL BRANCH
  >= 0.3937667468 D-o(D) distinct unloaded-to-unloaded internal unit contacts,
  each penetrating inward by > 0.7091387945 in the local tooth normal;

ROUNDED LONG-SIDE BRANCH
  >= 0.0977831787 D-o(D) distinct physical unit contacts,
  each transverse by > 1/2 to the associated long-side tangent.
```

This is a weight-free statement.  No individual KKT multiplier lower bound is assumed.

The next closing step is no longer to improve the scalar `q-k` floor.  It must use the
placement of these edges:

- on the tooth branch, the edges are internal to unloaded harmonic components whose
  tooth apexes are augmented triangular faces;
- on the long-side branch, the edges occur at near-straight outer-route boundary
  events and should be charged to train/interface direction capacity or a boundary
  deformation.

## 5. Scope audit

- The tooth-edge injectivity theorem has passed an independent hostile audit.
- The `1/15` threshold is within its certified `alpha_eta<pi/12` range.
- The long-side multiplicity improvement counts angular outer-face sectors, so it is
  safe under articulation/repeated-vertex outer walks.
- Bridge suppression is used only in its audited asymptotic form.
- The numerical endpoint uses `g=0.0021`, not the provisional `0.002123` refinement.
- All counted objects are actual physical unit-contact edges.
- Contact-isolated source points remain in the full source.
- No exact unit equilateral triangle or strict same-cardinality sub-`D` competitor is
  produced.

**Disposition:** proof-only current physical normal form.  C-II and Level I remain open.
