/**
 * Problem: Longest Common Subsequence (LCS)
 * LeetCode: #1143 (Medium)
 * 
 * Approach: 2D Dynamic Programming Tabulation
 * Time Complexity: O(M * N)
 * Space Complexity: O(M * N)
 */

#include <stdio.h>
#include <string.h>

int max(int a, int b) { return a > b ? a : b; }

int longestCommonSubsequence(const char *text1, const char *text2) {
    int m = strlen(text1);
    int n = strlen(text2);

    int dp[m + 1][n + 1];

    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            } else if (text1[i - 1] == text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[m][n];
}

int main(void) {
    const char *s1 = "abcde";
    const char *s2 = "ace";

    int len = longestCommonSubsequence(s1, s2);
    printf("[C] Longest Common Subsequence Test\n");
    printf("LCS length between \"%s\" and \"%s\": %d (Expected: 3)\n", s1, s2, len);
    return 0;
}
