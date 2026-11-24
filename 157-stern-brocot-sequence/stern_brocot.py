"""
Problem 157: Stern-Brocot Sequence
Description:
s(0) = 1, s(1) = 1
s(2n) = s(n)
s(2n+1) = s(n) + s(n+1)
Generates all positive rational numbers as s(n) / s(n+1).
"""

from math import gcd

def stern_brocot_sequence(n: int) -> list[int]:
    """Generates the first n terms of the Stern-Brocot sequence."""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    seq = [1, 1]
    while len(seq) < n:
        i = len(seq)
        if i % 2 == 0:
            seq.append(seq[i // 2])
        else:
            k = i // 2
            seq.append(seq[k] + seq[k + 1])
    return seq[:n]


def find_stern_rational_index(p: int, q: int, max_search: int = 1000) -> int | None:
    """
    Finds index i such that seq[i] / seq[i+1] == p / q.
    """
    g = gcd(p, q)
    p, q = p // g, q // g
    seq = stern_brocot_sequence(max_search)
    for i in range(len(seq) - 1):
        if seq[i] == p and seq[i + 1] == q:
            return i
    return None


if __name__ == "__main__":
    seq = stern_brocot_sequence(15)
    expected = [1, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3]
    assert seq == expected

    # Consecutive terms must be coprime
    for i in range(len(seq) - 1):
        assert gcd(seq[i], seq[i + 1]) == 1

    # Search for rational 3/5
    idx = find_stern_rational_index(3, 5)
    assert idx is not None and seq[idx] == 3 and seq[idx + 1] == 5

    print("[PASS] Problem 157: Stern-Brocot sequence and rational index search tests passed successfully.")
