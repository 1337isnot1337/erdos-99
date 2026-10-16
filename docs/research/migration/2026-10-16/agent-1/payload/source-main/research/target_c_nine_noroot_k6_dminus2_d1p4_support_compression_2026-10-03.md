# Target C: nine-no-root k=6 p=4 support compression

Date: 2026-10-03
Base main: 0524c5b4dccc9747d3ebb978f6e82cc9021b912f
Status: exact finite support reduction; C-II and Level I remain open.

Assume the already proved p=4 root-profile reduction on the worker-b k6 branch:
four touched singleton blocks, no touched empty or pair block, every other touched
root block complete, every singleton touched by at least four no-root cycles, and
touched-complete nullity at most one.

Let F be the distinct tetrahedral four-supports of the nine no-root cycles. Their
signed tetrahedron-boundary dependencies span Z. Restriction to the four singleton
triangles has kernel contained in the touched-complete dependency space, hence
dim ker <=1 and therefore dim Z<=5.

An exact finite census of the 35 tetrahedron-boundary vectors gives:
- 630 six-support sets have rank <=5;
- no seven-support set has rank <=5;
- every one of the 630 six-support sets is uniquely the five four-faces of one
  five-vertex set W plus one extra tetrahedron G.

Thus every survivor has 3<=m<=6. If m=6, the only positive multiplicity profiles
summing to nine are (3,2,1,1,1,1) and (2,2,2,1,1,1). Up to the stabilizer of W,
|G intersect W| is 3 or 2. Exhausting all multiplicity assignments and all four
singleton triangles with touch count at least four, then checking exact rational
triangle-boundary nullity <=1 on the remaining touched complete triangles, leaves:
- |G intersect W|=3: 61 skeletons;
- |G intersect W|=2: 25 skeletons.

All 86 survivors have multiplicity (3,2,1,1,1,1) and touched-complete nullity
exactly one. The (2,2,2,1,1,1) profile has zero survivors.

This is complete support-level finite verification. Cycle orientations and the
rank-three singleton coefficient space are not yet tested, so the p=4 branch is
not closed.