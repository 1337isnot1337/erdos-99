> Generated reading edition · [exact source](../../research/target_c_two_leaf_orbit_chamber_propagation_2026-09-14.md) · source SHA-256 `076e968e371383b4b914a48d2a3de4e2dd582f11a5f3023fe28488373a899b9e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "43c94ee487043aef2e00a979bc8be670ae34cc64", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_two_leaf_orbit_chamber_propagation_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "dc2805994869dda8f89196c59e898dfdd31e57890f661d424df5261915583e20"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — propagate the two-leaf atomic gap through §171 and the chamber ledger

**Date:** 2026-09-14  
**Repository base:** `d4154841` on `research/c2-gluing-sol-20260914`  
**Target:** Target C-II, canonical full-core Type-II branch  
**Claim class:** proof-only propagation from TL69 through audited-working §171 and exact planar ledgers

## LEVEL I STATUS

`STILL OPEN`

The two-leaf missing-budget theorem gives the stronger proof-only train gap

$$
g:=0.000698,
\qquad
{T-q/2\over D}\ge 2\sqrt{\Delta_2}+g-o(1),
\qquad
\Delta_2={\pi\over2\sqrt3}.
\tag{PC.1}
$$

This note reruns the audited §171 one-variable orbit/detour envelope with this input and then propagates the resulting `q-k` floor through the exact exceptional-face and inactive-chamber identities. The propagation uses the exact relation between `H_D`, `J_D`, and `q-k`; it does not lose a factor by reverting to the older coarse inequality `H_D>=3J_D/5`.

---

## 1. §171 with `g=0.000698`

Put

$$
C_{146}:={4\over9}(\pi+\sqrt{\Delta_2}).
$$

Audited §171 proves that any Type-II subsequential limit

$$
t=\lim {q-k\over D},
\qquad
\delta=\lim {b-P_F\over D}\ge0
$$

must satisfy

$$
F_t(\delta):=
10t-5\pi-5\delta
+\bigl(81(\pi+\delta)^2\delta\bigr)^{1/3}
-{8\Delta_2\over {9t\over2}-2\pi-2\delta}
\ge0,
\tag{PC.2}
$$

with feasible detour interval

$$
0\le\delta\le
{{9\over2}(t-C_{146})-g\over2}.
\tag{PC.3}
$$

Set

$$
\varepsilon_{69}:=0.0014334,
\qquad
t_{69}:=C_{146}+\varepsilon_{69}.
\tag{PC.4}
$$

At the right endpoint of (PC.3),

$$
\delta_{69}=
{{9\over2}\varepsilon_{69}-g\over2}
=0.00287615.
\tag{PC.5}
$$

The exact-rational certificate `verify_target_c_two_leaf_orbit_chamber_propagation.py` proves

$$
1.820946937951019<t_{69}<1.820946937995464,
\tag{PC.6}
$$

$$
F_{t_{69}}(\delta_{69})<-5.0\times10^{-5},
\tag{PC.7}
$$

and

$$
\partial_\delta F_{t_{69}}(\delta)>142
\qquad(0<\delta\le\delta_{69}).
\tag{PC.8}
$$

Audited §171 also proves strict monotonicity in `t`. Hence no feasible Type-II limit can have `t<=t_69`, and therefore

$$
\boxed{
\liminf {q-k\over D}
\ge t_{69}>1.82094693795.
}
\tag{PC.9}
$$

A high-precision non-load-bearing solve puts the unchanged envelope root at approximately

$$
\varepsilon_*=0.001433551478348,
$$

so the safe decimal in (PC.4) retains a visible sign margin.

---

## 2. Stronger exceptional-face floor

The exact train ledger is

$$
T=q+2f-k.
\tag{PC.10}
$$

Since `q<=P_F` and `k>=0`,

$$
T-{q\over2}
={q\over2}+2f-k
\le {P_F\over2}+2f.
$$

Full-core Type II has `P_F/D->pi`. Combining with (PC.1) gives

$$
\boxed{
\liminf {f\over D}
\ge f_{69}:=\sqrt{\Delta_2}-{\pi\over4}+{g\over2}
=0.167263643466509\ldots .
}
\tag{PC.11}
$$

This improves the AG42 value by `0.000139D` at first order. In particular `Q>=f` and the global exceptional-face perimeter obeys

$$
\liminf {Q+4f\over D}\ge5f_{69}
=0.836318217332545\ldots .
\tag{PC.12}
$$

---

## 3. Endpoint/interface floor

Define

$$
J_D:=(b-P_F)+(Q+4f).
\tag{PC.13}
$$

The stopped-train handshake gives the exact identity

$$
J_D=2T-P_F.
\tag{PC.14}
$$

Write

$$
C_{69}:=2\sqrt{\Delta_2}+g.
$$

Then

$$
2T=q+2(T-q/2)
$$

and `q>=q-k`, so (PC.1), (PC.9), and `P_F/D->pi` give

$$
\boxed{
\liminf {J_D\over D}
\ge j_{69}:=t_{69}+2C_{69}-\pi
=2.490001511845481\ldots .
}
\tag{PC.15}
$$

The increase over the AG42/§171 value `2.489387211845480...` is about `0.0006143D`.

---

## 4. Exact `H_D` propagation

Define

$$
H_D:=(b-P_F)+(Q+2f).
\tag{PC.16}
$$

The outer ledger is

$$
b+Q=2(q-k).
\tag{PC.17}
$$

Using (PC.13),

$$
J_D=2(q-k)+4f-P_F.
$$

Hence

$$
2f={J_D\over2}-(q-k)+{P_F\over2},
$$

and therefore the exact identity

$$
\boxed{
H_D={J_D\over2}+(q-k)-{P_F\over2}.
}
\tag{PC.18}
$$

This is stronger for the present constants than discarding correlation via `H_D>=3J_D/5`. Thus

$$
\boxed{
\liminf {H_D\over D}
\ge h_{69}:={j_{69}\over2}+t_{69}-{\pi\over2}
=1.495151367107289\ldots .
}
\tag{PC.19}
$$

---

## 5. Population, chamber-area, and rhombus-deficit consequences

The exact planar population identity is

$$
m-R_4={P_F+H_D\over2}+1.
\tag{PC.20}
$$

Therefore

$$
\boxed{
\liminf {m-R_4\over D}
\ge {\pi\over2}+{h_{69}\over2}
=2.318372010348541\ldots .
}
\tag{PC.21}
$$

Canonical Section 85 gives, with

$$
a_0={\sqrt3\over2},
\qquad
c_0={\sqrt3\over4},
$$

$$
A_{ch}-a_0Z_{ch}\ge c_0H_D.
$$

Hence

$$
\boxed{
\liminf {A_{ch}-a_0Z_{ch}\over D}
\ge \beta_{69}:=c_0h_{69}
=0.647419533208972\ldots .
}
\tag{PC.22}
$$

The full-source Oler count bound and (PC.21) similarly give

$$
\boxed{
\liminf {\Delta_2D^2-R_4\over D}
\ge \gamma_{69}:={h_{69}\over2}
=0.747575683553644\ldots .
}
\tag{PC.23}
$$

and `a_0 gamma_69=beta_69`.

---

## 6. Chamber slack and genuine residual remain different currencies

The exact chamber-interface cancellation theorem on this branch gives

$$
\Sigma_{ch}=J_D+a+L_{add}+R_F,
\qquad
a,L_{add},R_F\ge0.
\tag{PC.24}
$$

Consequently the correct raw chamber-slack floor is simply

$$
\boxed{
\liminf {\Sigma_{ch}\over D}
\ge j_{69}=2.490001511845481\ldots .
}
\tag{PC.25}
$$

This is mandatory boundary complexity, not fixed-wall spare. Section 85 still gives only `R_F>=0`; the stronger train constant does not manufacture a positive residual margin.

On the upper side, the residual-budget theorem gives

$$
R_F+\Sigma_{ext}<{P_K\over2}+P_F-q.
$$

Using `q>=q-k`, Cauchy's perimeter bounds, and (PC.9),

$$
\boxed{
\limsup {R_F+\Sigma_{ext}\over D}
\le {3\pi\over2}-t_{69}
=2.891442042405245\ldots .
}
\tag{PC.26}
$$

Adding the existing coarse loaded-rhombus allowance gives the joint-puncture coefficient

$$
3.863454192162531\ldots,
\tag{PC.27}
$$

still far from a numerical contradiction.

---

## 7. Research effect

The new two-leaf train theorem has therefore survived the full scalar propagation:

```text
atomic train gain              0.000698
q-k                            >= 1.82094693795 D
bounded exceptional faces f   >= 0.16726364347 D
J interface                    >= 2.49000151185 D
H correlated defect            >= 1.49515136711 D
chamber area surplus           >= 0.64741953321 D
rhombus count deficit          >= 0.74757568355 D
corrected residual upper cap   <= 2.89144204241 D
```

There is no scalar contradiction. The remaining gate is structural. The low-`Q-f` branch has a macroscopic third direction by the global pentagon two-window theorem, while the low-`R_F`, low-`Q-f` corner is forced toward the near-flat pentagonal trapezoid endpoint. The next useful attack must couple those local pentagonal teeth or the third train direction to mixed rigidity/diameter bracing; further decimal optimization of the chamber ledger will not close C-II.

**Disposition:** proof-only propagation. C-II and Level I remain open.
