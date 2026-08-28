"""
Problem: Quick Sort

Time Complexity: O(N log N) Average
Space Complexity: O(log N) recursion stack
"""

from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    print("[Python] Quick Sort Test")
    arr = [10, 7, 8, 9, 1, 5]
    sorted_arr = quick_sort(arr)
    print("Original:", arr)
    print("Sorted:  ", sorted_arr)
    assert sorted_arr == sorted(arr)
    print("Quick Sort test passed!")
