"""
Problem 161: Hofstadter Q-Sequence Generator
Defined by:
Q(1) = 1, Q(2) = 1
Q(n) = Q(n - Q(n - 1)) + Q(n - Q(n - 2)) for n > 2.
"""

def hofstadter_q(n: int) -> list[int]:
    """Generate first n terms of Hofstadter Q-sequence."""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    q = [0] * (n + 1)
    q[1] = 1
    q[2] = 1
    for i in range(3, n + 1):
        q[i] = q[i - q[i - 1]] + q[i - q[i - 2]]
    return q[1:]

if __name__ == "__main__":
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 6]
    assert hofstadter_q(10) == expected
    assert hofstadter_q(1) == [1]
    assert hofstadter_q(3) == [1, 1, 2]
    print("[PASS] Problem 161: hofstadter q sequence passed all tests.")
