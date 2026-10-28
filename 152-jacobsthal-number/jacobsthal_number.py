"""
Problem 152: Jacobsthal Number Generator
The Jacobsthal numbers J_n are defined by:
J_0 = 0, J_1 = 1, J_n = J_{n-1} + 2*J_{n-2} for n >= 2.
Direct formula: J_n = (2^n - (-1)^n) / 3.
"""

def jacobsthal(n: int) -> int:
    """Return the n-th Jacobsthal number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return (2**n - (-1)**n) // 3

def jacobsthal_range(count: int) -> list[int]:
    """Return the first count Jacobsthal numbers starting from J_0."""
    return [jacobsthal(i) for i in range(count)]

if __name__ == "__main__":
    expected = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171]
    assert jacobsthal_range(10) == expected
    assert jacobsthal(5) == 11
    assert jacobsthal(6) == 21
    print("[PASS] Problem 152: jacobsthal number passed all tests.")
