# GitHub reading edition

This edition displays mathematical sources with GitHub-compatible formatting.
Mathematical pages link to their sources and record source hashes so the
[generation manifest](manifest.json) can detect stale rendering. These hashes
do not freeze the current source or promote a mathematical claim.

Contribution instructions, workflow guides, task cards, and release documentation
link to their current files. Edit those files normally through Git; their reading
links contain no duplicated content or source hashes. Historical archives and
their original source records remain separate from current documents.

Unclosed source display delimiters are repaired only at paragraph boundaries and
flagged on their pages. Paragraphs with ambiguous inline delimiters are shown as
explicit source excerpts. These presentation notes preserve the underlying text
and make source formatting damage visible rather than inventing an equation.
Exact-source-bound TeX escape and punctuation corrections are disclosed on each
affected page and in the [presentation repair ledger](../docs/publication/reading-tex-repairs.json).
Deliberately truncated formula quotations remain literal text. Quoted and listed
equations retain their Markdown containers; the mathematical payload does not
include Markdown quote or table separators.

Start with the [problem](docs/problem/statement.md), [current state](docs/STATE.md),
[research map](docs/KNOWLEDGE_MAP.md), [glossary](docs/GLOSSARY.md), and
[numbered bibliography](docs/BIBLIOGRAPHY.md). Then choose [A](docs/targets/target-a/README.md),
[B](docs/targets/target-b/README.md), [C-II](docs/targets/target-c/CURRENT.md), or
a [current task](tasks/README.md). The [original repository overview](../README.md)
and [exact source documentation](../docs/README.md) remain available.

Regenerate with `python tools/build_reading_edition.py` from the repository root;
`python tools/build_reading_edition.py --check` verifies the entire edition.
