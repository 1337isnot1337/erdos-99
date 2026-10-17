"""Optional Linux namespace isolation; portable imports and no unsafe fallback."""
from __future__ import annotations

import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

try:
    import resource
except ImportError:  # Windows can still plan changes and run ordinary checks.
    resource = None

from .packages import Invalid, load_package
from .plan import Snapshot, git, make_plan, revision


def sandbox_prefix(bindings, *, writable=None):
    if sys.platform != 'linux':
        raise Invalid('optional Linux isolation backend is unavailable on ' + sys.platform +
                      '; refusing unisolated execution')
    if resource is None:
        raise Invalid('optional Linux isolation backend requires POSIX resource limits; '
                      'refusing unisolated execution')
    bwrap = shutil.which('bwrap')
    if not bwrap:
        raise Invalid('optional Linux isolation backend requires bubblewrap (bwrap); '
                      'refusing unisolated execution')
    args = [bwrap, '--unshare-all', '--die-with-parent', '--new-session', '--cap-drop', 'ALL',
            '--clearenv', '--setenv', 'PATH', '/usr/bin:/bin', '--setenv', 'HOME', '/tmp',
            '--setenv', 'LANG', 'C.UTF-8', '--setenv', 'PYTHONDONTWRITEBYTECODE', '1',
            '--setenv', 'PYTHONHASHSEED', '0', '--ro-bind', '/usr', '/usr',
            '--proc', '/proc', '--dev', '/dev', '--tmpfs', '/tmp']
    for target in ('bin', 'lib', 'lib64'):
        source = Path('/') / target
        if source.is_symlink():
            args += ['--symlink', os.readlink(source), '/' + target]
        elif source.exists():
            args += ['--ro-bind', str(source), '/' + target]
    # setup-python uses a tool-cache interpreter, often newer than /usr/bin/python3.
    # Expose the selected trusted runtime (and a local verification venv) explicitly.
    for prefix in sorted({Path(sys.base_prefix), Path(sys.prefix)}):
        if prefix != Path('/usr'):
            args += ['--ro-bind', str(prefix), str(prefix)]
    args += ['--setenv', 'LD_LIBRARY_PATH', str(Path(sys.base_prefix) / 'lib')]
    for source, target in bindings:
        args += ['--ro-bind', str(source), str(target)]
    if writable:
        args += ['--bind', str(writable), '/output']
    return args


def sandbox_unavailable_reason(require_replay_python=False):
    """Probe only trusted runtime startup; return why optional isolation cannot run.

    An installed bubblewrap binary is not enough: container or kernel policy may
    disable the required namespaces. This never runs contributed package code.
    """
    try:
        argv = sandbox_prefix([])
    except Invalid as exc:
        return str(exc)
    if require_replay_python and sys.version_info[:2] != (3, 14):
        return ('optional isolated package replay requires its declared Python 3.14 runtime; '
                f'current runtime is {sys.version_info[0]}.{sys.version_info[1]}')
    try:
        probe = subprocess.run(
            argv + ['--chdir', '/tmp', '--', sys.executable, '-I', '-S', '-c', 'pass'],
            stdin=subprocess.DEVNULL, capture_output=True,
            env={'PATH': '/usr/bin:/bin'}, timeout=5,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return 'optional Linux isolation backend cannot start the trusted runtime: ' + str(exc)
    if probe.returncode:
        detail = ' '.join(probe.stderr.decode('utf-8', errors='replace').split())[:300]
        return ('optional Linux isolation backend cannot create the required namespaces/runtime '
                f'(exit {probe.returncode})' + (': ' + detail if detail else ''))
    return None


def bounds(cpu):
    if resource is None:
        raise Invalid('POSIX resource limits are unavailable; refusing unbounded execution')
    os.umask(0o077)
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    resource.setrlimit(resource.RLIMIT_FSIZE, (8 * 1024 * 1024,) * 2)
    resource.setrlimit(resource.RLIMIT_AS, (1024 * 1024 * 1024,) * 2)
    resource.setrlimit(resource.RLIMIT_NOFILE, (128, 128))
    resource.setrlimit(resource.RLIMIT_CPU, (cpu + 1, cpu + 1))


def execute(argv, seconds, logfile):
    if sys.platform != 'linux' or resource is None:
        raise Invalid('optional Linux isolation backend is unavailable; refusing unisolated execution')
    started = time.perf_counter()
    with open(logfile, 'wb') as output:
        process = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=output,
                                   stderr=subprocess.STDOUT, env={'PATH': '/usr/bin:/bin'},
                                   start_new_session=True, preexec_fn=lambda: bounds(seconds))
        try:
            status = process.wait(timeout=seconds)
            outcome = 'passed' if status == 0 else 'failed'
        except subprocess.TimeoutExpired:
            outcome, status = 'timeout', None
        finally:
            # bwrap PID namespace + die-with-parent also cleans detached descendants.
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait()
    return {'status': outcome, 'exit_code': status,
            'seconds': round(time.perf_counter() - started, 6)}


def replay(root, plan, output):
    if plan['level'] != 'targeted-replay' or not plan['replay_allowed']:
        raise Invalid('plan does not authorize targeted replay')
    # Recompute from Git, never authorize work from an arbitrary JSON plan.
    fresh = make_plan(root, plan['base'], plan['head'])
    if fresh != plan:
        raise Invalid('stale or altered plan')
    unavailable = sandbox_unavailable_reason(require_replay_python=True)
    if unavailable:
        raise Invalid(unavailable)
    output.mkdir(parents=True, exist_ok=True)
    snapshot = Snapshot(root, plan['head'])
    results = {'version': 1, 'head': plan['head'], 'level': 'targeted-replay',
               'full_verified': False, 'status': 'failed', 'packages': []}
    for index, directory in enumerate(plan['packages']):
        package = load_package(snapshot, directory)
        if package['unresolved']:
            raise Invalid('unresolved input closure')
        record = {'package': directory, 'status': 'failed', 'commands': []}
        results['packages'].append(record)
        with tempfile.TemporaryDirectory(prefix='e99-replay-') as temp:
            work = Path(temp) / 'work'
            work.mkdir()
            for p in sorted(package['inputs']):
                target = work / p
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(snapshot.read(p))
                target.chmod(0o444)
            for number, command in enumerate(package['verify']['commands']):
                entry = command['argv'][1]
                # Isolated interpreter, no user site/customizations, explicit import roots.
                bootstrap = ('import runpy,sys;assert sys.version_info[:2]==(3,14);sys.path[:0]=["/work",'
                             + repr('/work/' + str(Path(entry).parent)) + '];'
                             + 'sys.argv=[' + repr(entry) + '];runpy.run_path('
                             + repr('/work/' + entry) + ',run_name="__main__")')
                argv = sandbox_prefix([(work, '/work')]) + [
                    '--chdir', '/work', '--', sys.executable, '-I', '-S', '-c', bootstrap]
                logfile = output / f'package-{index}-command-{number}.log'
                result = execute(argv, command['timeout_seconds'], logfile)
                result['log'] = logfile.name
                record['commands'].append(result)
                if result['status'] != 'passed':
                    break
            if all(r['status'] == 'passed' for r in record['commands']):
                record['status'] = 'passed'
        if record['status'] != 'passed':
            break
    if len(results['packages']) == len(plan['packages']) and all(p['status'] == 'passed' for p in results['packages']):
        results['status'] = 'passed'
    (output / 'replay.json').write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8', newline='\n')
    return results


def integrity(root, control, plan, output):
    """Run only trusted checkers against read-only contributed data, without secrets."""
    if not plan.get('merge_base'):
        raise Invalid('cannot validate integrity without ancestry')
    unavailable = sandbox_unavailable_reason()
    if unavailable:
        raise Invalid(unavailable)
    common = Path(git(root, 'rev-parse', '--git-common-dir').decode().strip())
    if not common.is_absolute():
        common = (root / common).resolve()
    # Preserve worktree .git's absolute pointer. No credentials are persisted by checkout.
    bindings = [(root, '/work'), (control, '/control'), (common, common)]
    # Local shared clones may use read-only object stores outside their .git.
    # These are Git-created metadata, never paths from contributed manifests.
    stores = [common / 'objects']
    seen = set()
    while stores:
        store = stores.pop().resolve()
        if store in seen:
            continue
        seen.add(store)
        if len(seen) > 8:
            raise Invalid('too many alternate Git object stores')
        alternates = store / 'info/alternates'
        if alternates.is_file():
            for raw in alternates.read_text().splitlines():
                alternate = Path(raw)
                if not alternate.is_absolute():
                    alternate = store / alternate
                alternate = alternate.resolve()
                bindings.append((alternate, alternate))
                stores.append(alternate)
    output.mkdir(parents=True, exist_ok=True)
    argv = sandbox_prefix(bindings) + ['--chdir', '/work', '--', sys.executable, '-I', '-c',
        'import runpy,sys;sys.path.insert(0,"/control/tools");'
        'sys.argv=["ci_integrity.py","--root","/work","--base-ref",'
        + repr(plan['merge_base']) + '];runpy.run_path("/control/tools/ci_integrity.py",run_name="__main__")']
    return execute(argv, 55, output / 'integrity.log')

