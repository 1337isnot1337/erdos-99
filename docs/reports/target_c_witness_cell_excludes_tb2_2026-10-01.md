<!-- theorem-state: {"artifact_id":"ART-5AD965A4AB9C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- witness cells eliminate the genuine two-bar strip branch

Date: 2026-10-01
Authoritative main before write: 91be6776e6748b0f449ccfff69bca1e352d1b75d
Dependencies: 4abd2eb3cbdeb122f8ca787cb9cdbd7522e9c978, a8cffebb2d0ba945ec45b18a5054cb56d4422121
Status: proof-only; C-II remains open.

## 1. Local interval-location lemma for a genuine two-bar blocker

Let \(\tau,\tau'\) be consecutive non-singleton global O-O trains on one shore of
the fixed-star complete rectangle, and let \(u,u'\) be their coherently oriented
rooted-shore unit vectors. A train from the opposite shore crosses both, so the
audited common-transversal/rooted-shore sign theorem identifies these ordinary
vectors with the real Section-90 phase lift.

Assume \(u\ne u'\). Put
\[
\varepsilon=d_{\mathbb{RP}^1}([u],[u'])\in(0,\pi).
\]
For the physical middle layer, the two outside-to-middle boundary-contact vectors are
\[
a=u,\qquad b=-u'.
\]
Because the common real lift has width \(<\pi\), the physical opening cone
\[
\Omega=\{w\in S^1:a\cdot w\ge0,\ b\cdot w\ge0\}
\]
has angular width exactly \(\varepsilon\).

Suppose no single switching diameter bar is a tangent certificate. Reaction
nondegeneracy and planar conic Caratheodory then give two actual switching diameter
vectors \(n_1,n_2\) with positive coefficients generating the exact nonzero layer
reaction. The pair is a minimal two-bar tangent certificate: if both bars shortened
some \(w\in\Omega\), their positive sum would have negative dot product with \(w\),
contradicting
\[
G=Aa+Bb,\qquad A,B>0,
\]
while if either bar blocked every \(w\in\Omega\), there would already be a one-bar
certificate.

The following strengthening of the audited two-bar geometry is then exact:
\[
\boxed{
[n_1],[n_2]\in I([u],[u']),
}
\tag{1}
\]
where \(I([u],[u'])\) is the closed minor projective interval between the two train
directions.

Proof. Rotate and, if necessary, reflect coordinates so
\[
u=(1,0),\qquad \arg u'=-\varepsilon.
\]
Then
\[
a=(1,0),\qquad \arg b=\pi-\varepsilon,
\]
and
\[
\arg w\in[\pi/2-\varepsilon,\pi/2]
\qquad(w\in\Omega).
\tag{2}
\]

For a switching bar \(n\), let
\[
I_n=\{w\in\Omega:n\cdot w<0\}.
\]
In a minimal two-bar certificate, both \(I_{n_1},I_{n_2}\) are nonempty and their
intersection is empty. Neither can equal all of \(\Omega\), because then the other
shortening interval would have to be empty and the other bar would itself be a
one-bar certificate. Thus each \(I_{n_j}\) is a nonempty proper interval of
\(\Omega\), so it has a boundary point \(w_j\in\Omega\) with
\[
n_j\cdot w_j=0.
\]
Projectively, a vector perpendicular to a direction of angle
\(\psi_j\in[\pi/2-\varepsilon,\pi/2]\) has direction
\[
\psi_j-\pi/2\in[-\varepsilon,0]\pmod\pi.
\]
Hence
\[
[n_j]\in[-\varepsilon,0]=I([u'],[u]),
\]
proving (1).

This is stronger than the previously used estimate
\[
d_{\mathbb{RP}^1}([n_1],[n_2])\le\varepsilon:
\]
both load-bearing diameter directions lie inside the train-direction interval itself.

## 2. The fixed witness cell rules out genuine TB2 exactly

The current fixed-star rectangle has, on each retained shore, one canonical witness
cell supplied by the local witness-cell theorem.

### Open witness cell

There are two fixed actual diameter edges \(h_-,h_+\) whose projective directions
are consecutive in the global diameter-direction order and every retained train
direction lies strictly in the open gap
\[
J=(\operatorname{dir}h_-,\operatorname{dir}h_+).
\tag{3}
\]

Take any adjacent retained pair with distinct train directions. Its minor interval
\(I([u],[u'])\) is contained in \(J\). If the strip had no one-bar tangent
certificate, Section 1 would produce two actual switching diameter edges with
directions in \(I([u],[u'])\subset J\). This is impossible because \(h_-,h_+\) are
consecutive global diameter directions.

Therefore:
\[
\boxed{
\text{on an open witness-cell shore, every non-antipodal adjacent strip has a
one-bar switching tangent certificate.}
}
\tag{4}
\]

There is no genuine non-antipodal TB2 branch.

### Threshold witness cell

In the threshold case one fixed actual diameter direction \(h_0\) lies between the
two witness edges and every retained train is projectively parallel to \(h_0\).
The common Section-90 real lift has width \(<\pi\), so all retained trains use the
same ordinary orientation. Hence for every adjacent pair
\[
u'=u,
\]
and the physical boundary vectors satisfy
\[
a=u,\qquad b=-u.
\]
Thus every adjacent strip is exactly antipodal:
\[
\boxed{
\text{on a threshold witness-cell shore, every adjacent strip is exact-antipodal.}
}
\tag{5}
\]

Combining (4) and (5), the fixed-star complete rectangle has the exact local fork
\[
\boxed{
\text{exact-antipodal strip}
\quad\text{or}\quad
\text{non-antipodal strip with a one-bar switching tangent certificate}.
}
\tag{6}
\]
No genuine non-antipodal two-bar tangent branch survives anywhere on either retained
shore.

## 3. Consequence for the joint stress-light cusp family

Use the joint stress-light cusp extraction on one retained shore. Write
\[
c_*={\kappa^4\over16\pi^3C_KM_K},
\qquad
H_*=\left\lceil{4\pi\over c_*}\right\rceil+1.
\]
It supplies a family \(\mathcal S\) of pairwise-disjoint adjacent strips satisfying
\[
|\mathcal S|
\ge
\left(
{c_*\over8(H_*+3)}-o(1)
\right)D,
\tag{7}
\]
whose adjacent train pairs are pairwise disjoint and whose complete switching packets
are pairwise edge-disjoint. Each strip also has
\[
1\le N_i\le H_*,
\qquad
\mu_i\le {8\over c_*D},
\qquad
0<|G_i|\le {8\over c_*}.
\tag{8}
\]

Partition \(\mathcal S\) into

- \(E\): exact-antipodal strips;
- \(U\): non-antipodal strips with a one-bar switching tangent certificate.

Equation (6) makes this partition exhaustive:
\[
\boxed{|E|+|U|=|\mathcal S|.}
\tag{9}
\]
Therefore
\[
\boxed{
\max\{|E|,|U|\}
\ge
\left(
{c_*\over16(H_*+3)}-o(1)
\right)D.
}
\tag{10}
\]

If \(U\) is the linear branch, choose one tangent-blocking switching diameter edge
from each strip. The switching packets are pairwise edge-disjoint, so these chosen
one-bar blockers are pairwise distinct.

If \(E\) is the linear branch, then for every retained strip
\[
G_i=W_i u_i-W_{i+1}u_{i+1}
=(W_i-W_{i+1})u_i\ne0,
\]
hence
\[
\boxed{
0<|W_i-W_{i+1}|
=|G_i|
\le {8\over c_*}.
}
\tag{11}
\]
Thus the exact-antipodal branch carries a linear family of disjoint strips with
nonzero uniformly bounded axial KKT reaction.

## 4. Remaining target

The fixed-star branch no longer has a genuine TB2 local obstruction.

Its live local alternatives are now:
\[
\boxed{
\begin{array}{l}
\text{linear exact-antipodal disjoint-cusp family with bounded nonzero axial reactions,}\\[2mm]
\text{or}\\[1mm]
\text{linear family of pairwise-distinct one-bar switching tangent blockers.}
\end{array}
}
\tag{12}
\]

Both alternatives still sit inside the same complete inverse-phase O-O rectangle and
retain the fixed full-span witness pair and the complete opposite transverse shore.

The next geometric target is global order for the selected one-bar blockers, or,
in the exact-antipodal branch, an order/variation obstruction for the bounded nonzero
axial reactions. The split-star O-O and inactive-interface branches remain open.

No computation, verifier, numerical experiment, CI result, or unexecuted verifier code
is used.
