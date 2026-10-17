# Target C-II: unloaded sink witnesses spend outer-walk excess

Date: 2026-10-05. Authority: audit.62 at main 583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1.
Status: proof-only Target C reduction. C-II and Level I remain open.

Let S_1,...,S_t be pairwise disjoint binary-only sink SCCs in the acute reduced
lower system of the preceding worker notes. For each S choose |S| distinct
implication witnesses and one further distinct internal incompatibility witness.
Let u(S) count selected witnesses with at least one unloaded endpoint, and let
R(S) be the total number of cyclic loaded-hull owner runs in S. The preceding
exact sink payment is

    u(S) + R(S) - |S| >= 1.                                      (1)

This note bounds the previously unpaid u(S) term.

For the audit.61 O--O owner motion, let s be the translation-cloud diameter.
The finite motion hypothesis gives

    s < gamma_D = D-sqrt(D^2-1) = 1/(D+sqrt(D^2-1)).

Every old noncontact that becomes a lower blocker therefore has old length
1 < ell <= 1+s. For D>=6,

    gamma_D < 1/(2D-1) <= 1/11,

so ell < 12/11. Canonical near-unit geometry gives maximum degree at most six
for the source graph of pairs of length at most t whenever
t < 1/(2 sin(pi/7)). This applies because

    1/(2 sin(pi/7)) > 49/44 > 12/11,

using sin(pi/7) < pi/7 < 22/49. Hence every relevant lower witness lies in one
full-source near-unit graph of maximum degree at most six.

Let b be the occurrence-counted outer contact-face boundary-walk length and B
the q-vertex loaded force hull. Canonical loaded-hull geometry supplies one
distinguished outer occurrence of each loaded vertex. Let U_out be the distinct
unloaded nonisolated vertices incident with the outer face. Selecting one outer
occurrence of each U_out vertex together with the q distinguished loaded
occurrences gives distinct positions in the length-b outer walk. Therefore

    |U_out| <= b-q.                                               (2)

Bridges and articulation repetitions only increase b.

Let Z_out be the number of contact isolates in the outer contact face.
Audit.61's bounded-face isolate reassignment removes bounded-face isolates from
the surviving intergroup lower system. Thus every selected lower witness with
an unloaded endpoint has such an endpoint in U_out union Z_out. Assign each
such witness to one unloaded endpoint. The degree-six bound implies, for any
family W of distinct surviving lower witnesses,

    #{e in W : e has an unloaded endpoint}
        <= 6 (b-q+Z_out).                                        (3)

The chosen witness packets for disjoint sink SCCs are physically distinct.
Consequently

    sum_a u(S_a) <= 6 (b-q+Z_out).                               (4)

Summing (1) and using (4) gives the new finite Target C reduction

    t <= 6 (b-q+Z_out)
         + sum_a (R(S_a)-|S_a|).                                 (5)

In particular, if every owner in a sink occupies exactly one loaded-hull run,
then R(S)=|S| and that sink must spend an unloaded witness. Hence

    #{single-run binary sink SCCs} <= 6 (b-q+Z_out).              (6)

This does not prove satisfiability. A single sink SCC can still contain
Theta(D) owners, and loaded-owner run excess can be linear. The remaining
owner-order problem is now concentrated in (i) charging repeated loaded-owner
runs to actual stopped-train / loaded-return currency, or (ii) excluding a
small number of macroscopic sink SCCs by outer order, active-diameter
coordinates, or an explicit satisfying assignment.

Unary rhombus blockers and the at most d_H inactive upper exceptions remain
separate. The macroscopic-container branch is untouched.

Everything above is an analytic finite proof. No computation or verifier is a
proof premise.
