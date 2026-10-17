"""Shared documentation scope for diff planning; mathematical inputs take priority."""
from __future__ import annotations

import json


WORKFLOW_DOCS = {
    'README.md', 'AGENTS.md', 'CONTRIBUTING.md', 'autoresearch.md',
    'docs/README.md', 'docs/START_HERE.md', 'docs/GLOSSARY.md',
    'docs/COORDINATION.md', 'docs/REVIEW_POLICY.md', 'docs/RESEARCH_WORKFLOW.md',
    '.github/PULL_REQUEST_TEMPLATE.md', '.github/copilot-instructions.md',
    'research/README.md',
    'docs/research/README.md', 'docs/research/bottleneck-brief.md',
    'docs/research/obstructions.md', 'docs/research/proposals.md',
    'docs/research/research-family-status.md', 'docs/research/research-priority-log.md',
    'docs/research/agent-procedure.md', 'docs/research/current-priorities.md',
    'docs/research/pr-intake.md', 'docs/research/research-archive-intake.md',
    'docs/research/research-package-guide.md',
}
WORKFLOW_PREFIXES = (
    'tasks/', 'docs/ci/', 'docs/launch/', 'docs/prompts/',
    'docs/research/tracks/', 'reading/',
)


def is_workflow_document(path: str, protected=()) -> bool:
    """Recognize navigation prose/metadata, never override a declared proof input."""
    if path in protected:
        return False
    if path == 'reading/manifest.json':
        return True
    if not path.endswith('.md'):
        return False
    return (path in WORKFLOW_DOCS or path.startswith(WORKFLOW_PREFIXES)
            or (path.startswith('docs/targets/') and path.endswith('/README.md')))


def mathematical_inputs(state: dict, read_optional=None) -> set[str]:
    """Collect current proof/certificate paths and their declared file dependencies.

    ``read_optional`` returns bytes/text for a current metadata file, or None when
    absent. It can read a Git snapshot or a checkout. No source hashes are used.
    A malformed available dependency map raises ValueError so callers cannot
    silently classify an unknown mathematical input as documentation.
    """
    protected = set()

    def paths(value, label):
        if not isinstance(value, list) or any(not isinstance(p, str) for p in value):
            raise ValueError(f'{label}: expected file path list')
        return value

    def visit(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key in ('report', 'audit') and isinstance(item, str):
                    protected.add(item)
                elif key in ('canonical_modules', 'certificates') and isinstance(item, list):
                    protected.update(p for p in item if isinstance(p, str))
                visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(state)
    if read_optional is None:
        return protected

    def metadata(path):
        raw = read_optional(path)
        if raw is None:
            return None
        obj = json.loads(raw)
        if not isinstance(obj, dict):
            raise ValueError(f'{path}: expected mapping')
        return obj

    registry = metadata('research/certificates.json')
    if registry is not None:
        records = registry.get('certificates')
        if not isinstance(records, list):
            raise ValueError('certificate registry: expected certificates list')
        for record in records:
            if not isinstance(record, dict) or not isinstance(record.get('path'), str):
                raise ValueError('certificate registry: missing certificate path')
            protected.add(record['path'])
            for field in ('proof_sources', 'executable_dependencies'):
                protected.update(paths(record.get(field, []), 'certificate ' + field))

    dependencies = {}
    supplement = metadata('docs/research/onboarding-prerequisites.json')
    if supplement is not None:
        additions = supplement.get('file_dependencies', {})
        if not isinstance(additions, dict):
            raise ValueError('onboarding dependencies: expected mapping')
        for path, required in additions.items():
            dependencies.setdefault(path, set()).update(paths(required, 'onboarding dependencies'))

    pending = list(protected)
    while pending:
        for path in dependencies.get(pending.pop(), ()):
            if path not in protected:
                protected.add(path)
                pending.append(path)
    return protected
