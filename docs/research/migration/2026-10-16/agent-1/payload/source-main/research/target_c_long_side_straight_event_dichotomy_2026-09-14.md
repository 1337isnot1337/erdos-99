# Target C-II — long-side near-straight event dichotomy

**Date:** 2026-09-14  
**Repository base:** `6b9afd0870cb6148e54762088f7e70f46767a70a`  
**Status:** proved proof-only source-level reduction; theorem-state authority unchanged  
**Scope:** finite distinguished outer-route geometry; numerical corollary uses the current low-`t` long-side branch  
**LEVEL I STATUS:** `STILL OPEN`

The outer-route directional-energy identity shows that the rounded long-side branch
contains many near-tangent contact-edge occurrences. Looking one step deeper, most
*internal route occurrences* are locally near-straight. Triangle-freeness then turns
every such occurrence into one of two physical events:

1. a degree-two contact vertex, which C26 forces to be positively diameter-loaded; or
2. a branching contact vertex carrying a strongly transverse extra unit contact.

This gives a finite tradeoff between loaded degree-two events and transverse contact
edges.

## 1. Near-straight internal occurrences

Retain the distinguished outer routes `W_i` between consecutive loaded force-hull
vertices. Orient `W_i` along its chord unit direction `u_i`. For its edge occurrences
write

\[
v_{i,j}\cdot u_i=\cos\theta_{i,j}.
\]

The exact directional-energy identity is

\[
d_{out}
=\sum_i\sum_j(1-\cos\theta_{i,j}).
\tag{SE.1}
\]

Fix `beta in(0,pi/3)` and let `A_beta` be the number of edge occurrences with
`|theta_{i,j}|>=beta`. Then

\[
A_\beta\le {d_{out}\over1-\cos\beta}.
\tag{SE.2}
\]

Let

\[
J=\{i:s_i>2\},
\qquad
L_{>2}=\sum_{i\in J}(s_i-2).
\]

An internal occurrence of `W_i` is `beta`-straight when both adjacent oriented edge
occurrences have angle less than `beta` from `u_i`. If `S_beta` is the total number of
such internal occurrences over `i in J`, then each bad edge occurrence spoils at most
two internal occurrences, while

\[
\sum_{i\in J}(\ell_i-1)
\ge\sum_{i\in J}(s_i-1)
=|J|+L_{>2}
\ge L_{>2}.
\]

Therefore

\[
\boxed{
S_\beta
\ge L_{>2}-{2d_{out}\over1-\cos\beta}.
}
\tag{SE.3}
\]

This is finite and occurrence-counted, so bridges and articulation repetitions remain
included.

## 2. A branching straight event has a transverse extra contact

Consider one `beta`-straight internal occurrence at a physical vertex `x`. Let `a`
and `b` be its predecessor and successor on that occurrence of the outer walk. From
`x`, the contact ray to `a` lies within `beta` of `-u_i`, while the contact ray to `b`
lies within `beta` of `+u_i`.

Suppose `deg_C(x)>=3` and choose any third contact neighbor `w`. Because the source is
unit-separated and triangle-free, the angular separation between any two contact rays
at one vertex is strictly greater than `pi/3`.

If the ray `xw` lay within angular distance `pi/3-beta` of the tangent axis
`R u_i`, then it would lie within `pi/3` of one of the two route-contact rays, a
contradiction. Hence its projective distance from the tangent axis is greater than
`pi/3-beta`. Equivalently,

\[
\boxed{
{|(w-x)\cdot Ju_i|\over|w-x|}
>\sin(\pi/3-\beta).
}
\tag{SE.4}
\]

Since `xw` is a unit contact, this is an absolute transverse-component bound.

For the useful choice `beta=pi/6`, every selected extra contact satisfies

\[
\boxed{|(w-x)\cdot Ju_i|>1/2.}
\tag{SE.5}
\]

No KKT coefficient enters this conclusion.

## 3. Finite event tradeoff

Let

- `V_2(beta)` be the number of distinct physical contact vertices of degree exactly
  two that support at least one `beta`-straight long-side internal occurrence;
- `E_perp(beta)` be the number of distinct physical extra contact edges selected from
  degree-at-least-three vertices supporting such occurrences, one edge selected per
  physical vertex.

A triangle-free unit contact vertex has degree at most five, because contact-neighbor
directions are pairwise separated by more than `pi/3`.

A degree-two physical vertex can occur at most twice on one face-boundary walk. Thus
degree-two vertices account for at most `2 V_2(beta)` straight occurrences.

A degree-at-least-three physical vertex can account for at most five outer-face
occurrences. If `B_beta` is the number of distinct such vertices, their straight
occurrences are at most `5B_beta`. One selected extra contact edge can be selected at
at most its two endpoints, so

\[
B_\beta\le2E_\perp(\beta).
\]

Consequently

\[
\boxed{
2V_2(\beta)+10E_\perp(\beta)
\ge S_\beta
\ge L_{>2}-{2d_{out}\over1-\cos\beta}.
}
\tag{SE.6}
\]

C26 says every nonisolated degree-two contact vertex in the fully force-visible C-II
core is positively diameter-loaded. Therefore every vertex counted by `V_2(beta)` is
an actual loaded diameter terminal.

## 4. Current low-`t` long-side corollary

At `t=t_42`, the long-side alternative and low-detour squeeze give

\[
{L_{>2}\over D}
\ge0.4363893718701161781\ldots-o(1),
\]

\[
{d_{out}\over D}
\le0.002883975+o(1).
\]

Set `beta=pi/6`. Since

\[
{d_{out}/D\over1-\cos(\pi/6)}
\le0.02152628245551690578\ldots+o(1),
\]

(SE.3) gives

\[
\boxed{
{S_{\pi/6}\over D}
\ge0.3933368069590823665\ldots-o(1).
}
\tag{SE.7}
\]

The finite tradeoff (SE.6) becomes

\[
\boxed{
2{V_2(\pi/6)\over D}
+10{E_\perp(\pi/6)\over D}
\ge0.3933368069590823665\ldots-o(1).
}
\tag{SE.8}
\]

In particular at least one of the following holds:

\[
\boxed{
{V_2(\pi/6)\over D}
\ge0.09833420173977059163\ldots-o(1),
}
\tag{SE.9}
\]

or

\[
\boxed{
{E_\perp(\pi/6)\over D}
\ge0.01966684034795411832\ldots-o(1),
}
\tag{SE.10}
\]

and every edge counted in the second branch has absolute transverse component greater
than `1/2` relative to one long loaded-hull side direction.

The first branch is not an anonymous boundary-event count: it is a linear population
of positively diameter-loaded vertices having full contact degree exactly two.

## 5. Frontier effect

The rounded long-side escape has now been reduced twice:

```text
L_{>2}=Omega(D), d_out small
 -> Omega(D) distinct near-tangent outer contacts
 -> Omega(D) near-straight internal route occurrences
 -> either
      Omega(D) loaded degree-two contact vertices,
    or
      Omega(D) strongly transverse physical contacts.
```

The transverse branch is naturally compatible with the weight-free train/phase
machinery. The degree-two loaded branch is now the sharper obstruction: a closing
continuation should couple those nearly tangential two-contact loaded terminals to the
near-extremal Woodall diameter thrackle and its KKT equilibrium. Local geometry alone
cannot exclude them; regular shell regressions show why the diameter reaction must be
used.

## 6. Reproducibility

Run

```bash
python3 research/verify_target_c_long_side_straight_event_dichotomy.py
```

for the Decimal certificate.
