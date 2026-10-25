"""
Problem 143: Extravagant Number Checker
An extravagant (or wasteful) number is a positive integer that has fewer digits than
the number of digits in its prime factorization (including exponents > 1).
Example: 12 = 2^2 * 3 has 2 digits, but factorization has 3 digits ('2', '2', '3').
"""

def prime_factorization(n: int) -> list[tuple[int, int]]:
    """Return list of (prime, exponent) factors."""
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
    """Count total digits in prime factorization."""
    factors = prime_factorization(n)
    total = 0
    for p, e in factors:
        total += len(str(p))
        if e > 1:
            total += len(str(e))
    return total

def is_extravagant(n: int) -> bool:
    """Return True if digits(n) < digits(factorization(n))."""
    if n <= 1:
        return False
    return len(str(n)) < factorization_digits_count(n)

if __name__ == "__main__":
    assert is_extravagant(4) is True   # 4 (1 digit) vs 2^2 (2 digits)
    assert is_extravagant(6) is True   # 6 (1 digit) vs 2 * 3 (2 digits)
    assert is_extravagant(8) is True   # 8 (1 digit) vs 2^3 (2 digits)
    assert is_extravagant(9) is True   # 9 (1 digit) vs 3^2 (2 digits)
    assert is_extravagant(12) is True  # 12 (2 digits) vs 2^2 * 3 (3 digits)
    assert is_extravagant(10) is False # Equidigital (2 digits == 2 digits)
    print("[PASS] Problem 143: extravagant number passed all tests.")
