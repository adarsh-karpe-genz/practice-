"""
Problem 79: Check Fascinating Number
Difficulty: Beginner / Easy

Problem Statement:
When a number (3 digits or more) is multiplied by 2 and 3, and the results
are concatenated with the original number (n + str(n*2) + str(n*3)),
if the resulting concatenated string contains all digits from 1 to 9 exactly once,
then it is called a Fascinating Number.
Examples:
  192 -> 192 * 2 = 384, 192 * 3 = 576 -> Concatenated: "192384576"
         Contains digits 1 to 9 each once -> True (Fascinating)
  219 -> 219 * 2 = 438, 219 * 3 = 657 -> Concatenated: "219438657" -> True

Concepts:
- Number multiplication and string concatenation
- Sorting digits and checking against "123456789"
"""

def is_fascinating(n: int) -> bool:
    """Check if n is a fascinating number."""
    if n < 100:
        return False
    concat_str = f"{n}{n * 2}{n * 3}"
    return "".join(sorted(concat_str)) == "123456789"


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 79: Fascinating Number Tests")
    print("=" * 50)

    test_cases = [
        (192, True),
        (219, True),
        (273, True),
        (327, True),
        (100, False),
        (123, False),
        (85, False),
    ]

    for num, expected in test_cases:
        res = is_fascinating(num)
        print(f"Number: {num:3d} -> Fascinating? {res:<5} | Expected: {expected}")
        assert res == expected, f"Failed for {num}"

    print("\n[PASS] All Fascinating Number tests passed successfully!")
