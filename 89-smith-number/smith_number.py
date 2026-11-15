"""
Problem 89: Check Smith Number
Difficulty: Beginner / Easy

Problem Statement:
A Smith Number is a composite number whose sum of digits is equal to the sum
of digits of all its prime factors (with multiplicity).
Examples:
  666 -> Composite!
         Sum of digits: 6 + 6 + 6 = 18
         Prime factorization: 2 * 3 * 3 * 37
         Sum of digits of factors: 2 + 3 + 3 + (3 + 7) = 18 -> True!
  4   -> Prime factors: 2, 2 -> 2 + 2 = 4 -> True!
  13  -> Prime (Smith numbers must be composite) -> False

Concepts:
- Prime factorization with multiplicity
- Sum of digits helper function
- Distinction between composite and prime numbers
"""

def sum_digits(n: int) -> int:
    """Helper to return sum of digits of n."""
    return sum(int(d) for d in str(abs(n)))

def prime_factors(n: int) -> list:
    """Return list of prime factors of n with multiplicity."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_smith_number(n: int) -> bool:
    """Check if composite number n is a Smith number."""
    if n <= 3:
        return False
    factors = prime_factors(n)
    if len(factors) <= 1:
        return False  # Prime numbers are not Smith numbers
    sum_orig = sum_digits(n)
    sum_factors = sum(sum_digits(f) for f in factors)
    return sum_orig == sum_factors

def smith_factorization_details(n: int) -> tuple[int, list[int], int]:
    """Return (sum of digits of n, prime factors, sum of digits of factors)."""
    def _sum_digits(x: int) -> int:
        return sum(int(d) for d in str(x))
    factors = []
    temp = n
    d = 2
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return _sum_digits(n), factors, sum(_sum_digits(f) for f in factors)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 89: Smith Number Tests")
    print("=" * 50)

    test_cases = [
        (4, True),
        (22, True),    # 2 + 2 = 4; factors: 2, 11 -> 2 + 1 + 1 = 4
        (27, True),    # 2 + 7 = 9; factors: 3, 3, 3 -> 3 + 3 + 3 = 9
        (666, True),
        (85, True),    # 8 + 5 = 13; factors: 5, 17 -> 5 + 1 + 7 = 13
        (13, False),   # prime
        (6, False),    # 6 != 2 + 3
    ]

    for num, expected in test_cases:
        res = is_smith_number(num)
        print(f"Num: {num:3d} -> Smith Number? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"
    d_sum, factors, f_sum = smith_factorization_details(22)
    assert d_sum == f_sum == 4 and factors == [2, 11]

    print("\n[PASS] All Smith Number tests passed successfully!")
