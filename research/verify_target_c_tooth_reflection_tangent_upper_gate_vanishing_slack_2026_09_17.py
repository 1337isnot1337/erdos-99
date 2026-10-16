import math

h = math.sqrt(303.0) / 52.0
c = 3.0 ** (1.0 / 8.0)
Cg = 17.0 / 50.0
limit = 2.0 * h * c

assert abs(limit - 0.7680475765016944) < 1e-14

for D in (1e8, 1e12, 1e16, 1e20):
    eta = 3.0 ** 0.25 * math.sqrt(D)
    L = math.sqrt(D * eta + eta * eta + Cg * D / 2.0)
    t = h + D ** (-1.0 / 3.0)
    assert t < Cg
    eps = (t * t + 4.0 * t * L) / (2.0 * D - Cg)
    scaled = eps * D ** 0.25
    assert scaled < 0.78
    assert eps < Cg

print('PASS: first upper gate has vanishing D^{-1/4} diameter slack')
print(f'leading slack constant={limit:.15f}')
