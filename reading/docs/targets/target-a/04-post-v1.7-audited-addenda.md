> Generated reading edition · [exact source](../../../../docs/targets/target-a/04-post-v1.7-audited-addenda.md) · source SHA-256 `e8362f708ba26e0a7f8aaf87750d9372863989ff6cf91c69c0788ee98680b902`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — post-v1.7 audited addenda

This file contains theorem-level additions audited after the append-only source-response
module through Section 145. It is part of the active Target A route map. It does not
renumber or rewrite the historical Sections 111–145.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

The direct endpoint remains

$$
\boxed{\dim\ker S\ge \Delta_\Lambda-d_{\rm int}},
$$

equivalently

$$
\boxed{\operatorname{rank}S\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.}
$$

---

# 146. Vanishing-gap finite-witness complexity

Section 136 imports the finite-rearrangement consequence of
Kuperberg–Kuperberg–Kuperberg: a triangular/honeycomb packing with any positive
linear gap defect is not completely saturated. Section 137 then concentrates a
fixed total homothetic strain into a fixed-width gap. The missing quantitative
question is what happens to the finite rearrangement witness as the gap width tends
to zero.

Normalize the triangular lattice $\Lambda$ to minimum separation one. For a line
$\ell$, let $\mathcal H_{d,\ell}$ be the gap-defect packing obtained by moving
every lattice point in one closed half-plane a perpendicular distance $d>0$ away
from $\ell$. Define

$$
\kappa(d,\ell)=
\min\left\{
|S|:
\begin{array}{l}
S\subset \mathcal H_{d,\ell}\text{ finite},\ T\subset\mathbb R^2\text{ finite},\\
|T|>|S|,\quad
(\mathcal H_{d,\ell}\setminus S)\cup T\text{ is unit-separated}
\end{array}
\right\}.
\tag{146.1}
$$

The Kuperberg theorem implies $\kappa(d,\ell)<\infty$ for every $d>0$ and every
line direction. Put

$$
\kappa_*(d)=\inf_\ell\kappa(d,\ell).
\tag{146.2}
$$

> **Theorem 146.1 (witness complexity diverges as the gap closes).**
> 

$$

> \boxed{\kappa_*(d)\longrightarrow\infty\qquad(d\downarrow0).}
> \tag{146.3}
> 
$$


> Equivalently, for every integer $K$ there is $d_K>0$ such that every positive-gain
> finite rearrangement of every width-$d$ triangular gap packing with
> $0<d<d_K$ deletes more than $K$ old centers.

### Proof

The covering radius of the unit triangular lattice is $1/\sqrt3$. Every center
moves by at most $d$ when the gap is inserted. Hence every point of the plane is
within

$$
\frac1{\sqrt3}+d
$$

of some center of $\mathcal H_{d,\ell}$. In particular, for

$$
0<d<1-\frac1{\sqrt3},
\tag{146.4}
$$

the gap packing is 1-saturated: no new point can be appended without deleting an old
center.

Assume (146.3) is false. Then there are $K<\infty$, widths $d_n\downarrow0$,
lines $\ell_n$, and positive-gain finite replacements

$$
S_n\longrightarrow T_n,
\qquad
|S_n|\le K,
\qquad
|T_n|>|S_n|,
\tag{146.5}
$$

such that

$$
(\mathcal H_{d_n,\ell_n}\setminus S_n)\cup T_n
$$

is unit-separated.

Form the bipartite strict-conflict graph on $S_n\sqcup T_n$, joining $s$ to
$t$ when $|s-t|<1$. For large $n$, (146.4) implies that every $t\in T_n$
has a conflict with a deleted center: otherwise $t$ could be appended to the
original gap packing. Decompose the graph into connected components. Replacing the
old vertices by the new vertices in any one component is feasible by itself, since
there are no strict cross-component conflicts and every point outside $S_n$ was
already compatible with all of $T_n$. Because the total gain is positive, one
component has

$$
|T_n'|>|S_n'|.
\tag{146.6}
$$

Replace $(S_n,T_n)$ by such a component.

A unit-separated set contains at most five points in an **open** unit disk about a
fixed center. Indeed, six radial directions would contain two with angular separation
at most $\pi/3$, and with both radii strictly below one their mutual distance would
be strictly below one. Since every $t\in T_n$ strictly conflicts with some
$s\in S_n$,

$$
|T_n|\le5|S_n|\le5K.
\tag{146.7}
$$

The connected conflict graph therefore has at most $6K$ vertices, every edge has
length strictly below one, and its entire geometric support has diameter below
$6K$.

The support must remain within a bounded distance of the defect line. If one support
point were farther than $6K+2$ from $\ell_n$, the whole connected support would
lie more than two units from the line in one half-plane. In a neighborhood containing
the support and its unit collar, $\mathcal H_{d_n,\ell_n}$ then coincides with a
translate of the perfect triangular lattice. The same replacement would therefore
be a finite positive-gain rearrangement of the perfect lattice. This is impossible:
the triangular lattice is a periodic maximum-density circle packing and hence is
completely saturated.

Choose an old center in the support and translate it to the origin. By the preceding
paragraph the translated defect lines have bounded offset from the origin. After
passing to a subsequence, their directions converge. The supports lie in one fixed
compact disk and have uniformly bounded cardinality. The gap displacement tends to
zero, so the old-center sets converge locally to the perfect triangular lattice.
After another subsequence, the removed centers have fixed limiting lattice labels and
the new points converge to a finite set $T_\infty$. All packing inequalities are
closed, hence

$$
(\Lambda\setminus S_\infty)\cup T_\infty
$$

is unit-separated and

$$
|T_\infty|>|S_\infty|.
$$

This is again a finite positive-gain rearrangement of the completely saturated
triangular lattice, a contradiction. Therefore (146.3) holds. $\square$

## 146.1 Exact scope

Theorem 146.1 gives a rigorous asymptotic obstruction but **no explicit rate** for
$\kappa_*(d)$. The Kuperberg block proof shows finiteness for each fixed
$d>0$, but does not state a polynomial or other quantitative support bound as
$d\downarrow0$. Do not claim $O(d^{-c})$, $\Theta(d^{-c})$, or any comparable
rate without a separate proof.

This also explains why Section 137 is enough for the free homothetic regression with
$\varepsilon_L=\alpha/L$, $\alpha>0$: accumulated strain is concentrated into a
**fixed positive** gap, so one fixed finite Kuperberg witness works for all sufficiently
large $L$. Theorem 146.1 becomes relevant only when every available concentration
produces a gap width tending to zero.

---

# 147. Audit of the five first-transition / gap obligations

The five proof obligations that motivated this addendum have the following exact
status.

1. **Same-hull add-one for fixed homothetic strain scale — proved.** Section 137
   proves that if $L\varepsilon_L\ge\eta>0$, the strained triangular rhombus can be
   rearranged inside its own hull to contain one additional unit-separated point for
   all sufficiently large $L$. In particular this applies to every fixed
   $\varepsilon_L=\alpha/L$, $\alpha>0$. It is a free-rhombus theorem; exterior
   blockers of an embedded source/scaffold domain still require protection.

2. **First-triangle perturbation unless a genuine cage remains — proved.** The
   one-point semicircle/cage theorem and the stronger fixed-container expansive-cone
   theorem in Sections 137–138 show that the first triangle-producing optimum can be
   perturbed to a triangle-free optimum unless a unit triangle is universally
   first-order locked by the active contact/container cone.

3. **Locked first-transition cage implies a Schur separator — not proved.** No map
   from one locked unit triangle, or from its local equilibrium certificate, to an
   independent $C^\partial\to O$ alternating nonlinkage has been established.
   Proposition 139.1 shows that exact local cages occur already in the smallest tree
   circuit. Thus local cage geometry alone cannot be treated as the missing Schur
   theorem. A valid proof must use the globally derived source/scaffold coupling.

4. **Two-leaf gadget — proved exactly.** Proposition 139.1 gives a one-parameter
   exact Euclidean family whose strict-conflict graph is the path
   $x_- - b - x_+$, whose retained shore is triangle-free, and for which either
   leaf swap creates an infinitesimally pinned unit triangle. The earlier numerical
   gadget is therefore superseded by this analytic regression family.

5. **Vanishing-gap witness size — partially quantified.** Theorem 146.1 proves the
   sharp qualitative asymptotic statement $\kappa_*(d)\to\infty$. No explicit
   growth rate is currently established.

None of these results changes the Level I status. The missing Target A bridge remains
an exact transport from global source/first-transition information to the Schur
response, or an exterior-compatible finite replacement carrying an actual
smaller-diameter certificate.
