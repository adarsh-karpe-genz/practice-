"""
Problem 147: Modular Exponentiation
Compute (base^exp) % mod efficiently in O(log exp) time using binary exponentiation.
"""

def power_mod(base: int, exp: int, mod: int) -> int:
    """Compute (base^exp) % mod using repeated squaring."""
    if mod == 1:
        return 0
    if exp < 0:
        raise ValueError("Exponent must be non-negative")
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def power_mod_recursive(base: int, exp: int, mod: int) -> int:
    """Compute (base^exp) % mod recursively in O(log exp)."""
    if mod == 1:
        return 0
    if exp == 0:
        return 1
    half = power_mod_recursive(base, exp // 2, mod)
    res = (half * half) % mod
    if exp % 2 == 1:
        res = (res * base) % mod
    return res


if __name__ == "__main__":
    assert power_mod(2, 10, 1000) == 24   # 1024 % 1000 = 24
    assert power_mod(3, 7, 13) == 3       # 2187 % 13 = 3
    assert power_mod(5, 0, 100) == 1
    assert power_mod(10, 5, 1) == 0
    assert power_mod(7, 256, 13) == pow(7, 256, 13)
    assert power_mod_recursive(2, 10, 1000) == 24
    assert power_mod_recursive(3, 7, 13) == 3
    print("[PASS] Problem 147: modular exponentiation passed all tests.")
