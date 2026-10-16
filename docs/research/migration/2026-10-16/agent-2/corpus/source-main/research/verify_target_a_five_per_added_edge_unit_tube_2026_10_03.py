#!/usr/bin/env python3
"""Exact integer certificate for the six-site obstruction in a one-ended unit tube."""

from itertools import combinations

def norm2(p):
    a, b = p
    return a*a + a*b + b*b

def sub(p, q):
    return (p[0]-q[0], p[1]-q[1])

def rot60(p):
    a, b = p
    return (-b, a+b)

def reflect(p):
    a, b = p
    return (a+b, -b)

def act(p, k, reflected):
    q = p
    for _ in range(k):
        q = rot60(q)
    if reflected:
        q = reflect(q)
    return q

def canonical(s):
    variants = []
    for base in s:
        translated = [sub(p, base) for p in s]
        for k in range(6):
            for reflected in (False, True):
                variants.append(tuple(sorted(act(p, k, reflected) for p in translated)))
    return min(variants)

represented_below_7 = {
    norm2((a,b)) for a in range(-3,4) for b in range(-3,4)
    if norm2((a,b)) < 7
}
assert represented_below_7 == {0,1,3,4}

points = [(a,b) for a in range(-2,3) for b in range(-2,3) if norm2((a,b)) <= 4]
assert len(points) == 19
anchor = (0,0)
others = [p for p in points if p != anchor]
anchored = []
for comb in combinations(others, 5):
    s = (anchor,) + comb
    if all(norm2(sub(x,y)) <= 4 for x,y in combinations(s,2)):
        anchored.append(frozenset(s))
assert len(anchored) == 54

orbits = {}
for s in anchored:
    c = canonical(s)
    orbits[c] = orbits.get(c,0) + 1
assert len(orbits) == 3

expected = {
    ((-2,0),(-2,1),(-2,2),(-1,0),(-1,1),(0,0)),
    ((-2,0),(-2,1),(-1,-1),(-1,0),(-1,1),(0,0)),
    ((-2,0),(-2,1),(-1,-1),(-1,1),(0,-1),(0,0)),
}
assert set(orbits) == expected

print("radius-two lattice points:", len(points))
print("anchored six-sets:", len(anchored))
print("dihedral/translation orbits:", len(orbits))
for rep in sorted(orbits):
    print("orbit multiplicity", orbits[rep], ":", rep)
