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
    """Method 2: Using bitwise AND operator (&)"""
    return (n & 1) == 0


def partition_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    """Partitions a list of integers into (evens, odds)."""
    evens = [x for x in numbers if is_even_bitwise(x)]
    odds = [x for x in numbers if not is_even_bitwise(x)]
    return evens, odds


def parity_sign_classification(n: int) -> str:
    """
    Classifies integer by parity and sign:
    e.g. 'positive even', 'negative odd', 'zero'.
    """
    if n == 0:
        return "zero"
    parity = "even" if is_even_bitwise(n) else "odd"
    sign = "positive" if n > 0 else "negative"
    return f"{sign} {parity}"


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
        assert is_even_modulo(num) == expected
        assert is_even_bitwise(num) == expected

    evens, odds = partition_even_odd([1, 2, 3, 4, 5, 6])
    assert evens == [2, 4, 6]
    assert odds == [1, 3, 5]

    assert parity_sign_classification(4) == "positive even"
    assert parity_sign_classification(-3) == "negative odd"
    assert parity_sign_classification(0) == "zero"

    print("[PASS] All Even/Odd tests passed successfully!")
