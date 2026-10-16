#!/usr/bin/env python3
"""Verify exact source/current-main reconciliation for this report batch."""
import argparse,hashlib,json,pathlib,subprocess
BASE=pathlib.Path(__file__).resolve().parent
def git(repo,*args):return subprocess.check_output(["git","-C",str(repo),*args],stderr=subprocess.DEVNULL)
def main():
 p=argparse.ArgumentParser();p.add_argument("--source",required=True,type=pathlib.Path);p.add_argument("--destination",required=True,type=pathlib.Path);a=p.parse_args();src=a.source.resolve();dst=a.destination.resolve();rows=[json.loads(x) for x in (BASE/"dispositions.jsonl").read_text().splitlines()]
 for r in rows:
  raw=git(src,"show",f"{r['source_commit']}:{r['path']}"); assert hashlib.sha256(raw).hexdigest()==r["source_sha256"]; assert git(src,"rev-parse",f"{r['source_commit']}:{r['path']}").decode().strip()==r["source_blob_sha1"]
  out=git(dst,"show",f"{r['current_main_commit']}:{r['path']}"); assert hashlib.sha256(out).hexdigest()==r["current_main_sha256"]==r["source_sha256"]; assert git(dst,"rev-parse",f"{r['current_main_commit']}:{r['path']}").decode().strip()==r["current_main_blob_sha1"]==r["source_blob_sha1"]
  assert not r["canonical"] and r["source_lifecycle"]=="unreviewed"; assert r["destination_path_present_at_frozen_baseline"] is False
 print(f"PASS: {len(rows)} source reports match current main byte-for-byte; provenance and noncanonical lifecycle verified")
if __name__=="__main__":main()
