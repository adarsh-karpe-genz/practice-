"""
Problem 156: Sylvester's Sequence
Description:
s(0) = 2, s(n) = s(n-1)^2 - s(n-1) + 1 for n >= 1.
Alternatively: s(n) = 1 + product(s(0) ... s(n-1)).
"""

from fractions import Fraction

def sylvester_sequence(n: int) -> list[int]:
    """Generates the first n terms of Sylvester's sequence."""
    if n <= 0:
        return []
    seq = [2]
    for _ in range(1, n):
        seq.append(seq[-1] ** 2 - seq[-1] + 1)
    return seq


def egyptian_fraction_sum(n: int) -> Fraction:
    """
    Computes sum of reciprocals sum_{i=0}^{n-1} 1 / s(i).
    By identity, this sum equals 1 - 1 / (s(n) - 1).
    """
    seq = sylvester_sequence(n)
    return sum(Fraction(1, x) for x in seq)


if __name__ == "__main__":
    seq = sylvester_sequence(5)
    expected = [2, 3, 7, 43, 1807]
    assert seq == expected

    # Verify Egyptian fraction identity: sum_{i=0}^{3} 1/s(i) = 1 - 1/(s(4) - 1)
    s_4 = seq[4]
    expected_sum = 1 - Fraction(1, s_4 - 1)
    assert egyptian_fraction_sum(4) == expected_sum

    print("[PASS] Problem 156: Sylvester's sequence and Egyptian fraction identity tests passed successfully.")
