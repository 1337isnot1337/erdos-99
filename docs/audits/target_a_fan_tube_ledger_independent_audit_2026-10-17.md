<!-- theorem-state: {"artifact_id":"ART-D6983CBF70C5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Target A seed-63 full-tube ledger: independent audit

**Audited source head:** `33a4aaa016d0a219e2f9e8e7a92c87ff4aa77afb`  
**Base:** `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`  
**Authority:** state `2026-10-15.publication.2`; priority `public-frontier.3`; catalogue `public-frontier.7`.  
**Target A and Level I remain open.** This audit makes no canonical promotion.

## Verdict and scope

**PASS for the stated fixed fixture.** I reconstructed the seed-63 triangular source, phase, response collar, tube, both basis matchings, the sector and sink ledgers, and the generic Schur-rank calculation. The claimed maximum raw Section-175 bound is indeed exactly `M-1` for every integer `M>=5`: a basis-independent inequality gives the upper bound, and the proposed deep-first matching attains it. The predecessor matching's value is `1`. The best bound is still short of the fixture's actual right deficiency `2M+2` by `M+3`.

The finite verifier is useful for checking the coordinate tables and endpoint cases, but it is not the proof of the all-`M` result. The all-`M` conclusion follows from the exact local tube table, explicit integer ranges, and the universal upper bound below. I found no discrepancy in those steps.

This is a fixed fan and phase calculation. The package does not supply the original flexible source, a canonical `j_*`, or a global minimizer. Its triangle-containing chamber is nonglobal for `M>=33` by the credited predecessor result. Neither the chamber's earlier stress claims nor that nonglobality proof is re-audited here.

## Reconstruction

### Phase, source and complete collar

Use triangular coordinates with squared norm `q(i,j)=i^2+ij+j^2` and phase `v=(1/5,1/7)`. The strict response offsets are exactly `0`, `(-1,0)`, and `(0,-1)`: their squared lengths are respectively `109/1225`, `669/1225`, and `739/1225`. The other four possibilities among zero and the six unit lattice directions have squared distance greater than one. Every remaining nonzero lattice difference has `q>=3` (the form is `0` or `1` modulo `3`), so its shifted distance is at least `sqrt(3)-|v|>1`. Thus the conflict shore is exactly the three-neighbor graph used in the package.

For `X_M={(i,j): i,j>=0, i+j<=M}`, the row labels strictly inside the hull are `Z={(i,j): i,j>=0, i+j<=M-1}`. The exterior collar labels are the disjoint union

`(-1,j), 0<=j<=M`; `(i,-1), 0<=i<=M`; and `(i,M-i), 0<=i<=M`.

To see completeness, labels with `i<=-2` or `j<=-2` lie more than one from the corresponding hull half-plane. Labels with `i+j>=M+1` lie more than one from the third half-plane, since their signed distance is at least `(sqrt(3)/2)(1+1/5+1/7)>1`. Among the remaining labels outside the displayed ranges, only `(-1,-1)`, `(-1,M+1)`, and `(M+1,-1)` remain; their squared distances to the closest hull corners are `2524/1225`, `1264/1225`, and `1404/1225`. Every displayed exterior label is strictly within one of a source label. Hence `|Z|=M(M+1)/2`, `|O|=3M+3`, with no omitted collar rows or distance-one ambiguity.

### Tube sets

Exact projection in the triangular metric for a unit segment with direction `(1,0)`, `(0,1)`, or `(-1,1)` gives the three finite offset tables in the source README. These represent all fan edge directions up to translation and reversal. For an offset outside `[-3,3]^2`, `q(w)>=12`; then its distance from a unit segment after the phase shift exceeds `sqrt(12)-1/3-1>1`. Thus the local tables are exhaustive, not a truncation assumption. Translating and taking their union over the fan edges gives

`T_Z={(0,j):0<=j<=M-1} disjoint-union {(1,j):0<=j<=M-2} disjoint-union {(2,0),(2,1)}`

and `T_O={(-1,1),(2,-1),(1,M-1)}`. The pieces are disjoint, so `|T_Z|=2M+1`, `|T_O|=3`, and `|T|=2M+4`. Every basis fan vertex has its matched row in `T_Z`, since that row is a strict conflict neighbor of a fan endpoint. Therefore the reported deletion of fan vertices and the matched partners of `T_Z` is the complete basis closure required by Section 174.

### Matchings and deep-first condition

For the optimal matching, the four cases in the package partition `Z`. Their images are respectively:

* `(0,j+1)` for `i=0,j>=1`;
* `(i+1,j)` for `i>=2,j<=1`;
* `(i+1,j)` for `i>=1,j>=2`;
* `(i,j)` for the remaining rows `(0,0),(1,0),(1,1)`.

Each image differs from its row by a strict conflict offset. The image ranges are disjoint and together equal `X_M` with the fan vertices other than `a=(1,1)` deleted. The complement therefore has exactly `M+1` labels, proving injectivity and showing that every unshielded terminal lies on the fan. Every terminal has a barycentric coordinate at most one, so all deep columns are in the basis.

For the predecessor matching, the nonidentity assignments form two disjoint chains: `(0,1)->(1,1)` followed by the `(1,j)->(1,j+1)` chain, ending with `(1,M-2)->(2,M-2)`; and `(2,0)->(2,1)` followed by `(i,1)->(i+1,1)` through `i=M-2`. Targets within the interior are supplied by the next shifted row in the same chain; the two terminal targets lie on the hull boundary and have no identity row in `Z`. No target overlaps either chain or a fixed identity image. The assignments are strict conflict edges and injective. Its omitted source labels are shallow (fan vertices or hull-boundary labels), so it also satisfies the deep-first restriction.

In both cases `|C|=|X_M|-|Z|=M+1` and `d_int=0`. The optimal matching leaves precisely `V(Sigma)\{a}` as terminals; the predecessor's terminals are the top-boundary labels `(i,M-i)` except `i=2,M-1`, together with `(0,1)` and `(2,0)`. This latter description has `(M-1)+2=M+1` distinct labels and its fan intersection is exactly `{(0,1),(2,0),(1,M-1)}`.

### Sector and sink ledger

Removing `T_Z` leaves exactly `g=|Z|-|T_Z|=(M^2-3M-2)/2` interior rows. They all lie in the `BC` polygon. For either matching, each such row is paired to a source in the same `BC` polygon: the remaining rows have either `i>=3`, or `i=2,j>=2`; the explicit matching rules preserve that sector on these ranges. This proves the actual sector-preserving bijection and gives surviving sector basis counts `(0,g,0,0)`, rather than relying on equality of totals alone.

Each exterior row has exactly one source neighbor: for a left-strip row `(-1,j)` it is `(0,j)`; for a bottom-strip row `(i,-1)` it is `(i,0)`; and for a top row `(i,M-i)` it is itself. Applying the two basis images, fan deletion, and `T_O` therefore gives the sink lists without a shared-sink ambiguity:

| Quantity | Predecessor | Optimal |
| --- | ---: | ---: |
| `C_i`, order AB/BC/CA/triangle | `(0,M-3,1,0)` | `(0,0,0,0)` |
| `O_i`, same order | `(0,2M-4,2,0)` | `(0,2M-5,0,0)` |
| `|O_iso|` | `M+2` | `M+5` |
| `Q=sum_i (|O_i|-|C_i|)_+` | `M` | `2M-5` |
| `Xi=|O_iso|+Q` | `2M+2` | `3M` |
| `Xi-|T_Z|` | `1` | `M-1` |

For the predecessor, `O_BC` consists of `(i,-1)` and `(i,M-i)` for `3<=i<=M`, while `O_CA={(-1,M),(0,M)}`. Its isolates are `(-1,j)` for `0<=j<=M-1,j!=1`, plus `(0,-1),(1,-1),(2,M-2)`. The optimal matching removes `(3,-1)` from `O_BC`, empties `O_CA`, and moves those three rows into the isolate set. These are disjoint lists, and together with the three exterior tube rows they partition all `3M+3` exterior labels. The predecessor's surviving source populations are `(0,g+M-3,1,0)` and the optimal populations `(0,g,0,0)`, agreeing with the Section-174 local population identity.

### Generic rank and the universal optimum

With algebraically independent edge entries, the diagonal conflict matching `x -> row x` saturates every source label: all such rows are in `Z sqcup O` and the phase makes every diagonal edge strict. Thus the full incidence matrix has generic column rank `|X_M|`. Each listed `Z`-perfect basis makes `A[Z,B]` invertible, so the Schur rank is `|X_M|-|Z|=M+1`. Consequently `h=|O|-rank(S)=2M+2`; since `|C|=M+1` and `d_int=0`, the left nullity is zero. This is a generic structural-rank statement; it does not assert the rank of a numerical all-ones specialization.

For any admissible basis, `O=T_O disjoint-union O_iso disjoint-union (disjoint-union_i O_i)`, and every `C_i` is nonnegative. Hence

`Xi-|T_Z| = |O|-|T_O|-|T_Z|-sum_i min(|C_i|,|O_i|) <= |O|-|T| = (3M+3)-(2M+4)=M-1`.

The optimal matching has `C_i=0` in every surviving sector and attains equality. This proves the exact maximum over all admissible bases; the finite sample is not used to infer the universal upper bound. Since the actual `h` is `2M+2`, the best full-tube bound loses `M+3` on this fixture. The predecessor's loss is `2M+1`.

## Reproduction and limits

From the exact source head `33a4aaa016d0a219e2f9e8e7a92c87ff4aa77afb`:

```sh
python research-packages/target-a-fan-tube-ledger/verify.py > /tmp/fan-normal.json
cmp research-packages/target-a-fan-tube-ledger/evidence.json /tmp/fan-normal.json
python -O research-packages/target-a-fan-tube-ledger/verify.py > /tmp/fan-optimized.json
cmp research-packages/target-a-fan-tube-ledger/evidence.json /tmp/fan-optimized.json
python scripts/research_package.py --package research-packages/target-a-fan-tube-ledger --check-only
```

I ran both replays and both byte comparisons successfully. They cover `M=5,...,20,24,32`: 36 complete ledgers and 72 intentionally failing ledger controls. The package metadata check reported `metadata-valid`, zero unresolved files, and did not claim mathematical approval. The all-`M` proof is the reconstruction above, not the finite execution.

The exact unresolved canonical step remains: derive `Xi>=j_*+|T_Z|` for an actual stress-generated plateau response using its original full source labels, or construct a strict same-cardinality competitor. The fixed fixture supplies neither `j_*` nor the required global source-response information. Therefore this result closes only the basis-optimization question for this one fan/phase and leaves Target A and Level I open.

**Provenance:** independent audit by OpenAI Codex (GPT-6) of the exact PR #87 head. The originating AI-produced package and the seed-63 predecessor receive the credit recorded in that package. This audit does not update the theorem manifest or promote a canonical claim.
