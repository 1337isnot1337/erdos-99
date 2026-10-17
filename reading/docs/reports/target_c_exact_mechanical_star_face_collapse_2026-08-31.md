> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_mechanical_star_face_collapse_2026-08-31.md) · source SHA-256 `62eb4e38766320d11978d33fafe70e0ab453484ce92e49e5208ec0262d947b95`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-772894FDBB39","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C76: exact mechanical star faces are straight-chain stresses

**Date:** 2026-08-31  
**Repository base:** `45f9d11f` (main after C75 / PR #79)  
**Run type:** exact KKT-polytope face classification  
**Target:** Target C Gate C-II, limiting face of the C66 near-star phase  
**Depends on:** C12 positive-support connectivity, C18 strict large-D diameter-star angle gap, C54 universal PSD, C68 radial-defect domination  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C66-C74 show that a hypothetical sequence with `D epsilon -> 0` becomes mechanically and electrically star-like around one diameter vertex, with an almost radial high-stress carrier. C76 identifies the exact KKT-polytope face approached by that degeneration.

Let `s=(alpha,beta)` be **any** normalized KKT stress for the C-II source, including a stress on a proper face of the normalized KKT polytope. For a diameter vertex `z`, define

$$
S_z(s):=\sum_{zk\in H}\beta_{zk}.
$$

For `D>=20`:

### Theorem C76 — exact mechanical star-face collapse

If

$$
\boxed{S_z(s)=1,}
$$

then the positive diameter support is one edge `za` of weight one, `D` is an integer, and the positive contact support is exactly the straight unit chain

$$
z=x_0,x_1,\ldots,x_D=a,
\qquad |x_{j+1}-x_j|=1,
$$

with every positive contact stress equal to `D`.

Equivalently, the normalized KKT-polytope face

$$
\mathcal S_z:=\{s:S_z(s)=1\}
$$

is either empty or a singleton straight-chain stress.

Thus an exact multi-leaf mechanical star is impossible in the large-`D` C-II geometry. The C66-C74 near-zero phase approaches only the C54.1 straight-chain stress face, not a generic star network.

---

## 1. Radial defect vanishes on an exact star face

C54 proves

$$
\Omega_s=L_C(\alpha)-L_H(\beta)\succeq0
$$

for every normalized KKT stress. Therefore the C68 radial test applies to arbitrary `s`.

Put

$$
r_i:=|p_i-z|,
\qquad
Q_z(s):=\sum_{ij}\alpha_{ij}[1-(r_i-r_j)^2].
$$

C68 gives

$$
\boxed{
Q_z(s)+
\sum_{\substack{ij\in H\\z\notin\{i,j\}}}
\beta_{ij}(r_i-r_j)^2
\le D^2[1-S_z(s)].
}
\tag{C76.1}
$$

If `S_z(s)=1`, normalization already makes every positive diameter edge incident to `z`, and C76.1 yields

$$
\boxed{Q_z(s)=0.}
\tag{C76.2}
$$

Every summand in `Q_z` is nonnegative because a unit contact satisfies `|r_i-r_j|<=1`. Hence every positive contact satisfies

$$
\boxed{|r_i-r_j|=1.}
\tag{C76.3}
$$

For a positive contact not incident to `z`, equality in the reverse triangle inequality forces `z,p_i,p_j` to be collinear with `p_i,p_j` on the same ray from `z`.

Therefore every component of the positive contact graph `C_s-z` is contained in one ray from `z`. Such a component attaches to `z` through at most one positive contact, since a ray contains only one source point at distance one from `z`.

---

## 2. Every positive radial branch carries star load

C12 states that for **every** normalized KKT stress, its positive unit-contact support has exactly one nontrivial connected component.

Let `R` be a component of `C_s-z`, attached through its unique positive port `zx_R`. Sum KKT equilibrium over all vertices of `R`. Internal positive contact forces cancel. Since every positive diameter edge is incident to `z`, the only possible diameter reactions on `R` come from `z`-star diameter edges with opposite endpoint in `R`.

If `R` contained no positive diameter partner of `z`, its summed reaction would be zero, while the unique surviving port force

$$
\alpha_{zx_R}(p_{x_R}-p_z)
$$

would be nonzero. Contradiction.

### Lemma C76.1

Every positive radial branch at `z` contains at least one positive diameter partner of `z`.

---

## 3. The C18 angle gap permits only one branch

Suppose two distinct radial branches `R,S` exist, and choose positive diameter partners `a in R`, `b in S`. Let their port neighbors be `x_R,x_S`.

Both port neighbors are source points at unit distance from `z`. Unit separation gives

$$
|x_R-x_S|=2\sin\frac{\angle x_Rzx_S}{2}\ge1,
$$

so

$$
\boxed{\angle x_Rzx_S\ge\frac\pi3.}
\tag{C76.4}
$$

Because each branch lies on one ray,

$$
\angle x_Rzx_S=\angle azb.
$$

For `D>=20`, C18 gives the strict global diameter-star bound

$$
\boxed{\angle azb<\Theta_D<\frac\pi3.}
\tag{C76.5}
$$

Equations C76.4-C76.5 contradict each other. Hence exactly one positive radial branch leaves `z`.

---

## 4. The unique branch is the straight diameter chain

All positive-contact vertices lie on one ray from `z`. A positive diameter partner must lie on that ray at radius exactly `D`, so there is only one such source point `a`. Therefore

$$
\boxed{H_s=\{za\},\qquad\beta_{za}=1.}
\tag{C76.6}
$$

The positive contact graph is connected, collinear, and joins radii `0` and `D`. Every positive contact changes the radial coordinate by exactly one. Starting at `z`, all positive-contact radii are integers. Thus

$$
\boxed{D\in\mathbb Z.}
\tag{C76.7}
$$

Connectivity and uniqueness of a source point at each location force exactly

$$
x_j=z+ju,
\qquad j=0,1,\ldots,D,
$$

for one unit vector `u`, with only the consecutive contacts `x_jx_{j+1}` in the positive support.

At each internal chain vertex, equilibrium equates the two adjacent contact stresses. Hence every chain edge has one common positive weight `a_0`. Endpoint equilibrium at `z`, against the diameter edge of weight one and length `D`, gives `a_0=D`. Thus

$$
\boxed{\alpha_{x_jx_{j+1}}=D\quad(0\le j<D).}
\tag{C76.8}
$$

This proves C76.

---

## 5. KKT-polytope consequence

Let `S` be the compact normalized KKT polytope. The linear functional `s -> S_z(s)` is at most one. C76 proves:

### Corollary C76.2 — the exact star face is a singleton

For `D>=20`,

$$
\{s\in S:S_z(s)=1\}
$$

is either empty or consists of the unique straight-chain stress C76.6-C76.8.

For any fixed configuration with no straight unit diameter chain through `z`, compactness therefore gives

$$
\max_{s\in S}S_z(s)<1.
\tag{C76.9}
$$

The gap is configuration-dependent; C76 makes no uniform-in-`D` claim.

If a fixed configuration does contain the chain face and `s_m in S` satisfies `S_z(s_m)->1`, every limit point of `s_m` is the same straight-chain stress. Thus the tiny transverse KKT coefficients in a near-star full-support stress are literally convergence toward one exposed chain vertex of the stress polytope.

---

## 6. Interaction with C75 and the current frontier

C75 is independent and complementary: a near-capacity force-visible core must have total missing-diagonal slack `Sigma_diag=O(D)`, so almost all of its quadratic rhombic bulk is geometrically close to acquiring an additional unit diagonal, regardless of KKT weights.

C76 says that the stress-side near-zero degeneration points toward a one-dimensional chain certificate. Thus the remaining C-II obstruction is now a precise mismatch:

```text
stress polytope:
    relative-interior stress -> straight-chain KKT vertex

weight-free geometry:
    quadratic clean rhombic bulk -> near-triangular missing-diagonal medium
```

A closing theorem must make those two limits incompatible uniformly across growing configurations.

Natural routes are:

1. show an exposed straight-chain KKT face cannot coexist with a near-capacity C75/C73 bulk;
2. use another normalized stress certificate supported by the transverse bulk and prove its mixing weight cannot vanish at the C66 scale;
3. derive a capacity loss from the presence of the exact/asymptotic diameter chain; or
4. use the reciprocal dual to convert vanishing transverse stress weights into forbidden dual collapse.

## Compact handoff

**C76:** for `D>=20`, any normalized KKT stress with all beta mass incident to one diameter vertex is exactly the single-edge straight-chain stress:

`H_s={za}`, `beta_za=1`, `D` integer, `C_s` is `D` consecutive unit edges on segment `za`, and every chain contact has `alpha=D`.

Proof:

`S_z=1 -> C68 Q_z=0 -> every positive contact radial -> every radial branch must carry star beta -> two branches would have port angle >=60 degrees but C18 forces diameter-partner angle <60 degrees -> one branch -> one leaf -> straight chain.`

**Status:** still open. C66-C74 near-zero stress is now convergence toward a straight-chain KKT face, while C75 supplies the first weight-free near-triangular bulk constraint.