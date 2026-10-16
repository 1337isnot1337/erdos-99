#!/usr/bin/env python3
"""Exact constants, marked-side count and eight-point fan-pentagon regression.

Assumes the finite geometric/canonical hypotheses explicitly listed in the report.
Checks rational lens margins, all marked subsets of cycles of sizes 3..10, and
all source/contact/diameter/reflection pairs of five exact Q(h) packets.
Also checks a seven-point Q(sqrt(3)) shared-blocker/adjacent-move regression.
Does not prove the arbitrary-size geometry, canonical source extraction, harmonic
co-embedding of the nonglobal packets, global minimality, a defect lower charge,
C-II, or Level I. The report supplies the proofs and separates those hypotheses.
Only integer/Fraction arithmetic is used; no numerical tolerance/dependencies.
"""

from fractions import Fraction as F
from itertools import combinations


def constants():
    assert F(4, 300) + F(7, 40000) < F(1, 64)
    assert F(1, 4) + (2 + F(2, 10000)) / 10000 < F(51, 200)
    assert F(51, 200) ** 2 + F(29, 30) ** 2 < 1
    assert 3 * F(29, 30) > 2 + F(2, 10000)
    assert 4 * F(31, 29) ** 2 - F(29, 15) ** 2 < 1
    assert (F(29, 15) - F(1, 5000)) ** 2 > 3
    for n in range(3, 11):
        for mask in range(1 << n):
            marked = {i for i in range(n) if mask & (1 << i)}
            sides = {i for i in range(n) if i in marked or (i + 1) % n in marked}
            assert len(sides) >= len(marked)
    print("PASS exact midpoint, normal-angle, lens and marked-side bounds")

    # Asymptotic relaxation in units pi/5, not finite graph/source data.
    q,b,t,k,sc = 5,5,3,2,2
    u,global_q,dtile,f,terminal = 1,1,1,1,5
    population,a,tr,augq = 4,4,0,0
    energy = augq+2*dtile
    assert b+global_q == 2*t
    assert population+u == q and k==sc
    assert 2*sc == a+tr-augq
    assert population+energy == 2*t
    assert terminal >= q and terminal <= t+2*f and f<=global_q
    assert augq == 2*t-q-u and dtile==u and energy==2*t-q+u
    assert energy < population
    print("PASS exact surviving normalized currency relaxation (no source claim)")


def packet(k):
    c, s = F(k*k-1, k*k+1), F(2*k, k*k+1)
    rho = 1 - (c - F(1, 2)) ** 2
    diameter = 1 / (2*s)
    # A pair (a,b) represents a+b sqrt(rho).
    def add(x, y):
        return (x[0] + y[0], x[1] + y[1])
    def sub(x, y):
        return (x[0] - y[0], x[1] - y[1])
    def mul(x, y):
        return (x[0]*y[0] + rho*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
    def sign(x):
        a, b = x
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        cmp = (a*a > b*b*rho) - (a*a < b*b*rho)
        return cmp if a > 0 else -cmp
    def point(x, y, yh=0):
        return ((F(x), F(0)), (F(y), F(yh)))
    def distance2(p, q):
        return add(mul(sub(p[0],q[0]), sub(p[0],q[0])),
                   mul(sub(p[1],q[1]), sub(p[1],q[1])))
    def orient(p, q, r):
        return sub(mul(sub(q[0],p[0]), sub(r[1],p[1])),
                   mul(sub(q[1],p[1]), sub(r[0],p[0])))
    points = [
        point(c, s-diameter),
        point(c-2*c*(1-2*s*s), s-4*s*c*c),
        point(0,0), point(c,s), point(2*c,0),
        point(c+2*c*(1-2*s*s), s-4*s*c*c),
        point(c-F(1,2),0,-1), point(c+F(1,2),0,-1),
    ]
    contacts, diameters = set(), set()
    for i,j in combinations(range(8),2):
        d2 = distance2(points[i],points[j])
        assert sign(sub(d2,(F(1),F(0)))) >= 0
        assert sign(sub(d2,(diameter**2,F(0)))) <= 0
        if sign(sub(d2,(F(1),F(0)))) == 0:
            contacts.add((i,j))
        if sign(sub(d2,(diameter**2,F(0)))) == 0:
            diameters.add((i,j))
    assert contacts == {(1,2),(2,3),(3,4),(4,5),(2,6),(4,7),(6,7)}
    assert diameters == {(0,j) for j in range(1,6)}
    for i,j,l in combinations(range(8),3):
        assert not {(i,j),(i,l),(j,l)} <= contacts
    cycle = [2,3,4,7,6]
    for i in range(5):
        a,b = cycle[i],cycle[(i+1)%5]
        assert all(sign(orient(points[a],points[b],points[z])) < 0
                   for z in cycle if z not in (a,b))
    for z in (0,1,5):
        assert any(sign(orient(points[cycle[i]],points[cycle[(i+1)%5]],points[z])) > 0
                   for i in range(5))
    reflected = point(c,s-1/diameter)
    assert distance2(reflected,points[2]) == (F(1),F(0))
    assert distance2(reflected,points[4]) == (F(1),F(0))
    assert all(sign(sub(distance2(reflected,points[z]),(F(1),F(0)))) < 0 for z in (6,7))
    competitor = [points[0]] + [(p[0],sub(p[1],(F(1,10),F(0)))) for p in points[1:]]
    for p,q in combinations(competitor,2):
        d2 = distance2(p,q)
        assert sign(sub(d2,(F(1),F(0)))) >= 0
        assert sign(sub(d2,(diameter**2,F(0)))) < 0
    assert c*c+s*s == 1 and c>F(1,2) and rho>0
    assert (1-c)*(2*c+1)>0
    print(f"PASS exact eight-point fan/pentagon source: k={k}, D={diameter}")


def shared_blocker():
    k = 100000
    c, s = F(k*k-1,k*k+1), F(2*k,k*k+1)
    diameter = 1/(2*s)
    # Coordinates here are pairs representing a+b sqrt(3).
    def point(x,y):
        return ((F(x),F(0)),(F(y),F(0)))
    def sign(x):
        a,b = x
        if b == 0:
            return (a>0)-(a<0)
        if a*b >= 0:
            return 1 if a>0 or b>0 else -1
        cmp = (a*a>3*b*b)-(a*a<3*b*b)
        return cmp if a>0 else -cmp
    def d2(p,q):
        x,xb = p[0][0]-q[0][0],p[0][1]-q[0][1]
        y,yb = p[1][0]-q[1][0],p[1][1]-q[1][1]
        return (x*x+3*xb*xb+y*y+3*yb*yb, 2*x*xb+2*y*yb)
    def cmp_sq(p,q,bound):
        a,b = d2(p,q)
        return sign((a-bound,b))
    source = [point(c,s-diameter),
              point(c-2*c*(1-2*s*s),s-4*s*c*c),
              point(0,0),point(c,s),point(2*c,0),
              point(c+2*c*(1-2*s*s),s-4*s*c*c),
              ((c/2+s/(4*diameter),s/2),(s/2-c/(4*diameter),-c/2))]
    contacts, diameters = set(),set()
    for i,j in combinations(range(7),2):
        assert cmp_sq(source[i],source[j],1)>=0
        assert cmp_sq(source[i],source[j],diameter**2)<=0
        if cmp_sq(source[i],source[j],1)==0:
            contacts.add((i,j))
        if cmp_sq(source[i],source[j],diameter**2)==0:
            diameters.add((i,j))
    assert contacts == {(1,2),(2,3),(3,4),(4,5)}
    assert diameters == {(0,j) for j in range(1,6)}
    moves = {}
    for i in (2,3):
        a = source[0]
        moved = tuple((source[i][j][0]+(a[j][0]-source[i][j][0])/diameter**2,F(0))
                      for j in (0,1))
        moves[i] = moved
        assert cmp_sq(moved,source[6],1)<0
        # Solo feasibility without the unary inactive blocker, on all source pairs.
        packet_without_blocker = source[:6]
        packet_without_blocker[i] = moved
        for p,q in combinations(packet_without_blocker,2):
            assert cmp_sq(p,q,1)>=0 and cmp_sq(p,q,diameter**2)<=0
    assert d2(moves[2],moves[3]) == ((1-1/diameter**2)**2,F(0))
    assert cmp_sq(moves[2],moves[3],1)<0
    print("PASS seven-point shared strict blocker and incompatible adjacent reflections")


if __name__ == "__main__":
    constants()
    for sample in (100,1000,10000,100000,1000000):
        packet(sample)
    shared_blocker()
    print("Scope: finite geometry and arithmetic; packets are nonglobal and nonharmonic.")
