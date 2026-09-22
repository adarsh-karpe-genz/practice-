"""
Problem 69: Check Spy Number
Difficulty: Beginner / Easy

Problem Statement:
A number is called a Spy Number if the sum of all its digits is equal
to the product of all its digits.
Examples:
  1124 -> Sum: 1 + 1 + 2 + 4 = 8, Product: 1 * 1 * 2 * 4 = 8 -> True (Spy Number)
  123  -> Sum: 1 + 2 + 3 = 6, Product: 1 * 2 * 3 = 6 -> True (Spy Number)
  124  -> Sum: 1 + 2 + 4 = 7, Product: 1 * 2 * 4 = 8 -> False

Concepts:
- Modulo % and integer division // for digit extraction
- Running accumulator for sum and product
- Integer comparison
"""

def is_spy_number(n: int) -> bool:
    """Check if the sum of digits of n equals the product of digits."""
    if n < 0:
        return False
    if n == 0:
        return True

    temp = n
    digit_sum = 0
    digit_prod = 1

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        digit_prod *= digit
        temp //= 10

    return digit_sum == digit_prod


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 69: Spy Number Tests")
    print("=" * 50)

    test_cases = [
        (1124, True),
        (123, True),
        (22, True),    # 2+2=4, 2*2=4
        (124, False),
        (132, True),
        (7, True),     # single digit: sum=7, prod=7
        (0, True),
    ]

    for num, expected in test_cases:
        res = is_spy_number(num)
        print(f"Number: {num:4d} -> Spy Number? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Spy Number tests passed successfully!")
