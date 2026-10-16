# Target C — C95 contact-activation pocket frontier

**LEVEL I STATUS: STILL OPEN.**

Full proof: [target_c_contact_activation_pockets_2026-09-01.md](../../reports/target_c_contact_activation_pockets_2026-09-01.md).

C94 leaves a macroscopic exact active-face tangent flat in the low-train chain branch.
C95 classifies the first new unit-contact event along any triangle-free continuation
that preserves the old pure-rhombic contact graph up to that event.

A new unit segment cannot cross an old unit edge: choosing the shorter endpoint piece
on each of two crossing unit segments would produce two source points at distance
strictly below one. It also cannot pass through a third source point. Hence its
relative interior lies in one face of the old plane contact graph.

If that face is a bounded unit rhombus, the new edge is a unit diagonal and immediately
creates a unit equilateral triangle. Therefore every triangle-free new contact lies in
the outer face.

Since the chord lies inside the convex hull, it lies in one convex indentation pocket
from the Oler-shell decomposition and closes a convex subpocket. If the old boundary
subchain has `r` unit edges, Oler gives

`area >= c_0(r-1)`, `c_0=sqrt(3)/4`.

The case `r=2` is already an equilateral triangle, so every triangle-free activation
has `r>=3` and consumes at least

`sqrt(3)/2 = 0.8660254037...`

of pre-existing shell area defect `G`.

Simultaneous first contacts form a noncrossing outerplanar chord family, but their
subpockets can be nested, so the individual area charges cannot yet be summed.

The remaining activation-boundary theorem is therefore precise: either extract
`Omega(D)` nonnested first-contact pockets from C94's macroscopic flat, or prove that a
nested outer-pocket family plus repeated new-diameter events cannot block all those
exact active-face directions.