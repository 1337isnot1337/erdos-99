<!-- theorem-state: {"artifact_id":"ART-A7EB34AEE617","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact loaded-boundary / harmonic-diameter budget

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** exact post-ZF ledger cancellation  
**Target:** UF near-circle branch after TD  
**Depends on:** HB, C40/ZK, loaded degree-three slack definition, ZU/ZT for corollaries  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The near-circle work repeatedly uses the fact that almost every loaded hull interval is a direct unit contact. There is an exact finite way to separate those mandatory boundary contacts from every additional loaded-loaded contact.

Define

\[
\boxed{
E_{BB}:=e_{BB}-(q-x_B)\ge0,
}
\tag{NBd.1}
\]

where HB proves the nonnegativity.

Let

\[
S:=\sum_r\delta_r,
\]

and retain the ZK nonnegative currencies

- `R_I=sum r_r`, total internal Eppstein slack;
- `s_B=3q-e_{BI}-2e_{BB}`, unused loaded contact-degree capacity;
- `c_I`, number of unloaded components;
- `s_C`, pinned-contact stress surplus.

Then every finite post-ZF survivor satisfies the exact identity

\[
\boxed{
S+R_I+s_B+2E_{BB}+3c_I+s_C
=q+2x_B.
}
\tag{NBd.2}

\]

Thus in the PR #119 small-outer-walk endpoint,

\[
q/D\to\pi,
\qquad
x_B=o(D),
\]

the entire collection of nonnegative currencies satisfies

\[
\boxed{
\frac1D
\left(
S+R_I+s_B+2E_{BB}+3c_I+s_C
\right)
\to\pi.
}
\tag{NBd.3}

\]

TD therefore has an immediate full-core consequence. If `zeta=0`, then

\[
S\ge(2-o(1))D,
\]

so

\[
\boxed{
R_I+s_B+2E_{BB}+3c_I+s_C
\le(\pi-2+o(1))D.
}
\tag{NBd.4}

\]

This does not close the branch, but it shows that the two diameter-scale harmonic carriers already consume more than `63%` of the complete loaded-boundary incidence budget.

---

## 1. Exact attachment-contact count

For one unloaded component, ZK defines

\[
s_r=e_r+t_r-2n_r-1,
\qquad
r_r=2n_r-\delta_r-2-e_r,
\]

and proves

\[
t_r-\delta_r-3=s_r+r_r.
\]

Summing over all components gives

\[
\boxed{
e_{BI}=S+3c_I+s_C+R_I.}
\tag{1.1}
\]

Here every contact from an unloaded component to a loaded terminal is counted once in `e_BI`, including duplicate contacts from one component to the same loaded terminal.

---

## 2. Loaded degree-three slack

The loaded degree cap gives

\[
e_{BI}+2e_{BB}\le3q.
\]

By definition

\[
\boxed{s_B:=3q-e_{BI}-2e_{BB}\ge0,}
\tag{2.1}
\]

so this is the exact identity

\[
\boxed{e_{BI}+2e_{BB}+s_B=3q.}
\tag{2.2}
\]

Insert (1.1):

\[
S+3c_I+s_C+R_I+2e_{BB}+s_B=3q.
\tag{2.3}
\]

---

## 3. Subtract the mandatory hull-side baseline

HB proves

\[
e_{BB}\ge q-x_B.
\]

Define `E_BB` by NBd.1, so

\[
e_{BB}=q-x_B+E_{BB}.
\]

Substitute in (2.3):

\[
S+3c_I+s_C+R_I
+2(q-x_B+E_{BB})
+s_B
=3q.
\]

Rearranging gives exactly

\[
\boxed{
S+R_I+s_B+2E_{BB}+3c_I+s_C
=q+2x_B.
}
\]

This proves NBd.2.

No ZR/ZF diameter-edge count is needed after HB and ZK are available; the identity is purely a loaded-contact incidence ledger.

---

## 4. Relation to ZU and the mixed defect

Put

\[
k:=d_H+s_Z.
\]

ZU gives

\[
c_I+e_{BB}+s_C=q-2+k.
\]

Using `e_BB=q-x_B+E_BB`,

\[
\boxed{
E_{BB}+c_I+s_C
=k+x_B-2.
}
\tag{4.1}

\]

Thus, up to the finite constant two, the mixed/diameter defect `k` is exactly the sum of

1. extra loaded-loaded contacts beyond good hull sides;
2. unloaded-component count;
3. pinned-contact stress surplus;

minus the outer-walk excess already used to define the baseline.

ZT gives

\[
q=x_B+Q+2k.
\]

Combining with (4.1) recovers the AR residual identity and provides consistency checks; NBd.2 is not a new assumption or an independent scalar degree of freedom.

---

## 5. Safe consequences

Because all terms on the left of NBd.2 are nonnegative,

\[
\boxed{S\le q+2x_B,}
\tag{5.1}
\]

which recovers the near-circle `S/D<=pi` estimate without using the false `e_BB/D->pi` statement corrected on PR #119.

More sharply,

\[
\boxed{2E_{BB}+3c_I+s_C\le q+2x_B-S.}
\tag{5.2}
\]

and

\[
\boxed{R_I+s_B\le q+2x_B-S.}
\tag{5.3}
\]

separately.

Using `k>=E_BB+c_I+s_C-x_B+2` from (4.1) and ZT, one also obtains the safe face-defect lower bound

\[
\boxed{
Q
\ge
2S-q-5x_B-O(1),
}
\tag{5.4}
\]

by eliminating the cheapest possible remaining currencies. In the strict near-circle limit this reduces to

\[
\liminf Q/D\ge2\liminf S/D-\pi,
\]

which is weaker than UF at its current crossover but becomes useful if TD is strengthened further.

---

## 6. Insert TD

TD proves in the UF near-circle phase

\[
\liminf S/D\ge\Sigma_{cap}(A_\zeta).
\]

Therefore NBd.3 gives

\[
\boxed{
\limsup
\frac{R_I+s_B+2E_{BB}+3c_I+s_C}{D}
\le
\pi-\Sigma_{cap}(A_\zeta).
}
\tag{6.1}
\]

At UF's population crossover,

\[
\Sigma_{cap}=0.9835132379\ldots,
\]

so the remaining total budget is at most

\[
2.1580794157\ldots D+o(D).
\]

At full core,

\[
\Sigma_{cap}=2,
\]

and the remainder is at most

\[
(\pi-2)D
=1.1415926535\ldots D.
\]

The significance is structural rather than numerical: every future theorem that forces any one of `R_I,s_B,E_BB,c_I,s_C` automatically subtracts from the same fixed budget already heavily occupied by the harmonic graph diameters.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `e_BI=S+3c_I+s_C+R_I` | proved | exact component identity from ZK |
| NBd.2 exact boundary budget | proved | loaded degree slack + HB baseline |
| relation `E_BB+c_I+s_C=k+x_B-2` | proved | ZU substitution |
| near-circle total budget `pi D+o(D)` | proved conditional on PR #119 endpoint | `q/D->pi`, `x_B=o(D)` |
| full-core remainder `<=pi-2` | proved conditional on TD full-core | insert `S/D>=2` |
| Level I | still open | remaining defect budget is still positive |

---

## 8. Next target

The full-core near-circle phase now has two simultaneous normal forms:

1. TD: two complementary diameter-scale harmonic carriers at the cap-minimal endpoint;
2. NBd: only `(pi-2)D+o(D)` total incidence budget remains for every other defect currency.

A useful closing theorem need only show that the two-carrier interface costs more than `pi-2` in any combination of

\[
R_I+s_B+2E_{BB}+3c_I+s_C.
\]

This is a substantially sharper target than another global face-count estimate.
