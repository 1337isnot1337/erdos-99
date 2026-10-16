# Target C — exact surplus–moment identity and scalar feasibility audit

**Date:** 2026-09-12  
**Status:** proof-only structural note; C-II remains open  
**Dependencies:** canonical Sections 62 and 75, plus the proof-only Type-II loaded-contact localization and Sections 160–163.

This note records an exact cancellation that is useful when the aggregate harmonic-cell
diameter moment is kept instead of discarded. It also checks the resulting scalar
system against an explicit normalized witness. The cancellation is real, but the
currently available scalar inequalities remain feasible; this route does not close C-II.

## 1. Exact finite identity

Use the Type-II notation

- `q` for the loaded force-hull vertex count;
- `m` for the number of nonunit force-hull sides;
- `k=d_H+s_Z`;
- `c_I` for the number of unloaded positive-contact components;
- `s_C` for their total pinned surplus;
- `S_D=sum_r d_r` for the harmonic-cell diameter moment; and
- `G_D=2+q+m-k-S_D` for the exact component remainder of Section 160.

The proof-only Type-II loaded-contact theorem gives

\[
e_{BB}=q-m,
\tag{1.1}
\]

and the canonical pinned ledger gives

\[
c_I+e_{BB}+s_C=q-2+k.
\tag{1.2}
\]

Therefore

\[
s_C=m+k-2-c_I.
\tag{1.3}
\]

Define the all-phase surplus numerator

\[
\mathcal M_D:=e_{BB}+2s_C-3k.
\tag{1.4}
\]

Substituting (1.1) and (1.3) gives

\[
\mathcal M_D=q+m-k-2c_I-4.
\tag{1.5}
\]

The definition of `G_D` then yields the exact finite identity

\[
\boxed{
S_D+G_D=\mathcal M_D+2c_I+6.
}
\tag{1.6}
\]

Thus the harmonic diameter moment plus the component remainder is not an independent
currency. Up to the explicit component-count constant, it is exactly the canonical
all-phase surplus.

## 2. Corollaries in the live normalized variables

Put

\[
t_D:={q-k\over D},\qquad
\kappa_D:={k\over D},\qquad
s_D:={S_D\over D},\qquad
g_D:={G_D\over D},\qquad
\mu_D:={\mathcal M_D\over D}.
\]

Canonical Section 75 gives `c_I=O(D^{2/3})`, so (1.6) becomes

\[
s_D+g_D=\mu_D+o(1).
\tag{2.1}
\]

The same substitution gives the exact finite relation

\[
Q+u_B=e_{BB}-2k
       =2(q-k)-\mathcal M_D-k-2c_I-4,
\tag{2.2}
\]

and hence

\[
\boxed{
{Q+u_B\over D}=2t_D-\mu_D-\kappa_D-o(1).
}
\tag{2.3}
\]

Here `Q` is the bounded-face degree excess and `u_B` is the outer-walk surplus. This
relation keeps the §123 loaded-boundary payment and the §163 return currency in the
same variables.

The retained-remainder inequality of §161 is

\[
5q-7k\ge3S_D+2G_D+c_*D-o(D),
\qquad
c_*={\pi\over4}(2-\sqrt3).
\tag{2.4}
\]

Using (1.6), (2.4) is equivalently

\[
\boxed{
5t_D-2\kappa_D
\ge s_D+2\mu_D+c_*-o(1).
}
\tag{2.5}
\]

The §163 cellwise return inequality becomes

\[
\boxed{
5t_D-2\mu_D-2\kappa_D
\ge2\sqrt{\Delta_2}-o(1),
\qquad
\Delta_2={\pi\over2\sqrt3}.
}
\tag{2.6}
\]

Equations (2.3), (2.5), and (2.6) are cleaner than the unreduced five-currency
system. They still contain no source-preserving diameter-decrease theorem.

## 3. Explicit scalar-feasibility witness

The following normalized values are an algebraic witness for the currently retained
scalar constraints. They are **not** claimed to come from a geometric source.

\[
\begin{array}{c|c}
\text{currency} & \text{normalized value}\\ \hline
t=(q-k)/D & 1.8210\\
\kappa=k/D & 0\\
q/D=t+\kappa & 1.8210\\
S_D/D=s & 2.7986\\
G_D/D=g & 0.2394\\
\mathcal M_D/D=s+g & 3.0380\\
m/D=\mathcal M_D/D-t & 1.2170\\
e_{BB}/D=q/D-m/D & 0.6040\\
u_B/D & 0.1040\\
Q/D=e_{BB}/D-u_B/D & 0.5000\\
f/D & 0.5000
\end{array}
\]

The relevant checks, with `c_det=\frac\pi2(2-\sqrt3)=0.420893...` and
`2\sqrt{\Delta_2}=1.904625...`, are:

\[
\begin{aligned}
5t&=9.1050
  >s+2\mu+c_*=9.0850,\\
5t-2\mu&=3.0290>1.904625,\\
Q+u_B&=0.6040=e_{BB}-2\kappa,\\
u_B+(\mu+\kappa-\pi)&\approx4.1\times10^{-4}\ge0,\\
2(q-s)+2(e_{BB}-k)+4f&\approx1.2528>c_{\rm det},\\
4f+Q&=2.500\ <10(e_{BB}-k)=6.040.
\end{aligned}
\]

The displayed decimals are rounded; no exact finite object is being asserted. The point
is that the signs and the available margins survive at normalized scale.

The witness also satisfies the current §146/§171 lower floors
`t>=1.819513...` and `t>=1.820883...`, since `t=1.8210`. It therefore blocks a purely
scalar claim that the surplus–moment identity alone contradicts the live Type-II floors.

## 4. What remains to close C-II

The identity removes one apparent degree of freedom but leaves the same geometric
escape already identified by the current route:

```text
harmonic diameter moment + component remainder
    -> exact all-phase surplus
    -> either loaded-boundary defect or outer-walk surplus.
```

A closing theorem still needs one of the following:

1. an upper bound on the same aggregate outer detour that retains `S_D` and `G_D`;
2. a geometric lower bound on `G_D` strong enough to violate (2.5) together with the
   actual Type-II `t` envelope; or
3. a source-preserving finite motion turning the forced detour into a strict diameter
   decrease.

No theorem-state file is changed. Contact-isolated points remain outside all core
rigidity statements, and the Type-I inactive-container branch is untouched.

**Disposition:** exact proof-only invariant plus scalar regression; C-II remains open.
