"""
Problem 91: Check Mersenne Number
Difficulty: Beginner / Easy

Problem Statement:
A Mersenne number is any positive integer of the form 2^k - 1, where k >= 1.
Examples:
  1  = 2^1 - 1 -> True
  3  = 2^2 - 1 -> True
  7  = 2^3 - 1 -> True
  15 = 2^4 - 1 -> True
  31 = 2^5 - 1 -> True
  6  (not of form 2^k - 1) -> False

Concepts:
- Adding 1 to test for power of 2
- Bitwise test (x & (x - 1) == 0)
- Logarithmic checks
"""

def is_mersenne_number(n: int) -> bool:
    """Check if n is of the form 2^k - 1."""
    if n <= 0:
        return False
    target = n + 1
    return (target & (target - 1)) == 0

def mersenne_exponent(n: int) -> int | None:
    """Return exponent p such that n = 2^p - 1, or None if n is not a Mersenne number."""
    if n <= 0 or (n & (n + 1)) != 0:
        return None
    return (n + 1).bit_length() - 1


def mersenne_sequence(count: int) -> list[int]:
    """Generate first count Mersenne numbers starting from p=1."""
    return [(1 << p) - 1 for p in range(1, count + 1)]


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 91: Mersenne Number Tests")
    print("=" * 50)

    test_cases = [
        (1, True),
        (3, True),
        (7, True),
        (15, True),
        (31, True),
        (63, True),
        (6, False),
        (10, False),
        (0, False),
    ]

    for num, expected in test_cases:
        res = is_mersenne_number(num)
        print(f"Num: {num:2d} -> Mersenne? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"
    assert mersenne_sequence(5) == [1, 3, 7, 15, 31]
    assert mersenne_exponent(31) == 5
    assert mersenne_exponent(10) is None

    print("\n[PASS] All Mersenne Number tests passed successfully!")
