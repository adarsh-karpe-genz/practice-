"""
Problem 158: Farey Sequence Generator
The Farey sequence F_n of order n is the sorted sequence of completely reduced
fractions between 0 and 1 with denominators <= n.
"""
import math

def farey_sequence(n: int) -> list[tuple[int, int]]:
    """Return the Farey sequence of order n as list of (numerator, denominator) tuples."""
    if n <= 0:
        return []
    # Using iterative Farey generation:
    # Given a/b and c/d, next fraction e/f has:
    # k = floor((n + b) / d)
    # e = k*c - a, f = k*d - b
    a, b = 0, 1
    c, d = 1, n
    result = [(a, b)]
    while c <= n:
        result.append((c, d))
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
    return result

if __name__ == "__main__":
    # F_5: 0/1, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 1/1
    expected_f5 = [(0, 1), (1, 5), (1, 4), (1, 3), (2, 5), (1, 2), (3, 5), (2, 3), (3, 4), (4, 5), (1, 1)]
    assert farey_sequence(5) == expected_f5
    assert farey_sequence(1) == [(0, 1), (1, 1)]
    print("[PASS] Problem 158: farey sequence passed all tests.")
