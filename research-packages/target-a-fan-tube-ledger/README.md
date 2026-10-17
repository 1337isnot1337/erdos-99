# Exact best-basis full-tube bound for the seed-63 fan

**Unreviewed proof candidate with exact finite evidence. Target A and Level I remain open.**

For the seed-63 triangular chamber, the fixed fan and phase below have
`|T_Z|=2M+1` and `|T_O|=3`. The raw Section-175 right-deficiency lower bound
is **at most `M-1` over every admissible basis matching**, and an explicit
deep-first matching attains that maximum. The predecessor's matching gives
only `1`. Both responses actually have `h=2M+2` and zero left Schur nullity.
Thus basis optimization improves the cut, but even its optimum loses
`M+3` relative to the trivial dimension bound. This is an exact limitation
of this fixed full-tube cut, not a counterexample to the canonical endpoint.

Originating agent: OpenAI Codex (GPT-6), proof, code, arithmetic and handoff.
No independent reviewing agent was used; no promotion is requested. Original
exposition and code are offered under the repository's Apache-2.0 terms.

## Source pins, objective and stopping rule

Baseline: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.
State: `2026-10-15.publication.2`; priority: `public-frontier.3`;
catalogue: `public-frontier.7`. `SOURCES.json` pins the complete predecessor
and the Section-174/175 interfaces by commit and SHA-256.

The selected card is `target-a-locked-sector-surplus`. Its first experiment
asks for every term of the three-channel fan ledger. The objective here is
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

The **optimal matching** maps a row `(i,j)` to

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
For both matchings the nonbasis points lie in the boundary collar, and all
deep source columns belong to the basis: any nonbasis fan point has at
least one barycentric coordinate zero or one. Hence the deep restriction
is independent and fully included, `d_int=0`, and `C^circ` is empty.

## Complete sector ledger and its proof

Let `g=(M^2-3M-2)/2`. In both cases the surviving sector basis and interior
row populations are `(0,g,0,0)` in the order AB, BC, CA, triangle. The
matching gives an actual sector-preserving bijection, rather than a count
obtained by dropping the unmatched side of a pair.

| Quantity | Predecessor basis | Optimal basis |
| --- | ---: | ---: |
| `|C^partial|` | `M+1` | `M+1` |
| `t_Sigma` | `3` | `M+1` |
| `(C_AB,C_BC,C_CA,C_triangle)` | `(0,M-3,1,0)` | `(0,0,0,0)` |
| `(O_AB,O_BC,O_CA,O_triangle)` | `(0,2M-4,2,0)` | `(0,2M-5,0,0)` |
| `|O_iso|` | `M+2` | `M+5` |
| `Q_Sigma=sum (|O_i|-|C_i|)_+` | `M` | `2M-5` |
| `Xi=|O_iso|+Q_Sigma` | `2M+2` | `3M` |
| raw right bound `Xi-|T_Z|` | `1` | `M-1` |
| actual generic `rank S` | `M+1` | `M+1` |
| actual `h=|O|-rank S` | `2M+2` | `2M+2` |
| actual left nullity `zeta` | `0` | `0` |
| loss relative to actual `h` | `2M+1` | `M+3` |

The surviving full source populations are `(0,g+M-3,1,0)` for the
predecessor and `(0,g,0,0)` for the optimal basis. This also verifies the
Section-174 population identity in each sector.

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

## Exact optimization over every basis

For any admissible basis and its closed shield, disjointness gives the
algebraic identity for the **raw Section-175 bound**

$$\Xi_\Sigma-|T_Z|
=|O|-|T_O|-|T_Z|-\sum_i\min(|C_i|,|O_i|)
\le |O|-|T|=M-1.$$

The optimal matching has `C_i=0` in every surviving sector, so it attains
equality. Consequently the maximum is exactly `M-1`; this is an analytic
optimization over all allowed matchings, not a finite sampling of bases.
Both explicit matchings satisfy the stronger deep-first normalization.
The actual deficiency `2M+2` is already forced by the elementary dimension
bound `rank S<=|C^partial|=M+1`, so the best raw tube cut is weaker by `M+3`.
The calculation is not evidence that the Schur theorem itself loses that
amount, or that the separate lens route, another fan or another phase does.

## Reproduction, controls and limits

`verify.py` imports no predecessor implementation or third-party code. It
uses rational projection in the triangular metric, a polygon ray test and
split-vertex flow. Its independent convex-collar enumeration checks the
entire shore before constructing any sectors. Explicit exceptions keep all
checks active under optimized Python. The finite domain is
`M=5,...,20,24,32`, with both matchings: **36 complete ledgers and 72 negative
control instances**. Each ledger deliberately omits basis closure and finds
nonzero sector `B-Z` imbalance; it also omits the two side sink strips and
finds `2M+2` missing actual collar rows. These are rejected incomplete
ledgers, not counterexamples to the correctly stated canonical identities.

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
review. Local execution uses CPython 3.14.8 and only its standard library.
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
basis, and the exact optimum over all bases. It changes no predecessor,
canonical claim, lifecycle, priority, certificate registration or task weight.

The next canonical question is still whether genuine global source-response
information forces `Xi>=j_*+|T_Z|`, or supplies a strict full-source competitor.
A useful first action is to derive a *joint* source-demand and sink-population
ledger for an actual plateau response before selecting its lattice phase;
minimizing the tube alone cannot select a favorable `j_*`. The blocker is
extraction of that actual source information, absent from this nonglobal
chamber. Reopening this same fixture solely to change its basis is unnecessary:
the best possible value for this phase and full tube is already `M-1`.
