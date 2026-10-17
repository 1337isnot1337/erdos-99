> Generated reading edition · [exact source](../../research/target_c_high_t_complete_rectangle_t18687_2026-09-15.md) · source SHA-256 `f3876c6fef66762064b2fd4c129d2c7d26afea43af6925727f5a284d383e066e`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "55e62dc4e5f053a4e2898c5ec558470bc4b7006e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_complete_rectangle_t18687_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7093b61cc289f997c250ca5e287cedd495ff335ae36dee42e2e5afb1a442e02f"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — a complete linear-by-linear train rectangle through `t<=1.8687`

**Date:** 2026-09-15  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** coupled paired-remainder O--O path through `1.8687`; audited train-length/terminal-energy inequality; exact stopped-train crossing topology and train ledger  
**Certificate:** `research/verify_target_c_high_t_complete_rectangle_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current high-`t` path theorem gives more than `0.0002038D-o(D)` pairwise-disjoint low-energy outer-to-outer trains in one shrinking dominant phase window. Each of those trains is itself macroscopic in the train-crossing graph. The missing observation is that every arbitrary complete train meets a **contiguous interval** of the selected path. A one-sided endpoint average then produces a genuine complete bipartite rectangle.

There exist train families

```math
A_*,B_*
```

such that

```math
\boxed{|A_*|>0.0000226D-o(D),}
\tag{HR.1}
```

```math
\boxed{|B_*|>0.3134D-o(D),}
\tag{HR.2}
```

with the following exact properties:

1. every train in `A_*` crosses every train in `B_*` in one strict rhombus;
2. the trains in `A_*` are pairwise noncrossing;
3. the trains in `B_*` are pairwise noncrossing;
4. `A_*` is one consecutive block of the live O--O complement-dual path.

Thus the live high-`t` branch contains an actual train-crossing

```math
\boxed{K_{|A_*|,|B_*|}}
```

with both shores linear in `D`, not merely a two-row ladder.

---

## 1. Every selected path train has more than `0.6536D` crossing neighbors

Let `tau` be one selected O--O path train. The coupled paired-remainder theorem selects it with

```math
e_\tau\le \lambda(\delta),
\qquad
\lambda(\delta)=0.5857-\delta.
\tag{HR.3}
```

The audited complement train rhombus-incidence theorem writes `r_tau` for the number of strict rhombi traversed by the stopped train and proves

```math
{r_\tau\over D}
\ge1-\delta-{e_\tau\over2}-o(1).
\tag{HR.4}
```

Hence

```math
{r_\tau\over D}
\ge1-{0.5857\over2}-{\delta\over2}-o(1).
\tag{HR.5}
```

At `t<=1.8687`, the matched atomic floor gives

```math
\delta<0.107+o(1).
```

Therefore

```math
\boxed{r_\tau>0.6536D-o(D).}
\tag{HR.6}
```

Each rhombus on `tau` is one crossing with another complete stopped train, and two distinct complete trains meet in at most one strict rhombus. Thus

```math
\boxed{|\Gamma(\tau)|=r_\tau>0.6536D-o(D),}
\tag{HR.7}
```

where `Gamma(tau)` is the crossing neighborhood of `tau` in the complete-train crossing graph.

---

## 2. Any complete train crosses one interval of the selected path

Write the selected O--O path as

```math
\tau_1,\ldots,\tau_m,
\qquad
m>0.0002038D-o(D).
\tag{HR.8}
```

Its pairwise-disjoint proper crosscuts have complement dual

```math
R_0-\tau_1-R_1-\tau_2-\cdots-\tau_m-R_m.
```

Take any other complete stopped train `sigma`. Its midpoint path is connected. Whenever `sigma` crosses one selected train `tau_j`, it moves across the corresponding edge of this complement-dual path. Two complete trains meet at most once, so `sigma` cannot cross the same selected edge twice.

Consequently the dual-region sequence traced by `sigma` is a trail in a path graph. Every trail in a path graph is monotone; its used edges form one consecutive interval. Therefore

```math
\boxed{
I_\sigma:=\{j:\sigma\text{ crosses }\tau_j\}
\text{ is empty or a consecutive interval.}
}
\tag{HR.9}
```

This is a finite source-level statement and does not require `sigma` to be outer-to-outer.

---

## 3. Only `3.0605D` complete train intervals are available

Let `T_tr` be the total number of complete stopped trains, including singleton trains. The exact stopped-train ledger gives

```math
T_{tr}=tD+2f.
\tag{HR.10}
```

Also

```math
f\le Q,
\qquad
{Q\over D}\le2t-\pi+o(1).
```

Hence, uniformly for `t<=T=1.8687`,

```math
{T_{tr}\over D}
\le5T-2\pi+o(1).
\tag{HR.11}
```

The exact Machin-arithmetic certificate proves

```math
\boxed{T_{tr}<3.0605D+o(D).}
\tag{HR.12}
```

Every nonempty interval `I_sigma` has one right endpoint on the selected path. Therefore the total number of right endpoints, counted with train multiplicity, is at most `T_tr`.

---

## 4. Nine-block right-endpoint averaging

Partition the selected path indices into nine consecutive blocks of sizes differing by at most one. By (HR.8), every block has

```math
>{0.0002038\over9}D-o(D)
>0.0000226D-o(D)
\tag{HR.13}
```

selected trains.

Assign each nonempty crossing interval `I_sigma` to the block containing its right endpoint. By (HR.12), some block `J` contains fewer than

```math
{3.0605\over9}D+o(D)
```

right endpoints.

Let `tau_a` be the first selected train of `J`. By (HR.7), more than

```math
0.6536D-o(D)
```

complete trains cross `tau_a`.

If such a train fails to cross every selected train in `J`, its interval starts no later than `a` but ends before the last index of `J`. Its unique right endpoint therefore lies in `J`. Hence at most the right-endpoint population of `J` can fail to cover the entire block.

It follows that the family

```math
B_*:=\bigcap_{j\in J}\Gamma(\tau_j)
```

satisfies

```math
|B_*|
>\left(0.6536-{3.0605\over9}\right)D-o(D)
>0.3134D-o(D).
\tag{HR.14}
```

Take

```math
A_*:=\{\tau_j:j\in J\}.
```

Equations (HR.13)--(HR.14) prove (HR.1)--(HR.2), and by construction every `A_* x B_*` pair crosses.

---

## 5. Both rectangle shores are internally noncrossing

The `A_*` trains are a subfamily of the selected same-window O--O path and are pairwise noncrossing.

Take distinct `sigma,rho in B_*`. Both cross `tau_a`. If `sigma` and `rho` crossed one another, then

```math
\tau_a,\sigma,\rho
```

would be three pairwise-crossing complete trains. This is impossible because the audited complete-train crossing graph is triangle-free.

Therefore

```math
\boxed{B_*\text{ is pairwise noncrossing.}}
\tag{HR.15}
```

Thus the rectangle is a true two-family pseudoline grid: every cross-pair meets exactly once and neither shore has an internal crossing.

---

## 6. Frontier effect

The current high-`t` object is now much more rigid than the finite-strip statement alone:

```text
1.844 < t <= 1.8687:
  one shrinking-phase O-O path of >0.0002038 D trains;
  one consecutive row block A_* with >0.0000226 D trains;
  one transverse family B_* with >0.3134 D trains;
  every A_* x B_* pair is one strict rhombus;
  both A_* and B_* are internally noncrossing.
```

The next step is to spend the global `O(D)` strict-rhombus angular-defect budget on this `Theta(D^2)` complete rectangle. That forces an oriented subrectangle with inverse-`D` phase width and common crossing order.

No C-II or Level-I closure is claimed here.

**Disposition:** proved proof-only complete linear-by-linear high-`t` train rectangle through `t<=1.8687`. C-II and Level I remain open.
