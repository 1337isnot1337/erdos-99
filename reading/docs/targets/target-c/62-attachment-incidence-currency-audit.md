> Generated reading edition · [exact source](../../../../docs/targets/target-c/62-attachment-incidence-currency-audit.md) · source SHA-256 `cc69a3b95317f24adcd64c5c514dc8016a7c7df53092a4dd594a652817be3b63`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — attachment-incidence currency audit

This module isolates the valid attachment-cell consequences from older mixed reports
whose cyclic tails used the rejected Reuleaux-cap detour. Everything below is proved
from the canonical post-ZF ledgers, planar attachment incidence, and triangle-free
penny-graph counting. No cyclic cap theorem, no KKT coefficient floor, and no
contact-isolate removal is used.

**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

---

# 62. Topology defect forces loaded-loaded contacts

Use the canonical post-ZF C-II notation:

- `B` is the loaded diameter-endpoint set, `q=|B|`;
- `I_1,...,I_{c_I}` are the connected components of the unloaded positive-contact
  graph;
- `A_r subset B` is the distinct loaded attachment set of `I_r`;
- `a_r=|A_r|`, `a=sum_r a_r`;
- `e_BB` is the number of loaded-loaded unit contacts;
- `s_C=sum_r s_r` is the extra pinned-contact left-nullity beyond the one mandatory
  positive equilibrium relation per unloaded component;
- `d_H=q-h` is the Woodall diameter-component defect;
- `s_Z=e+h-(2v-2)` is the mixed-rigidity surplus; and
- `k:=d_H+s_Z`.

The main exact theorem is

```math
\boxed{e_{BB}\ge d_H+s_Z.}
\tag{62.1}
```

Thus every unit of diameter-component or mixed-row defect is already visible as at
least one loaded-loaded unit contact. The theorem holds whether or not unloaded
contact components exist.

A second exact theorem gives the total perimeter of all harmonic attachment cells:

```math
\boxed{
\sum_r\operatorname{per}(P_r)
\le
\pi\bigl(2+2q-e_{BB}-(d_H+s_Z)\bigr),
\qquad
P_r:=\operatorname{conv}(A_r).
}
\tag{62.2}
```

In particular, using (62.1) and `q<=pi D`,

```math
\boxed{
\sum_r\operatorname{per}(P_r)
\le2\pi(q+1-k)
\le2\pi^2D+2\pi.
}
\tag{62.3}
```

So the entire attachment-cell perimeter correction is boundary order with an explicit
constant; there is no `D c_I` loss.

## 62.1 Local attachment-stress inequality

Fix one unloaded component `I_r`. Let

- `n_r=|I_r|`;
- `e_r` be the contacts internal to `I_r`;
- `t_r` be the contacts from `I_r` to `A_r`;
- `s_r=e_r+t_r-2n_r-1>=0`;
- `c_r` be the actual loaded-loaded unit contacts whose endpoints both lie in `A_r`;
- `c_r^partial` be those `c_r` contacts which are sides of
  `P_r=conv(A_r)`.

The induced straight-line contact graph on `I_r union A_r`, including those `c_r`
loaded-loaded contacts, is connected, planar, and triangle-free. Harmonic trapping
puts `I_r` in `P_r`, and the loaded terminals are in strictly convex position, so every
member of `A_r` is a vertex of `P_r`.

Let `L_r` be the outer-face walk length of this induced graph. Between two consecutive
vertices of `A_r` on `partial P_r`, the outer-face route has length one exactly when
that polygon side is one of the `c_r^partial` direct contacts; otherwise it has length
at least two. Hence

```math
L_r\ge c_r^partial+2(a_r-c_r^partial)
=2a_r-c_r^partial.
\tag{62.4}
```

For any connected triangle-free plane graph with `N` vertices, `M` edges, and
outer-face walk length `L`, Euler plus bounded-face length at least four gives

```math
M\le2N-2-{L\over2}.
\tag{62.5}
```

Here

```math
N=n_r+a_r,
\qquad
M=e_r+t_r+c_r=2n_r+1+s_r+c_r.
```

Insert (62.4) into (62.5):

```math
2n_r+1+s_r+c_r
\le
2n_r+2a_r-2-a_r+{c_r^partial\over2}.
```

Therefore

```math
\boxed{
s_r+c_r-{c_r^partial\over2}\le a_r-3.
}
\tag{62.6}
```

In particular

```math
\boxed{s_r\le a_r-3.}
\tag{62.7}
```

Summing over unloaded components gives

```math
\boxed{s_C\le a-3c_I.}
\tag{62.8}
```

This is an exact finite theorem. It does not assume `s_Z=0` or any diameter-topology
branch.

## 62.2 Planar attachment incidence

Assume first `c_I>0`. Contract each `I_r` to one interior incidence node and retain
one edge to each distinct loaded attachment in `A_r`. The resulting simple bipartite
plane graph has all loaded-side vertices on the outer face.

Let `q_used` be the number of loaded vertices used by at least one attachment set and
let `s>=1` be the number of connected incidence components containing an interior
node. For one connected piece with `q_j` loaded nodes, `c_j` interior nodes, `e_j`
incidence edges, and `f_j` faces, every loaded node lies on the outer face. Because the
graph is bipartite, its outer-face walk has length at least `2q_j`, while every bounded
face has length at least four. Thus

```math
2e_j\ge2q_j+4(f_j-1).
```

Euler gives `q_j+c_j-e_j+f_j=2`, hence

```math
e_j\le q_j+2c_j-2.
```

Summing over the `s` pieces gives

```math
\boxed{
a=\sum_r|A_r|
\le q_{used}+2c_I-2s
\le q+2c_I-2.
}
\tag{62.9}
```

This rederives the exact C37 incidence bound inside the present proof.

## 62.3 Proof that `e_BB>=d_H+s_Z`

The canonical post-ZF pinned ledger is

```math
\boxed{
c_I+e_{BB}+s_C=q-2+k,
\qquad k=d_H+s_Z.}
\tag{62.10}
```

If `c_I>0`, combine (62.8) and (62.9):

```math
s_C\le a-3c_I
\le q-c_I-2.
```

Insert this in (62.10):

```math
q-2+k
=c_I+e_{BB}+s_C
\le e_{BB}+q-2,
```

so

```math
e_{BB}\ge k.
```

If `c_I=0`, then by definition `s_C=0`, and (62.10) gives

```math
e_{BB}=q-2+k\ge k,
```

because a normalized KKT stress has a positive diameter edge and therefore `q>=2`.
This proves (62.1) in every post-ZF C-II branch.

### Exact quotient-slack refinement

For `c_I>0`, define

```math
u_A:=a-3c_I\ge0.
```

Let `p_A>=0` be the planar-incidence slack in

```math
a=q_{used}+2c_I-2s-p_A,
```

let `u_0=q-q_used>=0`, and let `r_Q>=0` be the excess loaded-loaded quotient
connectivity in

```math
e_{BB}=s+u_0-1+r_Q.
```

Subtracting the two exact expressions for `q` obtained from these definitions and
(62.10) gives

```math
\boxed{
s_C+r_Q
=k+u_A+p_A+(s-1).}
\tag{62.11}
```

Since (62.8) says `u_A-s_C>=0`,

```math
\boxed{
r_Q
=k+(u_A-s_C)+p_A+(s-1)
\ge k.}
\tag{62.12}
```

Thus the stronger statement behind (62.1) is that the loaded-loaded contacts needed
*in excess of bare quotient connectivity* already pay the complete topology defect.

## 62.4 Exact total attachment-perimeter bound

Let `delta_r` be the graph diameter of `C[I_r]`, with zero for a singleton. Define the
triangle-free penny-graph slack

```math
r_r:=2n_r-\delta_r-2-e_r\ge0,
\qquad
R_I:=\sum_rr_r.
```

Equation (62.7)'s pinned-nullity definition gives

```math
e_r+t_r=2n_r+1+s_r.
```

Therefore

```math
t_r-\delta_r-3=s_r+r_r.
\tag{62.13}
```

Let

```math
s_B:=3q-e_{BI}-2e_{BB}\ge0,
\qquad e_{BI}=\sum_rt_r,
```

using the canonical loaded contact-degree cap three. Summing (62.13) gives

```math
e_{BI}
=\sum_r\delta_r+3c_I+s_C+R_I.
```

Substitute this and (62.10) into the definition of `s_B`. The `3q` terms cancel and
yield the exact component-diameter ledger

```math
\boxed{
\sum_r\delta_r+R_I+s_B+3k
=6+e_{BB}+2s_C.
}
\tag{62.14}
```

Hence

```math
\sum_r\delta_r
\le6+e_{BB}+2s_C-3k.
\tag{62.15}
```

Harmonic trapping and the unit contact paths imply

```math
\operatorname{diam}(A_r)\le\delta_r+2.
```

Cauchy's planar perimeter-diameter inequality gives

```math
\operatorname{per}(P_r)
\le\pi(\delta_r+2).
```

Summing and using (62.15),

```math
\sum_r\operatorname{per}(P_r)
\le
\pi\bigl(6+e_{BB}+2s_C-3k+2c_I\bigr).
\tag{62.16}
```

Eliminate `c_I` with (62.10):

```math
6+e_{BB}+2s_C-3k+2c_I
=2+2q-e_{BB}-k.
```

This proves (62.2). Applying (62.1) proves the first inequality in (62.3), and
`q<=per(F)<=pi D` proves the second.

## 62.5 Coupling to the canonical renormalized surplus

The independently audited all-phase surplus theorem states, with

```math
\mu_D:={e_{BB}+2s_C-3k\over D},
```

that

```math
\liminf\mu_D\ge z_*>0.9604,
\qquad
10\arcsin z_*-4\pi={z_*\over3}.
\tag{62.17}
```

Using (62.1),

```math
2(e_{BB}+s_C)
=(e_{BB}+2s_C)+e_{BB}
\ge4k+\mu_DD.
```

Therefore

```math
\boxed{
\liminf_{D\to\infty}
{e_{BB}+s_C-2(d_H+s_Z)\over D}
\ge {z_*\over2}>0.4802.
}
\tag{62.18}
```

Also

```math
3\max\{e_{BB},s_C\}
\ge e_{BB}+2s_C
=3k+\mu_DD,
```

so

```math
\boxed{
\liminf_{D\to\infty}
{\max\{e_{BB},s_C\}-(d_H+s_Z)\over D}
\ge {z_*\over3}>0.32013.
}
\tag{62.19}
```

These are retained-currency statements: even after paying the complete Woodall/mixed
defect, a universal linear amount remains in actual loaded-loaded contacts and/or
pinned-contact self-stress.

## 62.6 Scope and regressions

- **No unloaded components (`c_I=0`):** handled separately; (62.1) follows directly
  from ZU.
- **Many singleton harmonic cells:** allowed; (62.2) shows their total attachment
  perimeter is still only boundary order.
- **Regular odd shell:** has `c_I=s_C=0`; the theorem reduces to its direct
  loaded-loaded contact ledger and is compatible.
- **Positive `s_Z`:** retained explicitly through `k=d_H+s_Z`.
- **Forest and cyclic Woodall branches:** both covered.
- **Contact-isolated source points:** untouched. The theorem concerns the positive
  contact core and does not identify `v` with the full source population `n`.
- **Rejected cyclic cap theorem:** not used. In particular no assertion
  `b-per(F)=o(D)` or `H_out=o(D^2)` occurs.
- **KKT coefficient floors:** not used.

## 62.7 Remaining obstruction

Section 62 removes one diffuse possibility from the post-ZF ledger: topology defect
cannot be hidden in attachment multiplicity while loaded-loaded contact currency stays
small. It also removes the old quadratic attachment-perimeter correction.

What remains is genuinely geometric. A large `e_BB` is compatible with a dense loaded
boundary graph, and a large `s_C` is compatible with many pinned self-stresses. The
next closing theorem must convert the retained linear currency in (62.18)--(62.19)
into one of:

1. a face/outer-walk contradiction;
2. a forced negative transfer/common-block contradiction; or
3. a simultaneous strict sub-`D` competitor.

Pure incidence counting cannot supply that final conversion.
