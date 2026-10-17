> Generated reading edition · [exact source](../../research/target_b_section120_nonpositive_capacity.md) · source SHA-256 `7707437133ad1d75ba317b1393fdec5e455e0052935c5881aa6c24e2dc36e6c8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "188efaacc5ad545bf147d434aebbada6bfe9cd27", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_b_section120_nonpositive_capacity.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "eee520a132eda5b7e93b3e41ff2d7b31451beb9fda0bfa01d41824f1f6064773"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target B Section 120 companion — nonpositive train capacity on a diameter arc

The exact boundary charge from Section 120 controls not only strict-backward trains but
also tangent separating trains.  This is important because the corrected higher-order
analysis allows `lambda=0` trains to block at quartic order.

Keep the Section-120 setup.  Let

$$
P_-:=\{\tau:\lambda_\tau<0\},
\qquad
P_0:=\{\tau:d_\tau\ne0,\ \lambda_\tau=0\},
$$

and

$$
S_-:=\sum_{\tau\in P_-}(-\lambda_\tau).
$$

Let `Gamma` be either boundary arc from the active diameter endpoint `z` to `a`,
directed from `z` to `a`, with unit-edge length `L`.

Every separating train has one unique terminal edge occurrence on `Gamma`, directed by
its train-coordinate vector `a_tau` from the `z`-side to the `a`-side.  The exact
projection loss of that occurrence is

$$
1-q\cdot a_\tau=1-\lambda_\tau/D.
$$

Thus:

- a tangent train in `P_0` contributes exactly `1`;
- a backward train with `x_tau=-lambda_tau/D in (0,1]` contributes exactly
  `1+x_tau`.

Injectivity of the terminal-edge charge therefore gives the stronger finite theorem

$$
\boxed{
L-D
\ge
|P_0|+|P_-|+{S_-\over D}.
}
\tag{120.N1}
$$

Equivalently,

$$
\boxed{
|P_0|+|P_-|
\le L-D,
}
\tag{120.N2}
$$

and

$$
\boxed{
S_-
\le D\bigl(L-D-|P_0|-|P_-|\bigr).
}
\tag{120.N3}
$$

Using `1+x>=2x` only on the backward terms while retaining the tangent cost gives
another useful form:

$$
\boxed{
S_-
\le {D\over2}\bigl(L-D-|P_0|\bigr).
}
\tag{120.N4}
$$

The original Section-120 backtracking theorem follows by discarding `|P_0|` and the
backward count.

## Tangent coordinate support and the quartic regression model

Canonical sign coherence says that, for one active diameter bar, all tangent separating
trains have the same oriented contribution.  The corrected tangent-class analysis
shows that these coordinates can create genuine higher-order obstruction; in
particular, Section 43.1 exhibits a same-oriented class of `2s` tangent trains that
quartically blocks an `s`-dimensional paired-angle subspace.

Equation (120.N2) gives a universal geometric bound on the **number of tangent
coordinates available to that bar**:

$$
\boxed{
|P_0|\le L-D.
}
\tag{120.N5}
$$

For the specific paired construction of Section 43.1, which uses two distinct tangent
trains per paired variable, this implies

$$
\boxed{
s\le\left\lfloor{|P_0|\over2}\right\rfloor
\le\left\lfloor{L-D\over2}\right\rfloor.}
\tag{120.N6}
$$

Equation (120.N6) is **not** asserted as a universal upper bound on the dimension of
all possible quartic blocker sets supported on `P_0`.  The higher-order equations
`S_1=S_3=0`, `S_2\ne0` are nonlinear, and the repo does not contain a theorem
classifying the maximum linear dimension of their solution set.  The universal result
proved here is the coordinate-support bound (120.N5), not a factor-two rank theorem.

For the shorter of the two boundary arcs, `L_*<=T` because the total pure-disk boundary
length is `2T`.  Hence

$$
\boxed{
|P_0|+|P_-|\le T-D.
}
\tag{120.N7}
$$

The explicit Section-43.1 paired regression then has

$$
\boxed{
s\le\left\lfloor{T-D\over2}\right\rfloor.}
\tag{120.N8}
$$

These are per-active-bar capacities.  They do **not** by themselves prove the global
component-quotiented rank bound, because different active diameter bars can use
different nonpositive train sets and blocker rows from one train can occur for several
bars.

The correct remaining Target-B task is therefore narrower than before Section 120:
prove that the internal component blocker/coforest rank cannot simultaneously realize
its required macroscopic lower bound while every active bar obeys the common-detour
capacity (120.N1).  Tangent coordinates are no longer uncharged; their available
support is charged to boundary detour, but the global sharing/overlap theorem across
active bars remains open.

**Theorem state:** unchanged.
