# Target C r=2 local-rank repair

This replaces the old r=2 support certificate's unsafe use of nonrepetition as a local-rank-one test.

For fixed disjoint weight-two supports M1,M2, let E* contain every repeated-support block of incidence at least 4, and every nonrepeated block of incidence at least 3, plus two-incidence blocks whose occurrence support is M1 or M2. Every actual-empty block lies in E*: rank one uses d1(P)>=2 and the only weight-two lines are M1,M2; rank two uses d2(P)>=4.

Let S* contain blocks surviving both sharp punctures, with incidence at least 2, and at least 4 when a support repeats. Every actual selected singleton lies in S*.

For the actual singleton triple S, C*=T\(E* union S) is a subset of the actual complete set. Since d_root=0, H(C*) is independent, and its face-local capacity is at least 4.

The executed exact verifier checks all 27,763 size-eight support orbits and all 210 disjoint pairsets. It tests 5,830,230 orbit/pairset cases and 2,437,069 eligible singleton triples. Structural passes: 0. Survivors: 0.

Thus the r=2 three-singleton branch remains closed without the false converse.
