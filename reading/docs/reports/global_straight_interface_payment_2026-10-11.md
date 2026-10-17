> Generated reading edition · [exact source](../../../docs/reports/global_straight_interface_payment_2026-10-11.md) · source SHA-256 `25354623c3559f78e5d8be5369a9c0f55cebd2c8c7efcb1bdd5ad79193430832`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2C7494B3907E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Straight lattice interfaces pay their boundary-row credits

**Classification:** proved candidate awaiting promotion; **unreviewed**.
**Level I and the finite-grain globalization remain open.**

Run baseline: `ab6dd3336f9f8d440f2bada76edb32153391cddc`, state
`2026-10-10.audit.234`; owned branch
`research/sol/global-independent-20261011`. This argument imports the finite
Oler inequality from [shared theory, Section 21.1](../theory/03-oler-shell.md),
not another worker's unreviewed research.

## 1. The global implication and its missing hypotheses

The implication under investigation is

```text
physical interface area pays internal lattice boundary credits
  + an o(D) bound for the remaining outer boundary and junction terms
  + a decomposition retaining every actual source label
  -> n-1 <= pi D^2/(2 sqrt(3)) + o(D)
  -> contradiction to the candidate positive linear population reserve.
```

The [reserve](global_boundary_zigzag_linear_reserve_2026-10-11.md) is an
unreviewed candidate. The present report proves the interface payment for
two complete lattice half-planes with straight, parallel front rows, and a
finite-window version with an explicit endpoint cost. It does not supply
the other premises. The canonical
[coherent-grain theorem](../targets/target-c/69-coherent-grain-interface-audit.md)
provides phase-coherent rhombus regions and an `O(D)` interface budget; it
does not identify those regions with complete lattice half-planes or make
their junction costs `o(D)`.

The [39-lattice regression](global_lattice_defect_from_linear_reserve_2026-10-11.md)
also remains binding: a finite collection of lattice descriptions by itself
does not justify summing an interface payment. The selected source must have
the actual geometry required below.

## 2. Statement

Write `a0=sqrt(3)/2`. For `i=A,B`, let a rank-two unit-separated lattice have
a basis

$$
u_i=(s_i,0),\qquad v_i=(b_i,h_i),\qquad s_i,h_i>0.
$$

Its covolume is `V_i=s_i h_i`; `s_i>=1` and `V_i>=a0`.
Put `t=(b,g)` with `g>=0`. Assume **every cross-pair** between

$$
P_A=\{k u_A+jv_A:k\in\mathbb Z,\ j\le0\},\qquad
P_B=\{t+k u_B+jv_B:k\in\mathbb Z,\ j\ge0\}
\tag{1}
$$

has distance at least one. In particular, the two populations are disjoint,
even if `g=0`. The assumption concerns the complete half-planes, including
all their rows, not just a finite seam sample.

For **every** pair of positive integers `N,M` such that

$$
Nh_A\ge1,\qquad Mh_B\ge1,
\tag{2}
$$

one has

$$
\boxed{
2g\ge a_0\left({1\over s_A}+{1\over s_B}\right)
-{N(V_A-a_0)\over s_A}-{M(V_B-a_0)\over s_B}.
}
\tag{3}
$$

No common horizontal period, commensurability, or common orientation of the
two full lattices is required. Their front rows must be parallel as displayed.

In particular, if both covolumes equal `a0`, then

$$
\boxed{g\ge {h_A+h_B\over2}.}
\tag{4}
$$

For triangular lattice polygons the lattice-point boundary credit along a
front edge, per unit edge length, is `1/(2s_i)`. Multiplying by `a0`
converts this to area credit `h_i/2`. Thus (4) pays the two front-edge
credits exactly per unit length. This interpretation concerns a full straight
interface, not an assertion that arbitrary finite convex hulls satisfy (1).

## 3. Reflecting a seam into a packing of the whole plane

Set

$$
w_A=Nv_A,\quad w_B=Mv_B,\quad q=2t+w_B,\quad
T=q+w_A,\quad H=T_y=2g+Mh_B+Nh_A.
\tag{5}
$$

The horizontal components of `w_i` can alternatively be reduced modulo
`s_i`; this changes no lattice row and is unnecessary for the proof.
For every integer `r`, retain these two slabs:

$$
A_r=rT+\{ku_A+jv_A:k\in\mathbb Z,\ -N\le j\le0\},
$$
$$
B_r=rT+t+\{ku_B+jv_B:k\in\mathbb Z,\ 0\le j\le M\}.
\tag{6}
$$

Each slab is a subset of one unit-separated lattice. The interface from
`A_r` to `B_r` is a translated restriction of (1). The interface from
`B_r` to `A_(r+1)` is also valid: central inversion

$$
I_r(x)=2rT+q-x
\tag{7}
$$

fixes the set `B_r`, since `j` changes to `M-j` and `k` to `-k`.
It sends `A_r` onto `A_(r+1)`, since

$$
q-(ku_A+jv_A)
=T-ku_A+(-N-j)v_A,
$$

where `-N-j` again runs through `[-N,0]`. Consequently all cross-pairs
at the reflected interface inherit their lower-distance bound from (1).

Consecutive A slabs have vertical gap `2g+Mh_B>=1`; consecutive B slabs
have vertical gap `2g+Nh_A>=1`. Pairs in any more distant slabs have at
least these gaps. This checks every pair in the union

$$
P=\bigcup_{r\in\mathbb Z}(A_r\cup B_r).
\tag{8}
$$

There are no coincident labels: cross-interface distances are at least one,
and same-type successive slabs have vertical separation at least one.
Thus `P` is a unit-separated plane packing. It has translation period `T`;
it need not have any nonzero horizontal period.

## 4. Counting density without a shared horizontal period

Modulo vertical translation by `H`, the A rows have total line density
`(N+1)/s_A`, and the B rows have total line density `(M+1)/s_B`.
Rows from different types may have the same height when `g=0`, but are
disjoint and their populations add. Counting in the square `[-L,L]^2`
gives

$$
|P\cap[-L,L]^2|
={4L^2\over H}\left({N+1\over s_A}+{M+1\over s_B}\right)+O(L).
\tag{9}
$$

For this limit the two lattices, `N,M,g`, and all phases are fixed.
Indeed each horizontal arithmetic progression contributes `2L/s_i+O(1)`
points, and each fixed row class occurs `2L/H+O(1)` times. The horizontal
shift caused by `rT` changes only the bounded counting error of a row.

Apply finite Oler to the square and divide by `4L^2`. Its boundary term
vanishes as `L` tends to infinity. Therefore

$$
{1\over H}\left({N+1\over s_A}+{M+1\over s_B}\right)\le {1\over a_0}.
\tag{10}
$$

Substituting `H=2g+NV_A/s_A+MV_B/s_B` proves (3).
The same square-counting argument applied to a single full lattice proves
the used covolume bound `V_i>=a0`; no equality classification is needed.

## 5. A uniform correction for nearly optimal covolumes

Let `Delta_i=V_i-a0>=0`. Choose

$$
N=\lceil1/h_A\rceil,\qquad M=\lceil1/h_B\rceil.
$$

Since `s_i>=1` and `V_i>=a0`,

$$
{N\over s_A}\le {1\over V_A}+{1\over s_A}\le {1\over a_0}+1,
$$

and likewise for B. Thus

$$
\boxed{
g\ge {a_0\over2}\left({1\over s_A}+{1\over s_B}\right)
-{1+a_0^{-1}\over2}(\Delta_A+\Delta_B).
}
\tag{11}
$$

At a seam of length `ell`, the formal area correction in (11) is at most
`(1+a0^(-1)) ell (Delta_A+Delta_B)/2`. Thus covolume defects `O(1/D)`
along total eligible seam length `O(D)` contribute only `O(1)`.
This is a quantitative consequence **when the complete-seam hypotheses
hold**. It does not certify finite endpoint or junction geometry.

The defect correction cannot simply be removed. Take both lattices with
basis `(19/10,0),(0,1)` and let `t=(19/20,8/25)`. The front rows have
minimum squared cross-distance

$$
(19/20)^2+(8/25)^2=10049/10000>1;
$$

every other cross-row pair has vertical distance greater than one. Yet
`g=8/25<a0/(19/10)`, so the uncorrected payment (4), extended to these
larger covolumes, would be false.

## 6. Finite windows: an explicit endpoint cost

The complete-half-plane premise can be replaced by a finite one, at a
quantified cost. Keep the same lattices and `g>=0`, and choose
`N=ceil(1/h_A)`, `M=ceil(1/h_B)`. Let `I` be **any** closed horizontal
interval of length `ell>0`. Assume every cross-pair between the finite sets

$$
\{ku_A+jv_A:-N\le j\le0,\ x\in I\},\qquad
\{t+ku_B+jv_B:0\le j\le M,\ x\in I\}
\tag{12}
$$

has distance at least one. These sets include **all** lattice sites in the
specified rows and horizontal window. They can be checked as finite sets;
no valid continuation of the seam beyond `I` is assumed.

Put

$$
E=a_0\left({1\over s_A}+{1\over s_B}\right)-2g
-{N\Delta_A\over s_A}-{M\Delta_B\over s_B},
\qquad S=s_A+s_B.
$$

Then

$$
\boxed{\ell\max(E,0)\le24S.}
\tag{13}
$$

In particular, with `kappa=1+a0^(-1)`,

$$
\boxed{
g\ell\ge {a_0\ell\over2}\left({1\over s_A}+{1\over s_B}\right)
-{\kappa\ell\over2}(\Delta_A+\Delta_B)-12(s_A+s_B).
}
\tag{14}
$$

Thus a finite triangular interface pays both front-row credits up to an
endpoint cost of at most `12(s_A+s_B)`. The estimate is uniform in the
length of the interface and in the relative horizontal phase.

Here is a packing proof that keeps the finite-window restriction explicit.
Choose the origin on the A front row nearest the midpoint of `I`, so that
`I=[c-ell/2,c+ell/2]` with `|c|<=s_A/2`. Choose the representative `b`
of the B front-row phase with `|b-c|<=s_B/2`. Choose lattice vectors
`w_A,w_B` of vertical components `Nh_A,Mh_B` and horizontal components
of absolute values at most `s_A/2,s_B/2`, respectively. As before set
`q=2t+w_B`, `T=q+w_A`, and `H=T_y`.

Set `K=3S/2`. These choices give

$$
|T_x|\le K,\qquad |(w_A)_x+2c|\le K,
\qquad |q_x-2c|\le K.
\tag{15}
$$

If `ell>2K`, trim both ends of `I` by `K`, obtaining an interval `J`
of width `W=ell-2K`. In every slab in (6), now retain only the points
whose **local** horizontal coordinate, before translation by `rT`, lies
in `J`. The direct interfaces use points in `I`. At a reflected interface,
the two preimages have local horizontal coordinates `-(w_A)_x-x_A` and
`q_x-x_B`. By (15), both lie in `I` whenever `x_A,x_B` lie in `J`.
Their row indices are still the indices in (12). Therefore every reflected
cross-pair is certified by the same **finite** assumption (12).
All nonadjacent pairs retain the vertical guards from Section 3.

This constructs an infinite unit-separated strip, invariant under `T`.
Let `n0` be its population per period, and set

$$
L_0={N+1\over s_A}+{M+1\over s_B},\qquad r_0=N+M+2.
$$

Counting each finite row gives `n0>=W L_0-r_0`. In the tilted coordinate
`u=x-(T_x/H)y`, the entire strip has width at most `W+|T_x|`:
the local vertical span of one period is `H-g<=H`. For `k` consecutive
periods, a containing parallelogram has area at most
`kH(W+|T_x|)` and perimeter at most
`2k|T|+2(W+|T_x|)`. Apply Oler to its `k n0` distinct labels and let
`k` tend to infinity. This yields

$$
n0\le {H(W+|T_x|)\over a_0}+|T|.
$$

Since `a0 L_0-H=E`,

$$
\boxed{WE\le H|T_x|+a_0|T|+a_0 r_0.}
\tag{16}
$$

If `E<=0`, (13) is immediate. If `E>0`, then

$$
E\le2a_0,\quad
H<a_0L_0\le2+4a_0<6,\quad
r_0\le {S\over a_0}+4,\quad |T|\le H+|T_x|<6+K.
\tag{17}
$$

The bound for `H` uses `N/s_A<=1/V_A+1/s_A` and its B analogue;
it does **not** assume an upper bound on the covolumes. Combining
(16)--(17) and `ell=W+2K` gives

$$
\ell E\le(6+5a_0)K+S+10a_0
<11K+S+10\le {45\over2}S<24S,
$$

where `S>=2`. If instead `ell<=2K`, the direct estimate
`ell E<=4a0 K<=6S` suffices. This proves (13). Finally the bound
`N Delta_A/s_A+M Delta_B/s_B<=kappa(Delta_A+Delta_B)` proves (14).

## 7. What summing the finite payment would require

For a collection of eligible physical interfaces, (14) gives a total
shortfall from the two front-row credits of at most

$$
{\kappa\over2}\sum_e\ell_e(\Delta_{A,e}+\Delta_{B,e})
+12\sum_e(s_{A,e}+s_{B,e}).
\tag{18}
$$

In particular this is `o(D)` if both sums are `o(D)`. A bounded primitive
row period and `o(D)` interface segments suffice for the second sum. Neither
condition follows merely from an `O(D)` bound on total interface length.
To use (18) in the implication from Section 1, one must also identify
disjoint physical area to pay the `g_e ell_e` terms and account for every
source label, outer boundary, and junction. The finite-window theorem does
not authorize counting the same gap area twice.

## 8. Validation and exact scope

Run

```bash
python3 research/verify_global_straight_interface_payment_2026_10_11.py
```

The finite checker uses exact rational and `Q(sqrt(3))` arithmetic. It
checks original and reflected seam pairs, neighboring slab pairs, row
identities, density/payment algebra, and a negative seam fixture. Cases
include equality in two triangular row orientations, incommensurate
horizontal row periods, a positive covolume defect, and the valid zero-gap
interlaced-row case. The infinite pair ledger and density limit are proved
above, not inferred from those finite cases.

The finite-window checks additionally exercise the horizontal phase reductions,
trimmed-window preimages, and tilted parallelogram enclosure. They check 5,694
original finite cross-pairs and 28,407 pairs among 507 strip labels. A valid
short triangular-lattice window has an invalid infinite continuation and
positive interface debt; this verifies that the finite theorem is being used
with its endpoint allowance, without assuming the stronger infinite premise.

The result supplies no source extraction, isolate allocation, curved seam
theorem, bound on the total junction count, or strict diameter improvement. It is one
exact payment rule for a global assembly argument; it is not Level I closure.
