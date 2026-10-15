#!/usr/bin/env python3
"""Validate the repository's theorem-state control layer.

This checker does not prove mathematics. It makes theorem-state corruption hard to
introduce accidentally by validating a strict manifest schema, lifecycle graph,
artifact registry, generated views, active routes/prompts, and PR promotion transaction.
"""

from __future__ import annotations

import argparse
import copy
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

import yaml
from jsonschema import Draft202012Validator

MANIFEST = "docs/state/theorem-state.yaml"
SCHEMA = "docs/state/theorem-state.schema.json"
ARTIFACT_INDEXER = "tools/build_artifact_index.py"
VIEW_GENERATOR = "tools/generate_theorem_state_views.py"
ENTRY_BUCKETS = (
    "current_canonical_entries",
    "audited_working",
    "regressions",
    "rejected_or_overridden",
)
EDGE_FIELDS = ("depends_on", "invalidates", "supersedes")
BASE_REQUIRED = {
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    ".github/copilot-instructions.md",
    ".github/workflows/theorem-state.yml",
    "docs/STATE.md",
    MANIFEST,
    SCHEMA,
    "docs/state/README.md",
    "docs/README.md",
    "docs/KNOWLEDGE_MAP.md",
    "docs/RESEARCH_WORKFLOW.md",
    "docs/reports/README.md",
    "docs/reports/REPORT_TEMPLATE.md",
    "docs/prompts/README.md",
    ARTIFACT_INDEXER,
    VIEW_GENERATOR,
    "tools/run_theorem_certificates.py",
}
OPERATIONAL = BASE_REQUIRED - {
    MANIFEST,
    SCHEMA,
    ".github/workflows/theorem-state.yml",
    ARTIFACT_INDEXER,
    VIEW_GENERATOR,
    "tools/run_theorem_certificates.py",
}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
SECTION_RE = re.compile(r"\bSections?\s+(\d+)(?:\s*[-–—]\s*(\d+))?", re.I)
CURRENT_SECTION_RE = re.compile(
    r"\b(?:currently\s+runs\s+through|canonical\s+development(?:\s+runs)?\s+through|"
    r"current\s+route(?:\s+runs)?\s+through)\s+Section\s+(\d+)\b",
    re.I,
)
LEVEL_RE = re.compile(r"\bLEVEL\s+I\s+STATUS\s*:\s*(?:STILL\s+)?(OPEN|CLOSED|SOLVED)\b", re.I)
FORBIDDEN_ACTIVE = (
    re.compile(r"\bC-I\s+remains\s+open\b", re.I),
    re.compile(r"\blive endpoint is the source-labeled planar Menger lemma\b", re.I),
    re.compile(r"\bcurrently runs through Section 167\b", re.I),
)


class Checker:
    def __init__(self, root: Path, base_ref: str | None = None):
        self.root = root.resolve()
        self.base_ref = base_ref
        self.errors: list[str] = []
        self.state: dict[str, Any] = {}

    def err(self, message: str) -> None:
        self.errors.append(message)

    def file(self, rel: str) -> Path:
        return self.root / rel

    def read(self, rel: str) -> str:
        try:
            return self.file(rel).read_text(encoding="utf-8")
        except FileNotFoundError:
            self.err(f"missing required file: {rel}")
        except UnicodeDecodeError:
            self.err(f"expected UTF-8 text file: {rel}")
        return ""

    def load(self) -> None:
        try:
            data = yaml.safe_load(self.file(MANIFEST).read_text(encoding="utf-8"))
        except FileNotFoundError:
            self.err(f"missing required state file: {MANIFEST}")
            return
        except yaml.YAMLError as exc:
            self.err(f"invalid YAML in {MANIFEST}: {exc}")
            return
        if not isinstance(data, dict):
            self.err(f"{MANIFEST} must contain a top-level mapping")
            return
        self.state = data

    def validate_schema(self) -> None:
        if not self.state:
            return
        try:
            import json

            schema = json.loads(self.file(SCHEMA).read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            self.err(f"cannot load strict schema {SCHEMA}: {exc}")
            return
        validator = Draft202012Validator(schema)
        for failure in sorted(validator.iter_errors(self.state), key=lambda e: list(e.absolute_path)):
            where = ".".join(map(str, failure.absolute_path)) or "<root>"
            self.err(f"schema: {where}: {failure.message}")

    def entries(self) -> Iterable[tuple[str, str, dict[str, Any]]]:
        targets = self.state.get("targets", {})
        if not isinstance(targets, dict):
            return
        for target_name, target in targets.items():
            if not isinstance(target, dict):
                continue
            for bucket in ENTRY_BUCKETS:
                rows = target.get(bucket, []) or []
                if not isinstance(rows, list):
                    continue
                for entry in rows:
                    if isinstance(entry, dict):
                        yield target_name, bucket, entry

    def entry_map(self) -> dict[str, tuple[str, str, dict[str, Any]]]:
        out: dict[str, tuple[str, str, dict[str, Any]]] = {}
        for target, bucket, entry in self.entries():
            ident = entry.get("id")
            if not isinstance(ident, str) or not ident:
                continue
            if ident in out:
                old_target, old_bucket, _ = out[ident]
                self.err(
                    f"duplicate theorem-state id {ident!r}: "
                    f"targets.{old_target}.{old_bucket} and targets.{target}.{bucket}"
                )
            else:
                out[ident] = (target, bucket, entry)
        return out

    def check_bucket_statuses(self) -> None:
        expected = {
            "current_canonical_entries": {"canonical"},
            "audited_working": {"audited-working"},
            "regressions": {"regression"},
            "rejected_or_overridden": {"rejected", "regression", "superseded"},
        }
        for target, bucket, entry in self.entries():
            status = entry.get("status")
            if status not in expected[bucket]:
                self.err(
                    f"targets.{target}.{bucket} entry {entry.get('id', '<missing-id>')} "
                    f"has status {status!r}; expected one of {sorted(expected[bucket])}"
                )

    @staticmethod
    def safe_rel(value: str) -> str | None:
        p = PurePosixPath(value)
        if p.is_absolute() or ".." in p.parts or value.startswith("./"):
            return None
        return p.as_posix()

    def registered_paths(self) -> set[str]:
        paths = set(BASE_REQUIRED)
        generated = self.state.get("generated_views", {})
        if isinstance(generated, dict):
            paths.update(x for x in generated.values() if isinstance(x, str))
        artifact_policy = self.state.get("artifact_policy", {})
        if isinstance(artifact_policy, dict) and isinstance(artifact_policy.get("index"), str):
            paths.add(artifact_policy["index"])

        for target in self.state.get("targets", {}).values():
            if not isinstance(target, dict):
                continue
            for key in ("route_map", "active_prompt", "current_frontier", "promoted_catalog_snapshot"):
                if isinstance(target.get(key), str):
                    paths.add(target[key])
            paths.update(x for x in target.get("canonical_modules", []) or [] if isinstance(x, str))

        for _, _, entry in self.entries():
            for key in ("report", "audit"):
                if isinstance(entry.get(key), str):
                    paths.add(entry[key])
            paths.update(x for x in entry.get("certificates", []) or [] if isinstance(x, str))

        active = self.state.get("active_prompts", {})
        if isinstance(active, dict):
            paths.update(x for x in active.values() if isinstance(x, str))
        paths.update(
            x
            for x in self.state.get("historical_prompt_compatibility_paths", []) or []
            if isinstance(x, str)
        )
        return paths

    def check_paths(self) -> None:
        for raw in sorted(self.registered_paths()):
            rel = self.safe_rel(raw)
            if rel is None:
                self.err(f"manifest path is not a safe repository-relative path: {raw!r}")
            elif not self.file(rel).is_file():
                self.err(f"registered theorem-state path does not exist: {rel}")

    def check_graph(self) -> None:
        nodes = self.entry_map()
        if not nodes:
            return
        policy = self.state.get("graph_policy", {})
        require_resolved = bool(policy.get("require_resolved_edges", True)) if isinstance(policy, dict) else True
        allowed_canonical = set(policy.get("canonical_dependency_statuses", ["canonical"])) if isinstance(policy, dict) else {"canonical"}

        for ident, (_, _, entry) in nodes.items():
            for field in EDGE_FIELDS:
                for target in entry.get(field, []) or []:
                    if require_resolved and target not in nodes:
                        self.err(f"graph edge {ident}.{field} references unknown theorem id {target!r}")
            if entry.get("status") == "canonical":
                for dependency in entry.get("depends_on", []) or []:
                    if dependency not in nodes:
                        continue
                    dep_status = nodes[dependency][2].get("status")
                    if dep_status not in allowed_canonical:
                        self.err(
                            f"canonical theorem {ident} depends on {dependency} with forbidden status {dep_status!r}"
                        )

        if isinstance(policy, dict) and policy.get("require_acyclic_depends_on"):
            visiting: set[str] = set()
            visited: set[str] = set()

            def visit(node: str, trail: list[str]) -> None:
                if node in visited:
                    return
                if node in visiting:
                    cycle = trail[trail.index(node):] + [node]
                    self.err("depends_on cycle: " + " -> ".join(cycle))
                    return
                visiting.add(node)
                trail.append(node)
                for dep in nodes[node][2].get("depends_on", []) or []:
                    if dep in nodes:
                        visit(dep, trail)
                trail.pop()
                visiting.remove(node)
                visited.add(node)

            for ident in sorted(nodes):
                visit(ident, [])

    @staticmethod
    def plain(text: str) -> str:
        return " ".join(text.replace("*", "").replace("`", "").split())

    @staticmethod
    def math(text: str) -> str:
        for old, new in {
            r"\operatorname{rank}": "rank",
            r"\Delta": "Delta",
            r"\partial": "partial",
            r"\Lambda": "Lambda",
            r"\le": "<=",
            r"\ge": ">=",
            r"\sqrt": "sqrt",
            r"\over": "/",
            r"\rm": "",
            r"\qquad": "",
            r"\text": "",
        }.items():
            text = text.replace(old, new)
        return re.sub(r"[\\{}()$`*\s,]", "", text)

    def endpoint(self, expected: str, text: str, where: str) -> None:
        hay = self.math(text)
        for clause in re.split(r"\s*,?\s*equivalently\s+", expected, flags=re.I):
            if self.math(clause) not in hay:
                self.err(f"{where} does not contain manifest endpoint clause: {clause!r}")

    @staticmethod
    def sections(text: str) -> list[int]:
        out: list[int] = []
        for match in SECTION_RE.finditer(text):
            out.append(int(match.group(1)))
            if match.group(2):
                out.append(int(match.group(2)))
        return out

    @staticmethod
    def gate(text: str, name: str) -> set[str]:
        text = Checker.plain(text)
        found: set[str] = set()
        for pattern in (
            rf"\b{re.escape(name)}\b\s*:\s*(OPEN|CLOSED)\b",
            rf"\b{re.escape(name)}\b\s+(?:IS|REMAINS)\s+(OPEN|CLOSED)\b",
            rf"\b{re.escape(name)}\b\s+(OPEN|CLOSED)\b",
        ):
            found.update(m.group(1).lower() for m in re.finditer(pattern, text, re.I))
        return found

    def operational_docs(self) -> set[str]:
        docs = set(OPERATIONAL)
        for target in self.state.get("targets", {}).values():
            if isinstance(target, dict):
                docs.update(
                    target[key]
                    for key in ("route_map", "current_frontier", "active_prompt")
                    if isinstance(target.get(key), str)
                )
        active = self.state.get("active_prompts", {})
        if isinstance(active, dict):
            docs.update(x for x in active.values() if isinstance(x, str))
        docs.update(
            x
            for x in self.state.get("historical_prompt_compatibility_paths", []) or []
            if isinstance(x, str)
        )
        return docs

    def check_level(self) -> None:
        expected = str(self.state.get("level_i_status", "")).lower()
        for rel in sorted(self.operational_docs()):
            if not self.file(rel).is_file():
                continue
            for match in LEVEL_RE.finditer(self.plain(self.read(rel))):
                actual = "closed" if match.group(1).lower() in {"closed", "solved"} else "open"
                if actual != expected:
                    self.err(f"{rel} declares LEVEL I {actual}, but manifest says {expected}")

    def check_stale_phrases(self) -> None:
        for rel in sorted(self.operational_docs()):
            if not self.file(rel).is_file():
                continue
            text = self.plain(self.read(rel))
            for pattern in FORBIDDEN_ACTIVE:
                match = pattern.search(text)
                if match:
                    self.err(f"stale active-state phrase in {rel}: {match.group(0)!r}")

    def check_a(self) -> None:
        a = self.state.get("targets", {}).get("target-a", {})
        if not isinstance(a, dict) or not isinstance(a.get("canonical_sections_through"), int):
            return
        section_number = a["canonical_sections_through"]
        for rel in (a.get("route_map"), a.get("active_prompt")):
            if not isinstance(rel, str):
                continue
            text = self.read(rel)
            nums = self.sections(text)
            if section_number not in nums:
                self.err(f"{rel} does not expose canonical Section {section_number}")
            elif max(nums) != section_number:
                self.err(f"{rel} reaches Section {max(nums)}, but manifest says {section_number}")
            endpoint = a.get("global_endpoint")
            if isinstance(endpoint, str):
                self.endpoint(endpoint, text, rel)
            locked = a.get("locked_branch_endpoint")
            if isinstance(locked, str):
                locked_core = re.sub(r"\s+in\s+Section\s+\d+\s*$", "", locked, flags=re.I)
                locked_clause = locked_core.split(":", 1)[1].strip() if ":" in locked_core else locked_core
                self.endpoint(locked_clause, text, rel)
        for rel in sorted(self.operational_docs()):
            if not self.file(rel).is_file():
                continue
            for match in CURRENT_SECTION_RE.finditer(self.plain(self.read(rel))):
                if int(match.group(1)) != section_number:
                    self.err(
                        f"stale Target A current-section claim in {rel}: "
                        f"Section {match.group(1)}; manifest says {section_number}"
                    )

    def check_b(self) -> None:
        b = self.state.get("targets", {}).get("target-b", {})
        if not isinstance(b, dict):
            return
        route = b.get("route_map")
        endpoint = b.get("global_endpoint")
        if isinstance(route, str) and isinstance(endpoint, str):
            self.endpoint(endpoint, self.read(route), route)
            self.endpoint(endpoint, self.read("docs/STATE.md"), "docs/STATE.md")

    def section(self, text: str, heading: str) -> str:
        headings = list(HEADING_RE.finditer(text))
        for index, current in enumerate(headings):
            if self.plain(current.group(2)).lower() != heading.lower():
                continue
            end = len(text)
            for later in headings[index + 1:]:
                if len(later.group(1)) <= len(current.group(1)):
                    end = later.start()
                    break
            return text[current.end():end]
        return ""

    def resolve(self, source: str, raw: str) -> str | None:
        target = raw.split("#", 1)[0].strip().strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:")):
            return None
        parts: list[str] = []
        for part in PurePosixPath(PurePosixPath(source).parent, target).parts:
            if part in ("", "."):
                continue
            if part == "..":
                if not parts:
                    return "__ESCAPES__"
                parts.pop()
            else:
                parts.append(part)
        return PurePosixPath(*parts).as_posix()

    def links(self, source: str, text: str) -> set[str]:
        out: set[str] = set()
        for raw in LINK_RE.findall(text):
            resolved = self.resolve(source, raw)
            if resolved not in {None, "__ESCAPES__"}:
                out.add(resolved)
        return out

    def check_c(self) -> None:
        c = self.state.get("targets", {}).get("target-c", {})
        if not isinstance(c, dict):
            return
        route, current, prompt = c.get("route_map"), c.get("current_frontier"), c.get("active_prompt")
        if not all(isinstance(x, str) for x in (route, current, prompt)):
            return
        assert isinstance(route, str) and isinstance(current, str) and isinstance(prompt, str)

        for key, label in (("c_i", "C-I"), ("c_ii", "C-II")):
            expected = c.get(key)
            if expected not in {"open", "closed"}:
                continue
            for rel in ("docs/STATE.md", route, current, prompt):
                statuses = self.gate(self.read(rel), label)
                if expected not in statuses:
                    self.err(f"{rel} does not explicitly declare {label} {expected}")
                if ({"open", "closed"} - {expected}) & statuses:
                    self.err(f"{rel} contains contradictory {label} status: {sorted(statuses)}")

        route_text = self.read(route)
        order = self.section(route_text, "Canonical reading order")
        if not order:
            self.err(f"{route} missing 'Canonical reading order' section")
        else:
            actual = {
                path
                for path in self.links(route, order)
                if path.startswith("docs/targets/target-c/") and path.endswith(".md")
            }
            expected = set(c.get("canonical_modules", []) or [])
            if actual != expected:
                if expected - actual:
                    self.err(
                        f"{route} canonical reading order omits manifest modules: "
                        + ", ".join(sorted(expected - actual))
                    )
                if actual - expected:
                    self.err(
                        f"{route} canonical reading order has unregistered modules: "
                        + ", ".join(sorted(actual - expected))
                    )

        route_links = self.links(route, route_text)
        for entry in c.get("current_canonical_entries", []) or []:
            if not isinstance(entry, dict):
                continue
            for key in ("report", "audit"):
                path = entry.get(key)
                if isinstance(path, str) and path not in route_links:
                    self.err(
                        f"canonical {entry.get('id', '<missing-id>')} {key} "
                        f"is not linked from {route}: {path}"
                    )

    def check_prompts(self) -> None:
        source = "docs/prompts/README.md"
        text = self.read(source)
        active = self.state.get("active_prompts", {})
        if not isinstance(active, dict):
            return
        expected = {x for x in active.values() if isinstance(x, str)}
        current = self.section(text, "Current prompts")
        if not current:
            self.err(f"{source} missing 'Current prompts' section")
        else:
            actual = {
                path
                for path in self.links(source, current)
                if path.startswith("docs/prompts/") and path.endswith(".md")
            }
            if actual != expected:
                if expected - actual:
                    self.err(f"{source} omits current manifest prompts: {', '.join(sorted(expected-actual))}")
                if actual - expected:
                    self.err(f"{source} marks unregistered prompts current: {', '.join(sorted(actual-expected))}")

        compatibility_expected = set(self.state.get("historical_prompt_compatibility_paths", []) or [])
        compatibility = self.section(text, "Compatibility paths")
        if not compatibility:
            self.err(f"{source} missing 'Compatibility paths' section")
        else:
            actual = {
                path
                for path in self.links(source, compatibility)
                if path.startswith("docs/prompts/") and path.endswith(".md")
            }
            if actual != compatibility_expected:
                if compatibility_expected - actual:
                    self.err(
                        f"{source} omits compatibility paths: "
                        + ", ".join(sorted(compatibility_expected - actual))
                    )
                if actual - compatibility_expected:
                    self.err(
                        f"{source} has unregistered compatibility paths: "
                        + ", ".join(sorted(actual - compatibility_expected))
                    )

        for rel in sorted(compatibility_expected):
            if not self.file(rel).is_file():
                continue
            first = "\n".join(self.read(rel).splitlines()[:8]).upper()
            if "HISTORICAL" not in first or "SUPERSEDED" not in first:
                self.err(f"legacy prompt path is not an explicit historical/superseded pointer: {rel}")
            if not (self.links(rel, self.read(rel)) & expected):
                self.err(f"legacy prompt path does not point to any current prompt: {rel}")

    def check_relative_links(self) -> None:
        checked = self.operational_docs() | set(self.state.get("generated_views", {}).values())
        for rel in sorted(x for x in checked if isinstance(x, str)):
            if not self.file(rel).is_file():
                continue
            for raw in LINK_RE.findall(self.read(rel)):
                resolved = self.resolve(rel, raw)
                if resolved is None:
                    continue
                if resolved == "__ESCAPES__":
                    self.err(f"relative link escapes repository in {rel}: {raw}")
                elif not self.file(resolved).exists():
                    self.err(f"broken relative link in {rel}: {raw} -> {resolved}")

    def run_subcheck(self, script: str) -> None:
        proc = subprocess.run(
            [sys.executable, script, "--root", str(self.root)],
            cwd=self.root,
            text=True,
            capture_output=True,
        )
        if proc.returncode:
            output = "\n".join(line for line in (proc.stdout + proc.stderr).splitlines() if line.strip())
            self.err(f"{script} failed:\n{output}")

    @staticmethod
    def semantic_state(state: dict[str, Any]) -> dict[str, Any]:
        out = copy.deepcopy(state)
        out.pop("state_version", None)
        out.pop("state_date", None)
        return out

    def git(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", "--no-replace-objects", *args],
            cwd=self.root,
            text=True,
            capture_output=True,
        )

    def changed_files(self) -> set[str] | None:
        if not self.base_ref:
            return None
        proc = self.git("diff", "--name-only", f"{self.base_ref}...HEAD")
        if proc.returncode:
            self.err(f"cannot diff promotion transaction against {self.base_ref}: {proc.stderr.strip()}")
            return None
        return {line.strip() for line in proc.stdout.splitlines() if line.strip()}

    def base_state(self) -> dict[str, Any] | None:
        if not self.base_ref:
            return None
        proc = self.git("show", f"{self.base_ref}:{MANIFEST}")
        if proc.returncode:
            self.err(f"cannot read base theorem state from {self.base_ref}: {proc.stderr.strip()}")
            return None
        try:
            data = yaml.safe_load(proc.stdout)
        except yaml.YAMLError as exc:
            self.err(f"base theorem state is invalid YAML: {exc}")
            return None
        if not isinstance(data, dict):
            self.err("base theorem state is not a mapping")
            return None
        return data

    @staticmethod
    def dict_without(data: Any, keys: set[str]) -> Any:
        if not isinstance(data, dict):
            return data
        return {k: v for k, v in data.items() if k not in keys}

    def check_transaction(self) -> None:
        if not self.base_ref:
            return
        changed = self.changed_files()
        base = self.base_state()
        if changed is None or base is None:
            return
        if self.semantic_state(base) == self.semantic_state(self.state):
            return

        if MANIFEST not in changed:
            self.err("theorem-state semantics changed without changing the manifest file")
        if base.get("state_version") == self.state.get("state_version"):
            self.err("theorem-state semantics changed without incrementing state_version")
        if "docs/STATE.md" not in changed:
            self.err("theorem-state semantics changed without updating docs/STATE.md")

        base_targets = base.get("targets", {}) if isinstance(base.get("targets"), dict) else {}
        head_targets = self.state.get("targets", {}) if isinstance(self.state.get("targets"), dict) else {}
        prompt_fields = {
            "target-a": {"status", "canonical_sections_through", "global_endpoint", "locked_branch_endpoint"},
            "target-b": {"status", "global_endpoint"},
            "target-c": {
                "status",
                "c_i",
                "c_ii",
                "canonical_modules",
                "current_canonical_entries",
                "regressions",
                "rejected_or_overridden",
            },
        }
        for target_name in sorted(set(base_targets) | set(head_targets)):
            before = base_targets.get(target_name)
            after = head_targets.get(target_name)
            if before == after or not isinstance(after, dict):
                continue
            route = after.get("route_map")
            if isinstance(route, str) and route not in changed:
                self.err(f"{target_name} state changed without updating its route map: {route}")
            if target_name == "target-c":
                current = after.get("current_frontier")
                if isinstance(current, str) and current not in changed:
                    self.err(f"target-c state changed without updating CURRENT.md: {current}")
            before_relevant = self.dict_without(before, set(before.keys()) - prompt_fields.get(target_name, set())) if isinstance(before, dict) else before
            after_relevant = self.dict_without(after, set(after.keys()) - prompt_fields.get(target_name, set()))
            if before_relevant != after_relevant:
                prompt = after.get("active_prompt")
                if isinstance(prompt, str) and prompt not in changed:
                    self.err(f"{target_name} frontier changed without updating active prompt: {prompt}")

        lifecycle_keys = {"status_vocabulary", "defaults", "artifact_policy", "graph_policy", "certificate_policy"}
        if any(base.get(key) != self.state.get(key) for key in lifecycle_keys):
            for rel in ("docs/state/README.md", "docs/RESEARCH_WORKFLOW.md"):
                if rel not in changed:
                    self.err(f"lifecycle policy changed without updating {rel}")

        generated = self.state.get("generated_views", {})
        if isinstance(generated, dict):
            for rel in generated.values():
                if isinstance(rel, str) and rel not in changed:
                    self.err(f"theorem-state semantics changed without refreshing generated view: {rel}")

        artifact_policy = self.state.get("artifact_policy", {})
        if isinstance(artifact_policy, dict):
            index = artifact_policy.get("index")
            if isinstance(index, str) and index not in changed:
                self.err(f"theorem-state semantics changed without refreshing artifact index: {index}")

    def run(self) -> list[str]:
        self.load()
        if not self.state:
            return self.errors
        self.validate_schema()
        self.check_bucket_statuses()
        self.entry_map()
        self.check_paths()
        self.check_graph()
        self.check_level()
        self.check_stale_phrases()
        self.check_a()
        self.check_b()
        self.check_c()
        self.check_prompts()
        self.run_subcheck(ARTIFACT_INDEXER)
        self.run_subcheck(VIEW_GENERATOR)
        self.check_relative_links()
        self.check_transaction()
        return self.errors


def run_checks(root: Path, base_ref: str | None = None) -> list[str]:
    return Checker(root, base_ref=base_ref).run()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--base-ref", help="git base ref for PR promotion-transaction checks")
    args = parser.parse_args(argv)
    errors = run_checks(args.root, base_ref=args.base_ref)
    if errors:
        for error in errors:
            print(f"theorem-state: {error}", file=sys.stderr)
        print(f"theorem-state: FAILED ({len(errors)} errors)", file=sys.stderr)
        return 1
    print("theorem-state: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
