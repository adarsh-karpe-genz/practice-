"""
Problem 75: Check Disarium Number
Difficulty: Beginner / Easy

Problem Statement:
A number is called a Disarium Number if the sum of its digits powered with
their respective positions (1-indexed from left to right) is equal to the number itself.
Examples:
  89  -> 8^1 + 9^2 = 8 + 81 = 89 -> True (Disarium)
  135 -> 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135 -> True (Disarium)
  175 -> 1^1 + 7^2 + 5^3 = 1 + 49 + 125 = 175 -> True (Disarium)
  80  -> 8^1 + 0^2 = 8 != 80 -> False

Concepts:
- String iteration with index tracking via enumerate(s, start=1)
- Exponentiation **
- Positional digit sum logic
"""

def is_disarium(n: int) -> bool:
    """Check if the sum of digits raised to their 1-based positions equals n."""
    if n < 0:
        return False
    s = str(n)
    total = sum(int(digit) ** pos for pos, digit in enumerate(s, start=1))
    return total == n


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 75: Disarium Number Tests")
    print("=" * 50)

    test_cases = [
        (89, True),
        (135, True),
        (175, True),
        (518, True),    # 5^1 + 1^2 + 8^3 = 5 + 1 + 512 = 518
        (1, True),      # 1^1 = 1
        (80, False),
        (100, False),
    ]

    for num, expected in test_cases:
        res = is_disarium(num)
        print(f"Number: {num:4d} -> Disarium? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Disarium Number tests passed successfully!")
