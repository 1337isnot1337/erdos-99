> Generated reading edition · [exact source](../../../docs/reports/target_c_semicircle_perimeter_interface_defect_2026-09-09.md) · source SHA-256 `5f37aeac6edf2548f50a457074cc56f5fd86d7d326e3d9f19722085235e7289f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3F6CE6727654","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — semicircle carrier perimeter forces linear loaded-interface face defect

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** equality-regime planar face identity / interface localization  
**Target:** TS full-core cap-minimal near-circle branch  
**Depends on:** TS, repaired TD/LC, NBd, NC, UF; planar Euler face count  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

TS proves that in the full-core, cap-minimal equality regime

$$
S/D\to2,
$$

there are two harmonic components `I_1,I_2` with

$$
\delta_i/D\to1,
\qquad
n_i/D^2\to\Delta/2,
$$

whose attachment cells converge to complementary semicircular caps.

This report uses the **actual semicircle perimeter**, rather than the shape-free Eppstein isoperimetric lower bound, to sharpen the internal edge deficit. It then combines the result with UF's global face-defect lower bound.

Let `Q_i` be the total bounded-face degree excess of the internal plane graph `C[I_i]`, and put

$$
Q_{int}:=Q_1+Q_2.
$$

Then

$$
\boxed{
R_I
\ge
\left(\frac\pi2-1-o(1)\right)D
+\frac12Q_{int}.
}
\tag{SI.1}
$$

The exact near-circle boundary budget consequently gives

$$
\boxed{
Q_{int}
\le
(\pi-2+o(1))D.
}
\tag{SI.2}

$$

UF at the full-core endpoint gives

$$
\boxed{
Q
\ge
\left(
\frac\pi5+\frac45\sqrt\Delta-o(1)
\right)D
=(1.3901687762\ldots-o(1))D.
}
\tag{SI.3}

$$

Every bounded face of the full contact graph that is not internal to an unloaded component is incident to a loaded terminal. Therefore, if `Q_B` denotes the total degree excess of bounded faces incident to `B_+`,

$$
Q_B\ge Q-Q_{int}.
$$

Combining SI.2--SI.3 yields the explicit interface obligation

$$
\boxed{
Q_B
\ge
\left[
2-\frac{4\pi}{5}+rac45\sqrt\Delta-o(1)
\right]D
=(0.2485761226\ldots-o(1))D.
}
\tag{SI.4}

$$

Thus the cap-minimal full-core survivor cannot hide all of its linear exceptional-face defect inside the two dense half-disk carriers. A definite linear amount must live on the loaded boundary/interface itself.

---

## 1. Internal convex hulls converge to semicircles

Let

$$
K_i:=\operatorname{conv}(I_i).
$$

C36 gives

$$
K_i\subseteq P_i,
$$

where `P_i` is the attachment cell. TS/repaired TD give

$$
P_i/D\to C_i
$$

for complementary radius-`1/2` semicircular caps `C_1,C_2`.

TS gives

$$
n_i/D^2\to\Delta/2.
$$

Apply Oler to the `n_i` unit-separated vertices inside `K_i`:

$$
a_0(n_i-1)
\le
\operatorname{area}(K_i)
+\frac{a_0}{2}\operatorname{per}(K_i),
\qquad
 a_0=\frac{\sqrt3}{2}.
\tag{1.1}
$$

Since `diam(K_i)<=D+o(D)`, its perimeter is `O(D)`. Divide by `D^2`. Because

$$
a_0\frac\Delta2=\frac\pi8,
$$

we obtain

$$
\liminf\frac{\operatorname{area}(K_i)}{D^2}\ge\frac\pi8.
$$

But `K_i subset P_i` and `area(P_i)/D^2->pi/8`, so

$$
\boxed{
\operatorname{area}(K_i)/D^2\to\pi/8.
}
\tag{1.2}
$$

Now take any Hausdorff-convergent subsequence of `K_i/D`. Its limit is a compact convex subset of `C_i` with the same area `pi/8` as `C_i`, hence equals `C_i`. Therefore the full sequence converges:

$$
\boxed{K_i/D\to C_i}
\tag{1.3}
$$

in Hausdorff distance.

Perimeter is continuous under Hausdorff convergence of planar convex bodies, so

$$
\boxed{
\frac{\operatorname{per}(K_i)}D
\to
1+\frac\pi2.
}
\tag{1.4}

$$

The `1` is the flat diameter edge of the limiting semicircle and `pi/2` is its half-circular arc.

---

## 2. The internal contact outer walk is at least the semicircle perimeter

Let `G_i=C[I_i]`. By definition `I_i` is a connected component of the contact graph after deleting the loaded terminals, so `G_i` is connected.

Let `k_i` be the length of the outer-face boundary walk of `G_i`, counting bridge occurrences with multiplicity. Every graph edge is a unit contact, so the geometric length of this closed outer walk is exactly `k_i`.

Every extreme vertex of `K_i=conv(I_i)` lies on the outer face of the straight-line plane graph `G_i`. Hence the convex hull of the outer-walk image is exactly `K_i`.

The closed-walk convex-hull perimeter lemma used in OP therefore gives

$$
\boxed{k_i\ge\operatorname{per}(K_i).}
\tag{2.1}
$$

Combining with (1.4),

$$
\boxed{
\frac{k_i}D
\ge
1+\frac\pi2-o(1).
}
\tag{2.2}

$$

This is stronger in the present semicircle geometry than Eppstein's shape-free isoperimetric outer-face lower bound.

---

## 3. Exact local face identity

Let `f_i` be the number of bounded faces of `G_i`, and define

$$
Q_i:=
\sum_{F\text{ bounded face of }G_i}
(\deg F-4).
\tag{3.1}
$$

The graph is simple and triangle-free. Bounded face walks therefore have length at least four; bridges may occur only on the outer walk and are counted with multiplicity in `k_i`.

Face-edge incidence gives

$$
2e_i
=k_i+4f_i+Q_i.
\tag{3.2}
$$

Euler for the connected plane graph gives

$$
n_i-e_i+f_i=1.
\tag{3.3}
$$

Eliminating `f_i` yields the exact identity

$$
\boxed{
 e_i
=2n_i-2-rac{k_i+Q_i}{2}.
}
\tag{SI.5}

$$

This is the component-level version of the familiar global triangle-free face ledger.

---

## 4. Exact internal Eppstein slack

ZK defines

$$
r_i:=2n_i-\delta_i-2-e_i.
$$

Insert SI.5:

$$
\boxed{
 r_i
=\frac{k_i+Q_i}{2}-\delta_i.
}
\tag{4.1}

$$

TS gives `delta_i/D->1`, while (2.2) gives `k_i/D>=1+pi/2-o(1)`. Hence

$$
\boxed{
 r_i
\ge
\left(\frac\pi4-\frac12-o(1)\right)D
+\frac{Q_i}{2}.
}
\tag{4.2}

$$

Summing `i=1,2` and discarding all other nonnegative `r_r` gives SI.1:

$$
R_I
\ge
\left(\frac\pi2-1-o(1)\right)D
+\frac{Q_{int}}2.
$$

Numerically,

$$
\frac\pi2-1
=0.5707963268\ldots .
$$

This supersedes TS's weaker shape-free charge

$$
R_I\ge(\pi/\sqrt2-2-o(1))D
=0.2214414690\ldots D.
$$

---

## 5. Attachment contacts receive the same perimeter improvement

The pinned-stress identity is

$$
s_i=e_i+t_i-2n_i-1.
$$

Using SI.5,

$$
\boxed{
 t_i
=3+s_i+\frac{k_i+Q_i}{2}.
}
\tag{5.1}
$$

Therefore

$$
\boxed{
 t_i
\ge
\left(\frac12+\frac\pi4-o(1)\right)D
+\frac{Q_i}{2}+s_i.
}
\tag{5.2}
$$

Even when `Q_i=s_i=0`, each semicircle carrier uses at least

$$
\left(\frac12+\frac\pi4\right)D
=1.2853981634\ldots D
$$

loaded attachment contacts.

Across both carriers,

$$
\boxed{
 t_1+t_2
\ge
\left(1+\frac\pi2-o(1)\right)D
+\frac{Q_{int}}2+s_1+s_2.
}
\tag{5.3}
$$

This is the precise boundary-contact cost of filling two semicircular caps with triangle-free penny graphs.

---

## 6. The exact near-circle boundary budget bounds internal face defect

NC gives `E_BB=o(D)`. NBd gives

$$
S+R_I+s_B+2E_{BB}+3c_I+s_C
=(\pi+o(1))D.
\tag{6.1}
$$

In the cap-minimal branch `S/D->2`. Insert SI.1 and discard the remaining nonnegative currencies:

$$
2D
+\left(\frac\pi2-1-o(1)\right)D
+\frac{Q_{int}}2
\le
(\pi+o(1))D.
$$

Therefore

$$
\boxed{
Q_{int}
\le
(\pi-2+o(1))D.
}
$$

This proves SI.2.

Observe that the same constant `pi-2` appeared earlier as the entire post-TD remainder. SI shows that any internal exceptional-face defect consumes **half a unit of that remainder per unit defect**, on top of the unavoidable semicircle perimeter cost.

---

## 7. Internal bounded faces persist as full contact faces

We need to compare `Q_int` with the global bounded-face defect `Q`.

### Lemma SI.1

Every bounded face of `G_i=C[I_i]` is also a bounded face of the full positive contact graph `C`, with the same boundary walk and degree.

### Proof

Let `F` be a bounded face of `G_i`. Suppose a full-contact edge not belonging to `G_i` entered the interior of `F`.

An edge with one endpoint on the boundary of `F` and the other endpoint outside `I_i` must end at a loaded terminal, because distinct unloaded components have no contact edges between them after deleting `B_+`. Every loaded terminal lies on the force hull outside the interior of `K_i`. A straight segment from a boundary vertex of the bounded face to such an exterior terminal cannot enter the face interior and later leave it without crossing another boundary edge of `G_i`, impossible in a penny-graph embedding.

A vertex of another unloaded component cannot lie strictly inside `F`: that component must have a contact path to its loaded attachments, and such a path would have to cross the boundary cycle/walk of `F`. The same planar obstruction applies.

Thus no full contact vertex or edge subdivides the interior of `F`. It remains a bounded face of `C` with the same degree. `square`

Consequently

$$
\boxed{Q_{int}\le Q.}
\tag{7.1}
$$

Moreover every global bounded face not counted in the internal bounded faces of some unloaded component is incident to at least one loaded terminal: if its boundary contained no loaded vertex, all consecutive boundary vertices would remain connected after deleting `B_+` and hence would belong to one `I_r`, making it an internal face of that component.

Define

$$
Q_B:=
\sum_{\substack{F\text{ bounded face of }C\\F\cap B_+\ne\varnothing}}
(\deg F-4).
\tag{7.2}
$$

Then exactly

$$
\boxed{
Q=Q_{all-int}+Q_B,
}
\tag{7.3}
$$

where `Q_all-int` sums the internal face defects over **all** unloaded components. In particular

$$
\boxed{Q_B\ge Q-Q_{int}.}
\tag{7.4}
$$

The other small components may contribute additional internal defect, so (7.4) is the safe inequality needed below.

---

## 8. UF forces a linear loaded-interface defect

UF gives in the near-circle branch

$$
\frac QD
\ge
\frac\pi5+rac45\sqrt{\Delta-\zeta}-o(1).
$$

At full core `zeta=0`,

$$
\boxed{
\frac QD
\ge
\frac\pi5+rac45\sqrt\Delta-o(1).
}
\tag{8.1}
$$

Subtract SI.2 using (7.4):

$$
\begin{aligned}
\frac{Q_B}{D}
&\ge
\frac\pi5+rac45\sqrt\Delta-(\pi-2)-o(1)\\
&=
2-\frac{4\pi}{5}+rac45\sqrt\Delta-o(1).
\end{aligned}
$$

Thus

$$
\boxed{
Q_B
\ge
(0.2485761226\ldots-o(1))D.
}
$$

This proves SI.4.

---

## 9. New normal form of the cap-minimal full-core branch

The branch now has the following forced structure:

```text
F/D -> disk;
q=(pi+o(1))D;
e_BB=(pi+o(1))D and no nonconsecutive B-B unit chords;
S=(2+o(1))D;
I1,I2 have delta_i=(1+o(1))D;
n_i=(Delta/2+o(1))D^2;
conv(I_i)/D -> complementary semicircular caps;
k_i >= (1+pi/2-o(1))D;
R_I >= (pi/2-1-o(1))D + Q_int/2;
Q_int <= (pi-2+o(1))D;
Q_B >= (0.2485761226-o(1))D.
```

Thus the next obstruction is no longer an arbitrary giant exceptional face. It is a **linear amount of exceptional-face degree excess touching the already almost-saturated loaded unit hull cycle**.

---

## 10. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| internal hulls converge to semicircles | proved | TS population + Oler + cap containment + convex compactness |
| internal outer walk `k_i/D>=1+pi/2` | proved | closed-walk perimeter bound |
| local face identity SI.5 | proved | Euler + exact face-incidence count |
| semicircle `R_I` lower bound SI.1 | proved | SI.5 + `delta_i/D->1` |
| internal faces persist globally | proved | planarity and component/loaded separation |
| `Q_int<=pi-2` | proved in cap-minimal full-core branch | NBd/NC + SI.1 |
| loaded-interface defect `Q_B>=0.248576D` | proved conditional on UF full-core bound | subtract SI.2 from UF |
| Level I | still open | boundary-interface defect may still be carried by long convex faces |

---

## 11. Next target

The remaining interface faces are incident to loaded force-hull terminals that already have two mandatory unit hull-side contacts at all but `o(D)` positions by NC.

A loaded terminal therefore has at most one contact edge entering the harmonic interior. The next exact target is an **interface-face defect versus one-slot boundary theorem**:

> in the two-semicircle cap-minimal geometry, show that a total loaded-interface excess `Q_B>=0.248576D` forces more than the available one-contact-per-loaded-terminal interior incidence, or else forces an `Omega(D)` outer-walk defect, contradicting `x_B=o(D)`.

Unlike earlier face-local area charging, this target uses the loaded degree-three cap and the semicircle interface topology, so the DP near-zero-excess pentagon regression does not directly defeat it.
