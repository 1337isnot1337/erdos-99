#!/usr/bin/env python3
"""Exact finite corroboration of boundary-strip/Euler/currency crop accounting.

The infinite saturated Delaunay tilings here are explicit lattices. Samples
are not arbitrary-container proofs and supply no canonical source endpoint.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g


def case(m, c, h):
    triangular = c == F(1, 2)
    h2 = F(3, 4) if triangular else h*h
    assert c*c+h2 == 1
    assert 0 <= c <= F(1, 2)
    q = g.Q(0, F(1, 2)) if triangular else g.Q(h)
    a = g.Q(0, F(1, 4))
    assert (q*F(1,2)-a).sign() >= 0

    def norm(p):
        i, j = p
        return i*i+j*j+2*c*i*j

    lower = 0
    for i in range(-m, m+1):
        for j in range(-m, m+1):
            if i or j:
                assert norm((i,j)) >= 1
                lower += 1
    # The short-diagonal acute triangles tile the plane. The local incircle
    # test follows from their opposite-angle sums, strictly less than pi
    # across long side edges and at most pi across short diagonals.
    assert F(1, 2)/(1+c) < 1  # circumradius squared
    assert 1-c > 0 and c > 0  # all three triangle angles acute

    def inside(p):
        i,j=p
        return 0 <= i <= m and 0 <= j <= m and i+2*j <= 2*m+1

    def deep(p):
        i,j=p
        gaps=[i,m-i,j,m-j]
        return all(gap*gap*h2 > 4 for gap in gaps) and \
            (2*m+1-i-2*j)**2*h2 > 4*(5-4*c)

    points={(i,j) for i in range(m+1) for j in range(m+1) if inside((i,j))}
    strip={p for p in points if not deep(p)}
    removed={p for p in points if deep(p) and p[0] == m//2 and p[1]%3 == 0}
    old=points-removed
    triangles=[]
    for i in range(m):
        for j in range(m):
            for t in [((i,j),(i+1,j),(i,j+1)),
                      ((i+1,j+1),(i,j+1),(i+1,j))]:
                if all(inside(p) for p in t):
                    triangles.append(t)
    verts=set(); edges={}; stars={p:[] for p in points}
    for idx,t in enumerate(triangles):
        verts.update(t)
        for p in t:stars[p].append(idx)
        for e in combinations(t,2):
            key=tuple(sorted(e));edges[key]=edges.get(key,0)+1
    assert all(v in (1,2) for v in edges.values())
    boundary=[e for e,k in edges.items() if k == 1]
    assert all(set(e) <= strip for e in boundary)
    assert all(len(stars[p]) == 6 for p in points-strip)
    graph={p:set() for p in verts}
    for p,r in edges:
        graph[p].add(r);graph[r].add(p)
    components=[]; unseen=set(verts)
    while unseen:
        seed=next(iter(unseen)); found={seed};todo=[seed];unseen.remove(seed)
        while todo:
            for r in graph[todo.pop()]:
                if r in unseen:unseen.remove(r);found.add(r);todo.append(r)
        assert found & strip
        components.append(found)
    chi=len(verts)-len(edges)+len(triangles)
    assert len(triangles) == 2*len(verts)-len(boundary)-2*chi
    assert chi <= len(components) <= len(strip)
    assert len(boundary) <= 24*len(strip)
    assert len(triangles) >= 2*len(old)-28*len(strip)
    # C lies in a unit-side m-by-m parallelogram, hence perimeter<=4m.
    # pi>3 gives the rational relaxation of the strip bound below.
    assert len(strip) <= F(80*m,3)+25
    axial_area=F(m*m)-F((m-1)**2,4)
    area=q*axial_area
    slack_upper=g.Q(2*area.b, F(2,3)*area.a)+2*m+1-len(old)
    assert slack_upper.sign() >= 0
    assert (slack_upper-len(removed)).sign() >= 0
    sigma=(q*F(1,2)-a)*len(triangles)
    budget=2*a*slack_upper+28*a*len(strip)
    assert sigma.sign() >= 0 and (budget-sigma).sign() >= 0
    # These examples have zero metric/combinatorial bad bulk triangles;
    # their nonzero excess in the rational rhombus case is retained.
    assert (q*F(1,2)-a-F(1,100)).sign() < 0
    return {'M':m,'cosine':str(c),'sine': 'sqrt(3)/2' if triangular else str(h),
            'old_source_labels':len(old),'auxiliary_additions':len(removed),
            'strip_points':len(strip),'bulk_triangles':len(triangles),
            'bulk_vertices':len(verts),'boundary_edges':len(boundary),
            'components':len(components),'euler_characteristic':chi,
            'lower_difference_checks':lower,'deep_valence_six':len(points-strip),
            'total_triangle_excess':[str(sigma.a),str(sigma.b)],
            'currency_upper_bound':[str(budget.a),str(budget.b)]}


if __name__ == '__main__':
    out=[case(m,c,h) for m in (7,13,25)
         for c,h in ((F(1,2),None),(F(95,193),F(168,193)))]
    print(json.dumps({'classification':'exact finite crop checks',
          'scope':'explicit saturated lattice examples; no source optimality or packet',
          'cases':out},sort_keys=True))
