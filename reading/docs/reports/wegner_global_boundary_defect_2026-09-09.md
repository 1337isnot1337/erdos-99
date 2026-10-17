> Generated reading edition · [exact source](../../../docs/reports/wegner_global_boundary_defect_2026-09-09.md) · source SHA-256 `9799b117c93154ed87671735693e69abe8a56ca070e7cc513926db2dc2620f76`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1144055F7305","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — Wegner improves the global boundary defect and plateau allowance

**Date:** 2026-09-09  
**Repository base:** `cf790155660ad46797e53c7f44371b078f7eab7b`  
**Run type:** external finite-packing theorem import / global source consequence  
**Target:** global diameter asymptotics and Target A scalar plateau defect  
**Depends on:** Wegner's finite circle-packing inequality, Oler, isodiametric/perimeter bounds, strict translated-lattice upper comparison  
**External source:** K. J. Böröczky and I. Z. Ruzsa, *Note on an Inequality of Wegner*, Discrete & Computational Geometry 37 (2007), 245--249, DOI `10.1007/s00454-006-1277-4`, quoting Wegner's theorem. The repository already indexes and archives this source.  
**Computation:** decimal evaluation only

## LEVEL I STATUS

`STILL OPEN`

Target A currently uses the universal Oler defect bound

```math
0<q_n:=n-1-\Delta D(n)^2\le\frac\pi2D(n),
\qquad
\Delta:=\frac\pi{2\sqrt3}.
```

Wegner's boundary correction gives a strict asymptotic improvement at exactly this linear scale.

Let

```math
W_n:=\left\lceil\sqrt{12n-3}-3\right\rceil,
\qquad
\kappa:=\frac1{\sqrt3}-\frac12.
```

Then every global minimum-diameter `n`-point source satisfies the finite inequality

```math
\boxed{
q_n
\le
\frac\pi2D(n)
-
\kappa\,[W_n-\pi D(n)]_+.
}
\tag{WG-G.1}

```

Since

```math
\frac n{D(n)^2}\to\Delta,
```

we have

```math
\frac{W_n}{D(n)}	o
\omega:=\sqrt{12\Delta}
=\sqrt{2\pi\sqrt3}
=3.2989083323\ldots>\pi.
```

Consequently

```math
\boxed{
\limsup_{n\to\infty}
\frac{q_n}{D(n)}
\le
C_W
:=
\frac\pi2-\kappa(\omega-\pi)
=1.5586279167\ldots .
}
\tag{WG-G.2}

```

The previous coefficient was

```math
\frac\pi2=1.5707963268\ldots,
```

so the certified boundary-order gain is

```math
\boxed{
\frac\pi2-C_W
=0.0121684101\ldots .
}
\tag{WG-G.3}

```

This also improves the asymptotic length of any fixed-diameter plateau from `pi D/2` to `C_W D`.

The gain does **not** resolve Target A's transfer-sign problem, because that identity contains a difference of two boundary defects. It is nevertheless a new global theorem available to every route.

---

## 1. Rescaled Wegner theorem

For `N>=2` nonoverlapping unit disks, Wegner's theorem states that the convex hull `D_disk` of their union satisfies

```math
\operatorname{area}(D_{disk})
\ge
2\sqrt3(N-1)
+(2-\sqrt3)W_N
+\pi,
\tag{1.1}
```

where

```math
W_N=\left\lceil\sqrt{12N-3}-3\right\rceil.
```

Let `K` be the convex hull of `N` points of minimum pairwise separation one. Scale the centers by two and place unit disks around them. Steiner gives

```math
\operatorname{area}(2K+B_1)
=4\operatorname{area}(K)+2\operatorname{per}(K)+\pi.
```

Substitution into (1.1), cancellation of `pi`, and division by four give

```math
\boxed{
\operatorname{area}(K)+\frac12\operatorname{per}(K)
\ge
\frac{\sqrt3}{2}(N-1)
+rac{2-\sqrt3}{4}W_N.
}
\tag{1.2}

```

Put

```math
a_0:=\frac{\sqrt3}{2},
\qquad
c_W:=\frac{2-\sqrt3}{4}.
```

Oler in the same normalization is

```math
\operatorname{area}(K)+\frac{a_0}{2}\operatorname{per}(K)
\ge a_0(N-1).
\tag{1.3}

```

Since

```math
\frac12-rac{a_0}{2}=c_W,
```

combining the better of (1.2) and (1.3) gives

```math
\boxed{
\operatorname{area}(K)
\ge
 a_0(N-1)
-\frac{a_0}{2}\operatorname{per}(K)
+c_W[W_N-\operatorname{per}(K)]_+.
}
\tag{1.4}

```

This is the exact Oler+Wegner form used below.

---

## 2. Apply to a global minimum-diameter source

Let `A_n` be a global minimizer with

```math
|A_n|=n,
\qquad
D=D(n),
```

and let

```math
K=\operatorname{conv}A_n.
```

The source has minimum separation one and diameter `D`, so

```math
\operatorname{area}(K)
\le\frac\pi4D^2,
\tag{2.1}
```

and

```math
\operatorname{per}(K)
\le\pi D.
\tag{2.2}
```

From (1.4), monotonicity of the positive part, and (2.1)--(2.2),

```math
\begin{aligned}
a_0(n-1)
&\le
\operatorname{area}(K)
+rac{a_0}{2}\operatorname{per}(K)
-c_W[W_n-\operatorname{per}(K)]_+\\
&\le
\frac\pi4D^2
+rac{a_0\pi}{2}D
-c_W[W_n-\pi D]_+.
\end{aligned}
\tag{2.3}
```

Divide by `a_0`. Since

```math
\frac{\pi}{4a_0}=\Delta,
\qquad
\frac{c_W}{a_0}
=rac{2-\sqrt3}{2\sqrt3}
=rac1{\sqrt3}-\frac12
=\kappa,
```

we obtain

```math
\boxed{
n-1
\le
\Delta D^2
+rac\pi2D
-\kappa[W_n-\pi D]_+.
}
\tag{2.4}

```

Subtract `Delta D^2`. This is WG-G.1.

The strict translated-lattice comparison already in the repository gives

```math
q_n>0,
```

so the complete finite sandwich is

```math
\boxed{
0<q_n
\le
\frac\pi2D(n)
-\kappa[W_n-\pi D(n)]_+.
}
\tag{2.5}

```

---

## 3. Asymptotic coefficient

The standard lattice/Oler asymptotics give

```math
\frac n{D(n)^2}\to\Delta.
\tag{3.1}
```

Therefore

```math
\frac{W_n}{D(n)}
\to
\sqrt{12\Delta}
=\omega.
\tag{3.2}
```

Since

```math
\omega-\pi
=0.1573156788\ldots>0,
```

the positive part in WG-G.1 is eventually active. Divide WG-G.1 by `D(n)` and pass to limsup:

```math
\limsup\frac{q_n}{D(n)}
\le
\frac\pi2-\kappa(\omega-\pi)
=:C_W.
```

Numerically,

```math
\kappa=0.07735026919\ldots,
```

```math
C_W=1.5586279167\ldots .
```

This proves WG-G.2--WG-G.3.

---

## 4. Improved plateau allowance

Fix a diameter value `D` occurring on a plateau, and let

```math
N_-:=\min\{n:D(n)=D\},
\qquad
N_+:=\max\{n:D(n)=D\}.
```

Because `D` is the same at both endpoints,

```math
N_+-N_-
=q_{N_+}-q_{N_-}.
\tag{4.1}
```

The strict lattice bound gives `q_{N_-}>0`. Hence

```math
N_+-N_-
<q_{N_+}.
\tag{4.2}
```

Along any unbounded sequence of plateaus, WG-G.2 gives

```math
\boxed{
\limsup
\frac{N_+-N_-}{D}
\le C_W
=1.5586279167\ldots .
}
\tag{WG-G.4}
```

This replaces the previous asymptotic allowance `pi/2=1.570796...`.

The same argument applies to the one-sided plateau slack

```math
p=N_+-N
```

used in Target A for any source `N` on the plateau:

```math
\boxed{
\limsup\frac pD\le C_W.
}
\tag{WG-G.5}
```

---

## 5. Target A update

Target A Section 114.2 currently records

```math
0<q_r\le\frac{\pi D(r)}2.
```

WG-G.1 is a strict finite strengthening:

```math
q_r
\le
\frac\pi2D(r)
-\kappa[W_r-\pi D(r)]_+.
```

Asymptotically the right side has coefficient `C_W` rather than `pi/2`.

The exact transfer identity remains

```math
J_{av}-B_{av}
=
\frac{\varepsilon^*t}{a_0}
+q_{N_-}-q_{m_+}.
```

The new theorem narrows the allowed range of each `q` term, but does not determine the sign of their difference. Therefore no Target A closure is claimed.

Likewise the continuum Hall plateau slack in Section 115 improves only quantitatively:

```math
p<(C_W+o(1))D
```

on unbounded plateaus. The structural source-to-response gap remains.

---

## 6. Equivalent positive lower bound for the old Oler defect `E(n)`

Target A also uses

```math
E(n)
:=
\Delta D(n)^2+rac\pi2D(n)-(n-1)
=rac\pi2D(n)-q_n.
```

WG-G.1 is equivalent to

```math
\boxed{
E(n)
\ge
\kappa[W_n-\pi D(n)]_+.
}
\tag{6.1}
```

Hence

```math
\boxed{
\liminf\frac{E(n)}{D(n)}
\ge
\kappa(\omega-\pi)
=0.0121684101\ldots .
}
\tag{6.2}
```

This is the first explicit positive linear lower bound on the classical Oler boundary defect in the current theorem stack.

Again, Target A uses a **difference** `E(m_+)-E(N_-)`, so two positive lower bounds do not control that difference.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| rescaled Wegner inequality | external theorem + exact Steiner rescaling | source already archived/indexed in repo |
| finite global WG-G.1 | proved | Oler+Wegner + isodiametric + perimeter-diameter |
| `W_n/D->sqrt(12Delta)` | proved from known density asymptotic | ceiling and `-3` are lower order |
| coefficient `C_W=1.5586279167...` | proved | direct limit of WG-G.1 |
| plateau coefficient improvement | proved | same-D identity `N_+-N_-=q_+-q_-` and `q_->0` |
| Target A sign resolved | no | transfer contains uncontrolled difference of endpoint defects |
| Level I | still open | theorem is a strict boundary-order improvement only |

---

## 8. Next target

Wegner converts the old unconstrained interval

```math
0<q_n\le(\pi/2)D
```

into a strictly smaller asymptotic interval. A stronger route would need a **stability-sensitive lower or upper comparison between two plateau endpoints**, not independent one-point bounds.

Natural next questions are:

1. can Wegner equality/stability constrain how `q_n/D` changes along a fixed-`D` plateau;
2. can the Groemer shape stability already used in Target C couple `E(m_+)` and `E(N_-)` because the two sources share a diameter scale;
3. can a same-hull saturation theorem turn the improved plateau allowance into a source Hall rank gain.

Absent such a cross-endpoint theorem, WG-G should remain a report-level global improvement rather than a claimed Target A solution.
