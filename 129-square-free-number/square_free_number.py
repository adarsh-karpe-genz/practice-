"""
Problem 129: Square-Free Number Checker
An integer n is square-free if it is divisible by no square number other than 1.
"""

def is_square_free(n: int) -> bool:
    """Return True if n is square-free, False otherwise."""
    if n <= 0:
        return False
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            temp //= d
            if temp % d == 0:
                return False
        d += 1
    return True

def square_free_range(limit: int) -> list[int]:
    """Return all square-free numbers up to limit."""
    return [x for x in range(1, limit + 1) if is_square_free(x)]

if __name__ == "__main__":
    assert is_square_free(10) is True  # 2 * 5
    assert is_square_free(12) is False # divisible by 4
    assert is_square_free(30) is True  # 2 * 3 * 5
    assert is_square_free(18) is False # divisible by 9
    assert square_free_range(10) == [1, 2, 3, 5, 6, 7, 10]
    print("[PASS] Problem 129: square-free number passed all tests.")
