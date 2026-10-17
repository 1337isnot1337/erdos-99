> Generated reading edition · [exact source](../../research/target_c_robust_nearcomplete_grid_zero_detour_endpoint_hostile_audit_2026-09-12.md) · source SHA-256 `31c3bd6d9515f1eca08557eb8b7c2d7a28bf468389c2bb6c0155d9ae80f21e09`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9911205bcc0819450e8558310f2e6736ca8b26e3", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_robust_nearcomplete_grid_zero_detour_endpoint_hostile_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "109d8ea74ccf6901662b180e6bda8cada53eb3800ca39571ee161a526feb9b4d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — robust near-complete grid / §154 endpoint exclusion

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_robust_nearcomplete_grid_zero_detour_endpoint_2026-09-12.md`  
**Disposition:** **PASS with one binding repair to Lemma 1.2's proof.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The main theorem survives hostile review. The only defect found is a tie-handling issue
in the source proof of the elementary inversion-threshold lemma. The lemma itself is
correct, and the replacement proof below is binding.

---

## 1. Binding repair: inversion-threshold lemma with ties

The source chooses an “upper quantile” of the `X` values and implicitly assumes a
small quantile block can be separated from ties. A macroscopic repeated value can make
that particular sentence false.

Use the following proof instead.

Let

```math
M:=\#\{(x,y)\in X\times Y:x\ge y\},
\qquad
\epsilon:={M\over |X||Y|}\to0.
```

For each `x in X` define

```math
L(x):=\#\{y\in Y:y\le x\}.
```

Then exactly

```math
\sum_{x\in X}L(x)=M.
\tag{A1.1}
```

Put `delta=sqrt(epsilon)` when `epsilon>0`. Markov gives

```math
\#\{x:L(x)>\delta|Y|\}
\le {M\over\delta|Y|}
=\delta|X|
=o(|X|).
\tag{A1.2}
```

Let

```math
X':=\{x\in X:L(x)\le\delta|Y|\}.
```

If `X'` is nonempty, choose

```math
x_*:=\max X'.
```

Then

```math
\#\{y\in Y:y\le x_*\}=L(x_*)\le\delta|Y|=o(|Y|).
```

Delete those `Y` values and put

```math
Y':=\{y\in Y:y>x_*\}.
```

We have deleted only `o(D)` elements from each side, and

```math
\boxed{\max X'=x_*<\min Y'.}
\tag{A1.3}
```

If `epsilon=0`, simply take `X'=X`, `Y'=Y`; then every `x<y` already. For all
sufficiently large indices with `epsilon>0`, (A1.2) leaves `X'` nonempty because
`delta->0`.

This proves the threshold lemma with arbitrary multiplicities and exact strict
separation. It is stronger and simpler than the quantile wording in the source.

After applying it to

```math
x_u=\alpha_u,
\qquad
y_v=\beta_v-\pi/3,
```

the source's strict condition

```math
\max\alpha_u+\pi/3<\min\beta_v
```

follows exactly.

---

## 2. Audit of the robust order theorem

After phase-tail removal and missing-degree pruning, there is `r_D=o(D)` with

```math
\deg_A(u)\ge|B|-r_D,
\qquad
\deg_B(v)\ge|A|-r_D.
```

For large `D`, every two same-shore trains have a common opposite neighbor and every
three have a common opposite neighbor.

The source defines the order of two `A` trains using any common `B` neighbor. This is
well-defined: two choices `b,b'` produce an actual complete `2 x 2` subgrid, and the
already-audited §76 signed monotone-grid lemma makes the two orders agree. Transitivity
is not inferred abstractly; one common `B` neighbor of any three `A` trains orders all
three on one real line. The same proof applies to `B`.

Therefore choosing the globally first `A` train and its globally last `B` neighbor
genuinely gives a crossing that is first on the `B` train and last on the `A` train.
No global product completeness is hidden here.

---

## 3. Audit of the two-leg projection

The repaired phase separation and shrinking atom width give exactly the §76 angular
hypotheses

```math
\pi/3<\beta_v-\alpha_u<2\pi/3
```

for every retained pair, whether or not that pair physically crosses. Hence the §76
common projection `e_D` is positive on every elementary displacement of every selected
train centerline.

Along the corner `A` train, crossings with unselected trains can occur between two
selected `B` crossings. They only add positive projection. The selected `B` rhombi
contribute the same half-end/full-interior vector sum as §76, so the first leg is at
least

```math
e_D\cdot\sum_{v\in N(u_*)}v-1.
```

The second leg is identical. The two endpoints are centers of actual source rhombi and
therefore belong to `conv(A)`, whose diameter is the source diameter `D`. Thus the
source inequality

```math
D\ge
\sum_{v\in N(u_*)}e_D\cdot v
+
\sum_{u\in N(v_*)}e_D\cdot u-2
```

is valid.

Since the two train-direction clusters shrink to axes at projective separation
`pi/3`, the §76 projection converges to their bisector and

```math
e_D\cdot u,\ e_D\cdot v
\ge\sqrt3/2-o(1)
```
uniformly. The robust leading bound

```math
a+b\le2/\sqrt3
```

therefore survives.

---

## 4. Audit of the endpoint equality structure

Assume zero normalized outer detour and

```math
(q-k)/D\to t_0
=\pi/2+(2/5)s_2.
```

The exact outer ledger gives

```math
Q/D\to(4/5)s_2.
```

Audited §154 gives `(Q+4f)/D>=4s_2-o(1)`, while `f<=Q` gives

```math
Q+4f\le5Q=4s_2D+o(D).
```

Hence the endpoint capacity is exactly saturated and

```math
(Q+4f)/D\to4s_2.
```

For every train-measure subsequential limit, §142 gives `x sigma>=2s_2`, while the
§154 endpoint-count proof gives `2x sigma<=4s_2` from the now-exact bounded endpoint
capacity. Thus

```math
\boxed{x\sigma=2s_2.}
```

Let `A_j` be the absolute atomic train mass in one orbit of the relation
`phi -> phi+pi/3 mod pi`, and let `E_j` be its normalized physical crossing mass.
Then

```math
E_j\le A_j^2/4
```

by triangle-free weighted Mantel, all limiting crossing mass lies on these exact
atomic relation orbits by §142, and

```math
\sum_jE_j=s_2^2,
\qquad
\sum_jA_j=2s_2.
```

Therefore

```math
s_2^2
=\sum_jE_j
\le{1\over4}\sum_jA_j^2
\le{1\over4}\left(\sum_jA_j\right)^2
=s_2^2.
```

Equality throughout forces exactly one positive orbit. This step does not assume a
finite global atom set.

A diagonal choice of shrinking neighborhoods of that orbit retains
`2s_2D+o(D)` trains and `s_2^2D^2-o(D^2)` crossings. The §153 elementary near-Mantel
lemma applies. Same-atom trains cannot cross once the neighborhoods are narrow enough,
so any atom split linearly across the two Mantel shores would contribute `Theta(D^2)`
missing cross pairs. Thus every positive atom belongs asymptotically to one shore.
With at most three atoms and two shores of mass `s_2`, one shore has a single atom of
mass `s_2`, while the other has an atom of mass at least `s_2/2`.

The selected opposite-shore atom pair therefore satisfies the robust theorem with

```math
a+b\ge{3\over2}s_2.
```

Numerically and exactly at the needed sign,

```math
{\sqrt3\over2}{3s_2\over2}
=1.2370906246\ldots>1,
```

giving the contradiction.

---

## 5. Scope

- No contact-isolated coordinate enters the core train or rigidity arguments.
- No local pentagon rigidity, positive per-face Oler slack, or false two-atom collapse
  is assumed.
- Missing train crossings are retained through the `o(D^2)` budget; the proof does not
  silently upgrade near-Mantel to a complete product.
- The conclusion is endpoint unattainability in the zero-detour Type-II class, not a
  complete C-II closure.
- Theorem-state authority remains audit.46 through canonical §123.

**Verdict:** PASS with the replacement proof of Lemma 1.2 above binding.
