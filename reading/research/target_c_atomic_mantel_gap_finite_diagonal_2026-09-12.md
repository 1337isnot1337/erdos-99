> Generated reading edition · [exact source](../../research/target_c_atomic_mantel_gap_finite_diagonal_2026-09-12.md) · source SHA-256 `b0d5825d4435c8bd5b73e03f70710f5d12eef0d58e2c740bce11363031ba0e4c`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 3 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — all-regime atomic Mantel gap via a finite two-scale diagonal

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only corollary of the robust near-complete-grid theorem; theorem authority unchanged.

The earlier attempted compactness proof of a uniform gap was correctly retracted:
total atomic mass is not upper-semicontinuous under weak convergence. The conclusion,
however, can be proved without passing atomic mass through a second weak limit.

The repair keeps the near-equality atom neighborhoods at the **finite-source level**.
If Type-II limits had atomic mass arbitrarily close to the §142 Mantel minimum, then for
the `j`-th such limit one dominant `pi/3` orbit already carries
`2sqrt(Delta_2)-o_j(1)` absolute train mass and `Delta_2-o_j(1)` crossing mass. Choose
shrinking neighborhoods of that orbit, then choose one sufficiently large finite source
realizing those statistics. This diagonal sequence directly contains two shrinking
phase families of combined size at least `(3/2)sqrt(Delta_2)D-o(D)` with only
`o(D^2)` missing crossings, contradicting the robust grid theorem.

Put

```math
\Delta_2={\pi\over2\sqrt3},
\qquad
s_2:=\sqrt{\Delta_2}.
```

### Theorem A — uniform all-regime atomic gap

There exists an absolute constant

```math
\boxed{\eta_{grid}>0}
\tag{A.1}
```

such that every audited-working Type-II train-measure subsequential limit in the §142
scope satisfies

```math
\boxed{x\sigma\ge2s_2+\eta_{grid},}
\tag{A.2}
```

where `x=lim T/D` and `sigma` is the total atomic mass of the limiting projective train
direction probability measure.

No numerical value of `eta_grid` is asserted.

Consequently

```math
\boxed{
\liminf {T-q/2\over D}
\ge2s_2+\eta_{grid},
}
\tag{A.3}
```

```math
\boxed{
\liminf {2f-k\over D}
\ge2s_2-{\pi\over2}+\eta_{grid},
}
\tag{A.4}
```

and the §146 weighted diameter-edge floor improves to

```math
\boxed{
\liminf {1\over D}
\left(
 h-{d_H\over9}-{10s_Z\over9}
\right)
\ge
{4\over9}(\pi+s_2)+{2\over9}\eta_{grid}.
}
\tag{A.5}
```

This is an all-regime Type-II strengthening; no outer-detour hypothesis is used.

---

## 1. Assume the gap fails

Audited §142 already proves

```math
x\sigma\ge2s_2
\tag{1.1}
```

for every Type-II subsequential limit.

Assume no positive uniform gap exists. For each integer `j>=1`, choose a Type-II
survivor subsequential limit `(x_j,mu_j)` whose atomic mass `sigma_j` satisfies

```math
2s_2
\le A_j:=x_j\sigma_j
\le2s_2+{1\over j}.
\tag{1.2}
```

Everything below is done first **inside this fixed `j`-th limit**. We do not take a
weak limit of the measures `mu_j`.

Let the atoms of `mu_j`, in absolute `D` normalization, be split into the orbits of

```math
\phi\mapsto\phi+{\pi\over3}\pmod\pi.
```

Let `M_{j,r}` be the total atomic mass in orbit `r`, and `E_{j,r}` the normalized
strict-rhombus crossing mass assigned to that orbit. Audited §142 gives

```math
E_{j,r}\le{M_{j,r}^2\over4}
\tag{1.3}
```

by weighted Mantel, while all limiting quadratic crossing mass lies on exact atomic
relation pairs, so

```math
\sum_rE_{j,r}=\Delta_2=s_2^2.
\tag{1.4}
```

Also

```math
\sum_rM_{j,r}=A_j.
\tag{1.5}
```

Therefore

```math
s_2^2
\le {1\over4}\sum_rM_{j,r}^2
\le {A_j^2\over4}
=s_2^2+O(1/j).
\tag{1.6}
```

Hence

```math
A_j^2-\sum_rM_{j,r}^2=o_j(1).
\tag{1.7}
```

Since

```math
A_j^2-\sum_rM_{j,r}^2
=2\sum_{r<s}M_{j,r}M_{j,s},
```

and `A_j->2s_2>0`, one orbit `r(j)` carries all but `o_j(1)` of the atomic mass:

```math
\boxed{
M_j:=M_{j,r(j)}=2s_2-o_j(1).
}
\tag{1.8}
```

All other orbit masses sum to `o_j(1)`. Equation (1.4) and (1.3) then also force the
dominant-orbit crossing mass to satisfy

```math
\boxed{
E_j:=E_{j,r(j)}=s_2^2-o_j(1).
}
\tag{1.9}
```

Thus the `j`-th fixed limiting measure already has one almost-Mantel-saturated
three-atom orbit. No second compactness step has occurred.

---

## 2. Freeze shrinking neighborhoods before choosing the finite source

Let the three possible atom directions in the dominant orbit be

```math
\phi_{j,0},
\qquad
\phi_{j,1}=\phi_{j,0}+\pi/3,
\qquad
\phi_{j,2}=\phi_{j,0}+2\pi/3
\quad(\bmod\pi).
```

Choose three disjoint projective arcs

```math
U_{j,0},U_{j,1},U_{j,2}
```

with radii at most `1/j`, boundaries of `mu_j`-measure zero, and so small that the
`mu_j` mass in their union differs from the three atomic masses by at most `1/j`.
Because the limiting crossing measure is supported on the exact relation and the
non-dominant orbit mass is `o_j(1)`, shrink the arcs further if necessary so that their
union carries crossing mass at least

```math
E_j-{1\over j}.
\tag{2.1}
```

Now return to one actual source sequence realizing the fixed limit `(x_j,mu_j)`. Choose
one sufficiently large member, with diameter `D_j`, so that simultaneously:

1. Type-II normalized errors are at most `1/j`;
2. the number `N_j` of complete trains whose directions lie in
   `U_{j,0} union U_{j,1} union U_{j,2}` satisfies
   
   ```math
   {N_j\over D_j}=2s_2-o_j(1);
   \tag{2.2}
   ```

3. the number `R_j^{orb}` of actual strict-rhombus crossings between those selected
   trains satisfies
   
   ```math
   {R_j^{orb}\over D_j^2}=s_2^2-o_j(1).
   \tag{2.3}
   ```


Choose the finite source far enough out that `D_j->infinity`. The three neighborhood
widths tend to zero because they were chosen at most `1/j`.

The induced physical train-crossing graph `G_j` on these `N_j` selected trains is
simple and triangle-free. Equations (2.2)--(2.3) give

```math
\boxed{
e(G_j)={N_j^2\over4}-o(D_j^2).
}
\tag{2.4}
```

This is now a purely finite near-Mantel statement.

---

## 3. Finite near-Mantel stability exposes two almost-complete atom groups

Apply the elementary §153 near-Mantel lemma to `G_j`. There is a partition

```math
V(G_j)=X_j\sqcup Y_j
```

such that

```math
|X_j|=s_2D_j+o(D_j),
\qquad
|Y_j|=s_2D_j+o(D_j),
\tag{3.1}
```

`X_j` is independent, `Y_j` spans only `o(D_j^2)` crossing edges, and only
`o(D_j^2)` pairs of `X_j x Y_j` are missing.

Write

```math
G_{j,r}:=\{\tau:[u_\tau]\in U_{j,r}\},
\qquad r=0,1,2.
```

For large `j`, each `U_{j,r}` has projective diameter below `pi/3`, so two trains in
the same `G_{j,r}` cannot cross in a strict triangle-free unit rhombus.

If one `G_{j,r}` had positive linear populations in both `X_j` and `Y_j`, every one of
those cross-side same-window pairs would be missing. Since the total cross-side missing
count is `o(D_j^2)`, each window group lies, up to `o(D_j)` trains, entirely on one
Mantel shore.

Both shores have limiting size `s_2D_j`. There are at most three nonnegligible window
groups. Therefore one shore consists, up to `o(D_j)`, of one group of size

```math
\boxed{s_2D_j+o(D_j),}
\tag{3.2}
```

and the other shore has a group of size at least

```math
\boxed{{s_2\over2}D_j+o(D_j).}
\tag{3.3}
```

Call these two opposite-shore groups `A_j,B_j`. Their projective direction widths tend
to zero, their limiting axes differ by exactly `pi/3`, and

```math
\boxed{
\#\bigl((A_j\times B_j)\setminus E(G_j)\bigr)=o(D_j^2).
}
\tag{3.4}
```

Thus the finite diagonal families satisfy every hypothesis of the robust near-complete
grid theorem proved on this branch, with

```math
a=s_2,
\qquad
b\ge{s_2\over2}.
```

That theorem forces

```math
{3\over2}s_2\le{2\over\sqrt3},
```

contrary to

```math
{3\over2}s_2=1.4284692102\ldots
>{2\over\sqrt3}=1.1547005383\ldots .
```

This contradiction proves Theorem A.

The proof never takes a second weak limit of the atomic masses. The diffuse-to-atom
semicontinuity regression is therefore irrelevant.

---

## 4. Propagation through §§142 and 146

Audited §142 gives, for every Type-II subsequential limit,

```math
{q/T}=y\le2(1-\sigma).
```

Hence

```math
\lim {T-q/2\over D}
=x\left(1-{y\over2}\right)
\ge x\sigma
\ge2s_2+\eta_{grid}.
```

This proves (A.3).

Use the exact train ledger

```math
T-q=2f-k
```

and the Type-II perimeter bound `q/D<=pi+o(1)` to get (A.4).

For (A.5), repeat the audited §146 algebra. Along a normalized subsequence put

```math
{h\over D}\to y_h,
\qquad
{d_H\over D}\to d,
\qquad
{s_Z\over D}\to s.
```

Since

```math
T=q+2f-k,
\qquad
q=h+d_H,
\qquad
k=d_H+s_Z,
```

(A.3) gives

```math
{f\over D}
\ge
s_2+{\eta_{grid}\over2}
-{y_h\over4}+{d\over4}+{s\over2}-o(1).
\tag{4.1}
```

The exact outer ledger and Type-II force-hull perimeter limit give

```math
\limsup {Q\over D}+2s\le2y_h-\pi.
\tag{4.2}
```

Since `Q>=f`, combine (4.1)--(4.2):

```math
{9y_h\over4}
\ge
\pi+s_2+{\eta_{grid}\over2}
+{d\over4}+{5s\over2}.
```

Rearrangement is exactly (A.5).

---

## 5. Scope and audit notes

- The theorem is qualitative but uniform. It proves existence of `eta_grid>0`; it does
  not compute it.
- The proof explicitly avoids the false atomic-mass semicontinuity step recorded in
  `target_c_atomic_mantel_uniform_gap_regression_2026-09-12.md`.
- The only diagonal is over **finite sources with preselected shrinking atom windows**;
  their counts and crossing deficits are carried directly into the robust-grid theorem.
- All train geometry remains on the nonisolated positive-contact core. Contact-isolated
  source points remain in the full source and are untouched.
- No outer-detour hypothesis is used.
- This strengthens the all-regime Type-II structural floor but does not yet eliminate
  every Type-II regime or the inactive-container branch.

**Disposition:** proof-only all-regime structural strengthening. C-II remains open.
