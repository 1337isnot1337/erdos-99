#!/usr/bin/env python3
"""Arithmetic regression for matched g=0.0050 low-t and bridge/pentagon split."""
from decimal import Decimal as D, getcontext
getcontext().prec = 80
PI = D('3.141592653589793238462643383279502884197169399375105820974944')
S = (PI / (D(2) * D(3).sqrt())).sqrt()
G = D('0.0050')
EPS = D('0.0023374')
C146 = D(4) * (PI + S) / D(9)
t = C146 + EPS
C0 = D(2) * S + G
r = D('4.5') * EPS - G
delta = r / D(2)
kappa = D(2) * r
assert delta == D('0.00275915')
assert kappa == D('0.01103660')

J = t + D(2) * C0 - PI
H = J / D(2) + t - PI / D(2)
f_floor = C0 / D(2) - t / D(4)
x_cap = D('2.25') * t - PI - C0 / D(2)
p5 = PI + C0 - D('2.5') * t
rank5 = D(2) * p5 - kappa
loo = D(3) * PI - D(5) * t
tooth_one = (D(5) * PI + D(2) * C0 - D(10) * t) / D(3)
pen = (tooth_one - delta / D('0.02')) / D(4)
residual_cap = D('1.5') * PI - t

L = t + D(2) * G
bridge_net = L - delta
bridge_sigma = bridge_net / D(2)
bridge_SE = bridge_net / D(4)

# S_E <= S_5 + 6(Q-f), hence sigma_R + 2S_5 >= L-delta-12(Q-f).
pent_net = L - delta - D(12) * x_cap
pent_sigma = pent_net / D(2)
pent_S5 = pent_net / D(4)
anchored = pent_S5 / D(65)
off_window = pent_S5 / D(10)
MR = pent_sigma / D(8) * (D(4) * S + pent_sigma / D(2))

# Overlay from the matched flat-center unloading algebra.
U = D(2) * PI + D(3) * S + D('1.5') * G - D(5) * t
U_positive_through = (D(2) * PI + D(3) * S + D('1.5') * G) / D(5)
H4 = U / D(9)
E3 = U / D(4)
cdf = S - PI / D(4) + D('2.5') * G
leaf_gate = L - D(8) * x_cap - D(4) * t + D(2) * PI

assert abs(x_cap - delta) < D('1e-70')
assert D('1.82185093') < t < D('1.82185095')
assert D('2.49950') < J < D('2.49952')
assert D('1.50080') < H < D('1.50082')
assert D('0.49934') < f_floor < D('0.49936')
assert D('0.49658') < p5 < D('0.49660')
assert D('0.98214') < rank5 < D('0.98216')
assert D('0.31552') < loo < D('0.31553')
assert D('0.43623') < tooth_one < D('0.43624')
assert D('0.07456') < pen < D('0.07458')
assert D('2.89053') < residual_cap < D('2.89055')
assert D('1.83185') < L < D('1.83186')
assert D('0.91454') < bridge_sigma < D('0.91455')
assert D('0.45727') < bridge_SE < D('0.45728')
assert D('1.79598') < pent_net < D('1.79599')
assert D('0.89799') < pent_sigma < D('0.89800')
assert D('0.44899') < pent_S5 < D('0.44900')
assert D('0.00690') < anchored < D('0.00692')
assert D('0.04489') < off_window < D('0.04491')
assert D('0.477') < MR < D('0.479')
assert D('0.03836') < U < D('0.03838')
assert D('1.82952') < U_positive_through < D('1.82953')
assert D('0.00426') < H4 < D('0.00427')
assert D('0.00959') < E3 < D('0.00960')
assert D('0.17941') < cdf < D('0.17942')
assert D('0.80555') < leaf_gate < D('0.80557')

for name, value in [
    ('s', S), ('t50', t), ('detour_cap', delta), ('kappa_cap', kappa),
    ('J_floor', J), ('H_floor', H), ('f_floor', f_floor), ('Q_minus_f_cap', x_cap),
    ('p5_floor', p5), ('pentagon_closure_rank_floor', rank5), ('L_OO_floor', loo),
    ('tooth_or_longside_floor', tooth_one), ('shallow_tooth_penetration_floor_eta002', pen),
    ('residual_cap', residual_cap), ('train_defect_floor', L),
    ('bridge_sigma_branch', bridge_sigma), ('bridge_SE_branch', bridge_SE),
    ('pentagon_currency_floor', pent_net), ('pentagon_sigma_branch', pent_sigma),
    ('pentagon_S5_branch', pent_S5), ('singleton_anchored_triangle_floor', anchored),
    ('two_window_off_floor', off_window), ('rhombic_Mantel_floor', MR),
    ('unloaded_flat_center_floor', U), ('unloaded_positive_through_t', U_positive_through),
    ('H4_floor', H4), ('E3_floor', E3), ('detour_free_constant', cdf),
    ('leaf_gate', leaf_gate),
]:
    print(name, '=', value)
print('PASS matched g=0.0050 low-t / bridge split arithmetic')
