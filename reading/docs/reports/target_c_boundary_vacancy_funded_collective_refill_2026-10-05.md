> Generated reading edition · [exact source](../../../docs/reports/target_c_boundary_vacancy_funded_collective_refill_2026-10-05.md) · source SHA-256 `a765e63ecf244e068558168c746b4253aa174e03ecccd678d4e4754f36182ea7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8A4840B492E3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — two boundary vacancies fund a collective full-interior refill

**Date:** 2026-10-05. **Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f.
**Run checkpoint:** 564ad3ed. **State:** 2026-09-14.audit.51.
**Classification:** proved source-replacement candidate awaiting independent audit.
Unreviewed and noncanonical. **LEVEL I STATUS: STILL OPEN.**

## 1. Stronger activation threshold

The preceding [unit-wall activation criterion](target_c_vacancy_funded_unit_wall_activation_2026-10-05.md)
excluded a sufficiently close fixed triangular rectangular wall enclosing
a population deficient by three slots. The present theorem lowers that
threshold to **two** by deleting two actual wall vertices and using their
labels to fund a full strict interior population. It does not require
old interior contacts or force activation of a new contact.

The replacement preserves cardinality, every exterior label and every
lower constraint, keeps the maximum diameter at most its old value, and
strictly decreases the number of contacts. Actual global optimality and
contact minimality then give a contradiction.

The closing gap is still whether the forced train/face bank produces a
complete actual enclosing wall with this integer population deficit.
No general full-core or macroscopic-container closure is claimed.

## 2. A relaxed unit-edge shield

**Lemma B.1.** Let $`|a-b|=1`$, let all four distances from $`x,y`$
to $`a,b`$ be at least $`t`$, with $`1/\sqrt2\le t\le1`$, and
let $`[x,y]`$ cross $`[a,b]`$. Then

```math
\boxed{|x-y|\ge\sqrt{4t^2-1}.}\tag{B.1}
```

For a proper crossing, write $`\theta_0=2\arcsin(1/(2t))`$.
If the side lengths at $`x`$ are $`r,s\ge t`$, then

```math
\cos\angle axb=1+\frac{(r-s)^2-1}{2rs}
\ge1-\frac1{2t^2}=\cos\theta_0.
```

The same holds at $`y`$. One of the quadrilateral angles at $`a,b`$
is therefore at least $`\pi-\theta_0\ge\pi/2`$. Its adjacent sides
are at least $`t`$, and the cosine law gives
$`|x-y|^2\ge2t^2(1+\cos\theta_0)=4t^2-1`$.
Degenerate crossings follow by continuity, or by the direct bound
$`|x-y|\ge2t`$ when a wall endpoint lies between the pair.

At $`t=19/20`$, the bound is $`\sqrt{261}/10>151/100`$.
This margin is used **before** moving a reference interior point, rather
than pretending that its final position stays separated from a deleted
wall vertex.

## 3. Release the whole triangular interior through two boundary holes

Fix $`m,n\ge3`$, $`u=(1,0)`$,
$`v_0=(1/2,\sqrt3/2)`$, and the complete rectangular triangular
grid wall $`W_0`$. Let $`K_0=(m-1)(n-1)`$. Remove the two adjacent
side-wall labels $`(1,0),(2,0)`$. Retain **all** $`K_0`$ interior
labels and all other wall points.

**Lemma B.2.** There is a finite sequential motion which fixes the
remaining wall, retains every interior label, stays unit-separated
throughout, and ends with all $`K_0`$ interior points strictly separated
from one another and from the remaining wall. Every interior point can
be required to move less than $`1/100`$ and stay strictly inside the
original parallelogram.

Use the same six-direction release rule proved in W.5. When two adjacent
direction neighbors are absent or already released, move the point in
their direction-vector sum. Every remaining unit contact lengthens
linearly or quadratically. Previously released contacts and noncontacts
have strict finite slack, so an arbitrarily small positive amplitude
preserves every lower constraint along the whole segment. Each label
moves only once, permitting the stated displacement bound.

For $`j=1,\ldots,n-1`$, release $`(1,j)`$ using missing
$`(1,j-1),(2,j-1)`$, then $`(2,j)`$ using missing
$`(1,j),(2,j-1)`$. The first pair is precisely the two removed
boundary pins. After these two columns are released, for
$`i=3,\ldots,m-1`$, release $`(i,1)`$ using missing
$`(i-1,1),(i-1,2)`$, and then $`(i,j)`$, $`j=2,\ldots,n-1`$,
using missing $`(i-1,j),(i,j-1)`$.

Every required neighbor pair consists of adjacent lattice directions and
is already absent from the remaining contact system. The order covers
all interior labels exactly once. This proves B.2. Sequential amplitudes
may decrease rapidly; no uniform radius in growing frame size is asserted.

## 4. Nearby actual walls and every exterior point

Let $`Y_*`$ be a strict endpoint realization of B.2, and write
$`p_z^0`$ for the original grid coordinate associated to its label $`z`$.
The positive minimum wall-distance excess to the **remaining** wall
gives a tolerance $`\eta_{m,n}>0`$, chosen also at most $`1/20`$.

Consider any actual simple unit-contact cycle $`W`$ whose vertices,
in the same order, are within $`\eta_{m,n}`$ of the corresponding
$`W_0`$ vertices after a Euclidean isometry. Remove its two corresponding
side vertices, denoted $`a_*,b_*`$. Every $`Y_*`$ point is still
strictly separated from the retained actual wall vertices.

Each reference $`p_z^0`$ has distance at least $`\sqrt3/2`$ from
the reference polygon boundary. The actual curve stays within
$`\eta_{m,n}\le1/20`$ of that curve. The winding-number argument
from W.6 therefore keeps both $`p_z^0`$ and its moved point strictly
inside the actual wall.

Let $`y`$ be any retained old exterior source point. Its distance to
every actual wall vertex, including $`a_*,b_*`$, was at least one.
Every $`p_z^0`$ is separated from every reference wall vertex by at
least one, hence from every actual wall vertex by at least
$`1-\eta_{m,n}\ge19/20`$. The segment from $`p_z^0`$ to $`y`$
crosses an actual unit wall edge. Lemma B.1 gives

```math
|p_z^0-y|\ge\sqrt{261}/10>151/100.
```

After its displacement of less than $`1/100`$, the target point is
therefore farther than $`3/2`$ from $`y`$. This checks **every**
exterior source point, including isolates and points near the opened
boundary gap. No exterior point is deleted or moved.

The final target points need not be separated from the two deleted wall
coordinates. Their original reference positions supply the shielding
margin. Neither reference points nor deleted wall coordinates are counted
as additional final source points or treated as diameter loads.

## 5. Exact source contradiction at deficiency two

**Theorem B.3.** Fix $`m,n\ge3`$. There exists $`\eta_{m,n}>0`$
such that every triangle-free contact-minimal global minimizer containing
an actual wall as in Section 4 satisfies

```math
\boxed{|A\cap\operatorname{int}(C_W)|\ge K_0-1.}\tag{B.2}
```

Suppose its enclosed set $`Z`$ had at most $`K_0-2`$ points.
Delete $`Z`$ and the two side-wall vertices $`a_*,b_*`$; insert
$`|Z|+2\le K_0`$ points of $`Y_*`$. Assign the old labels
bijectively to these positions. Cardinality remains exactly $`|A|`$.
Mutual and retained-wall lower constraints are strict by construction;
all exterior lower constraints are strict by Section 4. Retained old
pairs are unchanged.

All inserted points are in $`\operatorname{int}\operatorname{conv}W`$,
so every pair involving an inserted point has distance strictly less than
the old diameter. The remaining maximum is at most the old diameter.
Global optimality either directly contradicts a strict decrease or forces
equality at $`D(n)`$. In the latter case the new source is triangle-free:
all contacts are inherited by retained old points. Deleting the two wall
vertices removes their cycle contacts, and the inserted points have none.
Thus the total contact count strictly decreases, contradicting selection.

All source points, including every enclosed or exterior isolate, are
accounted for. Actual global optimality is used only after the complete
finite replacement is proved feasible. No activation of a KKT multiplier
and no full-source extension of the Section-57 affine kernel is used.

**Sequence scope.** First fix $`m,n`$. Any sequence of canonical sources
with these actual unit walls converging pointwise to the reference wall
and with enclosed populations at most $`K_0-2`$ is excluded eventually.
The wall tolerance depends on the fixed finite frame; this is not a
growing-frame or arbitrary-interface capacity theorem.

## 6. Certificate and live implication

```bash
python3 research/verify_target_c_boundary_vacancy_funded_collective_refill_2026_10_05.py
```

Four exact triangular packets release the whole interior through two
boundary holes. Complete oblique guarded source replacements retain all
labels, relocate both funding labels into the interior, remove contacts,
preserve the full maximum diameter and check every old/new pair.
Every new/exterior-guard distance is at least $`3/2`$. The rational
displacement bound and relaxed shielding constant are certified.

These guarded configurations are actual planar separated point sets,
but are not certified global minimizers. The contradiction for actual
minimizers is the analytic B.3 theorem. The earlier one-vacancy triangular
pinned-stress regression is retained; B.2 deliberately removes two pins.

The live source class is now restricted by B.3 as well as W.3. To close
the general full-core or macroscopic-container branch, the remaining
argument must force an actual complete near-triangular unit cycle and
the stated deficiency, or extend this protected replacement to the
interfaces supplied by the canonical train/phase structure. No current
scalar inequality supplies either hypothesis by itself.
