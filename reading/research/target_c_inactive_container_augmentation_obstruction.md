> Generated reading edition · [exact source](../../research/target_c_inactive_container_augmentation_obstruction.md) · source SHA-256 `2f32a79503ce3f1e53e4e68552ab0bdf6bf9bcc789571ea2211b50aa4bacd7f1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "af164407a949634beba2adcc0ac676a5f7e077eb", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_inactive_container_augmentation_obstruction.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e118e8a36cf8b0ab6c602ef8bfc574cd8b40d5e0f06cb5ffce7acdc1a781ac43"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — inactive-container augmentation obstruction

**Date:** 2026-09-12  
**Status:** proof-only negative theorem; theorem state unchanged  
**Level I / C-II:** open

The macroscopic-container branch supplies an actual convex container with quadratic
area, quadratic contact-isolated source population, perimeter `O(D)`, and Oler slack
`O(D)`. A tempting closure is to remove one or more diameter-carrying core points and
reinsert the same number of points into the inactive container.

The theorem below shows that the four container statistics alone cannot justify even
**one** additional point. There are arbitrarily large convex containers with exactly
those statistics whose isolated population already has maximum possible unit-separated
cardinality, despite having no unit contacts at all.

Thus a successful Type-I replacement theorem must use source-specific coupling to the
container boundary/core, not only area, perimeter, Oler slack, and contact isolation.

---

## 1. Packing number

For a compact convex body `C subset R^2`, let

$$
N(C):=\max\{|X|:X\subset C,\ |x-y|\ge1\text{ for }x\ne y\}.
\tag{IA.1}
$$

The maximum exists by compactness.

Let

$$
a_0={\sqrt3\over2}.
$$

Oler gives

$$
N(C)\le {area(C)\over a_0}+{per(C)\over2}+1.
\tag{IA.2}

Conversely, translated triangular-lattice averaging gives

\[
\boxed{N(C)\ge {area(C)\over a_0}.}
\tag{IA.3}

Indeed take the unit triangular lattice of covolume `a_0`. Averaging
`#((Lambda+t) cap C)` over one lattice fundamental domain gives exactly
`area(C)/a_0`, so some translate has at least that many points. Lattice points are
unit-separated.

---

## 2. Packing number is stable under a sufficiently small dilation

Assume `C` has nonempty interior and contains the origin in its interior. Put
`N=N(C)` and define

\[
\lambda_*:=\inf\{\lambda\ge1:N(\lambda C)\ge N+1\}.
\tag{IA.4}

### Lemma IA.1

\[
\boxed{\lambda_*>1.}
\tag{IA.5}

### Proof

If `lambda_*=1`, choose `lambda_j downarrow1` and `N+1` unit-separated points

\[
x_{j,1},...,x_{j,N+1}\in\lambda_jC.
$$

Put `y_{j,k}=x_{j,k}/lambda_j in C`. Then

$$
|y_{j,k}-y_{j,l}|\ge {1\over\lambda_j}.
$$

By compactness of `C^{N+1}`, pass to a subsequence on which every coordinate converges:
`y_{j,k}->y_k in C`. Taking limits gives

$$
|y_k-y_l|\ge1
$$

for all `k!=l`. Thus `C` contains `N+1` unit-separated points, contradicting the
definition of `N`. `square`

So for every

$$
1<\lambda<\lambda_*
$$

the enlarged body `lambda C` still has packing number exactly `N`.

---

## 3. Maximum cardinality with every pair strictly farther than one

Take the disk

$$
C_R:=B(0,R),\qquad R\to\infty,
$$

and let `N_R=N(C_R)`. Let `lambda_{*,R}>1` be the threshold from Lemma IA.1.
Choose

$$
0<\epsilon_R<\min\left\{ {\lambda_{*,R}-1\over2},\ {1\over R^2}\right\}
\tag{IA.6}

and put

\[
\lambda_R:=1+\epsilon_R.
$$

Choose a maximum unit-separated packing

$$
Y_R\subset C_R,
\qquad |Y_R|=N_R.
$$

Set

$$
\eta_R:={\epsilon_R\over2},
\qquad
X_R:=(1+\eta_R)Y_R,
\qquad
C'_R:=(1+\epsilon_R)C_R.
\tag{IA.7}

Then `X_R subset int(C'_R)`, and for distinct points

\[
|x-y|\ge1+\eta_R>1.
\tag{IA.8}

So every point of `X_R` is contact-isolated relative to the entire population
`X_R`.

But `lambda_R<lambda_{*,R}`, hence

\[
N(C'_R)=N_R=|X_R|.
\tag{IA.9}

Therefore there does not exist **any** unit-separated set of `|X_R|+1` points in
`C'_R`. This is stronger than saying that no extra point can be inserted while
holding `X_R` fixed: arbitrary global rearrangement of the whole population cannot
make room for one more point.

---

## 4. The examples have exactly the Type-I scale statistics

The disk has

\[
area(C'_R)=\pi(1+\epsilon_R)^2R^2=\Theta(R^2),
\qquad
per(C'_R)=2\pi(1+\epsilon_R)R=O(R).
\tag{IA.10}

Triangular-lattice averaging (IA.3) gives

\[
N_R\ge {\pi R^2\over a_0}=\Omega(R^2).
\tag{IA.11}

Define the Oler slack of the isolated population in the enlarged container by

\[
\sigma_R
:={area(C'_R)\over a_0}+{per(C'_R)\over2}+1-|X_R|.
\tag{IA.12}

It is nonnegative by Oler. On the other hand, using `|X_R|=N_R` and (IA.3),

\[
\begin{aligned}
\sigma_R
&\le {area(C'_R)-area(C_R)\over a_0}
   +{per(C'_R)\over2}+1.
\end{aligned}
$$

Since `epsilon_R<=R^{-2}`,

$$
area(C'_R)-area(C_R)=O(1),
$$

so

\[
\boxed{\sigma_R=O(R).}
\tag{IA.13}

Thus the sequence has simultaneously

\[
\boxed{
area(C'_R)=\Omega(R^2),\quad
|X_R|=\Omega(R^2),\quad
per(C'_R)=O(R),\quad
\sigma_R=O(R),
}
\tag{IA.14}

all points are contact-isolated, yet

\[
\boxed{N(C'_R)=|X_R|.}
\tag{IA.15}

There is zero augmentation capacity.

---

## 5. Consequence for the C-II macroscopic-container branch

The theorem rejects any implication of the form

```text
convex container
+ area = Omega(D^2)
+ isolated population = Omega(D^2)
+ perimeter = O(D)
+ Oler slack = O(D)
    => room for one (or cD) additional source point(s).
```

Even the one-point conclusion is false.

This does **not** refute a source-specific replacement theorem. The actual Type-I
container has extra structure absent from the examples above: its boundary belongs to
the old positive-contact/diameter-carrying source, internal chambers have the protected
isolate-hull/blocker structure, and exterior caps are coupled to the source hull.
Those data must do real work.

In particular, the result strengthens the warning from proof-only Section 95:

- Section 95 shows that moving protected isolates to first contact need not change the
  old KKT polytope.
- The present theorem shows that even arbitrary **repacking** based only on the four
  coarse container statistics need not free a single slot for a removed core point.

A viable Type-I closure therefore has to change the active diameter/contact structure,
force an exact triangle through the blocker graph, or prove an augmentation theorem
whose hypothesis explicitly uses the core/container coupling.

---

## 6. Scope audit

- The examples are abstract convex containers, not claimed global diameter minimizers.
  Their purpose is to disprove a proposed intermediate implication from the canonical
  Type-I container statistics alone.
- No statement is made about protected fixed-depth subpopulations. A theorem using a
  quantitatively protected collar plus the actual core boundary is not excluded.
- No source point is deleted in any claimed Target C theorem; this file proves only a
  negative model theorem.
- The theorem-state manifest is unchanged.

