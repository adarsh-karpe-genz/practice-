"""
Problem 06: Even or Odd Checker
Difficulty: Beginner / Easy

Problem Statement:
Given an integer `n`, determine whether it is Even or Odd.
- An even number is divisible by 2 with no remainder (e.g. -4, 0, 2, 4, 6).
- An odd number leaves a remainder of 1 or -1 when divided by 2 (e.g. -3, 1, 3, 5).

Concepts:
- Modulo operator (`n % 2 == 0`)
- Bitwise AND operator (`(n & 1) == 0`)
"""

def is_even_modulo(n: int) -> bool:
    """Method 1: Using modulo operator (%)"""
    return n % 2 == 0


def is_even_bitwise(n: int) -> bool:
    """Method 2: Using bitwise AND (Checks the lowest significant bit)"""
    return (n & 1) == 0


def partition_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    """Partition a list of integers into (evens, odds)."""
    evens = [x for x in numbers if is_even_bitwise(x)]
    odds = [x for x in numbers if not is_even_bitwise(x)]
    return evens, odds


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 06: Even or Odd Tests")
    print("=" * 50)

    test_cases = [
        (4, True),
        (7, False),
        (0, True),
        (-2, True),
        (-5, False),
    ]

    for num, expected in test_cases:
        res1 = is_even_modulo(num)
        res2 = is_even_bitwise(num)
        print(f"Number: {num:2d} -> Even? {res1} | Expected: {expected}")
        assert res1 == expected
        assert res2 == expected

    evens, odds = partition_even_odd([1, 2, 3, 4, 5, 6])
    assert evens == [2, 4, 6]
    assert odds == [1, 3, 5]
    print("\n[PASS] All Even/Odd tests passed successfully!")
