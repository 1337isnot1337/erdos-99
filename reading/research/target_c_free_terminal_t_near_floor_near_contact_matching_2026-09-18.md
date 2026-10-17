> Generated reading edition · [exact source](../../research/target_c_free_terminal_t_near_floor_near_contact_matching_2026-09-18.md) · source SHA-256 `612fcdb40df953f490232b0f3bcddb317f191a42d2a264f28040ddfa85ea8a0c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "15aaef95d6d709c158a5bc6ac9acd8ac81187419", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_t_near_floor_near_contact_matching_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "236cfdef3e9fa3e75da2c62d0a90cf67507f6a2dcdf83030bc6d84001123a577"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — near the new terminal `t` floor, small outer detour forces a linear near-contact matching

**Date:** 2026-09-18  
**Status:** proof-only terminal refinement; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE survivor sequences with `pi D-q=o(D)`  
**Depends on:** the terminal `t`-gap `0.00659`; the scope-safe matched all-train gap `g=0.007707`; audited atomic stopped-train orbit decomposition; audited §166 outer-atom detour capacity; the five-root pentagon closure lemma and contact-degree cap used in the existing dominant-orbit near-contact theorem  
**Certificate:** `research/verify_target_c_free_terminal_t_near_floor_near_contact_matching_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The exact-surplus near-contact theorem is no longer the right endpoint: the new terminal
`t` theorem proves that the actual loaded deficit variable is separated from that old
surplus endpoint by `0.00659`. This note moves the near-contact mechanism to the live
`t` endpoint.

The result is a quantitative dichotomy. In a `10^{-4}` window above the new `t` floor,
if the actual outer-walk detour is at most `10^{-5}D`, then the positive-contact core
contains a linear vertex-disjoint matching of noncontact pairs whose distances can be
made arbitrarily close to one. The matching density is at least `0.0461D`.

More generally, the proof gives an explicit two-parameter formula. The important point
is that the argument does **not** require the all-phase surplus to return to its now
excluded endpoint and does **not** require the nonunit force-hull-side count to be
sublinear.

---

## 1. Terminal constants and the live `t` stability budget

Put

$$
\Delta_2={\pi\over2\sqrt3},
\qquad
s_2=\sqrt{\Delta_2},
\qquad
g=0.007707,
$$

$$
C_0:=2s_2+g
=1.912332613727914\ldots,
$$

$$
M_*:=4s_2+2g
=3.824665227455829\ldots,
$$

and

$$
\mu_*:={\pi\over2}+{2s_2\over5}+{g\over5}
=1.953262849540479\ldots .
$$

The latest terminal theorem proves

$$
\boxed{
\liminf t_D\ge t_*:=\mu_*+0.00659
=1.959852849540479\ldots,
}
\tag{NF.1}
$$

where

$$
t_D={q-k\over D}.
$$

Its exact asymptotic decomposition is stronger than the number. On a convergent
terminal subsequence write

$$
r:=\lim {Q-f\over D}\ge0,
\qquad
\delta:=\lim {b-P_F\over D}\ge0,
$$

and

$$
a:=\lim\left({\tau_D\over D}-\left({\pi\over2}+g\right)\right)\ge0,
\qquad
\tau_D:=T-2\sqrt{R_4}.
$$

Then

$$
\boxed{
\lim(t_D-\mu_*)={2\over5}(r+\delta)+{1\over5}a.
}
\tag{NF.2}
$$

Fix a terminal window parameter `eta_t>=0` and suppose

$$
\limsup t_D\le t_*+\eta_t.
\tag{NF.3}
$$

Set

$$
e:=0.00659+\eta_t.
\tag{NF.4}
$$

Equations (NF.2)--(NF.3) give the single budget

$$
\boxed{
2(r+\delta)+a\le5e.
}
\tag{NF.5}
$$

In particular

$$
r+\delta\le{5e\over2},
\qquad
a\le5e.
\tag{NF.6}
$$

Thus the new `t` endpoint still has small superpentagonal degree excess, small outer
detour, and nearly minimal train slack whenever `eta_t` is small. Unlike the old
surplus endpoint, no conclusion about the nonunit-side currency is needed.

---

## 2. A dominant exact train orbit survives positive outer detour

Let `A` be the total atomic stopped-train mass in absolute `D` normalization. Group the
train-direction atoms into exact projective `pi/3` orbits. Write `M_j` for the atomic
mass of orbit `j`, `E_j` for its strict-rhombus crossing mass, and

$$
W:=\sup_jM_j.
$$

The audited atomic orbit decomposition gives

$$
E_j\le {M_j^2\over4},
\qquad
\sum_jE_j=\Delta_2.
\tag{NF.7}
$$

Audited §166, through the exposed-hull inequality, gives

$$
A\le C,
\qquad
C:=\lim {T-q/2\over D}.
\tag{NF.8}
$$

Since

$$
{T-q/2\over D}=C_0+a+o(1),
$$

(NF.5) yields

$$
C\le C_0+5e.
\tag{NF.9}
$$

Now

$$
4\Delta_2
\le\sum_jM_j^2
\le WA
\le W(C_0+5e).
$$

Hence some exact `pi/3` orbit carries atomic train mass at least

$$
\boxed{
W\ge W(e):={4\Delta_2\over C_0+5e}.
}
\tag{NF.10}
$$

This is the positive-detour replacement for the exact-surplus dominant-orbit estimate.

---

## 3. Outer detour bounds how much of that orbit can escape to the outer face

Let the limiting occurrence-counted outer direction measure be `nu`. Terminality gives
its total mass

$$
M=\pi+\delta.
\tag{NF.11}
$$

Audited §166 proves that an outer-direction atom of mass `w` has cubic detour cost

$$
\boxed{
w^3\le3M^2\delta.
}
\tag{NF.12}
$$

Assume on the subsequence that

$$
\delta\le d
\tag{NF.13}
$$

for some fixed `d>0`. Each of the at most three direction atoms in the dominant orbit
therefore has outer occurrence mass at most

$$
\boxed{
\omega(d):=\left(3(\pi+d)^2d\right)^{1/3}.
}
\tag{NF.14}
$$

Shrink three projective neighborhoods onto the dominant orbit. Every dominant-orbit
train has two terminal face-side occurrences. In the sequential limit
`D->infinity` followed by neighborhood radius `theta->0`, at least

$$
\boxed{
2W(e)-3\omega(d)
}
\tag{NF.15}
$$

bounded exceptional-face occurrences remain in those neighborhoods.

No claim is made that the entire outer direction measure is close to Lebesgue. The only
outer mass removed in (NF.15) is the actual atomic mass at the three limiting train
directions, exactly the quantity controlled by §166.

---

## 4. Near-floor degree arithmetic leaves many pentagons for the dominant orbit

Let

$$
B:=\lim {Q+4f\over D}.
$$

The exact route/train handshake gives

$$
\boxed{
B+\delta=M_*+2a.
}
\tag{NF.16}
$$

Also

$$
{f\over D}\to {M_*+2a-\delta-r\over5}.
\tag{NF.17}
$$

If `P_5` is the number of bounded pentagonal contact faces, degree arithmetic gives

$$
P_5\ge2f-Q=f-(Q-f).
$$

Therefore

$$
\boxed{
\liminf {P_5\over D}
\ge
{M_*\over5}+{2a\over5}-{\delta\over5}-{6r\over5}.
}
\tag{NF.18}
$$

For a small projective radius `theta`, let `P_5^{near}(theta)` count bounded pentagons
whose five side directions all lie within `theta` of the dominant three-line orbit.
Every pentagon not counted by `P_5^{near}(theta)` consumes at least one bounded
exceptional-face occurrence outside those neighborhoods. Combining (NF.15), (NF.16),
and (NF.18), then shrinking `theta`, gives

$$
\begin{aligned}
\lim_{\theta\downarrow0}\liminf {P_5^{near}(\theta)\over D}
\ge{}&
-{4M_*\over5}
-{8a\over5}
+{4\delta\over5}
-{6r\over5}\\
&+{8\Delta_2\over C_0+a}
-3\left(3(\pi+\delta)^2\delta\right)^{1/3}.
\end{aligned}
\tag{NF.19}
$$

The right side can be minimized exactly over the simple stability budget (NF.5).
For fixed `delta`, moving one unit of budget from `r` to `a` means replacing
`r` by `r-h` and `a` by `a+2h`; this strictly decreases the right side. Hence the
minimum has

$$
r=0,
\qquad
a=5e-2\delta.
\tag{NF.20}
$$

If `0<=delta<=d`, the resulting one-variable expression is decreasing throughout the
small concrete range used below. Thus its minimum is at `delta=d`.

Define

$$
\boxed{
\begin{aligned}
N(e,d):={}&-{4M_*\over5}
-{8\over5}(5e-2d)+{4d\over5}\\
&+{8\Delta_2\over C_0+5e-2d}
-3\left(3(\pi+d)^2d\right)^{1/3}.
\end{aligned}
}
\tag{NF.21}
$$

Then, in the stated small-window regime,

$$
\boxed{
\lim_{\theta\downarrow0}\liminf {P_5^{near}(\theta)\over D}
\ge N(e,d).
}
\tag{NF.22}
$$

The certificate checks the monotonicity used above and the concrete constants below.

---

## 5. Near-lattice pentagons give a vertex-disjoint matching of near contacts

The five-root closure lemma from the existing dominant-orbit theorem is finite. If a
strict convex unit pentagon has every projective side direction within `theta` of one
three-line `pi/3` orbit and

$$
10\sin(\theta/2)<1,
\tag{NF.23}
$$

then it contains two disjoint ears whose diagonals satisfy

$$
\boxed{
1<d_{ear}\le2\cos(\pi/3-\theta).
}
\tag{NF.24}
$$

Select one such ear from each near-orbit pentagon. As in the existing near-contact
proof, the selected diagonals are distinct and the auxiliary diagonal graph has maximum
degree at most five. A greedy matching therefore retains at least one ninth of them.

Consequently, whenever `N(e,d)>0`, for every

$$
0<\kappa<{N(e,d)\over9}
$$

and every metric tolerance `eps_geom>0`, after passing to the corresponding terminal
subsequence and then taking sufficiently large sources, there are at least

$$
\boxed{\kappa D}
\tag{NF.25}
$$

pairwise vertex-disjoint core-core nonedges with lengths in

$$
\boxed{(1,1+\mathrm{eps}_{geom}).}
\tag{NF.26}
$$

Each is an ear diagonal of an empty bounded pentagonal contact face. The emptiness is
from the existing isolate-host theorem: a bounded positive-contact face containing a
source point has degree at least seven.

This is a source-level near-active-constraint population. It is independent of the
nonunit force-hull-side currency that was eliminated from the new `t` theorem.

---

## 6. Concrete live-window corollary

Take

$$
\eta_t=10^{-4},
\qquad
e=0.00669,
\qquad
d=10^{-5}.
$$

Then

$$
W(e)=1.864339162491712\ldots,
$$

$$
\omega(d)=0.066651192127147\ldots,
$$

and the optimized bound (NF.21) is

$$
\boxed{
N(0.00669,10^{-5})
=0.415550892775345\ldots .
}
\tag{NF.27}
$$

Thus every terminal sequence satisfying

$$
\limsup t_D
\le1.959952849540479\ldots
\tag{NF.28}
$$

and

$$
\limsup {b-P_F\over D}\le10^{-5}
\tag{NF.29}
$$

has the following property: for every `eps_geom>0` and every

$$
\boxed{\kappa<0.046172321419482\ldots,}
\tag{NF.30}
$$

all sufficiently large members after the standard subsequence extraction contain at
least `kappa D` pairwise vertex-disjoint noncontact pairs at distances in
`(1,1+eps_geom)`.

A conservative repository-facing coefficient is

$$
\boxed{0.0461D.}
\tag{NF.31}
$$

Equivalently, the live terminal near-floor branch now has the source-level split

```text
actual outer detour >= 10^-5 D along the chosen limit,

or, if t <= t_* + 10^-4,

at least 0.0461 D pairwise vertex-disjoint core-core nonedges can be made
simultaneously arbitrarily close to unit length (in the asymptotic/subsequence sense).
```

This replaces the now-vacuous exact-surplus near-contact endpoint by a statement at the
actual post-`0.00659` `t` frontier.

---

## 7. Audit boundaries and next obstruction

1. **Sequential limits are explicit.** The train orbit is an atom of the limiting train
   measure. The proof first takes the source limit, then shrinks neighborhoods onto the
   three orbit directions. It does not treat finite-source train directions as exactly
   equal.
2. **Positive detour is retained.** Outer endpoints on the dominant orbit are removed
   using the audited cubic atom cost; no atomless-outer assumption is imported.
3. **No global outer regularity is assumed.** The outer measure may have diffuse or
   singular non-atomic structure away from the three dominant directions.
4. **No nonunit-side hypothesis is used.** The new terminal `t` identity already
   cancels that currency.
5. **No new local pentagon lemma is asserted.** The five-root closure and degree-five
   matching argument are reused from the existing certified near-contact theorem.
6. **No strict diameter descent is claimed.** Near-active nonedges are not active KKT
   rows. Their abundance alone does not produce a feasible full-source motion.

The remaining bottleneck is now sharper in the low-detour near-`t` branch. One must use
the linear matching of almost-active unit inequalities together with the rhombic train
shear coordinates and active diameter rows. A closing theorem would show either that a
positive fraction of those matched ears can be tightened simultaneously while all
active diameter inequalities are nonincreasing, or that locking them requires a
linear external-rank/stress payment incompatible with the terminal ledgers.

**Disposition:** proved a positive-detour dominant-orbit transfer to the actual new
terminal `t` floor and a `0.0461D` vertex-disjoint near-contact matching in the concrete
low-detour live window. The authoritative theorem-state ledger remains unchanged; C-II
remains open.
