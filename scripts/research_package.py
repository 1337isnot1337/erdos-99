#!/usr/bin/env python3
"""Check working-tree package metadata and source pins, without executing its commands."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.workflow_common import git, regular_file
from tools.localized_ci.packages import Invalid, MAX_BLOB, load_package


class WorkingSnapshot:
    def __init__(self, root):
        self.root = root
        paths = git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard").split("\0")
        self.tree = {path: None for path in paths if path}

    def regular(self, path):
        if path not in self.tree:
            raise Invalid("input is ignored or absent from the working-tree inventory: " + path)
        regular_file(self.root, path)

    def read(self, path):
        self.regular(path)
        source = regular_file(self.root, path)
        if source.stat().st_size > MAX_BLOB:
            raise Invalid("input exceeds the existing replay blob limit")
        return source.read_bytes()

    def ancestor(self, commit):
        result = subprocess.run(["git", "-C", str(self.root), "merge-base", "--is-ancestor", commit, "HEAD"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        return result.returncode == 0

    def read_at(self, commit, path):
        return subprocess.check_output(["git", "-C", str(self.root), "show", f"{commit}:{path}"],
                                       stderr=subprocess.PIPE, timeout=60)


def check(root, package):
    if not package.startswith("research-packages/") or len(package.split("/")) != 2:
        raise ValueError("expected research-packages/PACKAGE")
    result = load_package(WorkingSnapshot(root), package)
    return dict(status="metadata-valid", package=package,
                classification=result["task"]["classification"], unresolved=result["unresolved"],
                declared_seconds=result["seconds"],
                declared_package_dependencies=sorted(result["dependencies"]),
                full_verified=False, replay_authorized=False, executed_commands=False,
                limits="Metadata and source-pin check only; no replay or mathematical approval. The Git-blob planner and isolated backend remain authoritative for replay.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True)
    parser.add_argument("--check-only", action="store_true", help="explicit metadata-only mode (also the default)")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(check(args.root, args.package), indent=2))
    except (OSError, ValueError, Invalid, subprocess.SubprocessError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
