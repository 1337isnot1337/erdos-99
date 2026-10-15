<!-- theorem-state: {"artifact_id":"ART-0F5AB1E395D8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — hull depletion plus post-endpoint defect synthesis

**Date:** 2026-10-04
**Base:** current main `596445ac32ffd45e2cbb8df9dbeba15be3465cf5` plus the independently audited proof-only PR #667 hull-depletion theorem preserved on this branch
**Classification:** proof-only synthesis; no theorem-state promotion
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The independently audited PR #667 theorem raises the full-core Type-II surplus floor
to
\[
\mu_{\rm hull}
=\frac{\pi+\sqrt{\pi/(2\sqrt3)}}2
=2.046952730226875\ldots
\]
and excludes convergence to that endpoint. Its strongest use is not the scalar floor
alone. Combining its finite remaining-train ledger with the stopped-train
decomposition gives a sharper weighted physical-defect inequality.

Put
\[
\Delta_2=\frac{\pi}{2\sqrt3},
\qquad
s=\sqrt{\Delta_2}.
\]
Use the canonical full-core notation:

- \(m_B\): number of nonunit sides of the actual loaded force hull;
- \(S\): number of singleton stopped trains;
- \(R_4\): number of strict unit-rhombus faces;
- \(T\): all stopped trains;
- \(T_R=T-S\): non-singleton/rhombic trains;
- \(\sigma_R:=2T_R-4\sqrt{R_4}\);
- \(k=d_H+s_Z\);
- \(Q-f=\sum_{\deg F\ge6}(\deg F-5)\);
- \(b\): occurrence-counted outer contact walk;
- \(P_F=\operatorname{per}(F)\);
- \(d_D\le2\): trains with two good unit-hull ends in the PR #667 count; and
- \(M_D\): actual trains remaining after deleting every train having a good
  unit-hull end.

The main new consequence is
\[
\boxed{
5m_B+4S+2\sigma_R
\ge
2(\pi+s)D
+5k+2(Q-f)+2(b-P_F)-o(D).
}
\tag{S.1}
\]

Numerically,
\[
2(\pi+s)=8.1878109209075\ldots.
\tag{S.2}
\]

Thus the old \(Q-f\) and \(b-P_F\) currencies are not independent escape branches
in this composition: making either one large increases the required physical burden
in \(m_B,S,\sigma_R\).

This report also proves a free singleton second-depletion refinement, an exact
feasibility bootstrap, the resulting closure of the old terminal low-\(t\) branch,
and a conditional loaded-hull near-unit matching theorem. It records the precise
extra theorem needed to iterate the depletion argument through exceptional-face
train ends.

---

## 1. Exact finite synthesis

The audited #667 source identity is
\[
4\mu_DD+8c_I+18-2b-M_D-k-3m_B
=2(Q-f)+2-d_D.
\tag{S.3}
\]
The canonical full-core loaded-chord/pinned identity is
\[
\mu_DD=q+m_B-k-2c_I-4.
\tag{S.4}
\]
The exact all-train count is
\[
T=q-k+2f.
\tag{S.5}
\]
The exact good-hull-end count gives
\[
|G_D|=q-m_B-d_D,
\qquad
M_D=T-|G_D|.
\tag{S.6}
\]
Finally define
\[
\tau_D:=T-2\sqrt{R_4}.
\tag{S.7}
\]

Substitution and cancellation give the finite identity
\[
\boxed{
5m_B+4\tau_D+5d_D
=
2b-8\sqrt{R_4}+5M_D+5k+2(Q-f).
}
\tag{S.8}
\]

The singleton/rhombic-train split is exact:
\[
2\tau_D=2S+\sigma_R.
\tag{S.9}
\]
Therefore (S.8) is equivalently
\[
\boxed{
5m_B+4S+2\sigma_R+5d_D
=
2b-8\sqrt{R_4}+5M_D+5k+2(Q-f).
}
\tag{S.10}
\]

This identity is finite bookkeeping after the #667 good-hull classification. It does
not use the September post-endpoint asymptotic identity as a premise.

---

## 2. The weighted full-core frontier

The audited #667 depletion theorem proves
\[
R_G=o(D^2),
\]
where \(R_G\) counts rhombi incident with a good-hull train. Thus the \(M_D\)
remaining trains carry
\[
R_{\rm bulk}=R_4-R_G=(\Delta_2-o(1))D^2.
\]
Their crossing graph is simple and triangle-free, so Mantel gives
\[
M_D\ge(2s-o(1))D.
\tag{S.11}
\]

Type-II near-disk asymptotics give
\[
\frac{P_F}{D}\to\pi,
\qquad
\frac{\sqrt{R_4}}{D}\to s,
\qquad
b=P_F+(b-P_F).
\]
Insert these facts into (S.10), use \(d_D=O(1)\), and obtain (S.1).

### 2.1 Immediate three-way branch

Discarding the nonnegative bonus currencies in (S.1), every survivor must satisfy
\[
5\frac{m_B}{D}+4\frac{S}{D}+2\frac{\sigma_R}{D}
\ge8.1878109209075\ldots-o(1).
\tag{S.12}
\]
Consequently at least one of
\[
\boxed{
m_B\ge(0.545854061393833\ldots-o(1))D,
}
\tag{S.13}
\]
\[
\boxed{
S\ge(0.682317576742292\ldots-o(1))D,
}
\tag{S.14}
\]
or
\[
\boxed{
\sigma_R\ge(1.36463515348458\ldots-o(1))D
}
\tag{S.15}
\]
holds.

These are balanced-pigeonhole thresholds, not individually sharp branch constants.

### 2.2 Closure-budget formulation

Suppose future source-level theorems exclude
\[
m_B\ge aD,\qquad S\ge bD,\qquad \sigma_R\ge cD
\]
for every full-core survivor, with strict asymptotic upper thresholds satisfying
\[
\boxed{5a+4b+2c<2(\pi+s).}
\tag{S.16}
\]
Then (S.1) is impossible and the full-core Type-II branch closes.

For orientation,
\[
5(0.50)+4(0.65)+2(1.50)=8.10
<8.1878109209075\ldots.
\]
This is not a claim that those three upper bounds are currently proved. It quantifies
how much branch elimination would suffice.

---

## 3. Free second depletion of leftover singleton trains

A singleton stopped train is a train consisting of one contact edge incident with no
strict-rhombus face. It is therefore an isolated vertex of the strict-rhombus train
crossing graph.

Let \(S_0\) be the number of singleton trains among the \(M_D\) trains remaining
after the #667 good-hull deletion. Removing these \(S_0\) vertices deletes zero
rhombi. Hence the \(M_D-S_0\) remaining train vertices still carry
\(R_{\rm bulk}\) edges. Mantel gives
\[
\boxed{
M_D-S_0\ge2\sqrt{R_{\rm bulk}}
=(2s-o(1))D.
}
\tag{S.17}
\]
Substitute this into (S.10):
\[
\boxed{
5m_B+4S+2\sigma_R
\ge
2(\pi+s)D
+5S_0
+5k+2(Q-f)+2(b-P_F)-o(D).
}
\tag{S.18}
\]

Thus singleton trains do not provide a free escape from the new frontier.

- Singleton trains outside the good-hull family are charged again with coefficient
  five on the right side.
- Therefore any large singleton branch avoiding this stronger contradiction must
  concentrate a correspondingly large fraction of its singleton trains in the
  good-hull family.

A good-hull singleton is an actual unit loaded-hull side whose opposite train
incidence is not a strict rhombus. That leaves a concrete boundary structure for the
next attack: a large population of unit loaded-hull sides terminating immediately
into an exceptional-face or outer-bridge occurrence rather than entering the rhombic
bulk.

No contradiction from that boundary population is claimed here.

---

## 4. General second-depletion template

The singleton argument is an instance of a more general statement.

Let \(\mathcal H_D\subseteq M_D\) be any train subfamily such that the number of
strict rhombi incident with at least one train of \(\mathcal H_D\) is \(o(D^2)\).
After deleting \(\mathcal H_D\), the remaining train graph still has
\((\Delta_2-o(1))D^2\) edges. Therefore
\[
M_D\ge|\mathcal H_D|+(2s-o(1))D.
\tag{S.19}
\]
Equation (S.10) then yields
\[
\boxed{
5m_B+4S+2\sigma_R
\ge
2(\pi+s)D
+5|\mathcal H_D|
+5k+2(Q-f)+2(b-P_F)-o(D).
}
\tag{S.20}
\]

This is the correct mathematical formulation of a second depletion theorem.

### 4.1 Why exceptional-face train ends are not yet an unconditional application

It is tempting to take \(\mathcal H_D\) to be every train ending on a bounded
exceptional face. The #667 hull argument cannot simply be copied.

Unit hull sides lie on one convex outer boundary, so a narrow phase window has
\(O(\varepsilon D)\) such sides uniformly in the window position. Exceptional-face
edges have no analogous single global convex-boundary order. A linear exceptional
face population can support linearly many train ends concentrated in a few phases.
Existing pentagon/full-flower reports explicitly leave large phase-concentrated
rhombic train systems as live structural branches.

Therefore
\[
\text{exceptional-face end}
\Longrightarrow
o(D^2)\text{ incident rhombi}
\]
is not proved and is not asserted here.

The exact next theorem for this route is one of:

1. a source-level directional-dispersion theorem showing that a selected
   exceptional-terminal family occupies \(o(D)\) trains per fixed narrow phase bin;
2. a Groemer/KKT theorem converting phase concentration of bounded-degree
   exceptional faces into many near-active source constraints that can be spent; or
3. a high-degree-tail theorem coupling concentrated exceptional ends to loaded
   returns/rigidity strongly enough to eliminate that branch.

Any of these would let (S.20) iterate the #667 mechanism rather than merely improve a
scalar constant.

---

## 5. Exact remaining-train / feasibility identity

**Parallel-prior-art note.** Open PR #663,
`docs/reports/target_c_all_unit_hull_end_currency_2026-10-04.md` at
`70e2f6a95adcc5bac1ade91da9ea26ffdfe78cfd`, contains the exact identity

[
5t_DD+x_B+m_B+d_D=3b+2(Q-f)+N_0.
]

Using (x_B=m_B+u_B) and (b=q+x_B) turns that formula into (S.22) below,
with (N_0=M_D). PR #663 also proves the same asymptotic lower bound
(N_0/Dge2s-o(1)). Thus (S.22)--(S.26) have parallel prior art in #663;
this report does not claim priority for the numerical terminal threshold or its
underlying exact occurrence identity. The present value is an independent derivation
from the audited #667 stack and its integration with (S.1), singleton second
depletion, Groemer, and the #668/#671 fork. The September
`target_c_clean_endpoint_fullcore_boost_2026-09-09.md` already contains the same
constant under the stronger low-outer-walk hypothesis (x_B=o(D)).

The finite ledgers admit an even cleaner rewrite. Put
\[
u_B:=x_B-m_B\ge0.
\tag{S.21}
\]
Starting from the exact #667 identity and using
\(b=q+x_B=q+m_B+u_B\), one obtains
\[
\boxed{
5t_DD
=
3q+M_D+m_B+2u_B+2(Q-f)-d_D.
}
\tag{S.22}
\]
Since \(q=t_DD+k\), this is equivalently
\[
\boxed{
2t_DD
=
M_D+3k+m_B+2u_B+2(Q-f)-d_D.
}
\tag{S.23}
\]

Both identities are finite. The companion verifier checks them on all 102,496
enumerated ledger packets.

Insert the audited #667 depletion floor
\[
M_D\ge(2s-o(1))D.
\]
Then every full-core survivor satisfies
\[
\boxed{
t_D
\ge
s+\frac{3k+m_B+2u_B+2(Q-f)}{2D}
-o(1).
}
\tag{S.24}
\]

This is the useful bootstrap form: a defect that raises \(k,m_B,u_B\), or \(Q-f\)
raises the actual feasibility variable \(t_D=(q-k)/D\), rather than merely raising
the surplus \(\mu_D\).

---

## 6. Terminal loaded-hull branch closes below 2.26588

Now assume a terminal sequence in the standard sense
\[
\frac{\pi D-q}{D}\to0,
\qquad\text{equivalently}\qquad
\frac qD\to\pi.
\tag{S.25}
\]
Divide (S.22) by \(D\), use
\[
\frac{M_D}{D}\ge2s-o(1),
\qquad
m_B,u_B,Q-f\ge0,
\qquad
d_D=O(1),
\]
and obtain
\[
\boxed{
\liminf t_D
\ge
t_{\rm term}
:=
\frac{3\pi+2s}{5}
=
2.265880714899459\ldots.
}
\tag{S.26}
\]

This is a genuine proof-only branch elimination:
\[
\boxed{
q/D\to\pi
\quad\Longrightarrow\quad
\text{no survivor with }\limsup t_D<t_{\rm term}.
}
\tag{S.27}
\]

In particular, the old terminal-FREE near-floor regime around
\[
t_D=1.959852849540479\ldots
\]
cannot occur if the audited #667 theorem is admitted. Nor can a terminal-FREE
subcase whose hypotheses impose \(t_D\le2.02+o(1)\). Its conditional finite lemmas
may remain correct, but the combined asymptotic antecedent is empty in this
proof-only stack.

### 6.1 Why the earlier large-\(m_B\) calculation is only an intermediate bootstrap

Using only \(b\ge P_F\) in the exact \(m_B\) rewrite gives the weaker necessary
inequality
\[
\frac{m_B}{D}
\ge
3\pi+2s-5T-o(1)
\tag{S.28}
\]
on a terminal subsequence with \(\limsup t_D\le T\). At the old terminal floor this
would read
\[
m_B>(1.53013932679489\ldots-o(1))D.
\tag{S.29}
\]

But (S.29) must be fed back through the exact identity
\(b=q+m_B+u_B\). Doing so yields (S.26), so the apparent large-\(m_B\) survivor
does not exist. The correct conclusion is terminal low-\(t\) exclusion, not a live
large-\(m_B\) branch.

---

## 7. Loaded near-unit matching remains a valid conditional tool

Although the old near-\(1.96\) terminal regime is now empty, a linear \(m_B\)
population can still be useful in another scope that independently forces it.

Under the terminal perimeter condition \(q/D\to\pi\), Type-II near-disk geometry also
gives
\[
\frac{P_F-q}{D}\to0.
\tag{S.30}
\]
For the nonunit loaded-hull side lengths \(\ell_e>1\),
\[
\boxed{
P_F-q=\sum_{e\ {\rm nonunit}}(\ell_e-1).
}
\tag{S.31}
\]

If in some surviving subbranch
\[
m_B\ge(c-o(1))D
\tag{S.32}
\]
for fixed \(c>0\), then a diagonal choice \(\eta_D\downarrow0\) leaves
\((c-o(1))D\) nonunit hull sides of length in
\[
(1,1+\eta_D).
\]
Any \(r\)-edge subset of a cycle has a matching of size at least
\(\lfloor r/2\rfloor\). Hence there are
\[
\boxed{
\left(\frac c2-o(1)\right)D
}
\tag{S.33}
\]
pairwise vertex-disjoint actual source pairs \(\{u_i,v_i\}\) with
\[
u_i,v_i\in B,
\qquad
1<|u_i-v_i|\le1+\eta_D.
\tag{S.34}
\]
Both endpoints are actual loaded diameter endpoints, while the pair itself is a
strict noncontact.

This theorem remains useful if another high-surplus or nonterminal argument forces
(S.32). It is no longer advertised as the continuation of the obsolete terminal
near-\(1.96\) branch.

### 7.1 Regression: this is not PR #664 currency

PR #664 studies inactive source pairs at near-diameter scale
\[
|xy|\ge D-\frac cD.
\]
The pairs in (S.34) instead have near-unit scale
\[
|uv|=1+o(1).
\]
They are lower-constraint candidates, not upper-constraint diameter witnesses.

Therefore the tempting direct implication
\[
m_B\text{ linear}
\Longrightarrow
\text{the missing linear PR-\#664 near-diameter packet}
\]
is false as a statement of scale and is rejected.

The valid future target, if a live branch again forces (S.32), is a loaded
near-contact activation/repacking theorem using the pairs' actual diameter partners
and positive-contact equilibrium.

---

## 8. Groemer and the exceptional-face branch

Current main preserves, at unreviewed proof-only scope, the recovered all-degree
Groemer stability stack:

- `docs/reports/target_c_all_degree_groemer_face_stability_2026-09-14.md`;
- its independent and hostile audits;
- `docs/reports/target_c_groemer_pair_matching_refinement_2026-09-14.md`; and
- `docs/reports/target_c_anchored_groemer_triple_matching_refinement_2026-09-14.md`.

On the small force-hull-residual branch \(R_F=o(D)\), those reports yield a
vanishing-gap matching of hidden near-unit pairs with asymptotic coefficient
\[
0.018569404829612\ldots
\]
and a vertex-disjoint family of contact-anchored almost-equilateral triples with
coefficient
\[
0.012855741805116\ldots.
\]

These statements remain proof-only; this synthesis does not promote them.

Equation (S.1) makes them more strategically relevant. A large \(Q-f\) does not
relieve the #667 budget; it increases the right side. Thus the exceptional-face
problem should be split geometrically rather than treated as a scalar escape:

- small \(R_F\): spend the Groemer near-contact pairs / anchored almost-unit
  triangles using KKT/global minimality;
- linear \(R_F\): use the exact residual-gluing route rather than raw chamber Oler
  slack;
- persistent high-degree tail: couple the tail to actual loaded returns and rigidity.

The last item is the direction of open draft PRs #668 and #671. They are
coordination targets, not premises of (S.1)--(S.34). PR #668 isolates a persistent
unbounded face-degree obstruction in fixed-port routing; PR #671 converts quadratic
bulk behind contact separators into simultaneous disjoint loaded returns and gives
additional return pressure for high-degree convex faces. Their claims must retain
their own audit status before being imported into a closing proof.

The useful combined objective is
\[
\text{high-degree tail}
+\text{loaded returns}
+\text{weighted penalty }2(Q-f)
\Longrightarrow
\text{source-level contradiction}.
\tag{S.35}
\]

### 8.1 Quantitative conditional composition with PR #668 and #671

This subsection is conditional on the stated proof-only claims of open drafts #668
and #671. It is not a premise of (S.1)--(S.35).

PR #668 defines, for each fixed integer \(M\ge5\), the high-degree augmented-face
currency
\[
T_M:=\sum_{\deg f>M}(\deg f-4).
\tag{S.36}
\]
If a fixed normalized route obstruction \(\lambda>0\) persists at every sufficiently
small fixed neighborhood of the deep port, #668 proves
\[
\liminf\frac{T_M}{D}\ge\frac{\lambda}{10}
\qquad\text{for every fixed }M.
\tag{S.37}
\]

Let
\[
r_M:=\sum_{\deg f>M}(\deg f-5).
\]
If \(N_M\) is the number of faces in this tail, then
\[
r_M=T_M-N_M.
\]
Every tail face contributes at least \(M-3\) to \(T_M\), so
\[
N_M\le\frac{T_M}{M-3}
\]
and therefore
\[
\boxed{
r_M\ge
\left(1-\frac1{M-3}\right)T_M.
}
\tag{S.38}
\]
Since \(Q-f\ge r_M\), first taking the sequence limit for each fixed \(M\) and
then \(M\to\infty\) gives the conditional consequence
\[
\boxed{
\liminf\frac{Q-f}{D}\ge\frac{\lambda}{10}.
}
\tag{S.39}
\]

Thus the #667 weighted frontier strengthens to
\[
\boxed{
5m_B+4S+2\sigma_R
\ge
\left[2(\pi+s)+\frac{\lambda}{5}\right]D
+5k+2(b-P_F)-o(D)
}
\tag{S.40}
\]
on the persistent #668 obstruction branch. High-degree escape is therefore not
neutral: it increases the physical-defect burden by at least \(\lambda D/5\).

PR #671 supplies a complementary physical consequence for one convex exceptional
face of degree \(m\) with \(\ell\) loaded boundary vertices:
\[
\boxed{
N_{\rm ret}(f)
\ge
\left\lceil\frac{(m-2\ell)_+}{4\pi+2}\right\rceil,
}
\tag{S.41}
\]
where the returns are vertex-disjoint contact paths to distinct actual loaded
attachments. Hence one face with \(m\ge\lambda D\) and \(\ell=o(D)\) forces a
linear loaded-return family.

What is not yet proved is the global summation step needed to close the tail:
different high-degree faces may charge overlapping return structures, rhombi, or
loaded attachments. Neither #668 nor #671 currently provides an injective or
bounded-overlap map from the full \(T_M\) currency to distinct returns or to a finite
source-preserving replacement.

The sharpened high-degree obligation is therefore
\[
\boxed{
\text{construct a bounded-overlap tail-to-return charge, or turn the returns directly
into a same-cardinality strict-}D\text{ competitor.}
}
\tag{S.42}
\]

If that bridge is proved, (S.40) supplies the global scalar pressure and #671 supplies
the physical loaded routing; another standalone face-degree estimate should not be
the next target.

---

## 9. Type I remains separate

The audited-working Type-I normal form is
`docs/targets/target-c/162-typeI-container-exchange-unification-audited.md`.
It already supplies, in either a macroscopic internal chamber or exterior cap,

- quadratic inactive area/population;
- linear perimeter and Oler slack;
- finite exchange saturation;
- fixed-depth protection; and
- linearly many vertex-disjoint contact-isolated pairs at
  \[
  1+O(1/D).
  \]

This is stronger near-unit scale than (S.34), but the geometry is different:
Type-I pairs are protected interior isolates, whereas the Type-II pairs in (S.34)
are loaded force-hull vertices with actual diameter partners.

Thus #667 cannot close Type I and the two matching theorems cannot simply be
identified. They suggest one common research theme: a finite density-increasing
repacking/activation theorem using the appropriate protection and diameter
bookkeeping in each branch.

For Type I the exact remaining theorem is still the collective protected
density-increasing repacking stated in Section 162. Independent first-contact
activations are insufficient.

---

## 10. Revised proof-only full-core frontier

After the #667 audit and this synthesis, the proof-only full-core hierarchy is:

```text
canonical full-core Type II
  -> audited #667 hull-side depletion
  -> mu_D >= 2.046952730226875...
  -> exact weighted defect frontier
       5 m_B + 4 S + 2 sigma_R
       >= 2(pi+s)D + 5k + 2(Q-f) + 2(b-P_F) - o(D)

  -> leftover singleton second depletion
       add +5 S_0 on the right

  -> exact feasibility bootstrap
       2 t_D D = M_D + 3k + m_B + 2u_B + 2(Q-f) - d_D

  -> terminal q/D -> pi
       t_D >= (3pi+2s)/5 = 2.265880714899459...
       -> older terminal-FREE near-1.96 / <=2.02 regimes are empty

  -> if another live branch forces linear m_B
       -> linear vertex-disjoint loaded near-unit hull matching

  -> bounded-degree / small-residual exceptional geometry
       Groemer near-unit pairs and anchored almost-equilateral triples

  -> persistent high-degree tail
       #668 tail currency raises the weighted frontier
       #671 supplies face-local loaded returns
       missing bounded-overlap tail-to-return/global competitor bridge

  -> Type I remains separate
       protected collective density-increasing repacking still missing

  -> still required for full closure
       exact activation, finite source-preserving strict-D competitor,
       or an upper currency theorem violating the weighted frontier
```

This is stronger than the old post-endpoint statement that one of several defects is
merely linear. It does not change canonical theorem authority until the new stack is
separately promoted.

---

## 11. Verification

The companion certificate
`research/verify_target_c_hull_depletion_post_endpoint_synthesis_2026_10_04.py`
checks:

- exact identity (S.8) on 102,496 finite ledger packets;
- the singleton resolution (S.10);
- the exact feasibility identities (S.22)--(S.23);
- 276,939 finite second-depletion substitutions;
- exact rational enclosures for all displayed constants;
- the closure-budget example;
- the high-degree conversion (S.38) on finite degree-tail packets; and
- all 2,040 subsets of cycle edges through cycle size 10 for the matching lower bound.

Its independent execution passes. It does not certify the analytic #667 depletion
theorem, Groemer stability, source optimality, the proof-only claims of #668/#671, or
C-II closure.

**Disposition:** preserve as an unreviewed proof-only synthesis. The exact weighted
identity, singleton second depletion, feasibility bootstrap, and terminal low-\(t\)
elimination are new consequences of the independently audited #667 core. The loaded
near-unit matching remains a conditional tool in any branch that independently
forces linear \(m_B\). The direct \(m_B\to\)#664 bridge is explicitly rejected.
