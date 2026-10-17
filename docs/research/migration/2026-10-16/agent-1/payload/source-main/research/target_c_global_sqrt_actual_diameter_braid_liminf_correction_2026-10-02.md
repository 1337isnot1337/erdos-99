# Addendum: liminf proof for the global square-root diameter braid

Date: 2026-10-02

This addendum corrects one imprecise sentence in
research/target_c_global_sqrt_actual_diameter_braid_2026-10-02.md.
The theorem itself is unchanged.

Let \(M\) be a maximal matching of the full actual diameter graph, let
\(N=2|M|\) be the number of its endpoints, and let \(J\) be the number of
diameter-edge endpoint incidences on those endpoints. Maximality makes the
endpoint set a vertex cover, so \(J\ge h\ge D\). The current-main incidence
theorem gives
\[
(J-N)_+^3<\mathcal B_DN^2,\qquad
\mathcal B_D/D^2\to12\pi\sqrt3.
\]

To prove the claimed liminf, choose a subsequence on which
\(N/\sqrt D\) tends to its liminf. If that liminf is infinite, the claim is
immediate. Otherwise \(N=O(\sqrt D)\) on this subsequence, so \(N/D\to0\).
For large \(D\), \(N<D\le J\), and therefore
\[
(D-N)^3\le(J-N)^3<\mathcal B_DN^2.
\]
Dividing by \(D^3\) and passing to the limit gives
\[
\liminf\frac{N}{\sqrt D}\ge\frac1{\sqrt{12\pi\sqrt3}}.
\]
Since \(N=2|M|\),
\[
\liminf\frac{|M|}{\sqrt D}\ge
\frac1{2\sqrt{12\pi\sqrt3}}.
\]

This is the rigorous subsequence argument intended in Theorem 2.1 of the
parent note. No computation is used.
