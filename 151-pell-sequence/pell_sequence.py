"""
Problem 151: Pell Sequence Generator
The Pell numbers P_n are defined by:
P_0 = 0, P_1 = 1, P_n = 2*P_{n-1} + P_{n-2} for n >= 2.
"""

def pell_number(n: int) -> int:
    """Return the n-th Pell number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, 2 * b + a
    return b

def pell_range(count: int) -> list[int]:
    """Return the first count Pell numbers starting from P_0."""
    return [pell_number(i) for i in range(count)]

if __name__ == "__main__":
    expected = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985]
    assert pell_range(10) == expected
    assert pell_number(4) == 12
    assert pell_number(5) == 29
    print("[PASS] Problem 151: pell sequence passed all tests.")
