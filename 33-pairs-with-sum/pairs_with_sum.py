"""
Problem 33: Find All Pairs with a Given Sum
Difficulty: Beginner / Easy

Problem Statement:
Given a list of integers and a target sum, find all unique pairs of numbers
that add up to the target sum. Each pair should appear only once.
Example: nums = [1, 5, 3, 7, 9, 2, 6, 3], target = 8
         -> [(1, 7), (5, 3), (2, 6)]  (pairs summing to 8)

Concepts:
- Hash Set for O(N) lookup
- Tracking seen complements to avoid duplicate pairs
- Sorting pairs for consistent output format
"""

from typing import List, Tuple


def find_pairs_with_sum(nums: List[int], target: int) -> List[Tuple[int, int]]:
    """Find all unique pairs summing to target using a hash set (O(N) time)."""
    seen = set()
    used = set()
    pairs = []

    for num in nums:
        complement = target - num
        if complement in seen and (min(num, complement), max(num, complement)) not in used:
            pair = (min(num, complement), max(num, complement))
            pairs.append(pair)
            used.add(pair)
        seen.add(num)

    return sorted(pairs)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 33: Pairs with Sum Tests")
    print("=" * 50)

    test_cases = [
        ([1, 5, 3, 7, 9, 2, 6, 3], 8, [(1, 7), (2, 6), (3, 5)]),
        ([1, 2, 3, 4, 5], 6, [(1, 5), (2, 4)]),
        ([0, 0, 0], 0, [(0, 0)]),
        ([10, 20, 30], 100, []),
        ([-1, 1, 0, 2, -2], 0, [(-2, 2), (-1, 1)]),
    ]

    for nums, target, expected in test_cases:
        res = find_pairs_with_sum(nums, target)
        print(f"nums={nums}, target={target}")
        print(f"  -> Pairs: {res} | Expected: {expected}")
        assert res == expected, f"Failed for {nums}, target={target}"

    print("\n[PASS] All Pairs with Sum tests passed successfully!")
