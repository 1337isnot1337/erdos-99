> Generated reading edition · [exact source](../../../docs/audits/target_c_strict_turn_path_non_surrounding_independent_audit_2026-10-08.md) · source SHA-256 `e3003de1f625deb56794eeef486168f96ee81cb4f1ee5ddd56c02808c88700f2`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-808EC70A335F","canonical":true,"claim_ids":["C-STRICT-TURN-PATH-CONTACT-NON-SURROUNDING"],"claim_statuses":{"C-STRICT-TURN-PATH-CONTACT-NON-SURROUNDING":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C independent audit: strict-turn convex path contacts do not surround

**Date:** 2026-10-08
**Audit base:** 3b343135e7f051065a274f7a9f51b4b195cc193c, state 2026-10-08.audit.144.
**Target:** C-II; C-II and Level I remain open.
**Frozen source:** research/sol/target-c-exterior-cap-closure-20261006 at f4a362727779f6afc0f01738015112c04fdb73d5. At refresh it was 9 commits ahead of main and 151 behind.
**Source report:** docs/reports/target_c_exterior_loaded_tips_and_paired_packet_gluing_2026-10-06.md, SHA-256 01e106faa927a78b540a785b1a4d7b5d726a210182c47b1e6d0101710088124f.
**Frozen verifier:** research/verify_target_c_exterior_loaded_tip_pairing_2026_10_06.py, SHA-256 2201886a3452f54f6a18c8930dde07798312788ae3239abb0d90af577c692953.
**Saved certificate:** research/target_c_exterior_loaded_tip_pairing_certificate_2026_10_06.json, SHA-256 e3daa623a24699b7a4146134e42b29eb7d246a61843000655a9aad7770f78cd9.

## Verdict and exact scope

**PASS — promote C-STRICT-TURN-PATH-CONTACT-NON-SURROUNDING.** This is a local geometric theorem about one site and one convex unit-edge path. It does not assert that a site or packet exists in a canonical source.

Let $`A\subset\mathbb R^2`$ be finite and unit-separated. Let $`Q`$ be a convex polygon and $`P=(v_0,\ldots,v_m)`$ a proper boundary chain of $`Q`$, with $`|v_{i+1}-v_i|=1`$ for each side. The path vertices belong to $`A`$. Let $`T(P)`$ be the total turn of its edge directions, and assume $`T(P)<\pi`$. Let $`R\subseteq\{v_0,\ldots,v_m\}`$ contain every internal vertex of $`P`$, with either or both endpoints optionally omitted. Suppose $`x\in\operatorname{int}Q`$ and $`|x-v|\ge1`$ for every $`v\in R`$. Write $`N=\{v\in R:|x-v|=1\}`$. Assume no path edge has both endpoints in $N. Then

```math
0\notin\operatorname{int}\operatorname{conv}\{v-x:v\in N\}.
```

This is the maximal local no-triangle hypothesis needed by the proof: triangles elsewhere among path vertices are irrelevant. Omitted endpoint guards are immaterial because the proof uses only guarded internal vertices. The theorem refers only to contacts between $x$ and the path; other source points may still pin $x$.

## Independent reconstruction

Assume for contradiction that the unit-contact vectors strictly surround $x$. There are at least three of them. Because $x$ is inside the convex polygon $Q$, the polar directions from $x$ to successive vertices of $P$ follow the path order: for every oriented path side, $Q$ lies to its left, so the cross product of its endpoint vectors from $x$ is positive. Choose three consecutive path contacts $a,b,c$, with lifted polar angles

```math
\alpha<\beta<\gamma,\qquad
\delta_1=\beta-\alpha\in(0,\pi),\quad
\delta_2=\gamma-\beta\in(0,\pi).
```

Strict surrounding makes each cyclic gap between consecutive contact vectors less than $\pi$, so these two gaps are less than $\pi$ as well.

Let $p$ be the path vertex immediately after $a$. If $p=b$, then $a,p$ are consecutive path vertices both in $N$, contrary to the hypothesis. Thus $p\ne b$. Since $p$ lies between $a$ and $c$, it is internal and guarded. Let $\eta$ be the direction of the unit edge $ap$, and set $x=0$, $a=e_\alpha$, $b=e_\beta$, where $e_\theta=(\cos\theta,\sin\theta)$.

The guard at $p$ and the fact that $x$ lies on the interior side of $ap$ give

```math
0<\eta-\alpha\le \frac{2\pi}{3}.
```

Old source separation $|p-b|\ge1$ gives

```math
(b-a)\cdot e_\eta\le\frac{|b-a|^2}{2},
\quad\text{hence}\quad
\sin\!\left(\eta-\frac{\alpha+\beta}{2}\right)
\le
\sin\!\left(\frac{\delta_1}{2}\right).
```

If $\eta>\beta$, then $\eta-(\alpha+\beta)/2$ lies strictly between $\delta_1/2$ and $2\pi/3-\delta_1/2<\pi-\delta_1/2$. The sine is strictly greater than $\sin(\delta_1/2)$ throughout that interval, a contradiction. Therefore $\eta\le\beta$.

Now let $q$ be the path vertex immediately before $c$. The same no-adjacent-contact hypothesis gives $q\ne b$, so $q$ is internal and guarded. Let $\zeta$ be the direction of the unit edge $qc$. The interior-side orientation gives $\zeta-\gamma\in(0,\pi)$. Applying $|q-b|\ge1$ to $q=c-e_\zeta$ yields

```math
\sin\!\left(\zeta-\frac{\beta+\gamma}{2}\right)
\le
\sin\!\left(\frac{\delta_2}{2}\right).
```

The angle on the left is greater than $\delta_2/2$. If it is at least $\pi$, it is already at least $\pi-\delta_2/2$. If it is below $\pi$, the same strict sine comparison forces it to be at least $\pi-\delta_2/2$. Hence $\zeta\ge\beta+\pi$.

Convexity makes the path edge directions monotone, so the total turn between $ap$ and $qc$ is at least

```math
\zeta-\eta\ge\pi.
```

This contradicts $T(P)<\pi$. The origin is therefore not interior to the convex hull of the path-contact vectors.

By canonical C-ONE-SITE-CONTACT-SURROUND, if $x$ is also strictly inside the old source hull and every nonpath lower distance and every inserted-involving upper distance has strict margin, this geometric conclusion gives a sufficiently small finite motion that opens all the path contacts. Those extra full-source margins are hypotheses of that corollary; this audit does not infer them from the path.

## Hostile checks and certificate boundary

- The proof needs every internal vertex weakly guarded. If an internal $p$ or $q$ is unguarded, the $2\pi/3$ directional bound is unavailable. No such weakened scope is promoted.
- The proof uses convexity, $x\in\operatorname{int}Q$, and the path order of polar directions. It does not apply to a nonconvex wall, an arbitrary chord, or contacts to vertices outside $P.
- The frozen exact-rational verifier was run from the frozen source bytes. Its JSON output matched the saved certificate byte-for-byte. It checked 3,942 old/endpoint pair distances across a right-angle tip example, the exact half-turn example, and the shared-tip collision. This verifies those finite examples only; it does not encode the analytic strict-turn theorem.
- The exact half-turn path has total turn $`\pi`$, is unit-separated, and after adding $`x=0`$ has no triangle containing $`x`$ and a path edge. Its three unit-contact vectors strictly surround $`x`$. Positive weights $`25/14,25/14,1`$ on those contacts sum to zero. This is the existing C-EXTERIOR-WALL-HALF-TURN-PIN-REGRESSION and shows that $`T(P)<\pi`$ cannot be weakened to $`T(P)\le\pi`$.
- The theorem does not control additional source contacts, provide strict margins to contact isolates, produce a refill packet, or imply a source-preserving sub-$`D`$ competitor.

## Dependencies and frontier disposition

The promoted geometric claim has no theorem dependency. Its conditional motion consequence uses C-ONE-SITE-CONTACT-SURROUND under that theorem's exact full-source margin hypotheses. The complementary equality-case regression was already canonical and is not duplicated.

The cap-extraction theorem C-ANTIPODAL-EXTERIOR-CAP-PAIRING was independently promoted in Audit.115; the paired-cell shield and contact-budget results were promoted in Audit.85. This audit does not reopen or extend them. C-II remains open, and the active global source-capacity obligation is unchanged.
