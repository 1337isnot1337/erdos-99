> Generated reading edition · [exact source](../../research/target_c_high_t_host_cap_force_pair_separation_t18687_2026-09-17.md) · source SHA-256 `15156cb897b8a3224dda3ac63404fed0c01abd04d0c63ba9c90d5ce645b5e4c6`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cb118e4e371c871368bc11eea914b4b653a46cc3", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_host_cap_force_pair_separation_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "875ec83bbd1c7ff648a14bc1ae4d924371eed69ebc0e82bb73ce4d656eb039ba"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — host transverse margin separates every exact-force pair into opposite macroscopic endpoint caps

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** exact-antipodal interfaces on the selected one-sided coupled high-`t` path through `t=(q-k)/D<=1.8687`  
**Dependencies:** coupled host-margin sharpening; exact-antipodal exact-force pair; common-hub one-sided switching orientation; full-source diameter-midpoint localization; convex diameter-thrackle property  
**Certificate:** `research/verify_target_c_high_t_host_cap_force_pair_separation_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The older shared-endpoint-collapse theorem proved only that `o(D)` exact-antipodal interfaces can realize their two opposite-transverse bars as a diameter star. The later host-margin theorem and the source-wide midpoint bound give a pointwise statement: for all sufficiently large sources, **no exact-antipodal force pair can share an endpoint at all**.

More is true. Orient every switching diameter from its hub-side endpoint toward its birth-side endpoint, as in the global one-sided resultant theorem. If `v_i` is the exact row/reaction axis, then the two force bars have opposite signs of `d dot Jv_i` and each has absolute transverse component at least

```math
c_H-o(1),\qquad c_H=0.453819885927\ldots .
```

The full-source midpoint theorem therefore puts the four endpoints into two opposite row-normal caps at distance

```math
\left({c_H\over2}-o(1)\right)D
=(0.226909942963\ldots-o(1))D
```

from the common circumcenter coordinate. On the birth shore, one force bar starts in the positive cap and the other in the negative cap; on the hub shore the signs reverse. Since the physical birth host arcs are the two opposite support-normal branches, this also makes the exact force pair physically bilateral **without any pair-gap hypothesis or bounded exceptional set**.

---

## Theorem HC — endpoint-cap separation of an exact force pair

Let `i` be an exact-antipodal nonhub interface on one fixed side of the common routing hub. Let

```math
G_i=D(\lambda_i^-d_i^-+\lambda_i^+d_i^+),
\qquad \lambda_i^\pm>0,
\tag{HC.1}
```

be the exact positive two-ray force compression, with the switching directions oriented from the hub-side shore toward the birth-side shore. Let `v_i` be the common row axis, oriented so that the exact reaction is projectively `[v_i]`.

The coupled host-margin theorem gives

```math
|d_i^\pm\cdot Jv_i|\ge c_H-o(1),
\tag{HC.2}
```

and the exact-force theorem chooses the two bars with opposite transverse signs. Relabel so that

```math
d_i^+\cdot Jv_i\ge c_H-o(1),
\qquad
d_i^-\cdot Jv_i\le-c_H+o(1).
\tag{HC.3}
```

Write the corresponding diameter edges as

```math
e_i^+=x_i^+y_i^+,
\qquad e_i^-=x_i^-y_i^-,
\tag{HC.4}
```

where `x_i^\pm` are the birth-side endpoints and `y_i^\pm` the hub-side endpoints, so

```math
d_i^\pm={x_i^\pm-y_i^\pm\over D}.
\tag{HC.5}
```

Let `o` be the common source circumcenter and

```math
h_i(p):=\det(v_i,p-o)=(p-o)\cdot Jv_i.
\tag{HC.6}
```

Then, uniformly over all such interfaces,

```math
\boxed{
 h_i(x_i^+)\ge\left({c_H\over2}-o(1)\right)D,
 \qquad
 h_i(y_i^+)\le-\left({c_H\over2}-o(1)\right)D,
}
\tag{HC.7}
```

and

```math
\boxed{
 h_i(x_i^-)\le-\left({c_H\over2}-o(1)\right)D,
 \qquad
 h_i(y_i^-)\ge\left({c_H\over2}-o(1)\right)D.
}
\tag{HC.8}
```

Consequently, for all sufficiently large `D`:

1. `x_i^+ != x_i^-` and `y_i^+ != y_i^-`;
2. the two force bars have four distinct endpoints;
3. the two actual diameter chords cross;
4. the two birth endpoints lie on opposite physical host subarcs of the layer `R_i`.

Thus every exact-antipodal force cell is a genuine bilateral crossing two-chord cell, with no fixed projective pair-gap assumption.

---

## 1. Midpoint localization gives the four cap inequalities

For either selected diameter bar, let

```math
m_i^\pm={x_i^\pm+y_i^\pm\over2}.
```

The full-source midpoint theorem gives one sourcewise bound

```math
|m_i^\pm-o|\le L_D,
\qquad
L_D=O(D^{3/4})=o(D).
\tag{HC.9}
```

Using (HC.5),

```math
x_i^\pm=m_i^\pm+{D\over2}d_i^\pm,
\qquad
y_i^\pm=m_i^\pm-{D\over2}d_i^\pm.
\tag{HC.10}
```

Apply `h_i`. Since `|h_i(m_i^\pm)|<=L_D`,

```math
h_i(x_i^\pm)
=h_i(m_i^\pm)+{D\over2}(d_i^\pm\cdot Jv_i),
\tag{HC.11}
```

```math
h_i(y_i^\pm)
=h_i(m_i^\pm)-{D\over2}(d_i^\pm\cdot Jv_i).
\tag{HC.12}
```

Substituting (HC.3) and absorbing `L_D=o(D)` into the existing `o(D)` error proves (HC.7)--(HC.8).

The gap between the positive and negative endpoint caps is asymptotically

```math
(c_H-o(1))D
=(0.453819885927\ldots-o(1))D.
\tag{HC.13}
```

This is macroscopic; it does not depend on the projective angle between the two force bars.

---

## 2. Shared endpoints are pointwise impossible

Both selected bars cross the same one-sided interface. Relative to the common hubward train cut, a source vertex has one shore role, so a common endpoint of the two bars would have to be

- the birth-side endpoint of both bars, or
- the hub-side endpoint of both bars.

The first case would force one point to satisfy both inequalities for `x_i^+` and `x_i^-` in (HC.7)--(HC.8); the second would force one point to satisfy both inequalities for `y_i^+` and `y_i^-`. Since the positive and negative caps are disjoint for all sufficiently large `D`, both cases are impossible.

Hence

```math
\boxed{
\{x_i^+,y_i^+\}\cap\{x_i^-,y_i^-\}=\varnothing
}
\tag{HC.14}
```

at every exact-antipodal force interface once `D` is large enough.

This strictly strengthens the earlier global statement `|E_D^{star}|=o(D)`: under the later host-margin input, the star class is eventually empty.

Two vertex-disjoint actual diameter edges of a convex planar source cross, so (HC.14) also gives

```math
\boxed{e_i^+\pitchfork e_i^-}
\tag{HC.15}
```

without first imposing a fixed lower bound on their projective angle.

---

## 3. Opposite transverse signs identify the two physical birth hosts

The midpoint argument is not needed for the birth-side conclusion. The coupled host theorem says that the two physical host arcs are support-normal intervals around the two ideal opposite normals `+Jv_i` and `-Jv_i`, with half-width

```math
\vartheta_H=\arccos c_H<\pi/2.
\tag{HC.16}
```

Every switching diameter direction, oriented toward its birth endpoint, is an exact outward support normal at that birth endpoint. Therefore a birth normal on one host branch has positive `Jv_i` component and a birth normal on the other has negative `Jv_i` component, with magnitude at least `c_H-o(1)`.

The signs in (HC.3) consequently force

```math
\boxed{
x_i^+\in C_i^+,
\qquad x_i^-\in C_i^-
}
\tag{HC.17}
```

after naming the two physical layer-host subarcs by the sign of the `Jv_i` component.

Thus the physical bilateral-birth conclusion is pointwise. The older `O_\rho(1)` exceptional-set deletion used for fixed-gap force pairs is unnecessary once the coupled host-normal theorem is available.

---

## 4. Immediate consequences for the current growing corridor

Every internal interface of the current exact-phase force corridor already carries an exact positive force pair and the host margin (HC.2). Theorem HC therefore upgrades the whole corridor simultaneously:

```text
at every force-loaded separator, with no pair-gap hypothesis:
  one birth endpoint lies on each physical host;
  one hub endpoint lies in each opposite row-normal cap;
  all four endpoints are distinct;
  the two diameter bars cross;
  the exact positive KKT reaction identity is retained.
```

The fixed or shrinking pair-gap parameter remains useful only for quantitative **diamond width**, central-disk radius, and upper bounds on compressed two-ray coefficients. It is no longer needed to establish bilateral birth, internal vertex-disjointness, or crossing.

This distinction matters for later diagonal arguments: one may use a gap-free exact-force corridor when only topology, host lane, or the fixed individual transverse slope is needed, and pay a narrow-pair deletion only when an actual quantitative diamond aperture is used.

---

## 5. Frontier effect

The exact-antipodal branch no longer has a local star escape, even on a sparse or growing selected corridor. Its elementary force cell has the rigid form

```math
\boxed{
C_i^+\longleftrightarrow C_i^-
\quad\text{through two crossing diameter bars with opposite cap orientation.}
}
```

The remaining obstruction is global: such bilateral crossing cells can still be arranged in an ordered diameter thrackle near a disk. A closing theorem must use their interface order and common train grid, or the exact KKT force data, rather than attempting another local star/collision exclusion.

**Disposition:** proved pointwise four-cap separation, eventual emptiness of the exact-antipodal shared-endpoint class, and gap-free physical bilateral birth for every exact force pair. C-II and Level I remain open.
