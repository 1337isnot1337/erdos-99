# Target C: k6 p4 three-support closure

Date: 2026-10-04
Base main: 883a88ea86b9dfaf9d7843aa18ce0d8b6324c49d
Status: proof-only closure of the m=3 support slice in the nine-no-root k=6, D=-2, d_root=1, p=4 branch. C-II and Level I remain open.

The existing p=4 structural reduction proves that a survivor has exactly four touched singleton root blocks, every singleton is touched by at least four of the nine no-root four-cycles, and each no-root cycle touches exactly the four root triangles contained in its tetrahedral support. These inputs are proved in the worker-b k6 reduction chain carried by commit 8b6774a1de70277c88bbebf48772a49a32b5dba5.

Assume m=3 and call the three distinct tetrahedral supports F1,F2,F3. A fixed four-set supports exactly three distinct undirected four-cycle rows, so each support has multiplicity at most three. Nine rows on three supports therefore force multiplicity profile (3,3,3).

For any root triangle T, each support containing T contributes all three orientations and hence exactly three touches. A singleton needs at least four touches, so every singleton triangle must be contained in at least two of F1,F2,F3.

Two distinct tetrahedral four-sets can contain at most one common triangle: two different common three-subsets would force the four-sets to be equal. There are only three support pairs, so there are at most three distinct triangles contained in at least two of F1,F2,F3.

The branch requires four distinct singleton triangles, each contained in at least two supports. Contradiction.

Therefore there is no m=3 state in the nine-no-root k=6, D=-2, d_root=1, p=4 branch.

This is a direct incidence proof. No finite search, verifier, floating-point computation, or CI result is used. Separate exact certificates already exist for m=4,5,6; they still need current-main integration and joint audit before the full p=4 branch is promoted as canonical closure.
