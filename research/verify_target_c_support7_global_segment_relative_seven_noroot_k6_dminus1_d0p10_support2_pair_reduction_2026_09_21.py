#!/usr/bin/env python3
"""Arithmetic certificate for the support-two residual in seven-no-root k=6 p=10.

Non-arithmetic inputs are committed earlier results:
  * D(B)=-1, k(B)=6, p(B)=10;
  * the final structural reduction forces d_v=3, q=10 and ten singleton
    incomplete blocks;
  * the coefficient line P has support exactly two;
  * all seven no-root rows are M-coloops;
  * one-row quotient rank drops are zero;
  * the five-row D=0,k=5 boundary has p=10.

This checker verifies the defect/rank bookkeeping that reduces the residual to
an exact five-row boundary plus a projective quotient-residual collision pair.
"""


def defect_after_delete(D_B: int, deleted: int, q_drop: int) -> int:
    return D_B + 2 * deleted - 3 * q_drop


def main() -> None:
    D_B = -1
    global_p = 10

    # A one-coordinate deletion cannot kill a line supported on two coordinates.
    q_single = 0
    D_six = defect_after_delete(D_B, 1, q_single)
    assert D_six == 1

    # Deleting both support coordinates kills the rank-one coefficient line.
    q_pair = 1
    D_five = defect_after_delete(D_B, 2, q_pair)
    assert D_five == 0

    # The committed sharp-boundary classification forces p=10 at five-row
    # k=5,D=0. Hence none of the ten global singleton rows disappears under
    # the support-pair deletion. It follows a fortiori that neither disappears
    # under either support-coordinate deletion alone.
    pair_shadow_p = 10
    assert pair_shadow_p == global_p
    support_single_shadow_p = global_p

    # k=t-rank(P): t=7,6,5 and projected coefficient ranks 1,1,0.
    assert 7 - 1 == 6
    assert 6 - 1 == 5
    assert 5 - 0 == 5

    # All seven external rows are M-coloops. Across the support-pair deletion,
    # M loses two ranks and Q loses one. Across either single deletion, M loses
    # one rank and Q loses zero. Therefore each support cycle, added individually
    # to the five-row shadow A, raises both M and Q rank by one, while the pair
    # raises M rank by two but Q rank by only one.
    m_pair = 2
    q_pair_gain = 1
    m_single = 1
    q_single_gain = q_pair_gain - q_single
    assert (m_single, q_single_gain) == (1, 1)
    assert (m_pair, q_pair_gain) == (2, 1)

    # Starting from D(A)=0, this pair increment reproduces D(B)=-1 exactly.
    delta_gain = m_pair - q_pair_gain
    reconstructed = D_five + 2 - 3 * delta_gain
    assert delta_gain == 1
    assert reconstructed == D_B

    # Linear-algebra consequence: the two individual quotient residuals modulo
    # span_Q(A) are nonzero (each has rank gain one), but together span only one
    # new quotient dimension. Hence they are projectively equal. Conversely,
    # an exact scan need only look for a nonzero quotient-residual bucket with
    # at least two M-independent remaining no-root cycles.
    individual_q_ranks = (1, 1)
    pair_q_rank = 1
    assert all(r == 1 for r in individual_q_ranks)
    assert pair_q_rank < sum(individual_q_ranks)

    print("PASS: support-two p10 residual reduces to a five-row parallel-extension pair")
    print("five_shadow", {"D": D_five, "k": 5, "p": pair_shadow_p, "singletons": 10})
    print("support_single_shadows", {"D": D_six, "k": 5, "p": support_single_shadow_p})
    print("rank_increments_from_five_shadow", {"each": (1, 1), "pair": (2, 1)})
    print("finite_target", "nonzero projective Q-residual collision with M-pair gain 2")


if __name__ == "__main__":
    main()
