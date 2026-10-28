"""
Problem 164: Calkin-Wilf Sequence Generator
Generates every positive rational number exactly once in lowest terms.
Next rational from a/b is: a / (2*floor(a/b)*b + b - a) ... or via BFS on tree:
left child of a/b is a/(a+b), right child is (a+b)/b.
"""
from collections import deque

def calkin_wilf_sequence(count: int) -> list[tuple[int, int]]:
    """Return the first count fractions (num, den) from Calkin-Wilf tree via BFS."""
    if count <= 0:
        return []
    queue = deque([(1, 1)])
    result = []
    while len(result) < count:
        a, b = queue.popleft()
        result.append((a, b))
        queue.append((a, a + b))
        queue.append((a + b, b))
    return result

if __name__ == "__main__":
    expected = [(1, 1), (1, 2), (2, 1), (1, 3), (3, 2), (2, 3), (3, 1)]
    assert calkin_wilf_sequence(7) == expected
    assert calkin_wilf_sequence(1) == [(1, 1)]
    print("[PASS] Problem 164: calkin wilf sequence passed all tests.")
