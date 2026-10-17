from __future__ import annotations

import errno
import json
import subprocess
import sys
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

    def symlink(self, path, target, *, directory=False):
        try:
            path.symlink_to(target, target_is_directory=directory)
        except NotImplementedError as exc:
            self.skipTest(f"native symlink fixture unavailable: {exc}")
        except OSError as exc:
            if (exc.errno in {errno.EACCES, errno.EPERM, errno.ENOSYS, errno.ENOTSUP}
                    or getattr(exc, 'winerror', None) in {1, 50, 1314}):
                self.skipTest(f"native symlink fixture unavailable: {exc}")
            raise
        subprocess.run(["git", "-C", str(self.root), "config", "core.symlinks", "true"], check=True)

    def test_fast_docs_do_not_need_private_state(self):
        (self.root/"README.md").write_text("# Revised\n")
        self.commit()
        self.assertEqual(validate(self.root,self.base),[])

    def test_unchanged_long_archive_path_does_not_block_documentation(self):
        relative = 'docs/archive/' + '/'.join(['historical-' + 'a' * 70] * 3) + '/proof.md'
        self.assertGreater(len(relative), 240)
        archived = self.root / relative
        try:
            archived.parent.mkdir(parents=True)
            archived.write_text('# Retained historical proof\n', encoding='utf-8')
        except OSError as exc:
            if exc.errno == errno.ENAMETOOLONG or getattr(exc, 'winerror', None) == 206:
                self.skipTest(f'filesystem does not support this long-path fixture: {exc}')
            raise
        self.base = self.commit()
        (self.root / 'README.md').write_text('# Revised\n', encoding='utf-8')
        self.commit()
        self.assertEqual(validate(self.root, self.base), [])

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

    def test_symlinked_manifest_rejected_before_parsing(self):
        (self.root / 'docs/state').mkdir(parents=True)
        outside = self.root.parent / ('outside-' + self.root.name + '.yaml')
        outside.write_text('a private non-metadata file\n')
        self.addCleanup(outside.unlink)
        self.symlink(self.root / 'docs/state/theorem-state.yaml', outside)
        self.commit()
        process = subprocess.run(
            [sys.executable, str(Path(__file__).with_name('ci_integrity.py')),
             '--root', str(self.root), '--base-ref', self.base], capture_output=True, text=True)
        self.assertEqual(process.returncode, 1)
        self.assertIn('rejected before theorem metadata parsing', process.stdout)
        self.assertNotIn('Traceback', process.stderr)
        self.assertNotIn('a private non-metadata file', process.stdout + process.stderr)

    def test_unchanged_symlink_also_rejected(self):
        self.symlink(self.root / 'docs', self.root.parent, directory=True)
        self.base = self.commit()
        self.assertTrue(any('nonregular' in e for e in validate(self.root, self.base)))


if __name__=="__main__":
    unittest.main()

