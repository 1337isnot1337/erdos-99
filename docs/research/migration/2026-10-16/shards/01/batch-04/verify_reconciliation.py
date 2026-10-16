#!/usr/bin/env python3
"""Verify pinned source/main equality, exact report transforms, and support provenance."""
import argparse,hashlib,json,pathlib,subprocess
BASE=pathlib.Path(__file__).resolve().parent
def git(repo,*args):return subprocess.check_output(["git","-C",str(repo),*args],stderr=subprocess.DEVNULL)
def main():
 p=argparse.ArgumentParser();p.add_argument("--source",required=True,type=pathlib.Path);p.add_argument("--destination",required=True,type=pathlib.Path);a=p.parse_args();src=a.source.resolve();dst=a.destination.resolve();rows=[json.loads(x) for x in (BASE/"dispositions.jsonl").read_text().splitlines()]
 for r in rows:
  raw=git(src,"show",f"{r['source_commit']}:{r['path']}");assert hashlib.sha256(raw).hexdigest()==r["source_sha256"];assert git(src,"rev-parse",f"{r['source_commit']}:{r['path']}").decode().strip()==r["source_blob_sha1"]
  current=git(dst,"show",f"{r['current_main_commit']}:{r['path']}");assert hashlib.sha256(current).hexdigest()==r["current_main_sha256"]==r["source_sha256"];assert git(dst,"rev-parse",f"{r['current_main_commit']}:{r['path']}").decode().strip()==r["current_main_blob_sha1"]==r["source_blob_sha1"]
  transformed=raw
  for t in r.get("report_transformations",[]):
   assert t["kind"]=="dependency_path_relocation";old=t["find"].encode();new=t["replace"].encode();assert transformed.count(old)==t["count"];transformed=transformed.replace(old,new)
  local=(dst/r["path"]).read_bytes();assert local==transformed;assert hashlib.sha256(local).hexdigest()==r["final_destination_sha256"];assert git(dst,"hash-object",str(dst/r["path"])).decode().strip()==r["final_destination_blob_sha1"]
  assert not r["canonical"] and r["source_lifecycle"]=="unreviewed";assert r["destination_path_present_at_frozen_baseline"] is False
 supports=[json.loads(x) for x in (BASE/"support.jsonl").read_text().splitlines()]
 for r in supports:
  raw=git(src,"show",f"{r['source_commit']}:{r['source_path']}");out=(dst/r["destination_path"]).read_bytes();assert hashlib.sha256(raw).hexdigest()==r["source_sha256"]==hashlib.sha256(out).hexdigest()==r["destination_sha256"];assert git(src,"rev-parse",f"{r['source_commit']}:{r['source_path']}").decode().strip()==r["source_blob_sha1"]
 print(f"PASS: {len(rows)} source reports, {sum(len(r.get('report_transformations',[])) for r in rows)} exact link transformation, and {len(supports)} support files verified")
if __name__=="__main__":main()
