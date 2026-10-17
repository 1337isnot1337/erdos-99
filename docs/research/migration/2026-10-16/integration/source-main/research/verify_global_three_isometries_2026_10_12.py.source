#!/usr/bin/env python3
"""Rational interval certificate for a complete three-isometry endpoint.

Discovery was floating point; this certificate uses Fraction, integer square
roots and exact algebraic identities only. No SciPy, SymPy or floating point.
"""
if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        assert self.lo <= self.hi

    @staticmethod
    def point(x):
        return Interval(F(x), F(x))

    def __add__(self, other):
        other = other if isinstance(other, Interval) else self.point(other)
        return Interval(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        other = other if isinstance(other, Interval) else self.point(other)
        return self + (-other)

    def __rsub__(self, other):
        return self.point(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, Interval) else self.point(other)
        values = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return Interval(min(values),max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, Interval) else self.point(other)
        assert other.lo*other.hi > 0
        return self*Interval(1/other.hi,1/other.lo)

    def square(self):
        values = [self.lo**2,self.hi**2]
        return Interval(0 if self.lo <= 0 <= self.hi else min(values),max(values))

    def sqrt(self, bits=180):
        assert self.lo >= 0
        def bounds(x):
            scale = 1 << bits
            integer = isqrt(x.numerator*x.denominator*scale**2)
            denominator = x.denominator*scale
            return F(integer,denominator),F(integer+1,denominator)
        return Interval(bounds(self.lo)[0],bounds(self.hi)[1])


def cosine_root():
    # cos(2*pi/7) is the unique root in (1/2,1) of this polynomial.
    def polynomial(x):
        return 8*x**3+4*x**2-4*x-1
    lo, hi = F(1,2), F(1)
    assert polynomial(lo) < 0 < polynomial(hi)
    # Derivative 24x^2+8x-4 is >=6 throughout this interval.
    for _ in range(180):
        mid = (lo+hi)/2
        if polynomial(mid) < 0:
            lo = mid
        else:
            hi = mid
    assert polynomial(lo) < 0 < polynomial(hi)
    return Interval(lo,hi)


def squared_distance(p,q):
    return (p[0]-q[0]).square()+(p[1]-q[1]).square()


def rotation(q):
    c, s = (1-q*q)/(1+q*q), 2*q/(1+q*q)
    assert c*c+s*s == 1
    return c,s


def endpoint_certificate(parameters=None, state=None):
    c = cosine_root()
    s = (1-c.square()).sqrt()
    radius = Interval.point(1)/(2-2*c).sqrt()
    unit = (Interval.point(1),Interval.point(0))
    points = []
    cosines = []
    for _ in range(7):
        cosines.append(unit[0])
        points.append((radius*unit[0],radius*unit[1]))
        unit = (c*unit[0]-s*unit[1],s*unit[0]+c*unit[1])
    old_d2 = (1-cosines[3])/(1-c)
    assert old_d2.lo > 5
    parameters = parameters if parameters is not None else [
        (F(0),F(0),F(0)),
        (F(80223303,1000000000),F(570658219,500000000),F(-3437473,20000000)),
        (F(49087849,200000000),F(104067187,100000000),F(131086831,1000000000)),
    ]
    state = state if state is not None else [0,1,1,1,2,2,2]
    assert len(parameters) == 3
    assert all(len(row) == 3 and all(isinstance(x, F) for x in row)
               for row in parameters)
    assert len(state) == len(points) == 7
    assert all(type(x) is int and 0 <= x < len(parameters) for x in state)
    endpoint = []
    for point,group in zip(points,state):
        q,tx,ty = parameters[group]
        rc,rs = rotation(q)
        endpoint.append((rc*point[0]-rs*point[1]+tx,
                         rs*point[0]+rc*point[1]+ty))
    strict_lower = F(1000005,1000000)
    strict_upper = F(4477,1000)
    lower_pairs = upper_pairs = exact_units = mixed_pairs = 0
    for i,j in combinations(range(7),2):
        cyclic_step = min(j-i,7-(j-i))
        original = squared_distance(points[i],points[j])
        if cyclic_step == 1:
            # Exact identity: R^2(2-2c)=1, invariant under ring rotation.
            assert original.lo <= 1 <= original.hi
        else:
            assert original.lo > 1
        actual = squared_distance(endpoint[i],endpoint[j])
        if state[i] == state[j] and cyclic_step == 1:
            # Same common rational isometry preserves the exact unit length.
            assert actual.lo <= 1 <= actual.hi
            exact_units += 1
        else:
            assert actual.lo > 1
            if state[i] != state[j]:
                assert actual.lo > strict_lower
                mixed_pairs += 1
        assert actual.hi < strict_upper < old_d2.lo
        lower_pairs += 1
        upper_pairs += 1
    assert (lower_pairs,upper_pairs,exact_units,mixed_pairs) == (21,21,4,15)
    # The original regular rim also has a nonnegative normalized PSD stress.
    alpha = old_d2/7
    eigen2 = 2*(alpha*(1-cosines[2])-(1-cosines[6])/7)
    eigen3 = 2*(alpha*(1-cosines[3])-(1-cosines[2])/7)
    assert eigen2.lo > F(16,10)
    assert eigen3.lo > F(23,10)
    return {"arithmetic":"rational intervals and exact algebraic identities",
            "old_diameter_squared_lower":"5",
            "endpoint_diameter_squared_upper":"4477/1000",
            "mixed_pair_squared_lower":"1000005/1000000",
            "source_pairs":21,"endpoint_lower_pairs":lower_pairs,
            "endpoint_upper_pairs":upper_pairs,"retained_unit_contacts":exact_units,
            "mixed_pairs":mixed_pairs,"state":state,
            "parameters":[[str(x) for x in row] for row in parameters],
            "positive_stress_eigenvalue_lower_bounds":["8/5","23/10"],
            "global_optimality":"not asserted; strict endpoint disproves source globality"}


def row_benchmarks():
    results = []
    for m in (6,7,8,17,31):
        points = [(i,j) for i in range(m) for j in range(m)]
        old_d2 = 2*(m-1)**2
        theoretical_upper4 = (2*m-1)**2+3*(m-1)**2
        assert theoretical_upper4 < 4*old_d2
        maximum4 = count = 0
        for (i,j),(k,l) in combinations(points,2):
            assert (i-k)**2+(j-l)**2 >= 1
            new_d4 = (2*(i-k)+(j % 2)-(l % 2))**2+3*(j-l)**2
            assert 4 <= new_d4 <= theoretical_upper4 < 4*old_d2
            maximum4 = max(maximum4,new_d4)
            count += 1
        assert count == len(points)*(len(points)-1)//2
        results.append({"side":m,"labels":len(points),"all_pairs":count,
                        "old_diameter_squared":old_d2,
                        "endpoint_diameter_squared":str(F(maximum4,4))})
    return results


if __name__ == "__main__":
    certificate = endpoint_certificate()
    serialized = json.loads(json.dumps(certificate))
    parameters = [[F(x) for x in row] for row in serialized["parameters"]]
    assert endpoint_certificate(parameters, serialized["state"]) == certificate
    for bad_parameters, bad_state in [
        (parameters, serialized["state"][:-1]),
        ([[F(0), F(0), F(0)] for _ in range(3)], serialized["state"]),
    ]:
        try:
            endpoint_certificate(bad_parameters, bad_state)
        except AssertionError:
            pass
        else:
            raise AssertionError("corrupted endpoint certificate accepted")
    print(json.dumps({"three_isometries":certificate,
                      "witness_replay":"JSON round trip passed; truncated and identity mutations rejected",
                      "whole_source_rows":row_benchmarks()},indent=2))
