#!/usr/bin/env python3
"""Exact diameter geometry and a regression against pressure spreading.

Encode: actual rational unit-separated sources and all their diameters; weak
near-unit hull sides; ordered A/B boundary labels with internal rail occupancy;
a connected paired A staircase; positive normalized diameter weights; every
formal A and repeated B vector cut equation; transverse A rank; the full-span
negative-B classification and the pressure theorem (checked without radicals).
Omit: actual contact cuts/trains, vertex KKT, B derivative rank, positive contact
core, mixed stress/PSD, global optimality. The source has NO unit contacts.
Separately check the actual local grid contact/stress lemma. Its boundary loads
are prescribed, not claimed to be actual diameter loads or a global optimum.
All arithmetic is Fraction. General theorems have analytic proofs in the report.
"""

from fractions import Fraction as F
from itertools import combinations


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(t, a):
    return tuple(t * x for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def hull(points):
    ids = sorted(range(len(points)), key=lambda i: points[i])
    def half(seq):
        out = []
        for i in seq:
            while len(out) >= 2 and det(sub(points[out[-1]], points[out[-2]]),
                                        sub(points[i], points[out[-1]])) <= 0:
                out.pop()
            out.append(i)
        return out
    return half(ids)[:-1] + half(ids[::-1])[:-1]


def source(k):
    t = F(1, k)
    D = (1 + t*t)**2 / (4*t)
    d, q, a = 1-t*t, D-2*t, 2*t
    assert d*d + q*q == D*D and d < 1
    assert d*d + a*a == (1+t*t)**2 > 1
    o = (F(0), a/2)
    pts = [(-d/2, -q/2), (d/2, q/2),
           (-d/2, q/2+a), (d/2, -q/2+a),
           (-D/2, a/2), (D/2, a/2)]
    P = int(D // 1000)
    assert P >= 2
    r, m = P+2, 2*P+2
    A = [r-1, r, r-1, r, 0, m]
    B = [0, 1, 1, 0, 0, 1]
    arc = ['L', 'U', 'U', 'L', 'both', 'both']
    eta = 1/(100*D**4)
    weights = {(0, 2): eta, (4, 5): eta}
    fixed_B = (eta*D, eta*D)
    expected_diameters = set(weights) | {(0, 1), (2, 3)}
    # Points close to z/a leave room for the two asymmetric pivot bars.
    # t_circle near 1 => x nearly D/2, |y| small. Step 4/D gives >=1 spacing.
    for j in range(1, 2*P+1):
        tc = F(4, 5) + 4*j/D
        nx, ny = 2*tc/(1+tc*tc), (1-tc*tc)/(1+tc*tc)
        assert 0 < ny and nx > F(24, 25)
        x, y = D*nx/2, D*ny/2
        start = len(pts)
        pts += [add(o, (-x,-y)), add(o, (x,y)),
                add(o, (-x,y)), add(o, (x,-y))]
        if j <= P:
            # x increases with j: the more negative vertex has the smaller layer.
            lo, hi = P+1-j, r
        else:
            lo, hi = 0, r+j-P-1
        A += [lo, hi, lo, hi]
        B += [0, 1, 0 if lo == 0 else 1, 0]
        arc += ['L', 'U', 'U', 'L']
        for e in ((start, start+1), (start+2, start+3)):
            weights[e] = eta
            expected_diameters.add(e)
        fixed_B = add(fixed_B, scale(eta, (D*nx, D*ny)))
        if lo != 0:
            fixed_B = add(fixed_B, scale(eta, (-D*nx, D*ny)))
    # A tiny full-span paired packet connects the two halves of the A tree.
    c0, s0 = F(9999, 10001), F(200, 10001)
    start = len(pts)
    pts += [add(o, (-D*c0/2,-D*s0/2)), add(o, (D*c0/2,D*s0/2)),
            add(o, (-D*c0/2,D*s0/2)), add(o, (D*c0/2,-D*s0/2))]
    A += [0,m,0,m]; B += [0,1,0,1]; arc += ['L','U','U','L']
    for e in ((start,start+1),(start+2,start+3)):
        weights[e] = eta; expected_diameters.add(e)
    fixed_B = add(fixed_B, (2*eta*D*c0, F(0)))
    # Strong asymmetric bars use the SAME adjacent pivot gap as the weak bars.
    n1, n2 = (F(24,25), F(7,25)), (F(5,13), F(12,13))
    e1 = (len(pts), len(pts)+1)
    pts += [add(o, scale(-D/2,n1)), add(o, scale(D/2,n1))]
    A += [r-1,r]; B += [0,1]; arc += ['L','U']
    n2minus = (n2[0], -n2[1])
    e2 = (len(pts), len(pts)+1)
    pts += [add(o, scale(-D/2,n2minus)), add(o, scale(D/2,n2minus))]
    A += [r-1,r]; B += [1,0]; arc += ['U','L']
    expected_diameters |= {e1,e2}
    f1 = n2[1]/(n1[1]+n2[1]); f2 = 1-f1
    xp = f1*n1[0]-f2*n2[0]; yp = f1*n1[1]+f2*n2[1]
    rp = f1*n1[0]+f2*n2[0]
    c,s = F(8,17), F(15,17)
    fixed_mass = sum(weights.values())
    strong_mass = (c*q*(1-fixed_mass)+c*fixed_B[1]-s*fixed_B[0]) / (
        D*(s*xp-c*yp)+c*q)
    M = 1-fixed_mass-strong_mass
    assert M > F(2,5) and strong_mass > F(1,2)
    weights[(0,1)] = weights[(2,3)] = M/2
    weights[e1], weights[e2] = strong_mass*f1, strong_mass*f2
    assert sum(weights.values()) == 1 and all(w > 0 for w in weights.values())
    h = hull(pts)
    assert len(h) == len(pts) and len(pts)-1 < D
    hull_edges = {frozenset((h[i],h[(i+1)%len(h)])) for i in range(len(h))}
    assert frozenset((0,3)) in hull_edges and frozenset((1,2)) in hull_edges
    # Full exact geometry, including omitted-contact warning.
    actual_diameters = set()
    for i,j in combinations(range(len(pts)),2):
        z = dot(sub(pts[j],pts[i]),sub(pts[j],pts[i]))
        assert 1 < z <= D*D, (k,i,j,z)
        if z == D*D: actual_diameters.add((i,j))
    assert actual_diameters == expected_diameters
    for shore in ('L','U'):
        vertices = sorted((i for i in range(len(pts)) if arc[i] in (shore,'both')),
                          key=lambda i: pts[i][0])
        assert all(A[x] <= A[y] for x,y in zip(vertices,vertices[1:]))
        assert {A[i] for i in vertices} == set(range(m+1))
        assert all(B[i] == (0 if shore == 'L' else 1)
                   for i in vertices if 0 < A[i] < m)
    cuts = []
    gap_edges = set()
    orientations = {}
    for cut in range(1,m+1):
        force = (F(0),F(0))
        for (i,j),w in weights.items():
            if min(A[i],A[j]) < cut <= max(A[i],A[j]):
                vec = sub(pts[j],pts[i]) if A[i]<A[j] else sub(pts[i],pts[j])
                force = add(force,scale(w,vec))
        assert force[1] == 0 and force[0] > 0
        cuts.append(force[0])
    for (i,j),w in weights.items():
        vec = sub(pts[j],pts[i])
        if A[i] != A[j] and vec[1] != 0:
            e = tuple(sorted((A[i],A[j])))
            gap_edges.add(e)
            sign = 1 if (A[j]-A[i])*vec[1]>0 else -1
            orientations.setdefault(e,set()).add(sign)
        if B[i] != B[j]:
            vec_B = vec if B[i]<B[j] else scale(-1,vec)
            if vec_B[1] < 0:
                assert {A[i],A[j]} == {0,m}
    assert len(gap_edges) == m and all(sg == {-1,1} for sg in orientations.values())
    seen = {0}
    while True:
        new = seen | {b for a,b in gap_edges if a in seen} | {
            a for a,b in gap_edges if b in seen}
        if new == seen: break
        seen = new
    assert seen == set(range(m+1))  # graphic A rank exactly m
    FB = (F(0),F(0))
    for (i,j),w in weights.items():
        if B[i] != B[j]:
            vec = sub(pts[j],pts[i]) if B[i]<B[j] else sub(pts[i],pts[j])
            FB = add(FB,scale(w,vec))
    assert det((c,s),FB) == 0 and dot((c,s),FB)>0
    assert cuts[r-1] >= strong_mass*D*rp > D/3
    assert max(cuts[:r-1]+cuts[r:]) < 1/D**2
    L = F((m+1)**2,256)/(D+m+1)
    for i,j in actual_diameters:
        if {A[i],A[j]} == {0,m}: assert abs(pts[j][0]-pts[i][0]) > L
    # Pressure bound: avoid sqrt(Q^2), use the stronger Q>=D-2/D.
    N = weights[(0,2)]
    tan = s/c
    assert (D-2/D)*(M+N) <= (tan+D/L)*cuts[r-1]+F(3,2)*tan*N
    return len(pts),m,M,cuts[r-1]/D,max(cuts[:r-1]+cuts[r:]),len(actual_diameters)


def local_grid():
    u,v = (F(1),F(0)), (F(8,17),F(15,17))
    m,n = 7,5
    pts = {(i,j):add(scale(i,u),scale(j,v)) for i in range(m+1) for j in range(n+1)}
    contacts = {}
    for i in range(m):
        for j in range(n+1): contacts[((i,j),(i+1,j))] = F(j+1,3)
    for i in range(m+1):
        for j in range(n): contacts[((i,j),(i,j+1))] = F(i+2,5)
    for a,b in combinations(pts,2):
        z=dot(sub(pts[a],pts[b]),sub(pts[a],pts[b]))
        assert z>=1
        assert (z==1) == ((a,b) in contacts or (b,a) in contacts)
    for i in range(1,m):
        for j in range(1,n):
            p=(i,j); force=(F(0),F(0))
            for (a,b),w in contacts.items():
                if p==a: force=add(force,scale(w,sub(pts[b],pts[a])))
                elif p==b: force=add(force,scale(w,sub(pts[a],pts[b])))
            assert force==(0,0)
    G=sum(F(j+1,3) for j in range(1,n))
    assert all(sum(contacts[((i,j),(i+1,j))] for j in range(1,n))==G
               for i in range(m))
    return len(pts),len(contacts),G


def main():
    total=0
    for k in (12001,16001,20001):
        count,m,M,peak,other,dh=source(k)
        total+=count*(count-1)//2
        print(f'PASS k={k}: {count} actual hull points, {dh} actual diameters, '
              f'A rank {m}, weak mass>{float(M):.4f}, pivot pressure/D>{float(peak):.4f}; '
              'all other A pressures < D^-2')
    print(f'PASS: {total} rational pair checks; full-span negative-B classification; pressure inequality')
    count,contacts,G=local_grid()
    print(f'PASS local grid: {count} actual points, {contacts} actual contacts; common inner-row stress {G}')
    print('OMITTED: actual contact cuts/trains, source vertex KKT, B rank, global optimality')


if __name__=='__main__': main()
