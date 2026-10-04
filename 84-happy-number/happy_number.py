"""
Problem 84: Check Happy Number
Difficulty: Beginner / Easy

Problem Statement:
A Happy Number is a number which eventually reaches 1 when replaced
by the sum of the square of each digit repeatedly.
If the process loops endlessly in a cycle which does not include 1, it is unhappy.
Example:
  19 -> 1^2 + 9^2 = 82
  82 -> 8^2 + 2^2 = 68
  68 -> 6^2 + 8^2 = 100
  100 -> 1^2 + 0^2 + 0^2 = 1 (Happy!) -> True

Concepts:
- Sum of squares of digits calculation
- Cycle detection using hash set (seen set)
- While loop termination conditions
"""

def is_happy(n: int) -> bool:
    """Check if n reaches 1 through sum of squared digits."""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 84: Happy Number Tests")
    print("=" * 50)

    test_cases = [
        (19, True),
        (7, True),
        (1, True),
        (2, False),
        (4, False),
    ]

    for num, expected in test_cases:
        res = is_happy(num)
        print(f"Num: {num:2d} -> Happy? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Happy Number tests passed successfully!")
