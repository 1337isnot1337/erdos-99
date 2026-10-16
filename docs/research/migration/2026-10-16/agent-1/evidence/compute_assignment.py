#!/usr/bin/env python3
"""Recompute the deterministic three-way source-main migration allocation."""
from __future__ import annotations
import argparse, hashlib, json, math, os, re, subprocess
from collections import defaultdict
from pathlib import PurePosixPath

SOURCE_SHA = "42f0296d1aca068c809f74cee5dcdb4ebdb27c73"
DESTINATION_SHA = "c6e0394b3152d21075328bf4f26e6c070229bf13"
FROZEN_PATH = "docs/research/migration/2026-10-16/frozen-target-c-813-dispositions.jsonl"
INITIAL_LOADS = [90, 75, 60]


def git(repo: str, *args: str, input: bytes | None = None) -> bytes:
    p = subprocess.run(["git", "-C", repo, *args], input=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode:
        raise RuntimeError(f"git -C {repo} {' '.join(args)} failed: {p.stderr.decode(errors='replace')}")
    return p.stdout


def tree(repo: str, rev: str) -> list[dict]:
    out = git(repo, "ls-tree", "-rz", "--full-tree", rev)
    rows=[]
    for record in out.split(b"\0"):
        if not record: continue
        meta, path = record.split(b"\t", 1)
        mode, typ, oid = meta.decode("ascii").split()
        rows.append({"path": path.decode("utf-8"), "mode": mode, "type": typ, "oid": oid})
    return rows


def cat_blobs(repo: str, oids: list[str]) -> dict[str, bytes]:
    unique=list(dict.fromkeys(oids))
    p=subprocess.run(["git","-C",repo,"cat-file","--batch"],input=("\n".join(unique)+"\n").encode(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if p.returncode: raise RuntimeError(p.stderr.decode(errors="replace"))
    out=p.stdout; pos=0; result={}
    for wanted in unique:
        end=out.find(b"\n",pos)
        if end<0: raise RuntimeError(f"cat-file ended before {wanted}")
        fields=out[pos:end].split(); pos=end+1
        if len(fields)!=3 or fields[1]!=b"blob": raise RuntimeError(f"unexpected cat-file header {fields!r}")
        actual=fields[0].decode(); size=int(fields[2]); data=out[pos:pos+size]; pos+=size
        if len(data)!=size or out[pos:pos+1]!=b"\n": raise RuntimeError(f"truncated blob {actual}")
        pos+=1; result[actual]=data
    return result


def family_key(path: str) -> str | None:
    name=PurePosixPath(path).name
    suffix=PurePosixPath(name).suffix.lower()
    stem=name[:-len(PurePosixPath(name).suffix)] if PurePosixPath(name).suffix else name
    is_note=suffix in {".md", ".markdown"}
    is_verifier=suffix in {".py", ".cpp"} and stem.startswith("verify_")
    if not (is_note or is_verifier): return None
    if is_verifier: stem=stem[len("verify_"):]
    if not stem.startswith(("target_a_", "target_b_", "target_c_", "global_")): return None
    # Normalize only date separators, preserving hyphens elsewhere in titles.
    stem=re.sub(r"(\d{4})[-_](\d{2})[-_](\d{2})", r"\1_\2_\3", stem)
    return stem


def third_party_path(path: str) -> bool:
    p=PurePosixPath(path); suffix=p.suffix.lower()
    if p.parts and p.parts[0] == "papers" and suffix in {".pdf", ".djvu", ".ps", ".epub"}:
        return True
    return len(p.parts) >= 2 and p.parts[0] == "extracted" and p.parts[1] in {"images", "text"}


def is_research_markdown(path: str) -> bool:
    p=PurePosixPath(path)
    if p.suffix.lower() not in {".md", ".markdown"} or p.name.lower()=="readme.md": return False
    if path.startswith(("docs/reports/", "docs/audits/", "docs/targets/", "research/", "docs/archive/")):
        return not path.startswith("docs/research/migration/") and not path.startswith("research/cleanup/")
    if path.startswith("docs/research/"):
        return not path.startswith("docs/research/migration/")
    if path.startswith(("docs/theory/", "docs/problem/")) or path == "docs/literature_review.md":
        return True
    return False


def classify(path: str, size: int, conflict: bool) -> tuple[str,int,str]:
    p=PurePosixPath(path); suffix=p.suffix.lower()
    # Third-party academic PDFs and text/image extractions from them are reviewed for exclusion.
    if third_party_path(path):
        return "third_party_exclusion_review", 1+(3 if conflict else 0), "third-party academic PDF or extracted literature; do not copy"
    if is_research_markdown(path):
        kind="markdown_research_proof"; base=3; threshold=10000
    elif suffix in {".py", ".cpp"} and p.name.startswith("verify_"):
        kind="python_cpp_verifier"; base=3; threshold=8000
    else:
        kind="other"; base=1; threshold=20000
    addition=min(12, math.ceil(size/threshold))
    cost=base+addition+(3 if conflict else 0)
    return kind,cost,"same-path conflict; preserve source bytes separately and retain destination revision" if conflict else "source-main artifact requires reconciliation"


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-git",required=True)
    ap.add_argument("--destination-git",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    os.makedirs(a.out,exist_ok=True)
    source=tree(a.source_git,SOURCE_SHA); dest=tree(a.destination_git,DESTINATION_SHA)
    source_blobs=cat_blobs(a.source_git,[r["oid"] for r in source])
    dest_by_oid=defaultdict(list)
    for r in dest: dest_by_oid[r["oid"]].append(r["path"])
    dest_by_path={r["path"]:r for r in dest}
    dest_blob_data=cat_blobs(a.destination_git,[r["oid"] for r in dest if r["path"] in {s["path"] for s in source} and dest_by_path.get(r["path"],{}).get("oid") != next((s["oid"] for s in source if s["path"]==r["path"]),None)])
    frozen_blob=git(a.destination_git,"show",f"{DESTINATION_SHA}:{FROZEN_PATH}")
    frozen={}
    for line in frozen_blob.splitlines():
        r=json.loads(line)
        frozen[r["source"]["path"]]=r["source"]["sha256"]
    rows=[]; backlog=[]; source_by_path={}
    for s in source:
        path=s["path"]; raw=source_blobs[s["oid"]]; sha=hashlib.sha256(raw).hexdigest(); size=len(raw)
        source_by_path[path]=(s,sha,raw)
        if path in frozen:
            if frozen[path] != sha: raise RuntimeError(f"frozen report source hash mismatch: {path}")
            status="already_preserved_frozen_report_813"; exact=[]
        elif s["oid"] in dest_by_oid:
            exact=sorted(dest_by_oid[s["oid"]]); status="already_preserved_same_content"
        else:
            exact=[]; status="migration_backlog"
        same=dest_by_path.get(path)
        relation=("same_path_identical" if same and same["oid"]==s["oid"] else
                  "same_path_different_content" if same else
                  "path_absent_identical_blob_elsewhere" if exact else "path_absent")
        dsha=None
        if same and same["oid"] != s["oid"]:
            dsha=hashlib.sha256(dest_blob_data[same["oid"]]).hexdigest()
        row={"source_path":path,"source_mode":s["mode"],"source_git_blob_sha1":s["oid"],"source_sha256":sha,"source_bytes":size,
             "destination_relation":relation,"destination_same_path_sha256":dsha,"destination_identical_blob_paths":exact,
             "frozen_disposition":status=="already_preserved_frozen_report_813","backlog":status=="migration_backlog","status":status}
        if status=="migration_backlog":
            conflict=relation=="same_path_different_content"
            kind,cost,reason=classify(path,size,conflict)
            key=family_key(path) or path
            row.update({"unit_key":key,"cost_kind":kind,"file_cost":cost,"conflict_cost_added":3 if conflict else 0,"initial_disposition":reason})
            backlog.append(row)
        rows.append(row)
    units=defaultdict(list)
    for r in backlog: units[r["unit_key"]].append(r)
    unit_rows=[]
    for key,files in units.items():
        unit_rows.append({"unit_key":key,"file_count":len(files),"total_cost":sum(x["file_cost"] for x in files),"source_paths":sorted(x["source_path"] for x in files)})
    unit_rows.sort(key=lambda u:(-u["total_cost"],u["unit_key"]))
    loads=INITIAL_LOADS.copy()
    for u in unit_rows:
        owner=min(range(3),key=lambda i:(loads[i],i))
        u["agent"]=owner+1; u["workload_before"]=loads[owner]; loads[owner]+=u["total_cost"]; u["workload_after"]=loads[owner]
    owner_by_key={u["unit_key"]:u["agent"] for u in unit_rows}
    for r in rows:
        if r["backlog"]: r["agent"]=owner_by_key[r["unit_key"]]
        else: r["agent"]=None
    rows.sort(key=lambda r:r["source_path"])
    def jsonl(name,objects):
        path=os.path.join(a.out,name)
        with open(path,"w",encoding="utf-8",newline="\n") as f:
            for obj in objects: f.write(json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False)+"\n")
    jsonl("source-main-three-way-assignment.jsonl",rows)
    jsonl("source-main-three-way-units.jsonl",unit_rows)
    assigned=defaultdict(list)
    for u in unit_rows: assigned[u["agent"]].append(u)
    spread=max(loads)-min(loads); pct=100*spread/(sum(loads)/3)
    summary={"algorithm":"agent-shard-lpt-v1","source_main_sha":SOURCE_SHA,"source_main_tree":git(a.source_git,"rev-parse",f"{SOURCE_SHA}^{{tree}}").decode().strip(),"destination_main_sha":DESTINATION_SHA,"destination_main_tree":git(a.destination_git,"rev-parse",f"{DESTINATION_SHA}^{{tree}}").decode().strip(),"source_file_count":len(source),"destination_tracked_file_count":len(dest),
      "frozen_report_count":sum(x["status"]=="already_preserved_frozen_report_813" for x in rows),
      "same_content_preserved_count":sum(x["status"]=="already_preserved_same_content" for x in rows),"backlog_file_count":len(backlog),
      "backlog_unit_count":len(unit_rows),"starting_workloads":INITIAL_LOADS,"final_workloads":loads,"workload_spread_points":spread,"workload_spread_percent_of_mean":round(pct,6),
      "assigned_file_counts":{str(i):sum(x["agent"]==i for x in rows) for i in range(1,4)},"assigned_unit_counts":{str(i):len(assigned[i]) for i in range(1,4)},
      "reconciliation_counts":{k:sum(x["destination_relation"]==k for x in rows) for k in ["same_path_identical","same_path_different_content","path_absent_identical_blob_elsewhere","path_absent"]},
      "frozen_manifest_source":FROZEN_PATH,"frozen_manifest_sha256":hashlib.sha256(frozen_blob).hexdigest(),"grouping":"For .md/.markdown research notes and verify_*.py/.cpp files only, strip optional verify_ and extension; group target_a_, target_b_, target_c_, global_ basenames with ISO date separators normalized to underscores. Other files use full source path.","cost_rules":"Research Markdown 3+ceil(bytes/10000), verifier 3+ceil(bytes/8000), other 1+ceil(bytes/20000), size addition capped at 12; add 3 for same-path different-content. Third-party PDF/extraction review cost 1, plus conflict surcharge if applicable."}
    with open(os.path.join(a.out,"assignment-summary.json"),"w",encoding="utf-8") as f: json.dump(summary,f,indent=2,sort_keys=True); f.write("\n")
    # Hash every generated evidence file except this checksum file.
    sums={}
    for name in ["source-main-three-way-assignment.jsonl","source-main-three-way-units.jsonl","assignment-summary.json"]:
        sums[name]=hashlib.sha256(open(os.path.join(a.out,name),"rb").read()).hexdigest()
    with open(os.path.join(a.out,"SHA256SUMS"),"w",encoding="utf-8") as f:
        for name,digest in sums.items(): f.write(f"{digest}  {name}\n")
    print(json.dumps(summary,indent=2,sort_keys=True))
    print("SHA256SUMS",json.dumps(sums,sort_keys=True))

if __name__=="__main__": main()
