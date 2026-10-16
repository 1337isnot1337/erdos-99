#!/usr/bin/env python3
"""Regression checks for the vanishing-mass coercive cancellation kernel."""

import itertools
import math

z0 = 2.0477
d0 = z0 - 6.0 * math.sin(z0 / 6.0)
cH = 0.4143 + d0

assert 0.45381 < cH < 0.45383
assert 0.90763 < 2.0 * cH < 0.90765
assert 0.64179 < math.sqrt(2.0) * cH < 0.64181
assert 1.28359 < 2.0 * math.sqrt(2.0) * cH < 1.28361

# Adjacent dipoles d_i=e_i-e_{i+1} form a basis of the zero-sum
# hyperplane. For c=B s, verify the dimension-free norm inequalities
# ||c||_inf <= 2||s||_inf and ||c||_2 <= 2||s||_2.
for m in range(1, 6):
    for s in itertools.product(range(-2, 3), repeat=m):
        if not any(s):
            continue
        c = [0] * (m + 1)
        for i, x in enumerate(s):
            c[i] += x
            c[i + 1] -= x
        assert sum(c) == 0
        sinf = max(abs(x) for x in s)
        cinf = max(abs(x) for x in c)
        s2 = math.sqrt(sum(x * x for x in s))
        c2 = math.sqrt(sum(x * x for x in c))
        assert cinf <= 2 * sinf
        assert c2 <= 2 * s2 + 1e-12

        # If every local two-entry derivative block has magnitude at least
        # 2*cH*D*|s_i| on both signs (set D=1), the selected-row l2 norm
        # is at least 2*sqrt(2)*cH*||s||_2 and hence sqrt(2)*cH*||c||_2.
        lower_from_s = 2.0 * math.sqrt(2.0) * cH * s2
        lower_from_c = math.sqrt(2.0) * cH * c2
        assert lower_from_s + 1e-12 >= lower_from_c

        # The two-sided l-infinity cusp similarly gives cH*||c||_inf.
        two_sided_from_s = 2.0 * cH * sinf
        two_sided_from_c = cH * cinf
        assert two_sided_from_s + 1e-12 >= two_sided_from_c

# Reconstruction: every small integer zero-sum c has a unique adjacent-dipole
# coefficient sequence s given by prefix sums.
for m in range(1, 6):
    for prefix in itertools.product(range(-2, 3), repeat=m):
        c = list(prefix)
        c.append(-sum(prefix))
        if max(abs(x) for x in c) > 6:
            continue
        s = []
        running = 0
        for j in range(m):
            running += c[j]
            s.append(running)
        rebuilt = [0] * (m + 1)
        for i, x in enumerate(s):
            rebuilt[i] += x
            rebuilt[i + 1] -= x
        assert rebuilt == c

print("PASS: vanishing-mass coercive cancellation-kernel regressions")
print("c_H =", cH)
print("two-sided l_inf coefficient =", cH)
print("Euclidean normalized singular-value floor =", math.sqrt(2.0) * cH)
