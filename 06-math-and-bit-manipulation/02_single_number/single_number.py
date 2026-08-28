"""
Problem: Single Number
LeetCode: #136 (Easy)

Approach: Bitwise XOR
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

def single_number(nums: List[int]) -> int:
    unique = 0
    for num in nums:
        unique ^= num
    return unique

if __name__ == "__main__":
    print("[Python] Single Number Test")
    tests = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ]
    for nums, expected in tests:
        res = single_number(nums)
        print(f"nums: {nums} -> Single Number: {res} | Expected: {expected}")
        assert res == expected
    print("Single number tests passed!")
