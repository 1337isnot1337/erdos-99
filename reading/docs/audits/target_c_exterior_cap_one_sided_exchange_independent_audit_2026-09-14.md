> Generated reading edition · [exact source](../../../docs/audits/target_c_exterior_cap_one_sided_exchange_independent_audit_2026-09-14.md) · source SHA-256 `b17c5512b4b1bd1ab472b19bd943966d566207c1d7cc0b196a914df5175d5665`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E5C4C7D99B5F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit — one-sided protected exchange for exterior caps

**Date:** 2026-09-14
**Target:** Target C-II macroscopic-container branch
**Audited artifact:** docs/reports/target_c_exterior_cap_one_sided_exchange_2026-09-14.md
**Verdict:** PASS for the explicitly conditional finite exchange theorem; no C-II or Level I closure.

## Audited theorem

Let $A$ be a contact-minimal triangle-free global minimizer with
$\operatorname{diam}(A)=D$, $K=\operatorname{conv}(A)$, and let
$$
C=K\cap\{x:u\cdot x\ge c\}
$$
be an actual exterior cap whose closing chord is
$K\cap\{u\cdot x=c\}$. Let $Z$ be the cap sources off the closing chord and
assume:

1. every point of $Z$ is contact-isolated;
2. every retained source $a\in A\setminus Z$ satisfies $u\cdot a\le c$;
3. $\operatorname{diam}(C)\le D$; and
4. $C$ has nonempty interior and $A\setminus Z$ contains a nonisolated
   source; and
5. with $a_0=\sqrt3/2$ and
   $$
   \sigma=\frac{\operatorname{area}(C)}{a_0}
          +\frac{\operatorname{per}(C)}2+1-|Z|,
   $$
   the slack exceeds
   $$
   \frac{\operatorname{area}(C)}{a_0}\left(1-\frac1{\lambda^2}\right)
   +\frac{D}{a_0\lambda}+\frac{\operatorname{per}(C)}2+2
   \tag{A.1}
   $$
   for some $\lambda>1$.

If $A\setminus Z$ contains a nonisolated source, these assumptions are
inconsistent.

The theorem is finite, preserves the original source cardinality, and uses global
optimality only after constructing a same-cardinality source inside $K$. It is
not a theorem for internal chambers, where retained sources may lie on both sides
of the chamber boundary.

## Proof audit

Set
$$
U_\lambda=\operatorname{int}(C)\cap\{x:u\cdot x>c+\lambda\}.
$$
For $0<t<\lambda$, the section of $C$ by
$u\cdot x=c+t$ is a segment of length at most $\operatorname{diam}(C)\le D$.
Fubini therefore gives
$$
\operatorname{area}(U_\lambda)\ge
\operatorname{area}(C)-\lambda D.
\tag{A.2}
$$

For a triangular lattice of nearest-neighbor spacing $\lambda$, translation
averaging over one fundamental cell gives a translate containing at least
$$
\left\lfloor
\frac{\operatorname{area}(C)-\lambda D}{a_0\lambda^2}
\right\rfloor
\tag{A.3}
$$
lattice points in $U_\lambda$. A generic translation avoids the finite old source
set and the boundary of $K$, without changing the averaged count. Any two new
points are at distance at least $\lambda>1$. If $a\in A\setminus Z$ and
$y\in U_\lambda$, then
$$
|y-a|\ge u\cdot(y-a)>\lambda>1.
\tag{A.4}
$$
Thus the new points have no unit contacts with one another or with retained old
sources.

Writing $z=|Z|$, the definition of $\sigma$ gives
$$
z=\frac{\operatorname{area}(C)}{a_0}
  +\frac{\operatorname{per}(C)}2+1-\sigma.
\tag{A.5}
$$
Subtracting (A.5) from the unfloored quantity in (A.3) yields
$$
\sigma-\frac{\operatorname{area}(C)}{a_0}\left(1-\frac1{\lambda^2}\right)
-\frac{D}{a_0\lambda}-\frac{\operatorname{per}(C)}2-1.
$$
Under (A.1) this is $>1$, so the floor in (A.3) supplies at least $z+1$
new points. Delete $Z$ and one nonisolated retained source $v$, and insert
any $z+1$ of those points. The resulting set has exactly $|A|$ points,
is unit-separated by (A.4), and lies in $K$; hence its diameter is at most
$D$. Global minimum-diameter optimality forces equality, while deletion of
$v$ removes at least one contact and insertion creates none. This contradicts
contact minimality.

All inequality directions and the integer-floor margin are therefore correct.
The proof does not assume a simple cap boundary, does not delete retained
contact-isolated points, and does not use a KKT or affine-kernel extension.

The audited report also records the sharper finite form obtained by writing
$$
b_\lambda(C,u)=\int_0^\lambda
\mathcal H^1(C\cap\{x:u\cdot x=c+t\})\,dt.
$$
The protected lattice count then loses exactly
$b_\lambda(C,u)/(a_0\lambda^2)$, and the uniform $D/(a_0\lambda)$ term follows
from $b_\lambda(C,u)\le\lambda\operatorname{diam}(C)\le\lambda D$.
This refinement changes no source-cardinality or contact-count step.

The report also evaluates this refined threshold on the strained parallelogram
regression: with a side-parallel closing chord,
$b_{\lambda_D}=\lambda_D(m+1)$, while
$\sigma=2(m+1)+1$. Hence the refined threshold remains larger by a
linear term. This calculation is exact at the displayed symbolic level and confirms
that the profile refinement does not accidentally eliminate the hostile saturated-cap
model.

## Scope limitations

The audit does not establish the cap hypotheses from the general macroscopic
container dichotomy. In particular, the canonical branch supplies only a
linear-order slack estimate; it does not prove that the slack violates (A.1).
The strip loss $D/(a_0\lambda)$ is valid uniformly but is still linear in $D$.
No internal-chamber exchange follows from this one-sided argument.

Consequently the exact remaining implication is:
$$
\text{canonical exterior cap}
\quad\Longrightarrow\quad
\text{either (A.1) fails or a new low-slack/source-core argument is needed}.
$$
The low-slack cap, internal chamber, and full-core $\mu_D\ge1$ branches remain
unresolved.

## Promotion decision

This is an audited-working finite conditional theorem, not a canonical dependency.
No theorem-state manifest, route map, or prompt file is changed by this audit.
