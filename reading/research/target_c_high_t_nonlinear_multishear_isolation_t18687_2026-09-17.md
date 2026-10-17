> Generated reading edition · [exact source](../../research/target_c_high_t_nonlinear_multishear_isolation_t18687_2026-09-17.md) · source SHA-256 `5f6a9f8477036ff578936a8a83edbd8b530e82b5b6ee57737d6969cf5ea6a6f6`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bfc22d75d8ffac32ab499c92161a92870c363e52", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_nonlinear_multishear_isolation_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a06aaafb1936149a5264316b3b3115515cbcf0ba40f3643e4e9a2799e703aa71"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the entire high-`t` exact laminar multishear family is locally diameter-isolated

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** canonical C65-normalized full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** exact finite laminar multishear; complete high-`t` multishear cusp localization; one-sided interval support; exact KKT weighted first-variation identity; canonical C67/DB.3 parallel-diameter uniqueness; response-free two-sided bracing of every outer train  
**Certificate:** `research/verify_target_c_high_t_nonlinear_multishear_isolation_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The complete multishear cusp theorem proves a first-order statement: every nonzero tangent that cancels the full-support diameter displacement has actual diameter rows of both derivative signs, including at exact phase-equality blocks. Two possible loopholes remained in the wording of the frontier: perhaps a nonlinear curve on the exact cancellation set could evade the tangent obstruction, or perhaps a noncancelling curve could move the persistent diameter core and stay diameter-feasible.

Neither loophole survives.

The finite exact shear map is analytic. Compactness of normalized shear directions upgrades the tangent sign-cusp theorem to a **finite nonlinear local-isolation theorem** on the exact and near-cancellation sets. More generally, positive KKT stationarity shows that any local diameter-feasible shear would force the persistent full-span diameter support to consist of a **single actual diameter edge**. But the first selected high-`t` row is an outer-to-outer train, and the already-proved response-free bracing theorem forces at least two distinct crossing actual diameter edges. Since the one-sided chain has persistent set `P=H_0`, the singleton branch is impossible.

Therefore the original source is locally diameter-isolated inside the **entire exact laminar multishear family**, with no cancellation condition. Exact cancellation, near-cancellation, pure second-order persistent-core drift, and first-order noncancelling persistent-core motion are all closed as local deformation routes.

---

## 1. Exact finite setup

Fix `r>=2` and `r+1` consecutive selected high-`t` rows

```math
\tau_0,\ldots,\tau_r
```

on one side of the common diameter-routing hub, with coherent real unit shore vectors

```math
u_0,\ldots,u_r.
```

For `theta=(theta_0,...,theta_r)`, put

```math
\Delta_j(\theta_j):=R_{\theta_j}u_j-u_j
```

and define the exact full-support displacement

```math
\boxed{
G(\theta):=\sum_{j=0}^r\Delta_j(\theta_j).
}
\tag{NL.1}
```

The exact laminar multishear preserves every old unit contact for every `theta`, and all strict old noncontacts remain strict for sufficiently small `theta`.

Let `H` be the finite set of actual diameter edges of the source. For each `h in H`, let

```math
\Phi_h(\theta):=|r_h(\theta)|^2-D^2,
\qquad
\Phi_h(0)=0,
\tag{NL.2}
```

and write its first variation as the linear functional

```math
\ell_h(c):=D\Phi_h(0)[c].
\tag{NL.3}
```

The derivative of the full-support map is

```math
DG(0)[c]
=J\sum_{j=0}^r c_ju_j.
\tag{NL.4}
```

Hence its first-order cancellation space is

```math
\mathcal K
:=\ker DG(0)
=\left\{c:\sum_jc_ju_j=0\right\}.
\tag{NL.5}
```

The complete multishear cusp theorem says that for every nonzero `c in K`,

```math
\boxed{
\max_{h\in H}\ell_h(c)>0,
\qquad
\min_{h\in H}\ell_h(c)<0.
}
\tag{NL.6}
```

The witnesses may be chosen among the switching actual diameter edges in the selected block.

---

## 2. The tangent cusp has a uniform gap on normalized cancellation directions

Put

```math
S_{\mathcal K}:=\{c\in\mathcal K:\|c\|_2=1\}.
```

Because `H` is finite, the functions

```math
M_+(c):=\max_{h\in H}\ell_h(c),
\qquad
M_-(c):=-\min_{h\in H}\ell_h(c)
\tag{NL.7}
```

are continuous. Equation (NL.6) makes both strictly positive on the compact set `S_K`. Therefore

```math
\boxed{
\eta_0
:=\min_{c\in S_{\mathcal K}}
\min\{M_+(c),M_-(c)\}>0.
}
\tag{NL.8}
```

This constant is source- and block-dependent; no uniform lower bound in `D` is claimed. Its role is local: on one fixed finite source, the first-order sign cusp cannot collapse along a sequence of normalized exact-cancellation directions.

---

## 3. Exact cancellation is nonlinearly diameter-isolated

### Theorem NL-A — finite nonlinear sign cusp

There are constants `epsilon>0` and `eta>0`, depending on the fixed source and selected block, such that every nonzero `theta` satisfying

```math
\|\theta\|_2<\varepsilon,
\qquad
G(\theta)=0
\tag{NL.9}
```

obeys

```math
\boxed{
\max_{h\in H}\Phi_h(\theta)
\ge\eta\|\theta\|_2,
\qquad
\min_{h\in H}\Phi_h(\theta)
\le-\eta\|\theta\|_2.
}
\tag{NL.10}
```

In particular, the origin is an isolated point of

```math
\{\theta:G(\theta)=0,\ \Phi_h(\theta)\le0\text{ for every }h\in H\}.
\tag{NL.11}
```

So there is no nonconstant exact full-support cancellation deformation, of any differentiability class, that remains inside the diameter-`D` feasible set near the original source.

### Proof

If the positive half of (NL.10) failed, there would be nonzero exact-cancellation states

```math
\theta^{(n)}\to0
```

such that, with

```math
\rho_n:=\|\theta^{(n)}\|_2,
\qquad
c^{(n)}:={\theta^{(n)}\over\rho_n},
```

one has

```math
{1\over\rho_n}
\max_h\Phi_h(\theta^{(n)})\to0
```

along a subsequence after weakening to an upper bound tending to zero if necessary.

The unit sphere is compact, so pass to a subsequence with

```math
c^{(n)}\to c,
\qquad \|c\|_2=1.
\tag{NL.12}
```

Taylor expansion of (NL.1) gives

```math
G(\theta)
=DG(0)[\theta]+O(\|\theta\|_2^2).
\tag{NL.13}
```

Since `G(theta^(n))=0`, division by `rho_n` and passage to the limit yield

```math
DG(0)[c]=0,
\qquad c\in S_{\mathcal K}.
\tag{NL.14}
```

For every fixed actual diameter row,

```math
\Phi_h(\theta)
=\ell_h(\theta)+O(\|\theta\|_2^2).
\tag{NL.15}
```

There are only finitely many rows, so the remainder is uniform over `H`. Dividing by `rho_n` gives

```math
{\Phi_h(\theta^{(n)})\over\rho_n}
\longrightarrow\ell_h(c)
\qquad(h\in H).
\tag{NL.16}
```

Thus the assumed failure forces

```math
\max_h\ell_h(c)\le0,
```

contradicting (NL.6), or quantitatively (NL.8). The negative half is identical after applying the argument to `-min_h Phi_h`.

This proves (NL.10).

The proof is sequential and therefore does not require a smooth parametrization of `G^{-1}(0)`. It also covers flat paths whose first several derivatives at the origin vanish.

---

## 4. Near-cancellation cannot rescue the diameter constraints

The same compactness argument does not require exact cancellation.

### Theorem NL-B — linear persistent-core escape lower bound

There exist

```math
\varepsilon>0,
\qquad
\kappa>0
\tag{NL.17}
```

such that every nonzero small shear satisfying all active diameter inequalities

```math
0<\|\theta\|_2<\varepsilon,
\qquad
\Phi_h(\theta)\le0
\quad(h\in H)
\tag{NL.18}
```

must satisfy

```math
\boxed{
\|G(\theta)\|\ge\kappa\|\theta\|_2.
}
\tag{NL.19}
```

### Proof

If not, there is a sequence of diameter-feasible nonzero shears `theta^(n)->0` with

```math
{\|G(\theta^{(n)})\|\over\|\theta^{(n)}\|_2}\to0.
\tag{NL.20}
```

Normalize exactly as above. After taking a subsequence,

```math
c^{(n)}\to c,
\qquad\|c\|_2=1.
```

Equations (NL.13) and (NL.20) imply

```math
DG(0)[c]=0,
\qquad c\in\mathcal K.
\tag{NL.21}
```

Diameter feasibility and (NL.15) imply, for every `h`,

```math
\ell_h(c)\le0.
\tag{NL.22}
```

This contradicts the positive half of (NL.6).

Therefore (NL.19) holds.

### Consequence

Any proposed deformation in this exact contact-preserving shear family with

```math
G(\theta)=o(\|\theta\|_2)
\tag{NL.23}
```

is diameter-infeasible for all sufficiently small nonzero states. In particular,

```math
G(\theta)=O(\|\theta\|_2^2)
```

cannot provide a second-order escape.

This removes the apparent loophole left by the blockwise second-order cancellation identity. The quadratic charges in the critical phase-block calculation remain correct, but **inside the exact or near-exact full-support cancellation family they cannot overcome the already-uniform linear diameter cusp**.

Thus “second-order antipodal curvature” is not an independent closing route inside this exact shear family unless the deformation also moves the persistent diameter core at first order.

---

## 5. Positive KKT stationarity forces a singleton persistent support for any local escape

Orient the selected one-sided chain toward the hub so the active diameter supports are nested, and let

```math
P=\bigcap_jH_j=H_0
\tag{NL.24}
```

be the nonempty persistent set of actual diameter bars crossing every selected row. Give each `h in P` its signed unit direction

```math
v_h={\varepsilon_h r_h\over D},
\qquad |v_h|=1,
\tag{NL.25}
```

where `epsilon_h` is its common rooted cut-incidence sign.

### Theorem NL-C — singleton necessary condition

If there is a sequence of nonzero shears

```math
\theta^{(n)}\to0
\tag{NL.26}
```

for which every actual diameter remains at most `D`, then necessarily

```math
\boxed{|P|=1.}
\tag{NL.27}
```

### Proof

Normalize a hypothetical feasible sequence and pass to

```math
c^{(n)}\to c,
\qquad\|c\|_2=1.
\tag{NL.28}
```

As above, diameter feasibility gives

```math
\ell_h(c)\le0
\qquad(h\in H).
\tag{NL.29}
```

The exact KKT weighted first-variation identity holds for every shear direction:

```math
\boxed{
\sum_{h\in H}\beta_h\ell_h(c)=0.
}
\tag{NL.30}
```

C65 supplies

```math
\beta_h>0
\qquad(h\in H).
\tag{NL.31}
```

Therefore (NL.29)--(NL.31) force

```math
\boxed{
\ell_h(c)=0
\qquad\text{for every actual diameter edge }h.
}
\tag{NL.32}
```

Put

```math
g:=DG(0)[c]
=J\sum_jc_ju_j.
\tag{NL.33}
```

If `g=0`, then `c in K`, and the complete multishear cusp theorem contradicts (NL.32). Hence

```math
\boxed{g\ne0.}
\tag{NL.34}
```

For a persistent bar, the first relative displacement is `epsilon_h g`. Consequently

```math
\ell_h(c)
=2r_h\cdot(\varepsilon_hg)
=2D v_h\cdot g.
\tag{NL.35}
```

By (NL.32),

```math
v_h\cdot g=0
\qquad(h\in P).
\tag{NL.36}
```

Since `g` is nonzero in the plane, every `v_h` lies on the same one-dimensional line `g^perp`. Thus every persistent actual diameter edge has the same projective direction.

Canonical C67/DB.3 parallel-diameter uniqueness says two distinct actual diameter edges cannot have the same projective direction. Hence

```math
|P|\le1.
```

The first cut resultant is nonzero (`A_0>0`), so `H_0=P` is nonempty. Therefore `|P|=1`.

---

## 6. Outer-train bracing kills the singleton branch

The singleton necessary condition is incompatible with the geometry already proved for every outer train.

The first selected row `tau_0` is a complete outer-to-outer stopped train. The response-free two-sided bracing theorem says that its crossing actual diameter edges contain two edges `h_+,h_-` satisfying

```math
\boxed{
r_{h_+}\cdot Ju_0>0,
\qquad
r_{h_-}\cdot Ju_0<0.
}
\tag{NL.37}
```

In particular `h_+` and `h_-` are distinct. By definition, the set of actual diameter edges crossing the first selected cut is `H_0`. The one-sided orientation toward the hub gives

```math
\boxed{P=H_0.}
\tag{NL.38}
```

Therefore

```math
\boxed{|P|\ge2.}
\tag{NL.39}
```

This contradicts the necessary condition (NL.27) for any local diameter-feasible nonzero shear sequence.

### Theorem NL-D — complete local isolation in the exact laminar family

There exists `epsilon>0`, depending on the fixed source and selected row block, such that

```math
\boxed{
0<\|\theta\|_2<\varepsilon
\quad\Longrightarrow\quad
\max_{h\in H}\Phi_h(\theta)>0.
}
\tag{NL.40}
```

Equivalently, every sufficiently small nontrivial exact laminar multishear makes at least one old actual diameter edge strictly longer than `D`.

### Proof

If no such `epsilon` existed, there would be a sequence of nonzero shears `theta^(n)->0` for which every actual diameter remained at most `D`. Theorem NL-C would force `|P|=1`, while (NL.37)--(NL.39) force `|P|>=2`. Contradiction.

Thus the original source is a locally isolated diameter-`D` point of the entire selected exact laminar multishear family.

---

## 7. Persistent-stress consequences

The persistent-stress theorem defines

```math
p_D:=\sum_{h\in P_D}\beta_h,
\qquad
V_D:=\sum_{h\in P_D}\beta_hv_h,
\qquad
a_D:=\|V_D\|.
\tag{NL.41}
```

Before the bracing input, Theorem NL-C reduced a hypothetical local shear escape to the singleton condition

```math
P_D=\{h_*\},
```

which would imply

```math
p_D=a_D=\beta_{h_*}
```

and zero persistent directional dispersion. The response-free bracing theorem rules this possibility out at the first selected row. Therefore **none** of the persistent-stress regimes supports a local diameter-feasible deformation inside the exact laminar shear family.

This does not make the persistent-stress results obsolete. Their endpoint and variance structure can still feed a global diameter-thrackle contradiction or a finite nonlocal competitor. The point here is narrower: they cannot be converted into a small exact-laminar-shear escape.

---

## 8. Frontier effect

The following local deformation routes are now closed inside the exact laminar multishear family:

```text
nonzero exact full-support cancellation curve;
near-cancellation with G(theta)=o(||theta||);
pure second-order persistent-core drift;
noncancelling first-order persistent-core motion;
any other sufficiently small nontrivial exact laminar multishear.
```

So a source-preserving deformation proof of high-`t` C-II cannot come from taking a smaller parameter in the already-built laminar rotation family. It must either

1. leave this finite exact shear family by changing contact combinatorics or using a genuinely different source motion;
2. use a finite nonlocal move not connected to the identity through diameter-feasible exact shears;
3. derive an exact unit triangle; or
4. finish a global contradiction from the ordered diameter-thrackle / common-ladder / exact-antipodal-or-strong-TB1 structure.

The exact-antipodal/strong-TB1 endpoint-order route therefore becomes the cleanest continuation of the current high-`t` program. This report does not supply that final global contradiction.

No C-II closure is claimed here, and the macroscopic-container branch is untouched.

---

## 9. Scope audit

- All constants `eta`, `epsilon`, and `kappa` are finite-source constants. No uniform asymptotic lower bound is claimed.
- The nonlinear arguments use the finite set of actual diameter rows and ordinary Taylor expansion of the exact finite rotation formulas; no hidden smoothness of a candidate path is needed.
- NL-A and NL-B require the complete first-order multishear sign-cusp theorem at the selected block.
- NL-C uses full positive actual-diameter KKT visibility from C65. Nonnegative weights with zero-weight active rows would not suffice.
- The singleton conclusion uses the one-sided persistent-set identification `P=H_0` and canonical parallel-diameter uniqueness.
- NL-D uses the independent response-free two-sided bracing theorem for the outer train `tau_0`; it does not infer bracing from the multishear cusp theorem itself.
- Local isolation does not exclude a finite nonlocal competitor, a motion outside the exact laminar shear family, an exact triangle, or a global combinatorial contradiction.
- The report is proof-only. It does not alter the canonical theorem state or the active Target C prompt.

**Disposition:** proved nonlinear local diameter isolation of the complete high-`t` exact laminar multishear family. Exact/near cancellation, second-order drift, and noncancelling local persistent-core escapes are all closed. C-II and Level I remain open.
