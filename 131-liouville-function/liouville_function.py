"""
Problem 131: Liouville Function Calculator
The Liouville function lambda(n) = (-1)^Omega(n), where Omega(n) is the total
number of prime factors of n counted with multiplicity.
"""

def prime_factors_mult_count(n: int) -> int:
    """Count total prime factors with multiplicity Omega(n)."""
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

def liouville(n: int) -> int:
    """Compute Liouville function lambda(n)."""
    if n <= 0:
        raise ValueError("n must be positive")
    omega = prime_factors_mult_count(n)
    return -1 if (omega % 2 == 1) else 1

if __name__ == "__main__":
    assert liouville(1) == 1
    assert liouville(2) == -1
    assert liouville(4) == 1   # 2*2 -> 2 factors -> (-1)^2 = 1
    assert liouville(6) == 1   # 2*3 -> 2 factors
    assert liouville(8) == -1  # 2*2*2 -> 3 factors -> (-1)^3 = -1
    assert liouville(12) == -1 # 2*2*3 -> 3 factors
    print("[PASS] Problem 131: liouville function passed all tests.")
