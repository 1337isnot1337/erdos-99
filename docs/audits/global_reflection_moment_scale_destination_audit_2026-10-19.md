<!-- theorem-state: {"artifact_id":"ART-1FB8B367623B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
<!-- theorem-state: {"artifact_id":"ART-1FB8B367623B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Exact destination audit: reflected-scale moment obstruction

**Candidate:** `GLOBAL-REFLECTION-MOMENT-SCALE-OBSTRUCTION-PR959`  
**Destination commit reviewed:** `7d0a450fe66991036541023f95c44c064a04b6a8`  
**Theorem state / priority / catalogue:** `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`  
**Lifecycle:** destination candidate remains `unreviewed`; this audit makes no promotion.  
**Scope:** the exact asymptotic reflected-scale claim, its canonical Oler and isodiametric inputs, and the pinned finite controls.

## Review outcome

I reconstructed the empirical-disk and moment argument before reading the
historical source audit. I find the stated scale conclusion valid under the
listed hypotheses. The only compressed step is the conversion of fixed-region
Oler bounds into domination of a weak-limit measure; the finite-partition
argument below fills it. I found no missing global-minimality hypothesis in
this claim because it is a theorem about every sequence at the stated leading
density, including nonglobal sources.

The conclusion is exactly (A_j,B_j\to1) for a feasible, retained-label
reflected endpoint of diameter at most ((1+o(1))D_j), when the unit-separated
source has (D_j\to\infty) and (n_j/D_j^2\to\pi/(2\sqrt3)). Lines, offsets,
and label signs may vary arbitrarily. The endpoint must be an actual planar
placement of all labels and satisfy every lower pair constraint. The proof
uses its diameter bound, not a separate upper bound for each pair.

This excludes fixed macroscopic anisotropic scales along this one-step route.
It proves no convergence rate, source-derived endpoint, strict lower-order
diameter improvement, nonattainment, or triangle conclusion. It supplies no
canonical claim and leaves Level I, A, B, and C-II open; C-I remains closed.

## Source and lifecycle checks

The destination bytes were checked against the assignment pins:

| Artifact | Destination SHA-256 | Role |
| --- | --- | --- |
| `docs/reports/global_reflection_moment_obstruction_2026-10-12.md` | `4e3e129da1129a659fae627fb7467beb557ca2f5ef4b45563e1666f84d0c7454` | Full analytic argument |
| `research/verify_global_reflected_scale_2026_10_12.py` | `caef9c87b7773aa1089ec845d30b35fb09bd70bde5f0264a128b51fc7f531403` | Exact finite controls |
| `docs/audits/pr959_autonomous_proof_audit_2026-10-15.md` | `30ce4ddc5721a402f0b98080c48d7c0ae5cecbf4b0e27393300983ec60ad34f1` | Historical source-audit provenance |

The report is a transformed destination copy of the source artifact; its
destination hash above, not the historical source hash, is the reviewed text.
The prior audit identifies itself as an audit of source PR #959 at
`e25041f236d268a7e815dacd346180989690ed71` and explicitly says it is not the
destination exact-head audit. The candidate registry still lists this claim
as `unreviewed`. The task catalogue has no prior checks for the assigned card.
I read the candidate report and canonical dependency first, completed the
reconstruction below, and only then used that historical audit as a comparison.

The only canonical repository-theorem dependency is Oler Lemma 21.1 in
[`03-oler-shell.md`](../theory/03-oler-shell.md#211-the-finite-oler-inequality-and-an-improved-universal-diameter-bound).
The equality input is the planar isodiametric theorem: a bounded set attains
area \(\pi d^2/4\) at diameter \(d\) only when it is a disk up to a null set.
For a convex body this gives the actual disk. See Maggi, Ponsiglione, and
Pratelli, [*Quantitative stability in the isodiametric inequality via the
isoperimetric inequality*](https://cvgmt.sns.it/media/doc/paper/898/IsodiametricMPP.pdf),
Introduction, (1.1), and the equality discussion following (1.9). No rate from
the paper is used.

## Independent proof reconstruction

Put \(a_0=\sqrt3/2\), so the Oler bound is
\(N\le |K|/a_0+\operatorname{per}(K)/2+1\), and put
\(\eta_0=\pi/(4a_0)=\pi/(2\sqrt3)\). Center each source by its point
centroid and divide coordinates by \(D_j\). Its hull has diameter at most one.
Cauchy's perimeter bound gives \(\operatorname{per}(K_j)\le\pi D_j\), so
Oler implies

\[
 |K_j|\ge a_0(n_j-\pi D_j/2-1)
       = (\pi/4-o(1))D_j^2.
\]

The isodiametric upper bound is \(|K_j|\le\pi D_j^2/4\). Thus normalized hull
areas tend to \(\pi/4\). Their centroids lie in the hulls, and their diameters
are bounded, so the normalized hulls lie in a fixed compact ball. Every
Hausdorff limit is a convex body of area \(\pi/4\) and diameter at most one;
isodiametric equality makes it a radius-\(1/2\) disk.

For completeness, the local Oler statement does imply the asserted empirical
measure limit. Let
\(\nu_j=D_j^{-2}\sum_i\delta_{p_{ij}/D_j}\), whose mass tends to \(\eta_0\).
For a fixed rectangle \(R\), apply Oler to the labels in \(R\) and enclose
their hull in \(R\cap K_j\). After dividing by \(D_j^2\), the perimeter and
constant terms are \(O(D_j^{-1})\) and \(O(D_j^{-2})\). For a finite
rectangular partition and a nonnegative continuous test function, bound each
cell's contribution by its supremum times this Oler count. First let \(j\to\infty\),
then refine the partition. The cell boundary has zero area in the disk, and
this yields \(\int f\,d\nu\le a_0^{-1}\int_{B_{1/2}}f\,dx\) for every weak
limit \(\nu\) and every such \(f\). Hence \(\nu\le a_0^{-1}\,dx\) on its
limiting disk. Its mass is \(\eta_0=|B_{1/2}|/a_0\), so equality holds and
normalizing by the point count gives the uniform probability measure on the
disk. The point centroid is zero, so the disk center is zero. Compact support
gives convergence of all moments. This argument applies unchanged to an
endpoint: it has the same count and separation and normalized diameter at most
\(1+o(1)\), and all labels, including contact isolates, enter the measure.

Write \(X,Y\) for source coordinates in the varying normal/tangent frame after
normalization. Disk isotropy gives
\[
 s=\mathbb E X^2=\mathbb E Y^2=1/16,\qquad
 t=\mathbb E X^2Y^2=1/384,\qquad \mathbb E XY^2=0.
\]
The endpoint tangent coordinate is \(\sqrt{B_j}Y\), with mean zero. Source
and endpoint disk limits therefore give \(B_j\mathbb E Y^2\to s\) and
\(\mathbb E Y^2\to s\), hence \(B_j\to1\).

Let \(\gamma_j=c_j/D_j\), \(m_j=\mathbb E q_x\), and
\(V_j=\operatorname{Var}(q_x)\). The centered endpoint disk limit gives
\(V_j\to s\). For any signs,
\[
 V_j=A_j\bigl(\mathbb E|X-\gamma_j|^2-
              (\mathbb E[\sigma|X-\gamma_j|])^2\bigr)
 \ge A_j\operatorname{Var}(|X-\gamma_j|).
\]

If \(\gamma_j\) stays bounded, the last variance has a positive uniform lower
bound: the disk's normal marginal is not concentrated on a level set of
\(|X-\gamma|\), and this variance is continuous in \(\gamma\). Thus \(A_j\)
is bounded above. It is bounded away from zero, since \(|X|\le1\) and bounded
\(\gamma_j\) would otherwise force the entire centered endpoint normal
coordinate to have vanishing range, contradicting \(V_j\to s>0\). The means
\(m_j\) are bounded as well.

Along any convergent subsequence write \(A_j\to A>0\),
\(\gamma_j\to\gamma\), and \(m_j\to m\). The endpoint second normal moment
and centered mixed fourth moment converge to \(s\) and \(t\). Using source
centering, \(B_j\to1\), and \(\mathbb E XY^2\to0\), they give
\[
 A(s+\gamma^2)=s+m^2,\qquad
 A(t+\gamma^2s)=t+m^2s.
\]
In the second identity the cross term is controlled by the endpoint disk law:
\(\mathbb E[(q_x-m_j)q_y^2]\to0\) and
\(\mathbb E q_y^2\to s\), so \(\mathbb E[q_xq_y^2]\to ms\). Eliminating
\(m^2\) yields
\[
 (A-1)(t-s^2)=0,\qquad t-s^2=-1/768,
\]
and therefore \(A=1\). Every bounded-offset subsequential limit has this
scale.

If \(|\gamma_j|\to\infty\), the line is eventually outside the source hull.
Then \(|X-\gamma_j|\) is affine in \(X\), and
\(\operatorname{Var}(|X-\gamma_j|)=\mathbb E X^2\to s\), so the same variance
bound makes \(A_j\) bounded above. If a subsequence had \(A_j\to0\), each
sign class of centered endpoint normal coordinates would lie in an interval of
length at most \(\sqrt{A_j}\) times the source's normalized normal span.
The endpoint coordinates are bounded by their diameter, so any subsequential
limit would be supported on at most two points. This contradicts the continuous
normal marginal of the uniform disk, proving \(\liminf A_j>0\). If both signs
occur, opposite sign groups have normal separation at least
\(2\sqrt{A_j}(|\gamma_j|-1)\), which diverges and violates the endpoint
diameter bound. All signs therefore agree for sufficiently large \(j\). The
normal map is then affine on every label, so centering gives
\(V_j=A_j\mathbb E X^2\to A_js\); hence \(A_j\to1\).

For arbitrary offsets, any subsequence has a further subsequence with bounded
\(\gamma_j\), or one with \(|\gamma_j|\to\infty\). The two cases force
\(A_j\to1\), proving the full-sequence conclusion. The bounded-offset
equations only give \(m^2=\gamma^2\) after \(A=1\); they do not force the
offset or endpoint centroid to vanish, and no such conclusion is needed.

For application to global minimizers, the leading density follows from the
same constants. A triangular lattice of covolume \(a_0\) has average \(n\)
sites in a translate of the disk of radius \(\sqrt{a_0n/\pi}\); some translate
therefore contains at least \(n\) sites, so \(D(n)\le2\sqrt{a_0n/\pi}\).
Oler on a minimizing hull, with perimeter at most \(\pi D(n)\), gives
\[
 \frac{n}{D(n)^2}\le \frac{\pi}{4a_0}+\frac{\pi}{2D(n)}+\frac{1}{D(n)^2},
 \qquad
 \frac{n}{D(n)^2}\ge \frac{\pi}{4a_0}.
\]
Thus every unbounded sequence of global minima has
\(n/D(n)^2\to\pi/(4a_0)=\eta_0\). No lattice scaffold is identified with a
source; the lattice is used only as an independent diameter competitor for
this leading-density squeeze.

## Exact finite identity and controls

For a centered finite source define \(S_x=\mathbb E X^2\),
\(S_y=\mathbb E Y^2\), \(T=\mathbb E X^2Y^2\), and
\(U=\mathbb E XY^2\). Put \(z=\sigma|X-c|\),
\(m=\mathbb E q_x\), \(V_x=\mathbb E(q_x-m)^2\),
\(V_y=\mathbb E q_y^2\), \(W=\mathbb E(q_x-m)^2q_y^2\), and
\(L=\mathbb E(q_x-m)q_y^2\). Expanding the centered moments of
\(q_x=\sqrt A z\), \(q_y=\sqrt B Y\) gives
\[
 W+2mL-V_xV_y=AB\operatorname{Cov}(z^2,Y^2)
 =AB(T-S_xS_y-2cU).
\]
The last equality uses \(z^2=(X-c)^2\) and \(\mathbb E X=0\). Signs vanish
from this identity because they disappear in \(z^2\); the offset/odd-moment
term remains and cannot be discarded at finite size.

I ran the pinned exact verifier under the shared host compute lock:

```sh
flock -x /home/cinna/.local/state/erdos99-host-compute.lock -c \
  'python3 research/verify_global_reflected_scale_2026_10_12.py'
```

It passed 400 signed-parity cases against exhaustive assignments (97 feasible,
89 lower-pair, 124 upper-pair, 90 parity-inconsistent; 54 parallel-forcing
cases), and rejected incomplete/invalid sign lists. It checked all 12,246
pairs of the 157-label fixture, retained its two contact isolates, and verified
the exact endpoint range \([405441/403202,865065744/1008005]\) against old
squared diameter 916. It also checked the finite moment identity on that
fixture and an asymmetric nonzero-offset/odd-moment fixture. The \(M=40,K=1\)
and \(M=60,K=2\) family fixtures checked 29,403 and 182,710 pairs. These are
exact finite controls only; they do not verify the weak-limit proof, endpoint
existence for global minimizers, or Level I.

## Destination disposition and remaining bridge

The historical source audit is useful provenance and agrees with this
reconstruction, but it is not the independent destination audit. This report
is bound to the exact destination bytes and leaves the candidate's registry
status unchanged at `unreviewed`. No result here promotes a theorem or modifies
canonical state.

The remaining reflected-route obligation is source-specific: for every
sufficiently large triangle-free global diameter minimizer, derive parameters
with \(A,B\to1\) and a sign assignment that retains every label, satisfies all
lower pair constraints, and gives a strict whole-source diameter improvement;
or supply another full-source planar construction. Contact isolates and every
pair remain in the endpoint ledger. This audit finds no such extraction or
lower-order gain.

Prepared by Codex (GPT-6 Luna, xhigh) as an independent AI-agent mathematical
audit. No human mathematical referee is claimed. The linked paper is cited, not
copied; this first-party audit is contributed under Apache-2.0.
