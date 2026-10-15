<!-- theorem-state: {"artifact_id":"ART-3BCD66ABB9C7","canonical":true,"claim_ids":["C-PHYSICAL-FACE-DEPTH-POPULATION","C-SUBQUADRATIC-MACROFACE-NEAR-LOAD-CONTACTS"],"claim_statuses":{"C-PHYSICAL-FACE-DEPTH-POPULATION":"canonical","C-SUBQUADRATIC-MACROFACE-NEAR-LOAD-CONTACTS":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: physical-face return depth

Date: 2026-10-07. Audit base: `7859ac1fe23ac9d40ab3f3c4cdd626b8abdde523`, state `2026-10-07.audit.88`; Target C C-II open. Frozen source: PR #722, branch `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. Source artifact: [`target_c_macroscopic_face_return_depth_2026-10-05.md`](../reports/target_c_macroscopic_face_return_depth_2026-10-05.md).

## Verdict

**PASS — promote** the finite physical-face depth-population bound and its subquadratic-core macroscopic-face corollary, with the dependencies and scopes stated below.

The source report’s additional residual-cage/refill application is **not promoted**. The return lengths are contact-graph path lengths; they do not supply independent packing sites, spare capacity, or a finite competitor. The old wall-safe packet composition is also superseded at its stated hypotheses by Audit.86.

## 1. Exact statements

Use a canonical triangle-free C-II source with `D>=9`. Let `V` be its nonisolated positive-contact core and `B` its actual loaded diameter endpoints. Contact-isolated source points remain in the full source and are not included in `|V|`.

Let `Gamma` be a bounded actual physical contact face whose boundary is a simple cycle of `m>=5` contact edges. For each boundary vertex `x`, put

```text
d(x) = min_{b in B} |x-b|,
d_1 <= ... <= d_m = the sorted boundary depths,
k = ceil((m+2)/2).
```

**Finite population theorem (`C-PHYSICAL-FACE-DEPTH-POPULATION`).**

```text
|V| >= k + sum_{i=1}^k ceil(d_i).
```

In particular, if `t` boundary vertices have depth at least `rho>0`, then

```text
|V| >= k + ceil(rho) * max(0, k-m+t).
```

The only nontrivial dependency for this finite theorem is canonical `C-GLOBAL-FACE-RETURN-QUOTAS`, specifically its full-boundary single-face corollary. Apply it with no auxiliary edges, so the selected face remains this actual physical face. Its `k` paths start at distinct boundary vertices, are mutually vertex-disjoint in the actual contact graph, and end at distinct actual loaded vertices; a length-zero path at a loaded boundary vertex is allowed.

**Asymptotic corollary (`C-SUBQUADRATIC-MACROFACE-NEAR-LOAD-CONTACTS`).** Consider canonical sources with `D->infinity`, `|V|=o(D^2)`, and a bounded actual physical contact face as above with area at least `aD^2` for fixed `a>0`. Then its boundary length obeys

```text
2*sqrt(pi*a)*D <= m <= 13*pi*D,
```

where the lower bound is the planar isoperimetric inequality and the upper bound is the `C-INACTIVE-CHAMBER` total exceptional-chamber perimeter bound. For every fixed `eta>0`, if `t_eta` counts boundary vertices at distance at least `eta D` from the actual loaded set `B`, then

```text
t_eta <= m/2 + o(D).
```

Thus at least `m/2-o(D)` boundary vertices lie within `eta D` of actual loaded vertices, for every fixed `eta`; no rate uniform as `eta->0` is asserted. In particular, a fixed positive fraction more than half the boundary cannot remain a fixed macroscopic distance from `B`, and the entire boundary cannot do so.

Dependencies: `C-PHYSICAL-FACE-DEPTH-POPULATION` and `C-INACTIVE-CHAMBER`. The latter is needed for the stated linear perimeter upper bound; the finite count and the `t_eta<=m/2+o(D)` conclusion already give the depth restriction, but the promoted corollary records the stronger perimeter bracket claimed in the source.

## 2. Independent reconstruction of the finite count

The canonical full-boundary quota gives `k` simultaneously vertex-disjoint actual contact paths from distinct vertices of `partial Gamma` to distinct vertices of `B`. Truncate each at its first loaded vertex. Truncation preserves vertex-disjointness and distinct endpoints. If a path begins at `x` and has `ell` edges, the triangle inequality along its unit contact edges gives `ell>=|x-b|>=d(x)` for its loaded endpoint `b`; since `ell` is integral, `ell>=ceil(d(x))`. The path contains `ell+1` vertices of `V`.

Summing over the `k` disjoint paths gives at least `k` start vertices plus the sum of their rounded depths. Among any `k` distinct boundary starts, the smallest possible rounded-depth sum is `sum_{i=1}^k ceil(d_i)`. This proves the first inequality. If `t` starts are deep, at most `m-t` starts can be shallow, so at least `max(0,k-m+t)` selected paths have depth at least `rho`. Each contributes at least `ceil(rho)` edges in addition to the `k` path vertices. This proves the second inequality.

The endpoints are actual loaded source vertices, not arbitrary pins. The paths use actual unit contacts, not an auxiliary augmented edge. No path families from different faces are added. Contact isolates are neither path vertices nor silently counted in `V`.

## 3. Independent asymptotic deduction

For `t=t_eta`, apply the finite inequality with `rho=eta D`. If `t<=m-k`, then `t<=m-k`; otherwise

```text
t <= m-k + (|V|-k)/ceil(eta D).
```

Since `k=ceil((m+2)/2)`, `m-k<=m/2`. Also `|V|=o(D^2)` and `ceil(eta D)=Theta(D)` for fixed `eta`, so the correction is `o(D)`. Hence `t_eta<=m/2+o(D)`.

For a bounded face of area at least `aD^2`, isoperimetry gives `m>=2sqrt(pi*a)D`. Because `m>=5`, the face is an exceptional bounded chamber in the canonical Section 77 count; `C-INACTIVE-CHAMBER` bounds the sum of the perimeters of all such chambers by `13*pi*D`, so this face has `m<=13*pi*D`. Combining the two proves the displayed bracket and makes `o(D)=o(m)` here.

If `t_eta>=m/2+epsilon D` for fixed `epsilon>0`, then `t_eta-(m-k)>=epsilon D+1` (up to the integer rounding, which only strengthens the bound). The finite inequality yields `|V|>=k+ceil(eta D)(epsilon D+1)`, contradicting `|V|=o(D^2)`. The case `t_eta=m` is ruled out because `m>=2sqrt(pi*a)D` supplies a fixed positive epsilon. This is a boundary-attachment conclusion only; closeness is measured to actual loaded vertices.

## 4. Hostile scope checks and dispositions

- **Physical versus auxiliary faces:** only a bounded face of the actual contact graph with a simple cycle of unit contact edges is covered. A hull chord or outer-pocket edge is not treated as a contact path.
- **Loaded endpoint identity:** `B` is the actual loaded diameter-endpoint set. Arbitrary pins or selected stress endpoints are not substituted.
- **Core versus full source:** only `|V|` is bounded below. Contact-isolated points remain in the source but contribute no path vertices; no isolate rigidity or full-source population theorem follows.
- **Path lengths versus capacity:** the proof uses lengths only to count distinct core vertices. It assigns no lattice sites, independent refill currency, or deletion budget to a path.
- **One face versus many:** only the quota for this one selected face is used. The result does not sum populations across faces or imply simultaneous interior packets.
- **Asymptotic scope:** `eta` and `epsilon` are fixed positive constants. There is no uniform estimate as `eta` tends to zero, and quadratic-core sequences are outside the corollary.
- **No closure inference:** no strict sub-`D` competitor, strict refill, spare site, triangle, C-II closure, or Level I conclusion is proved.

I inspected and reran the registered `C-GLOBAL-FACE-RETURN-QUOTAS` verifier. It passed 153,600 exact integer cancellation ledgers, 10 rational face-family/separator packets, 14 simultaneous face demands, and 3 auxiliary-chord packets. Its own scope says its rational pinned frameworks use arbitrary bar lengths and do not certify unit-separated global minimizers or Level I. It is corroboration for the canonical quota input, not a certificate of the new depth or asymptotic deductions. No new computational verifier is needed; those deductions are analytic.

## 5. Frontier effect

In the subquadratic-core branch, an area-`Omega(D^2)` bounded physical face cannot have a fixed positive excess over half its boundary at any fixed macroscopic distance from actual loaded vertices. Any surviving such face must have at least half its boundary within each fixed macroscopic scale of actual loaded endpoints. This narrows the physical-face subcase of the inactive-container route; outer pockets, exterior caps, quadratic-core sequences, and the capacity/finite-competitor endpoint remain open.

| Claim | Verdict | Disposition |
| --- | --- | --- |
| Finite actual-face depth population bound | PASS | Promote `C-PHYSICAL-FACE-DEPTH-POPULATION` |
| Subquadratic-core macroscopic-face near-loaded-boundary corollary | PASS | Promote `C-SUBQUADRATIC-MACROFACE-NEAR-LOAD-CONTACTS` with `C-INACTIVE-CHAMBER` perimeter dependency explicit |
| Residual-cage/refill or packet-capacity application | NOT ESTABLISHED | Do not promote; Audit.86 supersedes its stated wall-safe packet version |
| C-II or Level I closure | NOT PROVED | Both remain open |
