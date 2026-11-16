"""
Problem 92: Check Woodall Number
Difficulty: Beginner / Easy

Problem Statement:
A Woodall number (or Cullen number of second kind) is any natural number of the form:
  W_n = n * 2^n - 1, where n >= 1.
First few Woodall numbers:
  n = 1 -> 1 * 2^1 - 1 = 1
  n = 2 -> 2 * 2^2 - 1 = 7
  n = 3 -> 3 * 2^3 - 1 = 23
  n = 4 -> 4 * 2^4 - 1 = 63
  n = 5 -> 5 * 2^5 - 1 = 159

Concepts:
- Sequence generation formula
- Search loop until generated term >= target
- Mathematical number properties
"""

def is_woodall_number(val: int) -> bool:
    """Check if val is of the form n * 2^n - 1 for n >= 1."""
    if val < 1:
        return False
    n = 1
    while True:
        w = n * (2 ** n) - 1
        if w == val:
            return True
        if w > val:
            return False
        n += 1

def woodall_sequence(count: int) -> list[int]:
    """Generate first count Woodall numbers n * 2^n - 1 starting from n=1."""
    return [n * (1 << n) - 1 for n in range(1, count + 1)]


def get_woodall_index(w: int) -> int | None:
    """Return n such that w = n * 2^n - 1, or None if not a Woodall number."""
    if w < 1:
        return None
    n = 1
    while True:
        val = n * (1 << n) - 1
        if val == w:
            return n
        if val > w:
            return None
        n += 1


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 92: Woodall Number Tests")
    print("=" * 50)

    test_cases = [
        (1, True),
        (7, True),
        (23, True),
        (63, True),
        (159, True),
        (2, False),
        (10, False),
        (20, False),
    ]

    for num, expected in test_cases:
        res = is_woodall_number(num)
        print(f"Num: {num:3d} -> Woodall? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"
    assert woodall_sequence(4) == [1, 7, 23, 63]
    assert get_woodall_index(23) == 3
    assert get_woodall_index(20) is None

    print("\n[PASS] All Woodall Number tests passed successfully!")
