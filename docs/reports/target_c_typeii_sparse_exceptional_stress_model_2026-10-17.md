<!-- theorem-state: {"artifact_id":"ART-9CC91762B85D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Exact sparse-exceptional stress model for the Type-II route

**Status:** unreviewed exact regression; not a canonical theorem premise.

**Source:** `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`  
**State:** `2026-10-15.publication.2`  
**Priority/catalogue:** `public-frontier.3` / `public-frontier.7`  
**Task:** [`target-c-typeii-stress-mass-access`](../../tasks/target-c-typeii-stress-mass-access.md)

## Result

An unweighted exceptional-edge count does not control normalized positive diameter-stress mass from unit separation, triangle-freeness, near-circular hull, leading hexagonal packing density, and exact KKT force balance alone. For every integer $R\ge16$, this report constructs a rational configuration of diameter $D=2R$ with:

- $2\lfloor\sqrt R\rfloor=o(D)$ actual diameter edges, all exceptional because their positive-contact components contain no two-dimensional grid;
- a nonnegative KKT stress normalized by $\sum_{e\in H}\lambda_e=1$, with all its diameter mass on one of those exceptional edges;
- a triangle-free unit-contact graph and population $|X_R|=(2\pi/\sqrt3)R^2+o(R^2)$; and
- a source hull whose area is $\pi R^2-o(R^2)$.

Thus the best upper bound on exceptional stress mass from those data alone is $1$, however small the exceptional count is. This is an isolated stationary model. **It is not proved to be a global minimizer or to lie in the canonical contact-minimal/diameter-pair-minimal normal form.** It therefore does not contradict Audit.173 or the theorem state. It identifies which part of a stress-mass estimate must use additional global-minimizer hypotheses.

## Exact construction

Fix an integer $R\ge16$, set $D=2R$, and let
\[
p_R=\min\{p\in\mathbb Z_{>0}:3p^2>R^2\},\qquad
 a_R=\frac{R^2-p_R^2}{R^2+p_R^2},\qquad
 b_R=\frac{2Rp_R}{R^2+p_R^2}.
\]
Put $u=(1,0)$ and $v=(a_R,b_R)$. The identity $a_R^2+b_R^2=1$ gives $|u|=|v|=1$. Also $R/\sqrt3<p_R<R$, so $0<a_R<1/2$ and $b_R>\sqrt3/2$; as $R\to\infty$, $p_R/R\to1/\sqrt3$ and $v\to(1/2,\sqrt3/2)$. All coordinates are rational.

Take the inner lattice part and central contact chain
\[
L_R=\{mu+nv:m,n\in\mathbb Z,\ |mu+nv|\le R-2,\ |n|\ge2\},
\qquad
P_R=\{ju:j=-R,-R+1,\ldots,R\}.
\]
For the boundary set let $s=\lfloor\sqrt R\rfloor$ and, for $j=0,\ldots,s$, put $t_j=j/s$ and
\[
q_j=R\left(\frac{1-t_j^2}{1+t_j^2},\frac{2t_j}{1+t_j^2}\right).
\]
Let $C_R$ contain these points and their rotations by $90^\circ$, $180^\circ$, and $270^\circ$, including each duplicate cardinal point only once. The ring has exactly $4s$ distinct rational points and includes $Ru$ and $-Ru$. Define $X_R=L_R\cup P_R\cup C_R$.

Every point lies in the closed radius-$R$ disk, while $Ru,-Ru\in X_R$. Hence $\operatorname{diam}(X_R)=2R=D$.

## Separation and triangle-freeness

For a lattice difference $mu+nv$, if $n=0$, its length is the integer $|m|$. If $|n|\ge2$, its vertical component has magnitude $|n|b_R\ge2b_R>1$. If $|n|=1$, the only integer horizontal offset giving length $1$ is $m=0$, which gives $\pm v$: the nearest competitor $m=-1$ has squared length $2-2a_R>1$, and every other integer offset is farther away. Thus the only unit lattice differences are $\pm u,\pm v$. The lattice contact graph is a subgraph of the square grid on integer coordinates $(m,n)$, hence triangle-free.

The chain has unit contacts exactly between consecutive points. Its distance from $L_R$ is at least $|n|b_R\ge2b_R>1$. Every point in $L_R$ has radius at most $R-2$, so its distance from $C_R$ is at least $2$.

The boundary angles in one quadrant are $\theta_j=2\arctan(j/s)$. Since $1\le (d/dt)(2\arctan t)\le2$ for $0\le t\le1$, consecutive ring angles differ by a value in $[1/s,2/s]$; rotations give the same bounds around the circle. Distinct ring points are separated by chord length at least
\[
2R\sin\frac{1}{2s}\ge\frac{2R}{\pi s}>1,
\]
where the last inequality holds for $R\ge16$, since $s\le\sqrt R$ and $\pi<4$. Every non-axis ring point is at angular distance at least $1/s$ from the central line, so its distance from the whole chain is at least $R\sin(1/s)\ge2R/(\pi s)>1$. The two axis ring points on that line are the chain endpoints themselves. These checks exhaust all pairs between the construction pieces. The contact graph is a disjoint union of square-grid subgraphs, a path, and isolated vertices, so it is triangle-free.

## Diameter edges and exceptional set

All points outside $C_R$ lie strictly inside the radius-$R$ disk. A pair has distance $2R$ only if both points lie on the circle and are antipodal. Since the ring is antipodally symmetric, the actual diameter graph consists exactly of its $4s/2=2s$ antipodal pairs.

Every endpoint of these pairs is either an isolated ring point or one of the two endpoints of the central path $P_R$. Neither contact component contains a two-dimensional source-contact grid. Hence every actual diameter edge is exceptional for same-component grid access, and
\[
|H_{\rm exc}|=2s\le2\sqrt R=o(2R)=o(D).
\]
For each fixed $\eta>0$, eventually $|H_{\rm exc}|\le\eta D$.

## Exact KKT stress

Use all point coordinates and a diameter variable $d$. For each distinct pair write lower constraints $g_{xy}=1-|x-y|\le0$ and upper constraints $h_{xy}=|x-y|-d\le0$. Give the upper constraint for the central antipodal pair $(-Ru,Ru)$ multiplier $\lambda=1$ and all other upper constraints multiplier zero. Give each of the $2R=D$ consecutive chain contacts multiplier $\mu=1$ and every other lower constraint multiplier zero. All multipliers are nonnegative, and $\sum_H\lambda=1$, the stationarity equation for $d$.

For a chain edge ordered from $ju$ to $(j+1)u$, the gradient of $1-|x-y|$ contributes $+u$ at its left endpoint and $-u$ at its right endpoint. These cancel at every interior chain point. At $-Ru$, its one chain contribution $+u$ cancels the active diameter gradient $-u$; at $Ru$, the chain contribution $-u$ cancels the diameter gradient $+u$. Every other point has zero force. Complementarity holds because every constraint with nonzero multiplier is active. This is an exact nonnegative KKT certificate, and its entire normalized positive diameter mass lies on the exceptional edge $(-Ru,Ru)$.

This proves stationarity only; it makes no second-order or global-minimality assertion.

## Near-disk population and hull

The lattice fundamental parallelogram has area $b_R$, diameter at most $2$, and $b_R\to\sqrt3/2$. Tiling by these cells bounds the number of lattice points in the radius-$(R-2)$ disk between the areas of the radius-$(R-4)$ and radius-$R$ disks, divided by $b_R$. The count is therefore $\pi R^2/b_R+O(R)$. Removing rows $n=-1,0,1$, adding the central chain, and adding the ring changes it by only $O(R)$. Consequently
\[
|X_R|=\frac{\pi R^2}{b_R}+O(R)
      =\frac{2\pi}{\sqrt3}R^2+o(R^2),
\]
the leading hexagonal-packing density for centers in a radius-$R$ disk.

The ring's largest angular gap is at most $2/s$. In every direction some ring point is within angle $1/s$, so $\operatorname{conv}(C_R)$ contains the radius-$(R\cos(1/s))$ disk. The full source hull lies inside the radius-$R$ disk and contains that smaller disk; its area deficit is at most $\pi R^2\sin^2(1/s)=O(R)=o(R^2)$. Thus the hull is asymptotically round.

## Verification

Run from the repository root:

```sh
python research/verify_target_c_typeii_sparse_exceptional_stress_2026_10_17.py
```

The checker uses only Python's standard library and exact rational arithmetic. For $R=16,25,36,64,100,256$, it verifies the rational basis and ring, pairwise ring separation, antipodal diameter-edge count, contact-chain force ledger, multiplier normalization, and exceptional-count ratio. It also prints the exact finite source and lattice-core populations. The all-$R$ separation, asymptotic count, hull, and stress claims are proved above; the finite replay does not establish global minimality.

## Relation to the canonical route and exact remaining gap

[Audit.173](../audits/target_c_uniform_harmonic_cells_global_diameter_access_independent_audit_2026-10-08.md)'s canonical result gives an unweighted $\eta D$ bound on actual diameter edges lacking same-component access to a Type-II grid, and explicitly does not bound their positive KKT mass. This model shows that nonnegativity, normalization, exact force balance, triangle-freeness, leading density, and roundness do not close that gap by themselves. A stress-weighted inequality such as
\[
\sum_{e\in H_{\rm exc}}\lambda_e=o(1)
\]
would require additional global-minimality information, or another argument converting concentrated load into a finite source-preserving endpoint.

The exact remaining C-II obligation is a canonical full-source same-cardinality move preserving every lower and actual-diameter upper pair constraint, including contact isolates, and yielding either a triangle-free endpoint at $D$ with lexicographically fewer contacts/diameter pairs or a strict sub-$D$ competitor. This report proves no such move and changes no canonical lifecycle. The macroscopic-container branch also remains open.

**AI role:** originated the construction and proof, then implemented and ran the exact finite checker. **Review:** no independent AI-agent audit has been performed; the result remains unreviewed.
