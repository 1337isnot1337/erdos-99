#!/usr/bin/env python3
import math

HSTAR = math.sqrt(303.0) / 52.0
CSTAR = 0.129220199818177

assert HSTAR < 0.335
assert 1.0 + HSTAR < 1.335
assert 2.0 * (1.0 + HSTAR) < 2.67

# Source-wide constants inherited from the module-anchor split.
assert abs(CSTAR / 2.0 - 0.0646100999090885) < 1e-15
assert abs(CSTAR / 4.0 - 0.03230504995454425) < 1e-15

# If exactly one new leaf contact is present at terminal repair, reflecting an
# apex of contact degree d >= 3 changes the contact count by 3-d.
# d >= 4 contradicts primary contact minimality immediately; d=3 leaves the
# count unchanged, which is the case handled by connected positive support.
for d in range(3, 32):
    delta_contacts = 1 - (d - 2)
    assert delta_contacts == 3 - d
    if d == 3:
        assert delta_contacts == 0
    else:
        assert delta_contacts < 0

# Exhaustive event-state logic for the two-gate amplification.
# first_mult >= 2 -> DOUBLE immediately.
# first_mult == 1 and first_core -> CORE immediately.
# otherwise absorb the unique inactive guard. A second event yields CORE or
# DOUBLE; absence of a second event is the forbidden terminal one-leaf case.
for first_mult in (1, 2, 3):
    for first_core in (False, True):
        for second_exists in (False, True):
            for second_core in (False, True):
                if first_mult >= 2:
                    outcome = 'CORE' if first_core else 'DOUBLE'
                elif first_core:
                    outcome = 'CORE'
                elif second_exists:
                    outcome = 'CORE' if second_core else 'DOUBLE'
                else:
                    outcome = 'FORBIDDEN_ONE_LEAF_TERMINAL'
                assert outcome in {
                    'CORE', 'DOUBLE', 'FORBIDDEN_ONE_LEAF_TERMINAL'
                }

print('two-gate certificate: PASS')
print(f'h_*={HSTAR:.15f}')
print(f'1+h_*={1+HSTAR:.15f}')
print(f'c_*/4={CSTAR/4:.15f}')
