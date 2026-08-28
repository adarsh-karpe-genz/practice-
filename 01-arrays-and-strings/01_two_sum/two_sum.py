"""
Problem: Two Sum
LeetCode: #1 (Easy)

Approach: Hash Map lookup (Single Pass)
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    print("[Python] Two Sum Test")
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for nums, target, expected in tests:
        res = two_sum(nums, target)
        print(f"nums: {nums}, target: {target} -> Result: {res}")
        assert res == expected, f"Failed for {nums}"
    print("All Two Sum tests passed!")
