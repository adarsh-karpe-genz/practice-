"""
Problem 141: Frugal Number Checker
A frugal number is a positive integer that has more digits than the number of digits
in its prime factorization (including exponents > 1).
Example: 125 = 5^3 has 3 digits, factorization 5^3 has 2 digits (5, 3). Frugal!
"""

def prime_factorization(n: int) -> list[tuple[int, int]]:
    """Return prime factors and their multiplicities as [(p, e), ...]."""
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
    """Count total digits used to write prime factorization p1^e1 * p2^e2..."""
    factors = prime_factorization(n)
    total_digits = 0
    for p, e in factors:
        total_digits += len(str(p))
        if e > 1:
            total_digits += len(str(e))
    return total_digits

def is_frugal(n: int) -> bool:
    """Return True if n has more digits than its prime factorization representation."""
    if n <= 1:
        return False
    digits_n = len(str(n))
    digits_factors = factorization_digits_count(n)
    return digits_n > digits_factors

if __name__ == "__main__":
    assert is_frugal(125) is True   # 125 (3 digits) vs 5^3 (2 digits)
    assert is_frugal(128) is True   # 128 (3 digits) vs 2^7 (2 digits)
    assert is_frugal(243) is True   # 243 (3 digits) vs 3^5 (2 digits)
    assert is_frugal(12) is False   # 12 (2 digits) vs 2^2 * 3 (3 digits: 2, 2, 3)
    print("[PASS] Problem 141: frugal number passed all tests.")
