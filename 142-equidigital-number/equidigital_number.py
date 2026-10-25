"""
Problem 142: Equidigital Number Checker
An equidigital number is a positive integer that has the same number of digits as
the number of digits in its prime factorization (including exponents > 1).
Example: 10 = 2 * 5 has 2 digits, and its factorization '2*5' has 2 digits (2, 5).
"""

def prime_factorization(n: int) -> list[tuple[int, int]]:
    """Return list of (prime, exponent) for n."""
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            factors.append((d, count))
        d += 1
    if temp > 1:
        factors.append((temp, 1))
    return factors

def factorization_digits_count(n: int) -> int:
    """Count total digits in prime factorization representation."""
    factors = prime_factorization(n)
    total = 0
    for p, e in factors:
        total += len(str(p))
        if e > 1:
            total += len(str(e))
    return total

def is_equidigital(n: int) -> bool:
    """Return True if digits(n) == digits(factorization(n))."""
    if n <= 1:
        return False
    return len(str(n)) == factorization_digits_count(n)

if __name__ == "__main__":
    # Primes are equidigital because p has len(str(p)) and its factorization is just p
    assert is_equidigital(2) is True
    assert is_equidigital(5) is True
    assert is_equidigital(10) is True  # 10 (2 digits) = 2 * 5 (2 digits)
    assert is_equidigital(14) is True  # 14 = 2 * 7
    assert is_equidigital(125) is False # Frugal
    print("[PASS] Problem 142: equidigital number passed all tests.")
