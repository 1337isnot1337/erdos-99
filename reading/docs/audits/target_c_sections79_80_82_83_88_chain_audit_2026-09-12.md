> Generated reading edition · [exact source](../../../docs/audits/target_c_sections79_80_82_83_88_chain_audit_2026-09-12.md) · source SHA-256 `6bc2faa43167f7c7373df84e8aa219dec487136a49ddd19915d9648f620f49ac`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4A8A00F09D74","canonical":true,"claim_ids":["C-HARMONIC-CARRIER-QUAD","C-HARMONIC-CELL-TILING","C-HARMONIC-WRAPPING"],"claim_statuses":{"C-HARMONIC-CARRIER-QUAD":"canonical","C-HARMONIC-CELL-TILING":"canonical","C-HARMONIC-WRAPPING":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — Sections 79, 80, 82, 83, and 88 chain audit

**Date:** 2026-09-12
**Verdict:** **PASS**, with the dependency order stated below.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit independently checks the proof-only Target C chain needed by Section 88:

```text
canonical stack -> Section 79 -> Section 80
canonical Section 78 -> Section 82
canonical Section 62 + Section 79 -> Section 83
canonical Section 62 + Sections 80,82,83 -> Section 88
```

The audit does not infer canonical status merely from the files being on `main`. It
reconstructs the load-bearing implications and records the regression that invalidated
the older high-diameter cap argument.

## 1. Section 79 — inactive chamber / rhombic saturation dichotomy

**Verdict: PASS.**

Canonical Section 77 gives

- `a0 Z_ch = A_ch + O(D)`;
- total inactive-chamber perimeter `P_ch <= 13 pi D`.

For chamber areas `A_j`, isoperimetry gives

`sum sqrt(A_j) <= P_ch/(2 sqrt(pi)) = O(D)`.

Therefore, with `A_max=max A_j`,

`A_ch <= sqrt(A_max) sum sqrt(A_j)`,

so any `A_ch=Omega(D^2)` forces `A_max=Omega(D^2)`. Since
`a0 Z_ch=A_ch+O(D)`, quadratic inactive population is equivalent at leading order to
quadratic inactive area, and hence forces one actual macroscopic inactive chamber.
Conversely `A_max=o(D^2)` forces `A_ch=o(D^2)` and `Z_ch=o(D^2)`.

In the no-macroscopic-chamber branch, canonical Section 67 gives

`m=R4+f+q-k+1`,

with `f,q,k=O(D)`, while canonical Section 68 gives total strict-rhombus area excess
`E4=O(D)`. Combining these with `a0 m=A_F-o(D^2)` yields

`A4=A_F-o(D^2)`.

The fixed-width Section-69 phase cut removes only `O_epsilon(D)` rhombi and retains
total physical perimeter `O_epsilon(D)`, so the coherent grains still fill the force
hull to `o(D^2)` area. The square-root grain bound gives the stated small-grain tail.
No hidden deletion of contact isolates or positive-core assumption occurs.

## 2. Section 80 — global container concentration and Type-II disk limit

**Verdict: PASS.**

The main potentially dangerous input is the equality-scale external population
statement. It is genuinely canonical: Section 77 derives

`a0 Z_ext = pi D^2/4 - A_F + O(D)`

by sandwiching the full-source and force-hull populations between the strict
translated-lattice lower bound and Oler upper bounds. It is not a one-sided cap
estimate.

Section 68 gives `delta_K=pi D^2/4-area(K)=O(D)`, hence the total exterior-cap area
satisfies

`A_ext=pi D^2/4-A_F+O(D)=a0 Z_ext+O(D)`.

The cap perimeter identity gives total cap perimeter at most `2 pi D`. Therefore the
same isoperimetric concentration argument used in Section 79 proves that quadratic
external population forces one macroscopic exterior cap with quadratic source
population and `O(D)` individual Oler slack.

If neither an internal inactive chamber nor an exterior cap is macroscopic, Sections
79 and 80 give

`Z_ch+Z_ext=o(D^2)`, hence `n-m=o(D^2)`.

Canonical Section 77 gives `a0 n=pi D^2/4+O(D)`, so

`m/D^2 -> pi/(2 sqrt(3))` and `area(F)/D^2 -> pi/4`.

The force hull itself has diameter exactly `D`: a normalized KKT stress has at least
one positive actual diameter row, and both endpoints lie in the loaded vertex set
inside `F`; conversely `F` lies in the source hull of diameter `D`. Thus normalized
force hulls have diameter one and area tending to the planar isodiametric maximum.
Blaschke compactness plus uniqueness of equality in the planar isodiametric theorem
forces every subsequential Hausdorff limit, after translation, to be the radius-`1/2`
disk. This justifies the Type-II near-disk statement.

The claim that source points outside the positive-contact core are contact-isolated is
also current-scope valid: Section 67 uses the relative-interior KKT stress, which is
strictly positive on every actual contact/diameter row, so every source incident to an
actual equality belongs to the full-support core.

## 3. Section 82 — harmonic carrier near-quadrangulation

**Verdict: PASS.**

For one unloaded harmonic component `I_r` with attachment set `A_r`, induced contact
graph `H`, local pinned surplus `s`, and loaded-loaded contact count `c`, the exact
Euler/face-incidence calculation gives

`L+Q = 4a-6-2s-2c`.

The Section-62 outer-walk and attachment-stress inequalities imply

`F4 >= n+8+3s+2c-3a >= n-3a+8`,

and the matching coarse upper bound gives `F4<=n+a-4`. The full strict-rhombus complex
has physical boundary `O(a)`.

The geometric prerequisites are valid:

1. no unloaded harmonic vertex lies on the boundary of `P=conv(A)`; positive harmonic
equilibrium plus a supporting line would force all unit neighbors collinear, giving
degree at most two;
2. adding the missing attachment-polygon sides makes the local graph 2-connected;
every component after deleting one vertex still contains an attachment, otherwise the
discrete maximum principle with one boundary value collapses that component;
3. bounded faces are therefore simple, and positive equilibrium excludes reflex
angles at unloaded vertices, so four-faces are convex strict unit rhombi.

For the canonical Section-78 carrier, the embedded quadratic rhombic subgrain forces
`n_*=Omega(D^2)`, while Section 62 gives `a_*=Theta(D)`. Hence

`F4,*=n_*+O(D)=Theta(D^2)`

and its outer/nonquadrilateral physical defect is `O(D)`. Re-running the Section-68/69
phase cut on the complete local rhombus complex is therefore legitimate.

## 4. Section 83 — attachment-cell disjointness and area additivity

**Verdict: PASS.**

The proof has two independent planar steps.

First, if an edge of `P_r=conv(A_r)` properly crossed an edge of `P_s`, their four
loaded endpoints would alternate on the convex force-hull boundary. Contact paths
through the two distinct connected unloaded components would be vertex-disjoint arcs
joining alternating boundary pairs in a disk, impossible in the plane contact graph.
Thus cell boundaries do not properly cross.

Second, containment is impossible. If `P_s subset P_r`, extremality of every loaded
vertex in `F` forces `A_s subset A_r`. Since every unloaded component has at least
three loaded attachments, two component nodes together with three shared loaded
vertices form an incidence subgraph with `e=6`, `q=3`, `c=2`, contradicting the
canonical Section-62 plane-incidence bound `e<=q+2c-2=5`.

Therefore distinct harmonic cells have disjoint interiors. Section 62 already gives
`sum per(P_r)=O(D)`, hence `sum sqrt(area(P_r))=O(D)`.

In the Section-79 rhombic-saturation branch, only `O(D)` strict rhombi touch loaded
vertices because every loaded vertex has positive-contact degree at most three. Every
remaining strict rhombus has all four vertices in one unloaded component and lies in
that component's harmonic cell. Thus

`sum area(P_r)=area(F)-o(D^2)`

and, writing `A4,r` for the unloaded-only rhombus area in cell `r`,

`sum_r (area(P_r)-A4,r)=o(D^2)`.

All deficits are nonnegative, so almost all macroscopic cell area is locally rhombus
saturated.

## 5. Section 88 — harmonic wrapping threshold and macroscopic long carrier

**Verdict: PASS.**

The old near-circle cap reports contained a real error: a circle subset of Euclidean
diameter at most `mu<1` need not lie in one arc of angular length `2 asin(mu)` once
`mu>=sqrt(3)/2`. Three equally spaced circle points are the sharp `120`-degree
counterexample. Section 88 explicitly removes that premise.

For a wrapping support set of normalized diameter `lambda<1`, put
`theta=2 asin(lambda)`. Three support anchors whose triangle contains the disk center
have cyclic gaps `g1+g2+g3=2 pi`, each at most `theta`. In the `g1` gap, the third
anchor restricts admissible points to endpoint intervals of lengths
`theta-g3` and `theta-g2`. Summing cyclically gives total allowed angular measure

`6 theta - 4 pi`.

The Type-II annular convergence converts angular measure `L` into force-hull boundary
length `(D/2+o(D))L`. Unit separation then gives

`limsup |A_r|/D <= 6 asin(lambda)-2 pi`.

Canonical Section 62 gives `t_r>=d_r+1` and loaded positive-contact degree at most
three, hence

`liminf |A_r|/D >= lambda/3`.

Thus every wrapping limit satisfies

`lambda/3 <= 6 asin(lambda)-2 pi`.

The left-minus-right function is strictly monotone on `[sqrt(3)/2,1)`, giving the
unique threshold

`mu0=0.889670810115...`.

For `mu<mu0`, every short macroscopic cell limit is cap type. Minimal short support
arcs are laminar: partial overlap would make the two support chords cross and force an
open intersection of the convex cell interiors. The exact circular-cap capacity is

`C(mu)=[2 pi-k sin(theta_mu)-sin(r_mu)]/8 < pi/4`.

Section 83's square-root area budget makes the total area of cells below `eta D^2`
`O(sqrt(eta)D^2)`, so the cap capacity transfers from finitely many Hausdorff limits
back to the varying cell family. Therefore cells with diameter `>mu D` carry at least
`Gamma(mu)D^2-o(D^2)`, where `Gamma(mu)=pi/4-C(mu)>0`.

The total cell-perimeter bound makes the number of such long cells uniformly bounded.
Hence one long cell has area `Omega_mu(D^2)`. Since the summed nonnegative local
rhombic deficit from Section 83 is `o(D^2)`, a maximizing long cell has rhombic filling
fraction `1-o(1)`. Taking `mu` to `mu0` slowly is uniform because
`Gamma(mu0)=0.3215335659...>0`; it yields

`diam(P_*) >= (mu0-o(1))D`, `area(P_*)>=c_*D^2`, and local rhombic fill `1-o(1)`

for one absolute `c_*>0`.

## 6. Dependency and lifecycle conclusion

The dependency order is acyclic and contains no rejected cyclic-cap theorem, no
full-source misuse of ZR/ZF, and no historical high-`mu` cap premise:

```text
C-INACTIVE-CHAMBER + C-RHOMBUS-POP + C-PUNCTURED-PHASE + C-COHERENT-GRAINS
    -> Section 79
Section 79 + canonical Section 77/68
    -> Section 80
C-HARMONIC-GRID-LOCAL + C-ATTACH-CURRENCY
    -> Section 82
C-ATTACH-CURRENCY + Section 79
    -> Section 83
C-ATTACH-CURRENCY + Sections 80,82,83
    -> Section 88
```

Section 88 remains a structural advance, not a proof of C-II. Its live Type-II
obstruction is quantitative grid coverage/minimality inside the `0.88967...D`
locally saturated harmonic carrier. The Type-I obstruction remains the inactive
packing's internal blocking/collective-deformation problem.

**Promotion recommendation:** Sections 79, 80, 82, 83, and 88 may be promoted together
in one theorem-state transaction with explicit dependency edges in the order above.
