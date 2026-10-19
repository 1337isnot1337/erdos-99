"""Replay the exact sector-population inequality on pinned Target A ledgers."""

import json




def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_xi(name, xi, o_iso, o_by_sector, c_by_sector):
    require(len(o_by_sector) == len(c_by_sector), name + ": sector arity mismatch")
    reconstructed = o_iso + sum(max(0, o - c) for o, c in zip(o_by_sector, c_by_sector))
    require(reconstructed == xi, name + ": sink-surplus reconstruction mismatch")


def check_pointwise(name, xi, o, t_o, c_sector_sum):
    # Xi = O_iso + sum_i (O_i-C_i)_+ >= |O|-|T_O|-sum_i |C_i|.
    margin = xi - (o - t_o - c_sector_sum)
    require(margin >= 0, name + ": exact sector population inequality failed")
    return margin


def main():
    seed63 = json.JSONDecoder().decode(open("research-packages/target-a-fan-tube-ledger/evidence.json").read())
    ledgers63 = seed63["ledgers"]
    admissible = [row for row in ledgers63 if row["section102_admissible"]]
    relaxed = [row for row in ledgers63 if not row["section102_admissible"]]
    require(len(admissible) == 18, "seed-63 admissible control count changed")
    require(len(relaxed) == 18, "seed-63 relaxed control count changed")

    margins63 = []
    for row in admissible:
        name = "seed-63 M=" + str(row["M"])
        require(row["canonical_boundary_schur"], name + ": missing admissible Schur basis")
        check_xi(name, row["Xi"], row["O_iso"], row["O_i"], row["C_i"])
        c_sector_sum = sum(row["C_i"])
        shield_terminals = row["boundary_terminals"] - c_sector_sum
        require(shield_terminals >= 0, name + ": negative shield-terminal count")
        require(row["O"] == row["T_O"] + row["O_iso"] + sum(row["O_i"]),
                name + ": exterior-sink partition mismatch")
        margins63.append(check_pointwise(
            name, row["Xi"], row["O"], row["T_O"], c_sector_sum
        ))

    # This guards the superseded depth-only relaxation: do not use these rows
    # to support the Section-102 conclusion, even if their relaxed cut is larger.
    for row in relaxed:
        require(not row["canonical_boundary_schur"], "relaxed basis accepted as canonical")
        require(row["basis"] == "relaxed-optimum", "unexpected seed-63 negative control")

    seed66 = json.JSONDecoder().decode(open("research-packages/target-a-full-tube-fan-ledger/evidence.json").read())
    cases66 = seed66["cases"]
    require(len(cases66) == 34, "seed-66 case count changed")
    margins66 = []
    for row in cases66:
        name = "seed-66 m=" + str(row["m"]) + " phase=" + str(row["phase_numerators"])
        o_by_sector = [sector["O"] for sector in row["sectors"]]
        c_by_sector = [sector["C"] for sector in row["sectors"]]
        check_xi(name, row["Xi"], row["isolated_exterior_sinks"], o_by_sector, c_by_sector)
        c_sector_sum = sum(c_by_sector)
        shield_terminals = row["shield_terminals"]
        require(shield_terminals >= 0, name + ": negative shield-terminal count")
        require(c_sector_sum + shield_terminals == 3 * row["m"] + 1,
                name + ": terminal population partition mismatch")
        require(row["exterior_rows"] == row["tube_exterior"]
                + row["isolated_exterior_sinks"] + sum(o_by_sector),
                name + ": exterior-sink partition mismatch")
        margins66.append(check_pointwise(
            name, row["Xi"], row["exterior_rows"], row["tube_exterior"], c_sector_sum
        ))

    result = {
        "status": "passed",
        "classification": "exact finite regression control; not a global-source result",
        "seed63": {
            "admissible_ledgers_checked": len(admissible),
            "nonadmissible_relaxed_ledgers_excluded": len(relaxed),
            "pointwise_population_checks": len(margins63),
            "minimum_margin": min(margins63),
        },
        "seed66": {
            "fixed_phase_cases_checked": len(cases66),
            "pointwise_population_checks": len(margins66),
            "minimum_margin": min(margins66),
        },
        "source_demand": "not supplied by either predecessor fixture",
        "canonical_implication": "none without proving the population condition in README.md",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


main()
