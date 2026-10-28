"""
Problem 150: Lucas Sequence Generator
The Lucas sequence L_n is defined by:
L_0 = 2, L_1 = 1, L_n = L_{n-1} + L_{n-2} for n >= 2.
"""

def lucas_number(n: int) -> int:
    """Return the n-th Lucas number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def lucas_range(count: int) -> list[int]:
    """Return the first count Lucas numbers starting from L_0."""
    return [lucas_number(i) for i in range(count)]

if __name__ == "__main__":
    expected = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
    assert lucas_range(10) == expected
    assert lucas_number(0) == 2
    assert lucas_number(1) == 1
    assert lucas_number(5) == 11
    print("[PASS] Problem 150: lucas sequence passed all tests.")
