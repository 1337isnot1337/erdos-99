# Target C-II — the final linear blocker fork has one common ordered-support normal form

**Date:** 2026-09-17  
**Status:** proof-only high-`t` synthesis/structural strengthening; no canonical promotion claimed  
**Scope:** the corrected linear obstruction shore in the canonical full-core/no-macroscopic-container Type-II branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** exact-antipodal/strong-TB1 density fork; exact-antipodal force-pair theorem; strong-TB1 blocker theorem; common diameter-routing hub; one-sided interval support; ordered convex diameter-thrackle geometry; one-turn hubward path-region order  
**Certificate:** `research/verify_target_c_high_t_unconditional_obstruction_support_normal_form_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The corrected high-`t` obstruction fork previously left two qualitatively different positive-density mechanisms:

- exact-antipodal interfaces carrying a two-bar exact force pair; or
- non-antipodal interfaces carrying one uniformly interior strong-TB1 blocker.

For support topology, this distinction is unnecessary. Each interface in either mechanism supplies at least one actual switching diameter bar, and all selected interfaces lie on one side of the same diameter-routing hub. A general one-bar order argument therefore puts **either mechanism** into the same three support normal forms.

The consequence is unconditional within the current high-`t` branch: one of a proper staircase, a cross-host nested rail, or a one-death macroscopic separator occurs at positive linear density.

---

## 1. General one-bar support lemma

Let `Z_D` be any family of nonhub interfaces on one fixed side of the common routing hub. Suppose that for every `i in Z_D` one chooses one actual switching diameter bar `h_i in X_i`.

Different interfaces on one hub side have disjoint switching sets, so the selected bars are distinct. Assume

\[
|Z_D|>zD-o(D)
\tag{UN.1}
\]

for some fixed `z>0`.

Then one of the following three alternatives contains more than

\[
\boxed{{z\over8}D-o(D)}
\tag{UN.2}

selected bars.

### (A) Proper staircase

There are interface tags

\[
i_1<i_2<\cdots<i_M<k
\]

and support ends

\[
b_1\le b_2\le\cdots\le b_M,
\qquad b_s\ge k,
\]

with

\[
I_s=\{i_s+1,\ldots,b_s\}.
\tag{UN.3}
\]

Thus both support endpoints advance monotonically and every interval contains the common hub cut.

### (B) Cross-host nested rail

There are

\[
i_1<i_2<\cdots<i_M<k,
\qquad
b_1\ge b_2\ge\cdots\ge b_M\ge k,
\]

so

\[
I_1\supsetneq I_2\supsetneq\cdots\supsetneq I_M,
\tag{UN.4}
\]

and every chosen bar joins one fixed pre-hub birth host arc to one fixed hubward partner host arc.

### (C) One-death plateau

There are strictly increasing birth interfaces `i_s` and one fixed post-hub interface `b_*` such that

\[
I_s=\{i_s+1,\ldots,b_*\}
\tag{UN.5}
\]

for every retained bar. Hence all retained bars belong to the same switching set `X_{b_*}`, and

\[
\boxed{
N_{b_*}:=|X_{b_*}|>{z\over8}D-o(D).
}
\tag{UN.6}

Since `J_{b_*}>=N_{b_*}`, this death interface is outside every fixed-threshold good class for all sufficiently large `D`.

Partner endpoints may collide in all three alternatives. Birth endpoints are distinct. After partner-degree thinning, each alternative contains

\[
\boxed{
\left({z\over32\,3^{1/8}}-o(1)\right)D^{1/4}
}
\tag{UN.7}

endpoint-disjoint bars, hence a pairwise-crossing diameter matching.

---

## 2. Proof of the general lemma

Every selected pre-hub switching interval starts at its tagged interface. Its birth endpoint lies in one of the two host-side boundary subarcs of the middle layer. Pigeonhole one fixed birth host side, retaining more than

\[
{z\over2}D-o(D)
\tag{UN.8}

bars.

Their birth endpoints are pairwise distinct and ordered by interface index, up to one global reversal of the host-arc orientation. Every selected bar crosses the common hub cut. If two partner endpoints on the opposite shore are distinct, the corresponding diameter edges are vertex-disjoint and therefore cross; convex chord order then forces compatible partner order. If the partner endpoints coincide, record a tie. Thus the partner map is weakly order-preserving.

The path-region labels on the hubward shore form one weakly increasing then weakly decreasing word. Hence the support-end labels of the fixed-birth-side family form a weakly unimodal sequence, up to reversal. One monotone prefix or suffix has at least half the family, giving

\[
>{z\over4}D-o(D)
\tag{UN.9}

bars with monotone support ends.

If the ends are nondecreasing, this is alternative (A), already stronger than (UN.2).

If the ends are nonincreasing, the supports are strictly nested. Apply the one-turn physical-host argument to this nested family. Either at least half the bars use one fixed hubward host arc, giving (B), or at least half have one common support-end tag, giving (C). This costs at most one further factor `1/2` and proves (UN.2).

The source-wide diameter-degree bound

\[
\Delta(H)\le(4\,3^{1/8}+o(1))D^{3/4}
\tag{UN.10}
\]

proves (UN.7), because births are already distinct and only partner collisions need to be thinned.

---

## 3. Apply the lemma to the final exact-antipodal / strong-TB1 fork

The current unconditional fork gives

\[
|E_D|+|S_D|>{7c_0\over8}D-o(D),
\qquad
c_0={113\over20{,}000{,}000}.
\tag{UN.11}

Therefore one mechanism has

\[
\boxed{
\max\{|E_D|,|S_D|\}
>s_0D-o(D),
\qquad
s_0={7c_0\over16}
={791\over320{,}000{,}000}.
}
\tag{UN.12}

If the larger mechanism is `S_D`, use the already chosen strong-TB1 bar at every interface.

If the larger mechanism is `E_D`, the exact-antipodal force theorem supplies two distinct actual switching bars which positively generate the exact reaction; choose either one consistently at each interface. The omitted mate and the exact two-ray reaction certificate remain attached to the interface, although only one bar is needed for the support-order lemma.

Thus the general lemma applies with `z=s_0` in either case.

### Unconditional support normal form

One of (A), (B), or (C) has size

\[
\boxed{
>{s_0\over8}D-o(D)
={791\over2{,}560{,}000{,}000}D-o(D)
=(3.08984375\times10^{-7})D-o(D).
}
\tag{UN.13}

After partner-degree thinning the corresponding endpoint-disjoint crossing family has size

\[
\boxed{
>
(6.73343031652\times10^{-8}-o(1))D^{1/4}.
}
\tag{UN.14}

This conclusion no longer conditions the support topology on which side of the exact-antipodal/strong-TB1 fork survives.

---

## 4. What structure remains attached to the chosen mechanism

The common support normal form does not erase the local obstruction type.

### If the selected branch came from `E_D`

At every retained interface there is a second switching diameter bar on the opposite transverse side, and the pair has an exact positive two-ray representation of the nonzero strip reaction

\[
G_i=D(\lambda_i^-d_i^-+\lambda_i^+d_i^+),
\qquad \lambda_i^\pm>0.
\tag{UN.15}

The ordered rail therefore carries an exact-antipodal force-pair tag at every birth interface.

### If the selected branch came from `S_D`

Every retained rail bar itself satisfies the fixed strong first-order margin

\[
 n_i\cdot w\ge D\sin\gamma
\quad(w\in\Omega_i,\ |w|=1),
\qquad
\gamma={c_0\over32}>0.
\tag{UN.16}

Thus the ordered rail consists of uniformly interior tangent blockers.

In both cases the interfaces live in the same high-`t` rectangle and share the common near-triangular transverse scaffold already proved for that rectangle.

---

## 5. Frontier effect

The final linear obstruction fork is now topologically unified:

```text
positive-density high-t blocker interfaces
          |
          v
one selected switching diameter per interface
          |
          v
fixed birth host side
          |
          v
weakly ordered hubward partner map
          |
          v
one-turn support-end word
          |
          +--> proper staircase
          |
          +--> cross-host nested rail
          |
          +--> one-death plateau with N_{b_*}=Theta(D).
```

The exact-antipodal versus strong-TB1 distinction survives only as additional local force/derivative data attached to the same three global support geometries.

This gives a cleaner closing target. A proof of C-II in the current high-`t` branch may now attack these three support normal forms directly. The death case localizes all missing complexity at one macroscopic separator. The staircase and cross-host cases have linear ordered endpoint/support data to combine with near-central diameter geometry and the common inverse-`D` train grid.

No C-II or Level-I closure is claimed.

**Disposition:** unified the corrected exact-antipodal/strong-TB1 density fork into one unconditional three-way ordered-support normal form with explicit positive linear density. C-II and Level I remain open.
