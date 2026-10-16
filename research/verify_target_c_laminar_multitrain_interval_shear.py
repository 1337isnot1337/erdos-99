#!/usr/bin/env python3
"""Regression checks for the exact interval-shear derivative formulas.

This is not a proof of the topological cut theorem.  It independently checks the
finite rotation algebra in IS.11--IS.18 on randomized interval rows.
"""

from math import cos, sin, hypot
from random import Random

rng = Random(20260915)

def rot(theta, u):
    x, y = u
    return (cos(theta)*x - sin(theta)*y, sin(theta)*x + cos(theta)*y)

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def scale(s, a):
    return (s*a[0], s*a[1])

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def J(a):
    return (-a[1], a[0])

def norm2(a):
    return dot(a, a)

for trial in range(200):
    m = rng.randrange(2, 16)
    angles = [rng.uniform(-1.0, 1.0) for _ in range(m)]
    u = [(cos(a), sin(a)) for a in angles]
    lo = rng.randrange(0, m)
    hi = rng.randrange(lo+1, m+1)
    I = range(lo, hi)
    c = [rng.uniform(-1.0, 1.0) for _ in range(m)]
    phi = rng.uniform(-3.14, 3.14)
    D = rng.uniform(2.0, 30.0)
    r = (D*cos(phi), D*sin(phi))

    A = (0.0, 0.0)
    B = (0.0, 0.0)
    for i in I:
        A = add(A, scale(c[i], J(u[i])))
        B = add(B, scale(c[i]*c[i], u[i]))

    lin = 2.0*dot(r, A)
    quad = norm2(A) - dot(r, B)

    for t in (1e-4, -1e-4, 3e-5):
        rt = r
        for i in I:
            Ru = rot(t*c[i], u[i])
            delta = (Ru[0]-u[i][0], Ru[1]-u[i][1])
            rt = add(rt, delta)
        exact = norm2(rt)
        pred = D*D + t*lin + t*t*quad
        # Cubic remainder: loose scale-aware check.
        err = abs(exact-pred)
        bound = 500.0*(1.0+D+m**3)*abs(t)**3
        if err > bound:
            raise AssertionError((trial, t, err, bound))

# Exact contact identity: u + (R_theta u-u) has unit length.
for _ in range(500):
    a = rng.uniform(-3.14, 3.14)
    th = rng.uniform(-1.0, 1.0)
    u0 = (cos(a), sin(a))
    Ru = rot(th, u0)
    moved = add(u0, (Ru[0]-u0[0], Ru[1]-u0[1]))
    if abs(hypot(*moved)-1.0) > 2e-15:
        raise AssertionError('contact rotation identity failed')

print('PASS: interval-shear exact rotation and second-variation regression')
