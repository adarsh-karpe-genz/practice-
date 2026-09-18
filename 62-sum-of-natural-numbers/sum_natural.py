"""
Problem 62: Sum of First N Natural Numbers
Difficulty: Beginner / Easy

Problem Statement:
Given a positive integer N, calculate the sum of all natural numbers from 1 to N.
Formula: N * (N + 1) // 2
Example: N = 5 -> 1 + 2 + 3 + 4 + 5 = 15

Concepts:
- Gauss formula O(1) time
- Iterative loop comparison O(N)
- Mathematical derivation verification
"""

def sum_natural_formula(n: int) -> int:
    """Calculate sum of 1 to n using formula O(1)."""
    if n < 1:
        return 0
    return n * (n + 1) // 2


def sum_natural_loop(n: int) -> int:
    """Calculate sum using loop O(N)."""
    return sum(range(1, n + 1))


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 62: Sum of Natural Numbers Tests")
    print("=" * 50)

    test_cases = [1, 5, 10, 100, 1000]

    for n in test_cases:
        r1 = sum_natural_formula(n)
        r2 = sum_natural_loop(n)
        print(f"N = {n:4d} -> Sum: {r1:7d}")
        assert r1 == r2

    assert sum_natural_formula(5) == 15
    assert sum_natural_formula(10) == 55
    assert sum_natural_formula(100) == 5050

    print("\n[PASS] All Sum of Natural Numbers tests passed successfully!")
