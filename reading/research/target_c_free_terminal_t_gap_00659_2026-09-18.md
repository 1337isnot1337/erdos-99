> Generated reading edition · [exact source](../../research/target_c_free_terminal_t_gap_00659_2026-09-18.md) · source SHA-256 `f4d4aa6cf687b1372b670195b3966eea03bad88c4d4ea2b28f28b909ee80331d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "0d8052a11c748616fb183256b03b7f0ce03c2b59", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_t_gap_00659_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "2a1b5dd1bb97ffa23d4384e17907093037ced825e6ff2d54a0fcedf66b51bdaa"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — terminal FREE surplus cancellation raises the actual `t` floor by `0.00659`

**Date:** 2026-09-18  
**Status:** proof-only terminal refinement; theorem-state authority unchanged  
**Scope:** terminal full-core Type-II FREE survivor sequences with `pi D-q=o(D)`  
**Depends on:** scope-safe matched all-train gap `g=0.007707`; exact terminal surplus decomposition; full-core loaded-chord identity; hostile-audited two-bin exact-orbit theorem; hostile-audited shared routewise retention; complement train/rhombus incidence; disjoint dominant/complement outer-energy support  
**Certificate:** `research/verify_target_c_free_terminal_t_gap_00659_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current terminal FREE package has an avoidable loss.  The latest quantitative
incidence theorem was stated as a gap for the all-phase surplus

$$
\mu_D:=\frac{e_{BB}+2s_C-3k}{D},
\qquad k=d_H+s_Z,
$$

and then converted to

$$
\mu_D=t_D+\frac{m_B}{D}+o(1),
\qquad
 t_D:=\frac{q-k}{D},
$$

leaving a separate branch in which linearly many nonunit loaded-hull sides `m_B`
could keep `t_D` near the old floor.

That split is not needed.  In the exact terminal surplus decomposition the `m_B`
term cancels **before** taking the endpoint limit.  The result is an exact finite
identity for `q-k` itself.  Therefore every stability estimate used by the recent
incidence argument applies directly to `t_D`, independent of `m_B`.

Retaining one further already-audited term, namely that dominant and complement
terminal-edge energy supports are disjoint, sharpens the scalar contradiction enough
to prove

$$
\boxed{
\liminf_{D\to\infty} t_D
\ge
1.959852849540479\ldots .
}
\tag{TG.1}
$$

This is an unconditional terminal FREE improvement of exactly `0.00659` above the
previous feasibility floor

$$
1.953262849540479\ldots .
$$

after the matched `g=0.007707` input.  In particular, the former alternative

```text
t near 1.9532628495...
OR
linear m_B
```

is removed: the first branch is impossible regardless of how the surplus is stored
in nonunit hull sides.

The same improvement raises the raw terminal inactive-chamber interface floor to

$$
\boxed{
\liminf\frac{\mathcal H_D}{D}
\ge2.301389136473497\ldots,
}
\tag{TG.2}
$$

and hence

$$
\boxed{
\liminf\frac{A_{ch}-(\sqrt3/2)Z_{ch}}D
\ge0.996530728089790\ldots .
}
\tag{TG.3}
$$

No source-preserving diameter decrease is claimed.  C-II remains open.

---

## 1. Exact cancellation: the terminal scalar is `t`, not `mu`

Retain the notation of the terminal surplus-endpoint theorem.  Put

$$
s_2:=\sqrt{\frac\pi{2\sqrt3}},
\qquad
 g:=0.007707,
$$

$$
\tau_*:=\frac\pi2+g,
\qquad
A_0:=2s_2+g.
\tag{1.1}
$$

Let

$$
\tau_D:=T-2\sqrt{R_4}
\tag{1.2}
$$

be the stopped-train slack used in the modern terminal ledger.  The matched all-train
theorem gives

$$
\frac{\tau_D}{D}\ge\tau_*-o(1).
\tag{1.3}
$$

The exact surplus decomposition already proved on the terminal FREE branch is

$$
\begin{aligned}
\mu_DD={}&
\frac{2P_F+2\sqrt{R_4}}5
+m_B
+\frac25(Q-f)
+\frac25(b-P_F)\\
&+\frac1{10}\rho_{rec}
+\frac1{10}\sigma_R
-2c_I-4,
\end{aligned}
\tag{1.4}
$$

with

$$
\rho_{rec}+\sigma_R=2\tau_D.
\tag{1.5}
$$

On the same full-core loaded-chord branch,

$$
\mu_DD=q+m_B-k-2c_I-4.
\tag{1.6}
$$

Subtract `m_B-2c_I-4` from (1.4) and (1.6).  Everything involving nonunit hull-side
count and component deatomization cancels exactly.  This gives the finite identity

$$
\boxed{
q-k
=
\frac{2P_F+2\sqrt{R_4}}5
+\frac25(Q-f)
+\frac25(b-P_F)
+\frac15\tau_D.
}
\tag{1.7}
$$

Thus the terminal feasibility variable `t_D=(q-k)/D` already has its own nonnegative
defect decomposition.

Terminal full-core geometry gives

$$
\frac{P_F}{D}\to\pi,
\qquad
\frac{\sqrt{R_4}}D\to s_2.
\tag{1.8}
$$

Define

$$
\mu_*:=
\frac{2\pi+2s_2}{5}+\frac{\tau_*}{5}
=
\frac\pi2+\frac{2s_2}{5}+\frac g5
=1.953262849540479\ldots .
\tag{1.9}
$$

Pass to a subsequence on which the normalized nonnegative defect currencies converge,
and write

$$
r:=\lim\frac{Q-f}{D},
\qquad
\delta:=\lim\frac{b-P_F}{D},
\qquad
 a:=\lim\left(\frac{\tau_D}{D}-\tau_*\right).
\tag{1.10}
$$

By (1.3), `a>=0`.  Equations (1.7)--(1.9) give the exact asymptotic identity

$$
\boxed{
\lim(t_D-\mu_*)
=
\frac25(r+\delta)+\frac15a.
}
\tag{1.11}
$$

There is no `m_B` term.

Consequently, if a terminal subsequence satisfies

$$
\limsup t_D\le\mu_*+\varepsilon,
\tag{1.12}
$$

then necessarily

$$
\boxed{
0\le\delta\le\frac52\varepsilon,
\qquad
0\le r\le\frac52\varepsilon,
\qquad
0\le a\le5\varepsilon.
}
\tag{1.13}
$$

These are exactly the stability bounds that the preceding quantitative incidence proof
obtained from an upper bound on `mu_D`.  They actually follow from an upper bound on
`t_D` alone.

---

## 2. Two-bin concentration in the `t`-stability box

The normalized all-train scalar satisfies, along the same subsequence,

$$
C:=\lim\frac{T-q/2}{D}
=A_0+a.
\tag{2.1}
$$

The hostile-audited two-bin exact-orbit theorem gives one dominant exact projective
`pi/3` orbit and bounds all residual exact-orbit train mass by

$$
\boxed{
r_2(C)
:=
\frac{C-\sqrt{8\Delta_2-C^2}}2,
\qquad
\Delta_2:=\frac\pi{2\sqrt3}.
}
\tag{2.2}
$$

On the present live interval `r_2` is increasing.  Choose

$$
\boxed{\varepsilon_0:=0.00659.}
\tag{2.3}
$$

Then (1.13) gives

$$
a\le0.03295,
\qquad
\delta\le0.016475.
\tag{2.4}
$$

The exact-rational certificate proves

$$
\boxed{
r_2(A_0+0.03295)<0.04111.}
\tag{2.5}
$$

Let `r_0=0.04111` for the rest of the finite scalar estimate.

---

## 3. Shared retention and the energy term that was previously discarded

The hostile-audited shared routewise-retention theorem supplies retained dominant
outer-occurrence mass `z` and retained complement O--O pair mass `p` satisfying

$$
\boxed{
z+p\ge\frac\pi2-r_0-o(1).}
\tag{3.1}
$$

For

$$
F(z):=z-6\sin(z/6),
\tag{3.2}
$$

the dominant retained occurrences consume at least `F(z)D-o(D)` of actual outer
directional energy.

Let `e_c D` be the selected terminal-edge directional energy of the retained complement
O--O family.  Complement train/rhombus incidence gives

$$
\boxed{
p(1-\delta)-\frac{e_c}{2}
\le\frac{r_0^2}{2}+o(1).}
\tag{3.3}
$$

The recent `0.00645` surplus-gap proof used only the coarse estimate `e_c<=delta`.
The earlier hostile-audited complement-incidence theorem proves more: the dominant and
complement selected terminal-edge supports are physically disjoint.  Therefore their
energy payments add, and

$$
\boxed{F(z)+e_c\le\delta.}
\tag{3.4}
$$

Substituting (3.4) into (3.3), every survivor must satisfy

$$
\boxed{
p
\le
\frac{r_0^2+\delta-F(z)}{2(1-\delta)}+o(1).}
\tag{3.5}
$$

Together with (3.1), this requires

$$
H(z):=
\frac\pi2-r_0-z
-
\frac{r_0^2+\delta-F(z)}{2(1-\delta)}
\le o(1).
\tag{3.6}
$$

This is the only change to the preceding incidence-gap architecture: retain the
`-F(z)` term instead of discarding it.

---

## 4. A rational contradiction at `epsilon=0.00659`

Set

$$
z_0:=1.5286.
\tag{4.1}
$$

The alternating Taylor bound

$$
\sin x\le x-\frac{x^3}{6}+\frac{x^5}{120}
\qquad(x\ge0\text{ in the present range})
$$

gives

$$
F(z_0)
\ge
\frac{z_0^3}{216}-\frac{z_0^5}{155520}.
\tag{4.2}
$$

The exact certificate proves

$$
\boxed{
F(1.5286)>0.0164822351>0.016475.
}
\tag{4.3}
$$

Hence (3.4) and (2.4) imply

$$
z<z_0.
\tag{4.4}
$$

Now

$$
H'(z)
=-1+\frac{F'(z)}{2(1-\delta)}.
\tag{4.5}
$$

For `0<=z<=z_0`,

$$
F'(z)=1-\cos(z/6)
\le\frac{z^2}{72}
\le\frac{z_0^2}{72}
<\frac1{30}.
\tag{4.6}
$$

Together with `delta<=0.016475`, this makes `H'(z)<0` throughout the feasible interval.
Thus (4.4) gives

$$
H(z)>H(z_0).
\tag{4.7}
$$

At `z_0`, (4.3) says `delta-F(z_0)<0`, so a still weaker lower bound is

$$
H(z_0)
>
\frac\pi2-r_0-z_0
-
\frac{r_0^2}{2(1-0.016475)}.
\tag{4.8}
$$

Using a Machin-series lower enclosure for `pi`, the certificate proves

$$
\boxed{
\frac\pi2-0.04111-1.5286
-
\frac{0.04111^2}{2(1-0.016475)}
>0.000227.
}
\tag{4.9}
$$

This contradicts the necessary condition (3.6).  Therefore no terminal FREE survivor
subsequence can satisfy (1.12) with `epsilon=0.00659`.

We have proved

$$
\boxed{
\liminf t_D
\ge
\mu_*+0.00659
=
1.959852849540479\ldots .
}
\tag{4.10}
$$

This proves (TG.1).

The scalar root of this particular retained-energy composition lies only slightly above
`0.00659`; no claim is made past the certified rational value.  Further decimal tuning
of this one-variable endpoint is not the useful next route.

---

## 5. Consequences for the terminal interface

The matched terminal chamber-interface derivation gives

$$
\frac{\mathcal H_D}{D}
\ge t_D+\gamma_g-o(1),
\qquad
\gamma_g:=2s_2-\frac\pi2+g
=0.341536286933018\ldots,
\tag{5.1}
$$

where

$$
\mathcal H_D=(b-P_F)+(Q+2f).
\tag{5.2}
$$

Insert (4.10):

$$
\boxed{
\liminf\frac{\mathcal H_D}{D}
\ge
2.301389136473497\ldots .
}
\tag{5.3}
$$

Canonical Section 85 then gives

$$
A_{ch}-a_0Z_{ch}
\ge\frac{\sqrt3}{4}\mathcal H_D,
\qquad a_0=\frac{\sqrt3}{2},
\tag{5.4}
$$

so

$$
\boxed{
\liminf\frac{A_{ch}-a_0Z_{ch}}D
\ge0.996530728089790\ldots .
}
\tag{5.5}
$$

The coefficient remains below one, so this is not by itself a closure.

Also, because

$$
\mu_D=t_D+\frac{m_B}{D}+o(1)
$$

with `m_B>=0`, (4.10) automatically strengthens the previous terminal surplus floor
to the same numerical value.  The logical direction is now the useful one: the actual
terminal feasibility variable `t_D` is bounded, not merely `t_D+m_B/D`.

---

## 6. Exact structural effect

The previous quantitative incidence note ended with the split

```text
m_B=o(D)  ->  t_D >= 1.9597128495...

or

m_B=Omega(D)  ->  unresolved nonunit-hull-side branch.
```

Equation (1.7) and the argument above remove that split entirely.  There is no longer a
terminal FREE branch in which nonunit hull-side count can keep `t_D` near the old
`1.9532628495...` feasibility edge.

For comparison, canonical Section 63 also gives the finite relation

$$
u_B=(P_F-q)+(b-P_F)-m_B\ge0,
\tag{6.1}
$$

so on the terminal face, where `P_F-q=o(D)`, any linear `m_B` already forces comparable
linear actual outer-walk detour `b-P_F`.  This is consistent with the cancellation
above, but (1.7) is stronger for the present purpose because the incidence proof never
needs to split on `m_B` at all.

The terminal FREE package now starts beyond

$$
\boxed{t_D=1.959852849540479\ldots-o(1)}.
$$

The older high-`t` support-normal-form machinery that stopped below about `1.87` is
therefore even farther from the live terminal branch.  The next useful theorem should
work directly in this higher-`t` regime and spend one of the actual source-level
currencies already forced there: the `~0.99653D` inactive-chamber Oler surplus, the
Section-122/123 aggregate attachment-cell detour, or the diffuse O--O diameter-bracing
family.  Another optimization confined to the old low-`t` window will not touch the
remaining terminal FREE branch.

---

## 7. Scope and hostile checks

1. **No theorem-state promotion.** All new conclusions remain proof-only because the
   matched `g=0.007707` and the downstream exact-orbit/retention/incidence stack are
   proof-only inputs.
2. **No deletion of source points.** Contact-isolated source points remain in the full
   source.  The identities used here are the established full-core source-derived
   ledgers.
3. **No `m_B=o(D)` assumption.** This is the main point of the note.  `m_B` cancels
   from (1.7) exactly.
4. **Occurrence conventions retained.** `b` is the occurrence-counted outer contact
   walk and `b-P_F` is the actual route detour from canonical Section 63.
5. **Complement energy is not double-counted.** Equation (3.4) is imported only from
   the earlier hostile-audited disjoint-support theorem: dominant and selected
   complement terminal edge classes are disjoint.
6. **Computation is certificate-only.** The theorem uses the symbolic identities and
   monotonicity above.  The Python file certifies the rational constants and Taylor
   inequalities; it is not empirical evidence for the theorem.

**Disposition:** proved proof-only terminal `t`-gap and chamber-interface refinement;
C-II remains open.
