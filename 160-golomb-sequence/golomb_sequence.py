"""
Problem 160: Golomb Sequence Generator
Golomb's sequence G_n is a non-decreasing integer sequence where G_n is the number
of times n appears in the sequence.
G_1 = 1, G_{n+1} = 1 + G_{n + 1 - G_{G_n}}
"""

def golomb_sequence(n: int) -> list[int]:
    """Generate the first n terms of the Golomb sequence (1-indexed, starting from G_1)."""
    if n <= 0:
        return []
    g = [0] * (n + 1)
    g[1] = 1
    for i in range(2, n + 1):
        g[i] = 1 + g[i - g[g[i - 1]]]
    return g[1:]

if __name__ == "__main__":
    expected = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5]
    assert golomb_sequence(10) == expected
    assert golomb_sequence(1) == [1]
    assert golomb_sequence(4) == [1, 2, 2, 3]
    print("[PASS] Problem 160: golomb sequence passed all tests.")
