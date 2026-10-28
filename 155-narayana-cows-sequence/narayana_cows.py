"""
Problem 155: Narayana's Cows Sequence Generator
Narayana's cows sequence is defined by:
N_0 = 1, N_1 = 1, N_2 = 1, and N_n = N_{n-1} + N_{n-3} for n >= 3.
"""

def narayana_number(n: int) -> int:
    """Return the n-th Narayana number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1, 2):
        return 1
    a, b, c = 1, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, c + a
    return c

def narayana_range(count: int) -> list[int]:
    """Return first count Narayana numbers starting from N_0."""
    return [narayana_number(i) for i in range(count)]

if __name__ == "__main__":
    # 1, 1, 1, 2, 3, 4, 6, 9, 13, 19
    expected = [1, 1, 1, 2, 3, 4, 6, 9, 13, 19]
    assert narayana_range(10) == expected
    assert narayana_number(5) == 4
    assert narayana_number(6) == 6
    print("[PASS] Problem 155: narayana cows passed all tests.")
