> Generated reading edition · [exact source](../../research/target_c_leaf_fan_outerwalk_fork_2026-10-02.md) · source SHA-256 `a38a8681b798c8af79ef9ac40ef6d318c8030b13cb1528063e5d9842ec0b590b`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C: outer-walk currency versus exact diameter-leaf fans

Date: 2026-10-02
Base: a5b22d70604c5da236f24587df43ac31a0d94e17
Status: proof-only reduction; C-II remains open.

Let H=(B,E_H) be the full actual diameter graph, h=|E_H|, and nu=nu(H).
Canonical ZF gives h >= ceil(D). Section 63 writes the positive-contact outer walk
between consecutive loaded hull vertices as intervals of integer lengths ell_i >= 1,
with

    x_B = sum_i (ell_i - 1).                                      (1)

Hence at most x_B loaded-hull intervals have length greater than one; every remaining
interval is one actual unit loaded-loaded contact.

## 1. Same-carrier leaves are consecutive

For a nonleaf diameter vertex a, let L(a) be its degree-one diameter neighbors and
t_a=|L(a)|.

Lemma 1. L(a) is one consecutive block in the cyclic order of B.

Proof. Take distinct p,q in L(a), and a loaded vertex z on the open hull arc from p
to q not containing a. In cyclic order write

    a, ..., p, ..., z, ..., q, ..., a.

Choose any diameter edge zw, which exists because every loaded vertex has positive
diameter degree. If w != a, then w != p,q because p,q are leaves. The
diameter-thrackle property makes zw cross both ap and aq. Crossing ap forces w onto
the open arc (a,p), while crossing aq forces it onto the disjoint open arc (q,a), a
contradiction. Thus every diameter edge at z is za, so z is in L(a). QED.

A carrier with t_a>0 therefore contributes exactly t_a-1 consecutive loaded-hull
adjacencies whose two endpoints are diameter leaves with common carrier a.

## 2. Matching pays for leaf blocks

Let

    P = sum_a t_a,
    c = number of carriers a with t_a>0,
    S = sum_{a:t_a>0} (t_a-1) = P-c.

Choosing one pendant edge at every carrier gives a matching, so

    c <= nu.                                                       (2)

Lemma 2.

    S >= h - 3 nu.                                                 (3)

Forest branch. Let K be the number of K_2 diameter components. Let E_core be the
edges whose two endpoints are nonleaves, put m=|E_core|, and let mu be the matching
number of the core-edge graph. Woodall makes that graph a disjoint union of paths, so
m <= 2 mu. The K isolated K_2 edges can be added to a maximum core matching, hence

    mu + K <= nu.                                                  (4)

Every diameter edge is exactly a core edge, a K_2 edge, or a leaf-to-nonleaf edge.
Therefore

    P = h - m - K >= h - 2 nu.                                    (5)

Together with (2), this proves (3) in the forest branch.

Cyclic branch. Write r for the odd cycle length. If there are no leaves, then S=0,
h=r=2nu+1, and h-3nu=1-nu <= 0. If there is a pendant leaf at a cycle vertex a,
use that leaf edge plus a maximum matching on the even path obtained from the cycle
by deleting a. This gives

    nu >= (r+1)/2,  hence  r <= 2nu-1.                             (6)

All noncycle edges are leaf-to-nonleaf edges, so P=h-r >= h-2nu+1. Using c<=nu
again proves (3). QED.

The forest estimate couples K_2 components and core-path matching in one matching
budget. Charging them independently loses an unnecessary extra nu.

## 3. Exact fan-contact / outer-walk fork

Call an internal same-carrier leaf-block adjacency pq a good fan contact if its
outer-walk interval has length one. Let A be the number of these contacts. At most
x_B of the S relevant intervals are bad by (1), so

    A >= max(0, h - 3nu - x_B).                                   (7)

Equivalently,

    A + x_B + 3nu >= h >= ceil(D).                                (8)

Every counted contact pq has one common diameter carrier a, hence

    |p-a| = |q-a| = D,    |p-q| = 1.                              (9)

Thus every counted edge is the unit base of an exact isosceles triangle with side
lengths (D,D,1). Its carrier angle is exactly 2 asin(1/(2D)).

This is stronger than merely knowing that many diameter leaves have contact degree
two or three: it identifies a linear-scale population of exact loaded-hull contacts
whose two endpoints share the same diameter carrier.

## 4. Small outer-walk excess forces one long exact fan

Bad relevant intervals split the carrier blocks into good runs. There are at most

    c + x_B <= nu + x_B                                           (10)

nonempty good runs. Hence, whenever A>0, one carrier supports a run of g consecutive
good fan contacts with

    g >= A/(nu+x_B)
      >= (h-3nu-x_B)/(nu+x_B)                                    (11)

when the final numerator is positive. The run is a consecutive loaded-hull chain

    p_0, p_1, ..., p_g

with

    |p_i-a| = D,    |p_i-p_{i+1}| = 1.                            (12)

So one actual diameter circle contains an exact unit-chord boundary chain.

In the current square-root hard regime nu=O(sqrt(D)), (8) gives

    A + x_B >= D - O(sqrt(D)).                                    (13)

Therefore, if x_B=o(D),

    A = D - o(D),                                                  (14)

and (11) forces

    g >= (D-o(D))/(x_B+O(sqrt(D))) -> infinity.                   (15)

If x_B=O(sqrt(D)), then g=Omega(sqrt(D)).

The companion matching/currency reduction gives

    x_B + Q + 2s_Z >= D - O(sqrt(D))                              (16)

in the same regime. Thus the low-x_B branch simultaneously has

    A = D-o(D),    Q+2s_Z >= D-o(D),                              (17)

plus a growing exact same-carrier circular unit-contact fan.

## 5. Remaining obstruction

This does not close C-II. Long (D,D,1) fans are locally feasible, and (7) gives
support geometry rather than a multiplier floor.

The square-root matching branch is now narrowed to either:

1. x_B = Omega(D); or
2. D-o(D) exact good fan contacts, a growing same-carrier unit-chord run, and
   Q+2s_Z >= D-o(D).

A closing argument should couple the second branch to KKT equilibrium and the
face/rank currency. Every internal vertex of a good run already has two positive unit
contacts and loaded contact degree at most three, leaving only the degree-two
tangential-balance case or one extra contact to charge. That coupling is not proved
here.

No computation, numerical search, verifier execution, or CI output is used.
