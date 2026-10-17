> Generated reading edition · [exact source](../../research/target_c_five_currency_atomic_tradeoff_2026-09-12.md) · source SHA-256 `2a8eed386885268e1ef8116be39dfa7c816c7ce801c956c17be593186d5b6316`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2a48eb108d47a7f1952f36603580888605a917c9", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_five_currency_atomic_tradeoff_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "21569898004bc594354067bf009a5d6217d3f4442821b21e9376f6fc24e3b8f3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — five-currency coupling with atomic outer-endpoint capacity

**Date:** 2026-09-12  
**Status:** proof-only candidate; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note couples the exact Type-II five-currency conservation law to the
all-regime atomic endpoint/outer-detour estimate.  The point is to retain the
harmonic diameter/remainder currency when bounding the same global endpoint
capacity `Q+4f`; the two upper bounds are complementary and must not be
replaced by either one alone.

The result is a scalar bridge toward the live source-level target.  It does not
identify local and global face occurrences, and it does not claim a C-II
closure.

## 1. Normalized quantities

Work along a Type-II subsequence on which the following normalized quantities
converge:

```math
t={q-k\over D},\qquad \kappa={k\over D},\qquad
s={1\over D}\sum_r d_r,\qquad g={G_D\over D},
```

and put

```math
\delta={b-\operatorname{per}(F)\over D}\ge0.
```

Here `G_D` is the exact component remainder

```math
G_D=2+q+m-k-\sum_r d_r
   =R_I+s_B+\sum_r(\delta_r+2-d_r)\ge0.
```

Let `Q` and `f` be the global bounded-face degree excess and bounded
nonquadrilateral-face count.  The Type-II loaded-hull identities and the
five-currency law are

```math
e_{BB}=Q+2k+u_B,
\qquad
2(q-k)+2=\sum_r d_r+G_D+Q+u_B+k.
```

After division by `D`,

```math
\boxed{Q+u_B=2t-s-g-\kappa.}
\tag{FC.1}
```

In particular,

```math
\boxed{Q\le2t-s-g-\kappa.}
\tag{FC.2}
```

The canonical outer-walk ledger gives

```math
\boxed{Q=2t-\pi-\delta.}
\tag{FC.3}
```

Equation (FC.3) uses `b+Q=2(q-k)` and `b/D\to\pi+\delta`; it is the same
outer-detour currency that appears in the atomic endpoint theorem.

## 2. Atomic endpoint capacity

The audited-working normalized §155 theorem gives, for every fixed Fejér order `N>=2`,

```math
\boxed{
\liminf {Q+4f\over D}
\ge R_N(\delta):=
\left(4\sqrt{\Delta_2}-\sqrt{U_N(\delta)}\right)_+,
}
\tag{FC.4}
```

where

```math
\Delta_2={\pi\over2\sqrt3},
```

```math
U_N(\delta)=
{(\pi+\delta)^2\over N}
+{2\delta^2\over N}
\sum_{j=1}^{N-1}
\left(1-{j\over N}\right)(36j^2-1)^2.
```

Since every bounded nonquadrilateral face contributes at least one unit to
`Q`, `f<=Q`, and hence

```math
Q+4f\le5Q.
\tag{FC.5}
```

Combining (FC.2), (FC.4), and (FC.5) gives the new remainder-aware bound

```math
R_N(\delta)
\le5(2t-s-g-\kappa).
\tag{FC.6}
```

Combining (FC.3), (FC.4), and (FC.5) gives the perimeter-aware bound

```math
R_N(\delta)
\le5(2t-\pi-\delta).
\tag{FC.7}
```

Therefore every such subsequential limit satisfies

```math
\boxed{
t\ge {1\over2}\max\{\pi+\delta,\ s+g+\kappa\}
       +{R_N(\delta)\over10}.
}
\tag{FC.8}
```

This is the new scalar bridge.  The first term is the existing outer-hull
bound.  The second term is new: if the retained harmonic diameter/remainder
profile exceeds the perimeter currency, the same endpoint-capacity demand
forces a larger `q-k` density.

## 3. Carrier-slack insertion

The exact component identity makes (FC.8) compatible with the audited internal
face estimate.  If one selected harmonic component has normalized internal
strict-rhombus area `A` and normalized attachment-cell diameter `lambda`, the
local area/slack theorem gives

```math
g\ge
\left[C_{loc}\sqrt A-\lambda\right]_+,
\qquad
C_{loc}=1.8477910534538295\ldots .
\tag{FC.9}
```

Thus any independently established lower bound on `s` and carrier data can be
inserted into the second branch of (FC.8) without discarding `G_D`.  This is
source-level information about the same harmonic cells, not a global/local
face-injectivity assumption.

At the audited Section-118 frontier profile,

```math
s\ge2.7985963122\ldots,
\qquad g\ge0.2910434605\ldots,
```

so `s+g` is `3.0896...`, slightly below `pi`.  The new remainder-aware branch
is therefore not active at this particular frontier profile; it becomes active
only on profiles for which the retained diameter/remainder currency exceeds
`pi+delta`.  This limitation is useful: it identifies the precise numerical
condition needed before the five-currency refinement improves the perimeter
branch.  The §171/§155 capacity term still has to be combined with a geometric
strict-descent or train-lock theorem to close the active regime.

## 4. Regression and exact limitation

The scalar witness

```math
t={13\over5},\quad \kappa=0,\quad s=3,\quad g={1\over2},\quad
Q={7\over10},\quad f={7\over10},\quad u_B=1
```

satisfies (FC.1), and its outer detour is

```math
\delta=2t-\pi-Q=5.2-\pi-0.7\approx1.3584.
```

At this detour `R_7(delta)=0`, so (FC.8) is satisfied.  This is an explicit
regression against any claim that the five-currency coupling alone closes the
high-density region.  It also shows why the next step must use source geometry:
when the outer detour is large, Fejér capacity no longer forces a positive
bounded-face endpoint demand.

The exact implication chain is therefore

```math
\text{five-currency conservation}
\to \text{two upper bounds for }Q+4f
\to \text{remainder-aware density tradeoff (FC.8)}
\to
\begin{cases}
\text{small-detour source-level bridge still needed},\\
\text{large-detour geometric/descent bridge still needed}.
\end{cases}
```

**Classification:** proved candidate awaiting independent audit; no theorem-state
mutation; C-II remains open.
