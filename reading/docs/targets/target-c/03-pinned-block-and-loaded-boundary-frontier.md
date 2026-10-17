> Generated reading edition · [exact source](../../../../docs/targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md) · source SHA-256 `1ce0a1fc17469e247e830e3289ce14b44289f81d7dbb55ae3594dddd93e485ba`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — pinned-block and loaded-boundary frontier

**LEVEL I STATUS: STILL OPEN.**

This module records the fully force-visible boundary/rank normal form after canonical C30-C32 and C33/C34/C39.

## Global boundary count

Let `q=|B_+|`, `m` be the number of nonisolated contact vertices, `e` the number of unit contacts, and `delta` the contact-graph diameter. Canonical C30 gives

`e >= 2(m-q)`

and Eppstein gives

`e <= 2m-delta-2`.

Hence

`2q >= delta+2 >= ceil(D)+2`,

so every fully force-visible survivor has `Theta(D)` positively diameter-loaded force-hull vertices.

## Positive self-stress boundary surplus

Pin `B_+` and let `c_I` be the number of connected components of the remaining contact graph and `e_BB` the number of loaded-loaded unit contacts. C33 proves

`e-e_BB >= 2(m-q)+c_I`,

hence

`2q >= delta+c_I+e_BB+2`.

With `sigma_B=2q-delta-2`,

`c_I+e_BB <= sigma_B`.

Thus a boundary close to the C30 minimum has few unpinned components and few direct loaded-loaded contacts.

## Block budgets

Canonical C31 gives for every bridge block `X`

`delta_X <= 2q_X+k_X-2`.

C34 gives the distinct-terminal refinement

`q_X+k_X >= 4`

for every nontrivial block.

C39 uses the strictly positive KKT self-stress. If `c_X` is the number of connected unpinned subcomponents of `X` and `p_X` the contact rows that become pinned-pinned under the C31 pinning, then

`delta_X <= k_X+2q_X-p_X-c_X-2`.

Summing over all bridge blocks,

`sum_X delta_X <= 2q-2-sum_X(p_X+c_X)`.

A nontrivial reaction-free block has `delta_X<=k_X-3`, hence bridge degree at least `5`.

## Boundary contact degree

C35 proves every loaded vertex has

`1 <= deg_C(b) <= 3`.

The proof uses extremality of loaded vertices and the fact that triangle-free unit-contact directions are separated by more than `60` degrees inside an angle smaller than `180` degrees.

## Boundary phase split

If `sigma_B` is a positive fraction of `D`, then the loaded boundary has a corresponding linear surplus above the pinned-rank minimum. This is the boundary-surplus phase.

If `sigma_B=o(D)`, then `c_I=o(D)` and `e_BB=o(D)`. C35-C40 refine this into the noncrossing harmonic response normal form in `04-near-minimal-response-frontier.md`.

The remaining task is geometric: rule out a sufficiently large global minimizer with `Theta(D)` positively loaded force-hull vertices, a connected triangle-free force-visible contact core spanning `D`, and the C10/C11 reciprocal-response identities.
