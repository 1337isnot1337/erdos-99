<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "4062632c468675ad34416163aecd88256b80501f", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_a_sector_deficit_duality_2026-09-04.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b9ea4ebd455b04fc036935c23a43b68d3b99d9fa02b8a9b6903022db0d295b11"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — Target A sector-deficit duality

**Date:** 2026-09-04  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** exact reformulation of the Section 174 endpoint  
**Target:** locked three-channel Schur sector branch  
**Status:** LEVEL I STILL OPEN

## 1. The response-corrected missing-population integer

Use the plateau-normalized notation of Sections 102, 113, and 114. Put

`s = Delta_Lambda-d_int`,

`zeta = |C^partial|-rank S`,

`h = |O|-rank S`.

Section 114 has

`Phi=|Y_0|+h`

and

`d_sc-Delta_Lambda = Phi-rho^dagger`.

Define the phasewise outer-collar deficit

`J := rho^dagger-|Y_0|`.

Then

`Delta_Lambda-d_sc = J-h`.

Call this exact survivor gap

`g := Delta_Lambda-d_sc = J-h`.

In a hypothetical Target A survivor, `g>=1` is an integer.

Section 102 also gives

`d_sc=d_int+|C^partial|-rank S`

and

`h=|O|-rank S`.

Subtracting yields

`d_sc-h=d_int+|C^partial|-|O|`.

Using `d_sc-h=Delta_Lambda-J` gives the exact global signed terminal identity

### Lemma SD1 — global terminal surplus

`|C^partial|-|O| = s-J`.

Thus the global boundary terminal surplus is short of the Schur demand `s` by exactly `J`; it is not equal to `s`.

## 2. Sector bookkeeping after a basis-closed tube shield

Let `W=widehat W_Sigma` be any basis-closed Section 174 tube shield. Let

`C_W=C^partial cap W`,

`O_W=O cap W`.

Let `O_iso` be the set of surviving exterior right vertices in `O\W` that have no surviving response neighbor in `G-W`.

By Section 174.2, every other surviving exterior vertex belongs to exactly one sector sink set `O_i`. Every surviving terminal in `C^partial\W` lies in exactly one component of `K^*\|Sigma|`, hence in exactly one `C_i^partial`. Therefore

`sum_i |C_i^partial| = |C^partial|-|C_W|`,

`sum_i |O_i| = |O|-|O_W|-|O_iso|`.

Put

`a_i := |C_i^partial|-|O_i|`.

Then Lemma SD1 gives

### Lemma SD2 — exact signed sector sum

`sum_i a_i`

`= s-J-|C_W|+|O_W|+|O_iso|`.

Define positive and negative sector masses

`P_Sigma := sum_i max(0,a_i)`,

`Q_Sigma := sum_i max(0,-a_i)`.

Then

`P_Sigma-Q_Sigma=sum_i a_i`.

## 3. Exact dual form of the Section 174 target

The three-sector population theorem (174.23) asks for

`P_Sigma >= s+|W\C^partial|`.

Since

`|W\C^partial|=|W|-|C_W|`,

substitute Lemma SD2 and `P_Sigma=sum_i a_i+Q_Sigma`. After cancellation, (174.23) is equivalent to

### Theorem SD3 — negative-sector form

`Q_Sigma >= J+|W|-|O_W|-|O_iso|`.

Equivalently,

`Q_Sigma >= J+|W\O|-|O_iso|`.

No inequality has been lost: this is algebraically equivalent to the current sufficient theorem (174.23).

Using `J=h+g`, it is also equivalent to

### Corollary SD4 — one-integer amplification form

`Q_Sigma - |W\O| + |O_iso| - h >= g`.

A hypothetical survivor has `g>=1`. Thus the locked three-channel branch can be closed by proving that its stress-generated shield increases the sectorized sink-surplus quantity on the left by at least the exact residual lattice-population gap `g`.

## 4. Interpretation

The Section 174 target is not fundamentally asking for `s` new positive terminals. The global signed terminal balance already contains `s-J`. The missing amount is the response-corrected compatible-grafting deficit `J`.

After sectorization, positive terminal surplus is created exactly when some sectors acquire compensating sink surplus. The quantity `Q_Sigma` measures that negative sector mass. The shield correction is explicit, and the remaining nonlocal obstruction is the same integer

`g=Delta_Lambda-d_sc`

that survives the full Hall-core contraction of Section 97.

This reformulation suggests a narrower target than (174.23): prove a stress-specific **one-unit sector-deficiency amplification** whenever `g>0`, then iterate or relate the amplification multiplicity to `g`.

No such amplification theorem is proved here.
