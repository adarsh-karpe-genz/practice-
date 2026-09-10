"""
Problem 35: Rotate a List by K Positions (Right Rotation)
Difficulty: Beginner / Easy

Problem Statement:
Given a list and an integer k, rotate the list to the right by k positions.
Elements that fall off the end wrap around to the front.
Examples:
  [1, 2, 3, 4, 5], k=2 -> [4, 5, 1, 2, 3]
  [1, 2, 3], k=4        -> [3, 1, 2]  (k > len, so k = k % len)

Concepts:
- Modulo to handle k > len(list)
- Slicing: rotated = nums[-k:] + nums[:-k]
- In-place three-reversal algorithm (O(1) extra space)
"""

from typing import List


def rotate_right_slicing(nums: List[int], k: int) -> List[int]:
    """Method 1: Slicing approach (O(N) time, O(N) space)"""
    if not nums:
        return nums
    k = k % len(nums)
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]


def rotate_right_reversal(nums: List[int], k: int) -> List[int]:
    """Method 2: Three-reversal algorithm (O(N) time, O(1) extra space)"""
    arr = nums[:]
    n = len(arr)
    if n == 0:
        return arr
    k = k % n

    def reverse(a, lo, hi):
        while lo < hi:
            a[lo], a[hi] = a[hi], a[lo]
            lo += 1
            hi -= 1

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    return arr


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 35: Rotate List Tests")
    print("=" * 50)

    test_cases = [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3], 4, [3, 1, 2]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([7], 3, [7]),
        ([], 5, []),
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
    ]

    for nums, k, expected in test_cases:
        r1 = rotate_right_slicing(nums, k)
        r2 = rotate_right_reversal(nums, k)
        print(f"nums={nums}, k={k} -> {r1} | Expected: {expected}")
        assert r1 == expected, f"Slicing failed for {nums}, k={k}"
        assert r2 == expected, f"Reversal failed for {nums}, k={k}"

    print("\n[PASS] All Rotate List tests passed successfully!")
