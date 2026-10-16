# Target C: close the h=5,m=6 multiplicity (3,1,1,1,1,1) profile

Date: 2026-09-25

Status: executed exact finite certificate, using the current-main coordinate model and the support-nullity reduction on this branch.

The preceding support-nullity compression leaves exactly two six-support families up to S7:

A={1234,1235,1236,1245,1345,2345},
B={1234,1235,1245,1267,1345,2345}.

For multiplicity (3,1,1,1,1,1), one support contributes all three no-root four-cycles and each other support contributes one. The stabilizers of A and B have orders 12 and 24. Their orbits on the possible triple support are:

A: {1234,1235}, {1236}, {1245,1345,2345}.
B: {1234,1235,1245}, {1267}, {1345,2345}.

Thus it is enough to scan the six representatives 1234,1236,1245 in A and 1234,1267,1345 in B.

For every representative the exact scan enumerated all 3^5=243 choices of the single cycle on the other five supports. It then enumerated all five-singleton sets S whose deletion leaves the touched complete-root rows independent. There are 450 such S in A and 500 in B. For each S it enumerated all local singleton directions that can satisfy d1>=3, retained exactly rank(P)=3 states with generalized weights (d1,d2,d3)>=(3,4,6), constructed the five external relation rows in the committed 15-dimensional relation coordinate model, and computed their rank increment over the independent complete-root span.

Exact representative results:

A, triple 1234: 27468 admissible rank-three generalized-weight states, increment census {0:27468}, max relation-row norm^2 76.
A, triple 1236: no generalized-weight-admissible rank-three state.
A, triple 1245: 29164 admissible states, increment census {0:29164}, max norm^2 86.

B, triple 1234: 20736 admissible states, increment census {0:20736}, max norm^2 76.
B, triple 1267: no generalized-weight-admissible rank-three state.
B, triple 1345: 20736 admissible states, increment census {0:20736}, max norm^2 38.

Weighting by the triple-support stabilizer-orbit sizes gives 246108 admissible states on the two canonical support families, all with external increment zero.

The rank computation used P=2^127-1. Lucas-Lehmer passed, and P^2>86^15, so the standard repository Hadamard argument certifies the modular rank decisions over Q.

A survivor in D=-2,d_root=0,p=5 requires external increment exactly five. Therefore the entire h=5,m=6 multiplicity profile (3,1,1,1,1,1) is empty.

The remaining m=6 multiplicity profile is (2,2,1,1,1,1). The h=5 cases with m=3,4,5 and the separate D=-1,(d_root,p)=(0,6) branch also remain open.
