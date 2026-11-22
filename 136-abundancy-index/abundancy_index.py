"""
Problem 136: Abundancy Index and Classification
The abundancy index of n is sigma(n) / n.
- Deficient if index < 2
- Perfect if index == 2
- Abundant if index > 2
"""

def sum_of_divisors(n: int) -> int:
    """Calculate sum of all divisors of n."""
    if n <= 0:
        return 0
    total = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            total += d
            if d * d != n:
                total += n // d
        d += 1
    return total

def abundancy_index(n: int) -> float:
    """Compute the abundancy index sigma(n)/n."""
    if n <= 0:
        raise ValueError("n must be positive")
    return sum_of_divisors(n) / n

def classify_abundancy(n: int) -> str:
    """Classify n as 'deficient', 'perfect', or 'abundant'."""
    idx = abundancy_index(n)
    if idx < 2.0:
        return "deficient"
    elif idx == 2.0:
        return "perfect"
    else:
        return "abundant"

def are_friendly_numbers(a: int, b: int) -> bool:
    """Two numbers are friendly if they share the exact same abundancy index sigma(n)/n."""
    if a <= 0 or b <= 0:
        return False
    # Use exact integer cross-multiplication: sigma(a)*b == sigma(b)*a
    return sum_of_divisors(a) * b == sum_of_divisors(b) * a


if __name__ == "__main__":
    assert abundancy_index(6) == 2.0
    assert classify_abundancy(6) == "perfect"
    assert classify_abundancy(28) == "perfect"
    assert classify_abundancy(12) == "abundant" # (1+2+3+4+6+12)/12 = 28/12 > 2
    assert classify_abundancy(8) == "deficient" # (1+2+4+8)/8 = 15/8 < 2
    assert are_friendly_numbers(6, 28) is True  # both perfect (index = 2)
    assert are_friendly_numbers(30, 140) is True  # both share index 12/5 = 2.4
    print("[PASS] Problem 136: abundancy index passed all tests.")
