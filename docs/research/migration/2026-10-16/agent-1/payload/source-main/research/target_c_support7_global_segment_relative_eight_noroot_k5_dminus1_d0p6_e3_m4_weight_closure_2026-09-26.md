# Target C: close p6 e3 m4 by empty-space rank

Date: 2026-09-26

This note closes the remaining e=3,m=4 slice of the final eight-no-root k=5, D=-1, d_root=0, p=6 branch.

The current reduction gives a rank-three coefficient space P in Q^8 with generalized weights at least (2,4,5), exactly three touched actual-empty blocks, and four distinct tetrahedral supports. The only support multiplicity profiles are (3,3,1,1), (3,2,2,1), and (2,2,2,2).

For a touched empty block b, let E_b be its two-row local constraint space and I_b its external-coordinate support. Since E_b is contained in P, if some tetrahedral support containing b occurs at least twice, then two selected no-root orientations on that support give two independent local quotient directions at b, so dim E_b=2. The generalized weight d2(P)>=4 then forces |I_b|>=4.

If no repeated support contains b, d1(P)>=2 forces |I_b|>=2. This can occur only in the (3,3,1,1) profile at a triangle shared by the two multiplicity-one supports. The prefilter conservatively retains it as a possible rank-one empty, whether or not the actual phase directions align.

If a and b are rank-two empty blocks, then E_a and E_b are two planes in the three-space P, hence they intersect nontrivially. Every vector in their intersection is supported on I_a intersect I_b. Since d1(P)>=2, necessarily |I_a intersect I_b|>=2.

These phase-independent necessary conditions reduce the complete four-support/multiplicity census from 399 S7-orbits to 38:
- (3,3,1,1): 135 to 17;
- (3,2,2,1): 226 to 13;
- (2,2,2,2): 38 to 8.

The companion verifier enumerates every phase choice on those 38 representatives. For each retained empty triple A it forms U(A)=sum E_b exactly over Q. Since U(A) is contained in P, every source state requires rank U(A)<=3.

Exact census:
- (3,3,1,1): 153 phase configurations, 261 empty triples, rank U = 4:30, 5:107, 6:124.
- (3,2,2,1): 351 phase configurations, 405 empty triples, rank U = 5:261, 6:144.
- (2,2,2,2): 648 phase configurations, 1296 empty triples, rank U = 5:729, 6:567.

Combined: 1152 phase configurations and 1962 retained empty triples, with rank-U census {4:30, 5:1097, 6:835}. Every possible e=3,m=4 state therefore has rank U(A)>3, contradicting rank P=3.

Thus the full e=3,m=4 slice is empty. Together with the existing e=3,m=3 and e=3,m=5 closures, the entire e=3 layer is closed.

The finite census is exact computational evidence. It reconstructs the committed K8 quotient normal form using Fraction arithmetic, quotients support/multiplicity data by all 5040 vertex permutations, and hard-asserts every count above. It uses no modular rank or external relation-rank calculation.

Remaining target: e>=4 in the final D=-1,d_root=0,p=6 branch.
