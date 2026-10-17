# Target C: common six-block puncture basis for the remaining `k=6, D=-1` Profile A

Date: 2026-09-22

Status: proved a stronger necessary condition and implemented it as an exact rational wrapper around the coverage-correct Profile A audit. No closure is claimed until the finite cover executes.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d2_profile_a_common_functional_basis_2026_09_22.py`

## 1. Input profile

A surviving synchronized six-row Profile A state has rank-two coefficient space, virtual deficiency two, exactly five singleton replacement blocks and one distinct pair replacement block. Its replacement-functional quotient has dimension

```text
s_6 = 6 - 2 + 2 = 6.
```

The six actual replacement classes span that quotient. Since there are exactly six of them, they form a basis.

Every one-coordinate puncture preserves coefficient rank two and has virtual deficiency two, so each five-row replacement-functional quotient has dimension

```text
s_5 = 5 - 2 + 2 = 5.
```

## 2. Common-basis lemma

Fix the five singleton states and the pair state of the six-row Profile A realization. For puncture `i`, functoriality gives a surjective quotient map

```text
pi_i : V_6 -> V_{5,i}.
```

A source replacement class maps to the corresponding punctured replacement class when its block remains virtual-canonical complete and maps to zero otherwise. Therefore the images of the same six fixed source classes must span `V_{5,i}`.

Since `dim V_6=6` and `dim V_{5,i}=5`, the kernel has dimension one. The already committed block-count test follows immediately: at most one of the six basis blocks can disappear under a puncture. But that count is not sufficient. If all six blocks survive, their punctured classes may still span dimension below five; if one disappears, the remaining five classes may be dependent.

The exact necessary condition is therefore

```text
rank(pi_i({five fixed singleton classes, fixed pair class})) = 5
```

for all six punctures simultaneously.

## 3. Singleton-state uniqueness

On a virtual-canonical complete block the three singleton constraints are represented, up to scalar, by `y`, `x`, and `x+y`. If two singleton states were compatible with the rank-two coefficient space, both `x` and `y` would lie in that space, giving the canonical-empty condition. Thus each of the five singleton-compatible complete blocks has exactly one singleton state.

There is no hidden product of singleton-state choices. The only remaining local choice is the pair state on the sixth replacement block; the three pair masks are tested individually.

## 4. Exact implementation

The wrapper imports the existing coverage-correct Profile A verifier and replaces only its pair-option filter. For every candidate pair block and pair state it reconstructs each of the six five-row punctures and computes the exact quotient rank of the descended five singleton classes plus that same pair class.

Classes whose blocks cease to be virtual-canonical complete are represented by zero, exactly as required by puncture functoriality. Classes whose blocks remain complete use the same singleton or pair state as at six rows.

All new ranks use direct Python `Fraction` elimination over `Q`. The base verifier still checks the six-row mixed rank, exact rank-two/d=2 puncture profile, and its existing certified modular relation ranks.

A genuine Profile A realization must therefore survive the new common-basis filter. A full 20,451-orbit result with zero survivors rigorously excludes Profile A.

## 5. Remaining bottleneck

The mathematical endpoint is now stricter than the previous survival-count audit: one fixed six-class basis must map onto all six five-row quotients. Execution remains the bottleneck; the GitHub Actions runner failures seen on the earlier audits occur before any job step and do not provide a mathematical census.
