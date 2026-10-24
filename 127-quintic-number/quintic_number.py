"""
Problem 127: Quintic Number Checker and Generator
A quintic number (or fifth power) is an integer of the form n = k^5 for some integer k.
"""

def is_quintic(n: int) -> bool:
    """Check if n is a quintic number (fifth power)."""
    if n < 0:
        return is_quintic(-n)
    if n == 0:
        return True
    root = round(n ** 0.2)
    return root ** 5 == n

def quintic_range(count: int) -> list[int]:
    """Return the first count quintic numbers starting from 1."""
    return [i ** 5 for i in range(1, count + 1)]

if __name__ == "__main__":
    assert is_quintic(32) is True
    assert is_quintic(243) is True
    assert is_quintic(100) is False
    assert is_quintic(0) is True
    assert is_quintic(-32) is True
    assert quintic_range(5) == [1, 32, 243, 1024, 3125]
    print("[PASS] Problem 127: quintic number passed all tests.")
