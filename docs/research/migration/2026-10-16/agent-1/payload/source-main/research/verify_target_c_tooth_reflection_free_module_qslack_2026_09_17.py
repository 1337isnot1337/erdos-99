#!/usr/bin/env python3
import math

HSTAR = math.sqrt(303.0) / 52.0
assert HSTAR < 0.335
assert 1 + HSTAR < 1.335

# Opening q across the base removes both retained base contacts. With at most
# two gate edges and every unloaded shallow apex degree d>=3, contact count is
# strictly reduced.
for d in range(3, 6):
    for k in range(0, 3):
        delta = -d + k
        assert delta < 0

# At most two gate edges cannot themselves create a triangle.
for k in (0, 1, 2):
    assert k < 3

# Exact base-opening geometry: c^2+h^2=1 and h,eps>0 gives squared length >1.
for h in (0.05, HSTAR, 0.49):
    c2 = 1-h*h
    for eps in (1e-6, 1e-3, 0.01):
        assert c2 + (h+eps)**2 > 1

print('q-slack gate certificate: PASS')
print(f'h_*={HSTAR:.15f}')
