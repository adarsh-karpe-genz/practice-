"""
Problem 128: Powerful Number Checker
A positive integer n is powerful if for every prime factor p of n, p^2 also divides n.
"""

def is_powerful(n: int) -> bool:
    """Check if n is a powerful number."""
    if n <= 0:
        return False
    if n == 1:
        return True
    
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            if count < 2:
                return False
        d += 1
    if temp > 1:
        return False
    return True

def powerful_numbers(limit: int) -> list[int]:
    """Return all powerful numbers up to limit."""
    return [i for i in range(1, limit + 1) if is_powerful(i)]

if __name__ == "__main__":
    assert is_powerful(1) is True
    assert is_powerful(4) is True
    assert is_powerful(8) is True
    assert is_powerful(9) is True
    assert is_powerful(12) is False  # 12 = 2^2 * 3 (3^2 does not divide 12)
    assert is_powerful(16) is True
    assert is_powerful(36) is True
    assert powerful_numbers(36) == [1, 4, 8, 9, 16, 25, 27, 32, 36]
    print("[PASS] Problem 128: powerful number passed all tests.")
