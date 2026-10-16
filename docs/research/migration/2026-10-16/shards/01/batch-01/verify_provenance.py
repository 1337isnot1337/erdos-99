#!/usr/bin/env python3
"""Verify batch-01 source provenance and imported report/support bytes."""
import argparse, hashlib, json, pathlib, re, subprocess, sys

BASE=pathlib.Path(__file__).resolve().parent
SHARD=BASE.parent

def sha(data): return hashlib.sha256(data).hexdigest()
def git(repo,*args): return subprocess.check_output(['git','-C',str(repo),*args],text=True).strip()
def transformed(data, steps):
    for step in steps:
        if step['kind']=='byte_repair':
            old=bytes.fromhex(step['find_hex']); new=bytes.fromhex(step['replace_hex'])
            assert data.count(old)==step['count']
            data=data.replace(old,new)
        elif step['kind']=='trim_terminal_lf':
            assert step['remove_count']==1 and data.endswith(b'\n\n')
            data=data[:-1]
        elif step['kind']=='dependency_path_relocation':
            old=step['find'].encode(); new=step['replace'].encode()
            assert data.count(old)==step['count']
            data=data.replace(old,new)
        else: raise ValueError(step)
    return data

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source',required=True,type=pathlib.Path)
    p.add_argument('--destination',required=True,type=pathlib.Path)
    a=p.parse_args(); source=a.source.resolve(); destination=a.destination.resolve()
    reports=[json.loads(x) for x in (BASE/'dispositions.jsonl').read_text().splitlines()]
    supports=[json.loads(x) for x in (BASE/'support.jsonl').read_text().splitlines()]
    for row in reports:
        source_path=source/row['path']; dest_path=destination/row['destination_path']
        raw=source_path.read_bytes()
        assert sha(raw)==row['source_sha256'], row['path']
        assert git(source,'rev-parse',f"{row['source_commit']}:{row['path']}")==row['source_blob_sha1'], row['path']
        expected=transformed(raw,row['transformations'])
        actual=dest_path.read_bytes()
        assert sha(expected)==row['destination_sha256']==sha(actual), row['path']
        assert git(destination,'hash-object',str(dest_path))==row['destination_blob_sha1'], row['path']
        first=actual.splitlines()[0].decode()
        state=json.loads(re.search(r'<!-- theorem-state: (\{.*\}) -->',first).group(1))
        assert state['canonical'] is False and state['status']=='unreviewed', row['path']
    for row in supports:
        raw=(source/row['source_path']).read_bytes(); dest_path=destination/row['destination_path']
        assert sha(raw)==row['source_sha256'],row['source_path']
        assert git(source,'rev-parse',f"{row['source_commit']}:{row['source_path']}")==row['source_blob_sha1'],row['source_path']
        assert sha(dest_path.read_bytes())==row['destination_sha256']==sha(raw),row['source_path']
        assert git(destination,'hash-object',str(dest_path))==row['destination_blob_sha1'],row['source_path']
    print(f'PASS: {len(reports)} reports and {len(supports)} support files match pinned source provenance and recorded transformations')

if __name__=='__main__': main()
