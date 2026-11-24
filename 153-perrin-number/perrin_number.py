"""
Problem 153: Perrin Number Sequence
Description:
P(0) = 3, P(1) = 0, P(2) = 2
P(n) = P(n-2) + P(n-3) for n >= 3.
"""

def perrin_sequence(n: int) -> list[int]:
    """Generates the first n Perrin numbers."""
    if n <= 0:
        return []
    base = [3, 0, 2]
    if n <= 3:
        return base[:n]
    seq = [3, 0, 2]
    for _ in range(3, n):
        seq.append(seq[-2] + seq[-3])
    return seq


def perrin_ratio_convergence(n: int) -> float:
    """
    Computes the ratio P(n) / P(n-1) which converges to the plastic ratio:
    psi ≈ 1.324717957244746...
    """
    seq = perrin_sequence(n + 1)
    if len(seq) < 2 or seq[-2] == 0:
        return 0.0
    return seq[-1] / seq[-2]


if __name__ == "__main__":
    seq = perrin_sequence(15)
    expected = [3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, 51]
    assert seq == expected

    # Ratio approaches plastic constant ~ 1.3247
    ratio_35 = perrin_ratio_convergence(35)
    assert abs(ratio_35 - 1.324718) < 1e-4

    print("[PASS] Problem 153: Perrin sequence and plastic ratio convergence tests passed successfully.")
