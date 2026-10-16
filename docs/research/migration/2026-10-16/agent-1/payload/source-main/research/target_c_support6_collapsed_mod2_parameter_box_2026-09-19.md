# Target C-II — a two-parameter collapsed closure patch is globally excluded

**Date:** 2026-09-19  
**Status:** proved candidate; theorem-state authority unchanged  
**Scope:** the regular collapsed support-six closure sheet near the certified mod-2 cell  
**Certificate:** `research/verify_target_c_support6_collapsed_mod2_parameter_box_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The prior exact certificate fixed the two free internal train angles

\[
\theta_{01}=-1.93018848,\qquad \theta_{02}=1.02838679
\]

and excluded the resulting regular local root from every global stopped-train
source by three mod-2 cycle-intersection equations. The present certificate removes
that artificial fixed-parameter restriction. It proves an exact two-parameter patch
of the local closure sheet, with the same strict rotation and crossing pattern, and
excludes the whole patch globally.

The parameter box is

\[
|\theta_{01}+1.93018848|\le10^{-4},\qquad
|\theta_{02}-1.02838679|\le10^{-4}.
\]

For every parameter pair in this box, interval Newton/Banach contraction gives a
unique solution of the ten independent face-closure equations in the solved-angle
box of radius `10^-3` about the recorded center. The exact output is

```text
parameter_radius 0.0001 solved_radius 0.001
Y 0.0008020692200950538 Z0 0.0405071517263458
Z 0.088161081419124 mapping_margin 0.00010976969848582223
```

The same box certifies the six strict convex pentagon turn conditions and the face
orders used by the earlier mod-2 proof. The three cycle pairs retain exactly the
same crossing-compatible train pairs, so the universal plane-intersection equations
remain

\[
x_{02,34}=0,qquad
x_{02,34}\oplus x_{04,34}=0,qquad
x_{04,34}=1.
\]

Their XOR is `0=1`. Therefore no point of this two-dimensional closure patch can be
embedded in a global stopped-train/rhombus source.

## Dependency chain

```text
fixed-parameter regular collapsed closure certificate
  -> rational interval Newton over a parameter rectangle
  -> constant face rotation and strict crossing sides
  -> audited mod-2 relation-cycle intersection equations
  -> 0=1, so the whole patch is globally nonintegrable
```

This is stronger than excluding a single root at one parameter value, but it remains
local in parameter space. It does not classify the 388 rotation cells, exclude the
entire collapsed branch, or provide a global source realization. The smallest live
obstruction is still the other crossing-threshold regions of the collapsed closure
family.

**Classification:** proved candidate awaiting independent promotion audit; no
canonical theorem-state files are changed.
