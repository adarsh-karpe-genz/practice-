"""
Problem 94: Check Fermat Number
Difficulty: Beginner / Easy

Problem Statement:
A Fermat number is a positive integer of the form:
  F_n = 2^(2^n) + 1, where n >= 0.
First few Fermat numbers:
  n = 0 -> 2^(2^0) + 1 = 2^1 + 1 = 3
  n = 1 -> 2^(2^1) + 1 = 2^2 + 1 = 5
  n = 2 -> 2^(2^2) + 1 = 2^4 + 1 = 17
  n = 3 -> 2^(2^3) + 1 = 2^8 + 1 = 257
  n = 4 -> 2^(2^4) + 1 = 2^16 + 1 = 65537

Concepts:
- Double exponentiation: 2**(2**n) + 1
- Power-of-two subtraction check
- Number theory
"""

def is_fermat_number(val: int) -> bool:
    """Check if val is of the form 2^(2^n) + 1 for n >= 0."""
    if val < 3:
        return False
    # val - 1 must be a power of two: 2^(2^n)
    target = val - 1
    if (target & (target - 1)) != 0:
        return False
    # The exponent itself (bit length - 1) must be a power of 2
    exp = target.bit_length() - 1
    return exp > 0 and (exp & (exp - 1)) == 0

def fermat_sequence(count: int) -> list[int]:
    """Generate first count Fermat numbers F_n = 2^(2^n) + 1 starting from n=0."""
    return [(1 << (1 << n)) + 1 for n in range(count)]


def get_fermat_index(val: int) -> int | None:
    """Return n such that val = 2^(2^n) + 1, or None if not a Fermat number."""
    if val < 3:
        return None
    temp = val - 1
    if (temp & (temp - 1)) != 0:
        return None
    power_of_two = temp.bit_length() - 1
    if (power_of_two & (power_of_two - 1)) != 0:
        return None
    return power_of_two.bit_length() - 1


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 94: Fermat Number Tests")
    print("=" * 50)

    test_cases = [
        (3, True),
        (5, True),
        (17, True),
        (257, True),
        (65537, True),
        (9, False),   # 9 - 1 = 8 = 2^3, but 3 is not a power of 2
        (10, False),
        (33, False),  # 33 - 1 = 32 = 2^5, but 5 is not a power of 2
    ]

    for num, expected in test_cases:
        res = is_fermat_number(num)
        print(f"Num: {num:5d} -> Fermat? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"
    assert fermat_sequence(5) == [3, 5, 17, 257, 65537]
    assert get_fermat_index(257) == 3
    assert get_fermat_index(33) is None

    print("\n[PASS] All Fermat Number tests passed successfully!")
