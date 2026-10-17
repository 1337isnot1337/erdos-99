# Hostile audit — train closure rank and response-free bracing

**Date:** 2026-09-12  
**Status:** audited-working proof-only material; theorem state unchanged  
**Audited source:** [train closure-rank saturation and response-free diameter bracing](target_c_train_closure_rank_and_bracing_2026-09-12.md)

## Verdict

The parallel-diameter lemma, the response-free two-sided bracing theorem, and the
exceptional-face closure-rank bound are valid under the stated canonical stopped-train,
core-only ZR/ZF, and relative-interior KKT hypotheses. The package does not close
C-II. It supplies a finite geometric restriction and an exact rank ledger; it does
not supply a quantitative conditioning bound or a finite descent through all external
rows.

## Checks

1. **Scope of the mixed framework.** The variables 'V', 'e', and 'h' are the
   nonisolated positive-contact core and its actual diameter rows. Contact-isolated
   source points never enter the affine kernel or the row count, so the package does
   not silently delete them.

2. **Parallel-diameter uniqueness.** If two diameter vectors are parallel and oriented
   alike, the cross distances are '|Du-v|' and '|Du+v|'. Their squared sum is
   '2D^2+2|v|^2', while each is at most 'D'; hence 'v=0'. The conclusion is exact for
   finite sets and does not use generic position.

3. **Shore shear.** A stopped outer train gives a Jordan shore split whose cut contacts
   all have one unit vector 'u'. Translating one shore by 'R_theta u-u' preserves
   internal contacts and changes every cut contact to the unit vector 'R_theta u'.
   All finitely many strict noncontact inequalities remain strict for sufficiently
   small 'theta'; source cardinality and all contact-isolated points are preserved.

4. **Two-sided signs.** Summing the positive contact KKT equilibrium over one shore
   gives a positive contact resultant equal to the positive combination of crossing
   diameter vectors. Its 'Ju' component is zero by stationarity on the shore shear.
   If all crossing 'r_h·Ju' have one sign, strict positivity of the diameter weights
   forces every one to vanish. Parallel-diameter uniqueness then leaves one crossing
   diameter, oriented as 'Du'. The exact squared-length formula under the shear is
   'D^2-2(D-1)(1-cos(theta))<D^2' for 'D>1'. An unchanged same-shore diameter would
   violate diameter-pair minimality; if none exists, the diameter itself decreases.
   Therefore both signs must occur.

5. **Train closure matrix.** Opposite sides of a strict rhombus force equal angular
   rates on each opposite train pair. The two coordinate closure equations for every
   bounded nonquadrilateral face, with occurrence signs retained, generate all remaining
   cycle constraints. Bounded face boundaries generate the real cycle space of a
   connected plane graph, including bridges and articulation vertices. Thus the contact
   flex quotient is 'ker C_face' modulo the constant global rotation.

6. **Rank saturation.** On a basis of non-Euclidean contact flexes, the diameter
   derivative matrix has full column rank by mixed ZF. Relative-interior KKT gives a
   strictly positive nonzero left-kernel vector. Hence the number of diameter rows is at
   least one larger than the contact-flex dimension, yielding
   'rank C_face >= T-h = 2f-s_Z'. The algebraic surplus identity
   'N_ext-[(2V_R-E_R)-r_x]=2x-2+s_Z+r_x' is exact.

## Hostile limits

- The two-sided bracing conclusion applies only to trains with two global outer-face
  endpoint occurrences. It does not apply directly to hole-ended or mixed outer/hole
  trains.
- 'rank C_face >= 2f-s_Z' is a rank statement, not a lower singular-value or angle
  bound. A near-one-dimensional face can still have full exact rank, so no asymptotic
  contradiction follows from small transverse components alone.
- The Maxwell row-count identity deliberately proves a barrier: external row counts
  have enough nominal capacity to lock the rhombic flex floor. Geometric rank on the
  train-shear subspace remains unproved.
- The finite shear is exact for the rhombus/contact subframework and for the full-source
  unit-separation/contact count, but it is not asserted to preserve all diameter rows;
  those rows are the intended locks. No strict-diameter descent is claimed without the
  sign argument's hypotheses.
- No Type-I inactive-container augmentation is supplied, and no global minimum-
  diameter theorem follows from this finite package.

**Claim classification:** audited-working finite structural theorem and explicit
rank-barrier reduction; proof-only research candidate; C-II remains open.
