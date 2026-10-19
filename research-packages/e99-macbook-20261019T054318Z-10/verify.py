"""Independent exact reconstruction of PR #114's finite cut-stress model."""

from fractions import Fraction as F

Vec = tuple[F, F]
Interval = tuple[int, int] | None


def v(x: int | F, y: int | F) -> Vec:
    return F(x), F(y)


def add(a: Vec, b: Vec) -> Vec:
    return a[0] + b[0], a[1] + b[1]


def scale(k: F, a: Vec) -> Vec:
    return k * a[0], k * a[1]


def dot(a: Vec, b: Vec) -> F:
    return a[0] * b[0] + a[1] * b[1]


def det(a: Vec, b: Vec) -> F:
    return a[0] * b[1] - a[1] * b[0]


def j(a: Vec) -> Vec:
    return -a[1], a[0]


def crosses(support: Interval, cut: int) -> bool:
    return support is not None and support[0] < cut <= support[1]


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
    def a_transverse(self) -> F:
        return self.a_vec[1]

    @property
    def b_vec(self) -> Vec | None:
        return None if self.b_sign is None else scale(F(self.b_sign), self.a_vec)


def fixture() -> list[Row]:
    return [
        Row("h0", None, F(1), v(1, 0), (0, 3), (0, 2), 1),
        Row("e02+", (0, 2), F(3), v(F(3, 5), F(4, 5)), (0, 2), (1, 2), 1),
        Row("e02-", (0, 2), F(4), v(F(4, 5), F(-3, 5)), (0, 2), (0, 1), -1),
        Row("e03+", (0, 3), F(8), v(F(8, 17), F(15, 17)), (0, 3), None, None),
        Row("e03-", (0, 3), F(15), v(F(15, 17), F(-8, 17)), (0, 3), None, None),
        Row("e12+", (1, 2), F(1), v(F(5, 13), F(12, 13)), (1, 2), (0, 2), 1),
        Row("e12-", (1, 2), F(1), v(F(5, 13), F(-12, 13)), (1, 2), (0, 2), -1),
    ]


def row_vector(row: Row, shore: str) -> Vec | None:
    return row.a_vec if shore == "A" else row.b_vec


def row_support(row: Row, shore: str) -> Interval:
    return row.a_support if shore == "A" else row.b_support


def changed(row: Row, **changes) -> Row:
    fields = {
        "name": row.name,
        "edge": row.edge,
        "beta": row.beta,
        "a_vec": row.a_vec,
        "a_support": row.a_support,
        "b_support": row.b_support,
        "b_sign": row.b_sign,
    }
    fields.update(changes)
    return Row(**fields)


def cut_contributions(rows: list[Row], shore: str, cut: int) -> dict[str, Vec]:
    out: dict[str, Vec] = {}
    for row in rows:
        vector = row_vector(row, shore)
        if vector is not None and crosses(row_support(row, shore), cut):
            out[row.name] = scale(row.beta, vector)
    return out


def cut_sum(rows: list[Row], shore: str, cut: int) -> Vec:
    total = v(0, 0)
    for contribution in cut_contributions(rows, shore, cut).values():
        total = add(total, contribution)
    return total


def cut_sums(rows: list[Row], shore: str, cuts: tuple[int, ...]) -> tuple[Vec, ...]:
    return tuple(cut_sum(rows, shore, cut) for cut in cuts)


def packet_data(rows: list[Row]) -> dict[tuple[int, int], tuple[F, Vec]]:
    result: dict[tuple[int, int], tuple[F, Vec]] = {}
    for edge in ((0, 2), (0, 3), (1, 2)):
        packet = [row for row in rows if row.edge == edge]
        transverse = sum((row.beta * row.a_transverse for row in packet), F(0))
        longitudinal = sum((row.beta * row.a_vec[0] for row in packet), F(0))
        result[edge] = transverse, v(longitudinal, 0)
    return result


def grouped_work(rows: list[Row], q: tuple[Vec, Vec], lambdas: tuple[F, F]) -> dict[str, F]:
    groups = {"internal": F(0), "boundary": F(0), "reference": F(0), "other": F(0)}
    for row in rows:
        if row.b_vec is None:
            continue
        category = (
            "internal" if row.edge == (1, 2)
            else "boundary" if row.edge == (0, 2)
            else "reference" if row.name == "h0"
            else "other"
        )
        for index, cut in enumerate((1, 2)):
            if crosses(row.b_support, cut):
                groups[category] += 2 * lambdas[index] * row.beta * dot(row.b_vec, j(q[index]))
    return groups


def internal_load(rows: list[Row]) -> Vec:
    total = v(0, 0)
    for row in rows:
        if row.edge == (1, 2) and row.b_vec is not None:
            total = add(total, scale(row.beta, row.b_vec))
    return total


def support_inventory_is_valid(rows: list[Row]) -> bool:
    if {row.name for row in rows} != {
        "h0", "e02+", "e02-", "e03+", "e03-", "e12+", "e12-"
    }:
        return False
    tree = {row.edge for row in rows if row.edge is not None}
    if tree != {(0, 2), (0, 3), (1, 2)}:
        return False
    if sorted(b - a for a, b in tree) != [1, 2, 3]:
        return False
    if not all(a < 2 <= b for a, b in tree):
        return False
    expected_a = {
        "h0": (0, 3),
        "e02+": (0, 2),
        "e02-": (0, 2),
        "e03+": (0, 3),
        "e03-": (0, 3),
        "e12+": (1, 2),
        "e12-": (1, 2),
    }
    expected_b = {
        "h0": (0, 2),
        "e02+": (1, 2),
        "e02-": (0, 1),
        "e03+": None,
        "e03-": None,
        "e12+": (0, 2),
        "e12-": (0, 2),
    }
    expected_signs = {
        "h0": 1,
        "e02+": 1,
        "e02-": -1,
        "e03+": None,
        "e03-": None,
        "e12+": 1,
        "e12-": -1,
    }
    return (
        {row.name: row.a_support for row in rows} == expected_a
        and {row.name: row.b_support for row in rows} == expected_b
        and {row.name: row.b_sign for row in rows} == expected_signs
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    rows = fixture()

    require(len(rows) == 7 and all(row.beta > 0 for row in rows), "row inventory or positive stress")
    require(support_inventory_is_valid(rows), "A/B support inventory or staircase tree")
    require(all(dot(row.a_vec, row.a_vec) == 1 for row in rows), "unit row length")
    for i, row in enumerate(rows):
        for other in rows[i + 1 :]:
            require(det(row.a_vec, other.a_vec) != 0, f"parallel rows: {row.name}, {other.name}")

    packets = packet_data(rows)
    require(packets == {
        (0, 2): (F(0), v(5, 0)),
        (0, 3): (F(0), v(17, 0)),
        (1, 2): (F(0), v(F(10, 13), 0)),
    }, f"edgewise packet balance/results: {packets}")

    a = cut_sums(rows, "A", (1, 2, 3))
    b = cut_sums(rows, "B", (1, 2))
    require(a == (v(23, 0), v(F(309, 13), 0), v(18, 0)), f"A cuts: {a}")
    require(b == (v(F(-11, 5), F(276, 65)), v(F(14, 5), F(276, 65))), f"B cuts: {b}")

    p_int = internal_load(rows)
    require(p_int == v(0, F(24, 13)), f"derived internal load: {p_int}")
    determinant = det(*b)
    require(determinant == F(-276, 13), f"B determinant: {determinant}")
    lambdas = (F(1, 5), F(-1, 5))
    shear = add(scale(lambdas[0], b[0]), scale(lambdas[1], b[1]))
    require(shear == v(-1, 0), f"shear: {shear}")

    work = grouped_work(rows, b, lambdas)
    require(work == {
        "internal": F(-48, 13),
        "boundary": F(48, 13),
        "reference": F(0),
        "other": F(0),
    }, f"work ledger: {work}")
    require(sum(work.values(), F(0)) == 0, f"total work: {work}")

    # Control 1: deleting a boundary row breaks both its A packet balance and
    # the cut combination that produced the claimed shear direction.
    removed = [row for row in rows if row.name != "e02-"]
    removed_packet = packet_data(removed)[(0, 2)][0]
    removed_b = cut_sums(removed, "B", (1, 2))
    removed_shear = add(scale(lambdas[0], removed_b[0]), scale(lambdas[1], removed_b[1]))
    require(removed_packet == F(12, 5), f"removed-row packet: {removed_packet}")
    require(removed_b == (v(1, F(24, 13)), b[1]), f"removed-row cuts: {removed_b}")
    require(removed_shear == v(F(-9, 25), F(-12, 25)), f"removed-row shear: {removed_shear}")
    require(removed_shear != v(-1, 0), "row removal retained the claimed shear")

    # Control 2: a weakened internal support omits e12- from B cut 2.
    weakened = [
        changed(row, b_support=(0, 1)) if row.name == "e12-" else row
        for row in rows
    ]
    weak_b = cut_sums(weakened, "B", (1, 2))
    weak_shear = add(scale(lambdas[0], weak_b[0]), scale(lambdas[1], weak_b[1]))
    require(not support_inventory_is_valid(weakened), "weakened internal support escaped support check")
    require(weak_b == (b[0], v(F(207, 65), F(216, 65))), f"weakened-support cuts: {weak_b}")
    require(weak_shear == v(F(-14, 13), F(12, 65)), f"weakened-support shear: {weak_shear}")
    require(weak_shear != v(-1, 0), "weakened support retained the claimed shear")

    # Control 3: independently perturb a still-positive stress coefficient.
    corrupt = [
        changed(row, beta=F(4)) if row.name == "e02+" else row
        for row in rows
    ]
    corrupt_packet = packet_data(corrupt)[(0, 2)][0]
    corrupt_b = cut_sums(corrupt, "B", (1, 2))
    corrupt_shear = add(scale(lambdas[0], corrupt_b[0]), scale(lambdas[1], corrupt_b[1]))
    require(corrupt_packet == F(4, 5), f"corrupt packet balance: {corrupt_packet}")
    require(corrupt_b == (b[0], v(F(17, 5), F(328, 65))), f"corrupt cuts: {corrupt_b}")
    require(corrupt_shear == v(F(-28, 25), F(-4, 25)), f"corrupt shear: {corrupt_shear}")
    require(corrupt_shear != v(-1, 0), "corrupted multiplier retained the claimed shear")

    print("PASS: exact seven-row A/B support and cut reconstruction")
    print("A cuts:", a)
    print("B cuts:", b)
    print("internal load:", p_int, "B determinant:", determinant)
    print("shear:", shear, "work ledger:", work)
    print("control 1 row removal:", removed_b, "shear", removed_shear)
    print("control 2 weakened support:", weak_b, "shear", weak_shear)
    print("control 3 positive-stress corruption:", corrupt_b, "shear", corrupt_shear)
    print("Scope: finite incidence/stress model; no source realization or global optimality")


main()
