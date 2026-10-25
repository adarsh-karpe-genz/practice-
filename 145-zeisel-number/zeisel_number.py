"""
Problem 145: Zeisel Number Checker
A Zeisel number is a square-free integer n with at least three prime factors
p_1 < p_2 < ... < p_k such that p_i = A * p_{i-1} + B for constants A and B.
"""

def get_prime_factors(n: int) -> list[int] | None:
    """Return distinct prime factors of square-free n, or None if not square-free."""
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            temp //= d
            if temp % d == 0:
                return None  # not square-free
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors

def is_zeisel(n: int) -> bool:
    """Check if n is a Zeisel number."""
    if n <= 1:
        return False
    factors = get_prime_factors(n)
    if factors is None or len(factors) < 3:
        return False
    
    # Check if there exist integers A, B such that p_{i+1} = A * p_i + B for all i
    p1, p2, p3 = factors[0], factors[1], factors[2]
    # Solve system:
    # p2 = A * p1 + B
    # p3 = A * p2 + B
    # => p3 - p2 = A * (p2 - p1)
    diff1 = p2 - p1
    diff2 = p3 - p2
    if diff1 == 0 or diff2 % diff1 != 0:
        return False
    A = diff2 // diff1
    B = p2 - A * p1
    
    # Check all subsequent factors
    for i in range(len(factors) - 1):
        if factors[i + 1] != A * factors[i] + B:
            return False
    return True

if __name__ == "__main__":
    # 105 = 3 * 5 * 7: diffs are 2, 2 => A=1, B=2. Zeisel!
    assert is_zeisel(105) is True
    # 1419 = 3 * 11 * 43: diffs: 11 - 3 = 8, 43 - 11 = 32 => A = 32/8 = 4, B = 11 - 4*3 = -1.
    # 4 * 11 - 1 = 43. Zeisel!
    assert is_zeisel(1419) is True
    # 30 = 2 * 3 * 5: A = 2, B = -1 => p2 = 2*2 - 1 = 3, p3 = 2*3 - 1 = 5. Zeisel!
    assert is_zeisel(30) is True
    assert is_zeisel(12) is False # Not square-free
    assert is_zeisel(7) is False  # Prime (fewer than 3 prime factors)
    print("[PASS] Problem 145: zeisel number passed all tests.")
