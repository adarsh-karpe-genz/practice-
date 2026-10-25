"""
Problem 144: Giuga Number Checker
A Giuga number is a composite number n such that for every distinct prime factor p of n:
p divides (n/p - 1), or equivalently n/p == 1 (mod p).
"""

def prime_factors(n: int) -> list[int]:
    """Return distinct prime factors of n."""
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors

def is_giuga(n: int) -> bool:
    """Check if composite number n is a Giuga number."""
    if n <= 3:
        return False
    primes = prime_factors(n)
    if len(primes) <= 1:
        # Must be composite and not prime/prime power
        return False
    for p in primes:
        if (n // p - 1) % p != 0:
            return False
    return True

if __name__ == "__main__":
    # Smallest Giuga number is 30: prime factors 2, 3, 5:
    # 30/2 - 1 = 14 (divisible by 2)
    # 30/3 - 1 = 9 (divisible by 3)
    # 30/5 - 1 = 5 (divisible by 5)
    assert is_giuga(30) is True
    assert is_giuga(6) is False  # 6/2 - 1 = 2 (div by 2), but 6/3 - 1 = 1 (not div by 3)
    assert is_giuga(12) is False
    print("[PASS] Problem 144: giuga number passed all tests.")
