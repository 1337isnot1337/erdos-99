# Target C-II — ground projection cuts support-seven `3+4` sign patterns

**Date:** 2026-09-19  
**Status:** exact local sign-pattern reduction for ground-on-hull support-seven branches; theorem-state authority unchanged  
**Scope:** seven raw ground rays in an open semicircle; with the sharper `H6` cone width used where stated  
**Certificate:** `research/verify_target_c_ground_semicircle_pairing_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Let the seven raw ground rays occur in angular order

\[
\theta_1<\theta_2<\cdots<\theta_7<\theta_1+\pi,
\qquad
u_i=(\cos\theta_i,\sin\theta_i).
\]

At the support-seven endpoint, `H6` already forces a `3+4` ground sign split. The same split is the only one left in the current convex `H8` endpoint, and it is a relevant split in ground-on-hull `H7a` casework.

There are two exact projection mechanisms below. The first excludes fourteen of the `35` possible minority patterns on any open semicircle. The second uses the stronger `H6` width `phi<2pi/3` and excludes eight more patterns not caught by the first. Thus `H6` drops from `35` raw `3+4` ground patterns to only `13`.

---

## 1. Open-semicircle pairing lemma

Let `P` be the size-three sign class and let `M` be its four-element complement. Ground equilibrium is

\[
\sum_{n\in P}u_n=\sum_{m\in M}u_m.
\tag{1}
\]

Suppose there is a pivot `p in M` and a bijection

\[
\sigma:M\setminus\{p\}\to P
\]

such that for every `m in M\setminus{p}`, the index `m` lies strictly between `p` and `sigma(m)`. Equivalently, either

\[
p<m<\sigma(m)
\]

or

\[
\sigma(m)<m<p.
\tag{2}
\]

Rearrange (1) as

\[
0=u_p+\sum_{m\in M\setminus\{p\}}
\bigl(u_m-u_{\sigma(m)}\bigr).
\tag{3}
\]

Dot with `u_p`. Because each matched majority ray lies on the same side of `p` as its minority partner but is closer to `p`,

\[
0<|\theta_m-\theta_p|
<|\theta_{\sigma(m)}-\theta_p|<\pi.
\]

Cosine is strictly decreasing on `(0,pi)`, so

\[
\bigl(u_m-u_{\sigma(m)}\bigr)\cdot u_p>0.
\]

Also `u_p\cdot u_p=1`. Thus the right side of (3) has positive dot product with `u_p`, contradiction.

The exact certificate enumerates all `35` minority subsets, all four possible pivots, and all `3!` matchings. Exactly fourteen subsets admit such a certificate:

\[
\boxed{
123,124,125,127,134,135,137,
157,167,357,367,457,467,567.
}
\tag{4}
\]

These are seven reflection classes under `i -> 8-i`. Seven sparse representatives are:

```text
123 ; p=7 ; (4,1) (5,2) (6,3)
124 ; p=7 ; (3,1) (5,2) (6,4)
125 ; p=7 ; (3,1) (4,2) (6,5)
127 ; p=5 ; (3,1) (4,2) (6,7)
134 ; p=7 ; (2,1) (5,3) (6,4)
135 ; p=7 ; (2,1) (4,3) (6,5)
137 ; p=5 ; (2,1) (4,3) (6,7)
```

Reflection produces `567,467,367,167,457,357,157`. The earlier convex-`H8` exclusion of `{1,3,7}` / `{1,5,7}` is exactly the final reflection class above, so (4) is the full finite closure of that same order-only pairing mechanism.

---

## 2. Sharper `H6` cone-width projection

For `H6`, the endpoint reduction proves the ground hull angle satisfies

\[
\phi:=\theta_7-\theta_1<\frac{2\pi}{3}.
\tag{5}
\]

Let

\[
\beta=\frac{\theta_1+\theta_7}{2},
\qquad
c=\cos(\phi/2)>\frac12,
\]

and define

\[
c_i=\cos(\theta_i-\beta).
\]

Then

\[
c_1=c_7=c,
\qquad
c\le c_i\le1,
\]

and the ordered sequence `c_1,...,c_7` is unimodal: cosine increases as the rays approach the cone bisector and decreases after they pass it.

For a minority pattern `P`, put `s_i=+1` on `P` and `s_i=-1` on its four-element complement. Ground equilibrium forces the bisector projection

\[
F_P:=\sum_{i=1}^7s_i c_i=0.
\tag{6}
\]

Normalize

\[
y_i=\frac{c_i-c}{1-c}.
\]

Then `y_1=y_7=0`, the interior sequence is unimodal in `[0,1]`, and because `sum_i s_i=3-4=-1`,

\[
F_P=-c+(1-c)\sum_{i=2}^6s_i y_i.
\tag{7}
\]

Use the layer-cake identity

\[
y_i=\int_0^1\mathbf 1_{\{y_i\ge t\}}\,dt.
\]

Every superlevel set of a unimodal sequence is a contiguous block of the interior indices `2,...,6`. Hence, if every contiguous interior block `B` satisfies

\[
\sum_{i\in B}s_i\le1,
\tag{8}
\]

then

\[
\sum_{i=2}^6s_i y_i\le1
\]

and therefore

\[
F_P\le1-2c<0,
\tag{9}
\]

contradicting (6).

The exact verifier checks condition (8) for all `35` minority subsets. Eighteen satisfy it. Ten were already excluded by the open-semicircle pairing lemma; the following eight are genuinely new `H6` exclusions:

\[
\boxed{
126,136,146,147,246,247,257,267.
}
\tag{10}
\]

Combining (4) and (10), the two certified local mechanisms exclude `22/35` possible `H6` ground minority patterns. Exactly thirteen remain:

\[
\boxed{
145,156,234,235,236,237,245,256,345,346,347,356,456.
}
\tag{11}
\]

Thus the unclassified `H6` branch is reduced at the ground from `35` raw `3+4` sign orders to `13`, before imposing relation-graph sign consistency or any non-ground reciprocal order information.

---

## 3. Other support-seven branches

For ground-on-hull `H7a`, the hull-angle bound gives only `phi_0<pi` at this stage, so the fourteen open-semicircle exclusions (4) apply whenever its ground split is `3+4`. The extra eight in (10) are `H6`-specific and are not claimed for `H7a`.

For fully convex `H8`, the open-semicircle hypothesis holds. The current twelve convex survivors have minority patterns among

\[
236,246,146,346,147,257.
\]

They avoid the fourteen order-only pairing obstructions. Some appear in the extra `H6` list, but the `H8` ground cone is not known to have width below `2pi/3`, so (10) cannot be transferred to them.

The thirteen `H6` patterns in (11) are not claimed realizable. They merely survive these two ground-only projection tests. The next H6 layer should combine (11) with relation-edge sign consistency and the new non-ground pentagon gap-order theorem.

No theorem-state file is changed. C-II remains open.
