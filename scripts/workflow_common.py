"""Non-executing helpers shared by research coordination commands."""
from __future__ import annotations

import datetime as dt
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile

REPOSITORY = "1337isnot1337/erdos-99"
ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r"[0-9a-f]{40}")


def now():
    return dt.datetime.now(dt.timezone.utc)


def timestamp():
    return now().isoformat()


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True,
                                   stderr=subprocess.PIPE, timeout=60).strip()


def gh(*args):
    return json.loads(subprocess.check_output(["gh", "api", *args], text=True,
                                              stderr=subprocess.PIPE, timeout=60))


def pages(endpoint):
    return [row for page in gh("--paginate", "--slurp", endpoint) for row in page]


def graphql(query, **variables):
    args = ["graphql", "-f", "query=" + query]
    for key, value in variables.items():
        if value is not None:
            args += ["-f", f"{key}={value}"]
    result = gh(*args)
    if result.get("errors"):
        raise ValueError("GitHub GraphQL query returned errors")
    return result["data"]


def repo_path(value):
    if (not isinstance(value, str) or not value or value.startswith(("/", "-"))
            or "\\" in value or "\x00" in value
            or any(part in ("", ".", "..") for part in value.split("/"))):
        raise ValueError(f"expected a repository-relative path: {value!r}")
    return PurePosixPath(value).as_posix()


def regular_file(root, value):
    value = repo_path(value)
    root = Path(root).resolve()
    candidate = root / value
    cursor = candidate
    while cursor != root:
        if cursor.is_symlink():
            raise ValueError(f"symlink is not a regular source: {value}")
        cursor = cursor.parent
    if not candidate.is_file():
        raise ValueError(f"missing regular source: {value}")
    return candidate


def atomic_json(path, value):
    path = Path(path)
    if path.is_symlink():
        raise ValueError("refusing to replace a symlink")
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix="." + path.name, dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
