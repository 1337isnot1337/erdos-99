#!/usr/bin/env python3
"""Finite exact packets for independent uneven convex side profiles.

Certifies Green identities, rational geometry and all finite pair tests.
Universal shields, Oler and arbitrary-source extraction remain analytic
or unproved as explicitly stated in the companion report.
"""
from fractions import Fraction as F
from itertools import combinations
import json

import verify_target_c_curved_wall_audit_2026_10_06 as g
from verify_target_c_near_triangular_curved_wall_capacity_audit_2026_10_06 import near_triangular_basis


def profile(m, concentration=0):
    result = []
    for j in range(m):
        side = (2*j > m-1)-(2*j < m-1)
        result.append(2*j-m+1+2*concentration*side)
    return result


def profile_data(a):
    m = len(a)
    assert all(a[j] < a[j+1] for j in range(m-1))
    assert all(a[j] == -a[m-1-j] for j in range(m))
    assert sum(a) == 0
    assert all((a[j]+a[j-1]) % 2 == 0 for j in range(1,m))
    bow = [F(0)]+[-sum(a[:i]) for i in range(1,m)]+[F(0)]
    gap = [0]+[a[i]-a[i-1] for i in range(1,m)]
    for i in range(1,m):
        assert bow[i] > 0
        assert 2*bow[i]-bow[i-1]-bow[i+1] == gap[i]
        green = sum(F(min(i,j)*(m-max(i,j)),m)*gap[j]
                    for j in range(1,m))
        assert green == bow[i]
        assert bow[i] >= F(i*(m-i),m)*gap[i]
    return bow, gap


def geometry(m, first, second):
    assert m >= 8 and len(first) == len(second) == m
    data = [profile_data(first), profile_data(second)]
    tangent, c, s = near_triangular_basis(m)
    max_rate = max(abs(a) for a in first+second)
    t = (1-2*c)/(10**6*m**4*(max_rate+1)**2)
    rotation = ((1-t*t)/(1+t*t),2*t/(1+t*t))
    u, v = (F(1),F(0)), (c,s)
    bases = [u,v,g.scale(u,-1),g.scale(v,-1)]
    profiles = [first,second,first,second]
    edge_families = [[g.mul(g.power(rotation,a),w) for a in rates]
                     for rates,w in zip(profiles,bases)]
    edges = sum(edge_families,[])
    wall = [(F(0),F(0))]
    for e in edges[:-1]:
        wall.append(g.add(wall[-1],e))
    assert g.add(wall[-1],edges[-1]) == (F(0),F(0))
    chord_u = sum(g.power(rotation,a)[0] for a in first)
    chord_v = sum(g.power(rotation,a)[0] for a in second)
    center = g.scale(g.add(g.scale(u,chord_u),g.scale(v,chord_v)),F(1,2))
    indices = list(range(3,m-2,3))
    mu = min([F(1)]+[F(bow[i]) for bow,gap in data for i in range(1,m)]+
             [bow[i]-F(3,2)*gap[i] for bow,gap in data for i in indices])
    assert mu > 0
    lam = mu/(100*m)
    spacing = 1+2*lam*t
    cloud = [g.add(center,g.scale(g.add(g.scale(u,F(i)-F(m,2)),
                                       g.scale(v,F(j)-F(m,2))),spacing))
             for i in range(1,m) for j in range(1,m)]
    bank = [side*m+i for side in range(4) for i in indices]
    assert len(bank) == 4*((m-3)//3)

    def root(index):
        side,i = divmod(index,m)
        rates = profiles[side]
        gap = rates[i]-rates[i-1]
        assert gap > 0 and gap % 2 == 0
        half_turn = g.power(rotation,gap//2)
        average = (rates[i]+rates[i-1])//2
        normal = g.turn(g.mul(g.power(rotation,average),bases[side]))
        return g.add(wall[index],g.scale(normal,3*half_turn[1])), half_turn[1]

    moved = list(wall)
    releases = {}
    for index in bank:
        moved[index],sine = root(index)
        releases[index] = 3*sine*sine
    return wall,edges,cloud,moved,bank,releases,data,root


def case(m,first,second,label):
    wall,edges,cloud,moved,bank,releases,data,root = geometry(m,first,second)
    source,target = wall+cloud,moved+cloud
    convex_checks,interior_checks = 0,0
    for i,e in enumerate(edges):
        assert g.dot(e,e) == 1
        for j,p in enumerate(wall):
            if j not in (i,(i+1)%(4*m)):
                assert g.cross(e,g.sub(p,wall[i])) > 0
                convex_checks += 1
        for p in cloud+[moved[j] for j in bank]:
            assert g.cross(e,g.sub(p,wall[i])) > 0
            interior_checks += 1
    area = sum(g.cross(wall[i],wall[(i+1)%(4*m)]) for i in range(4*m))/2
    assert area > 0 and 4*area*area < 3*(m*m+1)**2
    for i,j in combinations(bank,2):
        assert g.squared(wall[i],wall[j]) > 4
        assert g.squared(moved[i],moved[j]) > 4
    old_contacts = {tuple(sorted((i,(i+1)%(4*m)))) for i in range(4*m)}
    new_contacts = {p for p in old_contacts if not (set(p)&set(bank))}
    assert len(new_contacts) == 4*m-2*len(bank)
    pairs = []
    diameter = F(0)
    for i,j in combinations(range(len(source)),2):
        d = g.squared(source[i],source[j])
        assert d == 1 if (i,j) in old_contacts else d > 1
        diameter = max(diameter,d)
        pairs.append((i,j))
    upper_checks = 0
    for i,j in pairs:
        d = g.squared(target[i],target[j])
        assert d == 1 if (i,j) in new_contacts else d > 1
        assert d <= diameter
        if i in bank or j in bank:
            assert d < diameter
            upper_checks += 1
    for index in bank:
        for neighbor in ((index-1)%(4*m),(index+1)%(4*m)):
            assert g.squared(moved[index],wall[neighbor])-1 == releases[index]
    count_checks = 0
    for z in range((m-1)**2+1):
        required_packet = z+len(bank)
        available_packet = len(cloud)+len(bank)
        assert required_packet <= available_packet
        assert 4*m+z == 4*m-len(bank)+(z+len(bank))
        assert 4*m+z < (m+1)**2+1
        count_checks += 1
    result = {'M':m,'profile_label':label,'first_profile':first,'second_profile':second,
              'source_points':len(source),'interior_capacity':len(cloud),
              'moved_wall_vertices':len(bank),'old_contacts':len(old_contacts),
              'new_contacts':len(new_contacts),'old_pair_checks':len(pairs),
              'new_pair_checks':len(pairs),'strict_upper_checks':upper_checks,
              'convexity_checks':convex_checks,'interior_checks':interior_checks,
              'green_identity_checks':2*(m-1),'integer_population_checks':count_checks,
              'exact_area_threshold':True}
    if label == 'corner_concentration':
        b = 1
        bow,gap = data[0]
        assert bow[b]-F(3,2)*gap[b] < 0
        failed,sine = root(b)
        z = cloud[0]  # labelled (1,1)
        assert g.squared(wall[b],z) > 1
        assert g.squared(failed,z) < 1
        result['corner_root_lower_failure'] = True
        result['corner_first_order_margin'] = str(bow[b]-F(3,2)*gap[b])
    return result


def main():
    cases = [case(8,profile(8),profile(8,3),'two_independent_profiles'),
             case(10,profile(10,12),profile(10,1),'middle_concentration'),
             case(9,profile(9,4),profile(9,2),'odd_M_uneven_profiles'),
             case(12,profile(12,4),profile(12,7),'unequal_middle_profiles'),
             case(8,[-101,-5,-3,-1,1,3,5,101],profile(8),'corner_concentration')]
    print(json.dumps({'classification':'finite exact uneven-wall packet certificates',
                      'cases':cases,
                      'old_pair_checks':sum(c['old_pair_checks'] for c in cases),
                      'new_pair_checks':sum(c['new_pair_checks'] for c in cases),
                      'green_identity_checks':sum(c['green_identity_checks'] for c in cases),
                      'integer_population_checks':sum(c['integer_population_checks'] for c in cases),
                      'not_proved':['universal chamber extraction','global optimality',
                                    'full-core or container closure','Level I']},sort_keys=True))


if __name__ == '__main__':
    main()
