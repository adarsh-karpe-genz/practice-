"""
Problem 03: FizzBuzz Classic
Difficulty: Beginner / Easy

Problem Statement:
Given an integer `n`, return a list of strings where:
- For multiples of both 3 and 5, output "FizzBuzz"
- For multiples of 3 only, output "Fizz"
- For multiples of 5 only, output "Buzz"
- For all other numbers, output the number as a string.

Concepts:
- Modulo operator (%)
- Conditional logic (if / elif / else)
- List comprehension & building lists
"""

from typing import List


def fizz_buzz(n: int) -> List[str]:
    """Generate FizzBuzz sequence from 1 to n."""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:  # Divisible by both 3 and 5
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 03: FizzBuzz Tests")
    print("=" * 50)

    n = 15
    res = fizz_buzz(n)
    print(f"FizzBuzz up to {n}:")
    print(res)

    expected = [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
    assert res == expected, "FizzBuzz test failed!"
    print("\n[PASS] All FizzBuzz tests passed successfully!")
