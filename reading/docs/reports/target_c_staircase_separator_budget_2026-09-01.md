> Generated reading edition · [exact source](../../../docs/reports/target_c_staircase_separator_budget_2026-09-01.md) · source SHA-256 `05d4031ac218261c4ddb0373a1882944c0676c7f4f1a08ba3bde3831052a8464`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C8CE34F24E00","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C88: staircase separator budget

**Date:** 2026-09-01  
**Repository base:** `0db5a90a` (main after C87 / PR #92)  
**Status:** LEVEL I STILL OPEN

C87 collapses the canonical pure-rhombic chain face to a connected antitone prefix
tree with exactly `D` simple intervals, each represented by active diameter pairs in
both hull-arc orientations. C88 extracts the exact equality structure of that tree and
then uses the train-coordinate representation to force a quadratic number of
separations by trains outside the `D`-track chain atom.

## 1. Equality structure of the C87 edge count

Let the distinct left endpoints of the C87 simple intervals be

`a_1<...<a_s`.

For row `i` put

`B_i={b:(a_i,b) in E(G_P)}`,

`m_i=min B_i`, `M_i=max B_i`.

The C87 proof used

`|E(G_P)| <= sum_i(M_i-m_i+1) <= M_1-m_s+s <= D`.

C86 connectivity and C87 give equality `|E(G_P)|=D`. Hence equality holds at every
step. Therefore:

1. `a_i=i-1` for `1<=i<=s`;
2. `M_1=D` and `m_s=s`;
3. `m_i=M_(i+1)` for `1<=i<s`;
4. every row is complete: `B_i={m_i,m_i+1,...,M_i}`.

Put

`t_0=D`, `t_i=m_i` for `1<=i<=s`.

Then `t_s=s`, `t_0>=t_1>=...>=t_s`, and the entire tree is

`E(G_P)={(i-1,b): t_i<=b<=t_(i-1), 1<=i<=s}`.

This is the exact staircase normal form; adjacent rows meet in the sink `t_i`.

## 2. Total chain-interval length is shape-independent

For a simple prefix edge `e=(a,b)` define its chain length

`ell_e=b-a`.

### Theorem C88.1

Every C87 staircase tree satisfies

`sum_(e in E(G_P)) ell_e = D(D+1)/2`.

### Proof

Using the staircase form,

`sum_e a_e
 = sum_(i=1)^s (i-1)(t_(i-1)-t_i+1)
 = sum_(j=1)^(s-1) t_j - s(s-1)/2`.

Also

`sum_e b_e
 = sum_(i=1)^s sum_(b=t_i)^(t_(i-1)) b
 = D(D+1)/2 - s(s-1)/2 + sum_(j=1)^(s-1)t_j`.

Subtracting gives the claim. `square`

Equivalently,

`sum_e (D-ell_e)=D(D-1)/2`.

Thus no choice of staircase shape can make all prefix intervals nearly full length.
The aggregate missing chain span is fixed exactly.

## 3. Every diameter needs at least D separating trains

For an oriented source pair `h`, C80 train coordinates give

`r_h=sum_tau d_(h,tau) u_tau`,

where each nonzero `d_(h,tau)` equals `+1` or `-1`, and every `u_tau` is a unit
vector. Let

`k_h=sum_tau d_(h,tau)^2`

be the number of train tracks separating the endpoints of `h`.

If `h` is a diameter pair, `|r_h|=D`. Triangle inequality gives

`D <= k_h`.

For a C83 interval over the chain atom, exactly `ell_h=|I_h|` of those separating
trains lie in `P`. Therefore the number of separating trains outside the chain atom is
at least

`k_h-ell_h >= D-ell_h`.

No graph-distance theorem is needed; this follows directly from the exact train-vector
sum.

## 4. Quadratic non-chain separation budget

C87 supplies at least two actual active diameter pairs over every simple tree edge,
one in each arc orientation. Select one of each orientation for each simple edge.
Applying the preceding inequality and C88.1 gives

`sum_(selected h) # {tau notin P : tau separates h}`

`>= 2 sum_e(D-ell_e)`

`= D(D-1)`.

Hence:

### Theorem C88 — staircase separator budget

The canonical pure-rhombic C80-C87 chain-face survivor contains at least

`D(D-1)`

incidences between selected non-chain active diameter pairs and train tracks outside
`P` that separate their endpoints.

Additional active diameter pairs can only increase this incidence count.

This is an exact finite bound.

## 5. One non-chain train is macroscopically loaded

Let `T` be the total number of train tracks. There are `D` chain tracks, so averaging
C88 gives a non-chain train separated by at least

`D(D-1)/(T-D)`

of the selected active diameter pairs.

In the asymptotic pure-rhombic global-minimizer regime, Target B pinned rigidity gives

`q/T >= 1/2-o(1)`,

while convex perimeter gives

`q <= pi D+o(D)`.

Therefore

`T <= 2 pi D+o(D)`,

and some non-chain train separates at least

`(1/(2pi-1)+o(1))D
 = (0.189279...+o(1))D`

selected active diameter pairs.

### Corollary C88.2 — macroscopic secondary train cut

Every asymptotic canonical pure-rhombic chain-face survivor has a non-chain train whose
two sides are joined by `Omega(D)` active source diameter pairs; the explicit lower
coefficient above is valid from the currently promoted shell bounds.

## 6. Frontier effect

C87 forced one common chain train crossed by every nonempty prefix interval. C88 adds
a transverse statement: the paired staircase cannot be supported by the chain atom
alone. It necessarily spends a fixed quadratic total of separation incidences on the
other train directions, and one non-chain train carries a linear number of diameter
pairs.

The next target is a capacity theorem for such a macroscopically loaded non-chain
train. The diameter pairs it separates form a bipartite geometric-thrackle subgraph
across the train cut; because every diameter cycle is odd, that subgraph is a forest.
Combining its ordered caterpillar structure with the C87 paired staircase is the most
direct route to a contradiction.
