"""Dependency-free Phase 0 checks. Does not validate application functionality."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'PROJECT_STATUS.md', 'AGENTS.md', 'CONTRIBUTING.md', 'CHANGELOG.md', 'SECURITY.md',
    '.editorconfig', '.gitignore', '.gitattributes', '.env.example',
    '.github/CODEOWNERS', '.github/PULL_REQUEST_TEMPLATE.md',
    '.github/ISSUE_TEMPLATE/work-item.md', '.github/ISSUE_TEMPLATE/bug.md',
    '.github/ISSUE_TEMPLATE/config.yml', '.github/dependabot.yml',
    '.github/workflows/foundation.yml', 'docs/README.md',
    'docs/product/vision.md', 'docs/product/requirements.md',
    'docs/product/feature-catalog.md', 'docs/product/features.json',
    'docs/product/founder-brief.md', 'docs/product/user-stories.md',
    'docs/product/design-system.md', 'docs/architecture/overview.md',
    'docs/architecture/database.md', 'docs/architecture/api.md',
    'docs/architecture/ai.md', 'docs/architecture/integrations.md',
    'docs/architecture/sources.md', 'docs/security/threat-model.md',
    'docs/security/privacy.md', 'docs/planning/roadmap.md',
    'docs/planning/phase-1-backlog.md', 'docs/planning/decisions.md',
    'docs/planning/phase-0-issue.md', 'docs/planning/foundation-pr.md',
    'docs/planning/github-backlog.md',
    'docs/engineering/setup.md', 'docs/engineering/git-workflow.md',
    'docs/engineering/testing.md', 'docs/engineering/ci.md',
    'docs/engineering/release.md', 'docs/engineering/verification.md',
    'docs/engineering/foundation-review.md',
    'docs/engineering/github-governance.md', 'docs/engineering/phase-0-readiness.md',
    'docs/engineering/phase-0-approval-checklist.md',
    'docs/adr/README.md', 'docs/adr/0001-modular-monolith.md',
    'docs/adr/0002-isolation.md', 'docs/adr/0003-ai-and-actions.md',
    'docs/adr/0004-foundation-tooling.md', 'scripts/check_foundation.py',
    'docs/adr/0005-authentication-and-sessions.md',
    'docs/adr/0006-workspace-ownership-and-document-provenance.md',
]
STATUSES = {'Planned', 'In Development', 'Implemented', 'Verified', 'Released', 'Deprecated'}


def check(root: Path) -> list[str]:
    errors: list[str] = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f'Missing required file: {name}')

    files = [root / name for name in REQUIRED if (root / name).is_file()]
    for base in ('docs', '.github', 'scripts'):
        files.extend(p for p in (root / base).rglob('*') if p.is_file()
                     and p.suffix in {'.md', '.json', '.yml', '.py'})
    for path in sorted(set(files)):
        relative = path.relative_to(root)
        raw = path.read_bytes()
        try:
            content = raw.decode('utf-8')
        except UnicodeDecodeError:
            errors.append(f'{relative}: not UTF-8')
            continue
        if not raw.endswith(b'\n') or b'\r' in raw:
            errors.append(f'{relative}: expected LF and final newline')
        for number, line in enumerate(content.splitlines(), 1):
            # Preserve intentional Markdown two-space hard breaks in the source brief.
            if line.rstrip() != line and not (
                path.name == 'founder-brief.md' and line.endswith('  ')
                and line.rstrip() + '  ' == line
            ):
                errors.append(f'{relative}:{number}: trailing whitespace')
        if path.suffix == '.md':
            without_code = re.sub(r'```.*?```', '', content, flags=re.S)
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', without_code):
                if re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith('#'):
                    continue
                target_path = unquote(target.split('#', 1)[0].strip('<>'))
                resolved = (path.parent / target_path).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                    errors.append(f'{relative}: broken/escaping local link: {target}')

    feature_path = root / 'docs/product/features.json'
    if feature_path.exists():
        try:
            records = json.loads(feature_path.read_text(encoding='utf-8'))
            if not isinstance(records, list):
                raise ValueError('feature catalog must be a list')
            ids: set[str] = set()
            module_features: dict[int, set[str]] = {}
            catalog_path = root / 'docs/product/feature-catalog.md'
            catalog = catalog_path.read_text(encoding='utf-8') if catalog_path.exists() else ''
            for entry in records:
                for field in ('id', 'capability', 'description', 'priority', 'dependencies',
                              'story', 'acceptance', 'status'):
                    if not isinstance(entry.get(field), str) or not entry[field].strip():
                        raise ValueError(f'missing/empty field {field}')
                fid = entry['id']
                if fid in ids or not re.fullmatch(r'[A-Z]+-\d{3}', fid):
                    errors.append(f'Duplicate/invalid feature ID: {fid}')
                ids.add(fid)
                if entry['status'] not in STATUSES:
                    errors.append(f'{fid}: invalid status')
                if entry['priority'] not in {'P0', 'P1', 'P2', 'P3'}:
                    errors.append(f'{fid}: invalid priority')
                if type(entry.get('phase')) is not int or not 1 <= entry['phase'] <= 7:
                    errors.append(f'{fid}: invalid phase')
                module = entry.get('module')
                if type(module) is not int or not 1 <= module <= 15:
                    errors.append(f'{fid}: invalid module')
                    continue
                module_features.setdefault(module, set()).add(entry['capability'])
                expected = '| ' + ' | '.join([
                    fid, '**' + entry['capability'] + '**: ' + entry['description'],
                    entry['priority'], str(entry['phase']), entry['dependencies'],
                    entry['story'], entry['acceptance'], entry['status'],
                ]) + ' |'
                if catalog.splitlines().count(expected) != 1:
                    errors.append(f'{fid}: Markdown/JSON catalog mismatch')
            for entry in records:
                for dependency in re.findall(r'\b[A-Z]+-\d{3}\b', entry['dependencies']):
                    if dependency not in ids:
                        errors.append(f"{entry['id']}: missing dependency {dependency}")
            brief_path = root / 'docs/product/founder-brief.md'
            if brief_path.exists():
                brief = brief_path.read_text(encoding='utf-8')
                modules = re.findall(r'### 4\.(\d+) [^\n]+\n(.*?)(?=\n### 4\.|\n---)', brief, re.S)
                if len(modules) != 15:
                    errors.append('Expected all 15 source feature modules')
                for number, body in modules:
                    for capability in re.findall(r'^- (.+)$', body, re.M):
                        if capability not in module_features.get(int(number), set()):
                            errors.append(f'Missing source capability: {number}: {capability}')
            extras = {'Custom categories', 'Related records', 'Notes', 'Documents', 'Reminders', 'Timeline events'}
            if not extras <= module_features.get(8, set()):
                errors.append('Missing Life Areas prose requirements')
            if set(module_features) != set(range(1, 16)):
                errors.append('Catalog must cover modules 1 through 15')
        except (ValueError, KeyError, TypeError, AttributeError) as exc:
            errors.append(f'Invalid feature data: {exc}')
    return errors


if __name__ == '__main__':
    if sys.version_info < (3, 11):
        raise SystemExit('Python 3.11 or newer is required')
    failures = check(ROOT)
    if failures:
        print('\n'.join(f'ERROR: {failure}' for failure in failures))
        raise SystemExit(1)
    print('PASS: required files, UTF-8/LF hygiene, local file links and feature traceability')
