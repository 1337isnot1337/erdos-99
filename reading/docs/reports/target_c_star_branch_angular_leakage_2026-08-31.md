> Generated reading edition · [exact source](../../../docs/reports/target_c_star_branch_angular_leakage_2026-08-31.md) · source SHA-256 `df7e69e3ad0a360e126ad6f1d9769dfcaa70f663f4cc9d153e0d117d734866b5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4CB09197EFFF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C71: star-branch angular leakage

**Date:** 2026-08-31  
**Repository base:** `c130e1a7` (main after C70 / PR #74)  
**Run type:** exact KKT cut-force / local geometry theorem  
**Target:** Target C Gate C-II, near-zero response-defect phase  
**Depends on:** C18 explicit shared-endpoint diameter-angle gap, C35 terminal contact-degree cap, C65 full diameter visibility, C66 mechanical star concentration, C68 radialization, C70 boundary-response starization  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C66 proves that if

$$
\varepsilon:=\frac12\operatorname{tr}(\Lambda-L_H)
$$

satisfies `D epsilon -> 0`, then one diameter vertex `z` carries `1-o(1)` of the
normalized diameter stress. C68 shows that the contact-stress measure around the same
`z` is almost radial, and C70 shows that the boundary electrical response also
starizes around `z`.

C71 adds a local mechanical restriction that neither statement gives by itself. The
large-`D` global diameter geometry puts all diameter partners of `z` in a cone of
width strictly below `60` degrees, while two distinct unit-contact neighbors of `z`
must be separated by at least `60` degrees. The exact KKT cut-force law then implies:

> a near-zero mechanical diameter star cannot split macroscopic star load across two
> independent one-contact ports at its center.

Quantitatively, after deleting `z` from the positive contact graph, let `w_1>=w_2`
be the two largest amounts of `z`-star diameter weight carried by components attached
back to `z` through exactly one contact edge. If

$$
\delta_z:=1-\sum_{h\ni z}\beta_h,
$$

then

$$
\boxed{\delta_z\ge q_D w_2,}
$$

where `q_D>0` is explicit and tends to a positive constant. Hence in the C66 regime
`D epsilon ->0`, either a component returning to `z` through at least two contact
edges carries nonvanishing star mass, or one single physical contact port carries
`1-o(1)` of the star mass and has contact stress `Omega(D)`.

This splits the current C-II near-zero obstruction into a return/cycle phase and a
single-port high-stress spine phase.

---

## 1. Setup

Work in the C65 lexicographically normalized hypothetical C-II source. Thus one
relative-interior normalized KKT stress is positive on the entire actual contact graph
`C` and the entire actual diameter graph `H`, with

$$
\sum_{h\in H}\beta_h=1.
\tag{C71.1}
$$

Fix a diameter vertex `z`. Put

$$
S_z:=\sum_{za\in H}\beta_{za},
\qquad
\delta_z:=1-S_z.
\tag{C71.2}
$$

Thus `delta_z` is exactly the total normalized diameter weight on edges not incident
to `z`.

For two diameter partners `a,b` of `z`, C18 gives

$$
\angle azb<\Theta_D,
\tag{C71.3}
$$

where

$$
\Theta_D:=
\frac{
D\left(\frac{5\pi}{6}-\sqrt3\right)
+\frac{4\pi}{3}
+\frac{\pi}{2D}
}{D+1}.
\tag{C71.4}
$$

For `D>=20`, `Theta_D<pi/3`. Define

$$
\eta_D:=\frac\pi3-\Theta_D>0,
\qquad
c_D:=\cos\frac{\Theta_D}{2},
\qquad
q_D:=c_D\sin\frac{\eta_D}{2}>0.
\tag{C71.5}
$$

As `D->infinity`,

$$
\Theta_D\to\theta_\infty:=\frac{5\pi}{6}-\sqrt3,
$$

so

$$
q_D\to q_\infty
:=
\cos\frac{\theta_\infty}{2}
\sin\frac{\pi/3-\theta_\infty}{2}
=0.0727\ldots>0.
\tag{C71.6}
$$

The strict positivity of this limit is the only constant-level fact needed below.

---

## 2. Single-port components and their cut law

Delete `z` from the positive contact graph. Let `R` be one connected component of
`C-z`.

Call `R` **single-port** if exactly one contact edge joins it back to `z`; write that
edge as

$$
z x_R,\qquad x_R\in R.
$$

Define the `z`-star mass carried by `R`:

$$
w_R:=
\sum_{\substack{za\in H\\a\in R}}
\beta_{za}.
\tag{C71.7}
$$

Define also the total non-star diameter weight crossing the vertex cut
`(R,V\setminus R)`:

$$
\lambda_R:=
\sum_{\substack{bk\in H,\ b\in R,\ k\notin R\\z\notin\{b,k\}}}
\beta_{bk}.
\tag{C71.8}
$$

Every term in `lambda_R` is a non-star diameter edge, hence

$$
0\le\lambda_R\le\delta_z.
\tag{C71.9}
$$

Sum the KKT equilibrium equation over all vertices of `R`. Every internal contact
force cancels. Since `R` is single-port, the only surviving contact force is the port
edge. Internal diameter reactions also cancel. We obtain

$$
\alpha_{z x_R}(p_{x_R}-p_z)
=
D\sum_{\substack{za\in H\\a\in R}}
\beta_{za}u_a
+E_R,
\tag{C71.10}
$$

where

$$
u_a:=\frac{p_a-p_z}{D},\qquad |u_a|=1,
$$

and `E_R` is the vector sum of the non-star diameter reactions crossing the cut.
Every such diameter vector has length `D`, so

$$
|E_R|\le D\lambda_R.
\tag{C71.11}
$$

Put

$$
V_R:=D\sum_{\substack{za\in H\\a\in R}}
\beta_{za}u_a.
\tag{C71.12}
$$

All vectors `u_a` lie in the common angular interval of the diameter star at `z`, of
width at most `Theta_D`. Projection onto the interval bisector gives

$$
\boxed{|V_R|\ge D c_D w_R.}
\tag{C71.13}
$$

Whenever `w_R>0`, the direction of the positive vector sum `V_R` also lies inside
that same interval.

---

## 3. Angular leakage through one port

Let

$$
v_R:=p_{x_R}-p_z,
\qquad |v_R|=1,
$$

and assume `w_R>0`. Let `phi_R` be the smaller angle between `v_R` and `V_R`.
Equation C71.10 says that the error vector `E_R` moves `V_R` onto the ray spanned by
`v_R`.

For any nonzero vector `V`, the Euclidean distance from `V` to a ray making angle
`phi` with it is at least `|V| sin psi` whenever `phi>=psi` and
`0<=psi<=pi/2`. Therefore C71.10-C71.13 imply:

### Lemma C71.1 — single-port angular leakage

If `w_R>0` and `phi_R>=psi`, where `0<=psi<=pi/2`, then

$$
\boxed{
\lambda_R\ge c_D w_R\sin\psi.
}
\tag{C71.14}
$$

Thus rotating a macroscopic diameter-star resultant away from its one physical contact
port requires macroscopic non-star diameter weight. This is an exact KKT force
statement, not an electrical-response estimate.

---

## 4. Two independent ports force non-star diameter weight

Let `R` and `S` be distinct single-port components with positive star masses. Their
port neighbors `x_R,x_S` are distinct source points at unit distance from `z`.
Unit separation gives

$$
|x_R-x_S|
=2\sin\frac{\angle x_R z x_S}{2}
\ge1,
$$

hence

$$
\angle x_R z x_S\ge\frac\pi3.
\tag{C71.15}
$$

On the other hand, both `V_R` and `V_S` lie in the common diameter-star angular
interval, so

$$
\angle(V_R,V_S)\le\Theta_D.
\tag{C71.16}
$$

The angular triangle inequality gives

$$
\phi_R+\phi_S
\ge
\frac\pi3-\Theta_D
=\eta_D.
\tag{C71.17}
$$

Therefore at least one of `phi_R,phi_S` is at least `eta_D/2`. Apply C71.1 to that
component, then C71.9.

### Theorem C71.2 — two-port leakage

For any two distinct single-port components `R,S` with positive star masses,

$$
\boxed{
\delta_z\ge q_D\min\{w_R,w_S\}.
}
\tag{C71.18}
$$

Equivalently, if

$$
w_1\ge w_2\ge w_3\ge\cdots
$$

are the positive star masses of all single-port components, then

$$
\boxed{w_2\le\frac{\delta_z}{q_D}.}
\tag{C71.19}
$$

This is the main new quantitative statement.

---

## 5. Use the physical contact-degree cap

C35 gives

$$
\deg_C(z)\le3
\tag{C71.20}
$$

because `z` is a loaded boundary terminal.

Call a component of `C-z` **multi-port** if at least two distinct contact edges from
`z` enter it. There can be at most one such component. Let `W_multi` be its total
`z`-star diameter mass, taking `W_multi=0` when no multi-port component exists.

There are at most three single-port components. By C71.19, all but the largest of
their star masses sum to at most `2 delta_z/q_D`. Therefore some single-port
component `R` satisfies

$$
\boxed{
w_R
\ge
S_z-W_{\rm multi}-\frac{2\delta_z}{q_D}.}
\tag{C71.21}
$$

For this `R`, project C71.10 onto the bisector of the diameter-star cone. The star
term contributes at least `D c_D w_R`, while the error loses at most
`D lambda_R<=D delta_z`. Since the left side has magnitude
`alpha_{zx_R}`, we get

$$
\boxed{
\alpha_{zx_R}
\ge
D(c_D w_R-\delta_z).}
\tag{C71.22}
$$

Thus a dominant single port is automatically a high-stress physical contact.

---

## 6. Insert the C66 star-concentration estimate

C66 gives a diameter vertex `z` such that

$$
S_z\ge1-C_0D\varepsilon,
\qquad
C_0:=\frac{2\pi}{\kappa_0},
\tag{C71.23}
$$

where

$$
\kappa_0=\frac{2\gamma_0}{1+2\gamma_0}>0.
$$

Hence

$$
\delta_z\le C_0D\varepsilon.
\tag{C71.24}
$$

Combining C71.21-C71.24 gives the promised near-zero normal form.

### Theorem C71 — branch concentration at the C66 star center

Along any hypothetical C-II sequence satisfying

$$
D\varepsilon\longrightarrow0,
\tag{C71.25}
$$

choose the C66 star center `z`. Then one of the following holds along a subsequence.

1. **Return/cycle phase:** the multi-port component of `C-z` carries star mass bounded
   away from zero.
2. **Single-port phase:** one single-port component `R` satisfies
   $$
   \boxed{w_R\longrightarrow1,}
   \tag{C71.26}
   $$
   and its unique contact port obeys
   $$
   \boxed{
   \alpha_{zx_R}\ge(c_\infty-o(1))D,
   }
   \tag{C71.27}
   $$
   where
   $$
   c_\infty
   :=\cos\left(\frac{5\pi}{12}-\frac{\sqrt3}{2}\right)
   =0.90348\ldots .
   $$

Indeed, if `W_multi` does not stay bounded away from zero, pass to a subsequence with
`W_multi->0`; then C71.21, C71.23, and `delta_z->0` give `w_R->1`, and C71.22 gives
C71.27.

So the C66/C68/C70 near-zero phase cannot have two independent macroscopic physical
branches issuing from its common star center.

---

## 7. Relation to C68 and C70

C71 is not a restatement of either newer theorem.

- C68 controls the **aggregate transverse contact-stress energy**
  $$
  Q_z=\sum_C\alpha_{ij}[1-(r_i-r_j)^2]
  $$
  and gives `Q_z=o(D^2)` when `D epsilon->0`.
- C70 controls the **boundary response support** and gives total non-`z` response
  conductance `X_z=o(1)` in the same regime.
- C71 controls the **physical contact topology at z**. The strict C18 angle gap forces
  the mechanical star load either into a returning component or through one dominant
  contact port.

The three reductions are complementary. Together the single-port survivor is an
almost-radial, electrically starized framework whose dominant physical port has
stress of order `D`.

---

## 8. Exact next targets

C71 splits the remaining near-zero obstruction into two smaller mechanical problems.

### C71-A — return/cycle branch

A component attached to `z` by at least two unit contacts carries a nonvanishing
fraction of the diameter-star load. A closing estimate should convert the resulting
physical return path into quantitative non-`z` boundary response, contradicting C70.
The exact C58/C60 separator theorem identifies the zero-transfer limit; what is missing
is quantitative stability.

### C71-B — single-port spine branch

One contact edge has stress at least `(c_infty-o(1))D` and enters the component
carrying essentially the whole diameter-star load. The natural next move is to iterate
the cut law through that component. Either a return event occurs, or one obtains a
long nearly radial high-stress spine. C26 rules out a truly neutral unloaded degree-two
corridor, so every internal structural vertex must spend positive side incidence.
The unresolved issue is quantitative: those side stresses can still be arbitrarily
small.

C42 near-quadrangulation, C48 force-visible capacity, and C68 angular-energy control
are the strongest available inputs for charging that side incidence.

---

## 9. Regression audit

- A pure one-branch mechanical star is allowed and lands in C71-B.
- A contact cycle or two-port return through `z` is allowed and lands in C71-A.
- Tiny non-star diameter weights are allowed and appear explicitly as `delta_z`.
- The proof uses the physical contact-degree bound, not an abstract electrical degree
  bound.
- The positive constant `q_D` comes from global minimum-diameter geometry through C18.
  With only the elementary `60`-degree diameter-star bound, `q_D` would be zero and
  the theorem would disappear.
- No lower bound on individual side stresses, no lattice assumption, and no rattler
  exclusion is used.

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C71:
For the C66 star center z, let delta_z be total non-z diameter weight. If R is a
component of C-z attached through one physical contact, let w_R be its z-star beta
mass. C18 gives diameter-star cone width Theta_D<pi/3 for D>=20. Two distinct unit
contact ports are separated by >=pi/3.

Exact KKT cut equilibrium gives
  delta_z >= q_D min(w_R,w_S)
for two single-port components, where q_D->0.0727...>0.
Thus the second-largest single-port star mass is O(delta_z).

Since deg_C(z)<=3, either a multi-port return component carries nonvanishing star
mass, or one single port carries 1-o(1) star mass. In the latter case
  alpha_port >= (0.90348...-o(1)) D.

With C66, D epsilon->0 implies delta_z->0. Hence the near-zero C-II obstruction is
reduced to:
  A. return/cycle at z, or
  B. one Omega(D)-stress almost-radial spine port.
Next: quantitative separator stability for A or side-incidence/rhombic charging for B.
```
