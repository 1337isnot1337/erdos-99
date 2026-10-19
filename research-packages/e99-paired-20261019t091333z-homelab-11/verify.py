"""Check the captured replay matches the pinned certificate byte-for-byte."""

replay = open(
    "research-packages/e99-paired-20261019t091333z-homelab-11/pinned-replay.jsonl",
    "rb",
).read()
certificate = open(
    "research/certificates/target_c_unequal_height_release_2026_10_10.jsonl",
    "rb",
).read()
assert replay == certificate
assert len(replay.splitlines()) == 4
assert replay.count(b'"full_pair_state_checks":') == 3
assert b'"H": 30' in replay
assert b'"H": 31' in replay
assert b'"H": 100' in replay
assert replay.count(b'"all_upper_pairs_checked": true') == 3
assert replay.count(b'"global_minimizer": false') == 3
assert replay.count(b'"transported_isolate_active_support": [1, 2, 3]') == 3
assert b'"strict_limit_noncontact_pairs": 5858' in replay
assert b'"critical_pairs": [' in replay
print("PASS: captured 30/31/100 and symbolic replay exactly matches the pinned certificate")
