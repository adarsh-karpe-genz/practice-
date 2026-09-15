"""
Problem 49: Matrix Transpose
Difficulty: Beginner / Easy

Problem Statement:
Given a 2D matrix (list of lists), calculate and return its transpose.
The transpose of a matrix turns its rows into columns and columns into rows.
Example:
  [[1, 2, 3],
   [4, 5, 6]]
Transposed:
  [[1, 4],
   [2, 5],
   [3, 6]]

Concepts:
- Nested list comprehension
- zip(*matrix) Pythonic unpacking trick
- Matrix dimensions and row/column indexing
"""

from typing import List


def transpose_matrix_comprehension(matrix: List[List[int]]) -> List[List[int]]:
    """Method 1: Nested list comprehension."""
    if not matrix or not matrix[0]:
        return []
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def transpose_matrix_zip(matrix: List[List[int]]) -> List[List[int]]:
    """Method 2: Using zip(*matrix) unpacking trick."""
    if not matrix or not matrix[0]:
        return []
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 49: Matrix Transpose Tests")
    print("=" * 50)

    test_matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]

    r1 = transpose_matrix_comprehension(test_matrix)
    r2 = transpose_matrix_zip(test_matrix)
    print(f"Original: {test_matrix}")
    print(f"Transposed (Comp): {r1}")
    print(f"Transposed (Zip):  {r2}")
    assert r1 == expected
    assert r2 == expected

    # Square matrix
    sq = [[1, 2], [3, 4]]
    assert transpose_matrix_zip(sq) == [[1, 3], [2, 4]]

    print("\n[PASS] All Matrix Transpose tests passed successfully!")
