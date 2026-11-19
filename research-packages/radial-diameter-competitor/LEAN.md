# Lean proof of the radial path condition

[Radial.lean](Radial.lean) formalizes the global-minimizer consequence of [Section 2](README.md#2-ordering-the-radial-changes-when-the-interior-is-occupied). OpenAI Codex wrote the formalization from the research note at `6acad14f2915b5a9bc1d1b7ce5250a49d14128db`.

`diameter_pair_with_binned_paths` applies to any finite planar diameter minimizer in the exact `Erdos99.HasMinDist1` and `IsMinOn` domain of the [pinned bounty target](https://github.com/conjectures-io/conjectures-tasks/tree/2a58149e6edb0f1dc15b32391f8c29fdd85e9db3/pool/tier-1/erdos-99-formalized). Write `D` for its diameter, choose a center within `0.9D` of every point, and order the labels by decreasing radial bin with width `1/(32D)`. Ties within a bin may be broken arbitrarily. For `0 < ε ≤ 1/2` and `L = floor(sqrt(Dε)/64) ≥ 1`, some diameter pair has a directed path of `L` edges starting at each endpoint. Each edge is at most `1 + ε` long and follows the label order.

The proof chooses the largest reachable path depth from all short-path diameter endpoints at once. If those endpoints cover the diameter pairs, the radial move gives a strictly smaller-diameter configuration with all pair distances at least one. Dividing by its attained minimum pair distance puts the competitor in the exact feasible set at the original cardinality. The reusable declarations are `exists_replacement_of_short_path_cover` for the move and `no_strict_replacement_of_minimal` for the normalization argument. Erdős #99 remains open.

## Replay

Use Lean `v4.33.1`, mathlib `0df444a360eaa60ab8c11dca51a86af692955474`, and Formal Conjectures `6a786f997e18e8f095762a2830d191b7e25e505e`. The last commit is constructed from the [base commit](https://github.com/google-deepmind/formal-conjectures/tree/7d1a8c9912747679d0093f6d1216420c33ee5ffa) and the [pool patch](https://github.com/conjectures-io/conjectures-tasks/blob/2a58149e6edb0f1dc15b32391f8c29fdd85e9db3/tiers/tier-1/formal-conjectures-audit-fixes.patch) by the [contribution workspace bootstrap](https://github.com/conjectures-io/conjectures-contribution/blob/main/scripts/lean_workspace.sh).

From that Formal Conjectures checkout, set `E99_ROOT` to the absolute path of this Erdős #99 checkout and run:

```sh
lake exe cache get Mathlib
lake build 'FormalConjectures.ErdosProblems.«99»'
proof="$E99_ROOT/research-packages/radial-diameter-competitor/Radial.lean"
lake env lean -DwarningAsError=true -DautoImplicit=false -DrelaxedAutoImplicit=false "$proof"
{
  cat "$proof"
  printf '\n#print axioms Contribution.Erdos99.Radial.diameter_pair_with_binned_paths\n'
  printf '#print axioms Contribution.Erdos99.Radial.exists_replacement_of_short_path_cover\n'
} | lake env lean -DwarningAsError=true -DautoImplicit=false -DrelaxedAutoImplicit=false --stdin
```

Both audited theorems depend only on `propext`, `Classical.choice`, and `Quot.sound`. Project status is unreviewed pending independent mathematical review of the formal statement and its scope.
