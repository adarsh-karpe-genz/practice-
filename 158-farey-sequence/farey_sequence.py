"""
Problem 158: Farey Sequence
Description:
The Farey sequence of order n, F_n, is the sequence of completely reduced
fractions between 0 and 1 with denominators <= n, arranged in increasing order.
"""

from math import gcd

def euler_totient(n: int) -> int:
    """Computes Euler's totient function phi(n)."""
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count


def farey_sequence(n: int) -> list[tuple[int, int]]:
    """
    Generates Farey sequence of order n using the mediant property:
    Next term (x2, y2) from (x0, y0) and (x1, y1):
    k = (n + y0) // y1
    x2 = k * x1 - x0
    y2 = k * y1 - y0
    """
    if n < 1:
        return []
    x0, y0 = 0, 1
    x1, y1 = 1, n
    seq = [(x0, y0), (x1, y1)]
    while not (x1 == 1 and y1 == 1):
        k = (n + y0) // y1
        x2 = k * x1 - x0
        y2 = k * y1 - y0
        seq.append((x2, y2))
        x0, y0 = x1, y1
        x1, y1 = x2, y2
    return seq


def farey_length_formula(n: int) -> int:
    """
    Computes length of Farey sequence |F_n| = 1 + sum_{k=1}^n phi(k).
    """
    return 1 + sum(euler_totient(k) for k in range(1, n + 1))


if __name__ == "__main__":
    f5 = farey_sequence(5)
    expected_5 = [
        (0, 1), (1, 5), (1, 4), (1, 3), (2, 5),
        (1, 2), (3, 5), (2, 3), (3, 4), (4, 5), (1, 1)
    ]
    assert f5 == expected_5
    assert len(f5) == farey_length_formula(5)

    # Check neighbor determinant property: b*c - a*d == 1 for adjacent a/b and c/d
    for i in range(len(f5) - 1):
        a, b = f5[i]
        c, d = f5[i + 1]
        assert b * c - a * d == 1

    print("[PASS] Problem 158: Farey sequence and Euler totient length formula tests passed successfully.")
