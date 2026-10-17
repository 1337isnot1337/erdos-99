> Generated reading edition · [exact source](../../../docs/reports/target_c_rd_endpoint_singleton_layer_2026-09-10.md) · source SHA-256 `0cf42e3e1581628f21f1d2b5d3c0752d765cde7b83075c5378dcebef7cc1f723`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-952D377B86FD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — the RSR/DD endpoint forces a linear singleton unloaded layer

**Date:** 2026-09-10  
**Branch base:** `85d449e979dac29999eb0584a28691042de37925`  
**Depends on:** RD/RX on this branch, PC, ZI, DB  
**Run type:** exact equality-ledger extraction / endpoint structural reduction  
**Target:** Target C, C-II after ZF

## LEVEL I STATUS

`STILL OPEN`.

The RSR/DD optimizer gives the exact generic post-ZF threshold

$$
\lambda_{RD}=0.5981536184601480\ldots
$$

with unique scalar endpoint

$$
y_{RD}=1.5245227034919424\ldots,
\qquad
p_{RD}=3.0231369667364346\ldots .
$$

This report extracts the equality topology behind that endpoint.  If an unbounded
post-ZF survivor sequence were to satisfy

$$
\frac{e_{BB}+2s_C}{D}\to\lambda_{RD},
\tag{SL.1}
$$

then all of the following are forced:

$$
\boxed{
\frac hD\to y_{RD},
\qquad
\frac{\operatorname{per}F}{D}\to p_{RD},
}
\tag{SL.2}
$$

$$
\boxed{
Q=o(D),\quad s_Z=o(D),\quad d_P=o(D),\quad d_H=o(D),
}
\tag{SL.3}
$$

$$
\boxed{
\frac aD\to y_{RD},
\qquad
\frac{q-a}{D}\to0,
}
\tag{SL.4}
$$

where `a` is the number of missing force-hull side contacts / OP outer pockets and
`d_P` is the total outer-pocket degree excess above triangles.

Most importantly, if `N_1` is the number of unloaded contact components consisting of
a single vertex, then

$$
\boxed{
\liminf\frac{N_1}{D}
\ge y_{RD}-2\lambda_{RD}
=0.3282154665716463\ldots>0.
}
\tag{SL.5}
$$

The cancellation in SL.5 is exact: the lower bound is independent of how the endpoint
surplus splits between loaded-loaded contacts and pinned-contact stress surplus.

Thus an RD-near-extremal survivor cannot be a diffuse generic post-ZF core.  It must
have, simultaneously,

1. asymptotically no bounded-face or mixed-rank defect;
2. asymptotically no diameter-component defect;
3. almost every loaded force-hull side missing from the unit-contact graph;
4. almost every outer pocket triangular in the combinatorial sense; and
5. a positive linear population of singleton unloaded components.

---

## 1. Scalar endpoint localization

RX proves that the RD objective has a unique global minimizer.  Under SL.1 this gives

$$
\frac hD\to y_{RD},
\qquad
\frac{P_F}{D}\to p_{RD},
\tag{1.1}
$$

where `P_F=per(F)` and

$$
p_{RD}=p_e(y_{RD})<2y_{RD}.
\tag{1.2}
$$

The endpoint lies where the two area currencies and the two cavity obstructions meet:

$$
\Phi(y_{RD})=\Psi(p_{RD}),
\tag{1.3}
$$

and both JC and DD are active.

Put

$$
z_D:=\frac{Q+2s_Z}{D}.
\tag{1.4}
$$

RD Section 3 bounded the normalized DD-plus-exceptional-face cavity capacity by

$$
F_{y,p}(z)
=
\frac1{\sqrt6}(2y-z)^{3/2}\sqrt{2y-z-p}
+\frac{z^2}{4\pi},
\tag{1.5}
$$

and proved that `F_{y,p}(z)` is strictly decreasing in `z` throughout the feasible
range.  The RD scalar endpoint uses the relaxed value `F_{y,p}(0)` with equality.
Therefore any endpoint sequence must have

$$
\boxed{z_D\to0.}
\tag{1.6}
$$

Since `Q,s_Z>=0`, this immediately gives

$$
\boxed{Q=o(D),\qquad s_Z=o(D).}
\tag{1.7}
$$

---

## 2. DD equality forces almost every hull side to be missing

DD gives the exact outer-pocket estimate

$$
H_{out}
\le
\frac1{\sqrt6}(x_B+a)^{3/2}
\sqrt{b-P_F}.
\tag{2.1}
$$

RD replaced the first factor by the larger quantity `b`, using only

$$
\boxed{x_B+a\le b.}
\tag{2.2}
$$

At the endpoint,

$$
\frac bD
=
2\frac hD-rac{Q+2s_Z}{D}
\to2y_{RD},
\tag{2.3}
$$

while

$$
\frac{b-P_F}{D}
\to2y_{RD}-p_{RD}>0.
\tag{2.4}
$$

Thus the DD capacity used in RD has a strictly positive `D^2` limit.  If for some
`eta>0` one had along a subsequence

$$
\frac{b-(x_B+a)}D\ge\eta,
$$

then the first factor in (2.1) would lose a fixed positive amount on the `D^{3/2}`
scale while the square-root detour retains a fixed positive `D^{1/2}` limit.  This
would produce a fixed positive `D^2` loss relative to the active RD endpoint
capacity, contradicting SL.1 and the equality of the endpoint lower and upper area
budgets.

Hence

$$
\boxed{
\frac{x_B+a}{D}-\frac bD\to0.
}
\tag{2.5}
$$

But `x_B=b-q`, so

$$
b-(x_B+a)=q-a.
$$

Therefore

$$
\boxed{q-a=o(D).}
\tag{2.6}
$$

Since `q=h+d_H` and `d_H>=0`, we will shortly get `q/D->y_RD`; then (2.6) will give
`a/D->y_RD`.

---

## 3. PC collapses four defect currencies

PC gives the exact terminal partition

$$
\boxed{
q=a+d_P+Q+2(d_H+s_Z).
}
\tag{3.1}
$$

Therefore

$$
q-a=d_P+Q+2d_H+2s_Z.
\tag{3.2}
$$

Every term on the right is nonnegative.  Combine (2.6) with (1.7):

$$
\boxed{
d_P=o(D),\qquad d_H=o(D).}
\tag{3.3}
$$

The second relation and `q=h+d_H` yield

$$
\boxed{
\frac qD\to y_{RD}.
}
\tag{3.4}
$$

Then (2.6) yields

$$
\boxed{
\frac aD\to y_{RD}.
}
\tag{3.5}
$$

The interpretation of `d_P=o(D)` is strong because `a=Theta(D)`: all but `o(D)` of
the outer pockets have degree exactly three.  Indeed every nontriangular pocket
contributes at least one unit to

$$
d_P=\sum_P(k_P-3).
$$

Thus

$$
\boxed{
\#\{\text{nontriangular outer pockets}\}=o(D).
}
\tag{3.6}
$$

---

## 4. Exact contact/component bookkeeping

Let

$$
t_D:=\frac{e_{BB}}D,
\qquad
s_D:=\frac{s_C}{D}.
$$

Pass to a further subsequence so

$$
t_D\to t,
\qquad
s_D\to s.
\tag{4.1}
$$

Endpoint surplus gives

$$
\boxed{t+2s=\lambda_{RD}.}
\tag{4.2}
$$

PC gives

$$
e_{BB}=q-a+c_B.
\tag{4.3}
$$

By (2.6),

$$
\boxed{
\frac{c_B}{D}\to t.
}
\tag{4.4}
$$

Thus, asymptotically, every linear loaded-loaded contact at the endpoint is a non-hull
loaded chord: almost no force-hull side itself is a contact edge.

PC also gives the exact pocket/component balance

$$
\boxed{
a+(d_H+s_Z)=c_I+c_B+s_C+2.}
\tag{4.5}
$$

Using (1.7), (3.3), (3.5), and (4.4),

$$
\boxed{
\frac{c_I}{D}
\to y_{RD}-t-s
=y_{RD}-\lambda_{RD}+s.
}
\tag{4.6}
$$

In particular, since `s>=0`,

$$
\boxed{
\liminf\frac{c_I}{D}
\ge y_{RD}-\lambda_{RD}
=0.9263690850317943\ldots .
}
\tag{4.7}
$$

So the RD endpoint requires at least about `0.926D` unloaded contact components.
This alone is not a contradiction because many components may be singletons.

---

## 5. ZI forces at least `0.328D` singleton components

For each unloaded component `I_r`, let `delta_r` be the graph diameter of its induced
contact graph, with `delta_r=0` for a singleton.  ZI gives

$$
\boxed{
\sum_r\delta_r
\le
6-3(d_H+s_Z)+e_{BB}+3s_C.
}
\tag{5.1}
$$

Divide by `D` and use (1.7), (3.3), and (4.1):

$$
\limsup\frac1D\sum_r\delta_r
\le t+3s
=\lambda_{RD}+s.
\tag{5.2}
$$

Let `N_{\ge2}` be the number of unloaded components with at least two vertices.
Every such connected component has graph diameter at least one, so

$$
N_{\ge2}\le\sum_r\delta_r.
\tag{5.3}
$$

Let

$$
N_1:=c_I-N_{\ge2}
$$

be the number of singleton unloaded components.  Combining (4.6), (5.2), and (5.3),

$$
\begin{aligned}
\liminf\frac{N_1}{D}
&\ge
(y_{RD}-\lambda_{RD}+s)
-(\lambda_{RD}+s)\\
&=\boxed{y_{RD}-2\lambda_{RD}.}
\end{aligned}
\tag{5.4}

The `s` dependence cancels exactly.

Using the numerical orientation values from RX,

\[
y_{RD}-2\lambda_{RD}
=0.3282154665716463\ldots .
\tag{5.5}
$$

The sign is not close: the exact RX characterization gives `y_RD>3/2` and the
certified theorem gives `lambda_RD<0.599` numerically from the same root bracket, so
already

$$
y_{RD}-2\lambda_{RD}>1.5-1.198=0.302.
$$

Thus the linear singleton population is structurally robust, not a decimal artifact.

---

## 6. Diameter topology at the endpoint

The endpoint also has

$$
d_H=q-h=o(D).
\tag{6.1}
$$

Woodall's straight-line thrackle classification, now available on `main`, says that
for each finite source either

1. `d_H=0` and the full loaded diameter graph is connected odd-unicyclic with pendant
   leaves; or
2. `d_H>0` and the diameter graph is a caterpillar forest with exactly `d_H`
   components.

Thus an RD endpoint sequence has only two possibilities:

- infinitely often the connected odd-unicyclic Woodall topology; or
- a caterpillar forest with `o(D)` components despite `q~y_RD D` loaded terminals.

In either case the diameter graph has asymptotically one component per `omega(1)`
terminals, while the contact graph simultaneously has at least `0.328D` singleton
unloaded components.  This severe mismatch between diameter connectivity and contact
fragmentation is the next structural target.

---

## 7. What remains to close the endpoint

The new normal form is

```text
h/D -> y_RD = 1.5245227...
per(F)/D -> p_RD = 3.0231369...
Q + 2s_Z = o(D)
d_H = o(D)
d_P = o(D)
q/D -> y_RD
a/D -> y_RD
q-a=o(D)
nontriangular outer pockets=o(D)

c_I/D >= 0.926369... asymptotically
singleton unloaded components / D >= 0.328215...

Woodall diameter topology:
    either one connected odd-unicyclic graph with leaves,
    or o(D) caterpillar components.
```

A Level I closure now needs one more geometric bridge.  The most promising local
route is to exploit that almost all outer pockets are triangular while a positive
linear set of unloaded components are singleton vertices.  A singleton component has
at least three distinct loaded attachments, whereas a triangular outer-pocket apex
already lies on two unit contact edges joining consecutive loaded hull endpoints.
Any uniform turning/detour cost for the required third loaded attachment would sum
over a linear family and contradict the small endpoint detour

$$
\frac{b-P_F}{D}
\to2y_{RD}-p_{RD}
=0.0259084402474501\ldots .
$$

No such injection or turning lemma is claimed here; one unloaded component may still
interact with several pockets, so that step must be proved rather than assumed.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| RD endpoint localizes `(y,p)` | proved in RX | unique optimizer |
| `Q,s_Z=o(D)` | proved | strict decrease of RD cavity capacity in `z` |
| `q-a=o(D)` | proved | active DD bound + strict positive endpoint detour |
| `d_P,d_H=o(D)` | proved | exact PC nonnegative partition |
| `a/D,q/D->y_RD` | proved | preceding identities |
| `c_I/D->y_RD-lambda_RD+s` | proved subsequentially | PC balance |
| `N_1/D>=y_RD-2lambda_RD-o(1)` | proved | ZI diameter budget; `s` cancels |
| Woodall endpoint interpretation | proved from current main theorem | `d_H` is exact component switch |
| singleton-to-pocket injection | not proved | components may meet several pockets |
| Level I | still open | final local geometric bridge remains |

---

## 9. Next run

Prove a local lemma for a singleton unloaded component adjacent to a degree-three OP
outer pocket.  The target is a quantitative alternative: either the component cannot
serve as the pocket apex, or its mandatory third loaded attachment forces a definite
chain-chord detour / force-hull turning cost.  Because SL.5 supplies a linear number of
singletons while the total normalized detour at the endpoint is only about `0.02591`,
even a small uniform cost on a positive fraction would exclude the endpoint.