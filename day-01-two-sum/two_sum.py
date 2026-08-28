"""
================================================================================
Day 01: Two Sum
LeetCode: #1 (Easy)
================================================================================

Problem Statement:
------------------
Given an array of integers `nums` and an integer `target`, return indices of
the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not
use the same element twice. You can return the answer in any order.

Example 1:
----------
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
----------
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:
----------
Input: nums = [3, 3], target = 6
Output: [0, 1]

Constraints:
------------
- 2 <= len(nums) <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Approach & Complexity:
----------------------
Approach: One-pass Hash Map (Dictionary)
- As we iterate through the array, compute the required complement: complement = target - num.
- If the complement already exists in our dictionary, we have found the solution.
- Otherwise, store the current number with its index in the dictionary.

Time Complexity:  O(N) -> Single pass through the array of length N.
Space Complexity: O(N) -> Stores up to N elements in the hash map.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find indices of the two numbers that sum up to target using a hash map.
    """
    seen = {}  # maps value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


# ==============================================================================
# Unit Tests & Verification
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Running Day 01: Two Sum Verification")
    print("=" * 60)

    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
        {"nums": [-1, -2, -3, -4, -5], "target": -8, "expected": [2, 4]},
    ]

    for idx, test in enumerate(test_cases, 1):
        nums = test["nums"]
        target = test["target"]
        expected = test["expected"]
        result = two_sum(nums, target)

        status = "[PASS]" if result == expected else "[FAIL]"
        print(f"Test {idx}: nums={nums}, target={target}")
        print(f"  -> Result:   {result}")
        print(f"  -> Expected: {expected}")
        print(f"  -> Status:   {status}\n")
        assert result == expected, f"Test {idx} failed!"

    print("All test cases passed successfully!")
