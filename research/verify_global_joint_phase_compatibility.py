#!/usr/bin/env python3
"""Exact algebra for the formal global stress/strain phase mechanism.

No source configurations, global minimizers, continuum extraction, or Level I
closure are certified. See the accompanying unreviewed report for that gap.
"""

import sys

if not __debug__:
    raise SystemExit('Refusing optimized Python: exact assertions must execute')

import sympy as sp


def product(a, b):
    return sp.simplify(sum(a[i, j] * b[i, j]
                           for i in range(2) for j in range(2)))


def main():
    root3 = sp.sqrt(3)
    directions = [sp.Matrix([1, 0]), sp.Matrix([sp.Rational(1, 2), root3 / 2]),
                  sp.Matrix([-sp.Rational(1, 2), root3 / 2])]
    axes = [u * u.T for u in directions]
    dual = [sp.diag(1, -sp.Rational(1, 3)),
            sp.Matrix([[0, 1 / root3], [1 / root3, sp.Rational(2, 3)]]),
            sp.Matrix([[0, -1 / root3], [-1 / root3, sp.Rational(2, 3)]])]
    for i in range(3):
        for j in range(3):
            assert product(axes[i], dual[j]) == int(i == j)
        assert dual[i].trace() == sp.Rational(2, 3)

    opening = sp.symbols("t0:3", positive=True)
    coefficients = [[sp.Symbol(f"a{i}{j}", positive=True) if i != j else 0
                     for j in range(3)] for i in range(3)]
    stress = [sum((coefficients[i][j] * axes[j] for j in range(3)), sp.zeros(2))
              for i in range(3)]
    spin = sp.symbols('w0:3', real=True)
    strain = [opening[i] * dual[i] + sp.Matrix([[0, -spin[i]], [spin[i], 0]])
              for i in range(3)]
    for i in range(3):
        assert product(stress[i], strain[i]) == 0
        for j in range(i + 1, 3):
            value = product(stress[i] - stress[j], strain[i] - strain[j])
            expected = -coefficients[i][j] * opening[j] - coefficients[j][i] * opening[i]
            assert sp.simplify(value - expected) == 0
            assert sp.simplify(-value).is_positive

    # A stress-only rank-one laminate has mean I and strictly positive phase weights.
    a = sp.Rational(5, 3) * axes[0] + sp.Rational(8, 3) * axes[1]
    b = sp.Rational(1, 3) * axes[0] + sp.Rational(8, 9) * axes[2]
    jump = a - b
    normal = sp.Matrix([-root3, 2])
    assert jump.rank() == 1 and jump.det() == 0
    assert sp.simplify(jump * normal) == sp.zeros(2, 1)
    assert sp.simplify(a / 4 + 3 * b / 4) == sp.eye(2)
    assert a.det() > 0 and b.det() > 0
    assert a.det() == sp.Rational(10, 3) and b.det() == sp.Rational(2, 9)
    vector = sp.Matrix([2, root3])
    assert sp.simplify(jump - sp.Rational(4, 9) * vector * vector.T) == sp.zeros(2)
    assert sp.simplify(a.det() / 4 + 3 * b.det() / 4) == 1
    paired = product(jump, dual[2] - dual[1])
    assert paired == -sp.Rational(32, 9)

    # Independently rotated grain frames admit a jointly compatible laminate.
    rotation = sp.Matrix([[root3 / 2, sp.Rational(1, 2)],
                          [-sp.Rational(1, 2), root3 / 2]])
    common_stress = 2 * axes[1] + axes[2]
    rotated_stress = rotation * (axes[1] + 2 * axes[2]) * rotation.T
    assert sp.simplify(rotated_stress - common_stress) == sp.zeros(2)
    skew = sp.Matrix([[0, -sp.Rational(2, 3)], [sp.Rational(2, 3), 0]])
    fa = dual[0]
    fb = sp.simplify(rotation * dual[0] * rotation.T - skew)
    normal = sp.Matrix([1, root3 - 2])
    amplitude = sp.Matrix([sp.Rational(1, 3), (root3 + 2) / 3])
    assert sp.simplify(fa - fb - amplitude * normal.T) == sp.zeros(2)
    assert (fa - fb).rank() == 1
    assert product(common_stress, fa) == product(common_stress, fb) == 0
    # Independent finite double-integral identity, including nonzero boundary
    # work: two phases with arbitrary weights need not meet curl/div conditions.
    fraction = sp.symbols('fraction', real=True)
    s_mean = fraction * stress[0] + (1 - fraction) * stress[1]
    f_mean = fraction * strain[0] + (1 - fraction) * strain[1]
    boundary_work = (fraction * product(stress[0], strain[0])
                     + (1 - fraction) * product(stress[1], strain[1])
                     - product(s_mean, f_mean))
    ordered_product = (2 * fraction * (1 - fraction)
                       * product(stress[0] - stress[1], strain[0] - strain[1]))
    assert sp.simplify(ordered_product - 2 * boundary_work) == 0
    # A wrong cross-phase coefficient must disagree with the independent work.
    assert sp.simplify(ordered_product - boundary_work) != 0
    print("PASS: 9 exact dual-basis pairings; all phase opening traces = 2/3")
    print("PASS: all 3 symbolic cross-phase pairings are strictly negative")
    print("PASS: positive stress-only rank-one laminate has mean I and determinant mean 1")
    print("PASS: that laminate's paired strain/stress jump has product -32/9")
    print("PASS: 30-degree rotated positive phases have common stress and compatible rank-one strain jump")
    print("PASS: arbitrary skew parts cancel; exact two-phase boundary-work identity and false-factor control")
    print("Scope: formal matrix algebra only; no physical source extraction or global optimality.")


if __name__ == "__main__":
    main()
