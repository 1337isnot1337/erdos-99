#!/usr/bin/env python3
"""Create a LOCAL clean-root copy of an immutable candidate, without publishing.

The new repository has an identical Git tree, one synthetic snapshot commit,
no remote, no alternate object store and no inherited refs, messages or objects.
This removes inherited Git metadata, not sensitive content or rights obligations.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile


def git(root: Path, *args: str, input: bytes | None = None, env=None) -> bytes:
    return subprocess.check_output(
        ["git", "--no-replace-objects", "-C", str(root), *args],
        input=input, env=env, stderr=subprocess.PIPE, timeout=120,
    )


def valid_path(path: str) -> bool:
    return bool(path) and not path.startswith(("/", "-")) and "\\" not in path and all(
        x not in ("", ".", "..") and x.casefold() != ".git" for x in path.split("/")
    ) and PurePosixPath(path).as_posix() == path


def prepare(source: Path, destination: Path, ref: str = "HEAD") -> dict:
    source, destination = source.resolve(), destination.absolute()
    if destination.exists() or destination.is_symlink():
        raise ValueError("destination already exists; refusing overwrite")
    if not destination.parent.is_dir():
        raise ValueError("destination parent must already exist")
    if ref.startswith("-"):
        raise ValueError("invalid ref")
    candidate = git(source, "rev-parse", "--verify", ref + "^{commit}").decode().strip()
    if not re.fullmatch(r"[0-9a-f]{40}", candidate):
        raise ValueError("only SHA-1 Git object format is currently supported")
    tree = git(source, "rev-parse", candidate + "^{tree}").decode().strip()
    records = []
    for item in git(source, "ls-tree", "-rz", candidate).split(b"\0"):
        if not item:
            continue
        meta, raw_path = item.split(b"\t", 1)
        mode, kind, blob = meta.decode().split()
        path = raw_path.decode("utf-8")
        if mode not in ("100644", "100755") or kind != "blob" or not valid_path(path):
            raise ValueError("unsafe path or special Git object in candidate")
        records.append((mode, blob, path))
    # Build in a private sibling and expose only the completed, checked result.
    # An empty template disables inherited template hooks. Controlled Git config
    # disables global filters, signing and hooks without touching user settings.
    env = os.environ.copy()
    for key in list(env):
        if key.startswith("GIT_"):
            env.pop(key)
    env.update({"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull})
    date = git(source, "show", "-s", "--format=%cI", candidate).decode().strip()
    env.update({"GIT_AUTHOR_NAME": "E99 snapshot automation",
                "GIT_COMMITTER_NAME": "E99 snapshot automation",
                "GIT_AUTHOR_EMAIL": "publication@example.invalid",
                "GIT_COMMITTER_EMAIL": "publication@example.invalid",
                "GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date})
    with tempfile.TemporaryDirectory(prefix=".e99-clean-", dir=destination.parent) as temporary:
        target = Path(temporary) / "snapshot"
        target.mkdir(mode=0o700)
        git(target, "-c", "core.hooksPath=/dev/null", "init", "-q", "--template=", "-b", "main", env=env)
        for mode, blob, path in records:
            output = target / path
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(git(source, "cat-file", "blob", blob))
            output.chmod(0o755 if mode == "100755" else 0o644)
        # hash-object --no-filters and a temporary index avoid .gitattributes,
        # line-ending conversion or user clean filters changing the source tree.
        index_lines = bytearray()
        for mode, blob, path in records:
            written = git(target, "hash-object", "-w", "--no-filters", "--", path, env=env).decode().strip()
            if written != blob:
                raise ValueError("copied blob changed")
            index_lines.extend(f"{mode} {blob}\t{path}".encode() + b"\0")
        git(target, "update-index", "-z", "--index-info", input=bytes(index_lines), env=env)
        if git(target, "write-tree", env=env).decode().strip() != tree:
            raise ValueError("export tree differs from immutable candidate")
        message = ("Curated E99 publication snapshot\n\n"
                   "Synthetic export metadata; mathematical credit remains in NOTICE and source files.\n"
                   f"Prepared from candidate {candidate}.\n")
        clean = git(target, "-c", "commit.gpgSign=false", "commit-tree", tree, input=message.encode(), env=env).decode().strip()
        git(target, "update-ref", "refs/heads/main", clean, env=env)
        git(target, "reset", "--mixed", "-q", clean, env=env)
        if git(target, "status", "--porcelain", env=env):
            raise ValueError("export worktree differs from committed tree")
        if git(target, "rev-list", "--all", "--count", env=env).strip() != b"1":
            raise ValueError("export unexpectedly contains inherited history")
        if git(target, "remote", env=env).strip() or (target / ".git/objects/info/alternates").exists():
            raise ValueError("export unexpectedly references another object store")
        # Unreachable parent objects must be absent too, not merely hidden by refs.
        all_objects = git(target, "cat-file", "--batch-all-objects", "--batch-check=%(objecttype)", env=env).splitlines()
        if all_objects.count(b"commit") != 1 or b"tag" in all_objects:
            raise ValueError("export contains extra commit/tag objects")
        git(target, "fsck", "--strict", "--full", "--no-reflogs", env=env)
        if destination.exists() or destination.is_symlink():
            raise ValueError("destination appeared during preparation; refusing overwrite")
        target.rename(destination)
    return {"status": "LOCAL_PRIVACY_PREPARATION_ONLY", "source_candidate": candidate,
            "clean_candidate": clean, "identical_tree": tree, "files": len(records),
            "reachable_commits": 1, "all_commit_objects": 1, "remotes": [],
            "synthetic_identity": "E99 snapshot automation <publication@example.invalid>",
            "limits": ["No rights clearance or content-security clearance is granted.",
                       "No remote was created, changed, rewritten or published.",
                       "Existing staging GitHub refs and retained objects remain private-only."]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--ref", default="HEAD")
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = prepare(args.source, args.destination, args.ref)
    except (ValueError, UnicodeError, OSError, subprocess.SubprocessError) as error:
        print(json.dumps({"status": "FAILED", "error_type": type(error).__name__}))
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
