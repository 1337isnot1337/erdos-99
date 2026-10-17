> Generated reading edition · [exact source](../../research/target_c_three_cut_parallel_integration_classification_2026-09-15.md) · source SHA-256 `49d1d94d93fe93e1364bd746d921c209441489c48797de1acbae94396cd3ba96`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "7dd56a5591e5a2e0217cc04d9cf8dedb1837b069", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_three_cut_parallel_integration_classification_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b813b25c146d1e3c2fc51af676dbb78a720276d610dafc09c15477a34b6d26d8"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — exact classification of the rank-one three-cut integration regression

**Date:** 2026-09-15  
**Status:** proof-only exact structural strengthening  
**Scope:** the projectively-parallel case left open in `target_c_three_cut_kernel_cusp_2026-09-15.md`  
**Dependencies:** exact finite laminar multishear; three-cut kernel notation  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The three-cut kernel theorem proves exact finite localization when the three shore-oriented train vectors span the plane, by integrating

$$
G(\theta_1,\theta_2,\theta_3)
:=\sum_{j=1}^3(R_{\theta_j}u_j-u_j)=0
$$

with the implicit-function theorem.  It leaves the rank-one case as a separate regression.

That regression is completely classifiable.

Assume the three shore-oriented unit vectors are projectively parallel.  Then for one unit vector `u` and signs

$$
s_j\in\{-1,+1\}
$$

we may write

$$
u_j=s_ju.
\tag{PI.1}
$$

The exact full-support displacement is

$$
\boxed{
G(\theta)
=\sum_{j=1}^3s_j(R_{\theta_j}u-u).
}
\tag{PI.2}
$$

There are exactly two cases.

---

## 1. Mixed shore orientations integrate exactly

Suppose the signs are not all equal.  Choose indices `p,q` with

$$
s_p=-s_q.
$$

Set

$$
\theta_p(t)=t,
\qquad
\theta_q(t)=t,
\qquad
\theta_r(t)=0
$$

for the remaining index `r`.  Then identically for every real `t`,

$$
\begin{aligned}
G(\theta(t))
&=s_p(R_tu-u)+s_q(R_tu-u)\\
&=(s_p+s_q)(R_tu-u)\\
&=0.
\end{aligned}
\tag{PI.3}
$$

Thus the rank-one mixed-sign case has an explicit nonconstant exact kernel curve.  No implicit-function theorem is needed.

Applied to the exact finite multishear:

- every diameter row meeting none of the chosen cuts is unchanged exactly;
- every diameter row meeting all three is unchanged exactly by (PI.3);
- every old unit contact is preserved exactly;
- only rows whose cut support changes inside the selected triple can move.

Hence the finite-cusp localization from the nonparallel case extends verbatim to every projectively-parallel triple with mixed shore orientations.

---

## 2. Same shore orientation has no nontrivial exact kernel

Now suppose

$$
s_1=s_2=s_3=\sigma,
\qquad
\sigma\in\{-1,+1\}.
\tag{PI.4}
$$

Take scalar components of (PI.2) along `u` and `Ju`.  Since

$$
u\cdot R_\theta u=\cos\theta,
\qquad
Ju\cdot R_\theta u=\sin\theta,
$$

we have

$$
\boxed{
\sigma\,u\cdot G(\theta)
=\sum_{j=1}^3(\cos\theta_j-1)
\le0.
}
\tag{PI.5}
$$

Equality holds if and only if every `theta_j` is an integer multiple of `2pi`.  Therefore in a neighborhood of the origin,

$$
\boxed{
G(\theta)=0
\quad\Longrightarrow\quad
\theta=0.
}
\tag{PI.6}
$$

So the same-orientation rank-one case does **not** possess a nonconstant exact full-support cancellation curve.  This is a genuine second-order obstruction, not merely a failure of the rank hypothesis used by the implicit-function theorem.

---

## 3. The first-order kernel has a forced one-sided quadratic drift

In the same-orientation case, the derivative at the origin is

$$
DG(0)[c]
=\sigma Ju\,(c_1+c_2+c_3).
$$

Thus the first-order kernel is the two-plane

$$
\boxed{c_1+c_2+c_3=0.}
\tag{PI.7}
$$

Take any nonzero `c` satisfying (PI.7) and any differentiable path

$$
\theta_j(t)=t c_j+o(t).
$$

The radial component of the exact displacement obeys

$$
\begin{aligned}
\sigma\,u\cdot G(\theta(t))
&=\sum_j(\cos\theta_j(t)-1)\\
&=-{t^2\over2}\sum_jc_j^2+o(t^2).
\end{aligned}
\tag{PI.8}
$$

Since `c!=0`,

$$
\boxed{
\sigma\,u\cdot G(\theta(t))
=-{1\over2}\|c\|_2^2t^2+o(t^2)<0
}
\tag{PI.9}
$$

for all sufficiently small nonzero `t`.

No choice of second-order corrections to the three angles can remove this radial term: equation (PI.5) is exact and strictly negative away from the discrete trivial points.

Thus every nonzero first-order kernel direction in the same-orientation rank-one case produces a forced common second-order translation of every diameter row whose interval contains all three cuts.

---

## 4. Complete integration classification

Combining the parent three-cut theorem with the present calculation gives the exact local trichotomy for three selected cuts:

1. **rank two:** `span{u_1,u_2,u_3}=R^2`; the implicit-function theorem gives a one-dimensional exact `G=0` curve;
2. **rank one, mixed signs:** an explicit pair-cancellation curve gives `G=0` identically;
3. **rank one, same sign:** the origin is an isolated zero of `G`, and every nonzero first-order kernel direction has the one-sided quadratic drift (PI.9).

Therefore the only remaining failure of exact full-support cancellation is the very specific configuration

$$
\boxed{
u_1=u_2=u_3\quad\text{or}\quad u_1=u_2=u_3=-u
}
$$

under the coherent shore orientation.

The next useful theorem in that branch is no longer an integration question.  It is a second-order diameter-sign theorem for the common drift in (PI.9), coupled to the ordered switching interfaces at the two internal boundaries.

No diameter descent or C-II closure is claimed here.

**Disposition:** the rank-one three-cut integration regression is fully classified; exact finite localization fails only in the same-oriented parallel case, where the failure has a fixed one-sided quadratic form. C-II and Level I remain open.
