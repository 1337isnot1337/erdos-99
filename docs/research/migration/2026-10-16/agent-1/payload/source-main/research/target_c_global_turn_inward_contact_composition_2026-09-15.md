# Target C-II — global-turn tooth penetration sharpens the inward-contact endpoint

**Date:** 2026-09-15  
**Status:** proof-only structural composition; theorem-state authority unchanged  
**Scope:** canonical full-core Type-II branch; numerical endpoint uses audited minimax atomic gap `g=0.0021`  
**LEVEL I STATUS:** `STILL OPEN`

Two current source-level theorems fit together without any additional geometric
hypothesis:

1. the exact boundary-unit conversion
   \[
   N_2+2s_B+2|E_{bis}|\ge3q-b,
   \]
   where `N_2` counts genuine two-edge outer teeth, `s_B` is loaded contact-degree
   slack, and `E_bis` is a distinct family of strongly inward loaded-to-unloaded unit
   contacts;
2. the global-turn shallow-tooth theorem, which for every
   \[
   \eta\quad\text{with}\quad
   \alpha_\eta:=\arccos(1-\eta/2)<\pi/6
   \]
   gives
   \[
   E_{pen}(\eta)
   \ge {1\over2}\left(N_2-{d_{out}\over\eta}-2\right).
   \]

The second theorem has two improvements over the earlier penetration estimate: the
factor is `1/2` instead of `1/4`, and the admissible shallow threshold extends almost
to `2-sqrt(3)`.

Combining the two eliminates `N_2` and yields

\[
\boxed{
2|E_{pen}(\eta)|+2s_B+2|E_{bis}|
\ge3q-b-{d_{out}\over\eta}-O(1).
}
\tag{GI.1}

Let

\[
E_{str}(\eta):=E_{pen}(\eta)\cup E_{bis}.
\]

Since

\[
|E_{pen}|+|E_{bis}|\le2|E_{str}|,
\]

we obtain the two-currency physical burden

\[
\boxed{
4|E_{str}(\eta)|+2s_B
\ge3q-b-{d_{out}\over\eta}-O(1).
}
\tag{GI.2}

At the audited `g=0.0021` low-`t` floor, the exact threshold

\[
\eta={4\over15}
\]

gives

\[
\boxed{
\max\{s_B,|E_{str}(4/15)|\}
\ge(0.3847753715\ldots-o(1))D.
}
\tag{GI.3}

Every edge in `E_str(4/15)` is an actual unit contact with a uniform inward projection:

- the global-turn tooth contacts have inward component at least
  \[
  Y_{4/15}
  ={13\sqrt3-2\sqrt{14}\over30}
  =0.5011115241\ldots;
  \]
- the bisector contacts have inward component greater than `sqrt(3)/2` relative to
  their loaded hull-angle bisectors.

Thus the current low-`t` endpoint must carry either almost `0.385D` units of loaded
degree deficit or almost `0.385D` distinct genuinely inward unit contacts.

## 1. Finite composition

The loaded-unit inward-bisector theorem gives the finite identity

\[
N_2+2s_B+2|E_{bis}|\ge3q-b.
\tag{GI.4}
\]

The global-turn shallow-tooth theorem gives, whenever `alpha_eta<pi/6`,

\[
|E_{pen}(\eta)|
\ge {1\over2}
\left(N_2-{d_{out}\over\eta}-2\right).
\tag{GI.5}

Rearrange:

\[
N_2
\le2|E_{pen}(\eta)|+{d_{out}\over\eta}+2.
\tag{GI.6}
\]

Insert this upper bound for the same positive currency `N_2` into (GI.4):

\[
2|E_{pen}(\eta)|+{d_{out}\over\eta}+2
+2s_B+2|E_{bis}|
\ge3q-b.
\]

Therefore

\[
\boxed{
2|E_{pen}(\eta)|+2s_B+2|E_{bis}|
\ge3q-b-{d_{out}\over\eta}-2.
}
\tag{GI.7}

This proves (GI.1) with the explicit finite additive constant `2`.

Now

\[
|E_{pen}|+|E_{bis}|\le2|E_{str}|,
\]

so

\[
2|E_{pen}|+2|E_{bis}|\le4|E_{str}|.
\]

Replacing the contact sum in (GI.7) by this upper bound proves

\[
\boxed{
4|E_{str}(\eta)|+2s_B
\ge3q-b-{d_{out}\over\eta}-2.
}
\tag{GI.8}

No KKT multiplier floor or small-residual hypothesis is used.

## 2. Low-`t` normalization

Write

\[
t={q-k\over D},\qquad
\kappa={k\over D},\qquad
\delta={d_{out}\over D}={b-P_F\over D}.
\]

At the audited `g=0.0021` checkpoint, put

\[
C_0=2\sqrt{\Delta_2}+0.0021,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\]

The current §171 squeeze is

\[
2\delta+{\kappa\over2}\le
R(t):={9t\over2}-2\pi-C_0.
\tag{GI.9}

The exact boundary quantity satisfies

\[
{3q-b\over D}
=3t+3\kappa-\pi-\delta+o(1).
\]

At fixed `t`, this is minimized subject to (GI.9) at

\[
\kappa=0,
\qquad
\delta={R(t)\over2},
\]

so

\[
\boxed{
\liminf {3q-b\over D}
\ge
B(t):={3t\over4}+{C_0\over2}.
}
\tag{GI.10}

Divide (GI.8) by `D`.  Since `delta<=R(t)/2`,

\[
\boxed{
\liminf {4|E_{str}(\eta)|+2s_B\over D}
\ge
B(t)-{R(t)\over2\eta}.
}
\tag{GI.11}

If

\[
M_\eta:=\max\{s_B,|E_{str}(\eta)|\},
\]

then the left side of (GI.11) is at most `6M_eta`.  Therefore

\[
\boxed{
\liminf {M_\eta\over D}
\ge
{1\over6}
\left(B(t)-{R(t)\over2\eta}\right).
}
\tag{GI.12}

## 3. Current audited endpoint

Use

\[
t_{21}
={4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0017279
=1.82124143797944\ldots .
\]

At this point

\[
R(t_{21})=0.00567555\ldots,
\qquad
{R(t_{21})\over2}=0.002837775\ldots,
\]

and

\[
B(t_{21})=2.31929388534854\ldots .
\]

Take

\[
\boxed{\eta={4\over15}.}
\]

Then

\[
\cos\alpha_\eta=1-{\eta\over2}={13\over15}>{\sqrt3\over2},
\]

so

\[
\alpha_\eta<\pi/6
\]

with strict margin.  The detour payment is

\[
{R(t_{21})\over2\eta}
=0.01064165625\ldots .
\]

Therefore (GI.12) gives

\[
\boxed{
\liminf {M_{4/15}\over D}
\ge0.384775371516423\ldots .
}
\tag{GI.13}

The global-turn theorem gives the exact inward component

\[
\boxed{
Y_{4/15}
=\sin\left({\pi\over3}-\arccos{13\over15}\right)
={13\sqrt3-2\sqrt{14}\over30}
=0.501111524161584\ldots .
}
\tag{GI.14}

The bisector family is even more transverse:

\[
(w-v)\cdot n_v>{\sqrt3\over2}.
\tag{GI.15}

## 4. Why this is stronger than the previous contact conversion

The earlier shallow-tooth theorem used a pointwise-injective apex range and gave

\[
E_{pen}\ge{1\over4}
\left(N_2-{d_{out}\over\eta}\right)
\]

with `eta` restricted below approximately `0.06815`.  The resulting current-floor
two-way burden was only about `0.2840D`.

Global hull turning shows that shallow-apex duplication is globally exceptional rather
than locally impossible.  This permits `eta=4/15` and doubles the penetration factor.
The resulting lower bound (GI.13) is larger by about `0.1008D`.

## 5. Frontier effect

The low-`t` branch now has an unconditional physical dichotomy at scale nearly
`0.385D`:

```text
(A) s_B = Omega(D):
    many loaded hull vertices have contact degree below three;

or

(B) E_str = Omega(D):
    many distinct actual unit contacts point strongly into the force hull / tooth
    interior, with a uniform projection bounded away from zero.
```

No small-`R_F` hypothesis is needed for this dichotomy.  It therefore applies before
the separate small-residual pentagon reflection/hidden-chord reductions.

A closing theorem can now target a direct incidence/response cost of the inward-contact
family or show that the loaded degree deficit in branch (A) is incompatible with the
near-extremal diameter/thrackle topology.

## 6. Scope audit

- `N_2` is the actual two-edge outer-tooth count from the canonical distinguished
  outer-route decomposition.
- The global-turn shallow-tooth theorem supplies all but two distinct apices; the
  finite `-2` is retained in (GI.7) and disappears only after division by `D`.
- `E_bis` and `E_pen` may overlap; passing to their union uses the safe inequality
  `|E_pen|+|E_bis|<=2|E_str|`.
- Every counted edge is an actual unit contact in the source.
- The inward projection lower bounds are geometric and unweighted; no KKT coefficient
  floor is assumed.
- The only proof-only numerical input is the audited `g=0.0021` low-`t` checkpoint.
- No exact unit equilateral triangle or strict same-cardinality sub-`D` competitor is
  produced.

**Disposition:** proof-only structural strengthening.  C-II and Level I remain open.
