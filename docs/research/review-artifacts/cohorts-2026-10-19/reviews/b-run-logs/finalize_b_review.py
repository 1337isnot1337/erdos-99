import json,pathlib,hashlib,subprocess
run=pathlib.Path('/home/cinna/.local/state/erdos99-merge/20261019'); review=run/'reviews/b-review.json'; repo=run/'review-b'; data=json.load(open(review))
inputs={
116:[{'path':'docs/reports/target_c_quarter_fold_face_obstructions_slot02_2026-10-10.md','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'e441995708568951a3dd5eafcd162bf398669a46eaab99c91f142efc46e18f2f','git_blob':'5bd64db4c7e9dcad18e20bb820fb5adab24785e5'},{'path':'research/verify_target_c_quarter_fold_face_obstructions_2026_10_10.py','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'ced2ae1bb3ee3834f0a36d5869d25c7aedc0e447df2c8bb17013cf1d4a0a7d89','git_blob':'55a505dda56672c174372f71a725de5471e93589'},{'path':'research/target_c_quarter_fold_face_obstructions_certificate_2026_10_10.json','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'0ebf7367629a7555ce379b77f11af81b63d9e973eb0b84fd9a5eaee0512a3857','git_blob':'fad23c6de526520582ca54f079138ef1ade31e87'}],
127:[{'path':'research/target_c_open_cell_phase_flux_2026-10-03.md','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'82bcf72417a4e622cc72a2b52f7d4ae30b169a8970343d2a8ed7a9713f21ad1a','git_blob':'82411a0aad446f1f59461b4d45e061a5e9f87404'}],
132:[{'path':'research/target_c_branch_aware_iterative_pruning_atomic_gap_0071_2026-09-15.md','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'efe39d4523271be966ad4264959f8fa04474df6832d9bcd9fcc5513151b47ba6'},{'path':'research/target_c_branch_aware_iterative_pruning_atomic_gap_0071_hostile_audit_2026-09-15.md','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'0ecc90b876a568aa8ee9b57ad700fab712237083a8a072af4d19c3f91a480ba9'},{'path':'research/verify_target_c_branch_aware_atomic_gap_0071.py','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'79ef18464e8d271af7b16b17310ada1d78526d3cfdb6f34ced58f6e52e94466c'},{'path':'research/verify_target_c_branch_aware_atomic_gap_0071_pi_enclosure.py','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'f16635e93ffb5dc33d227eee6a44f6d721f6a503627fb43ec31bdf9c895f9009'}],
143:[{'path':'research-packages/e99-pass-20261018-homelab-06/README.md','revision':'f4dc4c6ec3a6bb08097ca9a963336ae454e14229','sha256':'13a0382b95d92eb95c8a3cf51b8b190e0aca43e63682c40fb164dd7882b2a7ac'},{'path':'research-packages/e99-pass-20261018-homelab-06/SOURCES.json','revision':'f4dc4c6ec3a6bb08097ca9a963336ae454e14229','sha256':'9df08c42bc8de2d7eefe1c6ed9941eefb77647d69a60a68bea6681c10c215ef7'},{'path':'research-packages/e99-pass-20261018-homelab-06/TASK.json','revision':'f4dc4c6ec3a6bb08097ca9a963336ae454e14229','sha256':'36656f1a9651485438874376ee7dac47996deee6b51db16056f3e4d9f2173e'},{'path':'research-packages/e99-pass-20261018-homelab-06/VERIFY.json','revision':'f4dc4c6ec3a6bb08097ca9a963336ae454e14229','sha256':'4c65ccf3aa1f7037f805f41ccecacafea509c7d8dbc2c584834d48d3679de5f4'},{'path':'research-packages/e99-pass-20261018-homelab-06/verify.py','revision':'f4dc4c6ec3a6bb08097ca9a963336ae454e14229','sha256':'da1f3fe7582f0259c1bf47ce751402c5d98febb17991d32056d76be534cb2f97'}],
168:[{'path':'docs/reports/global_reflection_moment_obstruction_2026-10-12.md','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'4e3e129da1129a659fae627fb7467beb557ca2f5ef4b45563e1666f84d0c7454'},{'path':'research/verify_global_reflected_scale_2026_10_12.py','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'caef9c87b7773aa1089ec845d30b35fb09bd70bde5f0264a128b51fc7f531403'},{'path':'docs/audits/pr959_autonomous_proof_audit_2026-10-15.md','revision':'7d0a450fe66991036541023f95c44c064a04b6a8','sha256':'30ce4ddc5721a402f0b98080c48d7c0ae5cecbf4b0e27393300983ec60ad34f1'}]
}
for d in data['prs']:
 n=d['number']
 if n in inputs:
  f=next(x for x in d['inventory']['paths'] if x.startswith('docs/') and x.endswith('.md'))
  raw=subprocess.check_output(['git','show',f"{d['head']}:{f}"],cwd=repo)
  first=raw.decode().splitlines()[0]; marker=json.loads(first[len('<!-- theorem-state: '):-len(' -->')])
  d['source_bindings']={'audit_artifact':{'path':f,'revision':d['head'],'sha256':hashlib.sha256(raw).hexdigest(),'git_blob':subprocess.check_output(['git','rev-parse',f"{d['head']}:{f}"],cwd=repo,text=True).strip(),'artifact_id':marker.get('artifact_id'),'canonical':marker.get('canonical'),'status':marker.get('status')},'reviewed_inputs':inputs[n]}
 if n==124:
  d['source_bindings']={'candidate_registry_and_tracks_reviewed_at':'8bc3d8f10ecf7204078f8db66005dfc0551263c6','source_scope':'TARGET-C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND-PR947 localization for s>=0, including s=0 and s=2; source report/candidate identity and canonical midpoint interfaces are detailed in b-correction-review.json and package notes.'}
# The all-26 static command is fully identified by its result artifact and status.
for d in data['prs']:
 for c in d['actual_commands']:
  if c.get('log')=='/tmp/review-b-integrity.json':
   c['exit_code']=0
# Add final repin authentication for B packages only.
rep=json.load(open('/tmp/review-b-final-repins.log'))
data['final_metadata_repin_validation']={'commit':'e185b58bfffa27be92d4ec91d919f1aa4f939725','result':'PASS' if rep['all_pass'] else 'FAIL','rows_checked':rep['rows_checked'],'rows':rep['checks'],'script':'/tmp/review-b-final-repins.py','log':'/tmp/review-b-final-repins.log'}
reg=json.load(open('/tmp/review-b-registry-lifecycle.log'))
data['candidate_lifecycle_recheck']={'commits':[x['commit'] for x in reg['snapshots']],'result':'PASS; PR124 localization candidate remains unreviewed and PR139 remains an unreviewed strengthening candidate retaining weaker canonical bound; PR153 remains unreviewed with explicit orientation warning. No theorem-state or canonical lifecycle promotion.','script':'/tmp/review-b-registry-lifecycle.py','log':'/tmp/review-b-registry-lifecycle.log'}
data['evidence_complete']=all(x['evidence_complete'] for x in data['prs']) and rep['all_pass']
review.write_text(json.dumps(data,indent=2)+'\n')
print('evidence_complete',data['evidence_complete'],'rows',len(data['prs']))
