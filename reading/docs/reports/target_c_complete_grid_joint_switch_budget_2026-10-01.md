> Generated reading edition · [exact source](../../../docs/reports/target_c_complete_grid_joint_switch_budget_2026-10-01.md) · source SHA-256 `5cbd8215e8c2ea39113fbe5603d1793b0924a6ddfaac57510b7f16c0900bed35`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-674A62F728E0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- joint two-shore switching budget

Date: 2026-10-01
Base main: 91be6776e6748b0f449ccfff69bca1e352d1b75d
Status: proof-only; C-II remains open.

Let A={tau_1,...,tau_m} and B={sigma_1,...,sigma_n} be the two pairwise-noncrossing shores of a complete global outer-to-outer train rectangle, ordered along their complement-dual paths. For an actual diameter edge h, let t_A(h) and t_B(h) be the numbers of adjacent selected positions where its signed cut incidence changes.

The new joint bound is

$$
\boxed{t_A(h)+t_B(h)\le 2.}
\tag{1}
$$

Therefore, if N_i^A and N_j^B count switching diameter rows at adjacent selected interfaces,

$$
\boxed{\sum_i N_i^A+\sum_j N_j^B\le 2h.}
\tag{2}
$$

Proof. Complete mutual crossing puts the train terminals on four disjoint outer-boundary host intervals Q_A^-,Q_B^-,Q_A^+,Q_B^+ in cyclic order. A boundary vertex p changes shore membership at most once along the ordered A cuts, and only if p lies on an A host interval. Write this change count c_A(p) in {0,1}; define c_B(p) similarly. The four host intervals are disjoint, so c_A(p)+c_B(p)<=1.

Every endpoint of an actual diameter is an extreme hull vertex. For h=xy, a change of its signed A-incidence requires a change in at least one endpoint-membership sequence, so t_A(h)<=c_A(x)+c_A(y), and similarly for B. Adding gives (1). Double counting gives (2).

If h switches on both shores, then (1) forces t_A(h)=t_B(h)=1. One endpoint lies on an A host interval and the other on a B host interval. Thus a shared-switch row has one of four corner types:
Q_A^-Q_B^-, Q_B^-Q_A^+, Q_A^+Q_B^+, Q_B^+Q_A^-.

Opposite corner types cannot coexist. Chords in opposite corners have endpoints in four grouped cyclic intervals, so they do not cross and cannot share an endpoint, contradicting the straight-line diameter-thrackle property. Hence all shared-switch rows occupy at most two adjacent corners and therefore have one endpoint on one common grid side Q.

The shared-switch graph is bipartite between Q and its neighboring host side(s), hence a forest because a straight-line thrackle has no even cycle. Every component is a caterpillar by the standard thrackle argument. If both adjacent corner types occur, the chord-crossing criterion orders their Q-endpoints as a prefix and suffix with at most one common transition hub.

For the current fixed-star rectangle,

$$
|A|,|B|\ge(c_*-o(1))D,\qquad c_*=\frac{\kappa^4}{16\pi^3C_KM_K}.
$$

Current main gives s_A>=ceil(|A|/2)-1 and s_B>=ceil(|B|/2)-1, so

$$
s_A+s_B\ge(c_*-o(1))D.
\tag{3}
$$

At the rooted endpoint h=pi D+o(D), (2) gives

$$
\sum_i N_i^A+\sum_j N_j^B\le(2pi+o(1))D.
\tag{4}
$$

Set H_*=ceil(4pi/c_*)+1. Fewer than (c_*/2+o(1))D active interfaces can have more than H_* switching rows. Hence at least

$$
\boxed{(c_*/2-o(1))D}
$$

interfaces across the two shores have between 1 and H_* switching rows, and one shore contains at least

$$
\boxed{(c_*/4-o(1))D}
$$

such bounded cusps.

This halves the bounded-cusp switching threshold obtained from separate shore budgets and localizes every diameter row reused by both shore-switching systems to one ordered common-side caterpillar.

Remaining target: combine this shared-switch localization with the one/two-bar adjacent-strip reaction and the complete transverse train order. The split-star and inactive-interface branches remain open.

No computation, verifier, numerical experiment, or CI output is used.
