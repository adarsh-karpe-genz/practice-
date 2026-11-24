"""
Problem 160: Golomb Sequence
Description:
A non-decreasing sequence of positive integers where the n-th term is the number
of times n appears in the sequence.
G(1) = 1, G(n) = 1 + G(n - G(G(n-1))) for n >= 2.
"""

def golomb_sequence(n: int) -> list[int]:
    """Generates the first n terms of the Golomb sequence (1-indexed, returns n terms)."""
    if n <= 0:
        return []
    seq = [0, 1]
    for i in range(2, n + 1):
        val = 1 + seq[i - seq[seq[i - 1]]]
        seq.append(val)
    return seq[1:]


def golomb_asymptotic_estimate(n: int) -> float:
    """
    Estimates G(n) using the asymptotic formula:
    G(n) ~ phi^(2 - phi) * n^(phi - 1)
    where phi is the golden ratio (1 + sqrt(5)) / 2.
    """
    phi = (1 + 5 ** 0.5) / 2
    c = phi ** (2 - phi)
    return c * (n ** (phi - 1))


if __name__ == "__main__":
    seq = golomb_sequence(15)
    expected = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6]
    assert seq == expected

    # Verify self-describing property: value k appears seq[k-1] times in a large prefix
    large_seq = golomb_sequence(50)
    for k in range(1, 7):
        assert large_seq.count(k) == large_seq[k - 1]

    est_50 = golomb_asymptotic_estimate(50)
    assert abs(est_50 - large_seq[49]) < 2.0

    print("[PASS] Problem 160: Golomb sequence and asymptotic estimate tests passed successfully.")
