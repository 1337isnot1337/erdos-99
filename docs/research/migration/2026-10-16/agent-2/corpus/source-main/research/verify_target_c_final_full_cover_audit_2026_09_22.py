#!/usr/bin/env python3
"""Audit the recorded exact full-cover closure of the final k=7 C profile.

This verifier checks the durable certificate in
``target_c_support7_global_segment_relative_eight_noroot_k7_final_full_cover_closure_2026-09-22.md``:
the macro-ranges must form an exact partition of the 325,955-state cover, the
reported counts must sum to the stated aggregate census, and every range must
report zero rank-11 lifts and the exact Hadamard bounds claimed by the note.

It does not treat a table as a substitute for running the finite geometric
verifier.  Its purpose is to make the recorded run auditable and to reject
silent omissions, overlaps, or arithmetic transcription errors in the durable
certificate.
"""

from __future__ import annotations

import re
from pathlib import Path


COVER_SIZE = 325_955
NOTE = Path(__file__).with_name(
    "target_c_support7_global_segment_relative_eight_noroot_k7_final_full_cover_closure_2026-09-22.md"
)


def main() -> None:
    text = NOTE.read_text()
    rows = []
    in_table = False
    for line in text.splitlines():
        if line.startswith("start,end,sync,witnesses,lifts,retained,extra10,extra11,"):
            in_table = True
            continue
        if not in_table:
            continue
        if not re.fullmatch(r"\d+(?:,\d+){11}", line):
            if rows:
                break
            continue
        rows.append(tuple(map(int, line.split(","))))

    assert len(rows) == 33, len(rows)
    cursor = 0
    for row in rows:
        start, end = row[:2]
        assert start == cursor, row
        assert start < end <= COVER_SIZE, row
        assert row[6] == row[5], row  # every retained lift has extra rank 10
        assert row[7] == 0, row       # no seven-row rank-11 lift
        assert row[8] <= 45 and row[9] <= 25, row
        assert row[10] <= 24 and row[11] <= 25, row
        cursor = end
    assert cursor == COVER_SIZE, cursor

    totals = [sum(row[index] for row in rows) for index in range(2, 8)]
    assert totals == [1_751_870, 136_450, 968_687, 49_249, 49_249, 0], totals
    assert max(row[8] for row in rows) == 45
    assert max(row[9] for row in rows) == 25
    assert max(row[10] for row in rows) == 24
    assert max(row[11] for row in rows) == 25
    assert "P = 2^127 - 1" in text
    assert "P^2 > 45^25" in text
    assert "P^2 > 24^15" in text
    assert "C:(5,12,12), d_6=5 is impossible." in text
    print("PASS: final k=7 C profile certificate has exact coverage and census")
    print("cover_partition", (0, COVER_SIZE))
    print("aggregate", totals)
    print("max_norm2_width", (45, 25, 24, 25))


if __name__ == "__main__":
    main()
