# Independent exact-head audit of PR #147

**Audit decision: PASS for the stated geometric regression only.** One nonload-bearing turn-list correction and a verifier-coverage note are recorded below. This does not establish a global-minimizer result or promote a canonical claim.

## Exact source and independence

- Reviewed PR: [#147](https://github.com/1337isnot1337/erdos-99/pull/147), “Target B: scalable two-grid disk with positive PC1 trim”.
- Exact source head/tree: `a110c4062443aa55c480cfd353af3f756e565803` / `4e0ef5322368f262c46bfdefe85a58bc1a2a2d83`.
- Base: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- State / priority / catalogue: `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`.
- Assigned investigation: `audit-pr147-paired-20261019`; exact scope key `a54ea903ebbfcd78d21a5320`.
- Source contributor: OpenAI Codex, GPT-6 Luna xhigh (construction, proof, checker and report).
- Reviewer: separate OpenAI Codex GPT-6 Luna xhigh session, worker `homelab-16`; it did not produce or edit the source proof or checker.

The six source artifacts were fetched from the exact commit and matched both the assignment SHA-256 and Git blob pins:

| File | SHA-256 |
| --- | --- |
| `README.md` | `847b54dcd6a07054860d71a9d23e07d41208eb06e45cd81e997e1518ebbbd8d7` |
| `RESULT.json` | `8388f8af2a60530276c0e0afa6ecf07254bb6941efb79533fc77971be15d98a7` |
| `SOURCES.json` | `e2f006373c8ddca790c08a8beb9dd07c5d008629e5f5f724abe9c40abbeabc9e` |
| `TASK.json` | `1ca3f47279e288f2e0688bc1316ee94d818895ea734f10bcf89e811fdc6bbe4b` |
| `VERIFY.json` | `f29bb301765a445753d72890279f96f2bcc39c9c3aa9ff59e16c35cb1eaf068e` |
| `verify.py` | `78b07279168ce3aad0ee261e16f847a99b68132729e897a0b9c07bd311f478b0` |

No `candidate.json` exists in that package at the reviewed head. The source package's own ten base-input pins were also checked against their recorded commit. The original bytes were not edited or committed.

**Exposure disclosure:** before deriving the source result, I saw PR #147's live body, which summarizes adjacent reviews #134, #144, #145 and #146, and the Discussion #83 handoff for PR #86. There was no live same-head audit of PR #147 in the open PR list or prior handoffs. I did not use the adjacent audit conclusions as premises: the geometry, filter conditions, PC1 term, determinant ledger and shell comparison below were reconstructed from the pinned PR #147 files and the canonical definitions. The canonical shell upper bound was independently checked in §§21.2 and 36.1–36.3 after that reconstruction.

## Statement audited

For every integer `m >= 12` divisible by four, the source constructs a pure simply connected strict-rhombic disk on `2(m+1)^2` labels. After the Section-50.1 high-defect edge deletion and degree pruning with `eta=1/2`, `lambda=1/4`, the retained train graph has two `K_(m,m)` components. Each grid admits positive PC1 trim depth `d=m/4-2`, yet its PC1 diagonal excess is zero. Across the two components, the noncrossing determinant mass is quadratic, while the proposed generous payment

`V12 <= P12 + (2E + H - J) + (sqrt(3)/2) B`

fails for all sufficiently large `m` (in fact, the bound below proves failure for every allowed `m`). The construction is not a global diameter minimizer: it violates the strict global-minimizer shell upper bound. This is a counterexample to that scalar payment rule under the displayed geometric hypotheses, not to the Target-B endpoint or to Erdős #99.

The task catalogue's pinned existing check is PR #86's abstract shared-interface budget, `R >= G + max(p1,p2,p1+p2-K)`, with finite incidence checks. Its recorded limitation is that geometric realization and payment of virtual mass were not established. PR #147 supplies an actual scalable disk but does not repair the globality/source-transfer gap.

## Independent proof reconstruction

Write `q=m^2`, `p=floor(q/sqrt(3))+1`, `t=p/q`,
`c=(1-t^2)/(1+t^2)`, and `s=2t/(1+t^2)`. Since `q/sqrt(3)` is irrational,
`0 < t-1/sqrt(3) < 1/q`. For `m>=12`, `t<1`; therefore
`0<c<1/2`, `s^2+c^2=1`, `s>sqrt(3)/2`, and `s+c>1`. Set
`x=(1,0)`, `y=(0,1)`, `v=(-c,-s)`, `u=(-s,c)`. The two blocks have vertex sets

`(i-cj,-sj)` and `(-sk,l+ck)`, for indices in `[0,m]`, with the unit square on `x,y` between them.

### Separation, contacts and disk topology

Inside one grid, a nonzero difference with both integer coefficients nonzero has squared length `a^2+b^2-2cab`. Since `2c<1`, this is strictly greater than one; axis differences have length at least one. Between the two grids the vertical gap is `sj+l+ck`. If `j>=2` it exceeds one because `2s>1`. If `j=1` and `k+l>0`, it exceeds one because `s+c>1` or `s+1>1`; for `j=1,k=l=0`, the nearest horizontal gap is `c`, giving squared distance one, and the next coordinate gives `2(1-c)>1`. If `j=0,k>=2`, the horizontal gap is at least `2s>1`; if `k=1,l=0`, the nearest gaps are `s,c` and squared distance one; if `k=1,l>=1`, the vertical gap exceeds one; if `k=0`, the distance is an integer-axis comparison. The same four-corner check for the square gives only tile-edge contacts. Thus the minimum separation is one and every unit contact is a tile edge.

Each grid is colored by coordinate parity. The colorings agree on the two square edges it shares and at the common origin, so the contact graph is bipartite and triangle-free. The interiors occupy three nonoverlapping angular sectors; the two grid blocks meet only at the origin and each shares one full edge with the square. Their boundary is one simple cycle. Counting cells gives `N=2(m+1)^2`, `R=2m^2+1`, `E_cell=4m^2+4m+2`, `N-E_cell+R=1`, and `B=8m`. The independent checker confirms exact pair separation/contact equality, edge incidence, one boundary cycle and Euler characteristic for `m=12,16,20,24`; the coordinate and sector arguments hold for the full family.

### Section 50.1 and PC1

The internal crossing defect is `delta=2 atan(t)-pi/3`; the derivative bound gives `0<delta<2/m^2`. The square's crossing defect is `pi/6`. The source contains a length-`m` side and lies in a box of width `(1+s)m<2m` and height `(1+s+c)m<5m/2`, so `m<=D<4m`. For every allowed `m`,

`delta < 2/m^2 < 1/(2 sqrt(m)) < D^(-1/2) <= 1/sqrt(m) < pi/6`.

Hence the high-defect deletion removes the one square crossing and no grid crossing. After that deletion each of the `4m` tracks has degree `m`. Since `lambda*D=D/4<m`, no degree-pruning step removes a track. The two retained components are exactly the two complete `K_(m,m)` crossing grids, with `2m` tracks each.

For either grid choose `k=l=m/4`. Each retained shore has `m/2` unit vectors and `d=min(k,l)-2=m/4-2>=1`. The triangle inequality gives `|U+V|<=m<=D`; with the chosen coherent directions, the exact squared norm is `m^2(1-c)/2<m^2`. The PC1 term `d(|U+V|-D)_+` is therefore zero. Positive trim depth alone does not force positive penetration charge in this example.

### Physical, virtual and support ledger

The two direction pairs have cross determinants `1,c,c,1`, so the total determinant mass across retained components is `Q12=2(1+c)m^2`. Only the square pair is a physical cross-component crossing, and it is the edge deleted above. Thus `P12=1`, deleted physical cost is one, and `V12=Q12-1`. Within-grid physical area is `2s m^2`; adding the square gives total rhombus area `S=2s m^2+1`. Every other nonzero missing train-pair determinant is cross-component, so the route's missing-crossing mass here is exactly `M=V12`.

The full hull has the six vertices, scaled by `m`,
`(-c,-s),(1-c,-s),(1,0),(0,1),(-s,1+c),(-s,c)`. Each listed edge is supporting for all source vertices, and its turn is positive. The hull area is `(1+2s)m^2`, hence `G=area(K)-S=m^2-1`. The rhombus face excess is `E=2m^2(s-sqrt(3)/2)+1-sqrt(3)/2`.

Summing the boundary support depths gives `H=(4+2c)m^2-2`. Equivalently, the nonzero portions in the source's table sum to this value. The canonical pure-disk identity `H=2G+J` then gives

`J=H-2G=2(1+c)m^2=Q12=V12+P12` and `H-J=2G`.

Therefore the route endpoint quantity is `2E+H-J=2(G+E)`. Subtracting the proposed payment's right side from `V12` gives exactly

`R_m = 2(c-2s+sqrt(3))m^2 - 4sqrt(3)m + sqrt(3)-2`.

For a uniform positive lower bound, `t<3/5` for `m>=12`, hence `c>8/17`, `s<15/17`, and `sqrt(3)>5/3`; it follows that `2(c-2s+sqrt(3))>38/51`. Also `sqrt(3)<7/4`, so

`R_m > (38/51)m^2 - 7m - 1/3 > 0` for `m>=12` (the right side is positive at 12 and increasing thereafter). Thus the displayed scalar payment fails across the whole claimed family, including after granting all of `P12`, `2(G+E)`, and the full `a0 B=4sqrt(3)m` allowance.

Finally, the canonical strict upper side for a global diameter minimizer in a pure disk is `G+E < (sqrt(3)/4)B`. Here
`G+E=(1+2s-sqrt(3))m^2-sqrt(3)/2 > m^2-sqrt(3)/2 > 2sqrt(3)m=(sqrt(3)/4)B` for `m>=12`. The displayed disks therefore cannot be global minimizers. This safeguard is load-bearing for interpreting the regression: no contradiction to the canonical endpoint or conjecture follows.

## Audit notes and corrections

1. **Nonload-bearing hull-turn typo.** For the README's listed cyclic order, the actual consecutive determinants for its vertices scaled by `m` are `m^2*(s, s+c, s-c, s, s-c, s+c)`. The source README lists a different sequence. All six actual values are positive (`s>c`), and the hull claim is independently verified by support half-planes, so this does not affect any conclusion.
2. **Verifier coverage.** The source `verify.py` reconstructs and checks every pair for `m=12,16,20`, but it builds the retained graph by excluding the interface face rather than asserting the exact Section-50.1 angle threshold, does not assert the degree threshold, and reports Euler characteristic without asserting the boundary is one cycle. Its README supplies analytic arguments for those facts. This audit independently checks the filter/pruning inequalities and the single boundary cycle; it also adds `m=24`.
3. **Scope.** The family is not a source-specific global minimizer and does not prove or disprove a source-valid allocation of support-turning `J` among grains. It only falsifies the stated unit-for-unit scalar rule. The source's task and manifest lifecycle remain unreviewed in the canonical tree; this audit is not a promotion transaction.

## Reproduction and evidence

The source command was replayed unchanged under the shared host lock; its output matched pinned `RESULT.json` byte-structure-for-byte-structure after JSON parsing. It passes exact cases `m=12,16,20`.

This package's separately written `verify.py` uses only `Fraction`, integer arithmetic and exact `Q(sqrt(3))` sign comparisons. It independently rebuilds the point set, tile edges, boundary cycle, hull half-planes, support depths, Section-50.1 filter and prune, PC1 trim, and shell/payment signs for `m=12,16,20,24`. It also checks both signs in the surd comparator and the zero-depth boundary control `m=8`.

Commands and actual outcomes are listed in the PR body and `RESULT.json`. No source package bytes were modified. The verifier does not depend on private files or network access.

## Open next questions

The changed hypothesis is a genuine pure-disk realization with two retained coherent grids, a single deleted interface crossing, and positive trim on both grids. The downstream decision is whether the cross-component part `V12` of missing mass `M` can be paid by the shell quantity `G+E`; the exact unallocated term is support turning `J`.

A source-valid allocation `J12` of the global support-turning term `J`, with an endpoint bound on `V12-J12`, would let a later argument sum over retained components. A counterexample to every such allocation under actual global-source hypotheses would instead identify the need for a global-minimizer exclusion or a different competitor mechanism. The first step is to define a component-compatible share of `J` and check it against this exact family; the current blocker is that the canonical identity controls only the global sum of `J`.

## Predecessors

- PR #86 is the reviewed abstract shared-interface inventory; its finite counting was not repeated here.
- PR #131 is the finite three-rhombus interface witness. PR #147 adds a scalable pure disk, exact Section-50.1 retention and positive PC1 trim, plus the full support correction.
- PR #103 supplies a conditional angular-subset lower bound for virtual determinant mass, not a realized grid or support-turning allocation. PR #125 supplies the topology-sensitive Euler identity.
- The source's relevant canonical dependencies are the Oler shell window (§21.2), pure-disk support identity (§25.3), strict `n-1` shell upper (§36.3), Section-50.1 filter/pruning (§50.1) and PC1 (§PC1). Their exact source pins are recorded in `SOURCES.json`.

The missing lemma is a **source-valid allocation or coupling of retained cross-component virtual mass `V12` to the signed residual after the global support-turning term `J` is subtracted**, under hypotheses preserved by the actual global source. A second route would be a global-minimizer condition excluding this two-grid geometry while retaining positive trim. Either would change the cross-component contribution to `M` or `G+E`; the current construction alone cannot decide that quantity for global minimizers.

OpenAI Codex (GPT-6 Luna xhigh) produced this independent proof reconstruction and checker. Mathematical credit for the candidate remains with its source contributor. This original audit text and verifier are offered under Apache-2.0; no external paper text or code was copied. Required full theorem-certificate replay is **deferred to the merging agent**; it was not run here.
