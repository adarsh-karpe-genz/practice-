"""
Problem 93: Check Cullen Number
Difficulty: Beginner / Easy

Problem Statement:
A Cullen number is any natural number of the form:
  C_n = n * 2^n + 1, where n >= 1.
First few Cullen numbers:
  n = 1 -> 1 * 2^1 + 1 = 3
  n = 2 -> 2 * 2^2 + 1 = 9
  n = 3 -> 3 * 2^3 + 1 = 25
  n = 4 -> 4 * 2^4 + 1 = 65
  n = 5 -> 5 * 2^5 + 1 = 161

Concepts:
- Sequence generation formula
- Search loop until generated term >= target
- Mathematical number theory
"""

def is_cullen_number(val: int) -> bool:
    """Check if val is of the form n * 2^n + 1 for n >= 1."""
    if val < 3:
        return False
    n = 1
    while True:
        c = n * (2 ** n) + 1
        if c == val:
            return True
        if c > val:
            return False
        n += 1

def cullen_sequence(count: int) -> list[int]:
    """Generate first count Cullen numbers n * 2^n + 1 starting from n=1."""
    return [n * (1 << n) + 1 for n in range(1, count + 1)]


def get_cullen_index(c_val: int) -> int | None:
    """Return n such that c_val = n * 2^n + 1, or None if not a Cullen number."""
    if c_val < 3:
        return None
    n = 1
    while True:
        val = n * (1 << n) + 1
        if val == c_val:
            return n
        if val > c_val:
            return None
        n += 1


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 93: Cullen Number Tests")
    print("=" * 50)

    test_cases = [
        (3, True),
        (9, True),
        (25, True),
        (65, True),
        (161, True),
        (4, False),
        (10, False),
        (30, False),
    ]

    for num, expected in test_cases:
        res = is_cullen_number(num)
        print(f"Num: {num:3d} -> Cullen? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"
    assert cullen_sequence(4) == [3, 9, 25, 65]
    assert get_cullen_index(25) == 3
    assert get_cullen_index(30) is None

    print("\n[PASS] All Cullen Number tests passed successfully!")
