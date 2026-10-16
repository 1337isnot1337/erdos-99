import math

h = math.sqrt(303.0) / 52.0
c = 1.0 / math.sqrt(1.0 + h / 2.0)
out = 2.0 * c

assert abs(c - 0.925539574680581) < 1e-15
assert abs(out - 1.851079149361162) < 2e-15

for D in (10**4, 10**6, 10**8, 10**12):
    x = float(D)
    m = math.floor(c * math.sqrt(x))
    q = math.floor(math.pi * x - 2.0 * m)
    assert q + 2*m <= math.pi*x + 1e-9
    a = math.asin(1.0/(2.0*x))
    floor = 2.0*x*math.cos((q-2)*a) - 2.0 - 2.0*(q-1)*(1.0-math.cos(a))
    assert floor > 0.0
    term_coeff = (math.pi*x-q)/math.sqrt(x)
    walk_coeff = floor/math.sqrt(x)
    if D >= 10**6:
        assert abs(term_coeff-out) < 2e-3
        assert abs(walk_coeff-out) < 2e-3

    eps = math.pi/2.0 - (math.pi*x-2.0*m-2.0)*a
    assert 0.0 < eps < math.pi/2.0
    trig = 2.0*x*math.sin(eps)
    if D >= 10**6:
        assert abs((trig-2.0*m)/math.sqrt(x)) < 2e-3

# x_B=a+d_P: a+d_P>=out*sqrt(D)-o(sqrt(D)) implies at least one is half that.
assert abs(out/2.0-c) < 1e-15

for D in (100, 10**4, 10**8):
    assert 2.0*D-2.0 > out*math.sqrt(D)

print('PASS: block-superbraid outer-walk currency arithmetic')
print(f'h_*={h:.15f}')
print(f'c_block={c:.15f}')
print(f'terminal/outerwalk coefficient={out:.15f}')
print(f'pocket split coefficient={out/2.0:.15f}')
