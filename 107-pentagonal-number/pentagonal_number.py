"""
Problem 107: Check Pentagonal Number
Difficulty: Beginner / Easy

Problem Statement:
A pentagonal number is a figurate number that extends the concept of triangular
and square numbers to the pentagon (5-gon).
The n-th pentagonal number is given by:
  P(n) = (3n^2 - n) // 2, for n >= 1.
First few pentagonal numbers:
  n = 1 -> 1
  n = 2 -> 5
  n = 3 -> 12
  n = 4 -> 22
  n = 5 -> 35
  n = 6 -> 51
  n = 7 -> 70

Concepts:
- 5-sided figurate numbers
- Solving quadratic equation 3n^2 - n - 2*val = 0
- Discriminant D = 1 + 24*val
"""

import math

def get_pentagonal_number(n: int) -> int:
    """Return the n-th pentagonal number for n >= 1."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return (3 * n * n - n) // 2

def is_pentagonal_number(val: int) -> bool:
    """Check if val is a pentagonal number:
    3n^2 - n - 2*val = 0
    Discriminant D = 1 + 24*val
    n = (1 + sqrt(D)) / 6
    """
    if val < 1:
        return False
    disc = 1 + 24 * val
    r = math.isqrt(disc)
    if r * r != disc:
        return False
    numerator = 1 + r
    return numerator % 6 == 0 and numerator // 6 >= 1

def pentagonal_sequence(count: int) -> list[int]:
    """Generate first count pentagonal numbers n(3n - 1)//2 starting from n=1."""
    return [get_pentagonal_number(i) for i in range(1, count + 1)]


def generalized_pentagonal_sequence(count: int) -> list[int]:
    """Generate generalized pentagonal numbers k(3k - 1)//2 for k = 1, -1, 2, -2..."""
    res = []
    k = 1
    while len(res) < count:
        for val in (k, -k):
            res.append(val * (3 * val - 1) // 2)
            if len(res) == count:
                break
        k += 1
    return res


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 107: Pentagonal Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 5),
        (3, 12),
        (4, 22),
        (5, 35),
        (6, 51),
        (7, 70),
    ]

    for n, expected in test_cases:
        res = get_pentagonal_number(n)
        print(f"P({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_pentagonal_number(expected) is True

    assert is_pentagonal_number(2) is False
    assert is_pentagonal_number(10) is False
    assert is_pentagonal_number(20) is False
    assert pentagonal_sequence(5) == [1, 5, 12, 22, 35]
    assert generalized_pentagonal_sequence(6) == [1, 2, 5, 7, 12, 15]

    print("\n[PASS] All Pentagonal Number tests passed successfully!")
