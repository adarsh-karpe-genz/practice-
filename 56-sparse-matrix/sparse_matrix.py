"""
Problem 56: Check if Matrix is Sparse
Difficulty: Beginner / Easy

Problem Statement:
A sparse matrix is a matrix in which the number of zero elements is strictly
greater than the number of non-zero elements.
Given a 2D matrix (list of lists), determine if it is a sparse matrix.
Example:
  [[1, 0, 0],
   [0, 0, 2],
   [0, 3, 0]]
Zeros: 7, Non-zeros: 2 -> 7 > (9 / 2) -> True

Concepts:
- 2D matrix traversal (nested loops / sum generator)
- Counting conditions
- Threshold check: zeros > (rows * cols) // 2
"""

from typing import List


def is_sparse_matrix(matrix: List[List[int]]) -> bool:
    """Check if zeros strictly exceed half the total elements in matrix."""
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    total_elements = rows * cols

    zero_count = sum(row.count(0) for row in matrix)
    return zero_count > (total_elements / 2)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 56: Sparse Matrix Tests")
    print("=" * 50)

    sparse_sample = [
        [1, 0, 0],
        [0, 0, 2],
        [0, 3, 0]
    ]

    dense_sample = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]

    assert is_sparse_matrix(sparse_sample) is True
    assert is_sparse_matrix(dense_sample) is False
    assert is_sparse_matrix([[0]]) is True
    assert is_sparse_matrix([[1]]) is False

    print("Sparse Matrix Sample -> True")
    print("Dense Matrix Sample  -> False")

    print("\n[PASS] All Sparse Matrix tests passed successfully!")
