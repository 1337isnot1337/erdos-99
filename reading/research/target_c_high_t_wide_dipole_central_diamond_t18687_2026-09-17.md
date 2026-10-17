> Generated reading edition · [exact source](../../research/target_c_high_t_wide_dipole_central_diamond_t18687_2026-09-17.md) · source SHA-256 `687f6080a545f36c9be25bc99e7d86a41ed905b9abbe5c34acb861a51dbb347b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "22b5f9d5759a86074f490fd3e5bb6525a033ea23", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_wide_dipole_central_diamond_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "caf762dec253cdbc8b159d0e23832b09a180e49d2b9279b9880c84fe0a3e30f1"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — every fixed-angle antipodal dipole contains one common macroscopic central disk

**Date:** 2026-09-17  
**Status:** proof-only high-`t` geometric strengthening; no canonical promotion claimed  
**Scope:** the `rho`-wide exact-antipodal side of the parameterized high-`t` robust fork, for any fixed `rho>0`  
**Dependencies:** parameterized robust antipodal-dipole theorem; canonical full-source circumradius/midpoint theorem FS.1/FS.6; convex diameter-thrackle property  
**Certificate:** `research/verify_target_c_high_t_wide_dipole_central_diamond_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The robust-angle theorem forces, at every `rho`-wide exact-antipodal interface, two vertex-disjoint actual diameter chords of length `D` whose projective crossing angle is at least `rho`.  The full-source geometry theorem independently puts the midpoint of **every** actual diameter chord inside one `O(D^(3/4))` ball about the source circumcenter.

Together these facts give a stronger geometric normal form.

Let

```math
\eta_0:=3^{1/4}\sqrt D,
\qquad
L_D:=\sqrt{D\eta_0+\eta_0^2}=O(D^{3/4}),
\tag{CD.1}
```

and let `o` be the canonical full-source circumcenter.  Fix any constant

```math
0<\rho\le {\pi\over2}.
\tag{CD.2}
```

For every `rho`-wide exact-antipodal blocker pair `e_1,e_2`, write `Q(e_1,e_2)` for the convex hull of their four endpoints.  Then, for all sufficiently large `D`,

```math
\boxed{
B\!\left(o,
{D\over2}\sin{\rho\over2}-L_D
\right)
\subset Q(e_1,e_2).
}
\tag{CD.3}
```

In particular each tagged dipole quadrilateral contains the **same** central disk of radius

```math
\left({1\over2}\sin{\rho\over2}-o(1)\right)D.
\tag{CD.4}
```

Its two diameter diagonals cross inside the common sublinear central ball

```math
\boxed{
|p(e_1,e_2)-o|
<\left(1+{2\over\sin\rho}\right)L_D
=O_\rho(D^{3/4})=o(D),
}
\tag{CD.5}
```

and its area satisfies

```math
\boxed{
\operatorname{area}Q(e_1,e_2)
={D^2\over2}\sin\eta
\ge {D^2\over2}\sin\rho,
}
\tag{CD.6}
```

where `eta` is the actual projective angle between the two diameter chords.

Thus a positive-density wide-antipodal branch cannot consist of remote or skinny local crossings.  It consists of linearly many tagged four-point diameter quadrilaterals, all of which contain one common fixed-fraction central disk and whose tagged diagonal intersections are all `o(D)` from the same circumcenter.

---

## 1. Midpoint localization gives a common centered four-vertex approximation

Take the two actual diameter chords and orient them so

```math
y_j-x_j=Dv_j,
\qquad |v_j|=1,
\qquad j=1,2,
\tag{CD.7}
```

with ordinary angle

```math
\eta:=\angle(v_1,v_2)
=d_{\mathbb{RP}^1}([e_1],[e_2])
\in[\rho,\pi/2].
\tag{CD.8}
```

Let

```math
m_j={x_j+y_j\over2}.
\tag{CD.9}
```

Canonical FS.6 gives, simultaneously for every actual diameter chord,

```math
\boxed{|m_j-o|<L_D.}
\tag{CD.10}
```

Therefore

```math
x_j=o-{D\over2}v_j+q_j,
\qquad
y_j=o+{D\over2}v_j+q_j,
\qquad |q_j|<L_D.
\tag{CD.11}
```

Define the centered ideal diamond

```math
Q_0:=\operatorname{conv}
\left\{
 o\pm{D\over2}v_1,
 o\pm{D\over2}v_2
\right\}.
\tag{CD.12}
```

Every one of the four actual vertices of `Q=Q(e_1,e_2)` is within `L_D` of its corresponding ideal vertex.

---

## 2. The ideal diamond has a fixed-fraction inradius

Put `R=D/2`.  Since `eta<=pi/2`, the four ideal vertices occur around `o` with successive angular gaps

```math
\eta,\ \pi-\eta,\ \eta,\ \pi-\eta.
```

The distance from `o` to the chord joining two radius-`R` points separated by an angle `theta` is `R cos(theta/2)`.  Hence the two alternating side distances of `Q_0` are

```math
R\cos{\eta\over2},
\qquad
R\sin{\eta\over2}.
\tag{CD.13}
```

The smaller is the second one, so

```math
\boxed{
B\!\left(o,{D\over2}\sin{\eta\over2}\right)
\subset Q_0.
}
\tag{CD.14}
```

Because `eta>=rho`,

```math
{D\over2}\sin{\eta\over2}
\ge{D\over2}\sin{\rho\over2}.
\tag{CD.15}
```

---

## 3. Vertex perturbations by `L_D` preserve a central disk

For a unit vector `z`, write `h_K(z)` for the support function of a compact convex set `K`, measured relative to the origin `o`.

Each actual vertex is obtained from its corresponding ideal vertex by a displacement of norm `<L_D`.  Therefore, for every unit `z`,

```math
\boxed{
h_Q(z)>h_{Q_0}(z)-L_D.}
\tag{CD.16}
```

Equation (CD.14) says

```math
h_{Q_0}(z)
\ge {D\over2}\sin{\eta\over2}
\tag{CD.17}
```

for every unit `z`.  Thus

```math
h_Q(z)>
{D\over2}\sin{\eta\over2}-L_D
\ge
{D\over2}\sin{\rho\over2}-L_D.
\tag{CD.18}
```

The support-function half-space representation of a convex body now gives (CD.3).

Since

```math
{L_D\over D}=O(D^{-1/4})\longrightarrow0,
\tag{CD.19}
```

the radius in (CD.3) is positive for all sufficiently large `D` and has asymptotic form (CD.4).

This is stronger than midpoint localization of the two diagonals separately: the complete four-endpoint quadrilateral contains a common macroscopic neighborhood of the global circumcenter.

---

## 4. The tagged diagonal crossing is itself central

Let `p` be the intersection of the two diameter lines.  Since the blocker edges are vertex-disjoint actual diameter chords, the convex-thrackle property makes them cross in their interiors, so this line intersection is also the diagonal intersection of `Q`.

Write

```math
p=m_1+t v_1=m_2+s v_2.
\tag{CD.20}
```

Taking the planar scalar cross product with `v_2` gives

```math
t(v_1\times v_2)
=(m_2-m_1)\times v_2.
\tag{CD.21}
```

Thus, using (CD.10) and `|v_1 x v_2|=sin eta`,

```math
|t|
\le {|m_2-m_1|\over\sin\eta}
<{2L_D\over\sin\eta}
\le{2L_D\over\sin\rho}.
\tag{CD.22}
```

Consequently

```math
|p-o|
\le|m_1-o|+|t|
<\left(1+{2\over\sin\rho}\right)L_D,
```

which proves (CD.5).

For fixed `rho`, this is `o(D)`.  The fixed-angle theorem therefore converts the previously uncontrolled intersection location of a narrow crossing pair into one common central crossing zone.

---

## 5. Exact macroscopic quadrilateral area

For any convex quadrilateral, the area is one half the product of its diagonal lengths times the sine of the angle between them.  Here both diagonals are actual diameter edges of length `D`, so

```math
\operatorname{area}Q
={1\over2}D\,D\sin\eta.
\tag{CD.23}
```

Using `eta>=rho` gives (CD.6).

This identity is exact and does not use the near-circle approximation.

---

## 6. Endpoint separation corollary

Equation (CD.11) also gives a direct metric version.  With the acute orientation in (CD.8),

```math
|x_2-x_1|
\ge D\sin{\eta\over2}-2L_D,
\qquad
|y_2-y_1|
\ge D\sin{\eta\over2}-2L_D,
\tag{CD.24}
```

while the crossed pairings satisfy

```math
|y_2-x_1|,\ |x_2-y_1|
\ge D\cos{\eta\over2}-2L_D.
\tag{CD.25}
```

Since `eta in [rho,pi/2]`, every distance between an endpoint of `e_1` and an endpoint of `e_2` is at least

```math
\boxed{
D\sin{\rho\over2}-2L_D
=
(\sin(\rho/2)-o(1))D.
}
\tag{CD.26}
```

Thus the four endpoints of a wide dipole are not merely distinct; they are mutually macroscopically separated across the two diagonal pairs.

---

## 7. Consequence for the parameterized robust fork

If the `rho`-wide exact-antipodal side wins the parameterized robust fork, then more than

```math
{c_0-6\rho\over2}D-o(D)
\tag{CD.27}
```

interfaces carry quadrilaterals satisfying (CD.3)--(CD.6), all with respect to the same circumcenter `o` and the same radius scale `L_D`.

After the existing diameter-degree conflict extraction, at least

```math
\left(
{c_0-6\rho\over32\,3^{1/8}}-o(1)
\right)D^{1/4}
\tag{CD.28}
```

of these tagged quadrilaterals can be chosen with mutually disjoint endpoint sets.  Every one still contains the same disk (CD.3), and every tagged diagonal intersection lies in the same central ball (CD.5).

So the wide-EA branch now has the simultaneous normal form

```text
positive linear density of tagged exact-antipodal interfaces
+
two actual diameter diagonals per tag, crossing at angle >= rho
+
every tagged four-endpoint hull contains one common radius-Theta_rho(D) disk
+
every tagged diagonal intersection lies in one O_rho(D^(3/4)) central ball
+
all cross-chord endpoint distances are Theta_rho(D)
+
an Omega_rho(D^(1/4)) endpoint-disjoint tagged subfamily survives.
```

A regular-shell style regression can still realize many central diameter crossings, so this is not by itself a contradiction.  What is new is that the **same interface tags that arise from distinct one-sided births now carry macroscopic central diamonds**.  The next useful step is to compare those birth tags with the ordered high-`t` train rectangle; a closure must use that train/order information rather than centrality alone.

No C-II or Level-I closure is claimed.

**Disposition:** upgraded every fixed-angle exact-antipodal blocker pair to a common-center macroscopic diamond with a centrally localized tagged crossing, exact area floor, and macroscopic endpoint separation. C-II and Level I remain open.
