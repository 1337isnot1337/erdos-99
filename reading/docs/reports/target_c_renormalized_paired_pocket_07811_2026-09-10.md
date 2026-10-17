> Generated reading edition · [exact source](../../../docs/reports/target_c_renormalized_paired_pocket_07811_2026-09-10.md) · source SHA-256 `cb69cc94801acec476b8ecd3d4009d7092ed32be5a4afdce3b75a48eebe5f9aa`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CCDB9C34489C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — paired outer-pocket capacity raises the all-phase renormalized surplus above 0.7811

**Date:** 2026-09-10  
**Repository base:** `fa824c13f570754bab484217c57cf420988cf9d3` (`research/c2-general-mu05947-20260910`)  
**Run type:** closing-proof continuation / exact renormalized cavity sharpening  
**Target:** Target C, all post-ZF survivors  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** none used  
**Computation:** none used in the proof; decimal evaluation only

## LEVEL I STATUS

`STILL OPEN`.

This report removes the entire low-`mu` outer-shell phase from the preceding GR/PT
split.  Let

```math
k:=d_H+s_Z,
\qquad
\mu_D:=\frac{e_{BB}+2s_C-3k}{D},
\qquad
y_D:=\frac hD.
```

The previous all-phase theorem GR proved only

```math
\liminf\mu_D>0.5947.
```

The new input is the opposite-pocket pairing forced by the full-source midpoint
polygon.  Combining that pairing with two exact PC identities gives a much stronger
renormalized pocket budget in which `k` cancels completely.  The result is

```math
\boxed{
\liminf_{D\to\infty}\mu_D
\ge
\mu_{RP}
:=
\frac{\pi\left(2\sqrt{3\pi^2+1}-1\right)}{4\pi^2+1}
=0.7811638359065726\ldots .
}
\tag{RP.1}
```

In particular

```math
\boxed{\mu_{RP}>0.78>0.70>u_\pi,}
\tag{RP.2}
```

where the preceding PT report proved

```math
u_\pi
=\frac{\pi(\sqrt{3\pi^2+4}-1)}{2(\pi^2+1)}
=0.6932725422\ldots .
```

Thus **PT-L is empty**: no sufficiently large post-ZF survivor can lie in any fixed
window `mu_D<=u<u_pi`.  The inactive outer-shell theorem remains a valid conditional
normal form, but the new lower bound shows that a genuine survivor cannot enter that
phase.

The proof does not use the unpromoted `lambda_PL=0.944988...` optimization from PR
#173.  Only the clean opposite-pocket isoperimetric lemma is rederived below from the
FS midpoint geometry.

---

## 1. Starting endpoint

Use the current post-ZF notation:

- `F` is the positive force hull;
- `h` is the number of actual diameter edges;
- `q` is the number of positively loaded diameter endpoints;
- `Q` is the bounded-face quadrangulation defect;
- `d_H=q-h`;
- `s_Z=e+h-(2v-2)`;
- `e_BB` is the loaded-loaded unit-contact count;
- `s_C` is the extra pinned-contact left-nullity;
- `a` is the number of missing force-hull contact sides / OP outer pockets;
- `d_P=sum_P(k_P-3)` is the total OP pocket degree excess;
- `c_B>=0` is the number of loaded-loaded contacts not lying on the force-hull boundary.

Put

```math
X:=d_P+Q.
\tag{1.1}
```

The preceding GR theorem supplies the all-phase attachment-cell bound

```math
\limsup\frac{C_{att}}{D^2}
\le\frac\pi4\mu^2
\tag{1.2}
```

along every convergent subsequence `mu_D->mu`, and FSDB supplies

```math
\liminf\frac{area(F)}{D^2}
\ge
\Phi(y):=\frac{y+\sin y}{4}
\tag{1.3}
```

when `y_D->y`.  DB gives

```math
2\rho\le y\le\pi,
\qquad
\rho=\cos\rho.
\tag{1.4}
```

Write

```math
G:=area(F)-C_{att}.
\tag{1.5}
```

Then (1.2)-(1.3) give the lower cavity requirement

```math
\boxed{
\liminf\frac G{D^2}
\ge
\Phi(y)-\frac\pi4\mu^2.
}
\tag{1.6}
```

The goal is to replace GR's generic isoperimetric cavity upper bound by an
opposite-pocket bound expressed directly in `mu` and `y`.

---

## 2. Exact cancellation of the mixed defect in the pocket budget

PC gives the finite exact identity

```math
\boxed{
e_{BB}=d_P+Q+2k+c_B.}
\tag{2.1}
```

Therefore

```math
\begin{aligned}
\mu_DD
&=e_{BB}+2s_C-3k\\
&=X-k+c_B+2s_C,
\end{aligned}
```

so

```math
\boxed{X\le\mu_DD+k.}
\tag{2.2}
```

The exact PC/TN boundary ledger also gives

```math
\boxed{q=a+d_P+Q+2k.}
\tag{2.3}
```

Since `a>=0`,

```math
X+2k\le q.
\tag{2.4}
```

But `q=h+d_H` and `k=d_H+s_Z`, hence

```math
\begin{aligned}
X
&\le h+d_H-2(d_H+s_Z)\\
&=h-d_H-2s_Z\\
&\le h-k.
\end{aligned}
\tag{2.5}
```

Add (2.2) and (2.5):

### Theorem RP.1 — renormalized pocket/face budget

For every finite post-ZF source,

```math
\boxed{
2(d_P+Q)\le\mu_DD+h.
}
\tag{RP.3}
```

More precisely, retaining the discarded `s_Z` gives

```math
\boxed{
2(d_P+Q)\le\mu_DD+h-s_Z.
}
\tag{2.6}
```

The key point is that the coefficient-three charge in `mu_D` is exactly strong enough
to cancel the apparently helpful `2k` term in PC.  A large diameter-tree or mixed-
stress defect cannot create unlimited outer-pocket degree.

Along a subsequence with `mu_D->mu` and `h/D->y`, write

```math
\tau:=\lim\frac{d_P}{D},
\qquad
\nu:=\lim\frac QD
```

after refining once if necessary.  RP.3 gives

```math
\boxed{
\tau+\nu\le\frac{\mu+y}{2}.
}
\tag{2.7}
```

---

## 3. Opposite macroscopic outer pockets

This section rederives only the part of the midpoint-polygon work needed here.
No scalar theorem from PR #173 is imported.

For each actual diameter edge `e=bk`, orient

```math
p_b-p_k=Du_e,
\qquad |u_e|=1,
```

and put

```math
P_H:=D\,conv\{\pm u_e:e\in H\}.
\tag{3.1}
```

FS.4 supplies one full-source circumcenter `o` and an error `L_D=o(D)` such that every
actual diameter midpoint

```math
m_e=\frac{p_b+p_k}{2}
```

satisfies `|m_e-o|<=L_D`.  Hence

```math
p_b-o=\frac D2u_e+(m_e-o),
\qquad
p_k-o=-\frac D2u_e+(m_e-o).
\tag{3.2}
```

Every force-hull vertex is an actual positively loaded diameter endpoint in the C-II
source.  Taking convex hulls in both directions gives

```math
\boxed{
d_{Haus}\left(F-o,\frac12P_H\right)\le L_D=o(D).
}
\tag{3.3}
```

Every actual force-hull vertex also has radius `D/2+o(D)` from `o`, uniformly.
Since `P_H/2` is centrally symmetric, every force-hull side whose length is
`cD+o(D)` with `c>0` has, after passage to a subsequence, an opposite side sector of
the same limiting chord length.  The radial annulus prevents the opposite limiting
flat segment from being filled by force-hull vertices a fixed angular distance inside
the segment: any such vertex would have support coordinate too large compared with
(3.3).  Thus there is an actual opposite force-hull side of length `cD+o(D)`.

Therefore every OP pocket with macroscopic hull chord is paired with a distinct
opposite OP pocket having the same normalized chord length.

This is an asymptotic pairing theorem, not a claim that microscopic sides pair one by
one.

---

## 4. Paired outer-pocket area capacity

Let an OP pocket have old unit-contact-chain length `ell_P` and force-hull chord
`s_P`.  Recall

```math
x_P:=\ell_P-2,
\qquad
\sum_Px_P=d_P.
\tag{4.1}
```

### Lemma RP.2 — equal-chord pair

If two convex pockets have the same chord length `s` and old-chain lengths
`ell_1,ell_2`, then

```math
\boxed{
area(P_1)+area(P_2)
\le\frac{(\ell_1+\ell_2)^2}{4\pi}.
}
\tag{RP.4}
```

#### Proof

Place the equal chords on top of one another with the pockets on opposite sides.  The
old chains form a rectifiable Jordan curve; the common chord becomes internal.  Its
perimeter is `ell_1+ell_2` and its enclosed area is exactly the sum of the pocket
areas.  The planar isoperimetric inequality gives RP.4. `square`

If the two chord lengths differ by `o(D)`, a radial rescaling by `1+o(1)` equalizes
them and changes lengths by `o(D)` and areas by `o(D^2)`, so RP.4 remains valid at
quadratic scale.

For a macroscopic pocket with `s_P=o(D)`, its own chain together with its chord is a
Jordan curve of perimeter `ell_P+o(D)`.  Isoperimetry gives

```math
area(P)\le\frac{\ell_P^2}{4\pi}+o(D^2).
\tag{4.2}
```

### Theorem RP.3 — paired outer-pocket capacity

Along every bounded-`mu` post-ZF sequence for which

```math
\frac{d_P}{D}\to\tau,
```

one has

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
\le\frac{\tau^2}{4\pi}.
}
\tag{RP.5}
```

#### Proof

Fix `epsilon>0` and call a pocket small when `x_P<epsilon D`.  The reflection bound

```math
area(P)\le\frac{\ell_P^2}{2\pi}
```

and

```math
\sum_P\ell_P=d_P+2a=O(D)
```

show that all small pockets together have area `O(epsilon D^2)+O(D)`.  Here
`d_P=O(D)` follows from RP.3 and `h=O(D)`, while `a<=q=O(D)`.

Only `O_epsilon(1)` macroscopic pockets remain.  Pass to a subsequence on which all
normalized chord and chain lengths converge.  Pair every positive limiting chord by
Section 3 and use RP.4.  Treat every zero-limiting-chord pocket by (4.2).

If the normalized total chain lengths of the resulting disjoint groups are
`m_1,...,m_t`, then

```math
\limsup\frac{H_{out}}{D^2}
\le\frac1{4\pi}\sum_jm_j^2+O(\epsilon).
```

The retained macroscopic chain mass is at most `tau+o(1)`, because each retained
`ell_P=x_P+2` and there are only `O_epsilon(1)` retained pockets.  Therefore

```math
\sum_jm_j^2\le\left(\sum_jm_j\right)^2\le\tau^2.
```

Let `epsilon downarrow0`. `square`

---

## 5. Add exceptional faces and use the renormalized budget

The canonical exceptional-face estimate gives

```math
\limsup\frac{A_{exc}}{D^2}
\le\frac{\nu^2}{4\pi}.
\tag{5.1}
```

RP.5 and (5.1) imply

```math
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le\frac{\tau^2+\nu^2}{4\pi}
\le\frac{(\tau+\nu)^2}{4\pi}.
\tag{5.2}
```

Insert (2.7):

```math
\boxed{
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le
\frac{(\mu+y)^2}{16\pi}.
}
\tag{5.3}
```

ZG charges the gap region to the outer pockets and exceptional faces up to `o(D^2)`,
so

```math
\boxed{
\limsup\frac G{D^2}
\le
\frac{(\mu+y)^2}{16\pi}.
}
\tag{5.4}
```

Combine with the whole-source lower requirement (1.6).  Every survivor subsequential
limit must satisfy

```math
\boxed{
\Phi(y)
\le
\frac\pi4\mu^2
+
\frac{(\mu+y)^2}{16\pi},
\qquad
2\rho\le y\le\pi.
}
\tag{RP.6}
```

This is the new all-phase feasible-region inequality.

---

## 6. Exact optimization

For fixed `mu>=0`, define

```math
F_\mu(y)
:=
\frac{y+\sin y}{4}
-
\frac\pi4\mu^2
-
\frac{(\mu+y)^2}{16\pi}.
\tag{6.1}
```

RP.6 requires `F_mu(y)<=0` for at least one `y in [2rho,pi]`.

Differentiate twice:

```math
F_\mu''(y)
=-\frac{\sin y}{4}-\frac1{8\pi}<0
\qquad(0<y<\pi).
\tag{6.2}
```

Thus `F_mu` is strictly concave on the entire DB interval.  Its minimum occurs at an
endpoint.

### 6.1 The `y=pi` endpoint

At `y=pi`,

```math
F_\mu(\pi)
=
\frac{3\pi^2-2\pi\mu-(4\pi^2+1)\mu^2}{16\pi}.
\tag{6.3}
```

The numerator is strictly decreasing for `mu>=0`, is positive at `mu=0`, and has the
unique positive root

```math
\boxed{
\mu_{RP}
=
\frac{\pi\left(2\sqrt{3\pi^2+1}-1\right)}{4\pi^2+1}.
}
\tag{6.4}
```

Hence

```math
\mu<\mu_{RP}
\quad\Longrightarrow\quad
F_\mu(\pi)>0.
\tag{6.5}
```

Also `mu_RP<4/5`: at `mu=4/5`, the numerator of (6.3) is

```math
\frac1{25}(11\pi^2-40\pi-16)<0,
```

because `pi<4` gives `11pi^2<44pi` and then `4pi-16<0`.

### 6.2 The `y=2rho` endpoint

Since `F_mu(2rho)` strictly decreases with `mu`, it is enough to show

```math
F_{4/5}(2\rho)>0.
```

Use the elementary audited bracket

```math
\frac{739}{1000}<\rho<\frac{37}{50}.
\tag{6.6}
```

The bracket follows directly from the alternating Taylor bounds for cosine at the two
rational endpoints.  Since `rho<37/50`,

```math
\sin\rho=\sqrt{1-\rho^2}
>
\frac{84}{125},
```

because

```math
\left(\frac{84}{125}\right)^2
<1-\left(\frac{37}{50}\right)^2.
```

Therefore

```math
\sin(2\rho)=2\rho\sin\rho
>
2\frac{739}{1000}\frac{84}{125}
=
\frac{15519}{15625}.
```

Thus

```math
\Phi(2\rho)
>
\frac14\left(
\frac{1478}{1000}+\frac{15519}{15625}
\right)
=
\frac{154451}{250000}
=0.617804.
\tag{6.7}
```

On the other hand, using `pi<22/7`, `pi>3`, and `2rho<37/25`,

```math
\frac\pi4\left(\frac45\right)^2
+
\frac{(4/5+2\rho)^2}{16\pi}
<
\frac{42781}{70000}
=0.6111571428\ldots .
\tag{6.8}
```

The exact rational margin is

```math
\frac{154451}{250000}-\frac{42781}{70000}
=
\frac{727}{109375}>0.
\tag{6.9}
```

Hence

```math
F_\mu(2\rho)>0
\qquad(0\le\mu\le\mu_{RP}).
\tag{6.10}
```

### 6.3 Conclusion

If `mu<mu_RP`, both endpoint values of the strictly concave function `F_mu` are
positive.  Therefore `F_mu(y)>0` for every `y in [2rho,pi]`, contradicting RP.6.
This proves RP.1.

The exact root has numerical value

```math
\mu_{RP}=0.7811638359065726\ldots .
```

For a proof-level rational bracket, the numerator in (6.3) is positive at
`mu=39/50=0.78` (already using `pi>3.14`) and negative at `mu=4/5`, so

```math
\boxed{0.78<\mu_{RP}<0.8.}
\tag{6.11}
```

---

## 7. The old low-`mu` phase is now empty

PT defined

```math
u_\pi
=\frac{\pi(\sqrt{3\pi^2+4}-1)}{2(\pi^2+1)}.
```

For completeness, `u_pi<0.70` follows from `pi<22/7`, `pi>157/50`, and

```math
\sqrt{1648}<\frac{203}{5}.
```

Indeed

```math
u_\pi
<
\frac{528}{35}\frac{1250}{27149}
<\frac7{10}.
\tag{7.1}
```

Together with (6.11),

```math
\boxed{\mu_{RP}>0.78>0.70>u_\pi.}
\tag{7.2}
```

Therefore the preceding phase split collapses to the high-renormalized-surplus side:
for every sufficiently large post-ZF survivor,

```math
\boxed{
\mu_D>u_\pi+\Omega(1).
}
\tag{7.3}
```

The macroscopic inactive outer-shell theorem is still correct as a conditional
statement, but it is no longer a live survivor branch.

---

## 8. Equality / near-endpoint information

A sequence approaching `mu_RP` must approach the binding concavity endpoint

```math
\boxed{h/D\to\pi.}
\tag{8.1}
```

because the other endpoint has a fixed positive margin and strict concavity excludes
interior equality.

Equality in (5.2) and RP.3 further forces, at leading order,

```math
\tau\nu\to0,
\qquad
\tau+\nu\to\frac{\mu_{RP}+\pi}{2},
\tag{8.2}
```

and equality in the two PC-derived bounds used in RP.3.  Since `h/D->pi`, the
projective diameter-direction set is asymptotically maximally dense.  This is a very
different endpoint from the old RSR/GR optimizer near `h/D=1.51`.

No contradiction from this endpoint is claimed here.  The next attack should retain
the finite `-s_Z` improvement in (2.6), the exact perimeter bound `q<=P_F<=pi D`, and
the paired-pocket chord/detour information instead of discarding them in RP.3.

---

## 9. Regression audit

| Claim / regression | Status | Reason |
| --- | --- | --- |
| exact budget RP.3 | proved finite | PC.2 + PC/TN boundary identity; `k` cancels algebraically |
| midpoint Hausdorff estimate | proved finite from FS.4 | each generator is within the midpoint error of a loaded endpoint and conversely |
| macroscopic opposite-side pairing | proved asymptotically | midpoint polygon is centrally symmetric; radial annulus prevents subdivision across a limiting flat |
| paired capacity RP.5 | proved asymptotically | pair/glue isoperimetry + zero-chord isoperimetry + small-pocket truncation |
| exceptional-face combination | proved | `tau^2+nu^2<=(tau+nu)^2` |
| feasible inequality RP.6 | proved | FSDB/GR lower gap + ZG + paired cavity upper bound |
| optimization / exact root | proved analytically | strict concavity reduces to two endpoints |
| regular odd shell | survives local geometry | RP uses the full-source GR/FSDB comparison, which synthetic shells lack as a global-minimum certificate |
| dense isolated filling | retained | no source point is deleted; global optimality enters through FSDB/GR |
| one giant zero-chord pocket | allowed | RP.5 has exactly the `1/(4pi)` coefficient for that case |
| Level I | still open | no upper bound contradicting `mu>=mu_RP` yet |

---

## 10. Failed / superseded routes

1. The previous PT-L inactive outer-shell branch is **superseded as a live branch** by
   RP.1 because `mu_RP>u_pi`.
2. Merely combining the unrenormalized paired-lens lower bound on
   `lambda=(e_BB+2s_C)/D` with GR leaves an uncontrolled `3k/D` gap.  RP.3 is the
   missing cancellation: it bounds the actual pocket/face currency directly in `mu`.
3. C37-C40 incidence alone still does not upper-bound the high-`mu` component face
   defect.  RP does not claim otherwise.
4. No equality uniqueness statement from Rogalski-Saint Raymond is used.

---

## 11. Promotion recommendation

**Hold as report pending independent audit.**  RP.1 is substantially stronger than GR
and changes the live phase structure, but it depends on the report-level FS.4/FSDB/ZG
and PC/TN stack.  The proof of the new algebraic cancellation and the endpoint
optimization is self-contained here.

If promoted, update:

- `docs/targets/target-c/README.md`;
- the active Target C continuation prompt;
- the current C-II frontier module;
- `research/README.md` with the exact check script.

---

## 12. Next run

The highest-value next theorem is a **strict renormalized paired-pocket stability
upgrade**.  RP.1 has a clean endpoint `h/D->pi`.  Retain instead of discarding:

```math
2(d_P+Q)\le\mu_DD+h-s_Z,
```

`q<=P_F<=pi D`, and the actual pocket chord/detour budget.  Any fixed deficit
`pi-h/D` or positive `s_Z/D` lowers the cavity capacity.  A quantitative argument
should either raise `mu_RP` again or force

```math
h/D\to\pi,\quad s_Z/D\to0,
```

where the diameter graph and force hull are near the maximally dense projective
configuration and may admit a direct structural contradiction.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New exact finite budget:
  k=d_H+s_Z,
  X=d_P+Q.
PC gives
  e_BB=X+2k+c_B,
  q=a+X+2k,
while q=h+d_H.  Hence
  X<=mu_D D+k,
  X<=h-k,
and therefore
  2X<=mu_D D+h
(with the stronger RHS mu_D D+h-s_Z available).

FS midpoint geometry pairs every macroscopic OP hull chord with an asymptotically
equal opposite chord.  Gluing each pair and using isoperimetry gives
  H_out/D^2 <= tau^2/(4pi), tau=d_P/D.
Zero-chord macroscopic pockets have the same coefficient by direct isoperimetry.
Together with A_exc<=nu^2 D^2/(4pi), nu=Q/D,
  G/D^2 <= (tau+nu)^2/(4pi)
          <= (mu+y)^2/(16pi).
GR/ZK+FSDB gives
  G/D^2 >= Phi(y)-pi mu^2/4,
  Phi(y)=(y+sin y)/4,
so every survivor limit needs
  Phi(y)<=pi mu^2/4+(mu+y)^2/(16pi), 2rho<=y<=pi.

The difference is strictly concave in y, so only y=2rho and y=pi matter.
The 2rho endpoint stays positive through mu=4/5 with exact rational margin
  727/109375.
The pi endpoint vanishes at
  mu_RP = pi(2sqrt(3pi^2+1)-1)/(4pi^2+1)
        = 0.7811638359065726... .
Therefore
  liminf mu_D >= mu_RP.
Since mu_RP>0.78>0.70>u_pi=0.6932725...,
the previous low-mu inactive-outer-shell survivor phase is empty.

Next:
retain the -s_Z term, perimeter/q constraints, and paired chord/detour data to
quantify stability away from the h/D->pi endpoint or contradict that endpoint.
```
