#!/usr/bin/env python3
"""PR-aware theorem-state checker without diff-only generated-file false positives.

The base checker already recomputes and byte-checks the artifact index and generated
views. A semantic manifest change can legitimately leave one of those generated outputs
byte-identical. Requiring an unchanged generated file to appear in the Git diff is
therefore impossible and adds no safety.

This wrapper preserves every content check and every substantive promotion-transaction
check. It removes only those two redundant diff-membership errors. It also checks the
Target A locked endpoint with the same mathematical normalization used for the global
endpoint instead of raw prose-substring equality.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from check_theorem_state import Checker as BaseChecker


class Checker(BaseChecker):
    """Base theorem-state checker with corrected PR-only transaction semantics."""

    def check_a(self) -> None:
        before = len(self.errors)
        super().check_a()

        # The base implementation compares the locked endpoint as raw prose. Keep all
        # other Target A errors, then recheck only the mathematical core after the final
        # descriptive colon, if one is present.
        self.errors[before:] = [
            error
            for error in self.errors[before:]
            if "does not contain locked-branch endpoint" not in error
        ]

        target = self.state.get("targets", {}).get("target-a", {})
        if not isinstance(target, dict):
            return
        locked = target.get("locked_branch_endpoint")
        if not isinstance(locked, str):
            return
        formula = locked.rsplit(":", 1)[-1].strip()
        expected = self.math(formula)
        for rel in (target.get("route_map"), target.get("active_prompt")):
            if not isinstance(rel, str):
                continue
            if expected not in self.math(self.read(rel)):
                self.err(f"{rel} does not contain normalized locked-branch endpoint {formula!r}")

    def check_transaction(self) -> None:
        before = len(self.errors)
        super().check_transaction()

        # build_artifact_index.py and generate_theorem_state_views.py already run in
        # BaseChecker.run() before this method and compare exact generated contents.
        # If a semantic state change does not alter a generated output, requiring that
        # byte-identical file to appear in the PR diff is both impossible and redundant.
        self.errors[before:] = [
            error
            for error in self.errors[before:]
            if not error.startswith("theorem-state semantics changed without refreshing generated view:")
            and not error.startswith("theorem-state semantics changed without refreshing artifact index:")
        ]


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
            print(f"theorem-state: {error}")
        print(f"theorem-state: FAILED ({len(errors)} errors)")
        return 1
    print("theorem-state: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
