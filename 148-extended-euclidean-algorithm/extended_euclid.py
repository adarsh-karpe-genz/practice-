"""
Problem 148: Extended Euclidean Algorithm
Description:
Computes the greatest common divisor (GCD) of two integers a and b,
as well as the coefficients x and y (Bézout coefficients) such that:
    a * x + b * y = gcd(a, b)
"""

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b).
    Recursive implementation.
    """
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)


def extended_gcd_iterative(a: int, b: int) -> tuple[int, int, int]:
    """
    Iterative implementation of the Extended Euclidean Algorithm.
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b).
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return (a, x0, y0)


def mod_inverse(a: int, m: int) -> int | None:
    """
    Computes modular inverse of a modulo m using Extended Euclidean Algorithm.
    Returns x such that (a * x) % m == 1, or None if inverse doesn't exist.
    """
    g, x, _ = extended_gcd_iterative(a, m)
    if g != 1:
        return None  # Inverse exists only if a and m are coprime
    return (x % m + m) % m


if __name__ == "__main__":
    test_cases = [(35, 15), (240, 46), (17, 3120), (101, 103)]
    for a, b in test_cases:
        g1, x1, y1 = extended_gcd(a, b)
        g2, x2, y2 = extended_gcd_iterative(a, b)
        assert g1 == g2, f"GCD mismatch for ({a}, {b})"
        assert a * x1 + b * y1 == g1, f"Bézout identity failed for ({a}, {b})"
        assert a * x2 + b * y2 == g2, f"Iterative Bézout identity failed for ({a}, {b})"

    # Test modular inverse
    inv = mod_inverse(3, 11)
    assert inv == 4 and (3 * inv) % 11 == 1
    assert mod_inverse(6, 9) is None

    print("[PASS] Problem 148: Extended Euclidean Algorithm tests passed successfully.")
