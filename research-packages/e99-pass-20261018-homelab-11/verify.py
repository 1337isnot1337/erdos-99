"""Finite bookkeeping regressions for endpoint assignments; not a theorem proof."""


def edge(a, b):
    return (a, b) if a < b else (b, a)


def check_assignment(edges, owners):
    assert set(owners) == set(edges)
    assert all(v in e for e, v in owners.items())
    assert len(set(owners.values())) == len(owners)
    vertices = {v for e in edges for v in e}
    adjacency = {v: [] for v in vertices}
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    partners = {owners[e]: next(v for v in e if v != owners[e]) for e in edges}
    for v in vertices:
        if v not in partners:
            partners[v] = min(adjacency[v])
    edge_value = {e: i + 1 for i, e in enumerate(sorted(edges))}
    endpoint_value = {v: edge_value[edge(v, p)] for v, p in partners.items()}
    for threshold in range(1, max(edge_value.values()) + 2):
        edge_tail = sum(value >= threshold for value in edge_value.values())
        endpoint_tail = sum(value >= threshold for value in endpoint_value.values())
        assert edge_tail <= endpoint_tail
    for power in (1, 2):
        assert sum(value ** power for value in edge_value.values()) <= sum(
            value ** power for value in endpoint_value.values()
        )
    return len(edges), len(set(owners.values()))


def forest_assignment(edges):
    adjacency = {}
    for a, b in edges:
        adjacency.setdefault(a, set()).add(b)
        adjacency.setdefault(b, set()).add(a)
    unseen = set(adjacency)
    owners = {}
    while unseen:
        root = min(unseen)
        parent = {root: None}
        queue = [root]
        unseen.remove(root)
        for u in queue:
            for v in sorted(adjacency[u]):
                if v not in parent:
                    parent[v] = u
                    unseen.discard(v)
                    queue.append(v)
                    owners[edge(u, v)] = v
                elif parent[u] != v:
                    raise AssertionError("fixture is not a forest")
    return owners


def cycle_leaf_assignment(cycle, leaves):
    owners = {}
    for i, u in enumerate(cycle):
        v = cycle[(i + 1) % len(cycle)]
        owners[edge(u, v)] = v
    for leaf, anchor in leaves:
        assert leaf not in cycle and leaf not in owners.values()
        owners[edge(leaf, anchor)] = leaf
    return owners


def main():
    forest = {
        edge(0, 1), edge(1, 2), edge(2, 3), edge(1, 4), edge(2, 5),
        edge(6, 7), edge(7, 8),
    }
    result_tree = check_assignment(forest, forest_assignment(forest))

    cycle = [0, 1, 2, 3, 4]
    leaves = [(5, 0), (6, 2), (7, 2)]
    unicyclic = {edge(cycle[i], cycle[(i + 1) % 5]) for i in range(5)}
    unicyclic.update(edge(leaf, anchor) for leaf, anchor in leaves)
    result_cycle = check_assignment(
        unicyclic, cycle_leaf_assignment(cycle, leaves)
    )

    # Loaded-only control: the active 5-cycle assignment cannot cover an
    # additional actual edge in a larger graph. Full-graph topology must be
    # established directly before using the injection.
    loaded = {edge(cycle[i], cycle[(i + 1) % 5]) for i in range(5)}
    extra = edge(8, 9)
    assert extra not in loaded
    assert set(cycle_leaf_assignment(cycle, [])) == loaded
    assert extra not in cycle_leaf_assignment(cycle, [])

    print("PASS forest edge injection and finite tail/moment domination:", result_tree)
    print("PASS odd-cycle-with-leaves injection and finite domination:", result_cycle)
    print("PASS loaded-subgraph control detects an uncovered extra edge")
    print("LIMIT: fixtures do not prove diameter-graph topology or endpoint bounds")


main()
