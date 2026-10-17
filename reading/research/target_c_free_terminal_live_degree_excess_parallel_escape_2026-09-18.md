> Generated reading edition · [exact source](../../research/target_c_free_terminal_live_degree_excess_parallel_escape_2026-09-18.md) · source SHA-256 `38343f8eba701aacb33a6d06d58cf08c1f5459068e24c7a00d7f57efce2424cd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d1589f4ce3a017265fe32fc350ff88c78b8729aa", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_live_degree_excess_parallel_escape_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ffcc3f9e83530f5b003d87f449d480b8f175c8e70553c59a54a2fb5bfe890e8f"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — live degree excess collapses the parallel residual escapes

**Date:** 2026-09-18  
**Status:** proof-only corollary; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE subsequences with `pi D-q=o(D)` and `limsup t_D<=mu_*+0.00710`  
**Depends on:** live detour-pinching theorem; bounded-pentagon no-parallel-side theorem; maximal two-anchor residual decomposition  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The live detour-pinching theorem proves

$$
r:={Q-f\over D}<0.000141+o(1).
\tag{1}
$$

The bounded-pentagon no-parallel-side theorem supplies, for the residual system after
maximal two-anchor activation,

$$
n_2\le x_U,
\qquad
2p_U\le x_U,
\tag{2}
$$

where `n_2` counts residual faces with two outer/activated incidences, `p_U` counts
mutually parallel one-anchor internal links, and

$$
x_U:=\sum_{F\in U}(\deg F-5).
$$

Since the total degree excess splits as

$$
x_A+x_U=Q-f
$$

with `x_A,x_U>=0`, (1)--(2) immediately give

$$
\boxed{
{n_2\over D}<0.000141+o(1),
\qquad
{p_U\over D}<0.0000705+o(1).
}
\tag{3}
$$

Thus neither of the two parallel-side residual mechanisms can occur at linear density
on the live terminal endpoint.  In particular, the explicit `p_U` flex correction in
the one-anchor theorem contributes at most `0.0000705D+o(D)` there, and the two-outside
parallel residual faces occupy at most `0.000141D+o(D)` vertices of the residual face
population.

This does not upper-bound `n_0`: the remaining low-flex obstruction may still use
zero-anchor residual faces.  But if one simultaneously approaches the pair-shield
counting floor, the structural excess

$$
E_U=a_F+{x_A\over2}+{n_0+n_2\over2}
$$

must be `o(D)`, and then `n_0=o(D)` as well.  Such a low-flex sequence is therefore,
up to `o(D)` exceptional residual faces, a degree-five one-anchor system with no mutual
parallel links.  Its nonzero pure-contact dual modes are exactly the sparse nonparallel
relation components isolated by the one-anchor corank theorem; the smallest possible
support remains a five-face `K_5` block.

The point is bookkeeping rather than closure: after combining the newest local
pentagon lemma with the live scalar pinching, the parallel residual escapes are too
small to carry a new macroscopic branch.  The unresolved macroscopic mechanism is the
nonparallel one-anchor core and its interaction with the positively locking actual
diameter graph.

No theorem-state file is changed.

**Disposition:** proved the live bounds `n_2/D<0.000141+o(1)` and
`p_U/D<0.0000705+o(1)` and reduced the pair-shield low-flex endpoint to the
nonparallel one-anchor core up to sublinear defects; C-II remains open.
