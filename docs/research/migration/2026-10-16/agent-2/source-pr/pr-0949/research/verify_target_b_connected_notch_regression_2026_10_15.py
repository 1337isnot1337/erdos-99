#!/usr/bin/env python3
"""Exact rational fixtures for PR 949's connected two-block notch geometry.

The basis is (1,0),(5/13,12/13), not the report's transcendental theta_m
sequence. Checks all source pairs, actual contacts, cell/boundary/train counts,
noncrossing opposite-block train pairs and explicit nonglobal competitors.
The asymptotic estimates and global-source hypotheses require analytic proofs.
"""
if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import isqrt


def edge(a, b):
    return tuple(sorted((a, b)))


def check_case(m, gap=2):
    width = 2*m+gap
    cells = {(i, j) for j in range(m) for i in [*range(m), *range(m+gap, width)]}
    cells |= {(i, m) for i in range(width)}
    boundaries = {}
    for i, j in cells:
        cycle = [(i,j), (i+1,j), (i+1,j+1), (i,j+1)]
        boundaries[i,j] = [edge(a,b) for a,b in zip(cycle,cycle[1:]+cycle[:1])]
    multiplicity = Counter(e for sides in boundaries.values() for e in sides)
    vertices = sorted({p for e in multiplicity for p in e})
    points = {p: (F(p[0])+F(5*p[1],13), F(12*p[1],13)) for p in vertices}
    contacts, distances = set(), []
    for a,b in combinations(vertices,2):
        squared = sum((points[a][d]-points[b][d])**2 for d in (0,1))
        assert squared >= 1
        distances.append(squared)
        if squared == 1:
            contacts.add(edge(a,b))
    assert contacts == set(multiplicity), "unlisted unit contact"
    assert all((sum(a)-sum(b)) % 2 for a,b in contacts)
    assert len(cells) == len(contacts)-len(vertices)+1
    links = {e: set() for e in contacts}
    for sides in boundaries.values():
        for a,b in [(sides[0],sides[2]), (sides[1],sides[3])]:
            links[a].add(b)
            links[b].add(a)
    unseen, train_of, train_count = set(contacts), {}, 0
    while unseen:
        todo, component = [min(unseen)], set()
        while todo:
            e = todo.pop()
            if e in component:
                continue
            component.add(e)
            todo.extend(links[e]-component)
        unseen -= component
        assert sum(len(links[e]) for e in component)==2*(len(component)-1)
        for e in component:
            train_of[e]=train_count
        train_count += 1
    crossings = {edge(train_of[sides[0]],train_of[sides[1]]) for sides in boundaries.values()}
    assert len(crossings)==len(cells)
    left_u = {train_of[edge((i,0),(i+1,0))] for i in range(m)}
    right_u = {train_of[edge((i,0),(i+1,0))] for i in range(m+gap,width)}
    left_v = {train_of[edge((0,j),(0,j+1))] for j in range(m)}
    right_v = {train_of[edge((m+gap,j),(m+gap,j+1))] for j in range(m)}
    missing = {edge(a,b) for first,second in [(left_u,right_v),(right_u,left_v)]
               for a in first for b in second}
    assert len(missing)==2*m*m and not missing & crossings
    assert gap==2
    assert len(cells)==2*m*m+2*m+2
    assert sum(v==1 for v in multiplicity.values())==8*m+6
    assert train_count==4*m+3
    assert len(vertices)==2*m*m+6*m+6
    assert max(distances)==F(85,13)*(m+1)**2
    assert (width*(m+1)-len(cells))*F(12,13)==2*m*F(12,13)
    side=isqrt(len(vertices))
    if side*side<len(vertices):
        side += 1
    assert 2*(side-1)**2<max(distances)
    return len(distances), len(vertices), train_count


def main():
    cases=[check_case(m) for m in (4,5,8)]
    try:
        check_case(4,gap=1)
    except AssertionError as exc:
        assert str(exc)=="unlisted unit contact"
    else:
        raise AssertionError("one-column notch accepted without its extra contacts")
    print("PASS: rational connected-notch fixtures (pairs, labels, trains):",cases)
    print("PASS: one-column mutation rejected for extra actual unit contacts")
    print("SCOPE: finite geometry and counts; no theta_m asymptotic or global-optimality certificate")


if __name__=="__main__":
    main()
