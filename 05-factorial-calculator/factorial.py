"""
Problem 05: Factorial Calculator
Difficulty: Beginner / Easy

Problem Statement:
Given a non-negative integer `n`, compute its factorial (n!).
The factorial of n is the product of all positive integers less than or equal to n.
Special case: 0! = 1.
Example: 5! = 5 * 4 * 3 * 2 * 1 = 120

Concepts:
- Loops (for / while)
- Recursion fundamentals (Base case & Recursive step)
- Edge-case handling (n = 0, n < 0 validation)
"""

def factorial_iterative(n: int) -> int:
    """Method 1: Iterative Loop (O(N) time, O(1) space)"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Method 2: Recursion (O(N) time, O(N) stack space)"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 05: Factorial Calculator Tests")
    print("=" * 50)

    test_cases = [
        (0, 1),
        (1, 1),
        (3, 6),
        (5, 120),
        (6, 720),
        (10, 3628800),
    ]

    for num, expected in test_cases:
        res_iter = factorial_iterative(num)
        res_rec = factorial_recursive(num)
        print(f"Factorial of {num:2d} -> Iterative: {res_iter:<8} | Recursive: {res_rec:<8} | Expected: {expected}")
        assert res_iter == expected, f"Iterative failed for {num}"
        assert res_rec == expected, f"Recursive failed for {num}"

    # Test negative error handling
    try:
        factorial_iterative(-5)
    except ValueError:
        print("\nNegative input validation test: [PASS]")

    print("\n[PASS] All Factorial tests passed successfully!")
