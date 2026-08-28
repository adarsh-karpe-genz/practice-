"""
Problem: Maximum Subarray Sum (Kadane's Algorithm)
LeetCode: #53 (Medium)

Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

def max_sub_array(nums: List[int]) -> int:
    max_so_far = nums[0]
    curr_max = nums[0]

    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        max_so_far = max(max_so_far, curr_max)
    return max_so_far

if __name__ == "__main__":
    print("[Python] Kadane's Algorithm Test")
    tests = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ]
    for nums, expected in tests:
        res = max_sub_array(nums)
        print(f"nums: {nums} -> Max Sum: {res} | Expected: {expected}")
        assert res == expected
    print("All Kadane tests passed!")
