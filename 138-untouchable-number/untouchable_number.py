"""
Problem 138: Untouchable Number Checker
An untouchable number is a positive integer that cannot be expressed as the sum of
all proper divisors of any positive integer (aliquot sum s(k) != n for all k).
"""

def aliquot_sum(n: int) -> int:
    """Return the sum of proper divisors of n."""
    if n <= 1:
        return 0
    total = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            total += d
            if d * d != n:
                total += n // d
        d += 1
    return total

def is_untouchable_up_to(n: int, search_limit: int = 1000) -> bool:
    """Check if n is not the aliquot sum of any number up to search_limit."""
    for k in range(1, search_limit + 1):
        if aliquot_sum(k) == n:
            return False
    return True

def untouchable_numbers_up_to(limit: int, search_depth: int = 500) -> list[int]:
    """Return all untouchable numbers up to limit."""
    return [x for x in range(2, limit + 1) if is_untouchable_up_to(x, search_depth)]


if __name__ == "__main__":
    # 2, 5, 52, 88, 96, 120 are famous untouchable numbers
    assert aliquot_sum(6) == 6
    assert aliquot_sum(4) == 3
    assert is_untouchable_up_to(2, 500) is True
    assert is_untouchable_up_to(5, 500) is True
    assert is_untouchable_up_to(4, 500) is False # aliquot_sum(9) = 1 + 3 = 4
    assert 2 in untouchable_numbers_up_to(10)
    assert 5 in untouchable_numbers_up_to(10)
    print("[PASS] Problem 138: untouchable number passed all tests.")
