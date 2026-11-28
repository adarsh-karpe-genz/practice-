"""
Problem 21: Sum of Elements in a List
Difficulty: Beginner / Easy

Problem Statement:
Given a list of numbers, compute the total sum of all its elements.
Example: [1, 2, 3, 4, 5] -> 15

Concepts:
- Accumulator variable in a loop
- Recursion fundamentals: base case (empty list) and step (head + rest)
- Built-in sum() function
"""

from typing import List


def sum_loop(numbers: List[int | float]) -> int | float:
    """Iterative accumulator."""
    total = 0
    for num in numbers:
        total += num
    return total


def sum_recursive(numbers: List[int | float]) -> int | float:
    """Recursive sum."""
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])


def sum_builtin(numbers: List[int | float]) -> int | float:
    """Built-in sum."""
    return sum(numbers)


def prefix_sums(numbers: List[int | float]) -> List[int | float]:
    """Cumulative prefix sum sequence."""
    running = 0
    result = []
    for x in numbers:
        running += x
        result.append(running)
    return result


def range_sum(numbers: List[int | float], left: int, right: int) -> int | float:
    """
    Computes range sum sum(numbers[left : right+1]) using prefix sum array in O(1) time.
    """
    if not numbers or left > right or left < 0 or right >= len(numbers):
        return 0
    pref = prefix_sums(numbers)
    return pref[right] - (pref[left - 1] if left > 0 else 0)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 15),
        ([-1, -2, -3, -4], -10),
        ([10, -5, 20, -15], 10),
        ([42], 42),
        ([], 0),
        ([100, 200, 300], 600),
    ]

    for nums, expected in test_cases:
        r1 = sum_loop(nums)
        r2 = sum_recursive(nums)
        r3 = sum_builtin(nums)
        assert r1 == expected and r2 == expected and r3 == expected
    assert prefix_sums([1, 2, 3, 4]) == [1, 3, 6, 10]

    # Test range sum
    assert range_sum([1, 2, 3, 4, 5], 1, 3) == 9  # 2 + 3 + 4
    assert range_sum([10, 20, 30], 0, 2) == 60

    print("[PASS] Problem 21: Sum of List tests passed successfully!")
