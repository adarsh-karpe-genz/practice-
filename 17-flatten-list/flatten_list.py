"""
Problem 17: Flatten a Nested List
Difficulty: Beginner / Easy

Problem Statement:
Given a list that contains sublists (e.g. 2D list or arbitrarily nested lists),
flatten it into a single 1D list containing all elements.
Example: [[1, 2], [3, 4], [5]] -> [1, 2, 3, 4, 5]

Concepts:
- Nested loops & List Comprehension
- Recursive flattening for deep nesting
"""

from typing import List, Any


def flatten_2d_list(nested: List[List[Any]]) -> List[Any]:
    """Method 1: List comprehension for 2D lists (Pythonic standard)"""
    return [item for sublist in nested for item in sublist]


def flatten_deep(nested: List[Any]) -> List[Any]:
    """Method 2: Recursive flattening for arbitrarily deep lists"""
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_deep(item))
        else:
            flat.append(item)
    return flat


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 17: Flatten List Tests")
    print("=" * 50)

    # 2D test
    list_2d = [[1, 2], [3, 4], [5]]
    res1 = flatten_2d_list(list_2d)
    print(f"2D List: {list_2d} -> Flat: {res1}")
    assert res1 == [1, 2, 3, 4, 5]

    # Deep nested test
    deep_list = [1, [2, [3, 4], 5], 6, [7, [8]]]
    res2 = flatten_deep(deep_list)
    print(f"Deep List: {deep_list} -> Flat: {res2}")
    assert res2 == [1, 2, 3, 4, 5, 6, 7, 8]

    print("\n[PASS] All Flatten List tests passed successfully!")
