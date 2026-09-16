"""
Problem 57: Move Zeroes to End of List
Difficulty: Beginner / Easy

Problem Statement:
Given a list of integers, move all 0s to the end of it while maintaining
the relative order of the non-zero elements.
Do this in-place or return a new list.
Example: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]

Concepts:
- Two-pointer technique (in-place modification)
- O(N) time complexity, O(1) auxiliary space
- List filtering and concatenation shortcut
"""

from typing import List


def move_zeroes_in_place(nums: List[int]) -> List[int]:
    """Method 1: Two-pointer in-place shift (O(N) time, O(1) space)."""
    arr = nums[:]
    insert_pos = 0

    # Place non-zero elements forward
    for num in arr:
        if num != 0:
            arr[insert_pos] = num
            insert_pos += 1

    # Fill remaining spots with zeroes
    while insert_pos < len(arr):
        arr[insert_pos] = 0
        insert_pos += 1

    return arr


def move_zeroes_pythonic(nums: List[int]) -> List[int]:
    """Method 2: List comprehension filtering."""
    non_zeroes = [x for x in nums if x != 0]
    zeroes = [0] * (len(nums) - len(non_zeroes))
    return non_zeroes + zeroes


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 57: Move Zeroes Tests")
    print("=" * 50)

    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 0], [0, 0, 0]),
        ([], []),
        ([42], [42]),
    ]

    for nums, expected in test_cases:
        r1 = move_zeroes_in_place(nums)
        r2 = move_zeroes_pythonic(nums)
        print(f"Original: {nums} -> Moved: {r1} | Expected: {expected}")
        assert r1 == expected
        assert r2 == expected

    print("\n[PASS] All Move Zeroes tests passed successfully!")
