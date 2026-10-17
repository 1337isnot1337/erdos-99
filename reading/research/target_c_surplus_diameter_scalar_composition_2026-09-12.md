> Generated reading edition · [exact source](../../research/target_c_surplus_diameter_scalar_composition_2026-09-12.md) · source SHA-256 `59448a6409dd72645d1386125ac9bb05c29fcea5db0383cdd966f78cb936d2fb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "99207ecf0d488482a49bb690f4066e7929cae87b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_surplus_diameter_scalar_composition_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "20b8b085e5ef42b47da8afc130f21467143e622d41de07b5f41d481107f300e6"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — renormalized-surplus / diameter-moment composition

**Date:** 2026-09-12  
**Classification:** rejected proof-only scalar composition; theorem-state authority
unchanged. A normalization error was identified on 2026-09-13. The claimed `2.0585`
floor and the claimed elimination of `t=1.9` are withdrawn. C-II remains open.

This note records an attempted composition of two proof-only endpoint inputs. It is
retained as provenance because it exposes a finite-versus-asymptotic bookkeeping
check. The attempted floor was obtained by treating the finite constant `2` as `2D`.

## 1. Variables and inputs

Normalize by the source diameter `D` and write

$$
 t={q-k\over D},\qquad \kappa={k\over D},\qquad
 e={e_{BB}\over D},\qquad s={s_C\over D},\qquad c={c_I\over D}.
$$

On the Type-II endpoint branch, use the proof-only identities

$$
 q/D=t+\kappa,
 \qquad e_{BB}=q-m,
 \qquad c_I+s_C=m+k-2.
\tag{1}
$$

The last two are the audited-working loaded-side/attachment identities with
`c_B=0`; `c_I/D\to0` by the canonical component-count theorem.  The exact
renormalized-surplus floor is canonical:

$$
 {e_{BB}+2s_C-3k\over D}
 \ge z_0-o(1),
 \qquad z_0=0.9604.
\tag{2}
$$

The conservative Section-131 endpoint moment inequality is

$$
 5q-7k\ge A_0D-o(D),
 \qquad A_0:=3(2.7985)+0.2104=8.6059.
\tag{3}
$$

The values `2.7985` and `0.2104` are rounded downward versions of the audited
Section-130 diameter moment and `c_*` payment, so (3) is used only as a
conservative proof-only endpoint input.

## 2. Exact elimination

From (1), with all quantities finite before normalization,

$$
 m=c_I+s_C-k+2,
$$

The `2` is an ordinary integer, not `2D`. Therefore, after division by `D`,

$$
 {m\over D}=c+s-\kappa+{2\over D},
 \qquad
 e={q-m\over D}=t+2\kappa-c-s-{2\over D}.
\tag{4-correct}
$$

Substituting (4-correct) into the surplus expression gives

$$
 {e_{BB}+2s_C-3k\over D}=t-\kappa+s-c-{2\over D}.
\tag{5-correct}
$$

Because `e\ge0`, (4-correct) also gives

$$
 s\le t+2\kappa-c-{2\over D}.
\tag{6-correct}
$$

Combining (5-correct) and (6-correct), and using `c\ge0`, yields

$$
 {e_{BB}+2s_C-3k\over D}
 \le 2t+\kappa-2c-{4\over D}
 \le 2t+\kappa-{4\over D}.
\tag{7-correct}
$$

Thus the canonical floor (2) gives only

$$
 2t+\kappa\ge z_0-o(1).
\tag{8-correct}
$$

Equation (3), after `q/D=t+\kappa`, is

$$
 5t-2\kappa\ge A_0-o(1).
\tag{9}
$$

There is no `+4` term to eliminate. Since `\kappa\ge0`, (9) itself gives only
the separate lower bound `t\ge A_0/5-o(1)=1.72118...-o(1)`; (8-correct) is
already satisfied there.

## 3. The old endpoint witness is not eliminated

The former normalized feasibility check retained `t=1.9,\kappa=0`. With the
corrected formula (7-correct), the corresponding upper bound tends to `3.8`, not
`-0.2`, so the canonical surplus floor does not eliminate `t=1.9`. Any use of the
old displayed elimination was invalid.

## 4. A corrected scalar witness

The corrected asymptotic ledger admits the rational values

$$
 t=1.9,\quad \kappa=0,\quad e=0.9,\quad c=0,
 \quad s=1,
$$

and set `q/D=t+\kappa=1.9`, `m/D=q/D-e=1`. Up to the vanishing `2/D`
finite correction, (4-correct) holds and

$$
 e+2s-3\kappa=2.9>0.9604,
$$

$$
 5t-2\kappa=9.5>8.6059.
$$

It also satisfies `q/D<\pi` and nonnegativity. This is only an asymptotic algebraic
witness; it is not claimed to come from a contact complex, KKT stress, or global
minimizer. Additional current ledgers may impose further constraints.

## 5. Consequence

The claimed `2.0585` endpoint interval is not a valid consequence of the corrected
ledger. This composition supplies no useful C-II narrowing beyond the separate moment
inequality.
The missing step remains geometric: couple the loaded diameter graph to actual cell
routes, or construct a source-preserving strict diameter decrease. No theorem-state
file is changed.
