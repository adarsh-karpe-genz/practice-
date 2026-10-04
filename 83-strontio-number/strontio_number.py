"""
Problem 83: Check Strontio Number
Difficulty: Beginner / Easy

Problem Statement:
A four-digit number is called a Strontio number if multiplying it by 2
produces a number whose tens and hundreds digits are identical.
Examples:
  1386 -> 1386 * 2 = 2772 -> Hundreds: 7, Tens: 7 -> 7 == 7 -> True
  1221 -> 1221 * 2 = 2442 -> Hundreds: 4, Tens: 4 -> 4 == 4 -> True
  1000 -> 1000 * 2 = 2000 -> Hundreds: 0, Tens: 0 -> True
  1234 -> 1234 * 2 = 2468 -> Hundreds: 4, Tens: 6 -> 4 != 6 -> False

Concepts:
- Integer multiplication
- Digit extraction via integer division and modulo: (val // 100) % 10 and (val // 10) % 10
- Four-digit range boundary check (1000 to 9999)
"""

def is_strontio(n: int) -> bool:
    """Check if 4-digit number n multiplied by 2 has matching tens and hundreds digits."""
    if n < 1000 or n > 9999:
        return False
    val = n * 2
    hundreds = (val // 100) % 10
    tens = (val // 10) % 10
    return hundreds == tens


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 83: Strontio Number Tests")
    print("=" * 50)

    test_cases = [
        (1386, True),
        (1221, True),
        (1000, True),
        (1111, True),   # 1111 * 2 = 2222 -> 2 == 2
        (1234, False),
        (999, False),   # not 4 digits
        (10000, False), # not 4 digits
    ]

    for num, expected in test_cases:
        res = is_strontio(num)
        print(f"Number: {num:4d} (x2 = {num*2:5d}) -> Strontio? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Strontio Number tests passed successfully!")
