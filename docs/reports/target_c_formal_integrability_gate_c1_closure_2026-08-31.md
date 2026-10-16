<!-- migration-source: path=docs/reports/target_c_formal_integrability_gate_c1_closure_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=26dd55ef187748f32700c77aad22aab960d5c561; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C: formal integrability and Gate C-I closure

**Date:** 2026-08-31  
**Repository base:** `f173aa9b` (main after C62 / PR #64)  
**Run type:** exact formal-series Farkas induction + real-closed-field transfer  
**Target:** Target C Gate C-I  
**Depends on:** C6 strong/weak support duality, C53-C54 universal PSD for every normalized KKT stress

## LEVEL I STATUS

**STILL OPEN, BUT GATE C-I IS CLOSED.**

This report proves that a contact-minimal triangle-free global minimizer has **no weak unit contacts**:

\[
\boxed{C=C_*.}
\]

The proof is substantially shorter than the preceding body-hinge route and removes the final jet-stitching issue from C62.

The key observation is that universal PSD is not merely a second-order statement. For every normalized KKT stress `s`, the weighted sum of the exact signed active distance gaps under an arbitrary displacement `Y` is the PSD quadratic form

\[
\boxed{
\sum_e\lambda_e G_e(Y)
=
\operatorname{tr}(Y^{\mathsf T}\Omega_sY)\ge0.
}
\]

This identity rules out a Farkas obstruction at **every formal Taylor order**. Starting with C6's relative-interior velocity that strictly releases every weak row, one recursively chooses all higher formal coefficients so that every strong active signed gap has nonnegative first nonzero coefficient. This gives a feasible configuration over the ordered formal Laurent-series field.

No convergence theorem is needed. Embed that field in its real closure. Tarski quantifier elimination for real closed fields transfers the existence of the infinitesimally displaced feasible configuration back to arbitrarily close real configurations. All weak contacts are strict there, all initially inactive pairs remain noncontacts, and all pair distances remain at most `D`. Global optimality forces diameter exactly `D`, contradicting contact minimality.

Thus Target C no longer needs any finite-integration regularity assumption in Gate C-I.

## 1. Exact signed active gaps

Let `A={p_1,...,p_n}` be a contact-minimal triangle-free global minimizer of diameter `D>1`.

For an active pair `e=ij`, write

\[
d_e=p_i-p_j.
\]

Set

\[
\sigma_e=
\begin{cases}
+1,&e\in C,\\
-1,&e\in H.
\end{cases}
\tag{C63.1}
\]

For a displacement field

\[
Y=(y_1,\ldots,y_n),
\]

define the signed linear row

\[
r_e(Y)=\sigma_e\,d_e\cdot(y_i-y_j)
\tag{C63.2}
\]

and the **exact signed active gap**

\[
\boxed{
G_e(Y)
=\sigma_e\left(|d_e+y_i-y_j|^2-|d_e|^2\right).
}
\tag{C63.3}
\]

Because active contacts have length one and active diameter pairs have length `D`, feasibility of the active row is exactly

\[
G_e(Y)\ge0.
\]

Expanding,

\[
\boxed{
G_e(Y)=2r_e(Y)+\sigma_e|y_i-y_j|^2.
}
\tag{C63.4}
\]

The fixed-diameter critical cone is the linearized system

\[
r_e(v)\ge0
\qquad(e\in C\cup H).
\tag{C63.5}
\]

## 2. Start with the C6 relative-interior release velocity

Assume for contradiction that there is at least one weak unit contact:

\[
C\setminus C_*\ne\varnothing.
\tag{C63.6}
\]

C6 supplies

\[
v\in\operatorname{ri}\mathcal K_D(A)
\tag{C63.7}
\]

such that

\[
r_e(v)=0\qquad(e\in E_*=C_*\cup H_*),
\tag{C63.8}
\]

while

\[
r_e(v)>0
\qquad(e\in (C\cup H)\setminus E_*).
\tag{C63.9}
\]

In particular every weak unit contact is already strict at the first formal order.

We shall construct a formal displacement

\[
Y(t)=\sum_{m\ge1}t^mY_m,
\qquad
Y_1=v,
\tag{C63.10}
\]

such that

\[
G_e(Y(t))\ge0
\]

in the ordered formal-power-series sense for every active row.

Weak rows are done at order one. Only the strong rows require recursion.

## 3. The exact PSD aggregate identity

Let

\[
\lambda=(\alpha,\beta)\ge0
\]

be any nonzero nonnegative dependence among a subset of the signed active rows:

\[
\sum_e\lambda_e r_e(\cdot)=0.
\tag{C63.11}
\]

Equivalently, the corresponding signed edge forces satisfy vertex equilibrium.

A nonzero nonnegative equilibrium dependence cannot be supported only on contacts. The standard free-framework extreme-vertex argument gives this directly: choose a vertex uniquely extreme in a generic direction among the vertices incident to positive stress; every positive incident contact force has a strictly positive projection there.

Hence

\[
\sum_H\beta_h>0.
\]

Normalize it to one. Dotting equilibrium with the source coordinates gives the scalar and tensor KKT identities, so the normalized dependence is a normalized KKT stress. By C53-C54,

\[
\Omega_\lambda
=L_C(\alpha)-L_H(\beta)
\succeq0.
\tag{C63.12}
\]

Now sum the exact signed gaps (C63.4). The linear part cancels by equilibrium:

\[
\sum_e\lambda_e r_e(Y)=0.
\]

Therefore

\[
\boxed{
\sum_e\lambda_eG_e(Y)
=
\sum_C\alpha_e|y_i-y_j|^2
-
\sum_H\beta_h|y_i-y_j|^2
=
\operatorname{tr}(Y^{\mathsf T}\Omega_\lambda Y).
}
\tag{C63.13}
\]

Because `Omega_lambda` is PSD, choose a real matrix square root

\[
\Omega_\lambda=B_\lambda^{\mathsf T}B_\lambda.
\]

Then

\[
\boxed{
\sum_e\lambda_eG_e(Y)
=\|B_\lambda Y\|_F^2\ge0
}
\tag{C63.14}
\]

for **every** displacement field `Y`, with no smallness, criticality, or support assumption.

This identity is the engine of the formal induction.

## 4. One formal Taylor step

Suppose real coefficient fields

\[
Y_1,\ldots,Y_{k-1}
\]

have been chosen. Let

\[
Y_{<k}(t)=\sum_{m=1}^{k-1}t^mY_m.
\]

Let `F_{k-1}` be the set of strong active rows whose signed gap has vanished through every order below `k`:

\[
[t^j]G_e(Y_{<k}(t))=0
\qquad(1\le j<k).
\tag{C63.15}
\]

Rows that have already acquired a positive leading coefficient need no further control.

For `e in F_{k-1}`, the coefficient of `t^k` after adding `t^kY_k` is

\[
\boxed{
2r_e(Y_k)+c_{e,k},
}
\tag{C63.16}
\]

where `c_{e,k}` is the coefficient of `t^k` in the quadratic term

\[
\sigma_e|\Delta Y_{<k}(t)|^2.
\]

Thus the next coefficient can be made nonnegative precisely when the finite linear system

\[
2r_e(Y_k)+c_{e,k}\ge0
\qquad(e\in F_{k-1})
\tag{C63.17}
\]

is feasible.

### Lemma C63.1 (every formal coefficient step is feasible)

System (C63.17) is feasible for every `k>=2`.

#### Proof

Suppose it were infeasible. Farkas' alternative gives nonnegative coefficients

\[
\lambda_e\ge0
\qquad(e\in F_{k-1}),
\]

not all zero, such that

\[
\sum_{e\in F_{k-1}}\lambda_e r_e(\cdot)=0
\tag{C63.18}
\]

and

\[
\sum_{e\in F_{k-1}}\lambda_ec_{e,k}<0.
\tag{C63.19}
\]

By Section 3, normalize `lambda` to a KKT stress with PSD stress matrix.

Every row in its support lies in `F_{k-1}`. Hence every coefficient below order `k` of each individual signed gap is zero. Therefore the weighted sum

\[
S_\lambda(t)
:=
\sum_e\lambda_eG_e(Y_{<k}(t))
\tag{C63.20}
\]

has zero coefficients below order `k`.

By (C63.13),

\[
S_\lambda(t)
=
\operatorname{tr}
\left(
Y_{<k}(t)^{\mathsf T}\Omega_\lambda Y_{<k}(t)
\right)
=
\|B_\lambda Y_{<k}(t)\|_F^2.
\tag{C63.21}
\]

This is a sum of squares of real polynomials in `t`. Its first nonzero coefficient, if any, occurs at an even order and is strictly positive. Since all coefficients below `k` vanish, its coefficient at order `k` cannot be negative.

But the linear weighted contribution of `Y_k` cancels by (C63.18), and `Y_{<k}` has no order-`k` linear term. Therefore

\[
[t^k]S_\lambda(t)
=
\sum_e\lambda_ec_{e,k},
\]

contradicting (C63.19). \(\square\)

## 5. Recursive formal integrability

Set

\[
Y_1=v.
\]

Every weak active row has a positive order-one coefficient by (C63.9). Every strong active row has zero order-one coefficient.

Apply Lemma C63.1 successively for

\[
k=2,3,4,\ldots
\]

to choose `Y_k`.

At each step, for every still-unresolved strong row choose a nonnegative order-`k` coefficient. If it is positive, that row is permanently resolved. If it is zero, retain the row for the next stage.

This constructs

\[
Y(t)=\sum_{m\ge1}t^mY_m
\in\mathbb R[[t]]^{2n}.
\tag{C63.22}
\]

For every active row `e`, exactly one of the following holds:

1. `G_e(Y(t))` has a first nonzero coefficient and that coefficient is positive;
2. every coefficient vanishes, so `G_e(Y(t))=0` as a formal series.

Hence in the standard ordering of the formal Laurent-series field,

\[
\boxed{
G_e(Y(t))\ge0
\quad\text{for every active row}.}
\tag{C63.23}
\]

Moreover every weak active row satisfies

\[
\boxed{G_e(Y(t))>0}
\tag{C63.24}
\]

because its order-one coefficient was already positive.

No convergence of the formal series is asserted or needed.

## 6. Inactive constraints remain strict over the infinitesimal field

Let

\[
\mathbb K_0=\mathbb R((t))
\]

be the formal Laurent-series field ordered by the sign of the first nonzero coefficient, with `t>0` infinitesimal.

Every coordinate of `Y(t)` lies in `t\mathbb R[[t]]`, so it is infinitesimal.

For any pair `ij` that was not a unit contact at the source,

\[
|p_i-p_j|^2-1>0
\]

is a positive real constant. Hence

\[
|p_i+Y_i(t)-p_j-Y_j(t)|^2-1>0
\tag{C63.25}
\]

in `K_0`.

Likewise, for any pair that was not a diameter pair,

\[
D^2-|p_i-p_j|^2>0
\]

is a positive real constant, so

\[
D^2-|p_i+Y_i(t)-p_j-Y_j(t)|^2>0.
\tag{C63.26}
\]

Combining (C63.23)-(C63.26), the formal configuration

\[
A(t)=\{p_i+Y_i(t):1\le i\le n\}
\tag{C63.27}
\]

satisfies

\[
1\le |p_i(t)-p_j(t)|\le D
\qquad(i\ne j)
\tag{C63.28}
\]

inside the ordered field.

Furthermore, every pair outside the strong contact set satisfies

\[
\boxed{
|p_i(t)-p_j(t)|>1
\qquad(ij\notin C_*).
}
\tag{C63.29}
\]

Indeed:

- weak unit contacts are strict at order one;
- initially inactive lower-distance constraints have positive constant slack.

Thus the formal contact graph is a subgraph of `C_*`.

## 7. Real-closed-field transfer gives actual nearby configurations

The ordered field `K_0` need not be real closed. Let

\[
\mathbb K
\]

be a real closure of `K_0` with the given ordering. Then `K` contains `R` as an ordered real-closed subfield and still contains the positive infinitesimal `t` and the formal configuration (C63.27).

Fix any real

\[
\varepsilon>0.
\]

Because every `Y_i(t)` is infinitesimal,

\[
\sum_i|Y_i(t)|^2<\varepsilon^2
\tag{C63.30}
\]

holds in `K`.

Consider the finite first-order formula over the language of ordered fields, with parameters given by the real source coordinates and `D`, asserting the existence of points `x_1,...,x_n` such that

\[
\sum_i|x_i-p_i|^2<\varepsilon^2,
\tag{C63.31}
\]

\[
1\le|x_i-x_j|\le D
\qquad(i\ne j),
\tag{C63.32}
\]

and

\[
|x_i-x_j|>1
\qquad(ij\notin C_*).
\tag{C63.33}
\]

The formal configuration makes this formula true in `K`.

The theory of real closed fields admits quantifier elimination. Consequently the ordered embedding

\[
\mathbb R\hookrightarrow\mathbb K
\]

is elementary. The same existential formula is therefore true over `R`.

We have proved:

### Theorem C63.2 (real realization of the formal release)

For every real `epsilon>0`, there is a real configuration

\[
A_\varepsilon=\{x_1,\ldots,x_n\}
\]

with

\[
\sum_i|x_i-p_i|^2<\varepsilon^2,
\]

all pair distances in `[1,D]`, and contact graph contained in `C_*`.

No analytic convergence or curve-selection theorem is required.

## 8. Gate C-I closes

The real configuration `A_epsilon` is unit-separated and has diameter at most `D`. Since `D=D(n)` is the global minimum possible diameter for `n` unit-separated points,

\[
\operatorname{diam}A_\varepsilon\ge D.
\]

Therefore

\[
\boxed{
\operatorname{diam}A_\varepsilon=D.
}
\tag{C63.34}
\]

Its contact graph is a subgraph of `C_*`. If the source had a weak unit contact, then

\[
C_*\subsetneq C,
\]

so `A_epsilon` has strictly fewer unit contacts than the contact-minimal source.

Because deleting contacts cannot create a unit triangle, `A_epsilon` is still triangle-free. This contradicts the definition of the contact-minimal source.

### Theorem C63 (Gate C-I closure)

For a contact-minimal triangle-free global diameter minimizer,

\[
\boxed{C=C_*.}
\tag{C63.35}
\]

Equivalently, every unit contact carries positive multiplier in some normalized KKT stress, and a relative-interior normalized KKT stress can be chosen with

\[
\boxed{\alpha_e>0\quad\text{for every unit contact }e.}
\tag{C63.36}
\]

Target C Gate C-I is closed.

## 9. Why the formal argument is legitimate

Three points are important.

### 9.1 Formal power series are enough

The recursive series need not converge. It is an actual element of the ordered field `R((t))`. Polynomial distance inequalities can be evaluated there exactly.

### 9.2 Transfer is finite

The final real-closed-field statement is a finite existential formula involving only the `2n` real coordinates, finitely many pairwise inequalities, and one proximity inequality. The infinite construction appears only in the witness inside the extension field.

### 9.3 Global optimality recovers exact diameter

Transfer gives diameter at most `D`, not an explicitly preserved diameter pair. That is sufficient: a smaller real diameter would contradict the definition of `D(n)`. Hence the transferred configuration automatically has exact diameter `D`.

## 10. Relation to C57-C62

The body-hinge stack remains valid and describes the equality geometry of selected zero-energy stresses, but it is not needed for the logical closure of Gate C-I once universal PSD is available.

C62 is the first nontrivial Taylor step of the present induction. C63 shows that the same Farkas/PSD mechanism continues through every formal order because the exact weighted gap sum is a PSD quadratic form.

Thus there is no residual higher-order locking hidden beyond C62.

## 11. Target C state after C63

Gate C-I is no longer open. Work should now move entirely to Gate C-II.

For the contact-minimal source:

- every unit contact is strong;
- there exists a normalized maximal-support KKT stress with positive coefficient on every unit contact and every strong diameter edge;
- its positive contact graph is the entire contact graph, connected and full-diameter;
- triangle-free source geometry still gives unit-contact degree at most five;
- all C-II bridge, path-packing, endpoint-count, additive-response, and near-star regressions remain binding.

The problem itself remains unresolved because the fully force-visible C-II branch has not yet been eliminated.

## 12. Compact handoff

**LEVEL I STATUS:** still open.

**Gate C-I:** CLOSED.

**C63 mechanism:** every nonnegative dependence among unresolved formal active rows is a normalized KKT stress. Universal PSD makes the exact weighted signed-gap polynomial a sum of squares. Therefore its next unresolved Taylor coefficient cannot be negative, so Farkas can never obstruct the next formal coefficient. Recursion gives a feasible infinitesimal formal configuration with every weak contact strict.

**Transfer:** the real closure of `R((t))` supplies an infinitesimal feasible witness. Quantifier elimination for real closed fields transfers existence to arbitrarily close real configurations. Global optimality restores diameter exactly `D`, while the contact graph is a strict subgraph of the source if any weak contact existed.

**Conclusion:** `C=C_*` in a contact-minimal triangle-free minimizer.

**Next:** Gate C-II only.
