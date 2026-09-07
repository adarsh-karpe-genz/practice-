"""
Problem 32: Collatz Conjecture - Count Steps to Reach 1
Difficulty: Beginner / Easy

Problem Statement:
The Collatz Conjecture says that for any positive integer N:
- If N is even: divide by 2
- If N is odd: multiply by 3 and add 1
Keep applying these rules until N becomes 1. Count the number of steps.
Example: N = 6 -> 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (8 steps)

Concepts:
- While loop with conditional branching
- Even/odd check with modulo
- Counting iterations
"""

def collatz_steps(n: int) -> int:
    """Count steps to reach 1 using Collatz rules."""
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


if __name__ == "__main__":
    print("=" * 50)
    print("Running Problem 32: Collatz Steps Tests")
    print("=" * 50)

    test_cases = [
        (1, 0),
        (6, 8),
        (27, 111),
        (2, 1),
        (4, 2),
        (16, 4),
    ]

    for n, expected in test_cases:
        res = collatz_steps(n)
        print(f"N = {n:4d} -> Steps: {res:4d} | Expected: {expected:4d}")
        assert res == expected, f"Failed for N={n}"

    print("\n[PASS] All Collatz Steps tests passed successfully!")
