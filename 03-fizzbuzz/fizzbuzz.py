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

from typing import List, Generator


def fizz_buzz(n: int) -> List[str]:
    """Classic FizzBuzz generation."""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def fizz_buzz_custom(n: int, rules: dict[int, str] | None = None) -> List[str]:
    """Customizable dictionary-driven FizzBuzz rules engine."""
    if rules is None:
        rules = {3: "Fizz", 5: "Buzz"}
    result = []
    for i in range(1, n + 1):
        label = "".join(text for divisor, text in rules.items() if i % divisor == 0)
        result.append(label if label else str(i))
    return result


def fizz_buzz_generator(n: int) -> Generator[str, None, None]:
    """
    Generator yielding FizzBuzz outputs lazily one by one up to n.
    O(1) auxiliary memory footprint.
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield str(i)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 03: FizzBuzz Tests")
    print("=" * 50)

    n = 15
    res = fizz_buzz(n)

    expected = [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
    assert res == expected, "FizzBuzz test failed!"
    assert fizz_buzz_custom(n) == expected, "Custom FizzBuzz failed!"

    # Test generator parity
    gen_res = list(fizz_buzz_generator(n))
    assert gen_res == expected, "FizzBuzz generator failed!"

    print("[PASS] All FizzBuzz tests passed successfully!")
