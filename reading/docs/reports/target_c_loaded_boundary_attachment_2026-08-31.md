> Generated reading edition · [exact source](../../../docs/reports/target_c_loaded_boundary_attachment_2026-08-31.md) · source SHA-256 `d04e9d88e89941e110aa9268877295746be5aebac427152c497f43e2fec4dafe`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-89EAEFAFBB3E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C35: loaded boundary degree and interior attachment

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C22, C26, C33 and elementary unit-contact angle geometry  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C33 forces a linear positively loaded boundary. Its contact attachment has a simple exact form.

Every `b in B_+` is an extreme convex-hull vertex. All unit-contact directions from `b` lie in an angular interval of width strictly less than `pi`. If `bc` and `bd` are distinct unit contacts, unit separation gives `angle cbd>=pi/3`; equality would make `bcd` a forbidden unit equilateral triangle. Hence contact directions are separated by strictly more than `pi/3`, so

```math
\boxed{1\le\deg_C(b)\le3.}
```

Delete `B_+` and let `I_1,...,I_{c_I}` be the connected components of the remaining contact graph. Let `t_r` be the number of contact edges from `I_r` to `B_+`. Summing positive contact equilibrium over `I_r` rules out `t_r=1`; if `t_r=2`, C22 makes the component a reaction-free two-terminal straight chain, which C26 excludes. Therefore

```math
\boxed{t_r\ge3.}
```

If `e_{BI}` is the total loaded-interior contact count and `e_{BB}` the loaded-loaded contact count,

```math
\boxed{e_{BI}\ge3c_I,\qquad e_{BI}+2e_{BB}\le3q.}
```

Moreover at most `2e_{BB}` loaded vertices fail to touch the unpinned interior. Combined with C33, a near-minimal boundary has only `o(D)` interior components, `o(D)` loaded-loaded contacts, and all but `o(D)` loaded vertices attached to the interior.

---

## 1. Loaded degree cap

Let `b in B_+`. Since `b` is a source diameter endpoint, it is an extreme vertex of `conv A`. Hence all vectors `x-b`, `x in A\setminus\{b\}`, lie in a closed wedge of opening angle `theta_b<pi`.

For two distinct unit-contact neighbors `c,d`,

```math
|c-d|^2=2-2\cos\angle cbd.
```

Unit separation gives `angle cbd>=pi/3`. Equality would imply all three distances `bc,bd,cd` equal one, a forbidden unit triangle. Thus

```math
\angle cbd>\frac\pi3.
\tag{C35.1}
```

Four contact directions inside a wedge of width `<pi` would make the angular difference from first to fourth exceed `pi`, impossible. Positive diameter loading guarantees at least one positive contact incidence. Therefore:

### Theorem C35.1

```math
\boxed{1\le\deg_C(b)\le3\quad(b\in B_+).}
\tag{C35.2}
```

---

## 2. Three boundary contacts per unpinned component

Let `I=V(C)\setminus B_+`, and let `I_r` be one connected component of `C[I]`. Let `t_r` be the number of contact edges joining it to `B_+`.

The full contact core is connected, so `t_r>=1`. Sum KKT contact equilibrium over all vertices of `I_r`. Every internal contact force cancels. Because no vertex of `I_r` is positively diameter-loaded, the remaining sum of the `t_r` positive boundary contact forces is zero.

A single nonzero force cannot sum to zero, so `t_r!=1`.

If `t_r=2`, then `I_r` is a connected reaction-free positive-contact region with exactly two positive-contact edges leaving it. C22 collapses it to one exact straight constant-stress unit chain, making every component vertex unloaded of full contact degree two. C26 forbids such vertices in C-II. Hence `t_r!=2`.

### Theorem C35.2

```math
\boxed{t_r\ge3.}
\tag{C35.3}
```

Summing gives

```math
\boxed{e_{BI}\ge3c_I.}
\tag{C35.4}
```

---

## 3. Boundary incidence budget

Sum full contact degrees over `B_+`:

```math
\sum_{b\in B_+}\deg_C(b)=e_{BI}+2e_{BB}.
\tag{C35.5}
```

By C35.1,

```math
\boxed{e_{BI}+2e_{BB}\le3q.}
\tag{C35.6}
```

Let `B_0` be the loaded vertices with no contact into `I`. Every `b in B_0` has positive contact degree, and every such contact is loaded-loaded. Therefore each `b in B_0` is an endpoint of at least one edge counted by `e_{BB}`, so

```math
\boxed{|B_0|\le2e_{BB}.}
\tag{C35.7}
```

C38 will improve this factor two using quotient connectivity.

---

## 4. Near-minimal boundary consequence

C33 gives

```math
c_I+e_{BB}\le\sigma_B:=2q-\delta-2.
\tag{C35.8}
```

If `sigma_B=o(D)`, then `c_I=o(D)` and `e_{BB}=o(D)`. Since canonical C30 gives `q=Omega(D)`, C35.7 shows all but `o(D)` loaded vertices have a direct contact into only `o(D)` unpinned components.

---

## 5. Regression audit

- Loaded degree three is allowed; the theorem only rules out degree four at an extreme triangle-free contact vertex.
- One interior component attached by three edges is allowed.
- Boundary-only contact cores have `I=empty` and are outside the attachment statements.

```text
C35:
Loaded vertices are extreme and triangle-free unit-contact directions are >60 degrees
apart inside a wedge of width <180 degrees, hence loaded contact degree <=3.  Each
unpinned component needs at least three boundary contact edges: one cannot balance, and
two invoke C22+C26.  Thus e_BI>=3c_I and e_BI+2e_BB<=3q.  Near C33 equality, almost
all loaded vertices attach to only o(D) interior components.
```
