> Generated reading edition · [exact source](../../../docs/reports/target_c_uniform_secondary_exact_flat_2026-09-05.md) · source SHA-256 `ea04414ffd7ad442cebe3307fd16e26272efd5bc6788f7b66e3a8e3ce9c08238`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-8241D61B5583","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C uniform secondary exact-active flat

**Date:** 2026-09-05  
**Repository state:** `9c78bad9` (`main`)  
**Run type:** exact cross-theorem consolidation / quantitative strengthening  
**Target:** Target C C80-C96 pure-rhombic chain-face branch  
**External web search:** not used  
**Computation:** arithmetic only

## LEVEL I STATUS

`STILL OPEN`

## 1. Point of the note

C94 is usually quoted as the dichotomy

`T >= (3-o(1))D`

or

`dim L >= (pi/sqrt(3)-1-o(1))D`.

That wording is useful for obtaining the stronger `0.813799...D` coefficient below `3D`, but it hides a uniform fact already implicit in C82+C86+C94:

> **Every** asymptotic C80 chain-face survivor has a positive linear-dimensional exact-active tangent flat supported entirely on secondary trains, including the high-train branch.

The universal coefficient is

`1+Delta_2-pi/2 = 0.3361033553...`.

## 2. Ingredients

Write

`x=T/D`, `y=q/T`,

`A=1+Delta_2`, `Delta_2=pi/(2sqrt(3))`.

C94 defines

`L = intersection_(h in H) ker g_h`

inside the train-angle quotient and proves the exact finite inequality

`dim L >= T-|H| >= T-q`.

C86 proves that after quotienting global rotation every vector in `L` has zero coordinate on all `D` chain trains in `P`, and every such vector integrates direction-by-direction to a nearby realization preserving every original unit contact and every original diameter pair exactly.

C82 gives, for bounded subsequential `x`,

`x >= A/(1-y/2)+o(1)`,

hence

`q/D=xy <= 2x-2A+o(1)`.

The convex-hull/diameter endpoint perimeter bound also gives

`q/D <= pi+o(1)`.

## 3. Uniform theorem

### Theorem — uniform secondary exact-flat floor

Every asymptotic canonical pure-rhombic C80 chain-face survivor satisfies

`dim L / D >= A-pi/2-o(1)`

that is,

`dim L >= (1+pi/(2sqrt(3))-pi/2-o(1))D`

`= (0.3361033553...-o(1))D`.

After fixing global rotation, this whole linear space is supported on the non-chain train coordinates, and every vector is an exact-active tangent direction in the C86 sense.

### Proof

First suppose `x=T/D` stays bounded along the chosen subsequence. From C82 and the perimeter endpoint bound,

`q/D <= min(pi, 2x-2A)+o(1)`.

Therefore C94's finite dimension inequality gives

`dim L/D >= x-q/D`

`>= max(x-pi, 2A-x)-o(1)`.

The decreasing line `2A-x` and increasing line `x-pi` meet at

`x_0=A+pi/2`.

Their common value is

`A-pi/2`.

Hence for every bounded `x`,

`max(x-pi,2A-x) >= A-pi/2`,

which proves the stated bound.

If `x` is unbounded, the endpoint perimeter bound alone gives

`dim L/D >= x-pi-o(1)`,

which tends to infinity and is stronger. Thus the same universal lower bound holds without any upper assumption on `T/D`.

Finally C86 identifies the chain coordinates of every vector in `L` and makes them all equal; subtracting global rotation sets all of them to zero. The same theorem gives the direction-by-direction exact-active integration. `square`

## 4. Relation to C94

The theorem does not supersede C94. It changes the useful way to split the remaining problem:

- if `T/D<3+o(1)`, C94 gives the much stronger coefficient
  `pi/sqrt(3)-1=0.813799...`;
- near the worst uniform point
  `T/D=A+pi/2=3.477696...`, the coefficient can fall to
  `A-pi/2=0.336103...`;
- for larger `T/D`, the elementary `T-q` bound rises again because `q<=pi D+o(D)`.

So `T>=3D` is not a no-flex escape. It is only the place where the particularly strong `0.8138D` low-train coefficient ceases to be automatic.

## 5. Consequence for the activation program

C95 and the simultaneous activation-dissection theorem should be viewed against a **uniform** linear flat, not only the low-train branch:

```text
all C80-C96 chain-face survivors
  -> secondary exact-active flat dimension >=0.336103D-o(D)
  -> C_ACT preserves the old KKT stress through first activation
  -> M simultaneous harmless contacts cost M sqrt(3)/2 shell area
  ?
```

The question mark remains the same real gap: a high-dimensional feasible exact-active set can meet low-rank boundary facets one at a time. The uniform dimension theorem does not justify the rejected C102 one-event rank inference.

A valid closing theorem still needs persistence, a monotone sequential charge, or a geometric statement forcing high simultaneous multiplicity.

## 6. Audit classification

| Statement | Classification | Reason |
| --- | --- | --- |
| `dim L>=T-q` | already canonical | Target B Section 40 / C94 |
| all chain coordinates vanish in `L` mod rotation | already canonical | C86 / C94 |
| `q/D<=2x-2A+o(1)` for bounded `x` | already canonical rearrangement | C82 / C94 |
| `q/D<=pi+o(1)` | already canonical | perimeter endpoint bound |
| uniform `dim L/D>=A-pi/2-o(1)` | proved here | minimax of the two endpoint bounds |
| high-train phase can avoid a linear exact flat | rejected | the uniform bound rules this out |
| linear flat alone forces one high-rank first event | rejected | separate activation-rank audit |

## 7. Handoff

```text
LEVEL I STATUS: STILL OPEN.

Uniform fact:
Every pure-rhombic C80 chain-face survivor has an exact-active secondary-train tangent flat of dimension at least

  (1 + pi/(2sqrt(3)) - pi/2 - o(1))D
  = (0.3361033553...-o(1))D.

The old T>=3D branch does not escape the flex mechanism; only the stronger 0.813799D coefficient is lost there.

Remaining activation lemma:
Turn this uniform linear exact-active dimension into either a persistent/sequential shell charge, one genuinely high-multiplicity event, a strict diameter decrease, or a forced unit triangle.
```
