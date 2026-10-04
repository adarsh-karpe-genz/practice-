"""
Problem 81: Check Fascinating Number
Difficulty: Beginner / Easy

Problem Statement:
When a number (3 digits or more) is multiplied by 2 and 3, and the results
are concatenated with the original number (n + str(2*n) + str(3*n)),
if the concatenated string contains all digits from 1 to 9 exactly once,
then the number is called a Fascinating Number.
Example:
  192 -> 192 * 2 = 384, 192 * 3 = 576
  Concatenation: "192" + "384" + "576" = "192384576"
  Contains digits 1 to 9 exactly once -> True!

Concepts:
- String concatenation of multiples
- Frequency checking of characters '1' through '9'
- Set / sorted string comparison with "123456789"
"""

def is_fascinating(n: int) -> bool:
    """Check if n multiplied by 1, 2, 3 concatenated contains digits 1-9 once."""
    if n < 100:
        return False
    concat_str = str(n) + str(n * 2) + str(n * 3)
    return "".join(sorted(concat_str)) == "123456789"

if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 81: Fascinating Number Tests")
    print("=" * 50)

    test_cases = [
        (192, True),
        (219, True),
        (273, True),
        (327, True),
        (100, False),
        (853, False),
    ]

    for num, expected in test_cases:
        res = is_fascinating(num)
        print(f"Num: {num:3d} -> Fascinating? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Fascinating Number tests passed successfully!")
