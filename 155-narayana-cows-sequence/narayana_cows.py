"""
Problem 155: Narayana's Cows Sequence
Description:
N(0) = 1, N(1) = 1, N(2) = 1
N(n) = N(n-1) + N(n-3) for n >= 3.
"""

def narayana_cows(n: int) -> list[int]:
    """Generates the first n terms of Narayana's cows sequence."""
    if n <= 0:
        return []
    base = [1, 1, 1]
    if n <= 3:
        return base[:n]
    seq = [1, 1, 1]
    for _ in range(3, n):
        seq.append(seq[-1] + seq[-3])
    return seq


def narayana_ratio_convergence(n: int) -> float:
    """
    Computes ratio N(n) / N(n-1) which converges to the supergolden ratio
    psi ≈ 1.465571231876768...
    """
    seq = narayana_cows(n + 1)
    if len(seq) < 2 or seq[-2] == 0:
        return 0.0
    return seq[-1] / seq[-2]


if __name__ == "__main__":
    seq = narayana_cows(12)
    expected = [1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41]
    assert seq == expected

    # Ratio approaches supergolden ratio ~ 1.46557
    ratio = narayana_ratio_convergence(40)
    assert abs(ratio - 1.46557) < 1e-4

    print("[PASS] Problem 155: Narayana's Cows sequence and supergolden ratio tests passed successfully.")
