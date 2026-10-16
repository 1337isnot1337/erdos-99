# Erdős Problem #99 — WO145 rhombic branch forces a large unloaded flat-center remainder

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II low-`t` small-residual branch  
**Claim class:** proof-only structural composition  
**Dependencies:** WO145 lossless train split; low-`t` flat-center amplification; loaded flat-center singleton payment; unloaded degree-three/degree-four flat-center consequences

## LEVEL I STATUS

`STILL OPEN`

The existing flat-center unloading gate is unconditional in the train split: a loaded
flat pentagon center costs two singleton stopped trains, and a coarse upper bound on the
total singleton population leaves a small linear unloaded remainder.

WO145 makes the **rhombic** side of the train split much stronger.  If the rhombic
slack branch occurs, then the non-singleton rhombic-train population itself is forced
well above its generic lower bound.  That sharply reduces the number of singleton
trains still available to pay loaded flat centers.

The result is a large branch-specific unloaded-center floor.  At the current WO145
Section-171 endpoint, on the existing `R_F=o(D)` low-`t` branch,

\[
\boxed{
\liminf {|U_3|+|U_4|\over D}
\ge0.264049655121665\ldots .
}
\tag{RFU.1}
\]

Consequently at least one of the already-established unloaded-center mechanisms is
macroscopic:

\[
\boxed{
\liminf {|H_4|\over D}
\ge0.0293388505690740\ldots
}
\tag{RFU.2}
\]

for a pairwise endpoint-disjoint hidden-pair family with inherited `o(D)` total
activation gap, or

\[
\boxed{
\liminf {|E_3|\over D}
\ge0.0660124137804163\ldots
}
\tag{RFU.3}
\]

for a set of distinct positive contacts with inherited `o(D^2)` total normalized KKT
weight.

This does not close either mechanism, but it makes them much larger than in the
unconditional loaded-center payment theorem.

---

## 1. Inputs and notation

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
s:=\sqrt{\Delta_2},
\qquad
g:=0.00145.
\tag{RFU.4}
\]

On a convergent low-`t` Type-II subsequence write

\[
t:=\lim{q-k\over D},
\qquad
\delta:=\lim{b-P_F\over D},
\qquad
\kappa:=\lim{k\over D}.
\tag{RFU.5}
\]

Assume the same small-residual hypothesis as the current flat-center amplification:

\[
R_F=o(D).
\tag{RFU.6}
\]

The WO145 all-train theorem upgrades the flat-center constant from the older
`2s+0.00042` to

\[
C_g:=2s+g.
\tag{RFU.7}
\]

Thus the existing flat-center population theorem gives

\[
\boxed{
{V_{flat}\over D}
\ge
P_g(t,\delta,\kappa)-o(1),
}
\tag{RFU.8}
\]

where

\[
\boxed{
P_g(t,\delta,\kappa)
:=\pi+2s+g-{5t\over2}+\delta+{\kappa\over2}.
}
\tag{RFU.9}
\]

The loaded flat-center theorem gives an exact finite payment: if `L` is the loaded
flat-center set and `S` the total singleton stopped-train population, then

\[
\boxed{2|L|\le S_E\le S.}
\tag{RFU.10}
\]

Finally the exact train ledger gives, in the same limit,

\[
\boxed{
{T\over D}\le5t-2\pi-2\delta+o(1).
}
\tag{RFU.11}
\]

---

## 2. Insert the WO145 rhombic branch before paying loaded centers

WO145 gives the lossless total train-defect floor

\[
{\rho_{rec}+\sigma_R\over D}
\ge t+2g-o(1).
\tag{RFU.12}
\]

Pass to the rhombic side of the resulting two-way branch:

\[
\boxed{
{\sigma_R\over D}
\ge {t+2g\over2}-o(1).
}
\tag{RFU.13}
\]

By definition

\[
\sigma_R=2T_R-4\sqrt{R_4},
\]

and Type-II rhombic saturation gives `sqrt(R_4)/D -> s`.  Therefore

\[
\boxed{
{T_R\over D}
\ge2s+{t+2g\over4}-o(1).
}
\tag{RFU.14}
\]

Since `T=T_R+S`, combine (RFU.11) and (RFU.14):

\[
\boxed{
{S\over D}
\le
5t-2\pi-2\delta-2s-{t+2g\over4}+o(1).
}
\tag{RFU.15}
\]

The loaded-center payment (RFU.10) now yields

\[
\boxed{
{|L|\over D}
\le
{5t\over2}-\pi-\delta-s-{t+2g\over8}+o(1).
}
\tag{RFU.16}
\]

This is the new ingredient: on the rhombic branch, the same large rhombic defect that
survives the train argument also removes singleton capacity from the loaded flat-center
escape.

---

## 3. Large unloaded-center remainder

Write

\[
V_{flat}=L\sqcup U_3\sqcup U_4.
\]

Subtract (RFU.16) from (RFU.8).  The unloaded population `U=U_3\sqcup U_4` satisfies

\[
\begin{aligned}
{ |U|\over D}
&\ge
\pi+2s+g-{5t\over2}+\delta+{\kappa\over2}\\
&\quad-\left({5t\over2}-\pi-\delta-s-{t+2g\over8}\right)-o(1)\\
&=
2\pi+3s+{5g\over4}-{39t\over8}
+2\delta+{\kappa\over2}-o(1).
\end{aligned}
\]

Hence

\[
\boxed{
\liminf {|U|\over D}
\ge
U_R(t,\delta,\kappa),
}
\tag{RFU.17}
\]

with

\[
\boxed{
U_R(t,\delta,\kappa)
:=2\pi+3s+{5g\over4}-{39t\over8}
+2\delta+{\kappa\over2}.
}
\tag{RFU.18}
\]

The `delta` and `kappa` terms are favorable and may be dropped for a conservative
endpoint value.

WO145 Section 171 gives

\[
 t\ge t_{145}
 ={4\over9}(\pi+s)+0.0015914
 =1.821104937979444\ldots .
\tag{RFU.19}
\]

At the lower endpoint `t=t145`, `delta=kappa=0`, direct substitution gives

\[
\boxed{
U_R(t_{145},0,0)
=0.264049655121665\ldots .
}
\tag{RFU.20}
\]

This proves (RFU.1) on the rhombic side of the low-`t` small-residual branch.

The coefficient in (RFU.18) stays positive, before using either favorable bonus, for

\[
 t< {8\over39}\left(2\pi+3s+{5g\over4}\right)
 =1.875268969799273\ldots .
\tag{RFU.21}
\]

This numerical positivity range should be intersected with the actual scope of the
underlying low-`t` flat-center theorem; no extension of that theorem's scope is claimed
here.

---

## 4. Existing unloaded-center consequences become macroscopic

The unloaded flat centers split as `U_3\sqcup U_4`, so at least one class has size at
least `|U|/2`.

If

\[
|U_4|\ge {|U|\over2},
\]

the existing degree-four activation theorem extracts a pairwise endpoint-disjoint
hidden-pair family satisfying

\[
|H_4|\ge {2|U_4|\over9}\ge {|U|\over9}.
\]

Its inherited activation budget has total hidden-side excess `o(D)`.  At the WO145
endpoint this gives

\[
\boxed{
{|H_4|\over D}
\ge {0.264049655121665\ldots\over9}-o(1)
=0.0293388505690740\ldots-o(1).
}
\tag{RFU.22}
\]

If instead

\[
|U_3|\ge {|U|\over2},
\]

the flat-center stress theorem assigns exterior positive contacts and deduplicates with
loss at most two, giving

\[
|E_3|\ge {|U_3|\over2}\ge {|U|\over4}
\]

and

\[
\sum_{e\in E_3}\alpha_e=o(D^2).
\]

Thus

\[
\boxed{
{|E_3|\over D}
\ge {0.264049655121665\ldots\over4}-o(1)
=0.0660124137804163\ldots-o(1).
}
\tag{RFU.23}
\]

This proves (RFU.2)--(RFU.3).

---

## 5. Updated low-`t` closing fork

On the `R_F=o(D)` low-`t` branch, WO145 now gives a useful nested split.

First, the global train defect gives either

```text
singleton side:
    S >= (t+2g)D/4 - o(D),
```

or

```text
rhombic side:
    sigma_R >= (t+2g)D/2 - o(D).
```

At the current endpoint these are approximately

```text
S >= 0.4560012 D,
```

or

```text
sigma_R >= 0.9120025 D.
```

On the rhombic side, the loaded-flat-center escape is then too expensive in singleton
trains, so at least `0.2640496D` flat centers must be unloaded.  Therefore the rhombic
side refines further to

```text
>= 0.02933885 D endpoint-disjoint near-active hidden pairs
   with o(D) total activation gap,

or

>= 0.06601241 D distinct positive contacts
   with o(D^2) total normalized KKT weight.
```

The remaining work is now branch-specific.  The singleton side needs a source-level
obstruction to a `0.456D` singleton-train population.  The rhombic side needs either a
uniform activation theorem for the disjoint hidden pairs or a quantitative prohibition
on the large low-stress positive-contact family.  This note proves neither obstruction.

---

## 6. Scope audit

- The statement is conditional on the same `R_F=o(D)` low-`t` branch as the inherited
  flat-center population theorem.
- The WO145 all-train gain and lossless train split are proof-only inputs on the full-core
  Type-II branch.
- The loaded-center payment `2|L|<=S_E<=S` is finite and does not assume singleton
  edges are bridges.
- The rhombic branch is a subsequence branch of the lossless train dichotomy; (RFU.14)
  is not asserted on the singleton branch.
- The positivity range (RFU.21) is only an algebraic range for the new coefficient and
  does not enlarge the inherited low-`t` theorem's domain.
- Contact-isolated source points remain in the full source.
- No exact unit triangle or strict same-cardinality diameter descent is produced.

**Disposition:** proof-only WO145/rhombic flat-center composition.  C-II remains open.
