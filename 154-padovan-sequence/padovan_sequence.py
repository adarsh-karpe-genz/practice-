"""
Problem 154: Padovan Sequence Generator
The Padovan sequence P_n is defined by:
P_0 = 1, P_1 = 1, P_2 = 1, and P_n = P_{n-2} + P_{n-3} for n >= 3.
"""

def padovan_number(n: int) -> int:
    """Return the n-th Padovan number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1, 2):
        return 1
    a, b, c = 1, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b
    return c

def padovan_range(count: int) -> list[int]:
    """Return first count Padovan numbers starting from P_0."""
    return [padovan_number(i) for i in range(count)]

if __name__ == "__main__":
    expected = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    assert padovan_range(10) == expected
    assert padovan_number(5) == 3
    assert padovan_number(8) == 7
    print("[PASS] Problem 154: padovan sequence passed all tests.")
