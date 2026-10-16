# Target C-II — the adjacent-strip KKT reaction is always nonzero

**Date:** 2026-09-15  
**Status:** proof-only exact structural strengthening  
**Scope:** any adjacent O--O strip in the canonical full-support KKT normalization  
**Dependencies:** adjacent switching outer-boundary order; sparse KKT layer reaction; convex-hull extremality of actual diameter endpoints  
**Supersedes:** the residual balanced-antipodal branch in `target_c_adjacent_strip_sparse_force_reaction_2026-09-15.md` and the weaker one-sided reduction `target_c_balanced_antipodal_reaction_one_sided_2026-09-15.md`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The sparse-force theorem writes the exact reaction of one physical layer between consecutive O--O cuts as

\[
\boxed{
G:=Aa+Bb
=\sum_{h\in H_{sw}}\beta_h n_h,
\qquad A,B>0,
\qquad \beta_h>0,
}
\tag{NR.1}
\]

where `a,b` are the two outside-to-middle unit boundary-contact vectors and every switching diameter vector

\[
n_h=m_h-x_h,
\qquad |n_h|=D,
\tag{NR.2}
\]

points from its exterior endpoint `x_h` into its middle-layer endpoint `m_h`.

The sparse-force theorem left one exceptional possibility,

\[
G=0
\iff
b=-a,\ A=B.
\]

That branch is incompatible with the audited convex-hull order of switching diameter endpoints.

### Theorem NR — reaction nondegeneracy

For every canonical adjacent O--O strip to which the strip-opening reduction applies,

\[
\boxed{G\ne0.}
\tag{NR.3}
\]

Consequently the generic sparse-force conclusion is unconditional:

\[
\boxed{
G=\lambda_1n_{h_1}+\lambda_2n_{h_2}
}
\tag{NR.4}
\]

for one or two actual switching diameter edges, with positive coefficients and with the unused second term omitted when one edge suffices.

Equivalently, the balanced-antipodal zero-reaction branch does not occur in the canonical source.

---

## 1. A convex-position separation lemma

Let `P` be a finite set of extreme vertices of one planar convex polygon, with its cyclic order.  Let `I` be a nonempty proper cyclic interval of these vertices and let `J=P\setminus I`.

Then

\[
\boxed{\operatorname{conv}(I)\cap\operatorname{conv}(J)=\varnothing.}
\tag{NR.5}
\]

Hence there is a linear functional `phi` and a constant `c` such that

\[
\phi(v)>c\quad(v\in I),
\qquad
\phi(w)<c\quad(w\in J).
\tag{NR.6}
\]

One direct proof is to choose points in the relative interiors of the two polygon edges crossing from `I` to `J`.  The segment joining those two points is a chord of the convex polygon.  Its supporting line separates the two open boundary arcs strictly, and therefore separates their vertex hulls.  The singleton cases are the same by a supporting-line perturbation.

Only the difference form will be used below: if `m` lies in one block and `x` in the complementary block, then after choosing the sign of `phi`,

\[
\boxed{\phi(m-x)>0.}
\tag{NR.7}
\]

---

## 2. One-sided switching cannot have zero reaction

Use the four open outer-boundary blocks from the audited switching-order theorem,

\[
B_L,\ B_M^+,\ B_R,\ B_M^-.
\tag{NR.8}
\]

Every endpoint of an actual diameter edge is an extreme point of the source convex hull, and the outer-face cyclic order restricted to diameter endpoints agrees with convex-hull cyclic order.

Assume first that every switching row is a **left switch**.  Then each edge joins

\[
x_h\in B_L
\]

to

\[
m_h\in B_M^+\cup B_M^-.
\]

The participating vertices in `B_L` lie in one cyclic interval of the convex-hull vertices.  Every middle endpoint lies in its complementary cyclic interval

\[
B_M^+\cup B_R\cup B_M^-.
\]

Apply the separation lemma with the sign chosen so that

\[
\phi(m_h-x_h)>0
\qquad(h\in H_{sw}).
\tag{NR.9}
\]

Because every `beta_h>0`,

\[
\phi\!\left(\sum_h\beta_hn_h\right)
=\sum_h\beta_h\phi(m_h-x_h)>0.
\tag{NR.10}
\]

Thus the switching reaction cannot vanish.

If every switching row is a **right switch**, use the single cyclic block `B_R` for the exterior endpoints and its complementary block for the middle endpoints.  The same argument gives

\[
\sum_h\beta_hn_h\ne0.
\tag{NR.11}
\]

Hence `G=0` is impossible in either one-sided branch.

---

## 3. Mixed switching orientations cannot have zero reaction

Now suppose both left-switch and right-switch rows occur.

The audited one-arc theorem then forces **every switching middle endpoint** onto one common middle boundary block

\[
B_M^\star\in\{B_M^+,B_M^-\}.
\tag{NR.12}
\]

Every switching exterior endpoint lies in

\[
B_L\cup B_R,
\]

which is contained in the complementary cyclic interval to `B_M^star`.

Apply the same convex-position separation lemma, this time with the middle block as `I`.  After choosing the sign of `phi`,

\[
\phi(m_h-x_h)>0
\qquad\text{for every left or right switching edge }h.
\tag{NR.13}
\]

Positive KKT weights again give

\[
\phi\!\left(\sum_h\beta_hn_h\right)>0,
\tag{NR.14}
\]

so the reaction is nonzero.

This also gives a shorter proof of the earlier one-sided-reduction note: the mixed case was never compatible with zero reaction, but neither are the two one-sided cases.

---

## 4. Consequence for the sparse-force theorem

The three switching possibilities are exhaustive:

1. left switches only;
2. right switches only;
3. both switch orientations.

Sections 2--3 show that the positive switching reaction is nonzero in all three cases.  Hence (NR.3) holds.

The conic Caratheodory argument from the sparse-force theorem now applies without an exceptional branch.  Therefore there are one or two actual switching diameter vectors generating the complete layer reaction:

\[
G
=\lambda_1n_{h_1}+\lambda_2n_{h_2},
\qquad
\lambda_j>0.
\tag{NR.15}
\]

Taking the dot product with any contact-opening tangent direction shows that the same one/two bars also form a tangent obstruction certificate.

Thus the live adjacent-strip problem has no three-bar force-balance degeneracy.  Its exact force obstruction is always one of

```text
one switching diameter bar;

two switching diameter bars sharing a loaded endpoint;

two vertex-disjoint switching diameter bars crossing properly.
```

The full switching graph can still contain more edges; (NR.15) sparsifies the exact reaction, not the active constraint set.

---

## 5. Frontier effect

The local reaction classification is now strictly two-bar:

```text
physical middle-layer translation
+ positive full-support KKT reaction
+ exact convex-hull switching order
 -> nonzero reaction
 -> one/two actual diameter bars generate the reaction
 -> the same one/two bars block every strict opening tangent ray.
```

The next geometric obligation is to eliminate or exploit those one/two-bar chord patterns using the train endpoints, the ordered switching caterpillar, and global minimality.  No balanced-antipodal three-bar force case remains.

No exact unit triangle or strict-diameter competitor is claimed here.

**Disposition:** proved proof-only exact nondegeneracy of the adjacent-strip KKT reaction; the sparse reaction is always generated by at most two switching diameter bars. C-II and Level I remain open.
