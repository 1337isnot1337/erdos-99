> Generated reading edition · [exact source](../../../docs/reports/target_c_annular_loaded_terminal_credit_2026-09-11.md) · source SHA-256 `591a23814a4506f48b70c4ad7e98114a5a00a705195f8321a960c01e188e6c1b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-D3FE8CC52D09","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — loaded-terminal credit in the annular capacity ledger

**Date:** 2026-09-11  
**Repository base:** branch after GA  
**Run type:** exact strengthening of global post-ZF annular/rhombus transport  
**Target:** Target C C-II after ZF  
**Depends on:** GR, promoted AV annular Voronoi capacity, C65 force-hull terminal identification  
**External input:** none beyond the already audited AV dependency

## LEVEL I STATUS

`STILL OPEN`.

GA applied the annular theorem AV only to the contact-isolated source points outside
the force hull.  In a post-ZF source one can include every loaded force-hull terminal
in the same annular packing set, because the loaded set is precisely the vertex set of
`F` and therefore lies on `partial F`.

This gives the exact strengthening

```math
\boxed{
E+\delta_K+a_0q
< P_K+(1+c_0)P_F+\pi,
\qquad
a_0={\sqrt3\over2},\quad c_0={\sqrt3\over4}.
}
\tag{LT.1}
```

Thus the mandatory linear loaded-terminal population consumes genuine annular packing
capacity instead of disappearing from the global rhombus-excess cancellation.

---

## 1. Apply AV to external points plus loaded terminals

Let

- `K=conv(A)` be the full source hull;
- `F` be the post-ZF force hull;
- `B_+=Vert(F)` with `q=|B_+|`;
- `Z_ext` be the source points outside `F`.

The set

```math
S:=(A\setminus F)\cup B_+
```

is a subset of the original source, hence is unit-separated.  Also

```math
A\setminus F\subset K\setminus int(F),
\qquad
B_+\subset\partial F\subset K\setminus int(F).
```

Therefore the promoted annular Voronoi theorem AV applies directly and gives

```math
\boxed{
a_0(Z_{ext}+q)
\le area(K)-area(F)+P_K+P_F+\pi.}
\tag{LT.2}
```

Equivalently, with

```math
\delta_F={\pi D^2\over4}-area(F),
\qquad
\delta_K={\pi D^2\over4}-area(K),
```

```math
\boxed{
a_0Z_{ext}
\le\delta_F-\delta_K+P_K+P_F+\pi-a_0q.}
\tag{LT.3}
```

---

## 2. Substitute the general rhombus-excess inequality

GR proves

```math
E+\delta_F<a_0Z_{ext}+c_0P_F.
\tag{2.1}
```

Insert LT.3:

```math
E+\delta_F
<\delta_F-\delta_K+P_K+(1+c_0)P_F+\pi-a_0q.
```

Cancel `delta_F` and rearrange:

### Theorem LT — loaded-terminal annular credit

```math
\boxed{
E+\delta_K+a_0q
< P_K+(1+c_0)P_F+\pi.
}
\tag{LT.4}
```

Since `P_K,P_F<=pi D`, this gives

```math
\boxed{
E+\delta_K+a_0q
<\pi D\left(2+{\sqrt3\over4}\right)+\pi.
}
\tag{LT.5}
```

The main use is not this crude perimeter relaxation but the exact finite form LT.4,
which retains the actual force-hull perimeter and the loaded count simultaneously.

---

## 3. Post-ZF diameter lower bound enters immediately

ZF gives

```math
h\ge\lceil D\rceil,
```

and the planar diameter graph satisfies `h<=q`.  Hence

```math
q\ge\lceil D\rceil.
\tag{3.1}
```

The stronger DB theorem gives asymptotically

```math
\liminf {h\over D}\ge2\rho=1.47817\ldots,
\qquad \rho=\cos\rho,
```

and therefore the same lower floor for `q/D`.

Thus LT.4 contains an unavoidable linear debit `a_0q`, not merely a nonnegative term.
No contradiction follows from the crude perimeter upper bounds alone, but future shell
or force-perimeter estimates should retain this term rather than reverting to GA.2.

---

## 4. Scope

- No assumption is made on `d_H`, `s_Z`, diameter topology, external-rattler count, or
  exceptional faces.
- Loaded vertices are counted only once even if they are also vertices of the full
  source hull.
- Interior force-hull source points cannot be added to the AV annular set without
  changing the inner body; LT makes no such claim.
- The theorem is strictly stronger than GA because `q>0` throughout post-ZF.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Instead of applying AV only to external rattlers, apply it to
    S=(A\F) union B_+.
This entire set lies in K\int(F), is unit-separated, and has size Z_ext+q. Thus
    a0(Z_ext+q)<=area(K)-area(F)+P_K+P_F+pi.
Combine with GR
    E+delta_F<a0 Z_ext+c0 P_F
and cancel delta_F:
    E+delta_K+a0 q < P_K+(1+c0)P_F+pi.
ZF/DB make q linear in D, so the annular packing ledger now retains a mandatory linear
loaded-terminal debit.
```
