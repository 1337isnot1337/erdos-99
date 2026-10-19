"""Exact checker for the finite two-shore cut-stress model in README.md."""

from fractions import Fraction as F

Vec = tuple[F, F]
Interval = tuple[int, int] | None


def vec(x: int | F, y: int | F) -> Vec:
    return (F(x), F(y))


def add(a: Vec, b: Vec) -> Vec:
    return (a[0] + b[0], a[1] + b[1])


def scale(k: F, a: Vec) -> Vec:
    return (k * a[0], k * a[1])


def dot(a: Vec, b: Vec) -> F:
    return a[0] * b[0] + a[1] * b[1]


def det(a: Vec, b: Vec) -> F:
    return a[0] * b[1] - a[1] * b[0]


def quarter_turn(a: Vec) -> Vec:
    return (-a[1], a[0])


def crosses(interval: Interval, cut: int) -> bool:
    return interval is not None and interval[0] < cut <= interval[1]


class Row:
    def __init__(self, name, edge, beta, a_vec, a_support, b_support, b_sign):
        self.name = name
        self.edge = edge
        self.beta = beta
        self.a_vec = a_vec
        self.a_support = a_support
        self.b_support = b_support
        self.b_sign = b_sign

    @property
    def c(self) -> F:
        return self.a_vec[1]

    @property
    def b_vec(self) -> Vec:
        assert self.b_sign in (-1, 1)
        return scale(F(self.b_sign), self.a_vec)


def rows_for_model() -> list[Row]:
    return [
        Row("h0", None, F(1), vec(1, 0), (0, 3), (0, 2), 1),
        Row("e02+", (0, 2), F(3), vec(F(3, 5), F(4, 5)), (0, 2), (1, 2), 1),
        Row("e02-", (0, 2), F(4), vec(F(4, 5), F(-3, 5)), (0, 2), (0, 1), -1),
        Row("e03+", (0, 3), F(8), vec(F(8, 17), F(15, 17)), (0, 3), None, None),
        Row("e03-", (0, 3), F(15), vec(F(15, 17), F(-8, 17)), (0, 3), None, None),
        Row("e12+", (1, 2), F(1), vec(F(5, 13), F(12, 13)), (1, 2), (0, 2), 1),
        Row("e12-", (1, 2), F(1), vec(F(5, 13), F(-12, 13)), (1, 2), (0, 2), -1),
    ]


def grouped(rows: list[Row], edge: tuple[int, int]) -> list[Row]:
    return [row for row in rows if row.edge == edge]


def packet_balances(rows: list[Row]) -> bool:
    for edge in ((0, 2), (0, 3), (1, 2)):
        packet = grouped(rows, edge)
        if not packet or sum((r.beta * r.c for r in packet), F(0)) != 0:
            return False
        resultant = (F(0), F(0))
        for row in packet:
            resultant = add(resultant, scale(row.beta, row.a_vec))
        if resultant[1] != 0 or resultant[0] <= 0:
            return False
    return True


def valid_model(rows: list[Row]) -> tuple[bool, str]:
    if {r.name for r in rows} != {
        "h0", "e02+", "e02-", "e03+", "e03-", "e12+", "e12-"
    }:
        return False, "row inventory"
    if any(r.beta <= 0 for r in rows):
        return False, "positive stress"
    if any(dot(r.a_vec, r.a_vec) != 1 for r in rows):
        return False, "unit row length"
    for i, row in enumerate(rows):
        for other in rows[i + 1 :]:
            if det(row.a_vec, other.a_vec) == 0:
                return False, "parallel diameter directions"
    if not packet_balances(rows):
        return False, "edgewise packet balance/resultant"

    tree = {(0, 2), (0, 3), (1, 2)}
    if {r.edge for r in rows if r.edge is not None} - tree:
        return False, "unexpected support type"
    reached = {0}
    while True:
        old = set(reached)
        for a, b in tree:
            if a in reached or b in reached:
                reached.update((a, b))
        if reached == old:
            break
    if reached != {0, 1, 2, 3} or len(tree) != 3:
        return False, "staircase tree"
    if [b - a for a, b in sorted(tree, key=lambda e: e[1] - e[0])] != [1, 2, 3]:
        return False, "staircase span lengths"
    if not all(a < 2 <= b for a, b in tree):
        return False, "common train cut"

    internal = grouped(rows, (1, 2))
    if len(internal) != 2 or any(r.b_support != (0, 2) for r in internal):
        return False, "internal rows are not full B support"
    if any(r.edge != (0, 2) for r in rows if r.name.startswith("e02")):
        return False, "boundary row support"

    a_cuts: list[Vec] = []
    for cut in (1, 2, 3):
        total = (F(0), F(0))
        for row in rows:
            if crosses(row.a_support, cut):
                total = add(total, scale(row.beta, row.a_vec))
        a_cuts.append(total)
    expected_a = [vec(23, 0), vec(F(309, 13), 0), vec(18, 0)]
    if a_cuts != expected_a:
        return False, "A cut equations"

    b_cuts: list[Vec] = []
    for cut in (1, 2):
        total = (F(0), F(0))
        for row in rows:
            if crosses(row.b_support, cut):
                total = add(total, scale(row.beta, row.b_vec))
        b_cuts.append(total)

    p_int = (F(0), F(24, 13))
    expected_b = [
        (F(-11, 5), F(276, 65)),
        (F(14, 5), F(276, 65)),
    ]
    if b_cuts != expected_b:
        return False, "B cut equations"
    if p_int[1] <= 0:
        return False, "positive internal cross-shore load"
    if det(*b_cuts) == 0:
        return False, "B phase is exact"

    # gamma_j / C_j = lambda_j. This gives an exact radical-free check of
    # gamma_1 v_1 + gamma_2 v_2 = -u.
    lambdas = (F(1, 5), F(-1, 5))
    combined = add(scale(lambdas[0], b_cuts[0]), scale(lambdas[1], b_cuts[1]))
    if combined != vec(-1, 0):
        return False, "two-cut shear direction"

    # Boundary-only row resultants on the two B cuts; h0 is parallel to u and
    # contributes no work against -Ju. Work uses Jv_j = JQ_j / C_j.
    boundary = [(F(-16, 5), F(12, 5)), (F(9, 5), F(12, 5))]
    boundary_work = F(0)
    for lam, r_boundary, q in zip(lambdas, boundary, b_cuts):
        boundary_work += 2 * lam * dot(r_boundary, quarter_turn(q))
    internal_work = -2 * sum((r.beta * abs(r.c) for r in internal), F(0))
    if boundary_work != F(48, 13) or internal_work != F(-48, 13):
        return False, "boundary payment"
    if boundary_work + internal_work != 0:
        return False, "first variation stationarity"

    return True, "all exact cut, support, phase, and payment checks"


def failure_controls(rows: list[Row]) -> None:
    missing_boundary = [r for r in rows if r.name != "e02-"]
    assert not packet_balances(missing_boundary)
    assert valid_model(missing_boundary)[0] is False

    weakened_internal = [
        Row(r.name, r.edge, r.beta, r.a_vec, r.a_support, (0, 1), r.b_sign)
        if r.name == "e12-"
        else r
        for r in rows
    ]
    assert valid_model(weakened_internal)[1] == "internal rows are not full B support"


def main() -> None:
    rows = rows_for_model()
    ok, reason = valid_model(rows)
    assert ok, reason
    failure_controls(rows)
    print("OK: exact m=3, n=2 support-incidence cut-stress model")
    print("A cut resultants: (23,0), (309/13,0), (18,0)")
    print("B cut resultants: (-11/5,276/65), (14/5,276/65)")
    print("internal variation: -48/13; boundary-row payment: +48/13")
    print("controls: missing boundary row and weakened internal support rejected")
    print("Scope: algebraic cut equations only; no planar source realization")


main()
