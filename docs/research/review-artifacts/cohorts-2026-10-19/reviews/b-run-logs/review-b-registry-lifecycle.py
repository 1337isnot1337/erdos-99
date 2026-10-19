import json,subprocess
repo='/home/cinna/.local/state/erdos99-merge/20261019/review-b'; revisions=['8bc3d8f10ecf7204078f8db66005dfc0551263c6','2d5aa36f01ac131b791b9b6a745e8c963f4a363c','e185b58bfffa27be92d4ec91d919f1aa4f939725']
ids=['TARGET-C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND-PR947','TARGET-C-POSITIVE-LEAF-ANCHOR-D23-PR947','TARGET-C-PR952-UNEQUAL-HEIGHT-ISOLATE-TRANSPORT']
rows=[]
for rev in revisions:
 data=json.loads(subprocess.check_output(['git','show',f'{rev}:docs/targets/target-c/candidate-registry.json'],cwd=repo,text=True)); by={x['candidate_id']:x for x in data['entries']}
 x={'commit':rev,'entries':[]}
 for i in ids:
  e=by[i]; row={'candidate_id':i,'status':e.get('status'),'source_lifecycle':e.get('source_lifecycle'),'not_claimed':e.get('claim',{}).get('not_claimed',[]),'obstructions_and_limits':e.get('obstructions_and_limits',[])}; x['entries'].append(row)
 rows.append(x)
# Verify all three remain explicitly unreviewed at each snapshot; PR124/139 wording never promotes their claims.
assert all(e['status']=='unreviewed' or e['status'].startswith('unreviewed strengthening candidate;') for r in rows for e in r['entries'])
print(json.dumps({'all_unreviewed_or_unreviewed_strengthening':True,'snapshots':rows},indent=2))
