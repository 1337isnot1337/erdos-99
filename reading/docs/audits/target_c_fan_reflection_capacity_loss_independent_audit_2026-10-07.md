> Generated reading edition · [exact source](../../../docs/audits/target_c_fan_reflection_capacity_loss_independent_audit_2026-10-07.md) · source SHA-256 `0bb290c8442e9ae5503b4c5dfc81d7ccbbee135c56d7835ca0406bcd87a127f1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0BA0EC9B17A5","canonical":false,"claim_ids":["C-FAN-REFLECTION-STRICT-CAPACITY-LOSS-REGRESSION"],"claim_statuses":{"C-FAN-REFLECTION-STRICT-CAPACITY-LOSS-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C fan-reflection strict-capacity-loss regression: independent audit

Date: 2026-10-07. Audit base: `149a7a0b410c9860197e220987a324a53093c72b` (`2026-10-07.audit.100`).

Source: PR #722 branch `research/target-c-residual-closure-20261005` at the frozen commit `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. The source report `docs/reports/target_c_fan_octagon_capacity_loss_2026-10-05.md` has SHA-256 `4975a6360ac6b74772eb63da27d21929a7695dd946e3034cb0b16f41ac42be84`; its exact verifier `research/verify_target_c_fan_octagon_capacity_loss_2026_10_05.py` has SHA-256 `25e928e9255bbcec5d7a96f2db4e95df9020f97538d95139ba0840e63f04ae95`.

## Claim under audit

For every real `D>=10`, there is an explicit ten-point, triangle-free, unit-separated source of actual diameter `D` with a simple eight-edge unit wall and an interior contact isolate `z` strictly clear of the old wall. Its degree-two diameter-fan leaf `p` has unique actual diameter partner `b` and two unit wall neighbors. Reflecting `p` across the line through those neighbors preserves the wall edges and does not increase any actual source distance, but it makes `z` collide with the moved wall vertex and changes the wall's strict unit-safe interior from nonempty to empty.

The statement is a finite local geometry regression. It does not assert global optimality, positive KKT stress, or that its eight-cycle contact core satisfies the canonical full-core hypotheses; it does not test unrestricted relocation of `z`.

## Independent reconstruction

Put

```text
e=1/(2D), d=e/2, a=1-e/2,
t=sqrt(1-e^2), h=sqrt(1-a^2),
```

so `0<e<=1/20`. In cyclic order define the wall

```text
p=(0,0),       r+=(-e,t),       T=(-1-d,t+h),
l+=(-2,t),     L=(-2-e,0),       l-=(-2,-t),
B=(-1-d,-t-h), r-=(-e,-t),
```

and add `z=(-1-d,0)` and `b=(-D,0)`.

### Old source and its actual diameter

The side vectors alternate between `(-e,t)` and `(-a,h)` up to signs, so all eight wall edges have length one. The upper chain lies strictly above the horizontal axis except at `p,L`, and the lower chain is its reflection; each chain is simple, so this is a simple polygon. The point `z` is strictly inside: the vertical line through `x=-1-d` meets the two wall chains at `T,B`, with `z` strictly between them.

The old unit-contact graph is exactly the eight-cycle. For nonconsecutive vertices on one chain, horizontal separation is greater than one. For a top vertex from `{r+,T,l+}` and a bottom vertex from `{r-,B,l-}`, vertical separation is at least `2t>1`. Pairs involving `p` or `L` and a nonincident wall vertex have horizontal separation greater than one. These cases exhaust nonconsecutive wall pairs.

The isolate `z` has distances `1+d` to `p,L`, squared distance `a^2+t^2>1` to `r+,r-,l+,l-`, and distance `t+h>1` to `T,B`. For the last inequality, `h^2=e-e^2/4>e^2` when `e<=1/20`, while `1-t=e^2/(1+t)<e^2`; hence `h>1-t`. All wall x-coordinates and `z` lie in `[-2-e,0]`, so `b` is more than one from every wall point and from `z`. Thus the source is unit-separated and triangle-free, and both `z,b` are contact-isolated.

The three diameter pairs are exactly `bp,br+,br-`. Indeed,

```text
|b-p|^2=D^2,
|b-r+|^2=|b-r-|^2=(D-e)^2+t^2=D^2.
```

For `T`, let `u=1+d`; then `1<u<1.025` and `t+h<1+sqrt(1/20)<1.224`, so
`|b-T|^2=(D-u)^2+(t+h)^2 < (D-1)^2+1.5 < D^2` for `D>=10`; the same holds for `B`. The points `l+,l-` are closer to `b` than `r+,r-` because `D-2<D-e`; `L,z` have horizontal separation less than `D`; and `p` is the only other point with horizontal coordinate zero. Finally, all nine noncarrier points lie in a rectangle of width less than `2.05` and height less than `2(1+sqrt(1/20))`, hence have pairwise distances below `4<D`. This proves the full source diameter and that `b` is the unique diameter partner of `p`.

The old wall-safe set contains `z`, since `z` is strictly inside and strictly farther than one from every wall vertex.

### Reflected endpoint and loss of wall capacity

The line `r+r-` is `x=-e`. Reflecting `p` across it gives `p'=(-2e,0)`. The new cyclic wall is simple: its upper chain after `r+` is x-monotone, and the only edge whose x-range overlaps the first edge `p'r+` is `r+T`; that edge has y>t except at `r+`, while `p'r+` has y<t except there. The remaining upper edges are horizontally disjoint from `p'r+`; the lower chain is its reflection. Every wall edge remains unit. The new vertex is also exactly the usual fan point

```text
p'=(1-D^(-2))p + D^(-2)b.
```

For every other source point `q`, convexity of the norm gives
`|p'-q| <= (1-D^(-2))|p-q| + D^(-2)|b-q| <= D`.
The old diameter pairs `br+` and `br-` remain, so the endpoint still has diameter `D`. The two wall contacts at `p'` remain unit. Directly, all other lower constraints also remain at least one except the pair `p'z`: pairs to `l+,l-,L` have horizontal separation greater than one; for `T,B`,

```text
|p'-T|^2=|p'-B|^2=2-2e+e^2+2th>1;
```

and `|p'-b|=D-2e>1`. But

```text
|p'-z|=1-3e/2<1.
```

For the reflected wall itself, split its polygon along the interior chord `p'L`. Its upper cap `(p',r+,T,l+,L)` is convex: its successive turn determinants are `(2-e)t`, `eh+at`, `2ah`, `at-eh`, `(2-e)t`, all positive for `e<=1/20`. Thus the upper half triangulates as `(p',r+,T)`, `(p',T,L)`, `(L,l+,T)` and the lower half is symmetric. The central upper triangle has circumcenter `c=(-1-d-e,h)` and radius one: its vectors from `c` to `p',L,T` have coordinates `(a,-h)`, `(-a,-h)`, `(e,t)`, all of length one. The adjacent upper triangles each have two unit sides. Their included-angle cosines are

```text
c_R=e*a-t*h,       c_L=-e*a-t*h.
```

Since `t*h<=sqrt(e)` and `e*a<=e`, both cosines exceed `-1/2` for `e<=1/20`; hence both circumradii, `1/sqrt(2(1+c_R))` and `1/sqrt(2(1+c_L))`, are strictly less than one. The lower triangles have the same bounds.

Every triangle of circumradius at most one is covered by the three closed unit disks centered at its vertices. If `x=sum(lambda_i v_i)` is in the triangle and `c` is its circumcenter, then

```text
sum(lambda_i |x-v_i|^2)=R^2-|x-c|^2<=1,
```

so at least one vertex is within distance one of `x`. The six triangles cover the reflected polygon. Therefore every interior point is within one of some wall vertex and the reflected strict wall-safe set is empty.

### Scope and compatibility

This is compatible with canonical `C-CENTERED-FAN-REFLECTIONS`: the diameter upper constraints and old wall contacts behave as its fan map predicts, while the full-source lower constraint at the isolate fails. The octagon's empty endpoint wall-safe set also shows that old strict wall-safe capacity is not transported by upper nonexpansiveness or by positive old clearance, even when `D` is arbitrarily large. The wall has eight sides, so the at-most-six-edge zero-capacity theorem does not decide the old wall.

The explicit ten-point source is not globally optimal: a ten-point subset of a `3x4` unit square grid has diameter at most `sqrt(13)<D`. No KKT stress or canonical full-core hypothesis is asserted. The example does not prevent relocating `z` outside this wall or using a collective move whose endpoint is checked against the full source.

## Exact verifier

The frozen verifier was inspected and rerun. It represents squared distances in `Q(sqrt((1-e^2)(1-a^2)))` and uses rational sign comparisons, not floating tolerances. It checks all 45 old and all 45 reflected source pairs, the exact contact and diameter sets, the sole lower collision, the central circumcircle identities, and the adjacent-triangle radius bounds for `D=10,20,100,1000,10000`. I additionally reran the same exact checker at rational `D=1001/100, 201/20, 201/2, 1000001/100000`; all passed. These finite certificates do not prove the real-parameter family. The universal claims above follow from the analytic inequalities in this audit.

The verifier does not establish global optimality, KKT equilibrium, canonical full-core hypotheses, arbitrary relocation feasibility, or a C-II/Level I consequence.

## Verdict

**REGRESSION VALID — promote** `C-FAN-REFLECTION-STRICT-CAPACITY-LOSS-REGRESSION`. Record it as a guardrail against transporting old strict wall capacity through the fan reflection using only upper nonexpansiveness or old clearance. Do not use it to reject the canonical fan theorem or to infer failure of C-II.
