#!/usr/bin/env python3
"""Certified finite decorated-grid regression, with rational interval arithmetic.

Contacts equal one by the analytic unit-vector/radical identities in the
report. Intervals certify every other source pair strictly above one.
The Oler capacity bound is checked exactly with rational sqrt(3) bounds.
No diameter loading, global optimality or uniqueness window is certified.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt

Q = 10**24


def rat(x):
    x = F(x)
    a = x.numerator*Q
    return a//x.denominator, -((-a)//x.denominator)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    products = [x*y for x in a for y in b]
    lo, hi = min(products), max(products)
    return lo//Q, -((-hi)//Q)


def inv(a):
    assert a[0] > 0
    return Q*Q//a[1], -((-Q*Q)//a[0])


def scale(a, r):
    return mul(a, rat(r))


def root(a):
    assert a[0] >= 0
    lo, hi = isqrt(a[0]*Q), isqrt(a[1]*Q)
    if hi*hi < a[1]*Q:
        hi += 1
    return lo, hi


def p_add(a, b):
    return add(a[0], b[0]), add(a[1], b[1])


def p_scale(p, r):
    return scale(p[0], r), scale(p[1], r)


def p_mul(p, a):
    return mul(p[0], a), mul(p[1], a)


def p_neg(p):
    return neg(p[0]), neg(p[1])


def rotation(p):
    return neg(p[1]), p[0]


def square_bounds(a):
    lo = 0 if a[0] <= 0 <= a[1] else min(a[0]*a[0], a[1]*a[1])
    return lo, max(a[0]*a[0], a[1]*a[1])


def distance_bounds(p, q):
    x = square_bounds(sub(p[0], q[0]))
    y = square_bounds(sub(p[1], q[1]))
    return x[0]+y[0], x[1]+y[1]


def main():
    cases = ((24, False), (30, False), (36, False), (32, True), (40, True))
    totals = dict(points=0, pairs=0, contacts=0, caps=0, crossings=0)
    sqrt3, sqrt5 = root(rat(3)), root(rat(5))
    c72 = scale(sub(sqrt5, rat(1)), F(1, 4))
    s72 = scale(root(add(rat(10), scale(sqrt5, 2))), F(1, 4))
    s36 = scale(root(sub(rat(10), scale(sqrt5, 2))), F(1, 4))
    cap_height = add(s72, s36)
    assert cap_height[1] < 2*Q
    assert s72[0] > rat(F(9, 10))[1]
    for M, augmented in cases:
        t = F(1, 200*M**3)  # the explicit capacity-optimal family, not L.2's unknown window
        cd, sd = (1-t*t)/(1+t*t), 2*t/(1+t*t)
        assert cd*cd+sd*sd == 1
        u = rat(1), rat(0)
        v = (sub(rat(cd/2), scale(sqrt3, sd/2)),
             add(rat(sd/2), scale(sqrt3, cd/2)))
        assert 0 < v[0][0] < v[0][1] < Q//2
        assert v[1][0] > Q*866//1000
        # r=M^2(sin(phi)/a0-1)=M^2(cd-1+sd/sqrt(3)); exact directed bounds.
        residual_lo = M*M*(cd-1+sd/F(sqrt3[1], Q))
        residual_hi = M*M*(cd-1+sd/F(sqrt3[0], Q))
        assert 0 < residual_lo < residual_hi < 1
        assert residual_hi < F(1, 100*M)
        points, labels, contacts = [], {}, set()
        def insert(label, p):
            labels[label] = len(points)
            points.append(p)
            return labels[label]
        def edge(a, b):
            contacts.add(tuple(sorted((a, b))))
        for i in range(M+1):
            for j in range(M+1):
                insert(('g', i, j), p_add(p_scale(u, i), p_scale(v, j)))
        for i in range(M+1):
            for j in range(M+1):
                a = labels[('g', i, j)]
                if i < M:
                    edge(a, labels[('g', i+1, j)])
                if j < M:
                    edge(a, labels[('g', i, j+1)])
        selection = list(range(8, M-8, 8 if augmented else 6))
        leaf_ids, cap_equilibria, anchor_equilibria = set(), [], []
        c36 = scale(add(sqrt5,rat(1)),F(1,4))
        gamma = rat(F(1,100))
        L1 = rat(1)
        L2 = add(L1,mul(scale(gamma,F(15,17)),inv(c36)))
        supports, midpoints = [], []
        for side in range(4):
            for k in selection:
                if side == 0:
                    a, b, w, normal = ('g', k, 0), ('g', k+1, 0), u, p_neg(rotation(u))
                elif side == 1:
                    a, b, w, normal = ('g', k, M), ('g', k+1, M), u, rotation(u)
                elif side == 2:
                    a, b, w, normal = ('g', 0, k), ('g', 0, k+1), v, rotation(v)
                else:
                    a, b, w, normal = ('g', M, k), ('g', M, k+1), v, p_neg(rotation(v))
                pa, pb = points[labels[a]], points[labels[b]]
                pc = p_add(pb, p_add(p_mul(w, c72), p_mul(normal, s72)))
                pd = p_add(pa, p_add(p_scale(w, F(1, 2)), p_mul(normal, cap_height)))
                pe = p_add(pa, p_add(p_mul(w, neg(c72)), p_mul(normal, s72)))
                cap = [labels[a], labels[b], insert(('c',side,k),pc),
                       insert(('d',side,k),pd), insert(('e',side,k),pe)]
                for idx in range(5):
                    edge(cap[idx], cap[(idx+1)%5])
                support = set(cap)
                assert all(not (support & other) for other in supports)
                supports.append(support)
                if augmented:
                    px_leaf = p_add(pd,p_add(p_scale(w,F(15,17)),p_scale(normal,F(8,17))))
                    pc_leaf = p_add(pc, p_add(p_mul(w, s72), p_mul(normal, c72)))
                    pd_leaf = p_add(pd, normal)
                    pe_leaf = p_add(pe, p_add(p_mul(w, neg(s72)), p_mul(normal, c72)))
                    leaves = [insert(('nc',side,k),pc_leaf), insert(('nd',side,k),pd_leaf),
                              insert(('ne',side,k),pe_leaf),insert(('nx',side,k),px_leaf)]
                    leaf_ids.update(leaves)
                    for old_idx, leaf_idx in zip(cap[2:], leaves[:3]):
                        edge(old_idx, leaf_idx)
                        cap_equilibria.append((old_idx, leaf_idx, cap, leaves[3]))
                    edge(cap[3],leaves[3])
                    # Four positive contact forces at each shared grid anchor.
                    din = v if side==0 else p_neg(v) if side==1 else u if side==2 else p_neg(u)
                    dw = v[0] if side in (0,2) else neg(v[0])
                    beta_a = mul(mul(s72,L2),inv(v[1]))
                    beta_b = mul(mul(s72,L1),inv(v[1]))
                    Na = sub(mul(beta_a,dw),mul(L2,c72))
                    Nb = add(mul(beta_b,dw),mul(L1,c72))
                    before, after = add(rat(2),Na),sub(rat(2),Nb)
                    assert before[0]>0 and after[0]>0
                    ea = p_add(p_add(p_mul(w,sub(rat(2),before)),p_mul(din,beta_a)),
                               p_mul(p_add(p_mul(w,neg(c72)),p_mul(normal,s72)),L2))
                    eb = p_add(p_add(p_mul(w,sub(after,rat(2))),p_mul(din,beta_b)),
                               p_mul(p_add(p_mul(w,c72),p_mul(normal,s72)),L1))
                    assert all(a<=0<=b for a,b in ea+eb)
                    anchor_equilibria.extend((cap[0],cap[1]))
                midpoints.append(p_add(pa, p_scale(w, F(1, 2))))
                for idx in cap:
                    assert distance_bounds(points[idx], midpoints[-1])[1] < 4*Q*Q
                if augmented:
                    for idx in leaves:
                        assert distance_bounds(points[idx], midpoints[-1])[1] < 9*Q*Q
        assert all(distance_bounds(a,b)[0] > (49 if augmented else 25)*Q*Q for a,b in combinations(midpoints,2))
        minimum_gap = None
        for i, j in combinations(range(len(points)), 2):
            lo, hi = distance_bounds(points[i], points[j])
            if (i,j) in contacts:
                assert lo <= Q*Q <= hi, (M,i,j,lo,hi)
            else:
                assert lo > Q*Q, (M,i,j,lo,hi)
                gap = lo-Q*Q
                minimum_gap = gap if minimum_gap is None else min(minimum_gap,gap)
        adjacency = [set() for _ in points]
        for a,b in contacts:
            adjacency[a].add(b)
            adjacency[b].add(a)
        assert all(not(adjacency[a] & adjacency[b]) for a,b in contacts)
        wall = {labels[('g',i,j)] for i in range(M+1) for j in range(M+1)
                if i in (0,M) or j in (0,M)}
        wall.update(idx for support in supports for idx in support)
        assert len(points)-len(wall)-len(leaf_ids) == (M-1)**2
        assert len(contacts) == 2*M*(M+1)+(8 if augmented else 4)*len(supports)
        # All nonboundary grid vertices retain opposite unit neighbors, giving
        # the analytic positive pinned equilibrium. Caps add no interior label.
        for i in range(1,M):
            for j in range(1,M):
                a = labels[('g',i,j)]
                expected = {labels[('g',i-1,j)], labels[('g',i+1,j)],
                            labels[('g',i,j-1)], labels[('g',i,j+1)]}
                assert adjacency[a] == expected
        if augmented:
            for old_idx, leaf_idx, cap, extra_leaf in cap_equilibria:
                assert adjacency[leaf_idx] == {old_idx}
                previous = cap[(cap.index(old_idx)-1) % 5]
                following = cap[(cap.index(old_idx)+1) % 5]
                expected = {previous,following,leaf_idx}
                if old_idx==cap[3]: expected.add(extra_leaf)
                assert adjacency[old_idx]==expected
                def difference(a, b):
                    return sub(a[0],b[0]), sub(a[1],b[1])
                if old_idx==cap[2]:
                    wp,wf=L1,L1
                    leaf_weight=mul(scale(s36,2),L1)
                elif old_idx==cap[4]:
                    wp,wf=L2,L2
                    leaf_weight=mul(scale(s36,2),L2)
                else:
                    wp,wf=L1,L2
                    leaf_weight=sub(mul(s36,add(L1,L2)),scale(gamma,F(8,17)))
                assert leaf_weight[0]>0
                equilibrium = p_add(p_add(p_mul(difference(points[previous],points[old_idx]),wp),
                                            p_mul(difference(points[following],points[old_idx]),wf)),
                                    p_mul(difference(points[leaf_idx],points[old_idx]),leaf_weight))
                if old_idx==cap[3]:
                    equilibrium=p_add(equilibrium,p_mul(difference(points[extra_leaf],points[old_idx]),gamma))
                assert all(a <= 0 <= b for a,b in equilibrium)
        crossings = {(i,j) for i in selection for j in selection}
        assert len(crossings) == len(selection)**2
        for i,j in crossings:
            cell = [labels[('g',i,j)],labels[('g',i+1,j)],
                    labels[('g',i+1,j+1)],labels[('g',i,j+1)]]
            assert all(tuple(sorted((cell[k],cell[(k+1)%4]))) in contacts for k in range(4))
        totals['points'] += len(points)
        totals['pairs'] += len(points)*(len(points)-1)//2
        totals['contacts'] += len(contacts)
        totals['caps'] += len(supports)
        totals['crossings'] += len(crossings)
        print(f'M={M}, radial pins={augmented}: {len(points)} source points, {len(supports)} disjoint pentagons, '
              f'{len(crossings)} selected rhombi; all noncontacts have positive certified gap')
    print('PASS:', totals)
    print('No actual diameter loads, canonical full-core sequence, global optimum, or numerical uniqueness window is asserted.')


if __name__ == '__main__':
    main()
