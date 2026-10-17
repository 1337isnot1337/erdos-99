ERDOS-99 INTEGRATION VERIFICATION RECEIPT

Purpose
-------
Preserve inspectable local evidence for the integration and its two bounded
followups. PR99 merged as 1dd10cdb1ecdd79be6285860ba3a17d6d946d79e, with tree
fd8bdc3484464778783805b05d006527b11bfa51, identical to the reviewed final head.
PR87 and PR92 were closed as superseded after integration. No new broad checks
or mathematical review were run while assembling this bundle.

Commit and tree identities
--------------------------
Full certificate/repository verification:
  local  3c45a937314c058884535c76871f120ef71baf59
  public c5911c89e0407e43d6ad637dc2620971b7d157b4
  tree   67bb73ab2b0a257b5ed0e0c9cc7106d8af5bb837
Integrity-budget followup:
  local  d7e5871ca14e66bf6a98fa3c89b512c4282f6a02
  public 2c38f9f0c5925bad5dd8f953ef912edf7aafe91a
  tree   aacdfc6d80435bd5e210a14b3f8f190bbdf7f8c4
Profile-only followup:
  local  221fa2bbcfa58567df17e9cebbb3f4d11bf038d0
  public bbc2052917a9ec588dbccf9374f28d5414970c11
  tree   fd8bdc3484464778783805b05d006527b11bfa51
Original comparison base: e396ea07887dd0528b817ce4e656ff0e6b01f8fb
Public mappings were supplied by the integrating agent; local trees were
independently resolved when assembling the bundle.

Recorded outcomes
-----------------
Full-suite tree:
  94/94 unique registered certificate commands: PASS, runner terminal OK.
  Full replay: 642.541 seconds against the recorded 1,200-second budget.
  Public corpus: zero errors; 94 certificates, 451 claims, 845 edges,
    1,451 artifacts, 25 tasks, seven nonredistributed-reference links.
  Trusted integrity: zero structural errors, exit 0, 128.275 seconds.
  Focused unittests: 155 total reported run; five skipped; 150 executed passes;
    zero failures/errors. The log reports 38.715 test seconds.
  Package metadata: valid, classification regression; no commands executed.
  Verification plan: full-verification-required; replay schedule requires-review;
    no automatic replay authorized. This is a plan, not replay evidence.
Budget-followup tree:
  Bounded integrity: exit 0 in 133.266 seconds, within its 180-second limit.
  CI unittests: 78 total reported run; five skipped; 73 executed passes;
    zero failures/errors. The log reports 22.901 test seconds.
Profile-followup tree:
  Independent static review: PASS within the workflow-boundary scope.
  Hosted run 39078673224: isolated Python startup passed; all 72 trusted-control
  tests passed with zero skips. The old e396 control then rejected an unchanged
  243-character archive path before theorem metadata parsing. This is a failed
  integration run with a verified sandbox repair, not a green integration check.

The full replay and repository checks above were performed on the full-suite
tree. The budget followup has separate recorded checks. The profile-only change
has the separate static review in this bundle. Do not describe the latest tree
as freshly running the full suite, or count skipped tests as executed passes.

Evidence files
--------------
index.json: structured results, exact identities, integration and hosted outcomes.
certificate-runner-summary.txt: all 190 unabridged runner lines, including all
  94 RUN lines with claim associations, all 94 PASS lines, and start/final totals.
logs/: eight complete original local logs plus both hosted job logs; no
  certificate output was discarded. The two hosted copies remove trailing
  spaces/tabs and the final blank line; all entries and timestamps remain.
receipts/certificates.json, repository.json, budget.json: portable JSON copies.
  Each log path is relative to its receipt file. Original absolute log paths,
  exact commands, candidate identities and recorded results are preserved.
receipts/original/: byte-for-byte source receipts. Absolute paths in these
  originals are explicitly historical local paths, not required live locations.
profile-boundary-review.txt: independent three-file static review and limits.
SHA256SUMS.txt: hashes of every other file in this bundle.

Complete certificate-log SHA256:
  2e4253031eee25f14b8db14e8e3ffefc0e60b3d03f43850df9a6c027f47fc281
Complete certificate-log bytes: 530174

Reproduction (commands below have NOT been rerun for this bundle)
----------------------------------------------------------------
Use a separate checkout; select the public commit for the relevant evidence.
The recorded runtime is CPython 3.14.7 on Linux x86_64. Dependency versions,
platform, budgets, original interpreter paths and exact argument vectors are
preserved in the JSON receipts. Install the full pinned verification lock:

  python3.14 -m venv /tmp/e99-receipt-reproduction
  /tmp/e99-receipt-reproduction/bin/python -m pip install --require-hashes --only-binary=:all: -r tools/requirements-verification-linux-x86_64.lock

On public commit c5911c89e0407e43d6ad637dc2620971b7d157b4:

  /tmp/e99-receipt-reproduction/bin/python tools/run_theorem_certificates.py
  /tmp/e99-receipt-reproduction/bin/python tools/check_public.py
  /tmp/e99-receipt-reproduction/bin/python tools/ci_integrity.py --root . --base-ref e396ea07887dd0528b817ce4e656ff0e6b01f8fb
  /tmp/e99-receipt-reproduction/bin/python -m unittest tools.test_task_selector tools.test_agent_workflow tools.test_local_ci tools.test_ci_integrity -q
  /tmp/e99-receipt-reproduction/bin/python scripts/research_package.py --package research-packages/target-a-fan-tube-ledger --check-only
  /tmp/e99-receipt-reproduction/bin/python tools/local_ci.py --base-ref e396ea07887dd0528b817ce4e656ff0e6b01f8fb --output /tmp/e99-reproduced-plan

The historical plan command used origin/main. Its recorded output resolves that
name to the exact base above; use the immutable SHA for later reproduction.

On public commit 2c38f9f0c5925bad5dd8f953ef912edf7aafe91a:

  /tmp/e99-receipt-reproduction/bin/python tools/ci_integrity.py --root . --base-ref e396ea07887dd0528b817ce4e656ff0e6b01f8fb
  /tmp/e99-receipt-reproduction/bin/python -m unittest tools.test_local_ci -q

The 180-second integrity limit was enforced by the recorded verification runner;
its command alone does not recreate the outer wall-time enforcement. Hosted
namespace checks require the actual supported Bubblewrap/AppArmor environment;
retain any skips as skips. Use original JSON records for the exact historical
commands and receipt budgets.

To verify the copied bundle's bytes (not the repository's mathematics):

  sha256sum --check SHA256SUMS.txt

Post-integration hosted verification
------------------------------------
The pull request publishing this bundle records its own hosted run ID, tested
head, trusted base and final outcome in its body. PR99 links that receipt PR:
https://github.com/1337isnot1337/erdos-99/pull/99
The run occurs after this evidence commit; no future pass is claimed here.
Optional package replay remains separately opt-in and is not inferred from a
structural job. Historical local namespace skips remain skips.
