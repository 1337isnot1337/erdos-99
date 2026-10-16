#!/usr/bin/env python3
"""Exact finite boundary-packet checks for the global linear-reserve candidate.

No floats, numerical optimization, or global-minimizer input is used. Unchanged
lattice pairs, far retained labels and cross-packet pairs are covered by explicit
geometric bounds; all retained labels potentially within unit distance are
enumerated. The universal theorem is analytic, not an inference from these cases.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from fractions import Fraction as F
from math import isqrt


SCALE = 10**50
SQRT3_LO = F(isqrt(3*SCALE*SCALE), SCALE)
SQRT3_HI = SQRT3_LO + F(1, SCALE)


def sign_quadratic(a, b):
    """Exact sign of rational a+b*sqrt(3)."""
    a, b = F(a), F(b)
    if not b:
        return (a > 0)-(a < 0)
    if not a:
        return (b > 0)-(b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    comparison = a*a - 3*b*b
    assert comparison != 0  # sqrt(3) is irrational and a,b are nonzero rationals.
    return ((comparison > 0)-(comparison < 0)) * ((a > 0)-(a < 0))


def interval_quadratic(a, b):
    vals = (F(a)+F(b)*SQRT3_LO, F(a)+F(b)*SQRT3_HI)
    return min(vals), max(vals)


def sqrt_interval(lo, hi=None):
    hi = lo if hi is None else hi
    assert 0 <= lo <= hi
    lower = isqrt((lo*SCALE*SCALE).__floor__())
    upper = isqrt((hi*SCALE*SCALE).__floor__()) + 1
    return F(lower, SCALE), F(upper, SCALE)


def floor(x):
    return x.numerator // x.denominator


def ceil(x):
    return -floor(-x)


def arithmetic_controls():
    """Independent interval oracle for the quadratic-field sign routine."""
    assert SQRT3_LO**2 < 3 < SQRT3_HI**2
    checked = 0
    for a in range(-8, 9):
        for b in range(-8, 9):
            lo, hi = interval_quadratic(a, b)
            expected = 0 if a == b == 0 else 1 if lo > 0 else -1
            assert a == b == 0 or lo > 0 or hi < 0
            assert sign_quadratic(a, b) == expected
            checked += 1
    for value in (F(0), F(1), F(2), F(3), F(9, 4)):
        lo, hi = sqrt_interval(value)
        assert 0 <= lo <= hi and lo**2 <= value <= hi**2
    print(f"PASS: {checked} sign controls and five outward square-root bounds")


def check_case(radius, tx, ty):
    radius, tx, ty = F(radius), F(tx), F(ty)
    assert radius >= 640000
    lower_top = sqrt_interval(radius*radius*(1-F(1, 200**2)))
    upper_top = sqrt_interval(radius*radius*(1-F(1, 400**2)))
    kmin = floor((lower_top[0]-ty)/(SQRT3_HI/2))-3
    kmax = ceil((upper_top[1]-ty)/(SQRT3_LO/2))+3
    rows = {}
    for k in range(kmin, kmax+1):
        ylo, yhi = interval_quadratic(ty, F(k, 2))
        nextlo, nexthi = interval_quadratic(ty, F(k+1, 2))
        if ylo < lower_top[1] or nexthi > upper_top[0]:
            continue
        ulo, uhi = sqrt_interval(radius*radius-nexthi*nexthi,
                                 radius*radius-nextlo*nextlo)
        vlo, vhi = sqrt_interval(radius*radius-(yhi+F(1, 2))**2,
                                 radius*radius-(ylo+F(1, 2))**2)
        left, right = ceil(uhi), floor(vlo)
        length = right-left
        assert length > 64
        offset = tx+F(k, 2)
        first_deleted = ceil(left-offset)
        last_deleted = floor(right-offset)
        deleted = last_deleted-first_deleted+1
        count = floor(F(length-2, 1)/F(19, 20))+1
        assert count-deleted >= 1
        assert deleted <= length+1
        rows[k] = (left, right, count, deleted)

    # No averaging is used in the finite examples: test actual translates.
    assert len(rows) >= radius/160000
    horizontal_intervals = sorted((v[0], v[1]) for v in rows.values())
    for (_, right), (left, _) in zip(horizontal_intervals, horizontal_intervals[1:]):
        assert right <= left
        assert (left+1)-(right-1) >= 2

    total_inserted = total_deleted = checked_neighbors = 0
    minimum_gain = min(count-deleted for _, _, count, deleted in rows.values())
    for k, (left, right, count, deleted) in rows.items():
        total_inserted += count
        total_deleted += deleted
        for i in range(count):
            px = F(left+1)+i*F(19, 20)
            height = F(1, 6) if i % 2 == 0 else F(1, 2)
            assert left+1 <= px <= right-1
            # Independent finite-union regression: every packet point lies in
            # one of 38 translates of Gamma=< (19/10,0), (1,sqrt(3)/2) >.
            sigma = i % 2
            residue = (left+1-k) % 19
            gamma_horizontal = (px-residue-sigma*F(19, 20)-k)/F(19, 10)
            assert gamma_horizontal.denominator == 1
            assert F(9, 10)**2+F(3, 4) == F(39, 25) > 1
            # px^2+(ty+k*sqrt(3)/2+height)^2 < radius^2.
            a = px*px+(ty+height)**2+F(3*k*k, 4)-radius*radius
            b = k*(ty+height)
            assert sign_quadratic(a, b) < 0

            # If a retained lattice label could have distance <=1, its row
            # differs by at most two, and its horizontal integer index lies
            # among the five values enumerated here. More distant rows have
            # vertical separation >=3*a0-1/2>1; more distant columns have
            # horizontal separation >1.
            for ell in range(k-2, k+3):
                center = floor(px-tx-F(ell, 2))
                for j in range(center-2, center+3):
                    qx = tx+j+F(ell, 2)
                    # Determine whether this original lattice label is in the disk.
                    qa = qx*qx+ty*ty+F(3*ell*ell, 4)-radius*radius
                    qb = ell*ty
                    if sign_quadratic(qa, qb) > 0:
                        continue
                    if ell in rows and rows[ell][0] <= qx <= rows[ell][1]:
                        continue
                    diff = k-ell
                    da = (px-qx)**2+F(3*diff*diff, 4)+height*height-1
                    db = diff*height
                    assert sign_quadratic(da, db) > 0, (radius, tx, ty, k, i, ell, j)
                    checked_neighbors += 1

        # Exact within-packet checks cover adjacent and all nonadjacent pairs.
        assert F(19, 20)**2+F(1, 3)**2 == F(3649, 3600) > 1
        assert F(19, 10) > 1
        # Exact lower-row clearance and the row-count/width constants.
        assert sign_quadratic(F(-5, 6), F(1, 2)) > 0
        assert 200**2-1 > 199**2

    gain = total_inserted-total_deleted
    assert gain >= len(rows) >= radius/160000
    return len(rows), total_deleted, total_inserted, gain, checked_neighbors, minimum_gain


def main():
    arithmetic_controls()
    cases = (
        (640000, F(0), F(0)),
        (1000000, F(0), F(0)),
        (1000000, F(1, 7), F(2, 9)),
        (2000000, F(3, 11), F(5, 13)),
        (10000000, F(2, 17), F(1, 19)),
    )
    neighbor_total = packet_total = insertion_total = gain_total = 0
    for radius, tx, ty in cases:
        packets, deleted, inserted, gain, checks, min_gain = check_case(radius, tx, ty)
        packet_total += packets
        neighbor_total += checks
        insertion_total += inserted
        gain_total += gain
        print(f"R={radius}, t=({tx},{ty}): packets={packets}, deleted={deleted}, "
              f"inserted={inserted}, gain={gain}, minimum packet gain={min_gain}, "
              f"retained-neighbor checks={checks}")
    print(f"PASS: {packet_total} simultaneous packets across {len(cases)} examples; "
          f"{insertion_total} contained inserted labels; {neighbor_total} exact "
          f"retained-lattice neighbor checks; total net gain={gain_total}.")
    print(f"PASS: exact 38-class packet-lattice membership for all {insertion_total} "
          "inserted labels; the unchanged triangular lattice is class 39.")
    print("All arithmetic is rational or exact Q(sqrt(3)). Scope: finite packet "
          "certificates; the all-radius linear reserve is an analytic candidate, "
          "not an audited Level I proof.")


if __name__ == "__main__":
    main()
