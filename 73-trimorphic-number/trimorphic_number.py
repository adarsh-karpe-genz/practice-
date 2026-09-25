"""
Problem 73: Check Trimorphic Number
Difficulty: Beginner / Easy

Problem Statement:
A number is called a Trimorphic Number if its cube ends with the number itself.
Examples:
  4  -> 4^3  = 64   (ends in 4)   -> True (Trimorphic)
  5  -> 5^3  = 125  (ends in 5)   -> True (Trimorphic)
  24 -> 24^3 = 13824 (ends in 24) -> True (Trimorphic)
  3  -> 3^3  = 27   (ends in 7)   -> False

Concepts:
- Number cubing (n ** 3)
- String suffix checking with endswith()
- Number theory properties
"""

def is_trimorphic(n: int) -> bool:
    """Check if n^3 ends with n."""
    if n < 0:
        return False
    cube = n ** 3
    return str(cube).endswith(str(n))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 73: Trimorphic Number Tests")
    print("=" * 50)

    test_cases = [
        (4, True),
        (5, True),
        (24, True),
        (25, True),   # 25^3 = 15625
        (49, True),   # 49^3 = 117649
        (3, False),
        (7, False),
        (0, True),    # 0^3 = 0
        (1, True),    # 1^3 = 1
    ]

    for num, expected in test_cases:
        res = is_trimorphic(num)
        print(f"Number: {num:3d} (Cube: {num**3:7d}) -> Trimorphic? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Trimorphic Number tests passed successfully!")
