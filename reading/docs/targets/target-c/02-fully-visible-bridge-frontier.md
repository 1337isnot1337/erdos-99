> Generated reading edition · [exact source](../../../../docs/targets/target-c/02-fully-visible-bridge-frontier.md) · source SHA-256 `fedd7ed7bc2c06977db8c17acaea1b33c8aa6a243eb2a3718a447602919d64bf`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — fully force-visible bridge frontier through C39

This module refines the C-II articulation branch under `C=C_*`.

**LEVEL I STATUS: STILL OPEN.**

C20-C29 remain canonical. Current main also supplies C30-C32; C34 and C39 below sharpen the bridge-block phase further.

## 1. No neutral contact transport

Choose a relative-interior normalized KKT stress, so every unit contact has positive stress.

C26 proves that any contact vertex outside `B_+` is a strict positive contact barycenter, hence not any source diameter endpoint. Contact minimality forces its full contact degree to be `3`, `4`, or `5`.

Therefore:

- no unloaded degree-one/two contact vertex exists;
- C21 neutral chains have no internal vertices;
- C22 reaction-free two-terminal regions are impossible;
- the bridge-block tree has no reaction-free degree-two node;
- the common positive-diameter route from C24 is either one block or one universal contact bridge.

## 2. Universal-bridge diameter normal form

If the C24 common route is one universal contact bridge, all positive diameter edges cross that bridge. C25 makes every connected component of `H_+` a common-cut caterpillar forest.

Canonical C32 strengthens this from the positive KKT diameter graph to the **entire nonisolated-core diameter graph**: after deleting at most one same-side diameter edge, the full core diameter graph is bipartite across the universal bridge cut. Consequently it has at most one diameter cycle, and any cycle must use that unique same-side cap.

Thus the universal-bridge phase is now a common-cut diameter pseudoforest, not merely a positive-diameter caterpillar statement.

## 3. Bridge-dominant stress has one macroscopic cut

Let

`S_br=sum_{e bridge} alpha_e`.

C27 gives: if `S_br>=eta D^2`, some individual bridge satisfies

`alpha_e >= eta D^2/(2*pi*D-3) = Omega_eta(D)`.

C20 identifies this with the length of the associated reciprocal-polygon diagonal. Rooting at the C23 hub, the same cut has exact crossing positive-diameter weight `w_e` and

`alpha_e<=D w_e`,

so `w_e=Omega_eta(1)`.

C29 additionally gives

`S_br<=2D(R-1)`,

where `R` is the number of loaded bridge blocks. Thus bridge-dominant stress forces

`R>=eta D/2+1`.

## 4. Loaded-block terminal structure

Canonical C31 gives, for any bridge block `X`,

`delta_X <= 2q_X+k_X-2`,

where `q_X=|B_+ cap X|`, `k_X` is bridge-tree degree, and `delta_X` is internal contact-graph diameter.

C34 adds a distinct-terminal inequality. Eppstein supplies four internal degree-two vertices in every nontrivial bridge block; C26 forces each to be loaded or to carry a distinct outgoing bridge. Hence

`q_X+k_X>=4`.

Therefore a nontrivial leaf, degree-two, and degree-three bridge block contains at least `3`, `2`, and `1` loaded vertices respectively.

## 5. Positive self-stress sharpens the block budget

C39 uses the strictly positive KKT contact stress under the C31 pinning.

Let

- `U_X=V(X)\B_+`;
- `c_X` be the number of connected components of `C[U_X]`;
- `p_X` be the contact rows incident to `X` that become pinned-pinned: internal loaded-loaded contacts plus bridges whose endpoint in `X` is loaded.

Each unpinned component carries an independent positive left-kernel relation, so

`e_X+k_X-p_X >= 2(m_X-q_X)+c_X`.

Hence

`delta_X <= k_X+2q_X-p_X-c_X-2`.

Summing over all bridge blocks, with singleton `delta_X=0`,

`sum_X delta_X <= 2|B_+|-2-sum_X(p_X+c_X)`.

For a nontrivial reaction-free block, `q_X=p_X=0,c_X=1`, hence

`delta_X<=k_X-3`.

Triangle-free cyclicity gives `delta_X>=2`, so every genuinely two-dimensional reaction-free block has

`k_X>=5`.

This excludes the reaction-free square with only four bridge attachments, which survived the earlier C28/C34 counts.

## 6. Current bridge split

```text
bridge-light:
    S_br=o(D^2)
    -> asymptotically all contact stress in nonbridge / two-edge-connected blocks

bridge-dominant:
    S_br>=eta D^2
    -> one alpha_e=Omega_eta(D) reciprocal diagonal
    -> same cut has w_e=Omega_eta(1) positive-diameter weight
    -> Omega_eta(D) distinct loaded bridge blocks
    -> no neutral series transport
    -> all block diameters share a self-stress-sharpened O(D) budget
    -> nontrivial reaction-free block degree >=5
    -> common route is one block or one universal bridge
       * universal bridge: full core diameter graph is a common-cut pseudoforest
       * one block: cycle / two-edge-connected reciprocal-response phase
```

## 7. Shortest bridge target

A sufficient closing theorem remains:

> **Macroscopic bridge-cut exclusion.** For every fixed `c>0`, no sufficiently large fully force-visible global minimizer has a positive contact bridge with both `alpha_e>=cD` and crossing positive-diameter weight `w_e>=c`.

C27 would then force `S_br=o(D^2)`.

The remaining obstacle is geometric, not rank bookkeeping: rule out a macroscopic reciprocal cut through a `Theta(D)` loaded boundary under the C18 diameter-star restrictions and C32 common-cut pseudoforest normal form.

## Binding cautions

- No individual KKT weight has a uniform lower bound.
- A macroscopic bridge resultant does not force a diameter star or narrow cone; crossing matchings remain possible.
- Contact-isolated source points are outside the force-visible core.
- C26-C39 do not apply to C-I weak-contact configurations unless explicitly stated.
