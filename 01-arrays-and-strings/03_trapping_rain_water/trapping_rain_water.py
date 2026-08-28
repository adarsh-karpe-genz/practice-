"""
Problem: Trapping Rain Water
LeetCode: #42 (Hard)

Approach: Two Pointers
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

def trap(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total_water += right_max - height[right]
            right -= 1

    return total_water

if __name__ == "__main__":
    print("[Python] Trapping Rain Water Test")
    tests = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ]
    for height, expected in tests:
        res = trap(height)
        print(f"height: {height} -> Trapped: {res} | Expected: {expected}")
        assert res == expected
    print("All Trapping Rain Water tests passed!")
