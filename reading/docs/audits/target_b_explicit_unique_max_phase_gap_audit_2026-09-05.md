> Generated reading edition · [exact source](../../../docs/audits/target_b_explicit_unique_max_phase_gap_audit_2026-09-05.md) · source SHA-256 `4b426b4df495b2a03c675dce71622a0d36c84f0e8338b045333400965668a0f2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a471b0e4615b3f5091c3fdd39adc56678d89f252", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/audits/target_b_explicit_unique_max_phase_gap_audit_2026-09-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c43cfef3c88d5006c51456991beaee78ebe65d955259eae8217a18e093a51344"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Audit — Target B explicit unique-max coherent phase gap

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_b_explicit_unique_max_phase_gap_2026-09-05.md`  
**Verdict:** PASS under its stated dense-core/coherence hypotheses.  
**Global LEVEL I status:** STILL OPEN.

## 1. Stability algebra

With

`e_AB=Mb-x`, `e_AC=Ma-y`, `e_BC=z`,

the transversal-triple inequality gives

`Mz<=ax+by`.

Hence

`Delta M^2=M(a+b)-E=x+y-z`

`>= (1-a/M)x+(1-b/M)y`

`>=kappa(x+y)`.

Thus the `A-B` missing fraction obeys

`epsilon=x/(Mb)<=Delta/(kappa tau)`.

PASS.

## 2. Dual-tree extraction

For the internally noncrossing `B` family, the complement dual is a tree. A train of `A` crosses a simple path in that tree.

If the total `A-B` missing count is `epsilon Mb`, averaging gives one backbone path with at least `(1-epsilon)b` `B` edges. With `r=sqrt(epsilon)`, at most `rM` `A` trains miss more than `rb` `B` tracks. Every retained crossing path meets the backbone in an interval and therefore contains the common central subpath after deleting `rb` backbone edges from each end.

Consequently the complete grid satisfies

`|A'|>=(1-r)M`,

`|B'|>=(1-epsilon-2r)b-O(1)`.

This uses the corrected dual-tree theorem and not the rejected assertion that the full complement dual is itself a path.

PASS.

## 3. Omitted same-phase trains are not free

Let

`L=(M-|A'|)/M+(b-|B'|)/M`.

The extraction gives

`L<=3sqrt(epsilon)+epsilon+o(1)`.

There are two distinct losses of size at most `L` in the selected diagonal estimate:

1. the retained coherent vector sums are shorter than the full ideal sums;
2. omitted `A/B` trains may themselves separate the selected diagonal with arbitrary signs.

The candidate charges both, giving

`D/M>=sqrt(F)-2L-o(1)`.

This is conservative and correct. No favorable sign is assumed for the omitted trains.

PASS.

## 4. Truly external train error

After extracting the complete positive-density grid, trim a further fixed fraction from both sides before choosing the central diagonal. The trimmed-grid penetration lemma then forces any non-`A/B/C` train separating that diagonal to cross `Omega(M)` retained grid tracks.

Since the total crossing mass involving such external trains is `o(M^2)`, only `o(M)` external trains can separate the diagonal. Their total train-coordinate contribution is therefore `o(M)`.

The quantifier order is valid: fix the auxiliary trim fraction, take the asymptotic limit, then send the trim fraction to zero. This auxiliary trim contributes no term to the final limiting constant.

PASS.

## 5. Uniform TG2 margin

Put

`c=2sqrt(3)/pi=1.1026577908...`,

`gamma_0=3/4-c/2=0.1986711045...`.

For `s<(1-t)/2`, the TG2 difference is decreasing in `s`, so at the boundary it is

`(1+t)[3(1+t)/4-c/2]>=gamma_0`.

For `s>=(1-t)/2`, use `s<=t` to get

`F-c(s+t)>=h(t):=3(1+t)^2/4-2ct`.

The minimum of `h` on the real line occurs at

`t_*=4c/3-1=0.4702103877...`

and equals

`h(t_*)=0.5841766434...>gamma_0`.

Thus the uniform margin claimed in the candidate is correct.

Also `F<=3` on the phase simplex, so `sqrt(F)<=sqrt(3)`.

PASS.

## 6. Numerical threshold

For

`epsilon_0=8*10^(-5)`,

`sqrt(epsilon_0)=0.0089442719...`

and

`L_0=3sqrt(epsilon_0)+epsilon_0`

`=0.0269128158...`.

Therefore

`4sqrt(3)L_0=0.186454...<gamma_0`,

leaving more than `0.012` of normalized squared-diameter margin before all `o(1)` terms.

The displayed theorem uses only a `0.01` residual margin, so it has explicit numerical slack.

PASS.

## 7. Global upper comparison

The hypothesis that the coherent component carries all but `o(M^2)` rhombi gives

`R/M^2=s+t-Delta+o(1)`.

Since `T=O(M)`, the pure-disk Euler identity yields

`n/M^2=s+t-Delta+o(1)`.

The strict triangular-lattice comparison therefore gives

`D^2/M^2<c(s+t-Delta)+o(1)<=c(s+t)+o(1)`,

contradicting the extracted-grid lower bound whenever `epsilon<=epsilon_0`.

PASS.

## 8. Conclusion

The explicit local gap

`liminf [M(a+b)-E]/M^2 >= 8*10^(-5) kappa tau`

is valid in the fixed-gap unique-max coherent phase regime.

It does not address the `kappa->0` two-largest-tie/balanced regime and does not by itself sum local deficits into a global contradiction.
