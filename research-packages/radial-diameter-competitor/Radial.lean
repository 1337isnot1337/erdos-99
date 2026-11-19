import Mathlib
import FormalConjectures.ErdosProblems.«99»

/-!
# Radial replacement for diameter minimizers

Formalization of the distance estimates in §2 of the accompanying research note.
The points are expressed relative to the chosen radial origin.
-/

namespace Contribution.Erdos99.Radial

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

private theorem sq_dist_smul (x y : E) {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) :
    dist (a • x) (b • y) ^ 2 =
      a * b * dist x y ^ 2 + (a - b) * (a * ‖x‖ ^ 2 - b * ‖y‖ ^ 2) := by
  simp only [dist_eq_norm_sub, norm_sub_sq_real, norm_smul, Real.norm_eq_abs,
    abs_of_nonneg ha, abs_of_nonneg hb, real_inner_smul_left, real_inner_smul_right]
  ring

private noncomputable def triangular (k : ℕ) : ℝ := (k : ℝ) * (k + 1) / 2

private theorem triangular_nonneg (k : ℕ) : 0 ≤ triangular k := by
  unfold triangular
  positivity

private theorem triangular_le_sq {k L : ℕ} (hL : 1 ≤ L) (hk : k ≤ L) :
    triangular k ≤ (L : ℝ)^2 := by
  have hkr : (k : ℝ) ≤ L := by exact_mod_cast hk
  have hLr : (1 : ℝ) ≤ L := by exact_mod_cast hL
  have h := mul_le_mul hkr (show (k : ℝ) + 1 ≤ 2 * L by linarith)
    (by positivity) (by positivity : (0 : ℝ) ≤ L)
  unfold triangular
  nlinarith

private theorem triangular_gap {i j : ℕ} (hij : i < j) :
    let d := triangular j - triangular i
    1 ≤ d ∧ triangular j + triangular i ≤ d ^ 2 := by
  dsimp
  have hi : (0 : ℝ) ≤ i := by positivity
  have hj : (i : ℝ) + 1 ≤ j := by exact_mod_cast hij
  have hprod := mul_nonneg (show 0 ≤ (j : ℝ) - i - 1 by linarith)
    (show 0 ≤ (j : ℝ) + i by positivity)
  have hgap : (j : ℝ) ≤ triangular j - triangular i := by
    unfold triangular
    nlinarith
  have hsq : (j : ℝ)^2 ≤ (triangular j - triangular i)^2 := by
    exact pow_le_pow_left₀ (by positivity) hgap 2
  constructor
  · linarith
  · refine le_trans ?_ hsq
    unfold triangular
    nlinarith

private noncomputable def factor (D : ℝ) (k : ℕ) : ℝ := 1 - (512 / D^2) * triangular k

private theorem factor_le_one (D : ℝ) (k : ℕ) : factor D k ≤ 1 := by
  unfold factor
  linarith [mul_nonneg (show 0 ≤ 512 / D^2 by positivity) (triangular_nonneg k)]

private theorem factor_zero (D : ℝ) : factor D 0 = 1 := by
  simp [factor, triangular]

private theorem factor_lt_one {D : ℝ} {k : ℕ} (hD : 0 < D) (hk : 0 < k) :
    factor D k < 1 := by
  have hkr : (0 : ℝ) < k := by exact_mod_cast hk
  have ht : 0 < triangular k := by unfold triangular; positivity
  have hp := mul_pos (show 0 < 512 / D^2 by positivity) ht
  unfold factor
  linarith

private theorem displacement_le {D ε : ℝ} {L k : ℕ}
    (hD : 0 < D) (hL : 1 ≤ L) (hk : k ≤ L)
    (hbudget : 4096 * (L : ℝ)^2 ≤ D * ε) (x : E)
    (hx : ‖x‖ ≤ D) : dist (factor D k • x) x ≤ ε / 8 := by
  have hmove : dist (factor D k • x) x = ‖(factor D k - 1) • x‖ := by
    rw [dist_eq_norm_sub, sub_smul, one_smul]
  rw [hmove, norm_smul, Real.norm_eq_abs]
  rw [abs_of_nonpos (sub_nonpos.mpr (factor_le_one D k))]
  have hs : 0 ≤ 512 / D^2 := by positivity
  have ht := triangular_nonneg k
  have h1 : -(factor D k - 1) = (512 / D^2) * triangular k := by
    unfold factor
    ring
  rw [h1]
  have h2 := mul_le_mul (mul_le_mul_of_nonneg_left (triangular_le_sq hL hk) hs) hx
    (norm_nonneg x) (by positivity)
  refine h2.trans ?_
  calc
    (512 / D^2 * (L : ℝ)^2) * D = (512 * (L : ℝ)^2) / D := by
      field_simp
    _ ≤ ε / 8 := by
      apply (div_le_iff₀ hD).2
      nlinarith only [hbudget]

private theorem factor_pos {D ε : ℝ} {L k : ℕ}
    (hD : 1 ≤ D) (hL : 1 ≤ L) (hk : k ≤ L)
    (hε : ε ≤ 1/2) (hbudget : 4096 * (L : ℝ)^2 ≤ D * ε) :
    0 < factor D k := by
  have hDp : 0 < D := by linarith
  have h := mul_le_mul_of_nonneg_left (triangular_le_sq hL hk)
    (show 0 ≤ 512 / D^2 by positivity)
  have h' : 512 / D^2 * (L : ℝ)^2 ≤ ε / (8 * D) := by
    rw [div_mul_eq_mul_div, div_le_div_iff₀ (by positivity) (by positivity)]
    nlinarith only [mul_le_mul_of_nonneg_right hbudget (show 0 ≤ D by positivity)]
  have h'' : ε / (8 * D) < 1 := by
    apply (div_lt_iff₀ (by positivity)).2
    linarith
  unfold factor
  linarith

/-- A close pair remains strictly separated when the two ordered radii are bounded
away from the center and respect the radial-bin error. -/
private theorem one_lt_dist_radial_of_ordered {D : ℝ} {i j : ℕ} {x y : E}
    (hD : 0 < D) (hij : i < j) (hb : 0 < factor D j)
    (hsep : 1 ≤ dist x y) (hy : D / 16 ≤ ‖y‖)
    (horder : ‖y‖ ^ 2 ≤ ‖x‖ ^ 2 + 1/16) :
    1 < dist (factor D i • x) (factor D j • y) := by
  let s := 512 / D^2
  let d := triangular j - triangular i
  let a := factor D i
  let b := factor D j
  have hs : 0 < s := by dsimp [s]; positivity
  have hd : 1 ≤ d ∧ triangular j + triangular i ≤ d ^ 2 := triangular_gap hij
  have hab : a - b = s * d := by dsimp [a, b, s, d, factor]; ring
  have hδ : 0 ≤ a - b := by rw [hab]; exact mul_nonneg hs.le (by linarith [hd.1])
  have ha : 0 ≤ a := by change 0 < b at hb; linarith
  change 0 < b at hb
  have ha₁ : a ≤ 1 := factor_le_one D i
  have hy₂ : (D / 16)^2 ≤ ‖y‖^2 := pow_le_pow_left₀ (by positivity) hy 2
  have hsq : s * (D / 16)^2 = 2 := by
    dsimp [s]
    field_simp
    ring
  have hlower :
      (a - b) * ((a - b) * (D / 16)^2 - 1/16) ≤
        (a - b) * (a * ‖x‖^2 - b * ‖y‖^2) := by
    apply mul_le_mul_of_nonneg_left _ hδ
    have hz := mul_le_mul_of_nonneg_left hy₂ hδ
    have ho := mul_le_mul_of_nonneg_left horder ha
    nlinarith only [hz, ho, ha₁]
  have hexpand :
      (a - b) * ((a - b) * (D / 16)^2 - 1/16) =
        s * (2 * d^2 - d/16) := by
    rw [hab, mul_assoc s d ((s * d) * (D / 16)^2 - 1/16),
      mul_right_comm s d ((D / 16)^2), hsq]
    ring
  have hgap : triangular j + triangular i < 2 * d^2 - d/16 := by
    nlinarith only [hd.1, hd.2, mul_nonneg (show 0 ≤ d by linarith [hd.1])
      (show 0 ≤ d - 1 by linarith [hd.1])]
  have hm := mul_lt_mul_of_pos_left hgap hs
  have habprod : 1 - a*b ≤ s * (triangular j + triangular i) := by
    have h := mul_nonneg (mul_nonneg hs.le (triangular_nonneg i))
      (mul_nonneg hs.le (triangular_nonneg j))
    -- The product of the two nonnegative radial displacements is retained.
    dsimp [a, b, factor, s] at h ⊢
    nlinarith only [h]
  have hsep₂ : 1 ≤ dist x y ^ 2 := by
    nlinarith only [hsep, mul_nonneg (show 0 ≤ dist x y - 1 by linarith)
      (show 0 ≤ dist x y + 1 by positivity)]
  have hscale := mul_le_mul_of_nonneg_left hsep₂ (mul_nonneg ha hb.le)
  change 1 < dist (a • x) (b • y)
  have hsquared : 1 < dist (a • x) (b • y)^2 := by
    rw [sq_dist_smul x y ha hb.le]
    rw [hexpand] at hlower
    nlinarith only [hlower, hm, habprod, hscale]
  by_contra! h
  have hpow := pow_le_pow_left₀ (dist_nonneg : 0 ≤ dist (a • x) (b • y)) h 2
  rw [one_pow] at hpow
  exact (not_le_of_gt hsquared) hpow

private theorem dist_smul_lt_of_bounds {D a b : ℝ} {x y : E}
    (hD : 0 < D) (ha : 0 ≤ a) (hab : a ≤ b) (hb : b ≤ 1) (ha₁ : a < 1)
    (hxy : dist x y ≤ D) (hy : ‖y‖ ≤ 9 * D / 10) :
    dist (a • x) (b • y) < D := by
  have heq : a • x - b • y = a • (x - y) + (a - b) • y := by module
  rw [dist_eq_norm_sub, heq]
  calc
    ‖a • (x - y) + (a - b) • y‖ ≤ ‖a • (x - y)‖ + ‖(a - b) • y‖ := norm_add_le _ _
    _ = a * dist x y + (b - a) * ‖y‖ := by
      simp only [norm_smul, Real.norm_eq_abs, abs_of_nonneg ha, dist_eq_norm_sub,
        abs_of_nonpos (sub_nonpos.mpr hab), neg_sub]
    _ ≤ a * D + (b - a) * (9 * D / 10) :=
      add_le_add (mul_le_mul_of_nonneg_left hxy ha)
        (mul_le_mul_of_nonneg_left hy (sub_nonneg.mpr hab))
    _ < D := by
      nlinarith only [mul_nonneg (sub_nonneg.mpr hb) hD.le,
        mul_pos (sub_pos.mpr ha₁) hD]

/-- A directed walk with an exact edge count. In the strictly ordered near-unit graph,
a walk cannot repeat a vertex. -/
inductive Path {ι : Type*} (edge : ι → ι → Prop) : ℕ → ι → ι → Prop
  | nil (i : ι) : Path edge 0 i i
  | cons {n : ℕ} {i j k : ι} : edge i j → Path edge n j k → Path edge (n + 1) i k

private theorem Path.snoc {ι : Type*} {edge : ι → ι → Prop}
    {n : ℕ} {i j k : ι} (p : Path edge n i j) (hjk : edge j k) :
    Path edge (n + 1) i k := by
  induction p with
  | nil j => exact .cons hjk (.nil k)
  | cons hij _ ih => exact .cons hij (ih hjk)

private theorem Path.prefix {ι : Type*} {edge : ι → ι → Prop}
    {n m : ℕ} {i j : ι} (p : Path edge n i j) (hm : m ≤ n) :
    ∃ k, Path edge m i k := by
  induction p generalizing m with
  | nil i =>
    have : m = 0 := by omega
    subst m
    exact ⟨i, .nil i⟩
  | cons hij _ ih =>
    cases m with
    | zero => exact ⟨_, .nil _⟩
    | succ m =>
      obtain ⟨k, hk⟩ := ih (m := m) (by omega)
      exact ⟨k, .cons hij hk⟩

/-- Direct every near-unit edge from the earlier to the later label. -/
def nearEdge {ι : Type*} [LT ι] (x : ι → E) (ε : ℝ) (i j : ι) : Prop :=
  i < j ∧ dist (x i) (x j) ≤ 1 + ε

omit [InnerProductSpace ℝ E] in
private theorem Path.dist_le {ι : Type*} [LT ι] {x : ι → E} {ε : ℝ}
    {n : ℕ} {i j : ι} (p : Path (nearEdge x ε) n i j) :
    dist (x i) (x j) ≤ (n : ℝ) * (1 + ε) := by
  induction p with
  | nil i => simp
  | @cons n i j k hij _ ih =>
    calc
      dist (x i) (x k) ≤ dist (x i) (x j) + dist (x j) (x k) := dist_triangle _ _ _
      _ ≤ (1 + ε) + (n : ℝ) * (1 + ε) := add_le_add hij.2 ih
      _ = ((n + 1 : ℕ) : ℝ) * (1 + ε) := by push_cast; ring

/-- If diameter endpoints with no length-`L` near-unit path cover all diameter
pairs, simultaneous radial replacements preserve unit separation and strictly
shorten every pair below the old diameter. The squared-radius order hypothesis
permits the arbitrary tie order within bins of width `1 / (32 * D)`. -/
theorem exists_replacement_of_short_path_cover {ι : Type*} [LinearOrder ι]
    (x : ι → E) {D ε : ℝ} {L : ℕ}
    (hD : 0 < D) (hε : 0 < ε) (hε' : ε ≤ 1/2) (hL : 1 ≤ L)
    (hbudget : 4096 * (L : ℝ)^2 ≤ D * ε)
    (hsep : ∀ i j, i ≠ j → 1 ≤ dist (x i) (x j))
    (hdiam : ∀ i j, dist (x i) (x j) ≤ D)
    (hradius : ∀ i, ‖x i‖ ≤ 9 * D / 10)
    (horder : ∀ i j, nearEdge x ε i j → ‖x j‖^2 ≤ ‖x i‖^2 + 1/16)
    (hcover : ∀ i j, dist (x i) (x j) = D →
      (¬ ∃ k, Path (nearEdge x ε) L i k) ∨ (¬ ∃ k, Path (nearEdge x ε) L j k)) :
    ∃ y : ι → E,
      (∀ i j, i ≠ j → 1 ≤ dist (y i) (y j)) ∧ ∀ i j, dist (y i) (y j) < D := by
  classical
  let start (i : ι) : Prop :=
    (∃ j, dist (x i) (x j) = D) ∧ ¬ ∃ k, Path (nearEdge x ε) L i k
  let reaches (i : ι) (n : ℕ) : Prop := ∃ p, start p ∧ Path (nearEdge x ε) n p i
  have hlength {i : ι} {n : ℕ} (h : reaches i n) : n < L := by
    obtain ⟨p, hp, path⟩ := h
    exact lt_of_not_ge fun hLn => hp.2 (path.prefix hLn)
  let rank (i : ι) := Nat.findGreatest (fun n => reaches i n) L
  have rank_reaches {i : ι} (h : ∃ n, reaches i n) : reaches i (rank i) := by
    obtain ⟨n, hn⟩ := h
    exact Nat.findGreatest_spec (hlength hn).le hn
  let depth (i : ι) := if ∃ n, reaches i n then rank i + 1 else 0
  have depth_pos (i : ι) : 0 < depth i ↔ ∃ n, reaches i n := by
    by_cases hi : ∃ n, reaches i n <;> simp [depth, hi]
  have depth_le (i : ι) : depth i ≤ L := by
    by_cases hi : ∃ n, reaches i n
    · simpa [depth, hi] using Nat.succ_le_of_lt (hlength (rank_reaches hi))
    · simp [depth, hi]
  have depth_lt {i j : ι} (hij : nearEdge x ε i j)
      (hmove : 0 < depth i ∨ 0 < depth j) : depth i < depth j := by
    by_cases hi : ∃ n, reaches i n
    · obtain ⟨p, hp, path⟩ := rank_reaches hi
      have hj : reaches j (rank i + 1) := ⟨p, hp, path.snoc hij⟩
      have hj' : ∃ n, reaches j n := ⟨_, hj⟩
      have hle : rank i + 1 ≤ rank j := Nat.le_findGreatest (hlength hj).le hj
      simp only [depth, if_pos hi, if_pos hj']
      omega
    · have hdi : depth i = 0 := by simp [depth, hi]
      rw [hdi] at hmove ⊢
      exact hmove.resolve_left (Nat.lt_irrefl _)
  have hLr : (1 : ℝ) ≤ L := by exact_mod_cast hL
  have hDL : 40 * (L : ℝ) ≤ D := by
    have h := mul_le_mul_of_nonneg_left hε' hD.le
    nlinarith only [h, hbudget, mul_nonneg (show 0 ≤ (L : ℝ) by positivity)
      (show 0 ≤ (L : ℝ) - 1 by linarith)]
  have hD1 : 1 ≤ D := by linarith
  have start_radius {p : ι} (hp : start p) : D / 10 ≤ ‖x p‖ := by
    obtain ⟨q, hq⟩ := hp.1
    rw [dist_eq_norm_sub] at hq
    linarith [norm_sub_le (x p) (x q), hradius q]
  have near_radius {i j : ι} (hi : 0 < depth i)
      (hij : dist (x i) (x j) ≤ 1 + ε) : D / 16 ≤ ‖x j‖ := by
    obtain ⟨p, hp, path⟩ := rank_reaches ((depth_pos i).mp hi)
    have hn : ((rank i : ℕ) : ℝ) + 1 ≤ L := by
      exact_mod_cast hlength (rank_reaches ((depth_pos i).mp hi))
    have hdist : dist (x p) (x j) ≤ (L : ℝ) * (1 + ε) := by
      refine (dist_triangle (x p) (x i) (x j)).trans ?_
      have hmul := mul_le_mul_of_nonneg_right hn (show 0 ≤ 1 + ε by linarith)
      linarith [path.dist_le]
    have ht : dist (x p) (x j) ≤ 3 * (L : ℝ) / 2 := by
      nlinarith only [hdist, mul_le_mul_of_nonneg_left hε' (show 0 ≤ (L : ℝ) by positivity)]
    have hnorm := norm_le_insert' (x p) (x j)
    rw [← dist_eq_norm_sub] at hnorm
    linarith [start_radius hp]
  let y (i : ι) := factor D (depth i) • x i
  have hpos (i : ι) : 0 < factor D (depth i) :=
    factor_pos hD1 hL (depth_le i) hε' hbudget
  have fixed {i : ι} (hi : ¬ 0 < depth i) : y i = x i := by
    have h : depth i = 0 := by omega
    simp [y, h, factor_zero]
  have close {i j : ι} (hij : nearEdge x ε i j)
      (hm : 0 < depth i ∨ 0 < depth j) : 1 ≤ dist (y i) (y j) := by
    have hj : 0 < depth j := Nat.zero_le _ |>.trans_lt (depth_lt hij hm)
    have hy := near_radius hj (show dist (x j) (x j) ≤ 1 + ε by simp; linarith)
    exact (one_lt_dist_radial_of_ordered hD (depth_lt hij hm) (hpos j)
      (hsep i j (ne_of_lt hij.1)) hy (horder i j hij)).le
  refine ⟨y, ?_, ?_⟩
  · intro i j hij
    by_cases hnear : dist (x i) (x j) ≤ 1 + ε
    · by_cases hm : 0 < depth i ∨ 0 < depth j
      · rcases lt_or_gt_of_ne hij with hlt | hlt
        · exact close ⟨hlt, hnear⟩ hm
        · rw [dist_comm]
          exact close ⟨hlt, by rwa [dist_comm]⟩ hm.symm
      · simp only [not_or] at hm
        rw [fixed hm.1, fixed hm.2]
        exact hsep i j hij
    · have hm (j : ι) : dist (y j) (x j) ≤ ε/8 :=
        displacement_le hD hL (depth_le j) hbudget (x j) (by linarith [hradius j])
      have h₁ := dist_triangle (x i) (y i) (x j)
      have h₂ := dist_triangle (y i) (y j) (x j)
      rw [dist_comm (x i) (y i)] at h₁
      linarith [hm i, hm j]
  · intro i j
    by_cases hm : 0 < depth i ∨ 0 < depth j
    · let a := factor D (depth i)
      let b := factor D (depth j)
      have hmin : a < 1 ∨ b < 1 :=
        hm.imp (factor_lt_one hD) (factor_lt_one hD)
      change dist (a • x i) (b • x j) < D
      rcases le_total a b with hab | hab
      · have ha : a < 1 := hmin.elim id (lt_of_le_of_lt hab)
        exact dist_smul_lt_of_bounds hD (hpos i).le hab (factor_le_one D _) ha
          (hdiam i j) (hradius j)
      · have hb : b < 1 := hmin.elim (lt_of_le_of_lt hab) id
        rw [dist_comm]
        exact dist_smul_lt_of_bounds hD (hpos j).le hab (factor_le_one D _) hb
          (hdiam j i) (hradius i)
    · simp only [not_or] at hm
      rw [fixed hm.1, fixed hm.2]
      refine lt_of_le_of_ne (hdiam i j) fun heq => ?_
      rcases hcover i j heq with hi | hj
      · exact hm.1 ((depth_pos i).mpr ⟨0, i, ⟨⟨j, heq⟩, hi⟩, .nil i⟩)
      · exact hm.2 ((depth_pos j).mpr ⟨0, j, ⟨⟨i, (dist_comm _ _).trans heq⟩, hj⟩, .nil j⟩)

abbrev Plane := EuclideanSpace ℝ (Fin 2)

/-- Normalize a separated strict competitor by its attained minimum distance.
This produces a competitor in the exact `HasMinDist1` domain of the pinned target. -/
theorem no_strict_replacement_of_minimal
    (A : Finset Plane) (hA : Erdos99.HasMinDist1 A)
    (hmin : IsMinOn (fun B : Finset Plane => Metric.diam (B : Set Plane))
      {B | B.card = A.card ∧ Erdos99.HasMinDist1 B} A)
    (y : A → Plane)
    (hsep : ∀ i j, i ≠ j → 1 ≤ dist (y i) (y j))
    (hstrict : ∀ i j, dist (y i) (y j) < Metric.diam (A : Set Plane)) : False := by
  classical
  obtain ⟨p, hp, q, hq, hpq⟩ := hA.2
  let i₀ : A := ⟨p, hp⟩
  let j₀ : A := ⟨q, hq⟩
  have hne : i₀ ≠ j₀ := by
    intro heq
    have he : p = q := congrArg Subtype.val heq
    simp [he] at hpq
  let pairs := (Finset.univ : Finset (A × A)).filter fun ij => ij.1 ≠ ij.2
  have hpairs : pairs.Nonempty := ⟨(i₀, j₀), by simp [pairs, hne]⟩
  obtain ⟨ij, hij, hleast⟩ :=
    Finset.exists_min_image pairs (fun ij => dist (y ij.1) (y ij.2)) hpairs
  have hijne : ij.1 ≠ ij.2 := (Finset.mem_filter.mp hij).2
  let m := dist (y ij.1) (y ij.2)
  have hm : 1 ≤ m := hsep _ _ hijne
  have hmpos : 0 < m := by positivity
  let z (i : A) := m⁻¹ • y i
  have hdist (i j : A) : dist (z i) (z j) = dist (y i) (y j) / m := by
    change dist (m⁻¹ • y i) (m⁻¹ • y j) = dist (y i) (y j) / m
    rw [dist_smul₀, Real.norm_eq_abs, abs_of_pos (inv_pos.mpr hmpos), div_eq_inv_mul]
  have hunit : dist (z ij.1) (z ij.2) = 1 := by
    rw [hdist]
    exact div_self hmpos.ne'
  have hsepz (i j : A) (hne : i ≠ j) : 1 ≤ dist (z i) (z j) := by
    rw [hdist, le_div_iff₀ hmpos, one_mul]
    exact hleast (i, j) (by simp [pairs, hne])
  have hinj : Function.Injective z := by
    intro i j heq
    by_contra hne
    have := hsepz i j hne
    rw [heq, dist_self] at this
    norm_num at this
  let B : Finset Plane := Finset.univ.image z
  have hcard : B.card = A.card := by
    change (Finset.univ.image z).card = A.card
    rw [Finset.card_image_of_injective _ hinj, Finset.card_univ, Fintype.card_coe]
  have hB : Erdos99.HasMinDist1 B := by
    constructor
    · intro u hu v hv huv
      obtain ⟨i, -, rfl⟩ := Finset.mem_image.mp hu
      obtain ⟨j, -, rfl⟩ := Finset.mem_image.mp hv
      exact hsepz i j (fun h => huv (congrArg z h))
    · exact ⟨z ij.1, by simp [B], z ij.2, by simp [B], hunit⟩
  have hzstrict (i j : A) :
      dist (z i) (z j) < Metric.diam (A : Set Plane) := by
    rw [hdist]
    exact (div_le_self dist_nonneg hm).trans_lt (hstrict i j)
  obtain ⟨ij', -, hmax⟩ := Finset.exists_max_image
    (Finset.univ : Finset (A × A)) (fun ij => dist (z ij.1) (z ij.2))
    ⟨(i₀, j₀), Finset.mem_univ _⟩
  have hBdiam : Metric.diam (B : Set Plane) < Metric.diam (A : Set Plane) := by
    refine (Metric.diam_le_of_forall_dist_le dist_nonneg ?_).trans_lt (hzstrict ij'.1 ij'.2)
    intro u hu v hv
    obtain ⟨i, -, rfl⟩ := Finset.mem_image.mp (Finset.mem_coe.mp hu)
    obtain ⟨j, -, rfl⟩ := Finset.mem_image.mp (Finset.mem_coe.mp hv)
    exact hmax (i, j) (Finset.mem_univ _)
  exact (not_lt_of_ge (hmin (show B ∈ {B | B.card = A.card ∧ Erdos99.HasMinDist1 B}
    from ⟨hcard, hB⟩))) hBdiam

/-- In the pinned Erdős #99 setting, a globally minimizing configuration has a
diameter pair from both of whose endpoints a directed near-unit path of length
`L` starts, for any order respecting the stated squared-radius bin error. -/
theorem diameter_pair_with_long_paths
    (A : Finset Plane) [LinearOrder A] (o : Plane) (ε : ℝ) (L : ℕ)
    (hA : Erdos99.HasMinDist1 A)
    (hmin : IsMinOn (fun B : Finset Plane => Metric.diam (B : Set Plane))
      {B | B.card = A.card ∧ Erdos99.HasMinDist1 B} A)
    (hε : 0 < ε) (hε' : ε ≤ 1/2) (hL : 1 ≤ L)
    (hbudget : 4096 * (L : ℝ)^2 ≤ Metric.diam (A : Set Plane) * ε)
    (hradius : ∀ i : A, ‖(i : Plane) - o‖ ≤ 9 * Metric.diam (A : Set Plane) / 10)
    (horder : ∀ i j : A, nearEdge (fun i : A => (i : Plane) - o) ε i j →
      ‖(j : Plane) - o‖^2 ≤ ‖(i : Plane) - o‖^2 + 1/16) :
    ∃ i j : A, dist (i : Plane) (j : Plane) = Metric.diam (A : Set Plane) ∧
      (∃ k, Path (nearEdge (fun i : A => (i : Plane) - o) ε) L i k) ∧
      (∃ k, Path (nearEdge (fun i : A => (i : Plane) - o) ε) L j k) := by
  classical
  let D := Metric.diam (A : Set Plane)
  let x (i : A) := (i : Plane) - o
  have hd (i j : A) : dist (x i) (x j) = dist (i : Plane) (j : Plane) :=
    dist_sub_right _ _ _
  have hdiam (i j : A) : dist (i : Plane) (j : Plane) ≤ D :=
    Metric.dist_le_diam_of_mem A.finite_toSet.isBounded i.property j.property
  have hD : 0 < D := by
    obtain ⟨p, hp, q, hq, hpq⟩ := hA.2
    have h := hdiam ⟨p, hp⟩ ⟨q, hq⟩
    change dist p q ≤ D at h
    linarith
  by_contra h
  have hcover (i j : A) (heq : dist (x i) (x j) = D) :
      (¬ ∃ k, Path (nearEdge x ε) L i k) ∨ (¬ ∃ k, Path (nearEdge x ε) L j k) := by
    rw [hd] at heq
    by_cases hi : ∃ k, Path (nearEdge x ε) L i k
    · exact Or.inr fun hj => h ⟨i, j, heq, hi, hj⟩
    · exact Or.inl hi
  have hsep (i j : A) (hne : i ≠ j) : 1 ≤ dist (x i) (x j) := by
    rw [hd]
    exact hA.1 i i.property j j.property (fun h => hne (Subtype.ext h))
  obtain ⟨y, hy, hy'⟩ := exists_replacement_of_short_path_cover x hD hε hε' hL
    hbudget hsep (fun i j => by rw [hd]; exact hdiam i j) hradius horder hcover
  exact no_strict_replacement_of_minimal A hA hmin y hy hy'

/-- Points in decreasing order of radial bin, with arbitrary ties, satisfy the
squared-radius error bound used in the replacement argument. -/
theorem squared_radius_le_of_bin_le {D r s : ℝ}
    (hD : 0 < D) (hr : 0 ≤ r) (hs : 0 ≤ s) (hrD : r ≤ D) (hsD : s ≤ D)
    (hbin : ⌊s / (1 / (32 * D))⌋ ≤ ⌊r / (1 / (32 * D))⌋) :
    s^2 ≤ r^2 + 1/16 := by
  let w : ℝ := 1 / (32 * D)
  have hw : 0 < w := by dsimp [w]; positivity
  have hbins : (⌊s / w⌋ : ℝ) ≤ (⌊r / w⌋ : ℝ) := by exact_mod_cast hbin
  have hquot : s / w < r / w + 1 := by
    linarith only [Int.lt_floor_add_one (s / w), Int.floor_le (r / w), hbins]
  have hdiff : s - r ≤ w := by
    have h := (div_lt_iff₀ hw).mp hquot
    rw [add_mul, div_mul_cancel₀ _ hw.ne', one_mul] at h
    linarith
  have hprod := mul_le_mul hdiff (show s + r ≤ 2 * D by linarith)
    (by linarith : 0 ≤ s + r) hw.le
  have hwD : w * (2 * D) = 1/16 := by
    dsimp [w]
    field_simp
    ring
  linarith only [show s^2 - r^2 ≤ w * (2 * D) by
    calc s^2 - r^2 = (s-r)*(s+r) := by ring
         _ ≤ _ := hprod, hwD]

/-- The length obtained by flooring the scale in the research note meets the
numerical budget required by the replacement theorem. -/
theorem floor_length_budget {D ε : ℝ} (hD : 0 ≤ D) (hε : 0 ≤ ε) :
    4096 * (⌊Real.sqrt (D * ε) / 64⌋₊ : ℝ)^2 ≤ D * ε := by
  have hs : 0 ≤ Real.sqrt (D * ε) / 64 := by positivity
  have h := pow_le_pow_left₀ (Nat.cast_nonneg _) (Nat.floor_le hs) 2
  nlinarith only [h, Real.sq_sqrt (mul_nonneg hD hε)]

/-- The diameter-pair conclusion with the bin width and floored path length
from the research note. The order may break ties within each bin arbitrarily. -/
theorem diameter_pair_with_binned_paths
    (A : Finset Plane) [LinearOrder A] (o : Plane) (ε : ℝ)
    (hA : Erdos99.HasMinDist1 A)
    (hmin : IsMinOn (fun B : Finset Plane => Metric.diam (B : Set Plane))
      {B | B.card = A.card ∧ Erdos99.HasMinDist1 B} A)
    (hε : 0 < ε) (hε' : ε ≤ 1/2) :
    let D := Metric.diam (A : Set Plane)
    let x (i : A) := (i : Plane) - o
    let L := ⌊Real.sqrt (D * ε) / 64⌋₊
    1 ≤ L →
    (∀ i, ‖x i‖ ≤ 9 * D / 10) →
    (∀ i j, i < j → ⌊‖x j‖ / (1 / (32 * D))⌋ ≤ ⌊‖x i‖ / (1 / (32 * D))⌋) →
    ∃ i j : A, dist (i : Plane) (j : Plane) = D ∧
      (∃ k, Path (nearEdge x ε) L i k) ∧ (∃ k, Path (nearEdge x ε) L j k) := by
  dsimp only
  intro hL hradius hbins
  let D := Metric.diam (A : Set Plane)
  let x (i : A) := (i : Plane) - o
  have hD₀ : 0 ≤ D := Metric.diam_nonneg
  have hD : 0 < D := by
    by_contra! h
    have hzero : D = 0 := le_antisymm h hD₀
    change 1 ≤ ⌊Real.sqrt (D * ε) / 64⌋₊ at hL
    simp [hzero] at hL
  refine diameter_pair_with_long_paths A o ε _ hA hmin hε hε' hL
    (floor_length_budget hD₀ hε.le) hradius ?_
  intro i j hij
  have hr (i : A) : ‖x i‖ ≤ D := by linarith [hradius i]
  exact squared_radius_le_of_bin_le hD (norm_nonneg _) (norm_nonneg _)
    (hr i) (hr j) (hbins i j hij.1)

end Contribution.Erdos99.Radial
