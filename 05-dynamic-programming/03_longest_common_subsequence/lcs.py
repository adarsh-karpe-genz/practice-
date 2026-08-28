"""
Problem: Longest Common Subsequence (LCS)
LeetCode: #1143 (Medium)

Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

if __name__ == "__main__":
    print("[Python] LCS Test")
    tests = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
    ]
    for s1, s2, expected in tests:
        res = longest_common_subsequence(s1, s2)
        print(f"'{s1}', '{s2}' -> LCS: {res} | Expected: {expected}")
        assert res == expected
    print("LCS tests passed!")
