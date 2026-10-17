<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a3e579df15ece6777a9959141095d976602f697e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_multirhombic_empty_pentagons_extended_range_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7b08b02992f5a3f6f7d845eadae76b89f494b45676f867746778a57b714faa65"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — multi-rhombic empty pentagons persist well beyond the path endpoint

**Date:** 2026-09-15  
**Status:** proof-only scope propagation corollary  
**Scope:** modern Branch R in the canonical full-core Type-II train-measure branch  
**Dependencies:** uniform all-train pentagon extension; modern Branch-R incidence inequality; multi-rhombic pentagon counting lemma; isolate-host face degree-`>=7` theorem  
**Certificate:** `research/verify_target_c_multirhombic_empty_pentagons_extended_range.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The first multi-rhombic pentagon theorem was written on the then-current `t<=1.8623` pentagon interval.  The uniform all-train scope audit shows that this cutoff is artificial.  The same incidence inequalities imply exact wider positivity thresholds.

Let

\[
X_2=\#\{P\in\mathcal P_5:d_R(P)\ge2\},
\qquad
X_3=\#\{P\in\mathcal P_5:d_R(P)\ge3\}.
\]

The finite counting theorem gives

\[
X_2\ge{I_5-Q\over4},
\qquad
X_3\ge{I_5-2Q\over3}.
\tag{MER.1}
\]

Using the uniform endpoint envelopes

\[
P_5/D\ge C_{707}+\pi-{5t\over2}-o(1),
\]

\[
Q/D\le2t-\pi+o(1),
\]

and the Branch-R incidence floor

\[
I_5/D\ge5\left(C_{707}+\pi-{5t\over2}\right)-\tau_0-o(1),
\]

one obtains

\[
\boxed{
\liminf {X_2\over D}
\ge {5C_{707}+6\pi-\tau_0-(29/2)t\over4},
}
\tag{MER.2}
\]

\[
\boxed{
\liminf {X_3\over D}
\ge {5C_{707}+7\pi-\tau_0-(33/2)t\over3}.
}
\tag{MER.3}
\]

Consequently the scalar positivity thresholds are

\[
\boxed{
t<{5C_{707}+6\pi-\tau_0\over29/2}
=1.90789\ldots
\Longrightarrow X_2=\Omega(D),}
\tag{MER.4}
\]

and

\[
\boxed{
t<{5C_{707}+7\pi-\tau_0\over33/2}
=1.86703\ldots
\Longrightarrow X_3=\Omega(D).}
\tag{MER.5}
\]

The exact certificate proves safe lower enclosures `>1.9078` and `>1.8670` respectively.

Representative safe finite endpoints are

\[
\begin{array}{c|c|c}
T & X_2/D\text{ lower} & X_3/D\text{ lower}\\ \hline
1.865 & 0.1518 & 0.0111\\
1.880 & 0.1011 & -\\
1.900 & 0.0286 & -\\
1.905 & 0.0104 & -\\
1.907 & 0.0032 & -.
\end{array}
\tag{MER.6}
\]

Every face counted here is source-empty.  Every `X_3` face contains at least one double-rhombic pentagon corner because three marked sides on a five-cycle cannot be independent.

Thus the local empty-hole structure survives beyond the separately proved O--O path range:

```text
Branch R, t < 1.86703...:
    linear source-empty pentagons with a double-rhombic corner;

Branch R, t < 1.90789...:
    linear source-empty pentagons with at least two strict-rhombus sides;

Branch R, t < 1.96182...:
    linear rhombus/pentagon interface at all;

all full-core, t < 2.02157...:
    linear source-empty pentagon sea.
```

No O--O path theorem is used in these extensions.  They come solely from the uniform all-train gap and exact global face/train bookkeeping.

**Disposition:** proved wider positivity ranges for the multi-rhombic empty-pentagon populations. C-II and Level I remain open.
