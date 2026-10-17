> Generated reading edition · [exact source](../../research/target_c_two_leaf_outer_energy_exclusion_t184364_hostile_audit_2026-09-15.md) · source SHA-256 `12dbc31843d077ae3df7e5e12943c33f7a4859114df7c70c74895209e606e725`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bb2069c0398a0f0142acc734a058847f45630dca", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_two_leaf_outer_energy_exclusion_t184364_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4f64a87007386f9a5f58135235f28cb3769b33a4bac0526de8fad187deb7d8e2"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — two-leaf outer-energy exclusion through `t=1.84364`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_two_leaf_outer_energy_exclusion_t184364_2026-09-15.md`
- `research/verify_target_c_two_leaf_outer_energy_exclusion_t184364.py`
- hostile-audited exclusion through `t=1.84362`
- `research/target_c_low_energy_oo_cross_phase_scope_repair_2026-09-15.md`
- hostile-audited strong physical center/leaf pair and phase-star capacity theorems

**Disposition:** **PASS at the stated proof-only full-core/no-macroscopic-container Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate raises the hostile-audited two-leaf exclusion from `1.84362` to `1.84364`. The final outer-energy contradiction still has macroscopic room, about `0.00155D`. The dangerous points are instead the small scalar localization margins and one changed retained-mass boundary case: at the new rounded endpoint the formal energy boundary `h_*` lies slightly **above** the localized residual interval. This audit checks that case explicitly and also rechecks the low-center capacity monotonicity rather than assuming an endpoint test controls the interval.

---

## 1. The repaired cross-phase theorem supplies exactly the implication used downstream

The old cross-phase O--O note had an over-narrow branch-selection argument. The committed scope repair replaces it and proves, at the full-core Type-II near-disk scope,

```math
\boxed{
\tau,\sigma\text{ noncrossing and in phases separated by }\pi/3
\Longrightarrow
 e_\tau+e_\sigma\ge2-\sqrt3-o(1).
}
\tag{HA.1}
```

The `1.84364` candidate uses only (HA.1), not the discarded path-length comparison and not any stronger pointwise threshold statement. Every good cross-leaf pair shares a center neighbor; triangle-freeness makes the pair noncrossing. Thus the repaired theorem applies to the full weighted product exactly as it does in the hostile-audited `1.84362` theorem.

**Verdict:** PASS.

---

## 2. Residual localization to `h<0.000325` is outward-safe

At

```math
T=1.84364,
\qquad
H=0.000325,
\qquad
x=0,
```

the exact certificate proves

```math
F(A_H)-\delta_H
>3.95\times10^{-7}.
```

This margin is small, so derivative direction matters. The candidate uses the same residual-coupled survivor function as the hostile-audited parent. On the present box the exact uniform estimates remain

```math
Q_x<-2.7,
\qquad
Q_h<-2.5.
```

Thus `x=0,h=H` is the most favorable point among all `h>=H` in the relevant feasible triangle; its contradiction excludes the whole region. No endpoint equality is used.

Hence every survivor with `t<=1.84364` satisfies

```math
0\le h<0.000325-o(1).
```

**Verdict:** PASS.

---

## 3. Dominant mass and crossing bounds have explicit outward margins

The proof uses

```math
W<1.912658,
\qquad
E_{dom}>0.90689964.
```

The certificate checks

```math
C_{707}+0.000325<1.912658
```

with strict outward algebraic enclosures, and

```math
\Delta_2-{(1.05\cdot0.000325)^2\over4}>0.90689964.
```

The latter has several times the precision needed for subsequent capacity estimates. The complete detour ceiling is bounded outward by

```math
\delta<0.05043104.
```

**Verdict:** PASS.

---

## 4. The retained-mass proof correctly handles `h_*>H`

This is the main change from the hostile-audited `1.84362` proof.

Assume

```math
z\le Z:=2.2194.
```

Let

```math
h_*:=R_T-2F(Z).
```

The exact certificate gives

```math
0.00032844816225<h_*<0.00032844816226,
```

while the residual localization gives

```math
h<H=0.000325.
```

Thus

```math
\boxed{h_*>H.}
\tag{HA.2}
```

This reverses the simple boundary placement used at `1.84362`, so it must be handled rather than copied.

For fixed `h` on the branch `delta>=F(Z)`, put

```math
\delta={R_T-x-h\over2}.
```

After replacing `z` by the adverse cap `Z`, the retained-survivor excess has `x` derivative

```math
1-
{1-F(Z)+1.05^2h^2\over4(1-\delta)^2}.
\tag{HA.3}
```

The certificate bounds the fraction in (HA.3) strictly below one on `0<=h<=H`, so the derivative is positive. Therefore this branch is maximized at its right endpoint

```math
x=h_*-h,
\qquad
\delta=F(Z).
\tag{HA.4}
```

On the complementary branch `delta<F(Z)`, energy feasibility forces

```math
z\le F^{-1}(\delta)<Z.
```

The hostile-audited survivor function `Q(t,h,x)` applies, and `Q_x<0`. Moving `x` backward to (HA.4) can only increase survivor capacity. Hence **both** branches reduce to the same boundary.

There the capped excess is

```math
B(h)=
Z+{1.05^2h^2\over2(1-F(Z))}
-\pi+{T\over2}+h_*+0.05h.
\tag{HA.5}
```

Its derivative is strictly positive for `h>=0`. Consequently, for the physically allowed `h<=H<h_*`,

```math
B(h)\le B(H)<B(h_*).
```

The proof deliberately uses the still larger extrapolated value `B(h_*)`, for which the exact certificate obtains

```math
B(h_*)<-2.77\times10^{-5}.
```

Thus the extrapolation is in the safe direction and no survivor can satisfy `z<=2.2194`.

**Verdict:** PASS.

---

## 5. Phasewise retained mass `>0.7045D` is certified despite the small margin

For

```math
f(s)=s-2\sin(s/2),
```

the phasewise selected occurrence energy is at least

```math
f(z_C)+f(z_U)+f(z_V).
```

If one phase had retained mass at most

```math
A=0.7045,
```

then, because `A<2.2194/3`, convexity and monotonicity make the cheapest possible split

```math
\left(A,{2.2194-A\over2},{2.2194-A\over2}\right).
```

The exact outward certificate gives

```math
f(A)+2f\!\left({2.2194-A\over2}\right)
-0.05043104
>3.42\times10^{-6}.
```

This is small but strictly positive and uses the full detour ceiling, so no unallocated outer-energy slack can rescue the split.

Therefore

```math
z_C,z_U,z_V>0.7045-o(1).
```

**Verdict:** PASS.

---

## 6. The low-center aggregate capacity has no hidden interior maximum

Assume the larger leaf satisfies

```math
U\ge M=0.528.
```

Put

```math
W_0=1.912658,
\qquad
C_0=W_0-2M=0.856658,
\qquad
K={2\over\sqrt3}.
```

For `M<=C<=C_0`, the strong aggregate phase-star capacity is

```math
\Phi(C)=
C(W_0-C)
-{1\over10}\left(3-{W_0\over C}\right)
\left({W_0+C\over2}-K\right)^2.
\tag{HA.6}
```

Checking only `Phi'(C_0)>0` would be insufficient unless one also rules out an interior maximum. Write

```math
r={W_0+C\over2}-K,
\qquad
q=3-{W_0\over C}.
```

Then

```math
\Phi''(C)
=-2-{1\over10}
\left(
-{2W_0r^2\over C^3}
+{2W_0r\over C^2}
+{q\over2}
\right).
\tag{HA.7}
```

On the whole interval, using the coarse rational bound `K>1.1547`,

```math
0<r<0.229958,
\qquad
q>-0.622459,
\qquad
C\ge0.528.
```

Dropping the positive middle term in (HA.7) gives the lower bound

```math
-{2W_0r^2\over C^3}+{q\over2}>-1.686.
```

Hence

```math
\boxed{\Phi''(C)<-1.8314<0.}
\tag{HA.8}
```

throughout the interval. Therefore `Phi'` decreases with `C`; the exact certificate's positive value at `C_0` implies `Phi'>0` everywhere to its left. Thus the maximum occurs at `C_0`. Its capacity lies more than `0.0063` below `E_0=0.90689964`.

**Verdict:** PASS.

---

## 7. The main center interval stays inside the strong physical-pair branch

Generic center capacity excludes `C>=1.044`. The remaining main interval is

```math
0.856658\le C\le1.044.
```

After the adverse replacements `W->W_0` and `U->M`, the smaller leaf is

```math
V=W_0-C-M,
```

so throughout this interval

```math
0.340658\le V\le0.528.
```

In particular the older safe lower bound `V>0.308` is respected. The adverse strong-branch ratio is

```math
{1.044+0.528-K\over0.528}<0.79034
<\sqrt{20/29}.
```

Since `C<K`, decreasing the leaf mass only decreases this ratio, so the same `1/10` branch applies to `V`.

The parent hostile audit already proves that correlated capacity increases with `W` and decreases with the larger leaf `U` in this sign regime. Thus `W=W_0,U=M` is adverse.

For the resulting one-variable capacity `G(C)`, exact differentiation gives

```math
G''(C)=-2-{4\over10}+{2\over10}{D_*\over C^3}.
```

The committed certificate proves `D_*<2C_0^3`, so

```math
G''(C)<-2
```

throughout the interval. At `c_0=0.931638`, the tangent parabola bound gives

```math
\max G
\le G(c_0)+{G'(c_0)^2\over4}
<0.906887344.
```

The margin below `E_0` exceeds `1.22e-5`.

Therefore

```math
\boxed{U,V<0.528-o(1).}
```

**Verdict:** PASS.

---

## 8. Common-center loss and pair-weight bookkeeping are safe

From the phasewise retained mass and leaf-mass bounds,

```math
P_U,P_V>0.7045-0.528-o(1)=0.1765-o(1).
```

Let `x,y` be the missing center incidences of the two leaves. The hostile-audited correlation gives

```math
\left(1-{0.528\over C}\right)(x+y)
\le C(W-C)-E_0+o(1).
```

Generic capacity forces `C>0.528`, because

```math
0.528(1.912658-0.528)<E_0.
```

A retained O--O train with center degree at most half the center family misses at least `CD/2-o(D)` center trains. Therefore total bad retained pair weight is bounded by

```math
B_{bad}
\le{2[C(W_0-C)-E_0]\over C-0.528}+o(1).
```

The claim `B_bad<0.0365` is equivalent to positivity of a quadratic with leading coefficient two. The exact certificate gives its discriminant

```math
-0.001091558144<0.
```

Thus even charging all bad weight to either single leaf leaves

```math
G_U,G_V>0.1765-0.0365-o(1)=0.14-o(1).
```

**Verdict:** PASS.

---

## 9. Final energy ledger is disjoint and has macroscopic slack

Every good cross-leaf pair shares a center neighbor, hence is noncrossing. By the repaired theorem (HA.1),

```math
e_\tau+e_\sigma\ge2-\sqrt3-o(1).
```

Weighted complete-product averaging therefore gives

```math
E_U+E_V
\ge(2-\sqrt3)\min(G_U,G_V)-o(1).
```

Using `sqrt(3)<1.7321` and `G_U,G_V>0.14-o(1)`,

```math
E_U+E_V>0.037506-o(1).
```

This leaf terminal energy lies on the selected leaf terminal-occurrence supports. The center one-well energy lies on the disjoint center phase window, so the two payments add without double counting:

```math
\delta
>0.037506+f(0.7045)-o(1)
>0.05198494736-o(1).
```

The complete detour ceiling is below `0.05043104+o(1)`. Thus the contradiction margin exceeds

```math
0.0015539D.
```

This is much larger than every earlier localization rounding margin and absorbs the asymptotic source/window errors.

**Verdict:** PASS.

---

## Final disposition

The extension from `1.84362` to `1.84364` introduces two genuine audit obligations: the `h_*>H` retained-mass geometry and low-center monotonicity. Both pass. The cross-phase terminal-energy dependency is valid under the separately committed scope repair.

Therefore the proof-only full-core Type-II strengthening

```math
\boxed{
\liminf {q-k\over D}\ge1.84364
}
```

is certified at the stated scope.

C-II and Level I remain open.
