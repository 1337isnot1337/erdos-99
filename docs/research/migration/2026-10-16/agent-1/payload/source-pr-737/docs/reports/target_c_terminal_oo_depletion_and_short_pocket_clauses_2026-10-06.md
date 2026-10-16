<!-- theorem-state: {"artifact_id":"ART-BB718593FC99","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: terminal O--O depletion and the long-pocket cost of binary clauses

Date: 2026-10-06. Authority: `583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1`,
state `2026-10-05.audit.62`. Classification: **proved candidates awaiting
independent audit**. C-II and Level I remain open. No literature import.

## 1. Source-level binary witnesses require long pockets

Use an actual narrow-window selected O--O family whose nonzero owners
satisfy acute binary contact preservation. If an old noncontact `ab` has

\[
 1<|a-b|<\sqrt2
\]

and a common unit-contact neighbor `z`, its endpoints cannot have two
distinct nonzero moving owners.

Indeed, `z` cannot have a third moving label or either endpoint's label:
one old contact would join two distinct acute moving owners. Thus `z` is
fixed. Both `za` and `zb` must be selected cut contacts. The angle between
their oriented unit vectors is

\[
 \theta=2\arcsin(|a-b|/2)\in(\pi/3,\pi/2).
\]

Their projective distance is therefore greater than `pi/3`. Both cannot
belong to the selected direction window. This is an exact finite argument.

Now use audit.62 loaded adjacency. Every loaded-loaded lower witness is
one nonunit loaded-hull side. If its old outer interval has length two,
its two endpoints have a common unit neighbor, so the witness cannot
supply a two-moving-owner implication or incompatibility. A surviving
binary loaded witness must use an interval of length at least three.

With canonical

\[
 u_B=x_B-m_B=\sum_{\text{nonunit hull intervals}}(\ell_i-2),
\]

each such interval costs at least one, and each physical hull side is
one witness. Thus

\[
 \boxed{N_{BB}^{\rm binary}\le u_B.}
 \tag{1}
\]

A loaded-only binary sink with `m` owners requires at least `m+1`
distinct physical witnesses, hence `m+1<=u_B`. The acute role uniqueness
and sink cost are independently checked in the predecessor audit report.
Unary loaded-pair clauses are not excluded by (1).

The first abstract search packet had `m_B=x_B=3`, so `u_B=0`. It is
therefore not realizable in this source-level narrow-window scope. The
strengthened search reserves at least three long-pocket units for its
three loaded witnesses; the four-train packet then survives the *new
abstract budgets* at `m_B=3,u_B=3,x_B=6`. Its source realization and
beneficial pin are still unproved.

## 2. Terminal O--O population theorem

Consider an unbounded sequence of canonical full-core Type-II sources
with

\[
 q/D\longrightarrow\pi,\qquad u_B=o(D).
 \tag{2}
\]

Let `N_OO` count **all** complete stopped trains with two ends on the old
outer contact face, including singleton bridges. Then

\[
 \boxed{N_{OO}=o(D).}
 \tag{3}
\]

This does not require narrow selected directions and allows `m_B=Theta(D)`.
It uses the actual positive KKT equilibrium, the canonical full-source
diameter midpoint bound, the near-disk force hull, and audit.53's
`R_O=o(D^2)` depletion of all outer-ended trains. It is stronger than the
terminal-bank bound when `m_B` remains linear.

### 2.1 Long outer intervals have a small terminal bank

Call an outer interval long if `ell_i>=3`. Its length satisfies

\[
 \ell_i\le3(\ell_i-2),
\]

so all long intervals contain at most `3u_B` edge occurrences. An O--O
train with no good or two-edge-pocket end spends two distinct occurrences
in this bank, so at most `3u_B/2` trains have no such anchor. Every other
O--O train has a unit hull end or a two-edge hull-pocket end.

### 2.2 Such a terminal is separated from its hull normal

For a good end the transverse contact direction `u` is the hull tangent,
so its determinant with the outward unit normal has absolute value one.

For a two-edge pocket, its unit path is an isosceles triangle above its
loaded-hull chord of length `c`. Here `1<c<=2`. If `t` is a unit chord
tangent and `n` its outward unit normal, either terminal contact direction
satisfies

\[
 |u\cdot t|=c/2\ge1/2,
 \qquad
 \boxed{|\det(u,n)|\ge1/2.}
 \tag{4}
\]

The chord is auxiliary; it is never counted as a unit contact. This
estimate uses the two *physical* unit edges only.

### 2.3 A train with such an end cannot have submacroscopic span

Suppose, for a contradiction, that O--O trains `tau_D` with a good or
two-edge-pocket end have terminal midpoint displacement `o(D)`.
Canonical train geometry orients all midpoint steps in the open
`pi/6` cone about `Ju`. Their total length is therefore at most
`2/sqrt(3)` times the terminal displacement. Their midpoint paths lie
in an `o(D)` ball around the anchored end.

Every long hull interval has contact length at most `u_B+2=o(D)`.
All other intervals have length one or two. Therefore an outer terminal
occurrence, even one in a long interval, is `o(D)` from the endpoints of
its assigned loaded-hull interval. In the near-disk force hull, the two
end occurrences of `tau_D` are consequently on one shrinking radial arc.

Choose the shore whose distinguished loaded occurrences lie on the
short cyclic hull interval between those ends. The proper train crosscut
gives this interval, with bridge occurrences retained. Every loaded
vertex on this shore has the same limiting outward radial normal `n_D`.
The normal of the hull side at the anchored terminal differs from `n_D`
by `o(1)`. Strict convexity, the inner/outer disk convergence, and unit
separation ensure this even when the outer walk repeats vertices.

There is no old diameter internal to the short shore: its loaded
vertices have diameter `o(D)`. If it had no loaded vertex at all,
summing positive contact equilibrium on the shore would already be
impossible, because its only contact cut is this train and all its cut
contacts have one coherent orientation.

Otherwise every actual crossing diameter, oriented outward from its
shore endpoint `b`, has vector

\[
 r_h/D=n_D+o(1)
 \tag{5}
\]

uniformly. To see this, canonical `C-FS-GEOM` bounds all diameter
midpoints within `O(D^(3/4))` of the common circumcenter; hence
`r_h=2(b-o)+O(D^(3/4))`. The near-disk short hull interval makes
`2(b-o)/D=n_D+o(1)`.

Summing the **actual vertex KKT equations** on the short shore gives

\[
 A_D u=\sum_{h\text{ crossing}}\beta_h r_h,
 \qquad A_D>0,\quad\beta_h>0,
 \tag{6}
\]

up to changing the sign of `u`. The contact coefficient is positive
because every cut contact is positive and their outside-to-inside
orientation is coherent along the monotone train. No isolate stress
row is introduced.

Taking determinants with `u`, (5) says all terms on the right of (6)
have one common nonzero sign: (4) gives determinant magnitude at least
`1/2-o(1)`. Their positive weighted sum cannot vanish. The left has
determinant zero. This contradiction uses no lower bound on individual
KKT weights.

Thus there is a universal `epsilon>0` along the sufficiently large
class (2) such that every anchored O--O train has terminal displacement
at least `epsilon D`. A failure of such a uniform bound would produce
the contradiction sequence just ruled out. No numerical value is claimed.

### 2.4 Compose with the canonical outer-train depletion

A non-singleton train with terminal displacement at least `epsilon D`
contains at least `epsilon D` strict rhombi, since each midpoint step has
length one. A rhombus belongs to exactly two complete trains. If `R_O`
counts rhombi incident with any outer-ended train, total rhombus incidence
of the anchored O--O family is at most `2R_O`. Consequently

\[
 \boxed{N_{OO}\le\frac32u_B+\frac{2R_O}{\epsilon D}.}
 \tag{7}
\]

Audit.53 gives `R_O=o(D^2)` at (2); hence (3). A singleton bridge cannot
be anchored in this regime, by the same zero-span shore contradiction;
the remaining singletons are charged to long outer intervals.

## 3. Exact composition with the face and train ledgers

Let `K_top=d_H+s_Z` (distinct from the owner count), let `X=Q-f`, and
let `S_BB` count singleton trains with two bounded physical-face ends.
Every outer edge occurrence is a train terminal occurrence, so exactly

\[
 b=2N_{OO}+N_{OB},\qquad
 |\mathcal O|=b-N_{OO},
\]

where `N_OB` counts old outer-to-bounded physical trains. The total
train count is `T=q-K_top+2f`. Therefore the old bounded-to-bounded
population is exactly

\[
 N_{BB}=2f-x_B-K_{\rm top}+N_{OO}.
\]

The rhombi not incident with any outer-ended train remain on this
bounded-to-bounded train graph. Delete its singletons before Mantel:

\[
 N_{BB}-S_{BB}\ge2\sqrt{R_4-R_O}.
\]

Combining gives the finite inequality

\[
 \boxed{2f\ge x_B+K_{\rm top}+S_{BB}
              +2\sqrt{R_4-R_O}-N_{OO}.}
 \tag{8}
\]

At (2), `R_4/D^2 -> pi/(2sqrt(3))` and (3) imply

\[
 \boxed{3x_B+5K_{\rm top}+2X+S_{BB}
       \le [2(\pi-s)+o(1)]D,\qquad
 s=\sqrt{\pi/(2\sqrt3)}.}
 \tag{9}
\]

This follows from `f=q-x_B-2K_top-X`, not addition of independent
depletion bounds. Because `x_B=m_B+o(D)`, it excludes the terminal
cases whose displayed bank combination exceeds `2(pi-s)D` with a
fixed positive margin. Smaller linear banks still satisfy it.

## 4. Hostile boundary checks and the surviving conversion

The short-pocket hypothesis in (4) is necessary. The exact convex
three-edge unit path

\[
 (0,0),\ (0,-1),\ (1,-1),\ (8/5,-1/5)
\]

has all its other pair distances greater than one. Its loaded closing
chord has length squared `13/5`; the first vertical contact has squared
determinant with the chord's outward unit normal `1/65<1/4`.
Thus a long pocket can supply a nearly radial contact end. It is charged
through `u_B` and is not an anchored end. This is a finite geometric
regression, not a canonical or globally optimal source.

The main large-bank case left by (9) has many short *outer-to-bounded*
trains ending on exceptional physical faces. Audit.53's outer-rate
determination gives their response rank, and audit.52 gives complete
face closure and contact integrability. Neither supplies an upper-safe
finite assignment. Pentagon return quotas have zero demand; full-boundary
returns have unrestricted loaded targets. The exact missing conversion
is a face-coupled finite motion or a certified discrete replacement,
using actual diameter loads rather than arbitrary pins.

For example the following leading-order ledger is not contradictory:
`q=b=Q=f=P_5=pi D`, `K_top=X=0` to leading order,
`T=3pi D`, `N_OO=0`, `N_OB=pi D`, `N_BB=2pi D`,
`S_G=pi D`, `S_BB=(2pi-2s)D`, and `sigma_R=0`.
Equation (9) is equality. It contains linear singleton and train-surplus
banks, no O--O supply, and a pentagon bank. It is only an algebraic
ledger; source realization, positive KKT and global optimality are
unproved. It shows why eliminating the large singleton/surplus case
needs the missing physical conversion instead of another cancellation
of these same counts.

Contact isolates remain in the global source. The proofs above use
core equilibrium only on actual core shores. Inactive upper exceptions,
all old diameters and unary lower tests remain mandatory for any proposed
competitor. Neither full-core nor macroscopic-container closure is claimed.

## 5. Dependencies and validation

Canonical: `C-LINEAR-NONMATCH` (finite train geometry and count),
`C-LOADED-HULL` and `C-RHOMBUS-POP` (occurrence order and force hull),
`C-FS-GEOM` (actual diameter midpoints), `C-FULLCORE-NEAR-DISK`,
`C-TERMINAL-PHYSICAL-FRUSTRATION` (outer-train depletion at (2)),
`C-LOADED-NEAR-UNIT-ADJACENCY` (finite loaded witness range), and
the exact bad-interval identity from audit.52/55. The narrow binary
clause theorem additionally uses the stated binary contact-preserving
selected-cut hypotheses; it is not imposed on arbitrary multishears.

The proofs are analytic. The exact verifier
`research/verify_target_c_terminal_oo_geometry_2026_10_06.py` checks
rational two-edge geometry, a positive determinant-cone margin, the
long-pocket regression, and the finite cancellations in (8)--(9).
It does not prove asymptotic source existence, the analytic compactness
argument, KKT realization, or global optimality. All new claims remain
unreviewed in the repository lifecycle.
