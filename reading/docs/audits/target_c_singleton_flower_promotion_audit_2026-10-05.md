> Generated reading edition · [exact source](../../../docs/audits/target_c_singleton_flower_promotion_audit_2026-10-05.md) · source SHA-256 `442a4f7008e8729f3e3d69b186b44c940a237383bbabb06f5150a4dac5810ef2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CF624260C6F4","canonical":true,"claim_ids":["C-BOUNDED-FACE-ENDPOINT-FAN","C-FULL-FLOWER-K-PAYMENT","C-FULL-FLOWER-PROJECTIVE-BLOCKER","C-GOOD-HULL-SINGLETON-CHARGE"],"claim_statuses":{"C-BOUNDED-FACE-ENDPOINT-FAN":"canonical","C-FULL-FLOWER-K-PAYMENT":"canonical","C-FULL-FLOWER-PROJECTIVE-BLOCKER":"canonical","C-GOOD-HULL-SINGLETON-CHARGE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent promotion audit — Target C bounded-face fans, flower blockers, and good-hull singleton charge

**Date:** 2026-10-05  
**Audit base:** \`6fb1ea2ec195bf1ec4bbc3e44dc2c768fd1934cc\`  
**Starting theorem state:** \`2026-10-05.audit.54\`  
**Target:** C-II / full-core train-defect frontier  
**Verdict:** **PASS for the four exact claims registered below.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit promotes:

1. \`C-BOUNDED-FACE-ENDPOINT-FAN\`;
2. \`C-FULL-FLOWER-PROJECTIVE-BLOCKER\`;
3. \`C-GOOD-HULL-SINGLETON-CHARGE\`;
4. \`C-FULL-FLOWER-K-PAYMENT\`.

The first two claims reconstruct older proof-only structural material under the current canonical core convention. The latter two are October full-core consequences of the canonical hull-depletion stack.

## 1. Bounded-face train endpoint fans are crossing-free

Audited sources:

- \`research/target_c_bounded_face_endpoint_fan_2026-09-12.md\`;
- \`research/target_c_bounded_face_endpoint_fan_hostile_audit_2026-09-12.md\`.

Let $F$ be one bounded physical nonquadrilateral contact face and let $\tau_1,\tau_2$ be distinct complete stopped trains having terminal occurrences on $F$.

The promoted statement is

$$
\boxed{\tau_1\text{ and }\tau_2\text{ cannot cross in a strict rhombus}.}
$$

The proof is finite and uses only current canonical ingredients.

### 1.1 Prefix Jordan cut

Assume the trains cross. Take the train-midpoint prefixes from their terminal edge midpoints on $F$ to their first mutual crossing $x$. Join their terminal midpoints by an arc in the open interior of $F$. The two prefixes and this face arc form a simple Jordan curve $\Gamma$.

The curve lies inside the full source hull $K$. Let $S$ be the nonisolated positive-contact-core vertices in $\operatorname{Int}\Gamma$. A terminal contact edge is crossed, so $S\neq\varnothing$.

Every active diameter endpoint is an extreme point of $K$, hence lies outside $\operatorname{Int}\Gamma$. Therefore summing KKT equilibrium over $S$ produces no diameter term.

The only contact edges crossing the shore are those crossed by the two selected train prefixes. For each prefix the physical contact edges share one projective direction $u_i$ and one coherent outside-to-inside orientation. Positive contact coefficients therefore give

$$
\epsilon_1A_1u_1+\epsilon_2A_2u_2=0,
\qquad
A_1,A_2>0.
$$

If the two projective directions are different, this is impossible in the plane.

If they are the same projective direction $u$, define the core velocity
$$
w(v)=
\begin{cases}
Ju,&v\in S,\\
0,&v\notin S.
\end{cases}
$$
All same-shore contact rows vanish. Every cut contact is parallel to $u$, so its first variation is $u\cdot Ju=0$. Every active diameter endpoint lies outside $S$, so all active diameter rows also vanish.

Thus $w$ is a mixed infinitesimal flex of the canonical nonisolated core. It is nonzero on $S$, while the two endpoints of any active diameter edge are distinct fixed core vertices outside $S$. Hence $w$ is not Euclidean, contradicting canonical \`C-ZRF\`.

This reproof does not use the older parallel-pair-cut candidate.

Singleton trains are isolated vertices of the strict-rhombus crossing graph, so the crossing-free statement is automatic when either train is singleton.

### 1.2 Endpoint pair simplicity

Audit.53 already canonically proves that the bounded-endpoint internal train graph is simple through \`C-RECIPROCAL-TRAIN-GRAPH\`. Thus no two distinct complete trains join the same unordered pair of bounded augmented endpoints.

The promoted fan claim therefore records the combined current-state finite fact:

- trains incident with one bounded physical exceptional face form an independent set in the strict-rhombus crossing graph;
- bounded endpoint pairs are simple.

No statement is made for repeated outer-face occurrences.

**Verdict:** canonical-ready.

## 2. Fully rhombic pentagons are exact projective two-blockers

Audited sources:

- \`research/target_c_full_flower_projective_blocker_2026-09-15.md\`;
- \`research/target_c_full_flower_projective_blocker_hostile_audit_2026-09-15.md\`.

Let $F$ be a bounded physical pentagonal contact face whose five boundary edges each have a strict rhombus on the opposite side. Its five boundary contacts therefore belong to five non-singleton stopped trains
$$
I(F)=\{\tau_1,\ldots,\tau_5\}.
$$

Canonical augmented-train loop exclusion makes these five trains distinct, and \`C-BOUNDED-FACE-ENDPOINT-FAN\` makes them pairwise noncrossing.

### 2.1 Pentagon direction lemma

Orient the unit side vectors counterclockwise:
$$
e_1,\ldots,e_5,\qquad
|e_i|=1,\qquad
\sum_i e_i=0.
$$

By canonical contact-face regularity the physical pentagon is strictly convex. Let $g_i\in(0,\pi)$ be its exterior turn at the next vertex. The skipped-vertex diagonal has length
$$
|e_i+e_{i+1}|=2\cos(g_i/2).
$$
It is a noncontact source pair, hence has length $>1$. Therefore
$$
\boxed{0<g_i<2\pi/3.}
$$

Now suppose four projective side directions lie in one projective arc $A$ of width $w\le\pi/3$. Rotate so the lifted arcs $A_+,A_-$ are antipodal around the horizontal axis. Every selected side has axial projection magnitude at least
$$
c=\cos(w/2)\ge\sqrt3/2.
$$

A $4+0$ lift split cannot close because $4c-1>0$. A $3+1$ split cannot close because
$$
3c-2\ge3\sqrt3/2-2>0.
$$
If all five projective directions lie in $A$, the same majority argument applies.

In the remaining $2+2$ split, the two complementary gaps between $A_+$ and $A_-$ have angular length at least
$$
\pi-w\ge2\pi/3.
$$
The fifth side occupies at most one of the two gaps. The other gap is empty, so two consecutive oriented side directions differ by at least $2\pi/3$, contradicting the strict turn bound.

Hence
$$
\boxed{\text{no projective arc of length }\pi/3\text{ contains four side directions of }F.}
$$

### 2.2 Two blockers per external train

A strict-rhombus crossing between train directions $\phi,\psi$ requires
$$
d_{\rm proj}(\phi,\psi)>\pi/3.
$$
For fixed $\phi$, the compatible projective directions form one open arc of length $\pi/3$. The direction lemma therefore says that any external train $\sigma\notin I(F)$ can cross at most three of the five flower trains.

Thus
$$
\boxed{\text{every external train is nonadjacent to at least two members of }I(F).}
$$

Since the five flower trains are pairwise noncrossing,
$$
\boxed{
\sum_{\tau\in I(F)}d_R(\tau)\le3(T_R-5).
}
$$

### 2.3 Global missing-pair consequence

Let $M$ be the number of fully rhombic physical pentagons.

Fix any strict-rhombus train $\sigma$. It can terminate on at most two full flowers. Each of the remaining at least $M-2$ flowers supplies two blocker terminal occurrences belonging to trains nonadjacent to $\sigma$.

A complete stopped train has exactly two terminal occurrences, so it can serve as a blocker for at most two different flowers. Hence
$$
\bar d_R(\sigma)\ge M-2.
$$

Summing nondegrees gives
$$
\boxed{
{T_R\choose2}-R_4
\ge
\frac{T_R(M-2)}2.
}
$$

Equivalently,
$$
\boxed{
R_4\le\frac{T_R(T_R-M+1)}2.
}
$$

This is an exact finite localization theorem; it does not claim that direction compatibility itself guarantees crossing.

**Verdict:** canonical-ready.

## 3. Good-hull singleton trains have a finite face/outer charge

Audited source:
\`docs/reports/target_c_good_hull_singleton_face_charge_2026-10-05.md\`.

Work in the canonical full-core Type-II loaded-chord branch. Let

- $G_D$ be the canonical family of complete trains with at least one good unit loaded-hull end;
- $S_G$ be the singleton trains in $G_D$;
- $x_B=b-q$;
- $m_B$ be the number of nonunit loaded-hull sides;
- $P_5$ be the number of bounded physical pentagonal contact faces;
- $X=Q-f=\sum_{\deg F\ge6}(\deg F-5)$.

The promoted finite theorem is
$$
\boxed{
S_G\le x_B+m_B+2P_5+4X+3.
}
$$

### 3.1 Good-hull singleton bridges

Canonical hull-side occurrence counting gives exact bad outer terminal capacity
$$
B_{\rm bad}=x_B+m_B.
$$

If a good-hull singleton contact edge is a bridge, its second terminal occurrence is also on the outer face. The good distinguished occurrence for that physical hull side is unique. The second bridge occurrence therefore belongs to a bad outer interval.

Distinct singleton trains have distinct terminal occurrences, so
$$
S_G^{\rm br}\le x_B+m_B.
$$

### 3.2 Nonbridge singletons charge exceptional faces

A nonbridge good-hull singleton has one exterior occurrence and one occurrence on a bounded exceptional physical face $F$.

Let $r(F)$ be the number of boundary edges of $F$ that are actual unit loaded-hull sides. In the full-core Type-II branch,
$$
r(F)\le\deg F-2.
$$

Indeed, if all but one side were loaded-hull sides, the remaining edge would join loaded vertices and be a unit contact; canonical loaded-chord localization would make it another hull side. If every side were a loaded-hull side, the face would be the whole loaded contact shell and no quadratic strict-rhombus bulk could remain.

For $d=\deg F\ge6$,
$$
d-2\le4(d-5),
$$
hence
$$
\sum_{\deg F\ge6}r(F)\le4X.
$$

### 3.3 Pentagon sharpening

For a pentagon, $r(F)\le3$.

If $r(F)=3$, the three loaded-hull sides must form one consecutive three-edge chain. Otherwise there are at least two hull-side chains. Every gap between chains connects loaded endpoints. A one-edge gap would be a loaded-loaded unit contact and therefore another hull side; hence every gap uses at least two non-hull edges. Two gaps would require at least four non-hull edges, impossible in a pentagon with three hull sides.

Let $e_1,e_2,e_3$ be the consecutive oriented hull-side vectors, and let $\Theta$ be the total exterior hull turn across their two internal vertices. The remaining two unit edges close the same endpoints, so
$$
|e_1+e_2+e_3|\le2.
$$

If $\Theta\le\pi$, projection onto the bisector of the first and third directions gives
$$
|e_1+e_2+e_3|
\ge3\cos(\Theta/2).
$$
Therefore
$$
\Theta\ge2\arccos(2/3)>\pi/2.
$$
If $\Theta>\pi$, the same lower bound is automatic.

Distinct $r(F)=3$ pentagons use disjoint internal hull-turn terms. Since total convex-hull turn is $2\pi$, at most three such pentagons occur. Consequently
$$
\sum_{\deg F=5}r(F)\le2P_5+3.
$$

Adding the bridge and face charges proves the finite singleton bound.

### 3.4 Eliminate singleton escape from the hull-depletion frontier

Let $S_0$ be singleton trains remaining after deleting $G_D$. They are isolated vertices of the remaining strict-rhombus crossing graph, so Mantel gives
$$
M_D-S_0\ge2\sqrt{R_{\rm bulk}}.
$$

Use the canonical exact good-hull ledger
$$
5m_B+4S+2\sigma_R+5d_D
=
2b-8\sqrt{R_4}+5M_D+5k+2X.
$$

With $S=S_G+S_0$, the singleton charge, $m_B\le x_B$, and
$$
x_B=(P_F-q)+(b-P_F)=E_F+G_F,
$$
one obtains the exact inequality
$$
\boxed{
13E_F+11G_F+8P_5+14X+2\sigma_R+5d_D+12
\ge
2P_F-8\sqrt{R_4}+10\sqrt{R_{\rm bulk}}+S_0+5k.
}
$$

Canonical full-core asymptotics then give
$$
\boxed{
13E_F+11G_F+8P_5+14X+2\sigma_R
\ge
[2(\pi+s)-o(1)]D+S_0+5k,
}
\qquad
s=\sqrt{\frac{\pi}{2\sqrt3}}.
$$

Since the five displayed coefficients sum to $48$,
$$
\boxed{
\max\{E_F,G_F,P_5,X,\sigma_R\}
\ge
\left(\frac{\pi+s}{24}-o(1)\right)D
+\frac{S_0+5k}{48}.
}
$$

Numerically $(\pi+s)/24\approx0.1706$.

If
$$
E_F,G_F,X,\sigma_R=o(D),
$$
then
$$
\boxed{
P_5
\ge
\frac{\pi+s}{4}D
+\frac{S_0+5k}{8}
-o(D).
}
$$

Thus good-hull singleton trains cannot hide the higher-surplus branch.

**Verdict:** canonical-ready.

## 4. Full-flower blockers force diameter-topology currency into train defects

Audited source:
\`docs/reports/target_c_full_flower_blocker_k_payment_2026-10-05.md\`.

Put
$$
r_4=\sqrt{R_4},
\qquad
r_b=\sqrt{R_{\rm bulk}},
\qquad
\delta_G=r_4-r_b\ge0,
$$
$$
\eta_D=M_D-2r_b\ge0,
\qquad
\sigma_R=2T_R-4r_4\ge0.
$$

Let $F$ be the number of fully rhombic physical pentagons and $S_G$ the good-hull singleton count.

### 4.1 Lower bound for full flowers

The exact remaining-train ledger is
$$
M_D=m_B-k+2f+d_D.
$$

Since every nonpentagonal exceptional face contributes at least one unit to $X=Q-f$,
$$
f-P_5\le X.
$$
Substituting $M_D=2r_b+\eta_D$ gives
$$
P_5
\ge
r_b+\frac{\eta_D}{2}
-\frac{m_B}{2}
+\frac{k}{2}
-\frac{d_D}{2}
-X.
$$

Every non-full pentagon has at least one boundary side whose train is singleton. A singleton contact edge borders at most two pentagons, so
$$
P_5-F\le2S.
$$

Write $S=S_G+S_0$. Since $S_0$ is isolated in the depleted crossing graph,
$$
S_0\le M_D-2\sqrt{R_{\rm bulk}}=\eta_D.
$$
Therefore
$$
\boxed{
F
\ge
r_b-\frac32\eta_D-\frac12m_B+\frac12k
-\frac12d_D-X-2S_G.
}
$$

### 4.2 Blocker upper bound

Canonical \`C-FULL-FLOWER-PROJECTIVE-BLOCKER\` gives
$$
{T_R\choose2}-R_4
\ge
\frac{T_R(F-2)}2,
$$
hence
$$
F\le T_R+1-\frac{2R_4}{T_R}.
$$

Let
$$
a=T_R-2r_4=\frac{\sigma_R}{2}.
$$
Exact algebra gives
$$
F
\le
r_4+1+
a\,\frac{3r_4+a}{2r_4+a}.
$$

Comparing the lower and upper bounds and multiplying by two yields
$$
\boxed{
k\le
2\delta_G+2+
\Psi(\sigma_R,r_4)
+3\eta_D+m_B+d_D+2X+4S_G,
}
$$
where
$$
\boxed{
\Psi(\sigma,r)
=
\sigma\frac{3r+\sigma/2}{2r+\sigma/2}.
}
$$

For $r>0,\sigma\ge0$,
$$
\sigma\le\Psi(\sigma,r)\le\frac32\sigma.
$$
Thus
$$
\boxed{
k
\le
2\delta_G+2+\frac32\sigma_R
+3\eta_D+m_B+d_D+2X+4S_G.
}
$$

Canonical hull depletion gives
$$
R_4-R_{\rm bulk}=o(D^2),
\qquad
R_4,R_{\rm bulk}=(\Delta_2-o(1))D^2,
$$
so
$$
\delta_G
=
\frac{R_4-R_{\rm bulk}}{\sqrt{R_4}+\sqrt{R_{\rm bulk}}}
=o(D).
$$

Therefore every full-core Type-II sequence satisfies
$$
\boxed{
\frac{k}{D}
\le
\frac32\frac{\sigma_R}{D}
+3\frac{\eta_D}{D}
+\frac{m_B}{D}
+2\frac{X}{D}
+4\frac{S_G}{D}
+o(1).
}
$$

In particular,
$$
\sigma_R,\eta_D,m_B,X,S_G=o(D)
\quad\Longrightarrow\quad
k=o(D).
$$

If $\liminf k/D\ge\kappa>0$, the coefficient sum $23/2$ gives
$$
\boxed{
\liminf
\frac{\max\{\sigma_R,\eta_D,m_B,X,S_G\}}{D}
\ge
\frac{2\kappa}{23}.
}
$$

This removes the escape in which a linear diameter-topology currency $k=d_H+s_Z$ is hidden solely inside a large full-flower population.

**Verdict:** canonical-ready.

## 5. Independent finite-ledger certificate

The new certificate
\`research/verify_target_c_audit55_singleton_flower_ledger_2026_10_05.py\`
was run independently during this audit. It passed:

- 4,676,599 exact good-hull singleton/depletion ledger packets;
- 846,411 exact full-flower $k$-payment packets and both $\Psi$ bounds;
- 44,940 exact blocker missing-pair rearrangement packets;
- the balanced coefficient identities.

The script checks algebra and cancellation only. The endpoint-fan, pentagon-turn, projective-blocker, and hull-turn arguments are analytic proofs above.

## 6. Effect on the canonical frontier

Audit.54 already gives an actual strict-source-competitor endpoint through certified wall-safe packing surplus, and a wall-disjoint pentagon train bulk in the low-endpoint-defect branch.

Audit.55 adds a complementary defect theorem.

Every full-core survivor must pay linearly in
$$
E_F=P_F-q,\quad
G_F=b-P_F,\quad
P_5,\quad
X=Q-f,\quad
\sigma_R,
$$
with the explicit balanced floor
$$
\max\{E_F,G_F,P_5,X,\sigma_R\}
\ge
\left(\frac{\pi+s}{24}-o(1)\right)D.
$$

If the metric/higher-degree/train-slack currencies are all sublinear, then the source contains more than $(\pi+s)D/4-o(D)$ physical pentagons.

Separately, a linear $k=d_H+s_Z$ cannot be hidden in full flowers: it must reappear linearly in at least one of
$$
\sigma_R,\quad
\eta_D,\quad
m_B,\quad
Q-f,\quad
S_G.
$$

These are not yet contradictions. Their value is to force the higher-surplus branch into physical train/face currencies that can be combined with the audit.53 loaded-return machinery and audit.54 wall-refill endpoint.

The next high-value theorem is to turn one of the now-forced linear pentagon/singleton/train-slack populations into either:

- a certified collective wall-safe packing surplus paying an actual diameter cover;
- an additional second-depletion family;
- or an exact unit equilateral triangle.

**Promotion recommendation:** advance theorem state to \`2026-10-05.audit.55\` and register all four claims as canonical.
