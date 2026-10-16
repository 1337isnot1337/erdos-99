# Curated related literature

This directory contains a curated set of additional source documents identified in
the 2026-08-30 literature audit for Erdős Problem #99. The files are grouped here
because they extend the seven-paper baseline in `papers/primary/` without being part
of the repository's frozen canonical theorem stack.

The collection is intentionally selective. It covers:

- the original formulation and the closest known finite-diameter follow-up;
- Oler-type finite-packing inequalities and their Minkowski/generalized forms;
- finite packing shape, hull, and parametric-density results;
- saturation, gap-defect, and generation results that bear on the report's
  boundary/strain obstruction; and
- exact reformulation and computational literature for related packing problems.

See [`docs/literature_review.md`](../../docs/literature_review.md) for the annotated
bibliography, source links, reading paths, and the papers deliberately left as
citation-only leads.

## Provenance and use

- The filenames are normalized author-year slugs; each source is listed with its
  bibliographic record and access URL in the review.
- `wegner-1986-finite-circle-packings.pdf` is an article-only extraction from the
  492-page Studia Scientiarum Mathematicarum Hungarica volume. The full volume is
  not copied into the repository.
- PDFs were checked with `qpdf --check` after normalization. They are source copies
  for research and citation; the review records explicit open licenses where the
  publisher or repository states one, but does not make a blanket redistribution
  claim for every historical journal scan.
- `SHA256SUMS` records the checksums of the bundled PDFs so that future refreshes can
  distinguish a source update from a filename or organization change.
- None of these additions changes the canonical status: the report still records
  Erdős Problem #99 as open and does not promote any related paper as a proof of the
  target statement.

## Targeted finite-equality check, 2026-10-06

`boroczky-ruzsa-2007-note-on-wegner.pdf` is the authors' PDF of
K. J. Boroczky and I. Z. Ruzsa, *Note on an inequality of Wegner*, dated
January 2, 2007, downloaded from https://users.renyi.hu/~carlos/wegner.pdf.
Printed page 2 explicitly transcribes the finite Groemer/Oler equality
case. Scale its center separation two to separation one. The check and
its exact applicability are recorded in
`docs/reports/target_c_sorted_rate_packet_classification_2026-10-06.md`.
The original Groemer article was not accessible at the inspected EUDML
entry (HTTP 403); no original-text inspection is claimed. This additional
source does not promote the new classification or imply diameter equality
uniqueness. Its byte checksum is recorded in SHA256SUMS.
The added PDF was parsed and rendered with Poppler and its SHA256 checked;
`qpdf` was unavailable in this run, so no qpdf validation is claimed for it.
