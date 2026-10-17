#!/usr/bin/env python3
"""Regression certificate for the weighted outer hidden-rank minimax theorem.

Pure stdlib. Checks the private-face rank table algebra, weighted ledger reduction,
minimax inequality, Pareto tradeoff, equality model, and the current t_21 endpoint.
"""
from decimal import Decimal, getcontext
from fractions import Fraction as Fr
from itertools import product

# Local hidden-rank lower table h(r), r=1,...,5.
h = {1: Fr(0), 2: Fr(0), 3: Fr(1), 4: Fr(2), 5: Fr(2)}
gamma = {1: Fr(0), 2: Fr(0), 3: Fr(1, 3), 4: Fr(2, 3), 5: Fr(0)}
for r in range(1, 6):
    assert h[r] == Fr(2, 3) * max(r - 2, 0) + gamma[r]

# Exact finite receiving-face identities.
for counts in product(range(4), repeat=5):
    N = {r: counts[r - 1] for r in range(1, 6)}
    G = sum(N.values())
    L_of = sum(r * N[r] for r in range(1, 6))
    rho = sum(max(r - 2, 0) * N[r] for r in range(1, 6))
    s2 = sum(min(r, 2) * N[r] for r in range(1, 6))
    zlow = sum(h[r] * N[r] for r in range(1, 6))
    beta = Fr(1, 3) * N[3] + Fr(2, 3) * N[4]
    assert L_of == s2 + rho
    assert s2 == 2 * G - N[1]
    assert zlow == Fr(2, 3) * rho + beta

# Symbolic endpoint algebra: R - 2q0 = 2F.
def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fr(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(c, a):
    return {k: c * v for k, v in a.items() if c * v}


R = {
    "pi": Fr(7),
    "Cg": Fr(3),
    "t": Fr(-27, 2),
    "delta": Fr(7),
    "kappa": Fr(3, 2),
}
q0 = {"pi": Fr(-1), "t": Fr(2), "delta": Fr(-1)}
Rm2q = add(R, scale(Fr(-2), q0))
assert Rm2q == {
    "pi": Fr(9),
    "Cg": Fr(3),
    "t": Fr(-35, 2),
    "delta": Fr(9),
    "kappa": Fr(3, 2),
}
Fsym = scale(Fr(1, 2), Rm2q)
Theta = scale(Fr(4, 7), Fsym)
assert Theta == {
    "pi": Fr(18, 7),
    "Cg": Fr(6, 7),
    "t": Fr(-5),
    "delta": Fr(18, 7),
    "kappa": Fr(3, 7),
}

# Scalar implication. a = 2Q/D - s2 >= 0 and beta >= 0.
# If z >= (2/3)rho+beta and 2x+rho >= 2F+a, then
# m=max(x,z) >= (4/7)F+(2/7)a+(3/7)beta.
vals = [Fr(i, 2) for i in range(9)]
checked = 0
for x, rho, z, a, beta in product(vals, vals, vals, vals[:5], vals[:5]):
    if z < Fr(2, 3) * rho + beta:
        continue
    m = max(x, z)
    # Strongest F allowed by the weighted inequality for this tuple.
    F0 = (2 * x + rho - a) / 2
    rhs = Fr(4, 7) * F0 + Fr(2, 7) * a + Fr(3, 7) * beta
    assert m >= rhs

    # With k_out >= x+rho and m>=x, k_out+m >= 2F+a.
    k0 = x + rho
    assert k0 + m >= 2 * F0 + a
    checked += 1
assert checked > 0

# Equality fingerprint at a=beta=0.
F0 = Fr(7)
m0 = Fr(4, 7) * F0
rho0 = Fr(3, 2) * m0
n5 = rho0 / 3
x0 = z0 = m0
k0 = x0 + rho0
u0 = x0 + n5  # OO shears + one common-rotation mode per r=5 face.
assert n5 == m0 / 2
assert z0 == 2 * n5
assert k0 == Fr(10, 7) * F0
assert u0 == Fr(6, 7) * F0
assert k0 - F0 == Fr(3, 7) * F0

# High-precision current safe endpoint, using the symbolic formula itself.
getcontext().prec = 70
D = Decimal
pi = D("3.141592653589793238462643383279502884197169399375105820974944592307816")
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s = Delta2.sqrt()
g = D("0.0021")
Cg = D(2) * s + g
t21 = D(4) / D(9) * (pi + s) + D("0.0017279")
q = D(2) * t21 - pi
Rnum = D(7) * pi + D(3) * Cg - D(27) / D(2) * t21
Fnum = (Rnum - D(2) * q) / D(2)
theta = D(4) * Fnum / D(7)
k_eq = D(10) * Fnum / D(7)
k_gap = D(3) * Fnum / D(7)
u_eq = D(6) * Fnum / D(7)
n5_eq = theta / D(2)

# Tight windows catch stale copied constants.
assert abs(q - D("0.5008902223690961698008711140858835913764")) < D("1e-39")
assert abs(Rnum - D("3.124566003589793238462643383279502884197")) < D("1e-39")
assert abs(Fnum - D("1.061392779425800449430450577553867850722")) < D("1e-39")
assert abs(theta - D("0.6065101596718859711031146157450673432698")) < D("1e-39")
assert abs(k_eq - D("1.516275399179714927757786539362668358175")) < D("1e-39")
assert abs(k_gap - D("0.4548826197539144783273359618088005074524")) < D("1e-39")
assert abs(u_eq - D("0.9097652395078289566546719236176010149048")) < D("1e-39")
assert abs(n5_eq - D("0.3032550798359429855515573078725336716349")) < D("1e-39")

print("finite face-count tuples checked:", 4**5)
print("scalar grid cases checked:", checked)
print("t21 =", t21)
print("q0 =", q)
print("R =", Rnum)
print("F =", Fnum)
print("Theta =", theta)
print("K_out at minimax equality =", k_eq)
print("kernel excess over F =", k_gap)
print("hidden-null structured load =", u_eq)
print("r=5 face density at equality =", n5_eq)
print("PASS")
