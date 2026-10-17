> Generated reading edition · [exact source](../../research/target_c_open_cell_strong_scc_bidirected_staircase_2026-10-04.md) · source SHA-256 `f2c27fc87849163db8094cdfb2242854a29bde8dacd5c23619f5a88fa0763286`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C: strong open-cell SCC collapses to a bidirected staircase tree

Date: 2026-10-04
Base main: 883a88ea86b9dfaf9d7843aa18ce0d8b6324c49d
Immediate dependency: b24d2df79d89b10f32e7ed17fc43a30af43fe975
Status: proof-only Target C-II candidate; theorem-state authority unchanged.
LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.

This note attacks the strongly connected branch left by the nonconstant open-witness-cell
condensation route. The preceding sign-nesting note proves, under the fixed-star
open-cell hypotheses, that the positive and negative actual-diameter support types are
separately nested interval chains and that both chains contain full support.

The result below shows that strong connectivity leaves no freedom in those two chains:
they must be the same maximal staircase chain. Thus the nonconstant open-cell strong
branch has the same support skeleton as the exact-phase opposed-bundle tree, but
without any claim of exact-phase bundlewise KKT balance.

No computation is a proof premise.

## 1. Abstract signed interval setup

Let the selected train cuts be indexed by $1,\ldots,m$, with physical layers
$0,\ldots,m$. An actual diameter joining layers $a<b$ has support

$$
I(a,b)=\{a+1,\ldots,b\}.
$$

Orient its diameter vector from the lower layer to the higher layer. Relative to a
fixed direction $e$ in the open witness cell, put $w=Je$. The sign
$\operatorname{sgn}(r_h\cdot w)$ is strict and fixed throughout the cell.

Thus a positive row with endpoints $a<b$ gives the directed gap edge

$$
a\longrightarrow b,
$$

while a negative row gives

$$
b\longrightarrow a.
$$

Let $\mathcal C_+$ and $\mathcal C_-$ be the sets of distinct positive and
negative support types. Assume:

1. each of $\mathcal C_+$ and $\mathcal C_-$ is a chain under inclusion;
2. both contain the full interval $\{1,\ldots,m\}$;
3. the full directed gap multigraph is strongly connected.

The first two statements are exactly the output of the preceding open-cell sign-nesting
theorem. Multiplicity is retained in the physical graph but is irrelevant to the
support classification below.

## 2. Every layer occurs in each sign family

Write a nested sign chain in endpoint form

$$
(a_1,b_1),\ldots,(a_s,b_s),
$$

from largest to smallest support. Then

$$
a_1\le a_2\le\cdots\le a_s<b_s\le\cdots\le b_2\le b_1.
\tag{2.1}
$$

Hence a fixed layer vertex can occur in this chain only as a lower endpoint or only
as an upper endpoint, never as both.

Suppose a layer vertex $j$ is not an endpoint of any positive row. Every gap edge
incident with $j$ then comes from the negative family. By (2.1), the negative chain
can make $j$ only a lower endpoint, only an upper endpoint, or omit it entirely.
Because negative edges are directed upper-to-lower, $j$ then has only incoming
negative edges, only outgoing negative edges, or no incident edge. In every case the
full directed graph fails to be strongly connected.

Therefore every layer vertex occurs as an endpoint in the positive family. The same
argument with the signs reversed proves the same for the negative family:

$$
\boxed{\text{every }j\in\{0,\ldots,m\}\text{ occurs as an endpoint in each sign chain.}}
\tag{2.2}
$$

Let the smallest positive type be $(A_+,B_+)$. If $B_+\ge A_++2$, every vertex
strictly between $A_+$ and $B_+$ is omitted from the entire positive chain,
contradicting (2.2). Hence

$$
B_+=A_++1.
$$

Similarly $B_-=A_-+1$ for the negative chain. Put

$$
c_+=B_+,\qquad c_-=B_-.
$$

In the positive family every vertex below $c_+$ is a lower endpoint and has only
positive outgoing edges; every vertex at least $c_+$ is an upper endpoint and has
only positive incoming edges. For the negative family the directions are reversed.

If $c_+<c_-$, every vertex

$$
c_+\le j<c_-
$$

has only incoming edges from both sign families. If $c_+>c_-$, every vertex in the
reverse gap has only outgoing edges. Both contradict strong connectivity. Therefore

$$
\boxed{c_+=c_-=:c.}
\tag{2.3}
$$

Both sign chains use the same left/right split

$$
L=\{0,\ldots,c-1\},\qquad R=\{c,\ldots,m\}.
\tag{2.4}
$$

In particular every nonempty-support diameter in either sign family joins $L$ to
$R$.

## 3. A sign chain cannot skip two endpoints at once

Because full support is present, each chain begins at $(0,m)$ and ends at
$(c-1,c)$. By (2.2), no lower endpoint value $0,\ldots,c-1$ and no upper endpoint
value $c,\ldots,m$ can be skipped. Thus between consecutive distinct types,
the lower endpoint changes by $0$ or $1$, and the upper endpoint changes by
$0$ or $-1$.

The only possible two-coordinate step is

$$
(a,b)\longrightarrow(a+1,b-1).
\tag{3.1}
$$

Assume first that (3.1) occurs in the positive chain. Partition the layer vertices as

$$
S=\{0,\ldots,a\}\cup\{b,\ldots,m\},\qquad
T=\{a+1,\ldots,b-1\}.
\tag{3.2}
$$

Every earlier positive type has both endpoints in $S$, while every later positive
type has both endpoints in $T$. Hence no positive edge crosses $S|T$.

Strong connectivity requires at least one directed crossing each way. Both crossings
would therefore have to come from the negative chain. A negative edge directed
$T\to S$ must have endpoint form

$$
(\alpha,\beta),\qquad \alpha\le a,\quad \beta\le b-1,
$$

whereas a negative edge directed $S\to T$ must have

$$
(\alpha',\beta'),\qquad \alpha'\ge a+1,\quad \beta'\ge b.
$$

These two intervals are incomparable: $\alpha<\alpha'$ and $\beta<\beta'$.
A nested interval chain cannot contain both. Thus the negative family cannot supply
both crossing directions, contradicting strong connectivity.

The same argument with the signs exchanged excludes (3.1) in the negative chain.
Consequently every step in either chain removes exactly one support coordinate:

$$
(a,b)\longrightarrow(a+1,b)
\quad\text{or}\quad
(a,b)\longrightarrow(a,b-1).
\tag{3.3}
$$

It follows already that each sign chain has exactly $m$ distinct support types,
with support sizes

$$
m,m-1,\ldots,1.
\tag{3.4}
$$

## 4. The positive and negative staircases must coincide

Suppose the two chains first diverge immediately after a common type $(a,b)$.
By (3.3), one chain must trim the left endpoint and the other must trim the right
endpoint.

Assume first

$$
\mathcal C_+:\ (a,b)\to(a+1,b),
\qquad
\mathcal C_-:\ (a,b)\to(a,b-1).
\tag{4.1}
$$

Use the same partition (3.2). In the positive chain, every edge crossing $S|T$
after the divergence has lower endpoint in $T$ and upper endpoint in the right
part of $S$, hence is directed $T\to S$. Once the positive chain first trims the
right endpoint, all later positive types lie wholly in $T$.

In the negative chain, every crossing edge after the divergence has lower endpoint
in the left part of $S$ and upper endpoint in $T$. Since negative edges are
directed upper-to-lower, these are also directed $T\to S$. Once the negative chain
first trims the left endpoint, all later negative types lie wholly in $T$.

Earlier common types have both endpoints in $S$. Hence the full graph has no edge
from $S$ to $T$, contradicting strong connectivity.

If the two choices in (4.1) are reversed, the identical argument gives only
$S\to T$ crossings and no $T\to S$ crossing. Therefore first divergence is
impossible:

$$
\boxed{\mathcal C_+=\mathcal C_-.}
\tag{4.2}
$$

Combining (3.3), (3.4), and (4.2), there is one common maximal staircase

$$
I_1\supsetneq I_2\supsetneq\cdots\supsetneq I_m,
$$

with

$$
I_1=\{1,\ldots,m\},\qquad I_m=\{c\},\qquad |I_j|=m-j+1.
\tag{4.3}
$$

Every type occurs with at least one physical row of each strict transverse sign.

## 5. Exact bidirected-tree normal form

Associate the interval $I(a,b)$ with the undirected gap edge $\{a,b\}$.
Start with $\{0,m\}$. Under each one-endpoint trim in (3.3), the next edge shares
one endpoint with the preceding edge and introduces one previously unseen layer
vertex. After $m-1$ trims, all $m+1$ layer vertices have appeared.

Therefore the $m$ distinct simple support edges form a spanning tree $T$ on
$\{0,\ldots,m\}$. Equation (4.2) says every edge of $T$ is represented in both
directions:

$$
\boxed{\text{the simple directed support is exactly the bidirected tree }\overleftrightarrow T.}
\tag{5.1}
$$

Conversely, if the two sign families are the same maximal staircase, every tree edge
is present in both directions, so the directed gap graph is strongly connected.
Thus (5.1) is an exact characterization of the strong branch under the open-cell
sign-nesting hypotheses.

Because each of the $m$ support types has at least one positive and one negative
physical representative,

$$
\boxed{N_{\rm diam}^{\rm supp}\ge 2m.}
\tag{5.2}
$$

Moreover the support sizes are $m,m-1,\ldots,1$. Counting diameter--selected-cut
incidences with physical multiplicity gives

$$
\boxed{
\sum_h |I_h|
\ge 2\sum_{j=1}^m j
=m(m+1).
}
\tag{5.3}
$$

This is stronger than the earlier linear strong-SCC diameter count: at the current
fixed-star extraction $m=\Omega(D)$, the strong branch carries
$\Omega(D^2)$ actual diameter/train-cut incidences.

All support intervals contain the common cut $c$, so every one of the rows counted
in (5.2) joins opposite shores of that cut. Reusing canonical C-WOODALL exactly as in
the exact-phase nested-bundle report, the corresponding physical diameter subgraph
is bipartite and has no cycle. Hence it is a forest. In particular it uses at least

$$
\boxed{2m+1}
\tag{5.4}
$$

distinct physical diameter endpoints.

## 6. What this does not prove

The conclusion is a support theorem. Unlike the exact-phase bundle theorem, it does
not prove

$$
\sum_{h:I_h=I}\beta_h(r_h\cdot Je)=0
$$

for each support type. It supplies no bundlewise equality of positive and negative
KKT mass, no exact axial reaction formula, and no exact-phase cotangent-ratio law.

Those statements require additional hypotheses and are not imported here.

Strong connectivity is also essential. For $m=2$, take positive types

$$
(0,2),(1,2)
$$

and negative types

$$
(0,2),(0,1).
$$

Both sign families are maximal nested chains containing full support, but they differ;
the resulting directed graph is not strongly connected. Thus nesting alone does not
force (4.2).

As an independent finite sanity check, exhaustive enumeration of abstract nested-chain
pairs through $m=6$ found no counterexample: the strongly connected cases were
exactly the $2^{m-1}$ common maximal staircases. This enumeration is computational
evidence only and is not used in the proof above.

## 7. Target-C frontier effect

Compose this theorem with the preceding open-cell sign-nesting/isolated-release
candidate and the current-main cut-divergence theorem. The nonconstant open-witness-cell
route is reduced to exactly the following fork:

1. an inverse-$D$ inactive near-unit or near-diameter source pair; or
2. a strongly connected gap graph whose support is one common bidirected maximal
   staircase tree, with at least $2m$ physical diameter rows and at least
   $m(m+1)$ diameter/train-cut incidences.

This does not close C-II. The next structural target is now specific: couple this
all-scales paired staircase to the retained opposite complete O--O shore and its
four-host order. A useful successor theorem would either force a transverse
full-support packet large enough to violate the Target-C source/diameter currency,
or convert the paired staircase plus its physical forest lift into a finite
source-preserving strict-diameter move. The inactive-pair branch separately needs
a source-level release or a bounded charging theorem.

Disposition: proof-only Target C candidate. C-II and Level I remain open.
