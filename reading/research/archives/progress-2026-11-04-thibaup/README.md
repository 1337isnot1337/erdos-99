> Generated reading edition · [exact source](../../../../research/archives/progress-2026-11-04-thibaup/README.md) · source SHA-256 `1427401a6a7c97166b8754244078188a44c5570c3622bc1dcef50eefeed8dea2`.
> [Current theorem state](../../../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Erdős #99 research progress archive — 4 November 2026

Submitted by [@thibaup](https://github.com/thibaup). Proposed lane: **archive**.
Scientific status: **partially_reviewed**. Research status at export: **paused**.
This contribution preserves locally saved progress; it establishes no solution
of the original problem and makes no canonical-state change.

For integer sizes at least two, let

```math
D_n=\min\{\operatorname{diam}(X):X\subset\mathbb R^2,\ |X|=n,
          \ |x-y|\ge1\text{ for all distinct }x,y\in X\}.
```

The original objective is to prove or disprove

```math
\exists N\ \forall n\ge N\ \forall X\quad
\bigl[|X|=n,\ \min_{x\ne y}|x-y|\ge1,\ \operatorname{diam}(X)=D_n\bigr]
\Longrightarrow
\exists\text{ distinct }a,b,c\in X:\ |a-b|=|b-c|=|c-a|=1.
```

All planar configurations and **every exact global minimizer** are quantified.
A disproof requires infinitely many sizes with rigorously certified exact global
triangle-free minimizers. Fixed-size examples, numerical optima, ordinary local
minima, asymptotic density, approximate contacts, lattice restrictions and
conditional finiteness results do not settle this statement.

The source is a non-Git handoff directory, followed by saved research through
the Wave133–135 reports and a partially saved Wave136 follow-up. The historical
root manifest is preserved as an input, not treated as a current Git identity.
The exact byte inventory is [inventory.json](../../../../research/archives/progress-2026-11-04-thibaup/inventory.json); its source-tree
SHA-256 is
`ba8d6c07727d1648c174db73944d4a45ddd0e11ae8752cff5d5283709656485d`.
The digest algorithm is specified in that inventory.

Of 4,853 original files (69,791,331 bytes), **4,731 text research artifacts** are
preserved in 40 UTF-8 JSONL [payload](../../../../research/archives/progress-2026-11-04-thibaup/payload/part-001.jsonl) shards, totaling
58,180,507 bytes. Each record has `path`, a zero-based `part`, total `parts` and
text `content`; the verifier rejoins fragments in order. The inventory index
links hash-pinned inventory shards. The full inventory maps
each original path and hash to its shard and published hash, or explains its
omission. Scripts have inert `.py.source` or `.ps1.source` names. Historical
source-relative links and instructions are data inside the payload.

The 122 omitted inputs comprise 91 bytecode caches, 25 third-party papers/page
images, three full paper extracts and three Lean source excerpts. Their paths,
sizes and original hashes remain inventoried. Private home paths were redacted;
three embedded copies of the excluded Lean extracts were removed. See
[export-report.json](../../../../research/archives/progress-2026-11-04-thibaup/export-report.json) and [NOTICE.md](NOTICE.md). The private
originals were preserved. This is a documented transformed export, not a claim
that every published file is byte-identical to its original.

Read [PROGRESS.md](PROGRESS.md) for the scientific frontier, navigation and
evidence gaps, and [VERIFICATION.md](VERIFICATION.md) for checks and their limits.
Historical filenames such as `verified-notes`, worker verdicts and active-goal
statements retain their original context. They are not a present certification
or an instruction to resume research. Failed, superseded and unreviewed attempts
are retained alongside corrections and the attribution ledger.

To verify the saved payload using Python's standard library:

```text
python research/archives/progress-2026-11-04-thibaup/verify_snapshot.py
```

To read the full archive as ordinary files, supply a new, nonexistent directory:

```text
python research/archives/progress-2026-11-04-thibaup/verify_snapshot.py --extract NEW_DIRECTORY
```

This restores only inert research text after checking all payload hashes. It
does not execute launchers or submit jobs. The optional `--source DIRECTORY`
also checks every included and omitted original against its source hash.
[build_snapshot.py](../../../../research/archives/progress-2026-11-04-thibaup/build_snapshot.py) records the deterministic export policy
and accepts an explicit source and separate destination.

The import base is `b05cd57b15252fe99577de3edb0b73070e79544f`.
Inherited upstream state: `2026-10-15.publication.2`, priority
`public-frontier.3`, catalogue `public-frontier.9`. This archive changes no
existing module, proof input, certificate, workflow or theorem-state entry.
Merge, if accepted, would preserve the archive; scientific promotion requires
the repository's separate review and state transaction.
