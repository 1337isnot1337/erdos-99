> Generated reading edition · [exact source](../../../docs/audits/target_c_explicit_rhombic_train_gap_independent_audit_2026-09-14.md) · source SHA-256 `2d3d0bcddcbbc6de17f136967cbfc187c24ebcf07f33cbe7055852925ad1a6e0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-FFEF3BF5881F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit — explicit rhombic-train Mantel gap

**Date:** 2026-09-14
**Audited artifact:** `research/target_c_explicit_rhombic_train_gap_2026-09-14.md`
**Repository base audited:** `fa39e093`
**Target:** Target C-II, canonical full-core Type-II branch
**Verdict:** **PASS at proof-only scope.** The explicit `0.0008 D` rhombic-train isoperimetric gap is valid. C-II and Level I remain open.

## 1. The notation repair is necessary

The older post-endpoint notes used `T=B_4/2` while audited §142 uses `T` for **all**
complete stopped trains, including singleton trains. Read literally with §142 notation,
`B_4=2T` is false in the presence of singleton trains. The audited artifact repairs
this by writing

$$
T_R:=B_4/2,
\qquad
T=T_R+S,
\tag{A.1}
$$

where `S` is the number of singleton stopped trains. All quantitative Mantel statements
in the audited artifact concern `T_R`, not the all-train count `T`.

This distinction is not cosmetic. It is the reason the recipient vacancy has the exact
interpretation

$$
\rho_{\rm rec}=b+4f+Q-B_4=2S.
\tag{A.2}
$$

## 2. Exact finite train bookkeeping

Use the canonical §142 auxiliary forest `Xi`: its vertices are positive contact edges
and each strict rhombus adds the two links joining opposite sides. Every component is a
path. A component is either

1. a singleton vertex, corresponding to a contact edge incident to no strict rhombus; or
2. a non-singleton path containing at least one strict-rhombus link.

For a non-singleton component, the two endpoints of the path are exactly the two
contact-edge occurrences incident to one strict rhombus on one side and no strict
rhombus on the other. Hence every non-singleton train contributes exactly two
occurrences to the physical boundary of the complete strict-rhombus complex, including
hole and component boundaries. Conversely every occurrence counted by `B_4` is one
endpoint occurrence of a unique non-singleton train. Therefore

$$
\boxed{B_4=2T_R.}
\tag{A.3}
$$

Audited §143 gives the all-train endpoint handshake

$$
b+4f+Q=2T.
\tag{A.4}
$$

Subtracting (A.3) from (A.4) and using (A.1) proves (A.2). It also gives the exact
split

$$
\tau_D=(q-k)+2f-2\sqrt{R_4}
=S+{\sigma_R\over2},
\qquad
\sigma_R:=B_4-4\sqrt{R_4}.
\tag{A.5}
$$

No outer-face injectivity or disk topology is used.

## 3. Restricting to rhombic trains loses no crossing mass

Let `G_R` have the `T_R` non-singleton trains as vertices and one edge for every strict
rhombus. Every strict rhombus lies at the crossing of its two opposite-direction train
components, and singleton trains cross no strict rhombus. Thus

$$
\boxed{e(G_R)=R_4.}
\tag{A.6}
$$

The canonical §142 proof that the stopped-train crossing graph is simple and
triangle-free applies verbatim to the induced non-singleton graph. Hence `G_R` is simple
and triangle-free.

In the full-core Type-II branch,

$$
R_4/D^2\to\Delta_2:=\pi/(2\sqrt3).
\tag{A.7}
$$

Mantel gives `T_R>=2sqrt(R_4)=Theta(D)`, while (A.3) and the canonical recipient bound
`B_4<=b+4f+Q=O(D)` give `T_R=O(D)`. Therefore `T_R=Theta(D)` and the empirical
direction measures on `G_R` have the same compactness scale used in §§164/168.

For every fixed `epsilon>0`, the global strict-rhombus angular-defect estimate says that
only `o(D^2)=o(T_R^2)` strict-rhombus crossings have direction separation at least
`pi/3+epsilon`. Because every edge of `G_R` is a strict rhombus, every normalized
crossing-measure limit for `G_R` is supported on the exact `+-pi/3` relation.
Simplicity gives domination by the product of the restricted empirical train measure.
Thus, if `M_r` and `E_r` are the `D`-normalized atomic train mass and crossing mass in
one exact three-direction orbit,

$$
E_r\le {M_r^2\over4},
\qquad
\sum_r E_r=\Delta_2.
\tag{A.8}
$$

These are precisely the inputs to the quantitative atomic part of audited §168.

## 4. The §168 robust-grid argument really is restriction-stable

The potentially dangerous point is whether audited §168.1--§168.4 secretly uses the
all-train exposed-hull inequality. It does not.

The proof up through the opposite-corner contradiction uses only:

- the total crossing mass `Delta_2`;
- the orbit capacities (A.8);
- finite triangle-free Mantel stability;
- the fact that trains in one sufficiently narrow direction window cannot cross;
- the §163 near-complete-grid theorem on actual complete stopped trains; and
- the fact that the endpoints of the §163 two-leg path are centers of actual source
  rhombi in the full source convex hull.

Every non-singleton rhombic train is a complete stopped train in the §142 sense, so the
§163 theorem applies to selected families from `G_R`. The §163 path uses only actual
strict-rhombus crossings between those selected trains; singleton trains never enter
its order or its path. Holes, defect faces, and omitted trains cannot shorten the common
projection, exactly as in the audited §163 proof.

The exposed-hull relation `q/T<=2(1-s)` first enters only in §168.5, when the atomic
gain is propagated back to the **all-train** ledger. The audited artifact does not use
that propagation to prove the rhombic-only gain.

Therefore the same explicit contradiction constant from §168 applies to `G_R`:

$$
A_R:=x_Rs_R\ge2\sqrt{\Delta_2}+0.0004,
\tag{A.9}
$$

where `x_R=lim T_R/D` on an arbitrary convergent subsequence and `s_R<=1` is the
total atomic mass of the restricted limit. Hence

$$
\boxed{
\liminf {T_R\over D}\ge2\sqrt{\Delta_2}+0.0004.
}
\tag{A.10}
$$

## 5. Explicit consequences

Using `B_4=2T_R`, (A.7), and (A.10),

$$
\sigma_R=2T_R-4\sqrt{R_4}
$$

gives

$$
\boxed{
\liminf {\sigma_R\over D}\ge0.0008.
}
\tag{A.11}
$$

For

$$
M_R={T_R^2\over4}-R_4,
$$

the exact rationalization is

$$
M_R={\sigma_R(T_R+2\sqrt{R_4})\over8}.
\tag{A.12}
$$

All factors are nonnegative. Taking lower limits in (A.12) using (A.7), (A.10), and
(A.11) yields

$$
\boxed{
\liminf {M_R\over D^2}
\ge0.0001\left(4\sqrt{\Delta_2}+0.0004\right)
=0.0003809651227455\ldots .
}
\tag{A.13}
$$

The post-endpoint identity

$$
\begin{aligned}
\mu_DD={}&{2P_F+2\sqrt{R_4}\over5}
+m_B+{2\over5}(Q-f)+{2\over5}(b-P_F)\\
&+{1\over10}\rho_{\rm rec}+{1\over10}\sigma_R-2c_I-4
\end{aligned}
\tag{A.14}
$$

is just the already-proved exact two-currency split after the notation repair
`rho_rec=2S`. Since every displayed defect currency is nonnegative, (A.11) indeed adds
`0.00008` to the proof-only asymptotic `mu_D` floor.

Likewise canonical Section 85 gives the finite stronger form

$$
A_{ch}-a_0Z_{ch}\ge{3c_0\over5}(B_4-P_F).
\tag{A.15}
$$

Substituting `B_4=4sqrt(R_4)+sigma_R` proves the stated extra chamber-surplus term
`(3c_0/5)(0.0008)D-o(D)` and the corresponding `0.00024D-o(D)` Oler-slack increment.

## 6. What is and is not established

The explicit rhombic gap is a real advance: the full-core branch is uniformly separated
from rhombic Mantel extremality at both linear train-boundary and quadratic crossing
scales. But it is not a closing contradiction. Canonical Section 85 already warns that
linear train-boundary excess can be stored in thin corridors with only linear Euclidean
area, so (A.11) cannot be converted into a quadratic packing contradiction by generic
isoperimetry.

The next live problem is to make the two exact excess mechanisms

$$
T-2\sqrt{R_4}=S+{\sigma_R\over2}
$$

pay different source-level currencies: singleton trains have no rhombic crossing at all,
while `sigma_R` is a genuine quadratic crossing-capacity deficit. Any closure attempt
that merges them back into one scalar `tau_D` discards the new information.

**Final disposition:** PASS at audited-working proof-only scope. The notation correction
`T_R` versus all-train `T` is binding for future use. No theorem-state promotion is
made here.
