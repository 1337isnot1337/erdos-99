> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_same_face_train_shear_2026-09-09.md) · source SHA-256 `a02185c533a9560b7fb4ae5475f17fe24dfee4ef6695b1e7476e23cc4be42725`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 6 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-3CC1B1CE4372","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZSF: any stopped train with both endpoints on one face is an exact global shear

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-weak-transverse-train`  
**Base:** stacked on PR #111 / ZGS  
**Run type:** exact extension of global train shears to bounded stopping faces  
**Target:** ZRC/ZPL hole-ending train branch  
**Depends on:** DT, C51, ZGS, ZK  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZGS proves that a stopped train with both endpoints on the global outer face is an exact contact-cut shear. The same proof works when both endpoints lie on one bounded nonquadrilateral face.

C51 makes every bounded face a strict convex polygon with empty interior relative to the embedded contact graph. The train midpoint arc can therefore be closed by an arc inside that face. The resulting Jordan curve crosses the contact graph exactly in the train's parallel contact edges.

Hence every **same-face train** — outer/outer or `F/F` for one bounded nonquadrilateral face `F` — is a genuine global contact cut. Rotating its common cut-edge direction preserves every actual contact length exactly, and the complete ZGS strict response / negative weighted diameter-curvature / two-sided cusp conclusions apply verbatim.

This reduces the ZPL hole-ending obstruction: only trains whose two endpoints lie on **different** stopping faces remain merely component-local train flexes.

---

## 1. Bounded stopping faces are empty convex regions

Let `F` be a bounded nonquadrilateral face of the complete positive contact graph.

C51 proves every bounded face is a strict convex polygon. In particular

- its boundary is a simple polygonal cycle;
- its open interior contains no contact-graph vertex or edge;
- any two interior points can be joined by an arc contained in the open face.

Let `tau` be a stopped train whose two endpoint contact edges `e_-,e_+` are both incident to `F`.

DT gives a simple train midpoint path `gamma_tau` from the midpoint of `e_-` to the midpoint of `e_+`. Its interior lies in the union of strict rhombi traversed by `tau`, and it intersects the contact graph only at midpoints of train contact edges.

---

## 2. Close the train through the bounded face

Choose a simple arc

```math
\eta_F
```

inside the open face `F` joining the endpoint midpoints. Near each endpoint it approaches from the `F` side of the corresponding contact edge.

Because the interior of `F` is disjoint from the contact graph,

```math
\eta_F
```

meets no contact edge except at its two endpoint midpoints.

The union

```math
\Gamma_\tau:=\gamma_\tau\cup\eta_F
```

is a simple closed curve after an arbitrarily small smoothing at the endpoint midpoints. DT excludes self-intersection of `gamma_tau`, and the closing arc lies in a face disjoint from the rhombic train interior.

No source vertex lies on `Gamma_tau`.

Let

```math
S_\tau,T_\tau
```

be the two Jordan shores.

Exactly as in ZGS, a contact edge joins the two shores iff it crosses `Gamma_tau`. The only such intersections are the train contact-edge midpoints. Therefore

```math
\boxed{
\delta_C(S_\tau)=E(\tau).
}
\tag{ZSF1}
```

The same conclusion holds for outer/outer trains by the original ZGS outer-face closure.

---

## 3. Exact finite global shear

Orient the train so every cut contact vector from `T_tau` to `S_tau` equals one fixed unit vector `u_tau`. This consistency is the same DT orientation used in ZGS.

For real `theta`, put

```math
\Delta_\theta:=R_\theta u_\tau-u_\tau
```

and translate every source point in `S_tau` by `Delta_theta`, leaving `T_tau` fixed.

Every same-shore contact is unchanged. Every cut contact vector becomes

```math
u_\tau+\Delta_\theta=R_\theta u_\tau,
```

still of length one.

Thus:

### Theorem ZSF.1 — same-face exact train shear

If the two endpoints of a stopped train lie on one common face of the complete contact graph — the outer face or one bounded nonquadrilateral face — then rotating that train direction is realized by a finite global shore translation preserving every actual contact length exactly.

For sufficiently small `theta`, all strict noncontact lower-distance constraints remain strict.

---

## 4. KKT resultant and strict cut sandwich

Define

```math
A_\tau:=\sum_{e\in\tau}\alpha_e.
```

Summing KKT equilibrium over one Jordan shore gives

```math
\boxed{
A_\tau u_\tau
=
\sum_{h\pitchfork\tau}\beta_h r_h.
}
\tag{ZSF2}
```

The right side is nonzero, so both shores contain actual diameter terminals and the induced terminal cut is nontrivial.

Put

```math
w_\tau:=\sum_{h\pitchfork\tau}\beta_h,
\qquad
C_\tau:=\sum_{b\in B_S,k\in B_T}c_{bk}.
```

ZK strict all-cut response gives

```math
C_\tau>w_\tau.
```

The piecewise-constant voltage test on the two Jordan shores gives

```math
C_\tau\le A_\tau.
```

The resultant norm gives

```math
A_\tau\le Dw_\tau.
```

Hence every same-face train satisfies

```math
\boxed{
 w_\tau<C_\tau\le A_\tau\le Dw_\tau.
}
\tag{ZSF3}
```

---

## 5. Exact negative weighted diameter curvature

The finite shear is identical to ZGS on crossing diameter pairs. Therefore

```math
\boxed{
\sum_{h\pitchfork\tau}\beta_h|r_h(\theta)|^2
=
w_\tau D^2
-2(A_\tau-w_\tau)(1-\cos\theta).
}
\tag{ZSF4}
```

For every sufficiently small nonzero `theta`,

```math
\boxed{
\sum_{h\pitchfork\tau}\beta_h
\bigl(D^2-|r_h(\theta)|^2\bigr)>0.
}
\tag{ZSF5}
```

Secondary diameter-pair minimality again forces the exact two-sided cusp:

```math
\boxed{
\exists h_+,h_-\pitchfork\tau:
\quad
r_{h_+}\cdot Ju_\tau>0,
\qquad
r_{h_-}\cdot Ju_\tau<0.
}
\tag{ZSF6}
```

Otherwise one shear sign would make every crossing active diameter pair nonincreasing to first order; weighted stationarity would force all derivatives to vanish, and the exact second-order formula would strictly shorten every crossing diameter pair, contradicting the secondary diameter normalization.

---

## 6. C66 alignment also extends verbatim

In the near-zero stress-star phase, the ZMA proof used only the exact cut resultant ZGS3. Since ZSF2 is the same resultant equation, every fixed-scale macroscopic same-face train satisfies the same alignment theorem.

For every fixed `c>0`, if

```math
A_\tau\ge cD,
```

then its projective train direction lies within `o_c(1)` of the C18 stress-star cone of width

```math
\frac{5\pi}{6}-\sqrt3+o(1)<\frac\pi3.
```

Hence:

### Corollary ZSF.2 — macroscopic same-face trains do not cross

For sufficiently large near-zero survivors, any two same-face trains with

```math
A_{\tau_1},A_{\tau_2}\ge cD
```

are pairwise noncrossing.

Thus every crossing of two same-face trains contains a mechanically light train at every fixed macroscopic threshold.

---

## 7. Endpoint-pairing graph of the macroscopic rhombic sea

For the ZRC component `Q_*`, let the stopping-face set consist of

- one symbol `O` for the global outer face;
- every bounded nonquadrilateral face incident to the boundary of `Q_*`.

Every component train has two endpoint faces and therefore determines an edge of a multigraph

```math
\mathcal E_{stop}
```

on this stopping-face set.

ZSF proves that every **loop edge** of this endpoint multigraph is an exact global train shear.

Therefore the remaining externally locked train-angle branch consists only of train edges joining two **distinct** stopping faces.

This is a strict reduction of ZPL-B, which previously treated all hole-ending trains as component-local.

---

## 8. Exact remaining endpoint split

Let `N_loop` be the number of weak-rich trains whose two endpoints lie on the same stopping face and `N_crossface` the number joining distinct stopping faces.

Since ZRC/ZWT gives

```math
N_{loop}+N_{crossface}=\Omega_\eta(D),
```

one of two alternatives holds.

### ZSF-A — linear many exact global weak shears

```math
N_{loop}=\Omega_\eta(D).
```

Then the source has a linear family of exact full-contact train shears. Every one is blocked only by the active diameter cusp and has the ZSF4 negative weighted curvature identity.

This is the natural input for a multi-shear Theorem-Z/circular-split argument.

### ZSF-B — linear cross-face train transport

```math
N_{crossface}=\Omega_\eta(D).
```

Then the macroscopic rhombic sea contains a linear family of weak-rich train paths joining distinct stopping faces. These are genuine defect-to-defect transport strips, not same-boundary shear modes.

The next topological target in this branch is a stopping-face transport theorem that charges these cross-face strips to hole separation, exceptional-face perimeter, or PI/GU pocket area.

---

## 9. Classification

**Status:** proved report-level exact extension of ZGS.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.
