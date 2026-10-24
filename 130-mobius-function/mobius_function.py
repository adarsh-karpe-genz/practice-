"""
Problem 130: Möbius Function Calculator
The Möbius function mu(n):
- mu(1) = 1
- mu(n) = 0 if n has a squared prime factor
- mu(n) = (-1)^k if n is the product of k distinct primes
"""

def mobius(n: int) -> int:
    """Compute the Mobius function mu(n)."""
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 1
    
    prime_factors = 0
    temp = n
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            prime_factors += 1
            temp //= d
            if temp % d == 0:
                return 0
        d += 1
    if temp > 1:
        prime_factors += 1
        
    return -1 if (prime_factors % 2 == 1) else 1

if __name__ == "__main__":
    assert mobius(1) == 1
    assert mobius(2) == -1
    assert mobius(4) == 0
    assert mobius(6) == 1   # 2 * 3 -> 2 primes -> (-1)^2 = 1
    assert mobius(30) == -1 # 2 * 3 * 5 -> 3 primes -> (-1)^3 = -1
    assert mobius(12) == 0  # 4 divides 12
    print("[PASS] Problem 130: mobius function passed all tests.")
