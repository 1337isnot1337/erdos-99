<!-- theorem-state: {"artifact_id":"ART-1A139A2F811F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - additive exclusion of the zero-transfer C-II branch

**Date:** 2026-09-11  
**Target:** Target C, C-II  
**Status:** STILL OPEN; hold report  
**Dependencies:** promoted C53/C63 C-II normalization, C26/C34/C35, the circular-planar resistance split representation, and SEPq  
**Purpose:** close the \(\min_{e\ne f}K_{ef}=0\) transfer branch without assuming \(s_Z=0\), a forest diameter graph, or absence of contact-isolated source points

## 1. Statement

Let \(A\) be the contact-minimal, then diameter-pair-minimal, triangle-free global
minimizer used in C-II, with \(C=C_*\) and \(H=H_*\). Let \(B\) be the loaded
diameter endpoints of a relative-interior normalized KKT stress, let \(q=|B|\), and
let

\[
K=Q^{\mathsf T}\Lambda^+Q
\]

be the C53 transfer kernel for all actual diameter edges. Assume \(D\ge9\). Then

\[
\boxed{\min_{e\ne f}K_{ef}=0\text{ is impossible}.}
\tag{ZA.1}
\]

Thus the only remaining C53 transfer alternative is

\[
\boxed{\min_{e\ne f}K_{ef}<0.}
\tag{ZA.2}
\]

This conclusion retains all contact-isolated source points: they are not inserted
into the response network, and no claim is made about their location.

## 2. Zero minimum makes every transfer diagonal

Use the legal C53 projective orientation and order the actual diameter edges by
their chord directions. Write

\[
u_e=a_e(1,t_e),\qquad a_e>0,
\]

with distinct strictly increasing slopes \(t_e\). Put

\[
\gamma_e=a_e\beta_e>0,
\qquad
M=\Gamma(\Beta^{-1}-K)\Gamma.
\]

C53 gives

\[
M\succeq0,\qquad M\mathbf1=0,\qquad Mt=0,
\tag{ZA.3}
\]

and, for \(e\ne f\),

\[
M_{ef}=-\gamma_e\gamma_fK_{ef}.
\tag{ZA.4}
\]

If \(\min_{e\ne f}K_{ef}=0\), then all off-diagonal \(K_{ef}\ge0\), hence all
off-diagonal \(M_{ef}\le0\). With \(M\mathbf1=0\), \(M\) is the Laplacian of the
complete graph with nonnegative edge weights

\[
w_{ef}=\gamma_e\gamma_fK_{ef}.
\]

Therefore

\[
0=t^{\mathsf T}Mt
 =\sum_{e<f}w_{ef}(t_e-t_f)^2.
\]

The slopes are distinct, so every \(w_{ef}=0\), and hence

\[
\boxed{K=\Beta^{-1}.}
\tag{ZA.5}
\]

The point of the next step is that (ZA.5) is much stronger than componentwise
star additivity.

## 3. A diagonal transfer kernel forces additive resistance on all terminals

Let \(W_{ij}\) be the effective resistance between loaded terminals \(i,j\in B\).
The circular-planar resistance split representation gives

\[
W=\sum_A\lambda_A\delta_A,
\qquad \lambda_A\ge0,
\tag{ZA.6}
\]

where \(A\) ranges over circular interval splits and \(\delta_A\) is one on pairs
separated by the split and zero on pairs on the same side. For the signed split
vector \(z_A=Q^{\mathsf T}\mathbf1_A\), centering yields

\[
K=\sum_A\lambda_A z_Az_A^{\mathsf T}.
\tag{ZA.7}
\]

The C53 interval-sign lemma says, for three projectively ordered diameter edges
\(e<f<g\),

\[
z_g(z_e-z_f)\le0,
\qquad
z_e(z_g-z_f)\le0.
\tag{ZA.8}
\]

Since \(K\) is diagonal, compare \(K_{ri}\) and \(K_{r,i+1}\). For \(r<i\),
(ZA.8) makes every term in

\[
0=K_{ri}-K_{r,i+1}
 =\sum_A\lambda_Az_r(z_i-z_{i+1})
\tag{ZA.9}
\]

nonnegative. For \(r>i+1\), the analogous comparison makes every term
nonpositive. Thus, for every split with \(\lambda_A>0\),

\[
z_i\ne z_{i+1}\quad\Longrightarrow\quad
\operatorname{supp}z_A\subseteq\{i,i+1\}.
\tag{ZA.10}
\]

Apply (ZA.10) at every gap. A split vector with support on two coordinates is
impossible when there are at least three diameter edges: at a neighboring gap one
of those two coordinates is compared with a zero coordinate, and (ZA.10) would
force the support into a different two-coordinate set. A nonzero constant split
vector is also impossible, because its contribution to the off-diagonal entry
\(K_{0,m-1}\) in (ZA.7) is strictly positive. Therefore every positive split has
either zero support or singleton support.

The zero-support case cannot occur. If \(z_A=0\), no diameter edge crosses the
split. Every terminal is incident with a diameter edge, so each shore contains a
whole diameter edge. Those two diameter chords lie in disjoint cyclic intervals;
they neither share an endpoint nor cross, contradicting the diameter-thrackle
property.

If \(z_A\) has singleton support, exactly one diameter edge crosses the split. The
two shores cannot both contain an internal diameter edge, for those two edges again
lie in disjoint cyclic intervals and do not cross. Hence one shore has no internal
diameter edge. Every terminal on that shore must be incident with the unique crossing
edge, so that shore consists of one terminal. Thus every positive split in (ZA.6)
is a singleton-terminal split.

Summing singleton splits gives numbers \(r_i\ge0\) such that

\[
\boxed{W_{ij}=r_i+r_j\qquad(i\ne j).}
\tag{ZA.11}
\]

This is the complete terminal additive-response conclusion. It is not a statement
about an independently selected star scaffold.

## 4. Additive response contradicts C-II degree caps

C34 gives the loaded endpoint count

\[
2q\ge\lceil D\rceil+2.
\tag{ZA.12}
\]

For \(D\ge9\), \(q\ge6\). The actual diameter graph has no isolated loaded terminal,
so it has at least three edges and the preceding split argument applies.

The positive contact network used to define \(\Lambda\) is connected and
circular-planar, with all \(q\) loaded terminals on its boundary. SEPq applies to
(ZA.11): there is a contact vertex \(z\) such that every component of the contact
network after deleting \(z\) contains at most one loaded terminal. Therefore

\[
\deg_C(z)\ge
\begin{cases}
q,&z\notin B,\\
q-1,&z\in B.
\end{cases}
\tag{ZA.13}
\]

C26/C35 give

\[
\deg_C(z)\le5\quad(z\notin B),
\qquad
\deg_C(z)\le3\quad(z\in B).
\tag{ZA.14}
\]

For \(q\ge6\), (ZA.13) and (ZA.14) are incompatible: an unloaded separator would
need degree at least six, while a loaded separator would need degree at least five.
This proves (ZA.1).

## 5. Branch coverage

The proof uses neither \(s_Z=0\) nor a forest classification of \(H\). Therefore it
removes the zero-transfer subcase from all three requested ledger branches:

* cyclic diameter topology with \(s_Z=0\);
* forest diameter topology with \(s_Z=0\);
* \(s_Z>0\).

It also does not assume that every source point lies in the positive contact core.
The remaining branches still include the negative-transfer alternative (ZA.2), the
non-additive high-surplus response regimes, and the contact-isolated population.

## 6. Audit of the exact failed implication

The valid chain is

\[
\min K_{ef}=0
\Rightarrow K=\Beta^{-1}
\Rightarrow W\text{ additive on all loaded terminals}
\Rightarrow \text{SEPq separator}
\Rightarrow \text{degree-cap contradiction}.
\]

The invalid shorter chain would have been

\[
K=\Beta^{-1}\Rightarrow\text{one geometric star center in the source graph}.
\]

No such geometric identification is used. SEPq supplies a separator in the actual
positive contact network and retains all of its topology.

This branch theorem is therefore stronger than the componentwise zero-transfer star
reduction, but it does not close C-II. The surviving negative-transfer branch is not
covered by the additive split argument.
