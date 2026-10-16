#!/usr/bin/env python3
"""Recompute batch textual overlap and exact duplicate candidates at the pinned tree."""
import argparse, collections, hashlib, io, json, pathlib, re, subprocess, tarfile

def git(repo,*args): return subprocess.check_output(['git','-C',str(repo),*args])
def shingles(text,n=5):
    words=re.findall(r'[a-z0-9]+',text.lower())
    return {tuple(words[i:i+n]) for i in range(max(0,len(words)-n+1))}
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source-repo',required=True,type=pathlib.Path)
    p.add_argument('--destination-repo',required=True,type=pathlib.Path)
    p.add_argument('--threshold',type=float,default=.018)
    a=p.parse_args(); source=a.source_repo.resolve(); destination=a.destination_repo.resolve()
    records=[json.loads(x) for x in (pathlib.Path(__file__).parent/'dispositions.jsonl').read_text().splitlines()]
    archive=tarfile.open(fileobj=io.BytesIO(git(destination,'archive','--format=tar','358af8253f85ab7b9cdbf976ce186ee8426718e')),mode='r:')
    corpus=[]; exact=collections.defaultdict(list)
    for member in archive.getmembers():
        if not member.isfile(): continue
        stream=archive.extractfile(member)
        if stream is None: continue
        raw=stream.read(); exact[hashlib.sha256(raw).hexdigest()].append(member.name)
        if member.name.endswith('.md'):
            ss=shingles(raw.decode('utf-8','ignore'))
            if len(ss)>=25: corpus.append((member.name,ss))
    inverted=collections.defaultdict(set)
    for j,(_,ss) in enumerate(corpus):
        for gram in ss: inverted[gram].add(j)
    print(json.dumps({'frozen_commit':'358af8253f85ab7b9cdbf976ce186ee8426718e','tracked_files':sum(map(len,exact.values())),'markdown_corpus':len(corpus),'threshold':a.threshold},sort_keys=True))
    for row in records:
        raw=(source/row['path']).read_bytes(); digest=hashlib.sha256(raw).hexdigest()
        overlaps=collections.Counter(j for gram in shingles(raw.decode('utf-8','ignore')) for j in inverted.get(gram,()))
        matches=[]
        q=shingles(raw.decode('utf-8','ignore'))
        for j,count in overlaps.most_common():
            other=corpus[j][1]; score=count/len(q|other)
            if score>=a.threshold: matches.append({'destination_path':corpus[j][0],'jaccard_5gram':round(score,4)})
        print(json.dumps({'index':row['index'],'path':row['path'],'exact_byte_matches':exact.get(digest,[]),'overlap_candidates':matches},sort_keys=True))
if __name__=='__main__': main()
