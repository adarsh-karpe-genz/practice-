"""
Problem 146: Carmichael Function lambda(n)
The Carmichael function lambda(n) is the smallest positive integer m such that
a^m == 1 (mod n) for all integers a coprime to n.
"""
import math

def lcm(a: int, b: int) -> int:
    """Return least common multiple of a and b."""
    return (a * b) // math.gcd(a, b)

def prime_factorization(n: int) -> list[tuple[int, int]]:
    """Return prime factors of n as [(p, e), ...]."""
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

def lambda_prime_power(p: int, k: int) -> int:
    """Compute lambda(p^k)."""
    if p == 2:
        if k == 1:
            return 1
        elif k == 2:
            return 2
        else:
            return 2 ** (k - 2)
    else:
        return (p - 1) * (p ** (k - 1))

def carmichael_lambda(n: int) -> int:
    """Compute Carmichael function lambda(n)."""
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 1
    factors = prime_factorization(n)
    res = 1
    for p, k in factors:
        res = lcm(res, lambda_prime_power(p, k))
    return res

def euler_totient(n: int) -> int:
    """Euler phi function for comparison with Carmichael lambda."""
    factors = prime_factorization(n)
    res = n
    for p, _ in factors:
        res = res * (p - 1) // p
    return res


def totient_carmichael_ratio(n: int) -> float:
    """Ratio phi(n) / lambda(n), which is always an integer >= 1."""
    return euler_totient(n) / carmichael_lambda(n)


if __name__ == "__main__":
    assert carmichael_lambda(1) == 1
    assert carmichael_lambda(8) == 2   # phi(8)=4, but lambda(8)=2 (since 1^2, 3^2, 5^2, 7^2 == 1 mod 8)
    assert carmichael_lambda(12) == 2  # lcm(lambda(4), lambda(3)) = lcm(2, 2) = 2
    assert carmichael_lambda(15) == 4  # lcm(lambda(3), lambda(5)) = lcm(2, 4) = 4
    assert carmichael_lambda(35) == 12 # lcm(4, 6) = 12
    assert totient_carmichael_ratio(8) == 2.0  # phi(8)=4, lambda(8)=2
    assert totient_carmichael_ratio(15) == 2.0 # phi(15)=8, lambda(15)=4
    print("[PASS] Problem 146: carmichael function passed all tests.")
