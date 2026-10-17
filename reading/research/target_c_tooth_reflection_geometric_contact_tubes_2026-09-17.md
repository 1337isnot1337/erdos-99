> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_geometric_contact_tubes_2026-09-17.md) · source SHA-256 `7907b24e903378625e857f5484bec6155261915e45d8474c847e848c41e2c673`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 9 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "33ac9f665900567fc14a27271e8a738829e43d95", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_geometric_contact_tubes_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8afe9a13c35f16a0655c7eed762543b2fe696d8ffbb63274b1435ef29f281b12"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — geometric packing enlarges reflection contact buffers to almost `kappa_D` depth

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the growing contact-buffer reduction; no canonical promotion claimed  
**Scope:** controlled slow-scale `eta=3/26` simultaneous reflection family  
**Dependencies:** simultaneous reflection block diagonalization; blocker thin-shell localization; flat-cap blocker direction cone  
**Certificate:** `research/verify_target_c_tooth_reflection_geometric_contact_tubes_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The first growing-buffer theorem used only the contact-graph degree bound and obtained contact radius of order `log kappa_D`. The geometry of the blocker modules gives much more. Each blocker module lies within `O(1)` of a circular arc of length `O(D^(3/4))`. A contact path of length `r` stays inside the Euclidean `r`-tube of that arc. Unit-disk packing then bounds the number of source points in the whole tube by

```math
O(D^{3/4}r+r^2)
```

per module, rather than `O(5^r)`.

Consequently, if

```math
\kappa_D\to\infty,
\qquad
\kappa_D=o(D^{1/4}),
\tag{GT.1}
```

then **any** integer radius satisfying

```math
\boxed{r_D=o(\kappa_D)}
\tag{GT.2}
```

has the following properties for the controlled simultaneous family:

```math
\boxed{
\left|N_{r_D}\left(\bigcup_iU_i\right)\right|=o(D),
}
\tag{GT.3}
```

and the individual contact neighborhoods `N_{r_D}(U_i)` remain pairwise disjoint with no contact edges between them.

A near-maximal explicit choice is

```math
\boxed{
r_D=\left\lfloor{\kappa_D\over\log\kappa_D}\right\rfloor,}
\tag{GT.4}
```

for which

```math
\boxed{
\left|N_{r_D}\left(\bigcup_iU_i\right)\right|
=O\left({D\over\log\kappa_D}\right)=o(D).
}
\tag{GT.5}
```

For the concrete polynomial scale

```math
\kappa_D=D^{1/8},
\tag{GT.6}
```

the branch retains `(rho_*-o(1))D^(1/8)` simultaneous reflection modules and each module has an isolated contact buffer of radius

```math
\boxed{
r_D\sim {8D^{1/8}\over\log D},}
\tag{GT.7}
```

while all buffered modules together contain only

```math
\boxed{O(D/\log D)}
\tag{GT.8}
```

source points.

Thus any contact obstruction to a local module repair must propagate through a genuinely long chain. A fixed-depth or logarithmic-depth closure is no longer a viable escape.

---

## 1. Blockers lie near one short circular arc

Fix one selected module `(q_i,U_i)`. Suppress the index. The thin-shell theorem gives

```math
D<|z-q|<D+h_*,
\qquad
h_*={\sqrt{303}\over52}<0.335,
\qquad z\in U.
\tag{GT.9}
```

The flat-cap direction theorem gives, uniformly over all blockers,

```math
\angle(z-x,n)
\le(A+o(1))D^{-1/4},
\qquad
A=2\,3^{5/8}+4\,3^{1/8}.
\tag{GT.10}
```

Since `|q-x|=O(1)` and `|z-x|=D-O(1)`, replacing the ray origin `x` by `q` changes the direction by only `O(D^-1)`. Hence, for all sufficiently large `D`,

```math
\boxed{
\angle(z-q,n)
\le C_AD^{-1/4},
\qquad
C_A:=A+1=9.56283745460\ldots .
}
\tag{GT.11}
```

Let `Gamma` be the circular arc centered at `q`, of radius exactly `D`, consisting of directions within `C_A D^-1/4` of `n`. Its length is

```math
\boxed{
L_\Gamma=2C_AD^{3/4}.
}
\tag{GT.12}
```

For every `z in U`, take the point of `Gamma` with the same polar direction. Equation (GT.9) then gives distance below `h_*`. Thus

```math
\boxed{U\subset N_{h_*}^{\mathbb R^2}(\Gamma).}
\tag{GT.13}
```

This uses both pieces of the current reflection normal form: inverse-quarter angular localization and fixed radial shell thickness.

---

## 2. A contact ball lies in a Euclidean tube

Let `G_1` be the original source unit-contact graph. If a source point `v` has graph distance at most `r` from `U`, there is a contact path of at most `r` unit edges from `v` to some `z in U`. Therefore

```math
|v-z|\le r.
```

Together with (GT.13),

```math
\boxed{
N_r^{G_1}(U)
\subset
A\cap N_{r+h_*}^{\mathbb R^2}(\Gamma).
}
\tag{GT.14}
```

No assumption on branching of the contact graph is needed.

---

## 3. Unit-disk packing in a tube around an arc

We use a deliberately elementary tube-area estimate.

Let `Gamma` be any rectifiable arc of length `L`, and let `R>0`. Cover `Gamma` by points whose consecutive arclength spacing is at most `R`. At most

```math
{L\over R}+2
```

cover points are needed. Every point within Euclidean distance `R` of `Gamma` lies within distance `2R` of one cover point. Therefore

```math
\boxed{
\operatorname{area}(N_R(\Gamma))
\le4\pi LR+8\pi R^2.
}
\tag{GT.15}
```

Now let `S` be any unit-separated set of points whose centers lie in `N_R(Gamma)`. The open radius-`1/2` disks about points of `S` are disjoint, and all lie in `N_{R+1/2}(Gamma)`. Applying (GT.15) at `R+1/2` and dividing by `pi/4`,

```math
\boxed{
|S|
\le
16L(R+1/2)+32(R+1/2)^2.
}
\tag{GT.16}
```

Apply this to

```math
S=N_r^{G_1}(U),
\qquad
R=r+h_*.
```

Using (GT.12)--(GT.14),

```math
\boxed{
|N_r(U)|
\le
32C_A(r+h_*+1/2)D^{3/4}
+32(r+h_*+1/2)^2.
}
\tag{GT.17}
```

This replaces exponential contact-ball growth by a linear-in-`r` geometric bound throughout the relevant range.

---

## 4. Sum the tube bounds over all selected modules

The controlled simultaneous family has

```math
M_D=(\rho_*-o(1)){D^{1/4}\over\kappa_D},
\qquad
\rho_*=0.129220199818177\ldots .
\tag{GT.18}
```

Summing (GT.17) over all modules gives

```math
\begin{aligned}
\left|N_r\left(\bigcup_iU_i\right)\right|
&\le
(32C_A\rho_*+o(1))
{D(r+h_*+1/2)\over\kappa_D}\\
&\quad+
O\left(
{D^{1/4}(r+1)^2\over\kappa_D}
\right).
\end{aligned}
\tag{GT.19}
```

The leading numerical coefficient is

```math
\boxed{
32C_A\rho_*
=39.5427765348\ldots .
}
\tag{GT.20}
```

If `r=r_D=o(kappa_D)`, the first term is `o(D)`. The second term is also `o(D)` because

```math
{D^{1/4}r_D^2/\kappa_D\over D r_D/\kappa_D}
={r_D\over D^{3/4}}
\to0,
\tag{GT.21}
```

using `r_D=o(kappa_D)=o(D^(1/4))`. This proves (GT.3).

For the explicit choice `r_D=floor(kappa_D/log kappa_D)`, equation (GT.19) becomes

```math
\left|N_{r_D}\left(\bigcup_iU_i\right)\right|
=O\left({D\over\log\kappa_D}\right),
\tag{GT.22}
```

which proves (GT.5).

---

## 5. The enlarged buffers are still pairwise disjoint

The simultaneous theorem gives

```math
\operatorname{dist}_{\mathbb R^2}(U_i,U_j)
=\Omega(\kappa_DD^{3/4}).
\tag{GT.23}
```

Every contact edge has Euclidean length one, so a contact path from `U_i` to `U_j` has at least this many edges. Since

```math
r_D=o(\kappa_D)
=o(\kappa_DD^{3/4}),
\tag{GT.24}
```

for large `D` one has

```math
2r_D+1
<\operatorname{dist}_{G_1}(U_i,U_j).
\tag{GT.25}
```

Therefore

```math
\boxed{
N_{r_D}(U_i)\cap N_{r_D}(U_j)=\varnothing,
\qquad
E_{G_1}(N_{r_D}(U_i),N_{r_D}(U_j))=\varnothing.
}
\tag{GT.26}
```

The contact buffers are simultaneously large in graph radius and completely independent across modules.

---

## 6. Polynomial example

Take `kappa_D=D^(1/8)`. Then

```math
M_D=(\rho_*-o(1))D^{1/8}.
\tag{GT.27}
```

Choose

```math
r_D=\left\lfloor{D^{1/8}\over\log(D^{1/8})}\right\rfloor
=\left({8+o(1)\over\log D}\right)D^{1/8}.
\tag{GT.28}
```

The total tube bound is

```math
\left|N_{r_D}\left(\bigcup_iU_i\right)\right|
=O(D/\log D),
\tag{GT.29}
```

while distinct blocker modules start at Euclidean distance

```math
\Omega(D^{7/8}).
\tag{GT.30}
```

Thus polynomially many modules each carry a contact-isolation radius that itself grows polynomially (up to one logarithm), yet all those large buffers together remain sublinear.

---

## 7. Frontier effect

The remaining local-repair obstruction now has to survive a much longer contact propagation than the first graph-degree estimate suggested. Around each blocker module there is an isolated contact neighborhood of any prescribed radius `o(kappa_D)`, and the union of all such neighborhoods is still `o(D)`.

At the polynomial scale `kappa_D=D^(1/8)`, any obstruction that relies on unit contacts must propagate through roughly `D^(1/8)/log D` contact layers before it can escape the isolated module buffer. The thin-shell theorem says its starting set is only a collection of monotone blocker paths.

This still does not prove a repair. A contact chain can in principle continue for that many layers while staying inside the narrow geometric tube. The immediate next target is therefore a propagation theorem for such a chain: use the loaded-tooth/support-normal orientation to show that a unit-contact path launched from the outer blocker shell must accumulate radial or tangential displacement faster than the `O(D^(3/4))` tube permits, or must terminate at a low-contact vertex that admits the compensating inward motion.

**Disposition:** replaced logarithmic graph-degree contact buffers by geometric buffers of arbitrary radius `o(kappa_D)`. In particular, polynomially many reflection modules can each be isolated through `D^(1/8)/log D` contact layers while the full buffered population remains `O(D/log D)`. C-II and Level I remain open.
