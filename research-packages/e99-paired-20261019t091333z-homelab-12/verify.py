"""Check declared text receipts; see README.md for the mathematical replay."""

report = open("docs/reports/global_annular_matching_competitor_2026-10-11.md", "rb").read()
aggregate = open("research/global_annular_matching_2026_10_11.json", "rb").read()
certificate = open("research/certificates/global_annular_matching_proofs_2026_10_16.json", "rb").read()

assert b"maximum cardinality" in report and b"Every conflict endpoint" in report
assert aggregate.count(b'"packet_cases": 48') == 1
assert b'"Level I"' in aggregate and b'"unrestricted global optimality"' in aggregate
assert certificate.count(b'"fixture": "packet"') == 48
assert certificate.count(b'"fixture": "full-column"') == 3
assert certificate.count(b'"fixture": "odd-cycle"') == 1
assert b'"graphs": 1024' in certificate and b'"mutations": 4' in certificate

# Negative control: a changed expected packet count is not present in the receipt.
assert b'"packet_cases": 47' not in aggregate
print("PASS: scoped source text and exact finite receipt shape; no proof claim")
