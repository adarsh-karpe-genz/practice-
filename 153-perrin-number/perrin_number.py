"""
Problem 153: Perrin Number Generator
The Perrin sequence P_n is defined by:
P_0 = 3, P_1 = 0, P_2 = 2, and P_n = P_{n-2} + P_{n-3} for n >= 3.
"""

def perrin_number(n: int) -> int:
    """Return the n-th Perrin number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2
    a, b, c = 3, 0, 2
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b
    return c

def perrin_range(count: int) -> list[int]:
    """Return first count Perrin numbers starting from P_0."""
    return [perrin_number(i) for i in range(count)]

if __name__ == "__main__":
    expected = [3, 0, 2, 3, 2, 5, 5, 7, 10, 12]
    assert perrin_range(10) == expected
    assert perrin_number(7) == 7
    assert perrin_number(9) == 12
    print("[PASS] Problem 153: perrin number passed all tests.")
