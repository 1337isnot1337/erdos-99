from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.ci_integrity import validate


class PublicIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.context = tempfile.TemporaryDirectory()
        self.addCleanup(self.context.cleanup)
        self.root = Path(self.context.name).resolve()
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "Fixture"], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.email", "fixture@example.invalid"], check=True)
        for path in ("README.md", "AGENTS.md", "autoresearch.md", "CONTRIBUTING.md", "LICENSE", "NOTICE"):
            (self.root / path).write_text("# present\n")
        (self.root / "tasks").mkdir()
        (self.root / "tasks" / "index.json").write_text(json.dumps({"schema_version":1,"tasks":[]})+"\n")
        self.base=self.commit()

    def commit(self):
        subprocess.run(["git", "-C", str(self.root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(self.root), "commit", "-qm", "fixture"], check=True)
        return subprocess.check_output(["git","-C",str(self.root),"rev-parse","HEAD"],text=True).strip()

    def test_fast_docs_do_not_need_private_state(self):
        (self.root/"README.md").write_text("# Revised\n")
        self.commit()
        self.assertEqual(validate(self.root,self.base),[])

    def test_broken_local_link_is_rejected(self):
        (self.root/"README.md").write_text("[broken](missing-document.md)\n")
        self.commit()
        self.assertTrue(any("broken" in x for x in validate(self.root,self.base)))

    def test_bad_json_and_undisclosed_index_paths(self):
        (self.root/"tasks"/"index.json").write_text("{")
        self.commit()
        self.assertTrue(any("tasks/index.json" in x for x in validate(self.root,self.base)))

    def test_cannot_walk_task_outside_repo(self):
        (self.root/"tasks"/"index.json").write_text(json.dumps({"tasks":[{"id":"evil","path":"../external"}]}))
        self.commit()
        self.assertTrue(any("noncanonical" in x for x in validate(self.root,self.base)))

    def test_no_executable_code_from_candidate(self):
        (self.root/"README.md").write_text("[valid](AGENTS.md)\n")
        (self.root/"untrusted.py").write_text('raise SystemExit("executed attacker code")\n')
        self.commit()
        self.assertEqual(validate(self.root,self.base),[])


if __name__=="__main__":
    unittest.main()

