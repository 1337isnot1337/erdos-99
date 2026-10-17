> Generated reading edition · [exact source](../../research/target_c_support6_pentagon_adjacent_lower_h5_p1_exclusion_2026-09-19.md) · source SHA-256 `b2c05a32d8716ea875211f6edf768fb9a14c1bd9e5f888130e204cc267bb7c4a`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c2333d76d835a8e88c366dec973a2fb7c39a68ae", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_pentagon_adjacent_lower_h5_p1_exclusion_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0bffb24644c8f6ae000a13a997ffe62bfe472bc437fd5b2e368dcf886a9b39e1"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — an adjacent-turn lower bound excludes the `P1` `H(3,3)` support-six signature

**Date:** 2026-09-19  
**Status:** proof-only structural strengthening; theorem-state authority unchanged  
**Scope:** strict convex equilateral force pentagons in the current noncollapsed support-six reciprocal `H5` branch  
**Depends on:** the existing one-turn bound `delta_i<2pi/3`; the existing two-turn upper bound `delta_i+delta_{i+1}<pi`; `target_c_support6_reciprocal_h5_translation_surface_signatures_2026-09-18.md`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The physical force pentagons satisfy a stronger local inequality than has been used so far. If

```math
0<\delta_0,\ldots,\delta_4<\pi
```

are the consecutive exterior turns of a strict convex equilateral pentagon whose side vectors sum to zero, and the already proved source-separation bound gives

```math
\delta_i<\frac{2\pi}{3},
```

then in fact every adjacent pair satisfies

```math
\boxed{
\frac{2\pi}{3}<\delta_i+\delta_{i+1}<\pi.
}
\tag{0.1}
```

The upper inequality is the existing closed-pentagon two-turn lemma. The new lower inequality follows directly from closure and the one-turn bound.

Applying (0.1) to the `P1` translation-surface signature

```math
(m_0,m_1,m_2,m_3,m_4)=(4,1,1,1,4)
```

forces the eleven selected physical gaps at the final cone point to sum to more than `11pi/3`, whereas that cone point requires the sum to be exactly `3pi`. Hence

```math
\boxed{
P_1\text{ cannot realize }(4,4,1,1,1),
\quad\text{equivalently }\mathcal H(3,3).
}
\tag{0.2}
```

Thus the five noncollapsed support-six translation-surface signatures from the preceding reduction drop to four:

```math
\boxed{
P_1:\mathcal H(4,2),\qquad
P_2:\mathcal H(6),\qquad
P_3:\mathcal H(4,4)\text{ or }\mathcal H(5,3).
}
\tag{0.3}
```

The collapsed support-six branch is unaffected.

---

## 1. New local lemma: two adjacent exterior turns exceed `2pi/3`

Let the five oriented unit side vectors of a strict convex equilateral pentagon be

```math
u_0,u_1,u_2,u_3,u_4,
\qquad
u_0+u_1+u_2+u_3+u_4=0,
\tag{1.1}
```

in counterclockwise direction order. Let `delta_i` be the turn from `u_i` to `u_{i+1}` cyclically. The current source theorem already gives

```math
0<\delta_i<\frac{2\pi}{3}.
\tag{1.2}
```

We prove

```math
\boxed{\delta_0+\delta_1>\frac{2\pi}{3}.}
\tag{1.3}
```

The other indices follow cyclically.

Assume instead

```math
s:=\delta_0+\delta_1\le\frac{2\pi}{3}.
\tag{1.4}
```

Rotate so that `u_0` has angle zero. Write

```math
\arg u_1=a,
\qquad
\arg u_2=s.
\tag{1.5}
```

Reflecting the picture if necessary, we may assume

```math
0<a\le\frac{s}{2}.
\tag{1.6}
```

Set

```math
S:=u_0+u_1+u_2
 =1+e^{ia}+e^{is}
 =R e^{i\phi}.
\tag{1.7}
```

Because the three vectors lie in an arc of width below `pi`, `R>0` and `0<phi<s`. Moreover

```math
e^{-is/2}S
=2\cos\frac{s}{2}+e^{i(a-s/2)}.
\tag{1.8}
```

The real part in (1.8) is positive and the imaginary part is nonpositive by (1.6), so

```math
0<\phi\le\frac{s}{2}\le\frac\pi3.
\tag{1.9}
```

Let

```math
t:=\frac{\delta_3}{2}\in(0,\pi/2).
\tag{1.10}
```

Since `u_3+u_4=-S` and the angle from `u_3` to `u_4` is `delta_3<pi`, the sum of those two unit vectors points along their angular bisector. Therefore

```math
R=2\cos t,
\qquad
\frac{\arg u_3+\arg u_4}{2}=\phi+\pi.
\tag{1.11}
```

We now compare `R` with the direction `phi`. Writing `S_x=R cos phi` and `S_y=R sin phi`, direct expansion gives

```math
\begin{aligned}
R^2-(S_x+\sqrt3 S_y)
&=8
\cos\frac{a+\pi/3}{2}
\cos\frac{s+\pi/3}{2}
\cos\frac{s-a}{2}.
\end{aligned}
\tag{1.12}
```

Every factor on the right is nonnegative under (1.4)--(1.6). Hence

```math
R^2\ge S_x+\sqrt3 S_y
 =2R\cos\left(\frac\pi3-\phi\right).
\tag{1.13}
```

Dividing by `R>0` and using `R=2 cos t`,

```math
\cos t\ge\cos\left(\frac\pi3-\phi\right).
\tag{1.14}
```

Both angles in (1.14) lie in `[0,pi/2)`, so cosine monotonicity yields

```math
t\le\frac\pi3-\phi.
\tag{1.15}
```

The second identity in (1.11) gives

```math
\arg u_4=\phi+\pi+t.
\tag{1.16}
```

Thus the final cyclic turn back to `u_0` is

```math
\delta_4
=2\pi-(\phi+\pi+t)
=\pi-\phi-t
\ge\frac{2\pi}{3}.
\tag{1.17}
```

This contradicts the strict one-turn bound (1.2). Therefore (1.3) holds. Cyclic relabeling proves the lower half of (0.1).

The proof is exact. It uses no compactness limit, numerical estimate, or reciprocal order-type assumption.

---

## 2. The two `P1` cone equations needed below

Use the `P1` force cycles and vertex classes from the current translation-surface reduction. For the candidate signature

```math
(m_0,m_1,m_2,m_3,m_4)=(4,1,1,1,4),
\tag{2.1}
```

the three-corner all-physical class `C_3` contains the exterior gaps

```math
\delta_{1,1},\quad \delta_{3,3},\quad \delta_{5,2}.
```

Its cone order is one, so

```math
\boxed{
\delta_{1,1}+\delta_{3,3}+\delta_{5,2}=\pi.
}
\tag{2.2}
```

The eleven-corner all-physical class `C_4` contains

```math
\begin{aligned}
&\delta_{1,2};\\
&\delta_{2,1},\delta_{2,2},\delta_{2,3};\\
&\delta_{3,2};\\
&\delta_{4,1},\delta_{4,2};\\
&\delta_{5,1},\delta_{5,3};\\
&\delta_{6,2},\delta_{6,3}.
\end{aligned}
\tag{2.3}
```

Its cone order is four. Since the sum of the `N` exterior gaps feeding a cone point of order `m` is `(N-2m)pi`, (2.3) must sum to

```math
\boxed{3\pi.}
\tag{2.4}
```

---

## 3. The new lower bound forces the `C_4` sum above `11pi/3`

The existing upper two-turn inequality on face `P_2` gives

```math
\delta_{2,0}+\delta_{2,4}<\pi.
```

Since all five gaps of `P_2` sum to `2pi`,

```math
\boxed{
\delta_{2,1}+\delta_{2,2}+\delta_{2,3}>\pi.
}
\tag{3.1}
```

Similarly, on `P_5`,

```math
\delta_{5,0}+\delta_{5,4}<\pi
```

implies

```math
\boxed{
\delta_{5,1}+\delta_{5,3}>\pi-\delta_{5,2}.
}
\tag{3.2}
```

Apply the new lower two-turn inequality (0.1) to faces `P_1` and `P_3`:

```math
\delta_{1,1}+\delta_{1,2}>\frac{2\pi}{3},
\qquad
\delta_{3,2}+\delta_{3,3}>\frac{2\pi}{3}.
\tag{3.3}
```

Adding (3.3) and eliminating `delta_11+delta_33` with (2.2),

```math
\boxed{
\delta_{1,2}+\delta_{3,2}
>\frac\pi3+\delta_{5,2}.
}
\tag{3.4}
```

The same lower inequality on `P_4` and `P_6` gives

```math
\boxed{
\delta_{4,1}+\delta_{4,2}>\frac{2\pi}{3},
\qquad
\delta_{6,2}+\delta_{6,3}>\frac{2\pi}{3}.
}
\tag{3.5}
```

Now sum the six groups in (2.3), using (3.1), (3.2), (3.4), and (3.5):

```math
\begin{aligned}
\sum_{C_4}\delta
&>
\left(\frac\pi3+\delta_{5,2}\right)
+\pi
+\frac{2\pi}{3}
+\left(\pi-\delta_{5,2}\right)
+\frac{2\pi}{3}\\
&=\boxed{\frac{11\pi}{3}}.
\end{aligned}
\tag{3.6}
```

But (2.4) requires the same sum to equal `3pi`. Contradiction.

Therefore the `P1` signature `(4,1,1,1,4)` is impossible.

---

## 4. Updated noncollapsed support-six endpoint

The previous surface-signature reduction left five possibilities. The present exclusion removes exactly the `P1` `H(3,3)` branch. The remaining noncollapsed candidates are

```math
\boxed{
\begin{array}{c|c|c}
\text{orbit}&g&\text{remaining cone orders}\\ \hline
P_1&4&(5,3,1,1,1)\\
P_2&4&(7,1,1,1,1)\\
P_3&5&(5,5,1)\text{ or }(6,4,1).
\end{array}}
\tag{4.1}
```

Equivalently, only

```math
\boxed{\mathcal H(4,2),\ \mathcal H(6),\ \mathcal H(4,4),\ \mathcal H(5,3)}
\tag{4.2}
```

remain on the uniform noncollapsed `H5` side.

This still does not exclude `P1`, `P2`, or `P3` as sign/order orbits. In particular, the stronger local inequality does not by itself contradict the four signatures in (4.2). Their elimination requires additional metric information, most naturally the full shared-edge unit-force equilibrium / reciprocal integrability constraints.

The collapsed support-six branch remains locally feasible and is untouched by this argument.

No theorem-state file is changed.

**Disposition:** proved the strict adjacent-turn lower bound `delta_i+delta_{i+1}>2pi/3` for every current physical force pentagon and used it to eliminate the `P1` `H(3,3)` translation-surface signature. C-II remains open.
