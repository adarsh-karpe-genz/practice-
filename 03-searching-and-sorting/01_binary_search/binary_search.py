"""
Problem: Binary Search
LeetCode: #704 (Easy)

Time Complexity: O(log N)
Space Complexity: O(1)
"""

from typing import List

def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    print("[Python] Binary Search Test")
    tests = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ]
    for nums, target, expected in tests:
        res = binary_search(nums, target)
        print(f"nums: {nums}, target: {target} -> Index: {res} | Expected: {expected}")
        assert res == expected
    print("All Binary Search tests passed!")
