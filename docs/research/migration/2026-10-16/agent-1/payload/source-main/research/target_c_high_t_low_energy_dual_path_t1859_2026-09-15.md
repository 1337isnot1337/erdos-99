# RETRACTED — former `t<=1.859` low-energy dual-path claim

**Date:** 2026-09-15  
**Status:** **RETRACTED / DO NOT CITE AS A THEOREM**  
**Replacement:** `research/target_c_opposite_branch_dual_path_t18593_2026-09-15.md`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The original version of this note used a terminal-energy threshold `e_tau<=0.99` and inferred that all selected O--O trains had one terminal near each of the two opposite ideal phase normals.  That inference omitted the required oriented-branch argument.

The audited endpoint-energy formula bounds deviations from projective normal directions, but at this large threshold it does not by itself exclude both terminal positions using the same oriented branch.  Without a proved opposite-branch choice, the claimed two disjoint terminal arcs and complement-dual path do not follow.

Accordingly the former path/hub/finite-strip conclusions are withdrawn.  The retained-mass bootstrap arithmetic in the old note is not the source of the error; the defect is specifically the branch-orientation step.

The replacement theorem

`target_c_opposite_branch_dual_path_t18593_2026-09-15.md`

uses the nearby stronger endpoint `t<=1.8593` but lowers the extraction threshold to `lambda=0.5025` and proves the missing same-branch exclusion by comparing

\[
D\sqrt{\lambda-\lambda^2/4}
\]

with the Section-157 bracing lower bound

\[
D(1-\delta-\lambda/2).
\]

An exact certificate gives strict positive margin at the corrected endpoint.

**Disposition:** retracted and superseded by the corrected opposite-branch theorem.  Historical commits remain in Git history for auditability.