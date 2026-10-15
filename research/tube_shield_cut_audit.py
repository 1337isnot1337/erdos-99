"""Exact finite audit of the tube-only response-cut bound.

Tests generic bipartite response graphs with two basis vertices, two terminals,
two matched interior rows and one exterior sink. All 1,024 edge sets containing
the prescribed basis matching are enumerated, along with every right-shore tube
and every admissible shield-terminal subset. Sectors are components after deleting
the basis-closed shield. Matching arithmetic is integer/exhaustive.

Encodes alternating orientation, basis closure, and the condition that every
shielded terminal has all neighbors in the tube. Omits unit geometry, locked
stress, source labels, and global optimality. A pass checks these finite models,
not the general theorem or Erdős #99. The adjacent 2026-09-08 report proves the
general bound. Run: python3 research/tube_shield_cut_audit.py
"""

from itertools import product


def matching_size(adj):
    owner = {}

    def augment(left, seen):
        for right in adj[left]:
            if right in seen:
                continue
            seen.add(right)
            if right not in owner or augment(owner[right], seen):
                owner[right] = left
                return True
        return False

    return sum(augment(left, set()) for left in adj)


def subsets(items):
    items = tuple(items)
    for bits in product((False, True), repeat=len(items)):
        yield {item for item, bit in zip(items, bits) if bit}


def run():
    basis, terminals, interior, sinks = {0, 1}, {2, 3}, {4, 5}, {6}
    left, right = basis | terminals, interior | sinks
    fixed = {(0, 4), (1, 5)}
    optional = sorted(set(product(left, right)) - fixed)
    checked = strict_improvements = 0
    for extra in subsets(optional):
        edges = fixed | extra
        adj = {x: {y for a, y in edges if a == x} for x in left}
        nullity = len(terminals) - (matching_size(adj) - len(basis))
        for tube in subsets(right):
            eligible = {c for c in terminals if adj[c] <= tube}
            for shield_terminals in subsets(eligible):
                shield = tube | shield_terminals | {b for b, z in fixed if z in tube}
                remaining = (left | right) - shield
                undirected = {v: set() for v in remaining}
                for a, b in edges:
                    if a in remaining and b in remaining:
                        undirected[a].add(b)
                        undirected[b].add(a)
                surplus = 0
                while remaining:
                    root = remaining.pop()
                    component, todo = {root}, [root]
                    while todo:
                        for neighbor in undirected[todo.pop()] - component:
                            component.add(neighbor)
                            remaining.discard(neighbor)
                            todo.append(neighbor)
                    surplus += max(0, len(component & terminals) - len(component & sinks))
                lower = len(shield_terminals) + surplus - len(tube)
                old_lower = surplus - len(shield - terminals)
                assert nullity >= lower, (edges, tube, shield_terminals, nullity, lower)
                assert lower >= old_lower
                strict_improvements += lower > old_lower
                checked += 1
    # One alternating path c -> z -> b -> o needs one unit of tube capacity.
    assert matching_size({0: {4, 6}, 2: {4}}) - 1 == 1
    print(f"PASS: {checked} exact graph/tube/shield cases; "
          f"{strict_improvements} strictly improved lower bounds.")
    print("No geometry or global-optimality claim is tested.")


if __name__ == "__main__":
    run()
