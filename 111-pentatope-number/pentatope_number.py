"""
Problem 111: Check Pentatope Number (4D Simplex)
Difficulty: Beginner / Easy

Problem Statement:
A pentatope number is a number in the fifth cell of any row of Pascal's triangle
starting with row 5. They represent 4-dimensional simplexes (hypertetrahedrons).
Formula:
  P_5(n) = n(n + 1)(n + 2)(n + 3) // 24, for n >= 1.
First few pentatope numbers:
  n = 1 -> 1
  n = 2 -> 5
  n = 3 -> 15
  n = 4 -> 35
  n = 5 -> 70
  n = 6 -> 126

Concepts:
- 4D figurate numbers
- Pascal's triangle diagonals
- Binomial coefficient C(n+3, 4)
"""

def get_pentatope_number(n: int) -> int:
    """Return the n-th pentatope number."""
    if n < 1:
        raise ValueError("n must be at least 1")
    return n * (n + 1) * (n + 2) * (n + 3) // 24

def is_pentatope_number(val: int) -> bool:
    """Check if val is a pentatope number."""
    if val < 1:
        return False
    n = 1
    while True:
        p = get_pentatope_number(n)
        if p == val:
            return True
        if p > val:
            return False
        n += 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 111: Pentatope Number Tests")
    print("=" * 50)

    test_cases = [
        (1, 1),
        (2, 5),
        (3, 15),
        (4, 35),
        (5, 70),
        (6, 126),
        (7, 210),
    ]

    for n, expected in test_cases:
        res = get_pentatope_number(n)
        print(f"P_5({n}) = {res} | Expected: {expected}")
        assert res == expected
        assert is_pentatope_number(expected) is True

    assert is_pentatope_number(2) is False
    assert is_pentatope_number(10) is False
    assert is_pentatope_number(50) is False

    print("\n[PASS] All Pentatope Number tests passed successfully!")
