from fractions import Fraction as F
from itertools import combinations
import json


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def point(x, y):
    return (F(x), F(y))


def distance2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def pair_table(points):
    return {
        (a, b): distance2(points[a], points[b])
        for a, b in combinations(sorted(points), 2)
    }


def edges_at(table, value):
    return [edge for edge, d2 in table.items() if d2 == value]


def isolates(labels, edges):
    incident = {label for edge in edges for label in edge}
    return sorted(set(labels) - incident)


def rank(matrix):
    if not matrix:
        return 0
    work = [[F(value) for value in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (r for r in range(pivot_row, row_count) if work[r][column]), None
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for r in range(row_count):
            if r == pivot_row:
                continue
            scale = work[r][column]
            if scale:
                work[r] = [
                    left - scale * right
                    for left, right in zip(work[r], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def lower_gradient(points, edge):
    a, b = edge
    delta_x = 2 * (points[a][0] - points[b][0])
    delta_y = 2 * (points[a][1] - points[b][1])
    result = [F(0)] * (2 * len(points))
    labels = sorted(points)
    ia, ib = labels.index(a), labels.index(b)
    result[2 * ia] = delta_x
    result[2 * ia + 1] = delta_y
    result[2 * ib] = -delta_x
    result[2 * ib + 1] = -delta_y
    return result


def equilibrium_matrix(points, lower_edges, upper_edges):
    columns = [lower_gradient(points, edge) for edge in lower_edges]
    columns.extend(
        [-value for value in lower_gradient(points, edge)]
        for edge in upper_edges
    )
    return [list(row) for row in zip(*columns)]


def matrix_times_vector(matrix, vector):
    return [sum((a * b for a, b in zip(row, vector)), F(0)) for row in matrix]


def check_pair_bounds(table, low, high, strict=False):
    if strict:
        require(all(low < value < high for value in table.values()), "strict pair bounds")
    else:
        require(all(low <= value <= high for value in table.values()), "closed pair bounds")


def check():
    old_d2 = F(81)
    source = {f"p{i}": point(i, 0) for i in range(10)}
    source["q"] = point(F(1, 2), F(11, 10))
    source_pairs = pair_table(source)
    source_contacts = edges_at(source_pairs, F(1))
    source_actual = edges_at(source_pairs, max(source_pairs.values()))
    expected_contacts = [(f"p{i}", f"p{i + 1}") for i in range(9)]
    require(len(source_pairs) == 55, "source pair count")
    check_pair_bounds(source_pairs, F(1), old_d2)
    require(max(source_pairs.values()) == old_d2, "source diameter squared")
    require(source_contacts == expected_contacts, "source contact path")
    require(source_actual == [("p0", "p9")], "source actual diameter pair")
    require(isolates(source, source_contacts) == ["q"], "source contact isolate")

    source_matrix = equilibrium_matrix(source, source_contacts, source_actual)
    weights = [F(9)] * 9 + [F(1)]
    require(rank(source_matrix) == 9, "source equilibrium rank")
    require(matrix_times_vector(source_matrix, weights) == [F(0)] * len(source_matrix),
            "source normalized stress force balance")
    normalized = [row + [F(0)] for row in source_matrix]
    normalized.append([F(0)] * 9 + [F(1)])
    require(rank(normalized) == 10, "normalized stress rank")

    retained = {label: value for label, value in source.items() if label != "p0"}
    retained_pairs = pair_table(retained)
    retained_contacts = edges_at(retained_pairs, F(1))
    require(len(retained) == 10 and len(retained_pairs) == 45, "deletion cardinality and pairs")
    check_pair_bounds(retained_pairs, F(1), old_d2)
    require(max(retained_pairs.values()) < old_d2, "deleted source has no old-D pair")
    require(retained_contacts == expected_contacts[1:], "deleted contact path")
    require(isolates(retained, retained_contacts) == ["q"], "retained contact isolate")
    retained_contact_matrix = equilibrium_matrix(retained, retained_contacts, [])
    require(rank(retained_contact_matrix) == len(retained_contacts),
            "retained contacts admit no nonzero equilibrium stress")

    # A concrete first motion opens every retained contact; q remains a label.
    velocities = {label: point(int(label[1:]), 0) for label in retained if label.startswith("p")}
    velocities["q"] = point(0, 0)
    for a, b in retained_contacts:
        edge = (retained[a][0] - retained[b][0], retained[a][1] - retained[b][1])
        velocity = (velocities[a][0] - velocities[b][0], velocities[a][1] - velocities[b][1])
        derivative = 2 * (edge[0] * velocity[0] + edge[1] * velocity[1])
        require(derivative == 2, "retained contact opens under the stated velocity")

    inserted = point(F(8, 5), F(11, 10))
    strict_restored = dict(retained)
    strict_restored["r"] = inserted
    strict_pairs = pair_table(strict_restored)
    check_pair_bounds(strict_pairs, F(1), old_d2)
    replacement_pairs = {
        edge: value for edge, value in strict_pairs.items() if "r" in edge
    }
    require(len(strict_restored) == len(source), "strict restoration cardinality")
    require(len(replacement_pairs) == 10, "all packet-to-retained pairs enumerated")
    require(all(F(1) < value < old_d2 for value in replacement_pairs.values()),
            "strict packet margins including retained isolate")
    require(len(edges_at(strict_pairs, F(1))) == 8, "strict restoration contact decrease")
    require(isolates(strict_restored, edges_at(strict_pairs, F(1))) == ["q", "r"],
            "strict restoration isolates")
    strict_d2 = max(strict_pairs.values())
    strict_actual = edges_at(strict_pairs, strict_d2)
    require(strict_d2 == F(3673, 50), "strict restoration diameter squared")
    require(strict_actual == [("p9", "q")], "inactive old upper becomes actual D-prime pair")
    require(source_pairs[("p9", "q")] == strict_d2 < old_d2,
            "old inactive upper is newly active only at smaller D-prime")
    require(all(strict_pairs[edge] == value for edge, value in retained_pairs.items()),
            "all retained-retained pairs unchanged")

    # Weak lower margin: putting the deleted label back recreates the source.
    weak_lower = dict(retained)
    weak_lower["p0"] = source["p0"]
    weak_lower_pairs = pair_table(weak_lower)
    require(weak_lower_pairs == source_pairs, "weak-lower control equals original source")
    require(len(edges_at(weak_lower_pairs, F(1))) == 9, "weak lower restores a contact")
    require(max(weak_lower_pairs.values()) == old_d2, "weak lower restores old diameter")

    # Weak upper margin: the rational point creates a new pair exactly at old D.
    weak_upper = dict(retained)
    weak_upper["rweak"] = point(F(32, 5), F(36, 5))
    weak_upper_pairs = pair_table(weak_upper)
    check_pair_bounds(weak_upper_pairs, F(1), old_d2)
    weak_upper_new = {
        edge: value for edge, value in weak_upper_pairs.items() if "rweak" in edge
    }
    require(all(value > F(1) for value in weak_upper_new.values()),
            "weak-upper control adds no contacts")
    require(weak_upper_pairs[("p1", "rweak")] == old_d2,
            "weak upper creates new actual old-D pair")
    require(max(weak_upper_pairs.values()) == old_d2, "weak-upper endpoint diameter")
    require(edges_at(weak_upper_pairs, old_d2) == [("p1", "rweak")],
            "weak-upper replacement diameter graph")
    require(len(edges_at(weak_upper_pairs, F(1))) == 8,
            "weak-upper control still deletes a contact")

    # A k-label packet after deleting only an isolate does not force improvement.
    q_prime = point(F(1, 2), F(6, 5))
    isolate_only = {f"p{i}": source[f"p{i}"] for i in range(10)}
    isolate_only["qprime"] = q_prime
    isolate_only_pairs = pair_table(isolate_only)
    check_pair_bounds(isolate_only_pairs, F(1), old_d2)
    qprime_pairs = {edge: value for edge, value in isolate_only_pairs.items() if "qprime" in edge}
    require(all(F(1) < value < old_d2 for value in qprime_pairs.values()),
            "isolated-label replacement has strict pair margins")
    require(len(edges_at(isolate_only_pairs, F(1))) == 9,
            "isolated-label one-for-one replacement preserves contacts")
    require(max(isolate_only_pairs.values()) == old_d2,
            "isolated-label one-for-one replacement preserves diameter")

    # A one-label shortfall after deleting p0 changes n and cannot compare to D(n).
    require(len(retained) == len(source) - 1, "shortfall control cardinality")
    require(max(retained_pairs.values()) == F(3673, 50) < old_d2,
            "shortfall control has a smaller but wrong-cardinality diameter")

    # The k+1 fallback deletes isolate q plus p0 and restores two packet labels.
    fallback = {f"p{i}": source[f"p{i}"] for i in range(1, 10)}
    fallback["qnew"] = source["q"]
    fallback["rnew"] = inserted
    fallback_pairs = pair_table(fallback)
    check_pair_bounds(fallback_pairs, F(1), old_d2)
    fallback_new = {
        edge: value for edge, value in fallback_pairs.items()
        if "qnew" in edge or "rnew" in edge
    }
    require(all(F(1) < value < old_d2 for value in fallback_new.values()),
            "k+1 fallback checks packet and every retained pair")
    require(len(fallback) == len(source), "k+1 fallback cardinality")
    require(len(edges_at(fallback_pairs, F(1))) == 8, "k+1 fallback contact decrease")
    require(max(fallback_pairs.values()) == F(3673, 50), "k+1 fallback strict diameter")

    return {
        "source": {
            "labels": len(source),
            "pairs": len(source_pairs),
            "contacts": len(source_contacts),
            "actual_diameter_pairs": source_actual,
            "D_squared": str(old_d2),
            "equilibrium_rank": rank(source_matrix),
            "normalized_rank": rank(normalized),
            "contact_isolates": ["q"],
        },
        "deletion": {
            "labels": len(retained),
            "pairs": len(retained_pairs),
            "contacts": len(retained_contacts),
            "old_D_pairs": edges_at(retained_pairs, old_d2),
            "contact_isolates": ["q"],
        },
        "strict_restoration": {
            "labels": len(strict_restored),
            "pairs": len(strict_pairs),
            "contacts": len(edges_at(strict_pairs, F(1))),
            "D_prime_squared": str(strict_d2),
            "actual_D_prime_pairs": strict_actual,
            "contact_isolates": ["q", "r"],
        },
        "controls": {
            "weak_lower_restores_source": True,
            "weak_upper_new_old_D_pair": ["p1", "rweak"],
            "isolate_only_k_packet_keeps_nine_contacts": True,
            "shortfall_labels": len(retained),
            "k_plus_one_fallback_contacts": len(edges_at(fallback_pairs, F(1))),
        },
        "verdict": "exact fixture and stated conditional implications pass; no source-wide packet extraction is proved",
    }


print(json.dumps(check(), indent=2, sort_keys=True))
