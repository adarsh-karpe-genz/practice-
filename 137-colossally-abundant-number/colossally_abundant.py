"""
Problem 137: Colossally Abundant Number Checker
A positive integer n is colossally abundant if there exists an epsilon > 0 such that
sigma(n) / n^(1 + epsilon) >= sigma(k) / k^(1 + epsilon) for all k >= 1.
For beginner exploration, we check whether n achieves the maximum ratio over 1..limit for some epsilon.
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

def is_colossally_abundant_candidate(n: int, epsilon: float, limit: int = 100) -> bool:
    """Check if n maximizes sigma(k) / k^(1 + epsilon) up to limit."""
    val_n = sum_divisors(n) / (n ** (1.0 + epsilon))
    for k in range(1, limit + 1):
        val_k = sum_divisors(k) / (k ** (1.0 + epsilon))
        if val_k > val_n + 1e-9:
            return False
    return True

if __name__ == "__main__":
    # 2, 6, 12, 60, 120 are known colossally abundant numbers
    # For epsilon = 0.24, 6 maximizes the quotient up to 50:
    assert is_colossally_abundant_candidate(6, epsilon=0.24, limit=50) is True
    assert sum_divisors(12) == 28
    assert sum_divisors(6) == 12
    print("[PASS] Problem 137: colossally abundant number passed all tests.")
