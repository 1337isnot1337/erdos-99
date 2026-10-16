#!/usr/bin/env python3
"""Run inspected Agent 3 verifiers and retain exact stdout/receipts."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--dirty-source-root", type=Path, required=True)
    ap.add_argument("--external-fixture-dir", type=Path, required=True,
                    help="locally held Packomania cci132/cci175 files; not copied into the destination")
    ap.add_argument("--evidence-dir", type=Path, required=True)
    ap.add_argument("--timeout", type=int, default=240)
    args = ap.parse_args()
    repo = args.repo.resolve()
    dirty = args.dirty_source_root.resolve()
    external = args.external_fixture_dir.resolve()
    evidence = args.evidence_dir.resolve()
    evidence.mkdir(parents=True, exist_ok=True)

    if not all((external / f"cci{n}.txt").is_file() for n in (132, 175)):
        raise SystemExit("external fixture directory must contain cci132.txt and cci175.txt")
    expected = {"132": "64c8a85573a5ced26e666fa25b713c4fc6264c409d811eab101cd13ff65ef00a",
                "175": "6f889e1143dbb5aee039224198617355070104f161a2bdd0705166eaf814f140"}
    input_hashes = {str(n): sha((external / f"cci{n}.txt").read_bytes()) for n in (132, 175)}
    if input_hashes != expected:
        raise SystemExit(f"external fixture hash mismatch: actual={input_hashes!r} expected={expected!r}")

    commands = [
        ("pr966_seed066_locked_fullrank", repo / "research/verify_target_a_seed066_locked_fullrank.py", [], repo),
        ("pr967_cartesian_certificate", repo / "research/check_seed054_cartesian_certificate.py", [], repo),
        ("pr967_rhombus_mesh", repo / "research/verify_seed054_rhombus_mesh.py", [], repo),
        ("pr969_seed063_tight_isolates", repo / "research/verify_target_a_seed063_tight_isolates.py", [], repo),
        ("branch_global_attainment", repo / "research/verify_global_attainment_infimum.py", [], repo),
        ("branch_global_isolate_forest", repo / "research/verify_global_isolate_forest_normalization.py", [], repo),
        ("branch_periodic_release", repo / "research/verify_periodic_release_diameter_transfer.py", [], repo),
        ("branch_target_c_cap_crop_suffix", repo / "research/verify_target_c_cap_crop_return_suffix_2026_10_08.py", [], repo),
        ("destination_global_palette_with_dirty_hybrid_fixture",
         repo / "research/verify_global_palette_transversal_2026_10_12.py",
         ["--fixture-dir", str(external)], repo),
        ("dirty_global_palette_worktree_snapshot",
         dirty / "research/verify_global_palette_transversal_2026_10_12.py", [], dirty),
    ]

    def git_status(root: Path) -> str:
        result = subprocess.run(["git", "-C", str(root), "status", "--porcelain=v1", "-z"],
                                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode("utf-8", "surrogateescape")

    before_dirty_status = git_status(dirty)
    records = []
    for name, script, extra, cwd in commands:
        if not script.is_file():
            records.append({"name": name, "status": "not_run_missing_script", "script": str(script)})
            continue
        command = [sys.executable, "-B", str(script), *extra]
        started = time.monotonic()
        try:
            proc = subprocess.run(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                  timeout=args.timeout, check=False)
            rc = proc.returncode
            output = proc.stdout
            status = "pass" if rc == 0 else "fail"
        except subprocess.TimeoutExpired as exc:
            rc = None
            output = (exc.stdout or b"") + b"\n[TIMEOUT]\n" + (exc.stderr or b"")
            status = "timeout"
        elapsed = time.monotonic() - started
        logfile = evidence / f"{name}.log"
        logfile.write_bytes(output)
        records.append({"name": name, "status": status, "returncode": rc,
                        "command": command, "cwd": str(cwd), "script_sha256": sha(script.read_bytes()),
                        "stdout_sha256": sha(output), "stdout_bytes": len(output),
                        "elapsed_seconds": round(elapsed, 3),
                        "log_path": str(logfile.relative_to(repo)),
                        "output_tail": output.decode("utf-8", "replace")[-2400:]})

    after_dirty_status = git_status(dirty)
    records.append({"name": "source_dirty_worktree_integrity", "status":
                    "pass_unchanged" if before_dirty_status == after_dirty_status else "fail_changed",
                    "porcelain_sha256_before": sha(before_dirty_status.encode("utf-8", "surrogateescape")),
                    "porcelain_sha256_after": sha(after_dirty_status.encode("utf-8", "surrogateescape")),
                    "porcelain_entry_count": before_dirty_status.count("\0")})
    receipt = {"python": sys.version, "external_fixture_hashes": input_hashes,
               "commands_timeout_seconds": args.timeout, "results": records}
    path = evidence / "verifier-results.json"
    path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"receipt": str(path.relative_to(repo)),
                      "status_counts": {s: sum(r.get("status") == s for r in records)
                                        for s in sorted({r.get("status") for r in records})},
                      "results": [{"name": r["name"], "status": r.get("status"),
                                   "returncode": r.get("returncode"),
                                   "elapsed_seconds": r.get("elapsed_seconds"),
                                   "output_tail": r.get("output_tail", "")[-600:]}
                                  for r in records]}, indent=2, sort_keys=True))
    return 0 if all(r.get("status") in ("pass", "pass_unchanged") for r in records) else 1


if __name__ == "__main__":
    raise SystemExit(main())
