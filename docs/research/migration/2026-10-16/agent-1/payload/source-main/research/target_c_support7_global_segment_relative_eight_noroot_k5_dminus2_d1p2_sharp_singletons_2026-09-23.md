# Target C: sharpen the eight-no-root `k=5,D=-2,d_root=1,p=2` branch

Date: 2026-09-23

Status: rigorous structural reduction of one of the five remaining arithmetic branches in the eight-no-root `k=5` layer. This is a proof-only metric-basis result. It does not close the branch, Target C-II, or Erdos Problem #99, and it does not change canonical theorem-state authority.

The input is the rank-three reduction in

`research/target_c_support7_global_segment_relative_eight_noroot_k6_layer_closure_k5_two_clean_reduction_2026-09-23.md`

and the certified five-row rank-three virtual-canonical theorem recorded and used in

`research/target_c_support7_global_segment_relative_five_noroot_k2_p3_sharp_singletons_2026-09-20.md`.

No new exhaustive computation is used.

## 1. Branch setup

Assume a hypothetical eight-no-root counterexample

`B=R union E`, `|E|=8`,

lies in

```text
k(B)=5,
D(B)=-2,
d_root=1,
p=2.
```

Let

`P <= Q^8`

be its rank-three external coefficient-constraint space.

The established all-depth deletion bounds give

```text
d_1(P)>=3,
d_2(P)>=4,
d_3(P)>=6.
```

For a deletion set `J subset E`, write `q_J` for the rank loss of `P` under puncturing on `J`. Then

```text
D(B\J)=-2+2|J|-3q_J.
```

In particular, a three-coordinate deletion with `q_J=0` gives a five-no-root shadow with

```text
rank(P_J)=3,
k=2,
D=4.
```

The root-row set itself is unchanged by puncturing. We keep root rows in blocks that become untouched, exactly as in the unstripped formulation of the five-row sharp-singleton theorem.

## 2. Every coordinate pair extends to a rank-preserving triple

Call a three-set `J` **good** when puncturing on `J` preserves `rank(P)=3`, equivalently `q_J=0`.

### Lemma 2.1

Every two-set `S subset E` is contained in at least four good three-sets.

Consequently every set of at most two coordinates is contained in a good three-set.

### Proof

Fix a two-set `S`.

For `j in E\S`, the triple `S union {j}` is bad exactly when `P` contains a nonzero word supported in that triple. Since `d_1(P)>=3`, such a word has support exactly `S union {j}`.

Suppose three distinct coordinates `j_1,j_2,j_3` were bad. Choose nonzero

```text
u_r in P,
supp(u_r)=S union {j_r},
r=1,2,3.
```

If `u_1,u_2,u_3` were independent, their span would be a three-dimensional subcode supported on

`S union {j_1,j_2,j_3}`,

which has size five. This contradicts `d_3(P)>=6`.

So the three vectors are dependent. But any two, say `u_1,u_2`, are independent because their supports differ. Write

`u_3=a u_1+b u_2`.

At coordinate `j_1`, both `u_2` and `u_3` vanish while `u_1` is nonzero, so `a=0`. At coordinate `j_2`, both `u_1` and `u_3` vanish while `u_2` is nonzero, so `b=0`. This gives `u_3=0`, contradiction.

Therefore at most two of the six choices `j in E\S` are bad. At least four are good. `square`

This is stronger than the previous two-clean statement on the `D=-2` side: not only does every one- and two-coordinate puncture preserve rank, but every fixed pair has at least four rank-preserving extensions to depth three.

## 3. Every good five-row shadow is a sharp two-singleton state

Fix a good triple `J`. The five-row coefficient space `P_J` has rank three and the unstripped five-row state has total incomplete-root cost `p=2`.

Any realization of `P_J` uses empty-block constraints plus at most two singleton-block constraints: the only selected incomplete-root cost available is two, a pair state contributes zero coefficient constraint, and a singleton contributes at most one line.

The certified five-row rank-three virtual-canonical theorem therefore applies. Let

- `C_J` be the virtual-canonical complete-block set;
- `d_J=|C_J|-rank H(C_J)` its complete-block deficiency;
- `q_J^c` be the number of canonical-complete blocks made incomplete in the actual shadow; and
- `p_{t,J}` be the selected incomplete-root cost in blocks still touched after deleting `J`.

The theorem gives

```text
d_J>=1,
D(B\J)>=5+p+3d_J-3q_J^c,
q_J^c<=p_{t,J}<=p=2.
```

Here `D(B\J)=4` and `p=2`, so

```text
4 >= 7+3d_J-3q_J^c.
```

With `d_J>=1` and `q_J^c<=2`, equality is forced throughout:

```text
d_J=1,
q_J^c=2,
p_{t,J}=2.
```

Each canonical-complete block made incomplete must consume at least one selected root row. Since there are exactly two changed blocks and total cost two, the shadow has exactly two selected singleton blocks, both touched, both canonical-complete, and no selected pair block or selected row in an untouched incomplete block.

The selected root state is inherited from the eight-row parent. Since at least one good triple exists, the parent itself must therefore have exactly two selected singleton blocks and no pair block.

Moreover, the argument holds for every good triple. Hence:

> **Theorem 3.1.** In the `D=-2,k=5,d_root=1,p=2` branch, the two selected incomplete blocks are singletons, and both remain touched and canonical-complete after every rank-preserving three-coordinate puncture.

This removes the pair-state alternative from the branch completely.

## 4. The two singleton blocks are touched at least four times

Fix one of the two singleton blocks `b`. Let

`T_b subset E`

be the set of external cycles touching it.

Theorem 3.1 says no good triple can contain all of `T_b`, because deleting such a triple would make `b` untouched.

Lemma 2.1 immediately gives

`|T_b|>=3`:

if `|T_b|<=2`, enlarge `T_b` to a two-set `S`, choose a good triple containing `S`, and obtain a contradiction.

The case `|T_b|=3` can also be excluded.

### Lemma 4.1: quotient-coset distance

For each selected singleton block `b`, its empty-state local coefficient space `E_b` satisfies

```text
E_b not subset P,
dim((E_b+P)/P)=1,
```

and the nonzero quotient coset has Hamming distance at least four from `P`.

### Proof

Every good puncture keeps `b` canonical-complete, so for every good triple `J`,

`pi_J(E_b) not subset pi_J(P)`.

Equivalently,

`E_b not subset P+K_J`,

where `K_J` is the coordinate subspace supported on `J`. In particular `E_b not subset P`.

Let `L_b` be the singleton local coefficient-constraint space. Compatibility gives `L_b subset P` and `L_b subset E_b`.

The local empty space has rank at most two. If `rank E_b=1`, then `L_b` must be zero, since otherwise `L_b=E_b subset P`; hence the quotient has dimension one. If `rank E_b=2`, the singleton determinant row is a nonzero line in `E_b`, so `dim(E_b intersect P)>=1`; because `E_b` is not contained in `P`, the quotient again has dimension one.

Choose `w_b in E_b\P`; its class generates the quotient line.

Suppose the coset `w_b+P` had a representative `v` supported on at most two coordinates. Put its support inside a two-set `S`. By Lemma 2.1 there is a good triple `J` containing `S`. Then

`v in K_J`,

so `w_b in P+K_J`, contradicting the good-puncture canonical-completeness condition.

Thus the coset distance is at least three.

Suppose instead that a minimum representative `v` had support exactly a triple `J`. If `J` were good, the same contradiction would apply. Hence `J` is bad. Since `d_1(P)>=3`, rank loss on the three-set produces a nonzero `u in P` with

`supp(u)=J`.

If `v` were proportional to `u`, then `v in P`, impossible. Otherwise choose a scalar `lambda` cancelling one nonzero coordinate of `v` against `u`. Then

`v-lambda u`

represents the same nonzero coset and has support at most two, contradicting the preceding paragraph.

Therefore the coset distance is at least four. `square`

Because `E_b` is supported only on the external cycles touching `b`, the vector `w_b` is supported inside `T_b`. A coset with minimum weight at least four cannot have a representative supported on fewer than four coordinates. Hence

`|T_b|>=4`.

Thus:

> **Theorem 4.2.** Each of the two forced singleton blocks in the `D=-2,k=5,d_root=1,p=2` branch is touched by at least four of the eight external cycles. Each also supplies a distinguished nonzero quotient line in `Q^8/P` whose coset distance from `P` is at least four.

## 5. Resulting branch profile

The branch is now reduced from an arbitrary `p=2` root state to the following exact necessary profile:

```text
D=-2,
k=5,
rank(P)=3,
(d1,d2,d3)(P)>=(3,4,6),
d_root=1,
p=2,

exactly two selected singleton blocks b_1,b_2,
|T_{b_1}|>=4,
|T_{b_2}|>=4,

for each r=1,2:
    E_{b_r} not subset P,
    dim((E_{b_r}+P)/P)=1,
    dist(E_{b_r}+P, P)>=4,

and after every good three-coordinate puncture:
    both singletons remain touched,
    both remain canonical-complete,
    virtual-canonical deficiency is exactly one,
    exactly two canonical-complete blocks are changed.
```

The eight no-root cycles contribute only 32 block-touch incidences in total, so the two forced singleton blocks consume at least eight of them. More importantly, the quotient-coset distance condition is an exact rank-three coefficient-space filter that can be imposed before any `T`-space reranking.

## 6. Remaining bottleneck

This note does not close the branch. The next finite target is to combine the two distance-at-least-four singleton quotient cosets with

- the generalized-weight constraints `(3,4,6)` on `P`;
- the fact that both singleton touch sets have size at least four;
- the single root complete-block dependence `d_root=1`; and
- the requirement that every good depth-three puncture has the same deficiency-one/two-singleton virtual profile.

A direct verifier can now reject the pair-state half of the `p=2` branch before coefficient-space generation and can reject any singleton block with touch multiplicity at most three or quotient-coset distance at most three.

The other four `k=5` arithmetic branches remain untouched by this note.