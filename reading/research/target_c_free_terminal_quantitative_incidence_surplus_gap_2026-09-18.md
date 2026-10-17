> Generated reading edition · [exact source](../../research/target_c_free_terminal_quantitative_incidence_surplus_gap_2026-09-18.md) · source SHA-256 `ea0920ef762fd7e9eb104f631dde98f5c0d12ebff908b18ecba4ba4955d41d54`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c6ffdd4eacefd4291b4f3f695689caee25e14bb8", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_quantitative_incidence_surplus_gap_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "dcfe13bdcd24e8531454c70dd111614acd46f7094b6ac59ecef28bb0329456bf"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — quantitative incidence gap above the terminal FREE surplus endpoint

**Date:** 2026-09-18  
**Status:** proof-only terminal strengthening; theorem-state authority unchanged  
**Scope:** full-core Type-II terminal FREE survivor sequences with `pi D-q=o(D)`  
**Depends on:** terminal FREE surplus-endpoint stability; hostile-audited two-bin dominant-orbit mass theorem; hostile-audited shared dominant/complement routewise retention; hostile-audited dominant outer-energy transport; hostile-audited complement O--O train/rhombus-incidence theorem  
**Refines:** the exact endpoint incidence exclusion and the `0.00122` outer-energy surplus gap  
**Certificate:** `research/verify_target_c_free_terminal_quantitative_incidence_surplus_gap_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The exact endpoint incidence exclusion has a large unused margin. Making that argument
quantitative gives a much larger explicit surplus gap than the one-sector outer-energy
argument.

Put

```math
\mu_*=
\frac\pi2+\frac25\sqrt{\frac\pi{2\sqrt3}}+\frac{0.007707}{5}
=1.953262849540479\ldots .
```

Then every terminal full-core Type-II FREE survivor sequence satisfies

```math
\boxed{
\liminf\mu_D
\ge
\mu_*+0.00645
=1.959712849540479\ldots .
}
\tag{QI.1}
```

The proof uses no new local geometry. It combines existing hostile-audited modules in a
regime where their constants have substantial room. The numerical root of the same
conservative scalar composition is approximately `0.006496326`; the theorem uses the
rational value `0.00645` and keeps a visible exact margin.

---

## 1. Stability window

Assume for contradiction that a terminal FREE subsequence satisfies

```math
\limsup\mu_D\le\mu_*+\varepsilon,
\qquad
\varepsilon:=0.00645=\frac{129}{20000}.
\tag{1.1}
```

Use the terminal surplus-stability variables

```math
a:=\lim\left(
\frac{\tau_D}{D}-\left(\frac\pi2+g\right)
\right),
\qquad
\delta:=\lim\frac{b-\operatorname{per}(F)}D,
\qquad
g=0.007707.
```

The exact nonnegative endpoint decomposition gives

```math
a\le5\varepsilon=0.03225,
\qquad
\delta\le\frac52\varepsilon=0.016125.
\tag{1.2}
```

Let

```math
\Delta_2:=\frac\pi{2\sqrt3},
\qquad
s_2:=\sqrt{\Delta_2},
\qquad
A_0:=2s_2+g.
```

The all-train scalar

```math
C:=\lim\frac{T-q/2}{D}
```

satisfies

```math
\boxed{
C=A_0+a\le A_0+0.03225
=1.944582613727914\ldots .}
\tag{1.3}
```

---

## 2. Two-bin concentration leaves at most `0.0404D` residual atomic train mass

Let `A` be the total absolute atomic train mass in the limiting projective train-phase
measure, and let `M` be the mass of the largest exact `pi/3` orbit. The hostile-audited
two-bin theorem gives

```math
M\ge m_2(A),
\qquad
m_2(x):=\frac{x+\sqrt{8\Delta_2-x^2}}2.
\tag{2.1}
```

The exposed-hull theorem gives `A<=C`, while `x-m_2(x)` is increasing on the present
physical interval. Thus the residual atomic train mass

```math
r:=A-M
```

obeys

```math
r\le C-m_2(C).
\tag{2.2}
```

At the maximal value in (1.3), the exact certificate gives

```math
C-m_2(C)
<0.040385207071175\ldots
<0.0404.
```

Hence

```math
\boxed{r<0.0404.}
\tag{2.3}
```

---

## 3. Shared retention forces complement O--O pair mass

The total complete-train density is

```math
\frac TD
= C+\frac{q}{2D}
\longrightarrow C+\frac\pi2.
```

The number `N_cD+o(D)` of complete trains outside the dominant exact orbit is at most

the total train count minus the dominant-orbit mass. Therefore

```math
\begin{aligned}
N_c
&\le C+\frac\pi2-m_2(C)\\
&=\frac\pi2+\bigl(C-m_2(C)\bigr)\\
&\le\frac\pi2+r.
\end{aligned}
\tag{3.1}
```

The hostile-audited shared routewise-retention theorem now supplies

- retained dominant-orbit outer-occurrence mass `z`, and
- retained complement O--O pair mass `p`,

with

```math
\boxed{
z+p\ge\pi-N_c
\ge\frac\pi2-r.}
\tag{3.2}
```

The retained dominant occurrences pay actual selected outer directional energy

```math
F(z):=z-6\sin(z/6).
```

That energy is a sub-sum of the total outer-route directional energy, so

```math
F(z)\le\delta.
\tag{3.3}
```

Use the rational threshold

```math
z_0:=1.519=\frac{1519}{1000}.
```

The alternating sine estimate gives

```math
\begin{aligned}
F(z_0)
&\ge
\frac{z_0^3}{216}-\frac{z_0^5}{155520}\\
&=0.0161743026743995\ldots\\
&>0.016125.
\end{aligned}
\tag{3.4}
```

Equations (1.2), (3.3), and (3.4) force

```math
z<1.519.
\tag{3.5}
```

Combining (2.3), (3.2), and (3.5),

```math
\begin{aligned}
p
&>\frac\pi2-0.0404-1.519\\
&=0.0113963267948966\ldots .
\end{aligned}
```

In particular,

```math
\boxed{p>0.0113.}
\tag{3.6}
```

This is much smaller than the exact-endpoint O--O population, but it is already far
more than the residual rhombus capacity can support once every retained complement
train must be macroscopic.

---

## 4. Complement incidence demand contradicts residual rhombus capacity

For the same retained complement O--O pair family, let `e_c` be the normalized weighted
sum of the two terminal outer-edge directional energies. The hostile-audited
train-length/rhombus-incidence theorem gives

```math
\boxed{
p(1-\delta)-\frac{e_c}{2}
\le\frac{r^2}{2}.}
\tag{4.1}
```

The left side is the weighted quadratic train-rhombus incidence demand. The right side
is the complete asymptotic supply of non-dominant strict rhombi, including all residual
exact `pi/3` orbits.

The conservative energy bound is simply

```math
e_c\le\delta,
\tag{4.2}
```

because the selected weighted complement terminal occurrences form a sub-sum of the
occurrence-counted outer route edges.

Using (1.2), (2.3), (3.6), and (4.2), the left side of (4.1) is strictly larger than

```math
0.0113(1-0.016125)-\frac{0.016125}{2}
=0.0030552875,
\tag{4.3}
```

while its right side is strictly smaller than

```math
\frac{0.0404^2}{2}
=0.00081608.
\tag{4.4}
```

The gap is

```math
0.0022392075.
```

Thus (4.1) is impossible. The assumption (1.1) is false, proving (QI.1).

---

## 5. Consequences and scalar saturation

Canonical loaded-contact localization gives

```math
\mu_D
=t_D+\frac{m_B}{D}+o(1),
\qquad
t_D:=\frac{q-k}{D},
```

so the new theorem also yields

```math
\boxed{
\liminf\left(t_D+\frac{m_B}{D}\right)
\ge1.959712849540479\ldots .}
\tag{5.1}
```

In particular, on every terminal subbranch with `m_B=o(D)`,

```math
\boxed{
\liminf t_D
\ge1.959712849540479\ldots .}
\tag{5.2}
```

Conversely, any terminal survivor with `t_D` near the old
`1.953262849540479...` floor must carry a linear population of nonunit force-hull
sides.

For orientation only, replacing the rational caps in this proof by the exact functions

```math
r(C)=C-m_2(C),
\qquad
F^{-1}(\delta)
```

and using the conservative `e_c<=delta` incidence inequality produces a scalar zero
near

```math
\varepsilon=0.006496326.
```

The certified `0.00645` gap is therefore already close to the limit of this exact
composition. Improving the constant further is secondary. The useful next step is to
feed the dichotomy in (5.1) into the global Sections 122--123 detour/payment currency:
large `m_B` changes `e_BB-k`, while the complementary branch has the stronger `t`
floor (5.2).

No theorem-state file is changed. All inputs beyond the canonical loaded-contact
identity remain proof-only under their recorded scopes.
