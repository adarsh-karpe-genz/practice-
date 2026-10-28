"""
Problem 148: Extended Euclidean Algorithm
Find integers x, y such that a*x + b*y = gcd(a, b).
Also useful for finding modular inverses.
"""

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (gcd, x, y) such that a*x + b*y = gcd(a, b)."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a: int, m: int) -> int | None:
    """Find modular inverse of a modulo m, such that (a * x) % m == 1."""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    return (x % m + m) % m

if __name__ == "__main__":
    gcd, x, y = extended_gcd(30, 20)
    assert gcd == 10
    assert 30 * x + 20 * y == 10
    
    gcd, x, y = extended_gcd(35, 15)
    assert gcd == 5
    assert 35 * x + 15 * y == 5

    # Modular inverse tests
    inv = mod_inverse(3, 11)  # 3 * 4 = 12 = 1 mod 11
    assert inv == 4
    assert (3 * inv) % 11 == 1
    assert mod_inverse(6, 9) is None # gcd(6,9)=3 != 1
    print("[PASS] Problem 148: extended euclidean algorithm passed all tests.")
