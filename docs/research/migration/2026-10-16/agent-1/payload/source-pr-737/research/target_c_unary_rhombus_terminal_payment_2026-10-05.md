# Target C-II: terminal payment for outer Horn owners and unary rhombi

Date: 2026-10-05.
Authority: main 583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1, state 2026-10-05.audit.62.
Status: proof-only Target C reduction. C-II and Level I remain open.

Work in the audit.61 acute binary O--O system after upper exceptions, active-diameter requirements, and bounded-face isolate reassignment. As in the actual disjoint-swap O--O specialization, every moving owner that contains a core vertex is a proper selected-cut region/slab, not the global rigid translation. Put
\[
X=b-q+Z_{\rm out},
\]
and let \(T_{\rm OO}\) be the number of selected global stopped O--O trains.

## 1. Sharper outer owner payment

There are at most \(b-q\) distinct unloaded nonisolated source vertices incident with the outer face. Including outer contact isolates,
\[
|U_{\rm out}|\le X. \tag{1}
\]

Let \(A\) be distinct moving owners. For each \(i\in A\), choose either an outgoing outer implication \(i\to j\) or an outer unary-zero witness. Let \(p_i\) be the endpoint of that witness owned by \(i\). Distinct owners give distinct \(p_i\).

If \(p_i\) is unloaded, charge it injectively to (1). If \(p_i\) is loaded, it is a core vertex. By the proper region/slab hypothesis, owner \(i\) has nonempty outer complement, and \(p_i\) gives \(r_i\ge1\) loaded-hull run. The existing terminal-run theorem gives
\[
\sum r_i\le T_{\rm OO}.
\]
Therefore
\[
\boxed{|A|\le T_{\rm OO}+X.} \tag{2}
\]
This replaces the earlier \(T_{\rm OO}+6X\) owner bound. The degree-six estimate remains useful for counting witness edges, but not owner tails.

Let \(R_{\rm rh}\) be owners having a unary-zero clause from a bounded strict-rhombus diagonal. If all-zero is the only lower-feasible assignment, every owner outside \(R_{\rm rh}\) either has an outer unary-zero witness or an outgoing implication. Otherwise its singleton assignment would satisfy all implications and incompatibilities. Hence
\[
\boxed{k-|R_{\rm rh}|\le T_{\rm OO}+X.} \tag{3}
\]

## 2. Unary rhombus roots inject into selected trains in the narrow-shore case

Assume additionally the actual one-shore system: selected train directions lie in a projective interval of width \(<\pi/3\), and owner labels are constant on complementary selected-cut regions.

Two selected trains cannot cross: a strict unit rhombus crossing requires projective side-direction separation \(>\pi/3\). Thus the selected O--O crosscuts are pairwise disjoint.

For \(i\in R_{\rm rh}\), audit.61 gives the rhombus ownership pattern: two adjacent vertices have owner \(i\), and the other two are fixed. The two moving/fixed contact edges are opposite sides of the rhombus, so they belong to one stopped train \(\tau\). Since their selected-cut owner labels differ, \(\tau\) is selected.

Because selected crosscuts are disjoint, \(\tau\) separates the same two complementary regions along its whole track. If one side is fixed, the other side has one owner label. Hence one selected train cannot support unary rhombus roots for two distinct owners. Choosing one blocker per root owner gives
\[
\boxed{|R_{\rm rh}|\le T_{\rm OO}.} \tag{4}
\]

The noncrossing hypothesis is essential to this proof; no such injection is asserted for arbitrary crossing-cut multishears.

Combining (3) and (4),
\[
\boxed{k\le2T_{\rm OO}+X.} \tag{5}
\]

Each selected O--O train contributes two outer terminal occurrences, counting the two facial occurrences of a singleton bridge separately. Stopped trains partition contact edges, so
\[
2T_{\rm OO}\le b. \tag{6}
\]
Thus
\[
\boxed{k\le b+X=2b-q+Z_{\rm out}.} \tag{7}
\]

If \(R_{\rm rh}=\varnothing\),
\[
\boxed{k\le T_{\rm OO}+X\le b/2+X.} \tag{8}
\]

## 3. Existing basin bounds sharpen

The same endpoint charge gives
\[
|B(S)|\le T_{\rm OO}+X
\]
for every nontrivial sink SCC and its complete incoming implication basin. A simple implication path has at most \(T_{\rm OO}+X+1\) owners and a two-path incompatibility fork at most \(T_{\rm OO}+X+2\).

If \(t_L\) counts loaded-only sink SCCs from the double-recurrence note, the same tail-endpoint split yields
\[
\boxed{k_{\rm bin}+2t_L\le T_{\rm OO}+X.} \tag{9}
\]

## 4. Remaining Target C bottleneck

The explicit unary-rhombus term is now paid by the selected train bank in the narrow-shore owner system rather than left unpriced. The full lower owner obstruction costs at most
\[
2T_{\rm OO}+b-q+Z_{\rm out}.
\]

The next strengthening is to show that the train bank used by loaded implication/outer-unary owners and the train bank used by rhombus roots cannot both saturate independently, or to charge rhombus-root trains into the audit.53 return/depletion ledger. The outer-isolate term \(Z_{\rm out}\) can also remain linear.

Upper exceptions, active-diameter extraction, and the macroscopic inactive-container branch remain separate. No C-II or Level I closure is claimed.

All statements here are analytic finite proofs. No computation or verifier output is a proof premise.
