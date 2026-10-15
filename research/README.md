# Reproducible research artifacts

The initial computation is `triangular-lattice-baseline.json`, generated with Python's standard library by:

```sh
python3 scripts/triangular_lattice.py --max-n 5
```

It records exact squared diameters and one witness for each lattice-restricted size (2\le n\le5). The coordinate pairs and integer metric are defined in [P99-COMP-001](../tasks/P99-COMP-001-triangular-lattice.md). No result here is asserted for unrestricted planar configurations.
