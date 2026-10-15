# Theorem ledger

[theorem-state.yaml](theorem-state.yaml) controls lifecycle. [STATUS.generated.md](STATUS.generated.md) and [THEOREM_GRAPH.generated.md](THEOREM_GRAPH.generated.md) are derived views. [artifact-index.jsonl](artifact-index.jsonl) classifies retained reports and audits without promoting unlisted claims. Run `python tools/generate_theorem_state_views.py --write`, `python tools/build_artifact_index.py --write --write-headers`, then `python tools/check_public.py` after an authorized state transaction.
