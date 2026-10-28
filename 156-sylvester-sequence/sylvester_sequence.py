"""
Problem 156: Sylvester's Sequence Generator
Sylvester's sequence is defined by:
s_0 = 2, and s_n = s_{n-1}^2 - s_{n-1} + 1 for n >= 1.
Alternatively: s_n = 1 + product_{i=0}^{n-1} s_i.
"""

def sylvester_number(n: int) -> int:
    """Return the n-th Sylvester number (0-indexed)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    s = 2
    for _ in range(n):
        s = s * s - s + 1
    return s

def sylvester_range(count: int) -> list[int]:
    """Return the first count terms of Sylvester's sequence."""
    res = []
    s = 2
    for _ in range(count):
        res.append(s)
        s = s * s - s + 1
    return res

if __name__ == "__main__":
    expected = [2, 3, 7, 43, 1807]
    assert sylvester_range(5) == expected
    assert sylvester_number(0) == 2
    assert sylvester_number(1) == 3
    assert sylvester_number(2) == 7
    assert sylvester_number(3) == 43
    print("[PASS] Problem 156: sylvester sequence passed all tests.")
