"""Exact audit WITHDRAWING the former C53 pentagon regression.

Run: python3 research/thrackle_interval_regression.py
Regular-pentagon chord directions are exact integer degrees here, from
arg(p_j-p_i)=90+36(i+j) for 0<=i<j<=4. One cut controls BOTH order and
orientation. Tests all circular vertex intervals and all projective cut types.
No floating point, network realization, or global packing certificate is used.
General chord-type reduction and C-I proof are in the 2026-09-09 restoration report.
"""


def signs(edges, interval):
    return tuple(int(j in interval)-int(i in interval) for i, j in edges)


def valid(z):
    x, y, w = z
    return w*(x-y) <= 0 and x*(w-y) <= 0


def main():
    base = [(0, 3), (1, 3), (0, 2)]
    checks = 0
    for lower in (0, 36, 108, -90, 180, 216, 288, 90):
        lifted = []
        for i, j in base:
            angle = 90+36*(i+j)
            edge = (i, j)
            while angle < lower:
                angle += 180
                edge = edge[::-1]
            while angle >= lower+180:
                angle -= 180
                edge = edge[::-1]
            lifted.append((angle, edge))
        lifted.sort()
        edges = [e for angle, e in lifted]
        for start in range(5):
            for length in range(6):
                interval = {(start+j) % 5 for j in range(length)}
                assert valid(signs(edges, interval)), (lower, edges, interval)
                checks += 1
        if lower in (0, -90):
            print('half-plane', (lower, lower+180), 'ordered/oriented', edges,
                  'signs at {0}', signs(edges, {0}))
    mixed_edges = [(3, 0), (3, 1), (2, 0)]
    mixed_angles = [18, 54, -18]
    assert not valid(signs(mixed_edges, {0}))
    assert mixed_angles != sorted(mixed_angles)
    print(f'PASS: {checks} exact consistently normalized pentagon/interval checks')
    print('WITHDRAWN: the old violating tuple uses incompatible order and orientation.')


if __name__ == '__main__':
    main()
