import json, subprocess, pathlib
RUN=pathlib.Path('/home/cinna/.local/state/erdos99-merge/20261019')
REPO=RUN/'review-b'
assignment=json.load(open(RUN/'reviews/b-assignment.json'))
integrity=json.load(open('/tmp/review-b-integrity.json'))
by_num={x['number']:x for x in integrity['results']}
scopes={
104:('Finite seven-label two-face shear with fixed retained isolate; enumerates all 21 pairs and bounds feasible shear by |c|<=21/100, with endpoint third diameter and outside failure.','accept_archive',['No source extraction or canonical move; this is a finite obstruction/cap only.'],[]),
106:('Six exact sparse-stress fixtures are excluded by same-cardinality lattice-disk competitors; exact source and competitor counts and excesses are reported.','accept_archive',['The result covers six fixtures, not a source-independent theorem.'],[]),
111:('Conditional full-pair restoration after deleting supplied p0 from a ten-chain plus pinned q: supplied r=(8/5,11/10) restores strict pair distances in (1,81), with diameter squared 3673/50.','accept_scoped',['Requires the supplied source configuration, stress, deletion, and insertion hypotheses; not a universal repair existence theorem.'],['Do not promote the conditional instance to source extraction or a global move.']),
114:('Exact algebraic cut-stress calculation in an abstract two-shore boundary-payment model, including cut vectors, packet balance, determinant, shear and work.','accept_archive',['No planar/global source realization is supplied.'],[]),
115:('Finite palette-transversal equivalence under the stated exact constraints, with verifier controls.','accept_scoped',['Applies to the finite palette model only; does not establish a global source move.'],[]),
116:('Independent report on PR948 quarter-fold face obstructions; source-only audit, with no new extraction or endpoint theorem.','accept_scoped',['Historical proof reconstruction was not repeated; source scope follows the cited report and canonical interfaces.'],[]),
124:('Destination audit accepts only near-diameter localization for every s>=0, including s=0 and s=2; companion endpoint-tail/moment and full diameter-edge transfer are excluded. Candidate registry wording remains unreviewed/noncanonical.','accept_scoped',['No global atlas/source extraction; no candidate promotion.','The full historical proof chain for inherited canonical hypotheses was not reconstructed.'],[]),
126:('For every m>=7 the moving rhombic wall source has (m+1)^2 labels and zero safe insertion capacity: tiling plus circumradius^2<=1/2 covers the full container by unit neighborhoods, while Oler slack grows quadratically.','accept_archive',['The all-m proof is conditional on the stated rhombic family and does not prove global source extraction.'],[]),
127:('Independent audit of the open-cell phase-flux identity; sign and inverse-D consequences are conditional on positive moving-diameter stress, non-grazing/source-window hypotheses and the cited Section 90 window.','accept_scoped',['No global theorem; inherited proof chain is not reconstructed end-to-end.'],[]),
129:('Wall-tolerance/refill ledger for the oblique grid family; at m=7 deleting 13 leaves 51 labels and 1,275 pairs, with exact maximum squared distance 84, exposing an unpaid deficit.','accept_archive',['No 13-label payback or global existence statement.'],[]),
132:('Conditional destination audit of the branch-aware 0.0071 atomic gap, relying on the stated pair-payment premise.','accept_scoped',['The pair-payment premise is not independently established here; no theorem promotion.'],['Keep the premise explicit in any downstream use.']),
133:('Independent exact audit of PR111 deletion/restoration source, stress, restored velocities and strict pair constraints.','accept_scoped',['Shares PR111’s supplied-instance scope; no universal repair claim.'],[]),
135:('Independent exact audit of PR104 fixed-isolate shear bounds and all-pair derivation.','accept_scoped',['Same finite fixture and assumptions as PR104; no canonical move or global extraction.'],[]),
136:('Independent reconstruction of PR114 cut rows, A/B cuts, packet balance, shear/work and perturbation controls.','accept_scoped',['Abstract model only; no source realization.'],[]),
137:('Independent exact rational audit of PR106’s six lattice competitor fixtures, including q-bound and finite enumeration.','accept_scoped',['Only six specified fixtures; no universal sparse-stress exclusion.'],[]),
142:('For rational t in (0,1/10], coupled shear moves PR104’s isolate below D; all 21 pairs are checked and D_t^2=1+(11/5-t)^2.','accept_archive',['Finite seven-label ladder only; no global source extraction.'],[]),
143:('Independent exact audit of PR129’s m=7 endpoint, checking all 1,275 pairs and maximum squared distance 84.','accept_scoped',['Finite endpoint only; unpaid refill deficit remains.'],[]),
149:('Independent analytic report for PR948 large-array boundary attachment, scoped to complete bent rhombic arrays with a,c>=delta D and boundary attachment lower bound r>=epsilon delta D.','accept_scoped',['Does not establish full-source extraction or a global result; finite verifier is supplementary to report proof.'],[]),
150:('Independent complete-array diameter-forest audit of PR948 with its stated boundary and array hypotheses.','accept_scoped',['No canonical source extraction or global theorem; report scope is conditional complete-array geometry.'],[]),
151:('Exact reflected-scale parity criterion: same-sign/opposite-sign cost comparison plus boundary-slack forcing; XOR consistency is equivalent to feasible parity choices.','accept_archive',['Finite criterion/implementation only; does not show a source realizes the requisite graph.'],[]),
152:('For every m>=7, a moving-wall rectangular endpoint with one exterior guard row has (m+1)(m+2) labels, all-pairs bounds and zero safe insertion capacity; Oler slack is quadratic.','accept_archive',['Applies to the specified family, not a canonical source extraction.'],[]),
155:('Abstract support-complete convex average over all stress-reachable actual diameter edges; zero-multiplier edges require an explicit sign branch, and all moving diameter rows shortening forces a near-active pair under endpoint minimality hypotheses.','accept_scoped',['Abstract stress/endpoint implication only; no planar source realization or global proof.'],[]),
160:('Independent exact audit of PR142 coupled shear, with rational range and strict pair bounds.','accept_scoped',['Same finite family as PR142; README proof supplies monotonicity argument, while checker does not separately assert y>0.'],[]),
164:('Exact finite eight-label paths with exterior point W_h for h=1 or 11/10; all 28 pairs, with one variant adding a contact and one none, each retaining unique source diameter and strict shorter endpoint.','accept_archive',['Finite examples only; no global move.'],[]),
168:('Asymptotic reflected-scale moment obstruction under the report’s exact scaling and weak-limit assumptions; does not imply a strict lower-order gain or source extraction.','accept_scoped',['No canonical promotion; full historical proof reconstruction not performed.','Report contains a duplicated identical theorem-state HTML marker requiring artifact hygiene review.'],['Confirm duplicate report marker does not cause artifact-index or generation ambiguity.']),
172:('Conditional annular-packet lemma: if safe core Y is separated and |Y|>=tau(G_D(A)), annular graph is G_D(A) plus isolated Y and M_D=n+|Y|-tau>=n; finite fixture has zero vacancy.','accept_scoped',['No proof that global sources supply such a core; no extraction theorem.'],[]),
}
records=[]
for p in assignment:
 n=p['number']; i=by_num[n]
 scope,disp,limits,repairs=scopes[n]
 # Pull declared source bindings from the exact immutable package head where present.
 sources=[]
 spaths=[x for x in p['paths'] if x.endswith('/SOURCES.json')]
 if spaths:
  raw=subprocess.check_output(['git','show',f"{p['head']}:{spaths[0]}"],cwd=REPO,text=True)
  sj=json.loads(raw)
  sources=[{'path':x.get('path'),'commit':x.get('commit'),'sha256':x.get('sha256'),'identity':x.get('identity')} for x in sj.get('inputs',[])]
 records.append({
  'number':n,'title':p['title'],'head':p['head'],'base':p['base'],'merge_base':i['merge_base'],
  'inventory':{'api_changed_files':p['changed_files'],'assignment_path_count':len(p['paths']),'github_changed_files':i['github_inventory_count'],'git_diff_count':i['git_inventory_count'],'full_path_inventory_match':i['inventory_match'],'paths':p['paths'],'modes':i['modes']},
  'static_integrity':{'head_ref_matches_immutable_sha':i['head_ref_match'],'json_python_parse_errors':i['json_jsonl_python_parse_errors'],'source_pin_count':i['source_pin_count'],'source_pin_errors':i['source_pin_errors'],'result':'PASS' if i['static_integrity_pass'] else 'FAIL','evidence':'/tmp/review-b-integrity.json'},
  'lane':('source-only audit report' if any(x.startswith('docs/') for x in p['paths']) else 'finite/conditional research archive'),
  'disposition':disp,'coverage':scope,
  'actual_commands':[
   {'command':'/home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/venv/bin/python /tmp/review-b-integrity.py','result':'PASS; exact immutable head, base/merge-base, API and git inventory, modes, source pins, JSON/JSONL and Python syntax checked for all 26 assigned PRs.','log':'/tmp/review-b-integrity.json'}
  ],
  'source_bindings':sources,
  'dependencies_and_evidence_reuse':'Exact underlying PR/result reuse is limited to the named audit targets in coverage; no full historical canonical proof chain was reconstructed. Source pins and immutable identities were checked independently.',
  'scope_limitations':limits,
  'open_obligations':repairs,
  'necessary_repairs':repairs,
  'evidence_complete':False
 })
obj={'reviewer':'/root/review_b','scope':'Group B assigned 26 PRs, finite C moves/capacity and related audits; plus separate amendment review for PR117/121 and PR124/139 registry reconciliation at 8bc3d8f10ecf7204078f8db66005dfc0551263c6.','evidence_complete':False,'integration_commit_for_special_audits':'8bc3d8f10ecf7204078f8db66005dfc0551263c6','metadata_repin_validation_commit':'173b3dd14fa784f65f80bb9485b0f72ed1a36916','metadata_repin_validation':{'result':'PASS','summary':'4 B-package repin rows across PR115, PR149 and PR172: old hashes match original named blobs; new hashes match exact 8bc metadata blobs; final SOURCES pins match repin rows. README/TASK/VERIFY/checker blobs were unchanged between 8bc and 173. 20 distinct B package metadata checks passed at 173; these are metadata checks and do not replace direct source/math review.','log':'/tmp/review-b-repins.py and /tmp/review-b-meta-*.log'},'correction_review':'/home/cinna/.local/state/erdos99-merge/20261019/reviews/b-correction-review.json','prs':records}
path=RUN/'reviews/b-review.json'
path.write_text(json.dumps(obj,indent=2)+'\n')
print(path)
print('written',len(records),'records; all evidence_complete false')
