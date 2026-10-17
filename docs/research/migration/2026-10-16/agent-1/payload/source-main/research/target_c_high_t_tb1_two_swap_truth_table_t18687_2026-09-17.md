# Target C-II — complete non-shell truth table for two exact TB1 swaps

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the parity-thinned one-sign strong-TB1 finite-swap reduction; no canonical promotion claimed  
**Scope:** two retained nonadjacent exact-swap coordinates in the one-sign strong-TB1 branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** max-swap inheritance lemma; common oriented swap-axis cone; uniform exact-swap scale `q_i=O(D^-1)`  
**Certificate:** `research/verify_target_c_high_t_tb1_two_swap_truth_table_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The max-swap inheritance theorem showed that a joint `11` obstruction not already present at the larger-`q` singleton state must lie in an `O(D^-2)` boundary shell. A second interpolation, now between the two opposite singleton states, makes the local Boolean classification complete.

For a previously strict pair whose endpoints lie in retained layers `i,j`, write

\[
r_{00}=r,
\qquad
r_{10}=r-q_iw_i,
\qquad
r_{01}=r+q_jw_j,
\qquad
r_{11}=r-q_iw_i+q_jw_j,
\]

with

\[
q_i,q_j\le {Q\over D},
\qquad
|w_i-w_j|\le {C\over D}.
\]

The new statement is:

> **Two-singleton shell lemma.** If both singleton states `10` and `01` violate the same distance boundary while `00` is strict, then the original pair lies within `O(D^-2)` of that boundary.

Since all four states differ by only `O(D^-1)`, for sufficiently large `D` they cannot hit opposite boundaries (`1` versus `D`) in the same local truth table. Combining this with max-swap inheritance gives an exact asymptotic classification.

If

\[
q_i>q_j,
\]

then outside the lower and upper `O(D^-2)` shells the only possible bad-pattern sets among

\[
\{10,01,11\}
\]

are

\[
\boxed{
\varnothing,
\quad
\{10\},
\quad
\{01\},
\quad
\{10,11\}.
}
\]

If `q_j>q_i`, interchange `10` and `01`. If `q_i=q_j`, the persistent two-pattern case is also forced into the shell, so only

\[
\varnothing,
\{10\},
\{01\}
\]

remain outside the shell.

Thus the non-shell inactive CSP is not a general binary CSP or even a general 2-SAT instance. Every local constraint is either a one-state singleton obstruction or a persistent obstruction attached to the strictly larger exact-swap magnitude. Persistent edges strictly decrease `q` and therefore form a DAG. Every local pattern that violates this truth table is forced into the already rigid `D^-2` shells; the upper shell is automatically a superdiameter geometric thrackle.

---

## 1. Setup

Let

\[
a=-q_iw_i,
\qquad
b=+q_jw_j.
\tag{TT.1}
\]

Then

\[
r_{10}=r+a,
\qquad
r_{01}=r+b.
\tag{TT.2}
\]

The singleton displacement vectors are almost opposite because `w_i,w_j` lie in one oriented inverse-`D` cone.

Define

\[
\lambda={q_j\over q_i+q_j},
\qquad
\mu={q_i\over q_i+q_j},
\qquad
h={q_iq_j\over q_i+q_j}.
\tag{TT.3}
\]

Then `lambda+mu=1` and

\[
\lambda a+\mu b
=h(w_j-w_i)=:e.
\tag{TT.4}
\]

Hence

\[
\boxed{
\lambda r_{10}+\mu r_{01}=r+e,
}
\tag{TT.5}
\]

with

\[
|e|
\le {Ch\over D}
\le {CQ\over D^2}.
\tag{TT.6}
\]

So the original state `00` lies within `O(D^-2)` of the segment joining the two singleton states.

---

## 2. Both singleton states hit the unit boundary

Assume

\[
|r|>1,
\qquad
|r_{10}|\le1,
\qquad
|r_{01}|\le1.
\tag{TT.7}
\]

The closed unit disk is convex, so (TT.5) gives

\[
|r+e|\le1.
\tag{TT.8}
\]

Therefore

\[
|r|\le1+|e|
\le1+{CQ\over D^2}.
\tag{TT.9}
\]

Thus

\[
\boxed{
0<|r|-1\le {CQ\over D^2}.
}
\tag{TT.10}
\]

A pair that blocks both opposite singleton swaps at the lower boundary is necessarily an ultra-near-unit pair.

---

## 3. Both singleton states hit the diameter boundary

Assume

\[
|r|<D,
\qquad
|r_{10}|\ge D,
\qquad
|r_{01}|\ge D.
\tag{TT.11}
\]

Let

\[
z=\lambda r_{10}+\mu r_{01}=r+e.
\tag{TT.12}
\]

The squared-norm interpolation identity gives

\[
|z|^2
=
\lambda|r_{10}|^2
+\mu|r_{01}|^2
-\lambda\mu|r_{10}-r_{01}|^2.
\tag{TT.13}
\]

Since

\[
|r_{10}-r_{01}|=|a-b|\le q_i+q_j\le {2Q\over D},
\tag{TT.14}
\]

we obtain

\[
|z|^2
\ge
D^2-{Q^2\over D^2}.
\tag{TT.15}
\]

On the other hand, `z=r+e` and (TT.6) imply

\[
|z|^2-|r|^2
\le
2D|e|+|e|^2
\le
{2CQ\over D}+{C^2Q^2\over D^4}.
\tag{TT.16}
\]

Combining (TT.15)--(TT.16),

\[
D^2-|r|^2
\le
{2CQ\over D}
+{Q^2\over D^2}
+{C^2Q^2\over D^4}.
\tag{TT.17}
\]

The singleton upper violation already gives `|r|=D-O(D^-1)`, so `D+|r|>=D` for large `D`. Therefore

\[
\boxed{D-|r|=O(D^{-2}).}
\tag{TT.18}
\]

Thus a pair that blocks both opposite singleton swaps at the upper boundary is necessarily an ultra-near-diameter pair.

---

## 4. Opposite boundaries cannot occur in one local truth table

Every two Boolean states differ by a displacement of norm at most

\[
q_i+q_j\le {2Q\over D}.
\tag{TT.19}
\]

If one state had length at most `1` while another had length at least `D`, the reverse triangle inequality would give

\[
D-1\le {2Q\over D},
\tag{TT.20}
\]

which is false for all sufficiently large `D`.

Hence all bad states of one pair, if there is more than one, hit the same boundary once `D` is large.

This removes a possible mixed lower/upper exception from the Boolean classification.

---

## 5. Complete truth table when `q_i>q_j`

Assume now

\[
q_i>q_j.
\tag{TT.21}
\]

Work outside both `O(D^-2)` boundary shells established in Sections 2--3 and in the max-swap inheritance theorem.

### 5.1 `10` and `01` cannot both be bad

If both singleton states were bad, Section 4 says they hit the same boundary. Sections 2--3 then force the corresponding `D^-2` shell, contrary to the present assumption.

Thus at most one singleton state is bad.

### 5.2 `11` cannot be bad while `10` is safe

Because `q_i` is the larger swap magnitude, the max-swap inheritance theorem applies with `10` as the larger singleton state. If `00` and `10` are safe but `11` is bad, the pair lies in a `D^-2` shell.

Therefore, outside the shell,

\[
11\text{ bad}\Longrightarrow10\text{ bad}.
\tag{TT.22}
\]

### 5.3 Allowed bad-pattern sets

The preceding two facts leave exactly

\[
\boxed{
\varnothing,
\quad
\{10\},
\quad
\{01\},
\quad
\{10,11\}.
}
\tag{TT.23}
\]

No other subset of `\{10,01,11\}` can occur outside the two ultra-thin shells.

The interpretation is exact:

- `\{10\}`: a blocker attached to layer `i` is disarmed when layer `j` is also swapped;
- `\{01\}`: a blocker attached to the smaller-`q` layer `j` is disarmed when layer `i` is also swapped;
- `\{10,11\}`: a persistent blocker survives the partner swap, and its responsible endpoint is the strictly larger-`q` layer.

---

## 6. Symmetry and equal swap magnitudes

If

\[
q_j>q_i,
\]

interchange the labels. The allowed non-shell bad-pattern sets are

\[
\boxed{
\varnothing,
\quad
\{10\},
\quad
\{01\},
\quad
\{01,11\}.
}
\tag{TT.24}
\]

If

\[
q_i=q_j,
\]

then either singleton may be treated as a larger-`q` singleton. Therefore a bad `11` state together with either safe singleton forces the shell, while both singletons bad also force the shell. Outside the shell,

\[
\boxed{
\varnothing,
\quad
\{10\},
\quad
\{01\}
}
\tag{TT.25}
\]

are the only possibilities.

---

## 7. Global finite-swap normal form

For every non-shell pair joining two retained layers, orient any persistent obstruction from its responsible singleton layer toward the partner layer.

Equations (TT.23)--(TT.24) show that a persistent edge always satisfies

\[
\boxed{q_{\rm source}>q_{\rm target}.}
\tag{TT.26}
\]

Hence the persistent-blocker digraph is a DAG.

All remaining non-shell binary behavior consists of disarmable singleton implications. All other local truth tables are confined to

\[
1<|xy|\le1+O(D^{-2})
\]

or

\[
D-O(D^{-2})\le|xy|<D.
\]

The upper shell lies above `sqrt(D^2-1)` and is therefore a geometric thrackle.

Thus the strong-TB1 subset-selection problem has the asymptotic form

```text
non-shell constraints:
    singleton implication
    or q-descending persistent obstruction

exceptional binary constraints:
    ultra-near-unit D^-2 shell
    or superdiameter D^-2 thrackle shell.
```

This is stricter than the previous statement that each inactive pair merely has support on at most two swap coordinates.

---

## 8. Remaining obstruction

This theorem still does not force a safe nonzero subset. A finite implication graph can feed into `q`-descending persistent blockers, and a global minimum-`q` coordinate can be blocked through a chain of disarmable implications ending at a larger-`q` vertex that has a persistent edge back downward. The truth-table theorem rules out many local patterns but not that global directed architecture.

The next closure target is therefore explicit:

1. exploit path-layer geometry to rule out long implication-to-descending-blocker chains; or
2. prove that blocking every nonzero subset forces a positive-density population in one of the two `D^-2` shells, where the ultra-near-unit matching / superdiameter-thrackle machinery can be applied.

No claim of C-II closure is made.
