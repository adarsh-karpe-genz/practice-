"""
Problem: Climbing Stairs
LeetCode: #70 (Easy)

Time Complexity: O(N)
Space Complexity: O(1)
"""

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1

if __name__ == "__main__":
    print("[Python] Climbing Stairs Test")
    tests = [(2, 2), (3, 3), (4, 5), (5, 8)]
    for n, expected in tests:
        res = climb_stairs(n)
        print(f"n: {n} -> Ways: {res} | Expected: {expected}")
        assert res == expected
    print("Climbing stairs tests passed!")
