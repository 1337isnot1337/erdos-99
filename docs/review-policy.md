# Mathematical review policy

This beta separates exploratory work from mathematical acceptance. A submitted or merged change is not automatically a theorem.

## Evidence status

Use these evidence labels in issues and pull requests, combining them when needed:

1. **Author-checked claim** — authors report checking the argument or computation; no independent review is implied.
2. **Unreviewed proposal** — a question, conjecture or candidate proof that has not been independently checked.
3. **Conditional claim** — a result with all unresolved assumptions stated explicitly.
4. **Reproduced computational evidence** — a computation or certificate rerun for the exact scope it checks.
5. **Independently agent-audited** — an agent that did not author the work checked a stated scope. This is not human review.
6. **Human-reviewed mathematical result** — a human who did not author the work checked the proof and stated scope.
7. **Rejected or superseded result** — a claim with a documented invalid step or replacement; preserve the reason so it is not repeated.
8. **Canonical mathematical statement** — a result explicitly promoted by maintainers after human mathematical review and a written scope check.

Statuses may not be inferred from a green test, an issue reaction, a merged pull request, or the passage of time. Reviewers may be any community member; no appointed panel or approved-reviewer roster is required.

## Review steps

- Reviewers first restate the exact question, definitions, quantifiers and hypotheses.
- Proof submissions must identify every implication and state where each cited lemma is proved.
- Computations must include the model, input bounds, exact arithmetic or error analysis, executable command, expected output and a negative control where applicable.
- A reviewer should try to falsify the claim with boundary cases, alternate configurations, degeneracies and counterexamples to intermediate steps.
- Contributions may be accepted or merged with an accurate evidence label while further review is pending. Lack of an appointed human reviewer does not block ordinary contribution acceptance.
- A consequential theorem claim may be promoted to canonical status only after independent human mathematical review. An author, coauthor or AI agent that generated the claim cannot serve as that human reviewer. Community members may volunteer reviews; no panel is designated in advance.
- If review is incomplete, preserve the result with its actual status and list the remaining question.

## Attribution and AI assistance

Submissions must identify all human authors and describe AI assistance, including the model or tool when known, date or version when available, and the parts it helped produce. Authors remain responsible for correctness, source attribution and license compliance. An AI-generated proof check is useful evidence but does not count as independent human mathematical review.

## Canonical promotion

Maintainers may promote a result only after its scope, provenance, attribution, independent human review and reproducibility are recorded. A canonical statement must include a stable identifier and an explicit statement of what it does not prove. Ordinary contributions can be merged before this higher bar is met. This beta has no theorem-promotion automation.
