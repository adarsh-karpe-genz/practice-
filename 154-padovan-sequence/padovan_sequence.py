"""
Problem 154: Padovan Sequence
Description:
P(0) = 1, P(1) = 1, P(2) = 1
P(n) = P(n-2) + P(n-3) for n >= 3.
"""

def padovan_sequence(n: int) -> list[int]:
    """Generates the first n numbers of the Padovan sequence."""
    if n <= 0:
        return []
    base = [1, 1, 1]
    if n <= 3:
        return base[:n]
    seq = [1, 1, 1]
    for _ in range(3, n):
        seq.append(seq[-2] + seq[-3])
    return seq


def padovan_ratio_convergence(n: int) -> float:
    """
    Computes the ratio P(n) / P(n-1) which converges to the plastic number
    rho ≈ 1.3247179572...
    """
    seq = padovan_sequence(n + 1)
    if len(seq) < 2 or seq[-2] == 0:
        return 0.0
    return seq[-1] / seq[-2]


if __name__ == "__main__":
    seq = padovan_sequence(15)
    expected = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37]
    assert seq == expected

    ratio = padovan_ratio_convergence(40)
    assert abs(ratio - 1.324718) < 1e-4

    print("[PASS] Problem 154: Padovan sequence and plastic number ratio tests passed successfully.")
