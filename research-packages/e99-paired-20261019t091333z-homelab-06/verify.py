"""Exact finite control for the common homothetic-cell-crop identity.

This checks a rational fixture and a threshold-breaking control. It does not
prove the asymptotic cell, face-tail, coherent-grain, or pseudogrid theorems.
"""
from fractions import Fraction as F
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(u, v):
    return (u[0] + v[0], u[1] + v[1])


def sub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def scale(s, u):
    return (s * u[0], s * u[1])


def norm2(u):
    return u[0] * u[0] + u[1] * u[1]


def inside_square(u):
    return abs(u[0]) <= 1 and abs(u[1]) <= 1


def common_crop_fixture():
    D = F(3)
    rho = F(1, 2)
    r0 = F(1, 10)
    delta = rho * r0 / 2
    inner = r0 * D / 2
    outer = r0 * D
    o = (F(0), F(0))
    a0 = (F(1), F(0))
    a = (F(1) - delta * D, F(0))
    require(norm2(sub(a, a0)) == (delta * D) ** 2,
            "positive fixture must attain the allowed attachment separation")
    require(outer <= 1 and 8 < D * D,
            "the rational square must contain the outer disk and have diameter below D")

    directions = [
        (F(1), F(0)), (F(-1), F(0)), (F(0), F(1)), (F(0), F(-1)),
        (F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5)),
        (F(4, 5), F(-3, 5)), (F(-4, 5), F(-3, 5)),
    ]
    checked = 0
    for u in directions:
        require(norm2(u) == 1, "fixture direction must be an exact unit vector")
        x = add(o, scale(inner, u))
        x_a = add(x, scale((1 - rho) / rho, sub(a0, a)))
        require(norm2(sub(x_a, o)) <= outer * outer,
                "translated point must stay in the larger disk")
        require(inside_square(x_a) and inside_square(a) and inside_square(a0),
                "translated point and attachments must lie in the rational convex cell")

        common_point = add(scale(1 - rho, a0), scale(rho, x))
        attachment_crop_point = add(scale(1 - rho, a), scale(rho, x_a))
        require(common_point == attachment_crop_point,
                "homothety identity failed: Q_* must be in every Q_a")
        require(inside_square(common_point), "common-crop point must stay in the cell")
        require(norm2(sub(common_point, a)) <= (rho * D) ** 2,
                "attachment crop must lie in the rho D ball")
        checked += 1

    # Failure control: if the arc separation exceeds rho*r0/2, aligned vectors
    # can push x_a outside B(o,r0 D), so the threshold is load-bearing.
    delta_bad = F(1, 16)
    a_bad = (F(1) - delta_bad * D, F(0))
    x_bad = (inner, F(0))
    x_a_bad = add(x_bad, scale((1 - rho) / rho, sub(a0, a_bad)))
    require(inside_square(a_bad), "negative-control attachment must remain in the cell")
    require(delta_bad > delta, "negative control must violate the arc-separation bound")
    require(norm2(sub(x_a_bad, o)) > outer * outer,
            "violating the delta bound should break the common-disk containment")
    return {"positive_exact_points_checked": checked,
            "negative_control": "separation above rho*r0/2 exits the larger disk",
            "fixture_cell": "[-1,1]^2; diameter^2=8 < D^2=9"}


print(json.dumps({"status": "PASS",
                  "scope": "exact rational crop identity fixture only; not an asymptotic proof",
                  "result": common_crop_fixture()}, sort_keys=True))
