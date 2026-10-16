#!/usr/bin/env python3
import math
import random

H_STAR = math.sqrt(303.0) / 52.0
C_STAR = 0.129220199818177
DELTA_STAR = 2.0 * (1.0 - math.cos(C_STAR / 2.0))
A0 = math.sqrt(3.0) / 2.0
C_POCKET = 8.0 / (math.pi * math.sqrt(3.0))


def nu(K: float) -> float:
    return 1.0 + DELTA_STAR * (1.0 - H_STAR / K) / 4.0


def x_floor(K: float) -> float:
    return math.sqrt(nu(K) / C_POCKET)


def detour_product(K: float) -> float:
    return (2.0 * A0 * nu(K) / math.pi) ** 2


def check_width_ledger() -> None:
    # Synthetic monotone visits to convex-pocket projection intervals.
    rng = random.Random(0xE99)
    for _ in range(10000):
        x = rng.uniform(0.01, 100.0)
        # total pocket perimeter P <= 4x, width_i <= P_i/2
        parts = [rng.random() for _ in range(rng.randint(1, 20))]
        s = sum(parts)
        perims = [4.0 * x * p / s for p in parts]
        widths = [0.5 * p * rng.random() for p in perims]
        assert sum(widths) <= 2.0 * x + 1e-10

        # A monotone run can visit each pocket in disjoint projection intervals.
        total_progress = 0.0
        for w in widths:
            cuts = sorted(rng.random() * w for _ in range(rng.randint(0, 8)))
            pts = [0.0] + cuts + [w]
            # choose a disjoint subcollection of alternate intervals
            contrib = sum(pts[j + 1] - pts[j] for j in range(0, len(pts) - 1, 2))
            assert contrib <= w + 1e-12
            total_progress += contrib
        assert total_progress <= 2.0 * x + 1e-10


def check_nonlinear_outer_currency() -> None:
    # Abstractly verify the implication
    # O = Z + H/a0 - u/2 >= B + U/2,
    # H <= 4x^2/pi, u>=0
    # => Z + C_POCKET x^2 >= B + U/2.
    rng = random.Random(0xC0FFEE)
    for _ in range(200000):
        x = rng.random() * 100.0
        Hmax = 4.0 * x * x / math.pi
        H = rng.random() * Hmax
        Z = rng.random() * 100.0
        u = rng.random() * 10.0
        O = Z + H / A0 - u / 2.0
        U = rng.random() * 10.0
        B = O - U / 2.0 - rng.random() * 10.0
        if B + U / 2.0 <= O + 1e-12:
            lhs = Z + C_POCKET * x * x
            assert lhs + 1e-10 >= B + U / 2.0


def check_routing_ledger() -> None:
    # Synthetic finite routing inequality:
    # G_low <= 2 x (U+1) + 2(1+t) Z.
    rng = random.Random(0xBAD5EED)
    for _ in range(100000):
        x = rng.uniform(0.0, 50.0)
        Z = rng.randint(0, 100)
        U = rng.randint(0, Z)
        t = rng.uniform(0.0, H_STAR + 0.01)
        # Internal progress: each of U+1 runs gets <=2x.
        internal = sum(rng.random() * 2.0 * x for _ in range(U + 1))
        # External-adjacent lower edges: at most 2Z, each gain <=1+t.
        m = rng.randint(0, 2 * Z) if Z else 0
        external = sum(rng.random() * (1.0 + t) for _ in range(m))
        G = internal + external
        assert G <= 2.0 * x * (U + 1) + 2.0 * (1.0 + t) * Z + 1e-10


def check_sqrt_frontier() -> None:
    # Leading-order constraints in the x=xi sqrt(D), Z=zeta sqrt(D),
    # u=eta sqrt(D) window:
    # C_POCKET xi^2 >= nu; 2 xi zeta >=1;
    # xi^3 eta >= detour_product.
    for K in (1.0, 400.0, 1e9):
        n = nu(K)
        xi0 = x_floor(K)
        zeta0 = 1.0 / (2.0 * xi0)
        eta0 = detour_product(K) / (xi0 ** 3)
        assert abs(C_POCKET * xi0 * xi0 - n) < 1e-12
        assert abs(2.0 * xi0 * zeta0 - 1.0) < 1e-12
        assert abs((xi0 ** 3) * eta0 - detour_product(K)) < 1e-12

        # Since xi0>1/sqrt(2), xi+1/(2xi) is increasing for xi>=xi0.
        assert xi0 > 1.0 / math.sqrt(2.0)
        for j in range(1, 10000):
            xi = xi0 + j / 1000.0
            assert xi + 1.0 / (2.0 * xi) >= xi0 + zeta0 - 1e-12


def main() -> None:
    check_width_ledger()
    check_nonlinear_outer_currency()
    check_routing_ledger()
    check_sqrt_frontier()

    for K in (1.0, 400.0):
        xf = x_floor(K)
        zf = 1.0 / (2.0 * xf)
        df = detour_product(K)
        ef = df / (xf ** 3)
        print(f"K={K:g}: nu={nu(K):.15f}")
        print(f"K={K:g}: x/sqrt(D) floor={xf:.15f}")
        print(f"K={K:g}: paired Z/sqrt(D) floor at x-floor={zf:.15f}")
        print(f"K={K:g}: x+Z sqrt coefficient={xf+zf:.15f}")
        print(f"K={K:g}: x^3*u / D^2 floor={df:.15f}")
        print(f"K={K:g}: u/sqrt(D) floor at x-floor={ef:.15f}")

    nu_inf = 1.0 + DELTA_STAR / 4.0
    x_inf = math.sqrt(nu_inf / C_POCKET)
    z_inf = 1.0 / (2.0 * x_inf)
    det_inf = (2.0 * A0 * nu_inf / math.pi) ** 2
    eta_inf = det_inf / x_inf ** 3
    print(f"nu_inf={nu_inf:.15f}")
    print(f"x_inf={x_inf:.15f}")
    print(f"z_at_x_inf={z_inf:.15f}")
    print(f"sum_inf={x_inf+z_inf:.15f}")
    print(f"detour_product_inf={det_inf:.15f}")
    print(f"eta_at_x_inf={eta_inf:.15f}")
    print("PASS: FREE pocket-width routing and outerwalk currency arithmetic/regression")


if __name__ == "__main__":
    main()
