#!/usr/bin/env python3
"""High-precision independent arithmetic check for M23 structural propagation."""
from decimal import Decimal as D, getcontext

getcontext().prec = 90
PI = D("3.141592653589793238462643383279502884197169399375105820974944592307816406286")
SQ3 = D(3).sqrt()
DELTA = PI / (2 * SQ3)
s = DELTA.sqrt()
g = D("0.002123")
Cg = 2 * s + g
C146 = D(4) / D(9) * (PI + s)
t = C146 + D("0.0017327")
A = D(9) * t / D(4) - PI - Cg / D(2)
assert abs(A - D("0.002837075")) < D("1e-70")

P = PI + Cg - D("2.5") * t
Smax = 5 * t - 2 * PI - 2 * s - g
Lmax = Smax / 2
U = P - Lmax
U_symbolic = 2 * PI + 3 * s + D("1.5") * g - 5 * t
assert abs(U-U_symbolic) < D("1e-70")
assert U > D("0.03707703")
assert U / 9 > D("0.00411967")
assert U / 4 > D("0.00926925")
assert (2 * PI + 3 * s + D("1.5") * g) / 5 > D("1.82866164")

W = PI - 6 * A
R = 2 * PI - 2 * t - 5 * A
J = (R - 2 * W / 3) / 52
assert W / 3 > D("1.04152340")
assert J > D("0.01045116")

B = t / 4 + Cg / 6
Mphys = t / 8 + Cg / 12
assert B > D("0.77310299")
assert Mphys > D("0.38655149")
assert abs(B/2-Mphys) < D("1e-70")

R171 = D("4.5") * t - 2 * PI - Cg
curv = (t - 2 * R171) / 2
assert abs(R171 - D("0.00567415")) < D("1e-70")
assert curv > D("0.90494896")

print("PASS: M23 endpoint structural propagation")
for name, value in [
    ("s", s), ("t23", t), ("A23", A), ("P23", P),
    ("loaded cap", Lmax), ("unloaded floor", U),
    ("H4 floor", U/9), ("E3 floor", U/4),
    ("W23/3", W/3), ("J_leaf floor", J),
    ("boundary-atom floor", B), ("physical max floor", Mphys),
    ("curvature max floor", curv),
]:
    print(f"{name}: {value}")
