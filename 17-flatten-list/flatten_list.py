"""
Problem 17: Flatten a Nested List
Difficulty: Beginner / Easy

Problem Statement:
Given a list that contains sublists (e.g. 2D list or arbitrarily nested lists),
flatten it into a single 1D list containing all elements.
Example: [[1, 2], [3, 4], [5]] -> [1, 2, 3, 4, 5]

Concepts:
- Nested loops and list comprehensions
- Recursive depth traversal
- Iterative stack-based flattening
"""

from typing import List, Any


def flatten_2d_list(nested_list: List[List[Any]]) -> List[Any]:
    """Flattens a 2D list into a 1D list using comprehension."""
    return [item for sublist in nested_list for item in sublist]


def flatten_deep(nested_list: List[Any]) -> List[Any]:
    """Recursively flattens an arbitrarily nested list."""
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_deep(item))
        else:
            flat.append(item)
    return flat


def flatten_iterative_stack(nested_list: List[Any]) -> List[Any]:
    """Iteratively flattens nested lists using an explicit stack."""
    stack = [nested_list]
    result = []
    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            for elem in reversed(curr):
                stack.append(elem)
        else:
            result.append(curr)
    return result


def max_nesting_depth(nested_list: List[Any]) -> int:
    """
    Computes the maximum nesting depth of a nested list.
    Example: [1, [2, [3]]] -> 3; [1, 2] -> 1; [] -> 0.
    """
    if not isinstance(nested_list, list):
        return 0
    if not nested_list:
        return 1
    depths = [max_nesting_depth(item) for item in nested_list]
    return 1 + max(depths)


if __name__ == "__main__":
    list_2d = [[1, 2], [3, 4], [5]]
    res1 = flatten_2d_list(list_2d)
    assert res1 == [1, 2, 3, 4, 5]

    deep_list = [1, [2, [3, 4], 5], 6, [7, [8]]]
    res2 = flatten_deep(deep_list)
    assert res2 == [1, 2, 3, 4, 5, 6, 7, 8]
    assert flatten_iterative_stack(deep_list) == [1, 2, 3, 4, 5, 6, 7, 8]

    # Test nesting depth
    assert max_nesting_depth([1, 2, 3]) == 1
    assert max_nesting_depth([[1], [2, [3]]]) == 3
    assert max_nesting_depth([]) == 1

    print("[PASS] Problem 17: Flatten List tests passed successfully!")
