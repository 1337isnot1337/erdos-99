from fractions import Fraction as F
from math import isqrt

# Exact rational certificate for the E5981 Target C report.
#
# Proposition tested:
#   In the post-ZF s_Z=0 circuit phase, the combined RSJ, FSDB, ZK, DD,
#   exceptional-face, and ZG inequalities admit no unbounded survivor sequence
#   with
#       nu=(e_BB+2*s_C-3*d_H)/D <= 0.5981.
#
# Encoded assumptions:
#   * E597's audited rational pi barriers and rho>0.739;
#   * RSJ's analytic one-variable minimization and monotonicity of r_+(y);
#   * FSDB area(F)/D^2 >= Phi(y) asymptotically;
#   * ZK attachment-cell area <= pi*nu^2*D^2/4+o(D^2);
#   * DD outer-pocket bound, Q/D <= 2y-p, and x_B+a <= 2h;
#   * exceptional-face area <= Q^2/(4*pi)+o(D^2);
#   * ZG: G <= H_out+A_exc+o(D^2).
#
# Omitted assumptions:
#   The script does not prove any of the named geometric/theorem inputs above.
#   It certifies only the finite rational inequalities used to combine them.
#
# Arithmetic:
#   fractions.Fraction and integer square-root checks only. No floating-point
#   value participates in any assertion. Decimal output is diagnostic.
#
# A PASS proves:
#   the 470-cell rational certificate in the accompanying report has positive
#   localization and area-capacity margins on the full normalized y-range.
#
# A PASS does NOT prove:
#   Level I, the s_Z>0 phase, or any global upper bound on nu.

PI_LO = F(6283, 2000)          # PI_LO < pi
PI_HI = F(3927, 1250)          # pi < PI_HI
PI_CRUDE_HI = F(22, 7)         # pi < 22/7
INV4PI_HI = F(500, 6283)       # 1/(4*pi) < 500/6283
DD_C = F(1633, 4000)           # > 1/sqrt(6)

U0 = F(5981, 10000)            # candidate excluded nu
Y_MIN = F(739, 500)            # 1.478 < 2*rho
Y_MAX = F(61, 40)              # 1.525
Y_STEP = F(1, 10000)
D_DEN = 100000                  # delta barriers to 1e-5
SQ_DEN = 1000000               # sqrt upper barriers to 1e-6


def phi_lower(y: F) -> F:
    """Rigorous rational lower bound for Phi(y)=(y+sin(y))/4."""
    # Here y<pi/2.  With z=pi/2-y,
    #   z < 11/7-y = z_up,
    # and cos(z) >= 1-z^2/2.  Hence
    #   sin(y)=cos(z) > 1-z_up^2/2.
    z_up = F(11, 7) - y
    assert z_up >= 0
    return (y + 1 - z_up * z_up / F(2, 1)) / 4


def j_upper(u: F, m: F) -> F:
    """Rigorous rational upper bound for J_u(m)."""
    # J_u(m)=pi*u^2/4+(u+m)^2/(4*pi).
    return PI_HI * u * u / 4 + INV4PI_HI * (u + m) * (u + m)


def ceil_sqrt_fraction(x: F, den: int) -> F:
    """Return the least k/den whose square is at least x, exactly."""
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
assert DD_C * DD_C * 6 > 1
assert PI_LO < PI_HI < PI_CRUDE_HI

# c_R=pi/(pi-2)^2 decreases for pi>2.  Since pi<PI_HI,
# c_R > PI_HI/(PI_HI-2)^2 > 2.41.
c_r_at_pi_hi = PI_HI / (PI_HI - 2) ** 2
assert c_r_at_pi_hi > F(241, 100)

# At y=1.525, Phi(y)<(y+1)/4.  The preceding c_R lower bound gives
# sqrt(Phi/c_R)<0.512, hence p_e<3.024 and m_e=p_e-y<1.499.
phi_upper_ymax = (Y_MAX + 1) / 4
assert phi_upper_ymax / F(241, 100) < F(64, 125) ** 2
m_e_upper = F(1499, 1000)

# With nu=0.5981, even that enlarged m is RSJ-infeasible at y=1.525.
ymax_rsj_margin = phi_lower(Y_MAX) - j_upper(U0, m_e_upper)
assert ymax_rsj_margin > 0

# E597 proves y_R<1.523.  RSJ proves r_+(y) strictly increasing for y>=y_R.
# Thus the preceding strict check implies any state with nu<=U0 has y<1.525.

# Uniform monotonicity for the detour localization.
# F_d(y)=J_U0(y-d)-Phi(y) has derivative
#   (U0+y-d)/(2*pi) - (1+cos y)/4.
# For y>=1.478 and d<=0.026, pi<22/7 and cos y<0.1, since
# 0<pi/2-y<11/7-1.478<0.1.
D_GLOBAL = F(13, 500)  # 0.026
zmax = F(11, 7) - Y_MIN
assert 0 < zmax < F(1, 10)
derivative_lower = (U0 + Y_MIN - D_GLOBAL) * F(7, 44) - F(11, 40)
assert derivative_lower > 0

cells = []
left = Y_MIN
while left < Y_MAX:
    right = min(left + Y_STEP, Y_MAX)

    # Find dbar with J_U0(right-dbar)<Phi(right).  Since F_d increases
    # with y, every feasible state in this cell must have delta<dbar.
    k = 0
    while True:
        dbar = F(k, D_DEN)
        if j_upper(U0, right - dbar) < phi_lower(right):
            break
        k += 1
        if k > 10000:
            raise RuntimeError("delta search failed")
    assert dbar <= D_GLOBAL
    localization_margin = phi_lower(right) - j_upper(U0, right - dbar)
    assert localization_margin > 0

    # DD and Q/D<=delta:
    #   H_out/D^2 <= (1/sqrt6)(2y)^(3/2)sqrt(delta),
    #   A_exc/D^2 <= delta^2/(4*pi).
    # Also (2 right)^(3/2)sqrt(dbar)
    #      =(2 right)*sqrt(2 right dbar).
    root_up = ceil_sqrt_fraction(2 * right * dbar, SQ_DEN)
    h_out_up = DD_C * (2 * right) * root_up
    cavity_up = h_out_up + INV4PI_HI * dbar * dbar

    # FSDB - ZK gives
    #   G/D^2 >= Phi(y)-pi*nu^2/4.
    gap_low = phi_lower(left) - PI_HI * U0 * U0 / 4
    capacity_margin = gap_low - cavity_up
    assert capacity_margin > 0

    cells.append(
        (left, right, dbar, root_up, localization_margin, capacity_margin)
    )
    left = right

worst_local = min(cells, key=lambda row: row[4])
worst_capacity = min(cells, key=lambda row: row[5])

print("PASS: exact rational E5981 certificate")
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
