> Generated reading edition · [exact source](../../research/target_a_one_source_arm_per_contact_edge_2026-10-03.md) · source SHA-256 `572671d08cdc4592f1d73a2af1d123b996b15ee46e4936bec53bf2c238022621`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f605c8a79435cb44146e46e3819e978b3764556d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_a_one_source_arm_per_contact_edge_2026-10-03.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "689db44ba530df0b10cf176a40d4a14094f0c2ea8787e53300508cdc68b07140"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target A: one strict source arm per unit contact edge

Date: 2026-10-03
Base main: 6c45398dcfe69e3b3bb322920a2911468dfe0573
Parent proof note on this branch: research/target_a_triangle_core_source_rank_2026-10-03.md
Status: proof-only candidate; noncanonical. Target A and Level I remain open.

This run is disjoint from the active Target B four-bar case-2 deformation route and
Worker B's finite nine-no-root k=5 support enumeration. It sharpens the
Section-176 source/contact-shield interface.

The new point is exact: for a strict source matching from the unit-separated response
set X* into the unit-separated source A0, a fixed unit contact edge of X* can be met
by at most one off-shield matching arm. The canonical Section-176.5 estimate charges
up to five source arms per shield vertex. The previous noncanonical lens argument on
this branch charged two source arms per contact edge. Both are improved below.

## 1. One contact edge supports at most one strict source arm

Let pq be a unit contact of X*. Let x be in X*\{p,q}, let a be in A0, and assume

    |x-a| < 1.

Suppose the closed segment [x,a] meets the relative interior of [p,q].

A nontrivial collinear overlap is impossible. Indeed x is unit-separated from p and q.
If x lies on the contact line outside [p,q], reaching the relative interior of [p,q]
already requires distance at least one. Also the intersection cannot occur at a
shield vertex: if p lies on [x,a], then either p=a, giving |x-p|<1, or p lies before
a and again |x-p|<|x-a|<1. Both contradict unit separation of X*.

Thus the intersection with the relative interior is either a proper crossing or the
source endpoint a itself. Let z be such an intersection point and put

    t = |p-z|,
    s = |x-z|,
    r = |a-z|.

Then 0<t<1, |q-z|=1-t, and s+r=|x-a|<1. Unit separation in X* gives

    1 <= |x-p| <= s+t,
    1 <= |x-q| <= s+1-t.

Hence

    s >= max(t,1-t)

and therefore

    r < 1-max(t,1-t) = min(t,1-t).                  (1)

The case z=a is included: then r=0.

Now suppose two distinct matching arms x_1-a_1 and x_2-a_2 meet the same contact
edge, at parameters t_1<=t_2. Applying (1) to both arms and joining a_1 to a_2
through their two intersection points gives

    |a_1-a_2|
      <= r_1 + (t_2-t_1) + r_2
      <  min(t_1,1-t_1)
         +(t_2-t_1)
         +min(t_2,1-t_2).                              (2)

The final expression is at most one in all three cases:

- if t_2<=1/2, it is 2t_2<=1;
- if t_1>=1/2, it is 2-2t_1<=1;
- if t_1<=1/2<=t_2, it is exactly 1.

Thus |a_1-a_2|<1, contradicting unit separation of A0.

Therefore:

### Theorem 1 — one-arm contact-edge crossing

For any strict matching from X* into A0 and any unit contact pq of X*,

    #{ x in X*\{p,q} :
       [x,a_x] meets relint[p,q] } <= 1.                 (3)

No lattice hypothesis is used.

## 2. Exact shield-crossing budget

Let Sigma be any finite unit-contact shield in X*. Consider off-shield response
vertices x in X*\V(Sigma) whose strict source arm [x,a_x] meets |Sigma|.

As above, such an arm cannot meet Sigma only at a shield vertex and cannot overlap a
contact edge collinearly. Hence it meets the relative interior of at least one contact
edge. Assign the arm to one such edge. Theorem 1 says no edge receives two arms.
Consequently

    boxed{
    #{ x in X*\V(Sigma) :
       [x,a_x] cap |Sigma| != empty }
    <= |E(Sigma)|.
    }                                                     (4)

For a connected unicyclic three-channel fan, |E(Sigma)|=|V(Sigma)|=:v, so the
canonical Section-176 source-crossing charge improves from 5v to v.

This is stronger than the two-source-per-lens estimate used in the parent proof note.
The lens theorem remains useful for other purposes, but it is not sharp for a single
strict source matching.

## 3. Current-main source-gate consequence

Use the independent zero-slack matchings of Section 177.5,

    M_C : C^partial -> A0,
    M_O : O -> A0,

and let L be the number of common source labels. Canonical Section 177.5A gives

    L >= |C^partial| + |O| - 20d - 25.                  (5)

Let

    B_C = C^partial cap widehat W_Sigma,
    b   = |B_C|,

and retain the Section-175 sets T_O, O_iso, C_i, O_i. Put

    P_Sigma = sum_i max(0, |C_i|-|O_i|),
    Q_Sigma = sum_i max(0, |O_i|-|C_i|).                 (6)

Using only current-main Section 176.3, at most 12d+9 common gates have their
M_C source label outside K*. By (4), at most |E(Sigma)| off-shield C-arms meet the
contact shield. Therefore every common-source gate except at most

    b + (12d+9) + |E(Sigma)| + |T_O|                    (7)

has all of the following properties:

1. its C endpoint belongs to some C_i;
2. its common source a lies in K* in the same shield sector as that C endpoint;
3. its C-arm does not meet Sigma;
4. its O endpoint is not in T_O.

If such an O endpoint is not isolated, choose a surviving response neighbor x of o.
Both a and x lie in the open unit disk B(o,1). If a and x were in different shield
sectors, the segment [a,x] would meet |Sigma|. Convexity of B(o,1) would then place a
point of |Sigma| at distance below one from o, contrary to o notin T_O. Thus x is in
the same sector as a, and o belongs to the matching O_i.

Distinct common labels have distinct C and O endpoints. Hence the nonexceptional
common gates number at most

    |O_iso| + sum_i min(|C_i|,|O_i|).                    (8)

Combining (5), (7), (8), and

    |C^partial| = b + sum_i |C_i|,
    |O| = |T_O| + |O_iso| + sum_i |O_i|,

gives the stronger active-sector budget

    boxed{
    sum_i |O_i| + P_Sigma
    <= |E(Sigma)| + 32d + 34.
    }                                                     (9)

In particular

    sum_i |O_i| <= |E(Sigma)| + 32d + 34.                (10)

Section 175.3 then gives

    rank S
    <= |T_Sigma| + sum_i min(|C_i|,|O_i|)
    <= |T_Sigma| + |E(Sigma)| + 32d + 34.                (11)

There is also a right-deficiency form that retains the sector imbalance instead of
discarding it. Section 175.4 gives

    h(G) >= |O_iso| + Q_Sigma - |T_Z|
         =  |O| - |T_Sigma| - sum_i|O_i| + Q_Sigma.

Using (9),

    boxed{
    h(G)
    >= |O| - |T_Sigma| - |E(Sigma)| - 32d - 34
       + P_Sigma + Q_Sigma.
    }                                                     (12)

Since P_Sigma+Q_Sigma=sum_i ||C_i|-|O_i||, this records every sector population
imbalance with the favorable sign.

The exact identity |O|-j_*=|C^partial|-s therefore shows that this simultaneous
zero-slack/locked subbranch closes whenever

    boxed{
    |C^partial|-s + P_Sigma+Q_Sigma
    >= |T_Sigma| + |E(Sigma)| + 32d + 34.
    }                                                     (13)

Equation (13) uses canonical current-main constants apart from the new one-arm theorem.

## 4. Sharpened stacked consequence on this branch

The parent proof note proves independently, by one-sided packing,

    exterior M_C source labels <= 8d+1.                  (14)

Replacing 12d+9 by 8d+1 in the calculation above improves (9), (11), and (12) to

    boxed{
    sum_i |O_i| + P_Sigma
    <= |E(Sigma)| + 28d + 26,
    }                                                     (15)

    boxed{
    rank S
    <= |T_Sigma| + |E(Sigma)| + 28d + 26,
    }                                                     (16)

and

    boxed{
    h(G)
    >= |O| - |T_Sigma| - |E(Sigma)| - 28d - 26
       + P_Sigma + Q_Sigma.
    }                                                     (17)

Keeping the `sum_i min(|C_i|,|O_i|)` term in the same common-source gate count,
rather than replacing it by `sum_i|C_i|`, also yields the sharper exact cap

    boxed{
    Q_Sigma <= b + |E(Sigma)| + 28d + 26 - |C^partial|.
    }                                                     (18)

Indeed, the lower gate count is
`|C^partial|+|O|-20d-25`, while the exceptional-gate upper count uses `8d+1`
exterior labels, at most `|E(Sigma)|` crossing arms, `|T_O|` collar sinks,
`|O_iso|` isolated sinks, and the retained sector term. Substitute
`|C^partial|=b+sum_i|C_i|` and
`|O|=|T_O|+|O_iso|+sum_i|O_i|`; the difference
`sum_i|O_i|-sum_i min(|C_i|,|O_i|)` is exactly `Q_Sigma`.

The same parent note proves, for a connected shield containing the locked unit
triangle and after choosing an admissible response-lattice rotation,

    |T_Sigma|
    <= floor(
       (4/sqrt(3)+4/pi)|E(Sigma)|
       +11/2+2pi/sqrt(3)-2sqrt(3)-6/pi ).                 (19)

For the Section-172 connected unicyclic fan, E=V=:v. Thus (17) closes the simultaneous
zero-slack/locked-fan subbranch whenever

    |C^partial|-s + P_Sigma+Q_Sigma
    >= floor(
       (4/sqrt(3)+4/pi)v
       +11/2+2pi/sqrt(3)-2sqrt(3)-6/pi )
       + v + 28d + 26.                                    (20)

The effective fan coefficient in (20) is

    1 + 4/sqrt(3) + 4/pi
    = 4.582640621493666...,

before the favorable sector-imbalance term P_Sigma+Q_Sigma is used.

For comparison, the previous parent-note combination had fan coefficient
5.582640621493666... because it charged two source labels per contact lens. The new
one-arm theorem removes one full v from that cost.

## 5. Proof status and remaining bottleneck

Theorem 1 and the shield budget (4) are analytic. Equations (9)-(13) use only current
main plus Theorem 1. Equations (14)-(20) additionally use the proof-only parent note on
this branch. No numerical search, verifier, CI output, or heuristic is a proof premise.

This does not close Target A. The remaining simultaneous-branch bottleneck is now the
quantitative inequality (13), or its sharper stacked form (20). In particular, the
proof still needs enough terminal population and/or sector imbalance to pay the
interior tube, one contact-edge per crossing source arm, and the boundary-order source
defect. The locked branch without a zero-slack source endpoint and the zero-slack
branch without a locked response fan remain separate.
