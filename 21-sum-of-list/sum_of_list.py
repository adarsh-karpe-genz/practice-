"""
Problem 21: Sum of List Elements
Difficulty: Beginner / Easy

Problem Statement:
Given a list of numbers, calculate and return the sum of all elements.
Example: [1, 2, 3, 4, 5] -> 15

Concepts:
- Accumulator loop pattern
- Basic recursion
- Python built-in sum()
"""

from typing import List


def sum_loop(numbers: List[int | float]) -> int | float:
    """Method 1: Manual Accumulator Loop (O(N) time, O(1) space)"""
    total = 0
    for num in numbers:
        total += num
    return total


def sum_recursive(numbers: List[int | float]) -> int | float:
    """Method 2: Recursive Sum"""
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])


def sum_builtin(numbers: List[int | float]) -> int | float:
    """Method 3: Built-in sum()"""
    return sum(numbers)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 21: Sum of List Tests")
    print("=" * 50)

    test_cases = [
        ([1, 2, 3, 4, 5], 15),
        ([10, -5, 20, -15], 10),
        ([42], 42),
        ([], 0),
        ([100, 200, 300], 600),
    ]

    for nums, expected in test_cases:
        r1 = sum_loop(nums)
        r2 = sum_recursive(nums)
        r3 = sum_builtin(nums)
        print(f"List: {nums} -> Sum: {r1} | Expected: {expected}")
        assert r1 == expected and r2 == expected and r3 == expected

    print("\n[PASS] All Sum of List tests passed successfully!")
