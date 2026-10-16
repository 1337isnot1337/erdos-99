from fractions import Fraction as F
from math import isqrt

# Exact rational certificate for the general post-ZF mu >= 0.5947 report.
#
# Proposition tested:
#   In the full post-ZF C-II class (no assumption s_Z=0), the combined
#   generalized renormalized-surplus inequality, FSDB/ZK force-gap bound,
#   DD outer-pocket bound, exceptional-face estimate, and ZG charging theorem
#   admit no unbounded survivor sequence with
#
#       mu=(e_BB+2*s_C-3*(d_H+s_Z))/D <= 0.5947.
#
# Encoded assumptions:
#   * audited rational pi and rho barriers from E597;
#   * the generalized RSJ fixed-y minimization proved in the adjacent report;
#   * FSDB: area(F)/D^2 >= Phi(y)+o(1);
#   * ZK: attachment area <= pi*mu^2*D^2/4+o(D^2);
#   * DD and the exact post-ZF identities implying
#         Q/D <= delta=2y-p,
#         (b-P_F)/D <= delta,
#         (x_B+a)/D <= 2y;
#   * exceptional-face area <= Q^2/(4*pi)+o(D^2);
#   * ZG: G <= H_out+A_exc+o(D^2).
#
# Omitted assumptions:
#   This script does not prove the named geometric inputs, KKT normalization,
#   global optimality, or the generalized fixed-y calculus. Those are proved or
#   audited in the theorem reports. It certifies only the finite rational
#   inequalities used in the final localization/capacity contradiction.
#
# Arithmetic:
#   fractions.Fraction and integer square-root checks only. Floating-point
#   conversions appear only in printed diagnostics after every assertion passes.
#
# A PASS proves:
#   the 465-cell rational certificate has strictly positive localization and
#   cavity-capacity margins throughout the full possible y interval.
#
# A PASS does NOT prove:
#   Level I, a contradictory upper bound on mu, or the theorem dependencies
#   listed above.

PI_LO = F(6283, 2000)          # PI_LO < pi
PI_HI = F(3927, 1250)          # pi < PI_HI
PI_CRUDE_HI = F(22, 7)         # pi < 22/7
INV4PI_HI = F(500, 6283)       # 1/(4*pi) < 500/6283
DD_C = F(1633, 4000)           # > 1/sqrt(6)

U0 = F(5947, 10000)            # candidate excluded mu
Y_MIN = F(739, 500)            # 1.478 < 2*rho
Y_MAX = F(3049, 2000)          # 1.5245
Y_STEP = F(1, 10000)
D_DEN = 100000                  # detour barriers to 1e-5
SQ_DEN = 1000000               # sqrt upper barriers to 1e-6


def phi_lower(y: F) -> F:
    """Rigorous rational lower bound for Phi(y)=(y+sin(y))/4."""
    # y<pi/2. With z=pi/2-y and pi/2<11/7,
    # z < 11/7-y. Since cos z >= 1-z^2/2,
    # sin y=cos z > 1-(11/7-y)^2/2.
    z_up = F(11, 7) - y
    assert z_up >= 0
    return (y + 1 - z_up * z_up / 2) / 4


def j_upper(u: F, m: F) -> F:
    """Rigorous rational upper bound for J_u(m)."""
    # J_u(m)=pi*u^2/4+(u+m)^2/(4*pi).
    return PI_HI * u * u / 4 + INV4PI_HI * (u + m) * (u + m)


def ceil_sqrt_fraction(x: F, den: int) -> F:
    """Least k/den whose square is at least x, computed exactly."""
    target = x.numerator * den * den
    d = x.denominator
    q = (target + d - 1) // d
    k = isqrt(q)
    while k * k * d < target:
        k += 1
    while k > 0 and (k - 1) * (k - 1) * d >= target:
        k -= 1
    out = F(k, den)
    assert out * out >= x
    return out


# Basic constant certificates.
assert PI_LO < PI_HI < PI_CRUDE_HI
assert DD_C * DD_C * 6 - 1 == F(67, 8000000)

# The generalized fixed-y threshold is increasing for y>=y_R.  The adjacent
# proof reduces y<Y_MAX to checking that the optimal crossover perimeter at
# Y_MAX still requires mu>U0.  We certify that check here.
#
# c_R=pi/(pi-2)^2. The function x/(x-2)^2 decreases on x>2, so pi<PI_HI gives
# c_R > c_r_lower below.
c_r_lower = PI_HI / (PI_HI - 2) ** 2

# Upper-bound Phi(Y_MAX) using a positive lower bound on
# z=pi/2-Y_MAX and the alternating cosine polynomial.
z_low = PI_LO / 2 - Y_MAX
assert 0 < z_low < 1
sin_upper = 1 - z_low * z_low / 2 + z_low ** 4 / 24
phi_upper_ymax = (Y_MAX + sin_upper) / 4

# At the crossover, p_e/2=1+sqrt(Phi/c_R).  The exact comparison below gives
# sqrt(Phi/c_R)<0.5116, hence p_e/2<1.5116.
s_bar = F(2558, 5000)          # 0.5116
assert phi_upper_ymax / c_r_lower < s_bar * s_bar
m_e_upper = 1 + s_bar

ymax_rsj_margin = phi_lower(Y_MAX) - j_upper(U0, m_e_upper)
assert ymax_rsj_margin > 0

# This same p_e bound gives p_e<3.0232<2*Y_MAX=3.049, so Y_MAX is above the
# unique RSJ crossover y_R.
assert 2 + 2 * s_bar < 2 * Y_MAX

# For detour localization define
#   F_d(y)=J_U0(y-d/2)-Phi(y).
# On the whole certified range, d<=0.026 and
#   F_d'(y)=(U0+y-d/2)/(2*pi)-(1+cos y)/4.
# Since cos y<0.1 and 1/(2*pi)>7/44, the displayed rational number is a
# uniform positive derivative lower bound.
D_GLOBAL = F(13, 500)          # 0.026
zmax = F(11, 7) - Y_MIN
assert 0 < zmax < F(1, 10)
derivative_lower = (
    (U0 + Y_MIN - D_GLOBAL / 2) * F(7, 44) - F(11, 40)
)
assert derivative_lower == F(23179, 440000)
assert derivative_lower > 0

cells = []
left = Y_MIN
while left < Y_MAX:
    right = min(left + Y_STEP, Y_MAX)

    # Choose dbar so J_U0(right-dbar/2)<Phi(right).  Monotonicity of F_d
    # then shows every feasible state in this cell has delta=2y-p<dbar.
    k = 0
    while True:
        dbar = F(k, D_DEN)
        if j_upper(U0, right - dbar / 2) < phi_lower(right):
            break
        k += 1
        if k > 10000:
            raise RuntimeError("detour search failed")
    assert dbar <= D_GLOBAL
    localization_margin = phi_lower(right) - j_upper(
        U0, right - dbar / 2
    )
    assert localization_margin > 0

    # DD + Q/D<=delta + (b-P_F)/D<=delta + (x_B+a)/D<=2y:
    #   H_out/D^2 <= (1/sqrt6)(2y)^(3/2)sqrt(delta),
    #   A_exc/D^2 <= delta^2/(4*pi).
    # Rewrite (2 right)^(3/2)sqrt(dbar)
    #          =(2 right)*sqrt(2 right dbar).
    root_up = ceil_sqrt_fraction(2 * right * dbar, SQ_DEN)
    h_out_up = DD_C * (2 * right) * root_up
    cavity_up = h_out_up + INV4PI_HI * dbar * dbar

    # FSDB - ZK gives
    #   G/D^2 >= Phi(y)-pi*mu^2/4.
    gap_low = phi_lower(left) - PI_HI * U0 * U0 / 4
    capacity_margin = gap_low - cavity_up
    assert capacity_margin > 0

    cells.append(
        (left, right, dbar, root_up, localization_margin, capacity_margin)
    )
    left = right

assert len(cells) == 465
worst_local = min(cells, key=lambda row: row[4])
worst_capacity = min(cells, key=lambda row: row[5])

# Lock the exact margins quoted in the report.
assert worst_local[0] == F(3753, 2500)        # 1.5012
assert worst_local[1] == F(15013, 10000)      # 1.5013
assert worst_local[2] == F(321, 20000)        # 0.01605
assert worst_local[4] == F(127118647, 76966750000000000)

assert worst_capacity[0] == F(3811, 2500)     # 1.5244
assert worst_capacity[1] == F(3049, 2000)     # 1.5245
assert worst_capacity[2] == F(2567, 100000)   # 0.02567
assert worst_capacity[3] == F(69941, 250000)  # 0.279764
assert worst_capacity[5] == F(
    1466294867848439, 307867000000000000
)

print("PASS: exact rational general-mu 0.5947 certificate")
print("cells =", len(cells))
print("ymax RSJ margin =", ymax_rsj_margin)
print("ymax RSJ margin decimal =", float(ymax_rsj_margin))
print("derivative lower bound =", derivative_lower)
print("derivative lower bound decimal =", float(derivative_lower))
print("worst localization cell =", worst_local[0], worst_local[1])
print("  dbar =", worst_local[2])
print("  exact localization margin =", worst_local[4])
print("  decimal localization margin =", float(worst_local[4]))
print("worst capacity cell =", worst_capacity[0], worst_capacity[1])
print("  dbar =", worst_capacity[2])
print("  sqrt upper =", worst_capacity[3])
print("  exact capacity margin =", worst_capacity[5])
print("  decimal capacity margin =", float(worst_capacity[5]))
