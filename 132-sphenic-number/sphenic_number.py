"""
Problem 132: Sphenic Number Checker
A sphenic number is a positive integer that is the product of exactly three distinct prime numbers.
"""

def is_sphenic(n: int) -> bool:
    """Return True if n is a sphenic number, False otherwise."""
    if n <= 0:
        return False
    factors = []
    temp = n
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            temp //= d
            if temp % d == 0:
                return False
        d += 1
    if temp > 1:
        factors.append(temp)
    return len(factors) == 3

def sphenic_numbers_up_to(limit: int) -> list[int]:
    """Return all sphenic numbers up to limit."""
    return [x for x in range(1, limit + 1) if is_sphenic(x)]

def sphenic_triplet(n: int) -> tuple[int, int, int] | None:
    """Return the 3 distinct prime factors (p, q, r) if n is sphenic, else None."""
    if not is_sphenic(n):
        return None
    factors = []
    temp = n
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return tuple(factors) if len(factors) == 3 else None


if __name__ == "__main__":
    assert is_sphenic(30) is True   # 2 * 3 * 5
    assert is_sphenic(42) is True   # 2 * 3 * 7
    assert is_sphenic(60) is False  # 2^2 * 3 * 5 (not distinct)
    assert is_sphenic(8) is False   # 2^3
    assert is_sphenic(66) is True   # 2 * 3 * 11
    assert sphenic_numbers_up_to(70) == [30, 42, 66, 70]
    assert sphenic_triplet(30) == (2, 3, 5)
    assert sphenic_triplet(42) == (2, 3, 7)
    assert sphenic_triplet(60) is None
    print("[PASS] Problem 132: sphenic number passed all tests.")
