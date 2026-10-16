import math

h = math.sqrt(303.0) / 52.0
c = 1.0 / math.sqrt(2.0 + h / 2.0)
out = 2.0 * c

assert abs(c - 0.679255355387642) < 1e-15
assert abs(out - 1.358510710775284) < 2e-15

for D in (10**4, 10**6, 10**8, 10**12):
    x = float(D)
    m = math.floor(c * math.sqrt(x))
    q = math.floor(math.pi * x - 2.0 * m)
    assert q + 2 * m <= math.pi * x + 1e-9
    a = math.asin(1.0 / (2.0 * x))
    floor = 2.0*x*math.cos((q-2)*a) - 2.0 - 2.0*(q-1)*(1.0-math.cos(a))
    assert floor > 0.0
    tc = (math.pi*x-q)/math.sqrt(x)
    dc = floor/math.sqrt(x)
    if D >= 10**6:
        assert abs(tc-out) < 2e-3
        assert abs(dc-out) < 2e-3
    eps = math.pi/2.0 - (math.pi*x-2.0*m-2.0)*a
    assert 0.0 < eps < math.pi/2.0
    tf = 2.0*x*math.sin(eps)
    if D >= 10**6:
        assert abs((tf-2.0*m)/math.sqrt(x)) < 2e-3

for D in (100, 10**4, 10**8):
    assert 2.0*D-2.0 > out*math.sqrt(D)

print('PASS: optimized superbraid outer-walk currency arithmetic')
print(f'h_*={h:.15f}')
print(f'c_opt={c:.15f}')
print(f'2*c_opt={out:.15f}')
