"""
Problem 164: Calkin-Wilf Sequence
Description:
Generates all positive rational numbers without repetition.
q(1) = 1/1
If q(n) = a/b, then q(n+1) = b / (2 * floor(a/b) * b + b - a)
or next fraction from a/b is b / (2 * (a // b) * b + b - a).
"""

from math import gcd

def calkin_wilf_sequence(n: int) -> list[tuple[int, int]]:
    """Generates the first n terms of the Calkin-Wilf sequence of fractions (a, b)."""
    if n <= 0:
        return []
    seq = [(1, 1)]
    for _ in range(1, n):
        a, b = seq[-1]
        next_a = b
        next_b = 2 * (a // b) * b + b - a
        seq.append((next_a, next_b))
    return seq


def find_calkin_wilf_index(p: int, q: int, max_search: int = 200) -> int | None:
    """
    Finds the 1-based index of fraction p/q in the Calkin-Wilf sequence.
    """
    g = gcd(p, q)
    p, q = p // g, q // g
    seq = calkin_wilf_sequence(max_search)
    for idx, (a, b) in enumerate(seq, 1):
        if a == p and b == q:
            return idx
    return None


if __name__ == "__main__":
    seq = calkin_wilf_sequence(10)
    expected = [
        (1, 1), (1, 2), (2, 1), (1, 3), (3, 2),
        (2, 3), (3, 1), (1, 4), (4, 3), (3, 5)
    ]
    assert seq == expected

    # Consecutive terms check
    for a, b in seq:
        assert gcd(a, b) == 1

    # Search rational 3/2 -> 5th term
    assert find_calkin_wilf_index(3, 2) == 5

    print("[PASS] Problem 164: Calkin-Wilf sequence and rational index search tests passed successfully.")
