<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "82ebe29c263d3a027bbddc0b781144262ce7ea60", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_additional_common_host_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "80f6859686c266b4f866c37acc5b16348143f1fbece6605bd08d40adcfa24ea1"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — ten further collapsed chambers reject a common outer host

**Status:** proved finite chamber-local candidate; theorem-state authority unchanged.
**Scope:** the ten additional strict collapsed support-six interval boxes `ch4`,
`ch5`, `ch6`, `ch7`, `ch8`, `ch9`, `ch10`, `ch11`, `ch12`, and `ch13` in `verify_target_c_support6_collapsed_additional_chambers_2026_09_18.py`.
**Certificate:** `verify_target_c_support6_collapsed_additional_common_host_2026_09_18.py`.

The exact interval-Newton verifier certifies ten further regular local roots of the
collapsed `K_6`-minus-matching face-closure equations.  In each box the six outside
host trains are projectively parallel.  If all six terminate at one outer host, the
parallel trains are noncrossing and their six endpoints have a cyclic order.  Every
alternating pair of endpoint-disjoint internal trains must then cross as a proper
unit rhombus.

The new certificate exhausts all `6! = 720` endpoint orders for each box. In every order it finds
an alternating pair whose interval-certified projective direction gap is strictly
below `pi/3`, whereas a proper unit-rhombus crossing requires a gap strictly above
`pi/3`.  The worst certified gaps are:

| chamber | orders | largest witness upper bound | `pi/3` lower bound | margin |
|---|---:|---:|---:|---:|
| `ch4` | 720 | `0.8774034006` | `1.0471975511` | `0.1697941506` |
| `ch5` | 720 | `0.9730766085` | `1.0471975511` | `0.0741209427` |
| `ch6` | 720 | `0.9046132326` | `1.0471975511` | `0.1425843186` |
| `ch7` | 720 | `1.0431900382` | `1.0471975511` | `0.0040075130` |
| `ch8` | 720 | `0.9235524378` | `1.0471975511` | `0.1236451134` |
| `ch9` | 720 | `0.9809724675` | `1.0471975511` | `0.0662250837` |
| `ch10` | 720 | `0.9873606311` | `1.0471975511` | `0.0598369201` |
| `ch11` | 720 | `1.0032941416` | `1.0471975511` | `0.0439034096` |
| `ch12` | 720 | `0.8137620162` | `1.0471975511` | `0.2334355350` |
| `ch13` | 720 | `0.8881255453` | `1.0471975511` | `0.1590720059` |

Therefore none of the ten chambers can attach all six parallel host trains to one common
outer host.  This is a strict global attachment exclusion, not merely a local
pentagon check.

The result does **not** exclude these chambers from multi-host stopped-train
embeddings.  The full planarization search for these boxes has ten and nine
angle-eligible train pairs and is not included in this theorem.  It also does not
classify the collapsed two-parameter family, establish a global source embedding,
or close C-II.

Dependency chain:

```text
interval-Newton local root in ch4/ch5/ch6/ch7/ch8/ch9/ch10/ch11/ch12/ch13
  -> six parallel host trains
  -> common-host endpoint cyclic order
  -> alternating endpoint chords must cross
  -> exact projective gap < pi/3 in every order
  -> common-all-outer-host attachment excluded.
```

**Classification:** proved finite chamber-local attachment obstruction; C-II remains
open.
