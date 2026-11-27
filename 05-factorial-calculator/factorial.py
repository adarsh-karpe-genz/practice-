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
    """Method 1: Iterative Loop"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Method 2: Recursive approach"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def count_trailing_zeros(n: int) -> int:
    """Calculates number of trailing zeros in n! using Legendre formula."""
    count = 0
    k = 5
    while k <= n:
        count += n // k
        k *= 5
    return count


def double_factorial(n: int) -> int:
    """
    Computes double factorial n!! = n * (n-2) * (n-4) ...
    Examples: 5!! = 5 * 3 * 1 = 15; 6!! = 6 * 4 * 2 = 48.
    """
    if n < 0:
        raise ValueError("Double factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    res = 1
    for i in range(n, 0, -2):
        res *= i
    return res


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 05: Factorial Tests")
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
        assert factorial_iterative(num) == expected
        assert factorial_recursive(num) == expected

    # Test negative error handling
    try:
        factorial_iterative(-5)
    except ValueError:
        pass

    assert count_trailing_zeros(5) == 1
    assert count_trailing_zeros(10) == 2
    assert count_trailing_zeros(25) == 6

    # Test double factorial
    assert double_factorial(5) == 15
    assert double_factorial(6) == 48
    assert double_factorial(0) == 1

    print("[PASS] All Factorial tests passed successfully!")
