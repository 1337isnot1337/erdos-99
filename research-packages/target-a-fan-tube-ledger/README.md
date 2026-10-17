# Admissible and relaxed full-tube bounds for the seed-63 fan

**Fixed-fixture regression with an independent AI-agent audit and exact finite evidence. Target A and Level I remain open.**

For the seed-63 triangular chamber, the fixed fan and phase below have
`|T_Z|=2M+1` and `|T_O|=3`. The maximum raw Section-175 bound is **1 over
Section-102 admissible bases**. The predecessor already attains it.
The value `M-1` is the optimum over a larger class of `Z`-perfect matchings.
Its witness omits `M-2` required deep columns and is inadmissible in Section 102.
Both full Schur complements have generic rank `M+1` and right deficiency
`2M+2`. Only the predecessor has the required canonical boundary interface.
The admissible tube bound loses `2M+1` relative to that actual deficiency.

This corrects [PR #87](https://github.com/1337isnot1337/erdos-99/pull/87)
at `33a4aaa016d0a219e2f9e8e7a92c87ff4aa77afb`. Its checker tested geometric
distance from the hull instead of the incidence definition of `X^circ`.
The companion [audit correction](../../docs/audits/target_a_fan_tube_ledger_independent_audit_2026-10-17.md)
supersedes the same mistaken acceptance in PR #92.

Originating agent: OpenAI Codex (GPT-6), proof, code, arithmetic and handoff.
The correction was developed by the implementing AI session and its mathematical
collaborator. A separate reviewer then reconstructed the proof and ran independent
adversarial checks; see the [audit record](../../docs/research/review-artifacts/fan-ledger-correction/independent-audit.txt)
for its exact source, scope and limitations. No canonical promotion is requested.
Original exposition and code are offered under the repository's Apache-2.0 terms.

## Source pins, objective and stopping rule

Baseline: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.
State: `2026-10-15.publication.2`; priority: `public-frontier.3`;
original catalogue: `public-frontier.7`. `SOURCES.json` pins the complete predecessor
and the Section-102/174/175 interfaces by commit and SHA-256.

The originating card was `target-a-locked-sector-surplus`. Its completed starter
asked for every term of the three-channel fan ledger. The objective here is
to calculate that ledger without merging sinks, omitting basis partners or
discarding an interior tube term, then determine whether choosing a better
basis can repair the loss. The falsification tests are independent exact
segment-distance enumeration, polygon sector classification, basis balance,
complete collar enumeration and vertex-capacitated alternating flow. Stop
once the optimum over bases for this supplied fixture is determined; do not
expand into new random phases or infer global source realization.

The canonical implication remains

$$\Xi_\Sigma\ge j_*+|T_Z|\ \Longrightarrow\ h\ge j_*
\ \Longrightarrow\ \text{the Target A Schur endpoint}.$$

This fixture supplies no original flexible source, `N`, `j_*` or `s`.
Assigning a convenient demand would not instantiate the canonical theorem.
The result measures the cut's loss against a known response rank.

## Complete supplied geometry

Use triangular-lattice coordinates `e1=(1,0)`, `e2=(1/2,sqrt(3)/2)` and
`q(i,j)=i^2+ij+j^2`. For every integer `M>=5`, set

$$X_M=\{(i,j):i,j\in\mathbb Z_{\ge0},\ i+j\le M\},\qquad
v=(1/5,1/7),\qquad K_M=\operatorname{conv}X_M.$$

All lattice row labels below denote the physical point `(i,j)+v`; source
labels denote `(i,j)` without the shift. In particular equal labels on the
two shores are different physical points. The source has
`n=(M+1)(M+2)/2` labels, minimum separation one and diameter `M`.
Nonzero integer lattice differences have `q>=1`, and convexity bounds the
diameter by the three hull corners, with equality on a hull side.

Each source has exactly the strict response neighbors with offsets
`{(0,0),(-1,0),(0,-1)}`. Their squared distances are
`109/1225`, `669/1225`, `739/1225`. Checking zero and the six unit lattice
directions excludes the other four possibilities. Every other nonzero
lattice vector has norm at least `sqrt(3)`: `q` is never two, as its residue
modulo three is zero or one. Since `|v|<1/3`, those vectors remain farther
than one. These strict inequalities also exclude source/row unit equalities.

The **complete** open convex collar shore `Y=(Lambda+v) cap (K_M+B(0,1))`
has labels

$$Z=\{(i,j):i,j\ge0,\ i+j\le M-1\},$$

$$O=\{(-1,j):0\le j\le M\}\ \sqcup\
\{(i,-1):0\le i\le M\}\ \sqcup\
\{(i,M-i):0\le i\le M\}.$$

Here `Z` is strictly inside the hull; all ranges are over integers.
For completeness, a row with `i<=-2` or `j<=-2` is excluded by its distance
to the corresponding hull half-plane. A row with `i+j>=M+1` is excluded
by the third half-plane: its distance is at least
`(sqrt(3)/2)(1+1/5+1/7)>1`. The only remaining labels outside the displayed
ranges are `(-1,-1)`, `(-1,M+1)`, `(M+1,-1)`. Their closest hull corners
give squared distances `2524/1225`, `1264/1225`, `1404/1225`, respectively,
all above one. Each displayed row is a strict neighbor of a source point.
Thus no collar sinks are omitted. In particular `|Z|=M(M+1)/2` and
`|O|=3M+3`. The phase coordinates and their sum exclude hull incidences.

Let `a=(1,1)`, `b=(2,1)`, `c=(1,2)` and reaction endpoints
`r_A=(0,1)`, `r_B=(2,0)`, `r_C=(1,M-1)`. The fan consists of the triangle
`abc`, edges `r_A--a`, `r_B--b`, and the chain
`(1,2)--(1,3)--...--(1,M-1)`. It has `M+2` vertices and edges.
Its four geometric sectors, in the order used by the checker, are polygons
with these vertex lists; consecutive collinear vertices are allowed:

- AB: `[r_A,(0,0),r_B,b,a]`;
- BC: `[r_B,(M,0),r_C,c,b]`;
- CA: `[r_C,(0,M),r_A,a,c]`;
- triangle: `[a,b,c]`.

Fan boundaries are deleted. Hull boundary points outside the fan belong to
the adjacent sector. No sectors are defined by graph connectivity alone.

## Exact tube and two matchings

Direct segment projection gives the following local table. For the unit
segment from zero to `d`, the listed labels `w` are exactly those with
`dist(w+v,[0,d])<1`.

| `d` | Row labels `w` |
| --- | --- |
| `(1,0)` | `(-1,0),(0,-1),(0,0),(0,1),(1,-1),(1,0)` |
| `(0,1)` | `(-1,0),(-1,1),(0,-1),(0,0),(0,1)` |
| `(-1,1)` | `(-2,1),(-1,0),(-1,1),(0,-1),(0,0)` |

These are finite exact rational calculations, reproduced for every integer
`w` in `[-3,3]^2`. That table is exhaustive: outside this box,
`q(w)>=3 max(|w_1|,|w_2|)^2/4>=12`, so distance to the segment is greater
than `sqrt(12)-1/3-1>1`. Reversing a segment only changes its chosen origin.
Union of these translated tables along the fan gives

$$T_Z=\{(0,j):0\le j\le M-1\}\ \sqcup\
\{(1,j):0\le j\le M-2\}\ \sqcup\ \{(2,0),(2,1)\},$$

$$T_O=\{(-1,1),(2,-1),(1,M-1)\}.$$

Therefore `|T_Z|=2M+1`, `|T_O|=3`, `|T|=2M+4`. These sets do not depend on
the matching. The closed shield removes source vertices
`V(Sigma) union mu^{-1}(T_Z)` as well as the tube rows. Every matched row
of a basis fan vertex is in the tube, so this is the full basis closure.

The **predecessor matching**, written here from rows to sources, is the
identity except for these assignments:

$$\begin{aligned}
(0,1)&\mapsto(1,1),& (2,0)&\mapsto(2,1),\\
(1,j)&\mapsto(1,j+1)&& (1\le j\le M-3),\\
(1,M-2)&\mapsto(2,M-2),\\
(i,1)&\mapsto(i+1,1)&& (2\le i\le M-2).
\end{aligned}$$

The **relaxed optimal matching** maps a row `(i,j)` to

$$\begin{cases}
(0,j+1),&i=0,\ j\ge1,\\
(i+1,j),&j\le1,\ i\ge2,\\
(i+1,j),&j\ge2,\ i\ge1,\\
(i,j),&\text{otherwise}.
\end{cases}$$

All rules apply only to rows of `Z`. They are disjoint and cover all rows;
each is a strict conflict edge. The second matching has image exactly
`X_M minus (V(Sigma) minus {a})`, which proves injectivity by row ranges
and population. Thus all `M+1` nonbasis columns are on the fan.
Section 102 defines

$$X^\circ=\{x\in X_M:N(x)\subseteq Z\}
=\{(i,j):i,j\ge1,\ i+j\le M-1\}.$$

The diagonal matching `x -> row x` makes all these columns independent.
Thus the deep restriction has `d_int=0`, and every Section-102 basis must
contain **all** of `X^circ`. The predecessor does. The relaxed matching omits

$$\{(2,1)\}\ \sqcup\ \{(1,j):2\le j\le M-2\},$$

which has `M-2` columns. Having a barycentric coordinate at most one does
not exclude incidence depth. At `M=5`, the geometric-distance predicate
accepts the relaxed matching but it omits `(1,2)`, `(1,3)` and `(2,1)`.
These are explicit negative controls in the corrected checker.

For the relaxed comparison only, write `C=X_M\B` and use the full Schur
complement on all of `C`. Its nonempty `C intersect X^circ` cannot be treated
as the empty deep complement of the canonical normalization.

## Complete sector ledger and its proof

Let `g=(M^2-3M-2)/2`. In both cases the surviving sector basis and interior
row populations are `(0,g,0,0)` in the order AB, BC, CA, triangle. The
matching gives an actual sector-preserving bijection, rather than a count
obtained by dropping the unmatched side of a pair.

| Quantity | Admissible predecessor | Relaxed optimum (inadmissible) |
| --- | ---: | ---: |
| nonbasis column count | `M+1` | `M+1` |
| omitted deep columns | `0` | `M-2` |
| boundary terminal count | `M+1` | `3` |
| nonbasis fan vertices | `3` | `M+1` |
| `(C_AB,C_BC,C_CA,C_triangle)` | `(0,M-3,1,0)` | `(0,0,0,0)` |
| `(O_AB,O_BC,O_CA,O_triangle)` | `(0,2M-4,2,0)` | `(0,2M-5,0,0)` |
| isolated exterior rows | `M+2` | `M+5` |
| sector surplus `Q_Sigma` | `M` | `2M-5` |
| total surplus `Xi` | `2M+2` | `3M` |
| raw right bound | `1` | `M-1` |
| generic rank of full Schur complement | `M+1` | `M+1` |
| full right deficiency | `2M+2` | `2M+2` |
| actual left nullity `zeta` | `0` | `0` |
| loss relative to actual `h` | `2M+1` | `M+3` |

Here `C_i` counts all surviving nonbasis columns in the comparison.
The relaxed matching has no such survivor. Its table does not certify
Section-102 admissibility or the canonical boundary Schur interface.
The surviving full source populations are `(0,g+M-3,1,0)` for the
predecessor and `(0,g,0,0)` for the relaxed basis.

Here are the explicit sink sets, which prove the table without assuming
that an exterior point has a surviving neighbor. In the predecessor case,

$$O_{BC}=\{(i,-1):3\le i\le M\}\ \sqcup\
\{(i,M-i):3\le i\le M\},\qquad O_{CA}=\{(-1,M),(0,M)\},$$

$$O_{\rm iso}=\{(-1,j):0\le j\le M-1,\ j\ne1\}
\ \sqcup\ \{(0,-1),(1,-1),(2,M-2)\}.$$

For the optimal matching remove `(3,-1)` from `O_BC`, make `O_CA` empty,
and add those three sinks to `O_iso`. AB and the triangle have no surviving
sinks in either case. These lists, together with `T_O`, partition **all**
`3M+3` exterior rows disjointly. To verify the lists, an exterior label `o`
can neighbor only sources `o`, `o+(1,0)`, `o+(0,1)`. Delete the fan and
matched partners of `T_Z`, then apply the displayed polygon boundaries.
For example the entire surviving left strip is isolated except `(-1,M)`
in the predecessor case; the optimal matching removes its sole remaining
source `(0,M)`. The other changes follow from removal of `(0,M)` and
`(3,0)`. All endpoints of these integer ranges are retained.

Finally the full response graph has the injective matching `x -> x+v`
saturating every source. Comparing it with either `Z`-perfect matching,
the symmetric difference has disjoint alternating paths starting at each
nonbasis column and ending at distinct exterior rows. A path cannot end
at a matched interior row: its matching edge continues to a basis column.
This gives `M+1` vertex-disjoint terminal-to-sink paths. Conversely there
are only `M+1` terminals. Thus the generic Schur rank is `M+1`.
Equivalently, over independent edge indeterminates the matching monomial
of the corresponding bordered determinant is nonzero; block elimination
subtracts the invertible `Z` basis. This is generic rank, not the rank of
an all-ones specialization. The checker independently reproduces the path
count using split-vertex integral flow for both matchings.

## Exact optimization in the two basis classes

For any `Z`-perfect matching and its closed shield, use all unmatched columns
in `C_i`. Disjointness gives the relaxed algebraic cut identity

$$\Xi_\Sigma-|T_Z|
=|O|-|T_O|-|T_Z|-\sum_i\min(|C_i|,|O_i|)
\le |O|-|T|=M-1.$$

The relaxed matching has `C_i=0` in every surviving sector and attains
`M-1`. This proves the relaxed optimum, but its witness is inadmissible.

Now impose Section 102. Every basis contains `X^circ`, so all `M+1`
nonbasis columns are boundary terminals: `C=C^partial`. The fan has only
three boundary source vertices, namely `r_A`, `r_B` and `r_C`. Therefore
`t_Sigma=|C intersect V(Sigma)|<=3`.

Every exterior row has exactly one source neighbor. The three rows in
`T_O` neighbor only those three boundary fan vertices. Each surviving
terminal consequently has an exterior neighbor outside `T_O` in its own
sector. Different terminals have different neighbors. A terminal is never
a matched basis partner, so closure removes it exactly when it is on the fan.
It follows that `|O_i|>=|C_i|` and

$$\sum_i\min(|C_i|,|O_i|)=\sum_i|C_i|=M+1-t_\Sigma.$$

Substitution in the cut identity gives

$$\Xi_\Sigma-|T_Z|=(M-1)-(M+1-t_\Sigma)=t_\Sigma-2\le1.$$

The admissible predecessor has `t_Sigma=3` and attains equality. Thus **1
is the exact admissible optimum for every integer `M>=5`**. This is an
all-basis proof; the finite checker verifies the witnesses and failure control.
The actual deficiency `2M+2` follows already from
`rank S<=|C^partial|=M+1`, so the admissible raw cut loses `2M+1`.
The lens route, other fans, other phases and actual global sources remain separate.

## Reproduction, controls and limits

`verify.py` imports no predecessor implementation or third-party code. It
uses rational projection in the triangular metric, a polygon ray test and
split-vertex flow. Its independent convex-collar enumeration checks the
entire shore before constructing any sectors. Explicit exceptions keep all
checks active under optimized Python. The finite domain is
`M=5,...,20,24,32`, with both matchings: **36 complete ledgers, 72 ledger
failure controls and 18 admissibility failure controls**. Each ledger deliberately omits basis closure and finds
nonzero sector `B-Z` imbalance; it also omits the two side sink strips and
finds `2M+2` missing actual collar rows. These are rejected incomplete
ledgers, not counterexamples to the correctly stated canonical identities.
At every size, the incidence predicate rejects the relaxed matching that
the historical geometric predicate accepted. The `M=5` omitted set is checked explicitly.

From the repository root:

```sh
python research-packages/target-a-fan-tube-ledger/verify.py > /tmp/e99-fan-normal.json
cmp research-packages/target-a-fan-tube-ledger/evidence.json /tmp/e99-fan-normal.json
python -O research-packages/target-a-fan-tube-ledger/verify.py > /tmp/e99-fan-optimized.json
cmp research-packages/target-a-fan-tube-ledger/evidence.json /tmp/e99-fan-optimized.json
python scripts/research_package.py --package research-packages/target-a-fan-tube-ledger --check-only
python tools/check_public.py
python tools/local_ci.py --base-ref origin/main
```

The checker has no runtime repository reads; `SOURCES.json` additionally
declares the mathematical inputs, this proof and saved generated evidence.
Empty unresolved **file** closure makes no claim of independent mathematical
review. The checker uses only the Python standard library. Actual correction-run
environment and results belong in the integration review record.
Finite replay checks the declared sizes; arbitrary `M>=5` follows from the
local exhaustive tables, the range identities and the universal bound above.
Repository-wide certificate replay is **deferred to the merging agent**.
Final exact-head structural results and planner scope are recorded in the PR.

The source chamber is supplied geometry. The predecessor proves strict
same-cardinality competitors for every `M>=33`, so the unbounded tail is
**nonglobal**. No globality is claimed at the remaining finite sizes. Its
fixed-container saturation, positive stress and fixed-hull lock are credited
to the predecessor, not re-audited here. This package proves the tube,
matching, sector and optimization statements directly, without importing
those stronger hypotheses or any Oler estimate. No physical source labels
are removed from a proposed endpoint; shield deletion is graph accounting.
No planar replacement, original flexible source, all-global-minimizer theorem,
zero-slack resolution or Target A/Level I closure is supplied.

## Predecessor credit and Open next questions

The chamber, phase, fan and first matching come from the AI-produced
[seed-63 report](../../docs/reports/target_a_seed063_tight_isolates_and_locked_fan_regression_2026-10-13.md),
originally source PR #969. Its lens penalty and neutral Schur response already
block stress-to-nullity shortcuts. The independent Schur checker in destination
[PR #78](https://github.com/1337isnot1337/erdos-99/pull/78) checks abstract
rank/linkage and shield bookkeeping. This package adds the previously
uncalculated full **geometric** tube/sector ledger, the explicit optimal
basis, and the distinct admissible and relaxed optima. It changes no predecessor,
canonical claim, lifecycle, priority, certificate registration or task weight.

The next canonical question is still whether genuine global source-response
information forces `Xi>=j_*+|T_Z|`, or supplies a strict full-source competitor.
A useful first action is to derive a *joint* source-demand and sink-population
ledger for an actual plateau response before selecting its lattice phase;
minimizing the tube alone cannot select a favorable `j_*`. The blocker is
extraction of that actual source information, absent from this nonglobal
chamber. Reopening this same fixture solely to change its basis is unnecessary:
the admissible optimum for this phase and full tube is already `1`.

Downstream use: this closes the basis-only repair of this fixture. Future work
must supply a joint source-demand and sink-population inequality for an actual
response, or change an explicit geometric hypothesis. Another basis enumeration
cannot improve the admissible optimum.
