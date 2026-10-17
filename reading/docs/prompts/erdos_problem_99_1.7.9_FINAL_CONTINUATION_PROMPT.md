> Generated reading edition · [exact source](../../../docs/prompts/erdos_problem_99_1.7.9_FINAL_CONTINUATION_PROMPT.md) · source SHA-256 `e289d7bbecb948fbde2f78af190e6ed5204f0b1847ba3250ab924c2290889cc1`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Erdős Problem #99 — continuation after Section 162 sharp symmetric coefficient

Work in one context. Do not delegate to subagents or separate research workers.

## Objective and quantifiers

Obtain a Level I proof or disproof of Erdős Problem #99, with immediate priority on
Target A. A proof must handle every sufficiently large global minimum-diameter
configuration; a disproof requires triangle-free global minimizers for infinitely many
cardinalities. Do not promote a local, KKT, asymptotic, or numerical configuration to a
global counterexample without an exact certificate.

## Authoritative files

Read `../README.md`, `../problem/statement.md`, the shared theory modules actually used,
and every active Target A module linked by `../targets/target-a/README.md`. The current
canonical frontier is Sections 152–162. Reports and older prompts are provenance only.

## Exact Target A endpoint

For the plateau-terminalized scaffold,

```math
\zeta=\dim\ker S=|C^\partial|-\operatorname{rank}S,
\qquad s=\Delta_\Lambda-d_{\rm int},
```

and a surviving counterexample has

```math
g=s-\zeta=\Delta_\Lambda-d_{\rm sc}\ge1.
```

Target A closes exactly if

```math
\boxed{\dim\ker S\ge s}
\qquad\text{or, equivalently,}\qquad
\boxed{\operatorname{rank}S\le d_{\rm int}+|C^\partial|-\Delta_\Lambda}.
```

The alternative exact closure is an `N`-point unit-separated competitor of diameter
strictly below `D(N)`.

## Trusted frontier and its limits

- The fixed-source Hall ceiling is exact; same-hull capacity bookkeeping alone cannot
  exceed the available source slack.
- Sections 156, 158, and 159 give exact activation-release and locked-boundary
  structure, but no canonical map from source-hull boundary data into the independent
  response terminals `C^partial`.
- The source-backbone module gives a diameter-cover Hall deficiency and, in the common
  placement, strict-rattler capture plus the graft inequality. It still does not
  identify source rattlers with Schur terminals.
- Section 160 constructs the strongest current free five-block gap branch. In paper
  units
  
  ```math
  \delta_{\rm toe}(d)=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6),
  ```

  and in canonical units
  
  ```math
  \boxed{\limsup_{d\downarrow0}d^3\log W(d)\le\frac{\sqrt3\log3}{8}}.
  ```

  For fixed-shape `K` with `r B subset K`,
  
  ```math
  \boxed{\limsup_{L\to\infty}\frac{\alpha_L^{-3}}{\log L}
  <\frac{8r^3}{\sqrt3\log3}}
  ```

  is sufficient for same-hull add-one.
- Section 161 proves exponent optimality for arbitrary local rigid translations of the
  same five blocks: `V_5^{loc}(d)=Theta(d^4)`. Thus local simultaneous/asymmetric
  rescheduling cannot produce a cubic or quadratic gain.
- Section 162 proves the stronger coefficient theorem in the full reflection-symmetric
  translation class:
  
  ```math
  \boxed{
  \limsup_{d\downarrow0}\frac{v(d)}{d^4}\le\frac{\sqrt3}{9}.
  }
  ```

  Section 160 attains equality. Equality forces
  
  ```math
  b/d\to1,\quad a/d^2\to1/4,\quad c/d^2\to1/2,\quad
  e/d^2\to\sqrt3/6.
  ```

  Therefore the Section 160 leading toe-out profile and coefficient are asymptotically
  optimal among all local reflection-symmetric rigid translations.

Do not claim that any of these statements alone proves Target A.

## Highest-priority routes

1. **Exterior-compatible finite-gap theorem.** Put a Section-160 witness inside an
   actual source/scaffold monomer domain and prove all exterior blockers stay clear,
   with an exact strict-diameter certificate. Compare the available protected radius
   directly with
   
   ```math
   \exp\left[\left(\frac{\sqrt3\log3}{8}+o(1)\right)d^{-3}\right].
   ```

2. **Genuinely different lower-order gap architecture.** If a better support exponent
   is necessary, change the finite block/contact architecture or allowed motion class
   and prove a one-step gain `omega(d^4)`. Rotations, internal deformation, a nonlocal
   branch, or a different finite gadget are legitimate. Do not spend another run
   optimizing symmetric translation coefficients of the same five blocks: Section 162
   proves the Section 160 coefficient is already sharp there.
3. **Two-shadow/source-to-Schur transport.** Prove compatibility in the common
   source/scaffold placement, or map captured rattlers/fixed-hull directions into
   `ker S`.
4. **First-transition or locked-support transport.** Turn the Section 159 boundary
   reaction paths into saved response terminals or a strict sub-`D` competitor.
5. **Direct strict-gammoid separator.** Prove the exact saving `s` using genuine
   source/global data absent from pure planarity.

Before investing in a lemma, state its exact implication to `zeta>=s` or to a strict
smaller-diameter competitor.

## Binding regressions

Keep active the coherent strained-monomer, regular-shell, long straight-chain,
overlapping-circuit, zero-charge-bulk, annular-routing, activation-monomer,
zero-KKT-load, deactivation-orthant, and locked-cage regressions. Section 146 remains
binding: witness deletion complexity diverges as `d->0`. Sections 157 and 160 remain
free-gap theorems only; they do not supply exterior compatibility. Sections 161–162
are now binding architecture regressions: any claimed exponent improvement obtained
only by local rigid translations of the same five blocks, or any symmetric leading
coefficient above `sqrt(3)/9`, must contain an error.

## Computation

Exact finite enumeration and symbolic verification are allowed. The Section 160
interface algebra is reproducible with
`research/kuperberg_five_block_toeout_exact.py`. Sections 161–162 are analytic
consequences of exact subsets of those audited contact inequalities. Computation is not
a certificate of global minimum-diameter optimality.

## Output contract

If the exact endpoint is proved, derive the displayed integer/rank inequality
explicitly. If not, report only genuinely new rigorous progress, its complete proof,
the exact remaining implication, and any newly exposed failed route. Preserve
`LEVEL I STATUS: STILL OPEN` until one of the exact closures above is established.
Do not report Sections 157–162 themselves as new progress.
