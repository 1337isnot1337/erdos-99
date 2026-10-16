#!/usr/bin/env python3
"""Verify batch-02 source provenance, transformations, and stronger successor."""
import argparse,hashlib,json,pathlib,re,subprocess
BASE=pathlib.Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def git(repo,*args):return subprocess.check_output(['git','-C',str(repo),*args],text=True).strip()
def transform(data,steps):
 for s in steps:
  if s['kind']=='byte_repair':
   a=bytes.fromhex(s['find_hex']);b=bytes.fromhex(s['replace_hex']);assert data.count(a)==s['count'];data=data.replace(a,b)
  elif s['kind']=='dependency_path_relocation':
   a=s['find'].encode();b=s['replace'].encode();assert data.count(a)==s['count'];data=data.replace(a,b)
  else:raise ValueError(s)
 return data
def main():
 p=argparse.ArgumentParser();p.add_argument('--source',required=True,type=pathlib.Path);p.add_argument('--destination',required=True,type=pathlib.Path);a=p.parse_args();src=a.source.resolve();dst=a.destination.resolve()
 rows=[json.loads(x) for x in (BASE/'dispositions.jsonl').read_text().splitlines()]; imported=[x for x in rows if x['disposition']=='imported_full_first_party_report']; skipped=[x for x in rows if x['disposition'].startswith('verified_subsumed')]; supports=[json.loads(x) for x in (BASE/'support.jsonl').read_text().splitlines()]
 for r in imported:
  raw=(src/r['path']).read_bytes();assert sha(raw)==r['source_sha256'];assert git(src,'rev-parse',f"{r['source_commit']}:{r['path']}")==r['source_blob_sha1'];out=transform(raw,r['transformations']);p=dst/r['destination_path'];assert sha(out)==r['destination_sha256']==sha(p.read_bytes());assert git(dst,'hash-object',str(p))==r['destination_blob_sha1'];st=json.loads(re.search(r'<!-- theorem-state: (\{.*\}) -->',p.read_text().splitlines()[0]).group(1));assert st['canonical'] is False and st['status']=='unreviewed'
 for r in skipped:
  raw=(src/r['path']).read_bytes();assert sha(raw)==r['source_sha256'];assert git(src,'rev-parse',f"{r['source_commit']}:{r['path']}")==r['source_blob_sha1'];sraw=subprocess.check_output(['git','-C',str(dst),'show',f"{r['destination_frozen_commit']}:{r['destination_path']}"]);assert sha(sraw)==r['destination_sha256'];assert git(dst,'rev-parse',f"{r['destination_frozen_commit']}:{r['destination_path']}")==r['destination_git_blob_sha1']
 for r in supports:
  raw=(src/r['source_path']).read_bytes();p=dst/r['destination_path'];assert sha(raw)==r['source_sha256'];assert git(src,'rev-parse',f"{r['source_commit']}:{r['source_path']}")==r['source_blob_sha1'];assert sha(p.read_bytes())==r['destination_sha256']==sha(raw);assert git(dst,'hash-object',str(p))==r['destination_blob_sha1']
 print(f'PASS: {len(imported)} imported reports, {len(skipped)} verified subsumption, {len(supports)} support file')
if __name__=='__main__':main()
