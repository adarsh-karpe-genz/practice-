"""
Problem 133: k-Almost Prime Checker
A positive integer n is k-almost prime if it has exactly k prime factors (counted with multiplicity).
"""

def count_prime_factors(n: int) -> int:
    """Count total prime factors with multiplicity."""
    if n <= 1:
        return 0
    count = 0
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            count += 1
            temp //= d
        d += 1
    if temp > 1:
        count += 1
    return count

def is_k_almost_prime(n: int, k: int) -> bool:
    """Check if n is a k-almost prime."""
    if n <= 1 or k <= 0:
        return False
    return count_prime_factors(n) == k

def k_almost_primes_in_range(start: int, end: int, k: int) -> list[int]:
    """Return all k-almost prime numbers in [start, end]."""
    return [x for x in range(start, end + 1) if is_k_almost_prime(x, k)]


def is_semiprime(n: int) -> bool:
    """Return True if n is a semiprime (2-almost prime)."""
    return is_k_almost_prime(n, 2)


if __name__ == "__main__":
    # 2-almost primes (semiprimes): 4 (2*2), 6 (2*3), 9 (3*3)
    assert is_k_almost_prime(4, 2) is True
    assert is_k_almost_prime(6, 2) is True
    assert is_k_almost_prime(8, 3) is True  # 2*2*2
    assert is_k_almost_prime(12, 3) is True # 2*2*3
    assert is_k_almost_prime(7, 1) is True  # Prime
    assert is_k_almost_prime(16, 4) is True # 2^4
    assert is_semiprime(15) is True
    assert k_almost_primes_in_range(1, 10, 2) == [4, 6, 9, 10]
    print("[PASS] Problem 133: almost prime passed all tests.")
