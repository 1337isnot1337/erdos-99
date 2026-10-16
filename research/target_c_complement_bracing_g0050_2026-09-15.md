<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c59c1d128c46ef41cd1aa5dc1de536183fa868e8", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_complement_bracing_g0050_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8a7f28934378f06783991072dd7000440829f0c50c3686f14967530ca423c3f7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — `g=0.0050` propagates through complement outer-train bracing

**Date:** 2026-09-15  
**Repository base:** `74fd0e6ab9a810a878998426524cd80d9153132a`  
**Status:** proof-only strengthening of the audited complement-bracing theorem; theorem-state authority unchanged  
**Scope:** fully force-visible no-container/full-core Type-II branch  
**LEVEL I STATUS:** `STILL OPEN`

The audited complement outer-train bracing theorem proves a second, disjoint outer
route-energy payment from trains outside the dominant atomic `pi/3` orbit.  Its scalar
certificate was instantiated with the older atomic train gap

\[
g=0.00042,
\qquad
C_0=2\sqrt{\Delta_2}+g,
\qquad
\Delta_2={\pi\over2\sqrt3},
\]

and therefore gave only

\[
\liminf {q-k\over D}\ge1.82806.
\]

Current `main` already contains the independently hostile-audited matched atomic gap

\[
\boxed{g=0.0050.}
\]

The complement-bracing proof is symbolic in the lower scalar floor `C>=C_0`; none of
its geometric lemmas uses the numerical value `0.00042`.  Replacing `C_0` by

\[
\boxed{C_{50}:=2\sqrt{\Delta_2}+0.0050}
\]

and rerunning the same one-variable endpoint raises the safe Type-II floor to

\[
\boxed{
\liminf {q-k\over D}\ge1.82890.
}
\]

The scalar zero is approximately

\[
1.8289123539\ldots,
\]

but only the safely rounded value `1.82890` is claimed.

---

## 1. Inputs already audited on `main`

On a convergent full-core Type-II subsequence write

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D}.
\]

Let

\[
C={T-q/2\over D}.
\]

The imported iterative-pruning theorem gives

\[
\boxed{C\ge C_{50}:=2\sqrt{\Delta_2}+0.0050.}
\tag{GB.1}
\]

The Section-171 upper envelope remains

\[
\boxed{
C\le U:={9t\over2}-2\pi-2\delta-\frac\kappa2.
}
\tag{GB.2}
\]

Thus

\[
\boxed{
2\delta+{\kappa\over2}
\le R_{50}(t):={9t\over2}-2\pi-C_{50}.
}
\tag{GB.3}
\]

The same matched theorem also gives `T_R/D>=C_50-o(1)` and
`sigma_R/D>=0.0100-o(1)`, but those stronger rhombic-only conclusions are not used in
the scalar propagation below.

---

## 2. Every complement-bracing inequality remains symbolic in `C_0`

The audited complement theorem uses one dominant exact `pi/3` train orbit.  If `M` is
its absolute train mass, then

\[
M\ge{4\Delta_2\over C}.
\tag{GB.4}
\]

The number of trains outside the frozen dominant-orbit windows satisfies

\[
N_c
\le
N_*:=U+{t+\kappa\over2}-{4\Delta_2\over U}.
\tag{GB.5}
\]

The joint orbit-capacity theorem gives an upper bound on the actual dominant-window
outer terminal occurrence mass `K`:

\[
\delta\ge\Phi(K),
\qquad
\Phi(z):=z-6\arcsin(\tanh(z/6)).
\tag{GB.6}
\]

Let

\[
Q(\delta):=\Phi^{-1}(\delta).
\]

Then the complement trains have at least

\[
\pi+\delta-Q(\delta)
\]

outer terminal occurrences.  The audited pair-retention argument loses at most
`delta` of pair mass to hull-side capacity, so the retained complement outer-to-outer
pair mass is bounded below by

\[
\boxed{
p_*
:=
\left[
\pi-Q(\delta)-U-{t+\kappa\over2}+{4\Delta_2\over U}
\right]_+.
}
\tag{GB.7}
\]

Audited Section 157 and the near-antipodal noncrossing-capacity lemma then force the
complement terminal energy

\[
\boxed{
E_{comp}\ge J(p_*),
\qquad
J(p):=2p-6\sin(p/3)
}
\tag{GB.8}
\]

on the relevant range `p_*<=1`.

Independently, the retained dominant-window occurrences have mass

\[
\boxed{
z_*
:=
\pi-t-\kappa-2U+{8\Delta_2\over U}
}
\tag{GB.9}
\]

and consume the disjoint edge-energy amount

\[
\boxed{
E_{dom}\ge F(z_*),
\qquad
F(z):=z-6\sin(z/6).
}
\tag{GB.10}
\]

Therefore every survivor obeys

\[
\boxed{
\delta\ge F(z_*)+J(p_*).
}
\tag{GB.11}
\]

Equations (GB.4)--(GB.11) are exactly the already-audited complement-bracing stack.
They use only the abstract lower bound `C>=C_0`; replacing the old `C_0` by the stronger
`C_50` changes no geometric argument.

---

## 3. Feasible-region minimization remains at `kappa=0` and maximal detour

Define

\[
\mathcal M(t,\delta,\kappa)
:=F(z_*)+J(p_*)-\delta.
\]

The audited derivative argument applies with `C_50` in place of the weaker `C_0`.
For completeness, the relevant signs only improve:

\[
{\partial z_*\over\partial\kappa}
={4\Delta_2\over U^2}>0,
\]

while

\[
N_*:=U+{t+\kappa\over2}-{4\Delta_2\over U}
\]

has

\[
{\partial N_*\over\partial\kappa}
=-{2\Delta_2\over U^2}<0.
\]

Hence both `z_*` and `p_*` increase with `kappa`, so

\[
\boxed{\mathcal M\text{ is minimized at }\kappa=0.}
\tag{GB.12}
\]

For `delta`, the stronger lower bound `U>=C_50>C_0` makes the derivative caps no worse
than those already hostile-audited.  On the interval from the previous certified floor
through `t=1.82890`, the companion certificate verifies

\[
z_*<1.30,
\qquad
0.61<p_*<1,
\qquad
Q(\delta)<1.61,
\]

and the same coarse inequalities give

\[
{\partial\mathcal M\over\partial\delta}<0.
\tag{GB.13}
\]

Thus the weakest feasible point is again

\[
\boxed{
\kappa=0,
\qquad
\delta={R_{50}(t)\over2},
\qquad
U=C_{50}.
}
\tag{GB.14}
\]

---

## 4. One-dimensional boundary margin

At (GB.14), put

\[
\delta_{50}(t):={R_{50}(t)\over2},
\tag{GB.15}
\]

\[
z_{50}(t)
:=
\pi-t-2C_{50}+{8\Delta_2\over C_{50}},
\tag{GB.16}
\]

\[
N_{50}(t)
:=
C_{50}+{t\over2}-{4\Delta_2\over C_{50}},
\tag{GB.17}
\]

\[
p_{50}(t)
:=
\pi-Q(\delta_{50}(t))-N_{50}(t).
\tag{GB.18}
\]

The boundary contradiction margin is

\[
\boxed{
\mathcal M_{50}(t)
:=
F(z_{50}(t))+J(p_{50}(t))-\delta_{50}(t).
}
\tag{GB.19}
\]

Exactly as in the audited complement theorem,

\[
z_{50}'(t)=-1,
\qquad
\delta_{50}'(t)=9/4,
\]

and

\[
p_{50}'(t)
=-{9/4\over\Phi'(Q(\delta_{50}(t)))}-{1\over2}<0.
\]

All three terms make `M_50` strictly decrease with `t` on the certified interval.
Thus a positive margin at one endpoint excludes the entire interval below it once the
previous lower-floor theorem is included.

---

## 5. Certified new floor

The independent high-precision verifier gives at

\[
\boxed{t=1.82890}
\]

\[
\begin{aligned}
\delta_{50}&=0.0186195395462494157\ldots,\\
z_{50}&=1.2927188367325205668\ldots,\\
F(z_{50})&=0.009977\ldots,\\
Q(\delta_{50})&=1.5996201137927153\ldots,\\
p_{50}&=0.6175356313684415\ldots,
\end{aligned}
\]

and

\[
\boxed{
\mathcal M_{50}(1.82890)
=0.0000622842731984975\ldots>0.
}
\tag{GB.20}
\]

It also verifies

\[
\mathcal M_{50}(1.82891)
=0.0000118581320796781\ldots>0
\]

and brackets the scalar crossing between

\[
1.8289123539
<t_*<
1.8289123540.
\tag{GB.21}
\]

We keep the materially safer round constant `1.82890`.

### Theorem GB.1 — matched-gap complement-bracing floor

Every convergent full-core Type-II survivor subsequence in the proof-only scope satisfies

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}
\ge1.82890.
}
\tag{GB.22}
\]

This supersedes both the `1.82515` matched-gap joint-orbit floor and the `1.82806`
complement-bracing floor.

---

## 6. Frontier effect

The improvement is not a new geometric theorem; it is the missing composition of two
already hostile-audited advances that were merged in rapid succession:

```text
iterative two-shore pruning
 -> matched atomic gap g=0.0050
 -> tighter all-train envelope C >= 2 sqrt(Delta2)+0.0050

complement outer-to-outer trains
 -> two-sided actual-diameter bracing
 -> near-antipodal noncrossing capacity
 -> second outer directional-energy payment

both together
 -> t=(q-k)/D >= 1.82890.
```

The retained complement-pair population at the new endpoint is still

\[
p_{50}=0.6175\ldots,
\]

so the complement-bracing mechanism remains macroscopic.  The next progress should
therefore alter the geometry or capacity estimate, not tune this scalar root.

No source-preserving diameter decrease or exact unit equilateral triangle is produced.
C-II remains open.

**Classification:** proof-only strengthening pending hostile audit.
