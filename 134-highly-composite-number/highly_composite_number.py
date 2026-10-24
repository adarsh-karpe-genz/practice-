"""
Problem 134: Highly Composite Number Checker
A highly composite number (or anti-prime) is a positive integer that has more divisors
than any smaller positive integer.
"""

def count_divisors(n: int) -> int:
    """Return the number of positive divisors of n."""
    if n <= 0:
        return 0
    count = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            count += 1 if d * d == n else 2
        d += 1
    return count

def is_highly_composite(n: int) -> bool:
    """Check if n is a highly composite number."""
    if n <= 0:
        return False
    if n == 1:
        return True
    div_n = count_divisors(n)
    for m in range(1, n):
        if count_divisors(m) >= div_n:
            return False
    return True

if __name__ == "__main__":
    # The first few highly composite numbers are 1, 2, 4, 6, 12, 24, 36, 48, 60, 120
    assert is_highly_composite(1) is True
    assert is_highly_composite(2) is True
    assert is_highly_composite(4) is True
    assert is_highly_composite(6) is True
    assert is_highly_composite(12) is True
    assert is_highly_composite(8) is False  # d(8) = 4, but d(6) = 4 so not strictly greater
    assert is_highly_composite(10) is False
    print("[PASS] Problem 134: highly composite number passed all tests.")
