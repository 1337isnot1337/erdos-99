<!-- theorem-state: {"artifact_id":"ART-118DFF33EB07","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Independent audit — PR #117 phase-integrated sink criterion

**Date:** 2026-10-19  
**Audited source:** PR #117, head `52a89ded959be4c96db4bdc4622ee73f7f63c3bd`  
**Base:** `7d0a450fe66991036541023f95c44c064a04b6a8`  
**State / priority / catalogue:** `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`  
**Assigned scope:** `audit-pr117-phase-integrated-sinks-macbook-20261019`, scope key `39ebb5d0d2595860279d95f9e81b2222e3743442635c6878b9ec8b5db796fa06`.

## Verdict

**CONDITIONAL PASS.** Given the actual Section-165 plateau response, a fixed Section-172 fan, the Section-102 admissible basis and its Section-113 perfect matching, and the Section-174/175 partitions, the lattice-cell average and the integer threshold imply that condition (2) yields a generic phase with

\[
\Xi_\Sigma(v)\ge j_*(v)+|T_Z(v)|.
\]

The published text explicitly requires a measurable basis but does not separately specify the auxiliary matching $\mu_0(v)$ used by the Section-174 basis-closed shield and hence by $C_i,O_i,\Xi_\Sigma$. A bare measurable column-basis selection does not by itself make those sets measurable. This is repaired by selecting $B(v)$ and $\mu_0(v)$ jointly and lexicographically: there are finitely many possible incidences and matchings, each with a Borel fiber. Under that explicit convention the expectations in (1) are defined. If “measurable basis” was intended to include its matching, the repair is only a clarification. The report does not prove condition (2) for any source, let alone every sufficiently large global source. Target A and Level I remain open; no claim lifecycle changes.

Reviewer: OpenAI Codex, GPT-6 Luna xhigh, in an independent reviewer session. The originating PR identifies its author as OpenAI Codex, GPT-6 Luna xhigh. The reviewer did not produce or edit the candidate proof or verifier. This audit adds no external material; its new text is offered under Apache-2.0.

## Exact candidate and exposure

The audited package is `research-packages/e99-pass-20261018-local-01` in PR #117. Its five pinned artifact hashes are:

| File | SHA-256 |
| --- | --- |
| `README.md` | `27d223939702a6e0ce72adcdeedd173201ef4a6ae9e0a98a5a2c64b61a5b5cfb` |
| `SOURCES.json` | `43587af2eb27213634b9debb08e3dd0d2b4887b6903938db78ad02a2c0c1a020` |
| `TASK.json` | `8e604411bfe615702b5855b1c7a87858e77922427886ed621792484a2daa23b2` |
| `VERIFY.json` | `65afec8fd5212d5666e4baa23aef0844a6bae79d5c71f901afca0df8ab25c98b` |
| `verify.py` | `7265f783cf0a5ebcb7c26169b50796ff7af900a39e086fa3d1560959d0a2b920` |

All 16 input hashes in that package's `SOURCES.json` matched their pinned Git blobs or the pinned verifier copy. The package is explicitly classified `unreviewed`; this audit reviews only its phase-integrated implication and selector measurability. I read the published candidate proof before reconstructing it from Sections 102, 165, 174, and 175. The launch overlap snapshot exposed the two Discussion #83 handoff excerpts about the earlier seed-63 and seed-66 checks before I finished that reconstruction; I treated them as scope pointers, then checked the source identities and phase argument directly. I read the PR #117 producer handoff after deriving the pointwise sink/basis algebra, and read the corrected seed-63 audit and the PR #78 Schur audit after completing the reconstruction. I did not author, edit, or supply the candidate proof or verifier. The finite checker is replay evidence, not an analytic proof.

## Statement and hypotheses checked

Let $A\subset H$ be the actual $N$-label triangle-free global source optimum, including any contact-isolated labels. Let $X^*\subset K^*=\operatorname{conv}X^*$ be the actual right-endpoint plateau optimum, with $|X^*|=m^*$ and $t=(D-d)/2>1$. Assume the Section-165 placement $K^*+\mathbb B\subseteq H$. Fix the canonical three-channel unit-contact fan $\Sigma\subset X^*$, independent of lattice translation.

For each generic translate $v\in F$, use a Section-102 basis $B(v)$ of the full interior-row matroid that extends a basis of the restricted deep-column matroid, together with a perfect matching $\mu_0(v):B(v)\to Z(v)$ used by Section 113. Write $Z,O,Y_0,T_\Sigma,T_Z,T_O,C_i,O_i,O_{\rm iso}$ for the Section-175 sets and put

\[
\Xi_\Sigma=|O_{\rm iso}|+\sum_i(|O_i|-|C_i|)_+,
\qquad j_*=N-m^*-|Y_0|,
\]

\[
d_{\rm int}=|C^\circ|,
\qquad t_\Sigma=|C^\partial\cap V(\Sigma)|,
\qquad a_0=\sqrt3/2,
\qquad A_\Sigma=\operatorname{area}N_1(|\Sigma|).
\]

The downstream quantity is the integer residual $R(v)=\Xi_\Sigma(v)-j_*(v)-|T_Z(v)|$, and hence the canonical locked-branch difference $\zeta-s=h(G)-j_*$. The discriminating check is to reconstruct each partition and count identity, establish measurability of the finite selector, and verify that cell integration counts the full unit tube and both collar bands. A counterexample to any identity, a non-Borel selector, or a positive-measure exceptional phase set would stop the implication. Once those checks pass, the investigation stops at the conditional criterion; it does not pivot to deriving (2) from source geometry.

The audited conditional claim is that

\[
\operatorname{area}(K^*+t\mathbb B)+a_0\,\mathbb E_v[d_{\rm int}+t_\Sigma]
>a_0(N-1)+\pi+2|E(\Sigma)|
\tag{2}
\]

implies the displayed locked-branch inequality at some generic phase.

## Proof reconstruction

### Measurable phase data and basis selector

Take a bounded half-open fundamental cell $F$ of area $a_0$, and set $\mathbb E_v f=a_0^{-1}\int_F f(v)\,dv$ on its full-measure generic subset. Since $K^*+t\mathbb B$ is bounded and $v\in F$, only finitely many lattice indices can contribute to $Z,O,Y_0,T_\Sigma$, or to any response edge. Membership of a translated site in $\operatorname{int}K^*$, the annular collars, or the strict unit disk about a fixed point is Borel in $v$. The exceptional equality sets lie on finitely many polygonal or parallel-body boundaries and distance-one circles; they have planar measure zero. Hence the generic phases have full measure.

For a fixed candidate subset of the finite set $X^*$, being a basis of the row matroid is equivalent, by Section 102, to existence of a matching saturating the relevant finite shore. Being a basis of the restricted deep-column matroid is the analogous finite matching-rank predicate after testing that all conflict neighbors lie in $Z(v)$. These are finite unions and intersections of the Borel incidence predicates above. Order all admissible triples $(I^\circ,B,\mu_0)$ lexicographically and select the first; $\mu_0$ ranges over finitely many perfect matchings in the finite support graph. Each selector fiber is the Borel set where that triple is admissible and every earlier triple is not. This defines a Borel Section-102 basis and Section-113 matching on the generic phase set. The counts $d_{\rm int},t_\Sigma,\Xi,j_*,|T_Z|$ are then bounded integer-valued Borel functions, so all expectations used below exist. Values on the measure-zero exceptional set do not affect them. The term $\mathbb E_v[d_{\rm int}+t_\Sigma]$ and condition (2) depend on the selected basis; $\Xi_\Sigma$ additionally uses its selected $\mu_0$. The area-only condition obtained by dropping the nonnegative basis term does not depend on either choice.

### Pointwise sink and basis bookkeeping

The Section-175 disjoint partition is

\[
O=T_O\sqcup O_{\rm iso}\sqcup\bigsqcup_i O_i,
\qquad T_\Sigma=T_Z\sqcup T_O.
\]

For every phase, $(u-c)_+\ge u-c$. Therefore

\[
\Xi_\Sigma\ge |O_{\rm iso}|+\sum_i(|O_i|-|C_i|)
=|O|-|T_O|-\sum_i|C_i|.
\]

The sectors contain precisely the nonfan boundary terminals, so

\[
\sum_i|C_i|=|C^\partial|-t_\Sigma.
\]

For the Section-102 admissible basis, $|B|=|Z|$, $C=X^*\setminus B$, and the deep nonbasis loops are exactly $C^\circ$, with $|C^\circ|=d_{\rm int}$. Thus

\[
|C^\partial|=m^*-|Z|-d_{\rm int}.
\]

This is the point where the restricted-deep-basis extension matters; a depth-only matching does not justify the identity. Subtracting $j_*+|T_Z|$ gives the pointwise bound

\[
\Xi_\Sigma-j_*-|T_Z|
\ge |O|+|Y_0|+|Z|-|T_O|-|T_Z|-N+d_{\rm int}+t_\Sigma.
\tag{3}
\]

The actual source label count enters only as $N=|A|$. No contact isolate is removed, and $X^*$ is not identified with $A$.

### Lattice-cell expectations

For every bounded measurable planar set $U$, translation averaging over a lattice cell gives

\[
\frac1{a_0}\int_F\#((\Lambda+v)\cap U)\,dv
=\frac{\operatorname{area}U}{a_0},
\]

by summing the indicators over lattice translates of $F$. Apply this to the interiors of $K^*$, $K^*+\mathbb B$, and $K^*+t\mathbb B$. The two disjoint collar bands $O$ and $Y_0$ cover the latter outer difference up to boundaries of measure zero. Hence

\[
\mathbb E|Z|=\frac{\operatorname{area}K^*}{a_0},
\qquad
\mathbb E(|O|+|Y_0|)=\frac{\operatorname{area}(K^*+t\mathbb B)-\operatorname{area}K^*}{a_0}.
\]

Every point within distance strictly below one of $|\Sigma|$ lies in $\operatorname{int}(K^*+\mathbb B)$, since $|\Sigma|\subset K^*$. Thus $T_\Sigma$ counts the full lattice intersection with $N_1(|\Sigma|)$, and

\[
\mathbb E(|T_Z|+|T_O|)=A_\Sigma/a_0.
\]

Taking expectations in (3) proves exactly

\[
\mathbb E[\Xi_\Sigma-j_*-|T_Z|]
\ge \frac{\operatorname{area}(K^*+t\mathbb B)-A_\Sigma}{a_0}
-N+\mathbb E[d_{\rm int}+t_\Sigma].
\tag{1}
\]

### Integer threshold and endpoint

Section 175.5 gives $A_\Sigma\le\pi+2e$, where $e=|E(\Sigma)|$, because $\Sigma$ is fixed, connected, and has total edge length $e$. Combining this bound with (1) and (2) yields

\[
a_0\,\mathbb E[\Xi_\Sigma-j_*-|T_Z|]
\ge \operatorname{area}(K^*+t\mathbb B)-A_\Sigma-a_0N
+a_0\mathbb E[d_{\rm int}+t_\Sigma]
>-a_0.
\]

The residual is integer-valued. If it were negative at every generic phase, it would be at most $-1$ almost everywhere and its mean would be at most $-1$, a contradiction. Therefore a generic phase has residual at least zero, which is exactly $\Xi_\Sigma\ge j_*+|T_Z|$. By Section 175.4 this gives $h(G)\ge j_*$; Section 175.6 then gives $\zeta-s=h(G)-j_*\ge0$, the stated locked-branch endpoint. Since $d_{\rm int},t_\Sigma\ge0$, dropping their expectation gives the stated basis-independent, stronger area-only sufficient condition.

## Adversarial scope checks and controls

- **Fixed fan:** the area term and full-tube lattice average use the same \(\Sigma\) at every phase. A fan selected anew from each phase would require a separate measurable-selection and averaging argument; it is not the claim audited here.
- **Exact basis/matching:** all basis-dependent terms use the Section-102 restricted-deep-basis extension, and matching-dependent sector sets use the same measurable Section-113 perfect matching. The verifier excludes the 18 seed-63 relaxed-optimum records that fail Section 102.
- **Partitions:** $O_i$ are pairwise disjoint by Section 174; $O_{\rm iso}$ is the remaining exterior population after removing $T_O$ and all $O_i$. $T_Z,T_O$ partition the tube.
- **Source labels:** every actual source label remains counted in $N$, including contact isolates. The proof uses no source deletion, source-to-scaffold identification, or moved endpoint.
- **Finite controls:** the pinned PR #117 verifier passed 18 admissible seed-63 ledgers and 34 seed-66 cases, excluded 18 inadmissible relaxed controls, and reported minimum pointwise margins 0 and 2. The two predecessor verifiers also exited successfully. These finite fixtures do not encode the area average, global source hypotheses, or condition (2).
- **Predecessors/live overlap:** The corrected `target-a-fan-tube-ledger` audit records why the Section-102 restricted-deep-basis definition must be used; the PR #117 controls preserve that correction. Discussion #83 comments 19004038 and 19004106 request the seed-63 all-$M$ ledger and the seed-66 full-tube/phase audit. PR #121 concerns separate full-shore source-image matching. PR #102 is the abstract source-image Hall formula. None supplies or duplicates this conditional phase-average audit.

## Commands and limits

On the exact pinned source bytes, I verified the five package artifact hashes above and all 16 `SOURCES.json` input hashes. Under the shared compute lock, I ran the byte-identical PR #117 verifier from its immutable pinned copy; the two predecessor checkers ran from this checkout. To reproduce after checking out PR #117 at the pinned head, run these commands from the repository root:

```text
python research-packages/e99-pass-20261018-local-01/verify.py
python research-packages/target-a-fan-tube-ledger/verify.py
python research-packages/target-a-full-tube-fan-ledger/verify.py
```

The PR #117 verifier's finite result is as stated above. No new analytic checker or theorem certificate was run. Required repository-wide theorem-certificate replay is **deferred to the merging agent**. The following claim is not established: for every sufficiently large actual global source, condition (2) holds or some alternative source-specific bound forces the residual nonnegative.

## Remaining lemma

Derive (2), or a stronger lower bound for the actual phase-averaged sector surplus, from global source geometry while retaining $N$ and the actual plateau response. If (2) fails for a particular source, that failure only makes this sufficient criterion inconclusive; it does not refute the desired locked-branch surplus.
