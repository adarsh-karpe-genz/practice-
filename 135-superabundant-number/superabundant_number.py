"""
Problem 135: Superabundant Number Checker
A positive integer n is superabundant if for all m < n:
sigma(m) / m < sigma(n) / n
where sigma(n) is the sum of all divisors of n.
"""

def sum_divisors(n: int) -> int:
    """Return the sum of divisors of n."""
    if n <= 0:
        return 0
    total = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            total += d
            if d * d != n:
                total += n // d
        d += 1
    return total

def is_superabundant(n: int) -> bool:
    """Check if n is a superabundant number."""
    if n <= 0:
        return False
    if n == 1:
        return True
    idx_n = sum_divisors(n) / n
    for m in range(1, n):
        if (sum_divisors(m) / m) >= idx_n:
            return False
    return True

if __name__ == "__main__":
    # The first few superabundant numbers are 1, 2, 4, 6, 12, 24, 36, 48, 60, 120
    assert is_superabundant(1) is True
    assert is_superabundant(2) is True
    assert is_superabundant(4) is True
    assert is_superabundant(6) is True
    assert is_superabundant(12) is True
    assert is_superabundant(8) is False
    print("[PASS] Problem 135: superabundant number passed all tests.")
