/**
 * Problem: Coin Change (Fewest number of coins)
 * LeetCode: #322 (Medium)
 * 
 * Approach: Bottom-up 1D DP Tabulation
 * Time Complexity: O(Amount * Coins.length)
 * Space Complexity: O(Amount)
 */

#include <stdio.h>
#include <stdlib.h>

int min(int a, int b) {
    return a < b ? a : b;
}

int coinChange(const int *coins, int coinsSize, int amount) {
    int maxVal = amount + 1;
    int *dp = (int *)malloc((amount + 1) * sizeof(int));
    for (int i = 0; i <= amount; i++) dp[i] = maxVal;
    dp[0] = 0;

    for (int i = 1; i <= amount; i++) {
        for (int j = 0; j < coinsSize; j++) {
            if (coins[j] <= i) {
                dp[i] = min(dp[i], dp[i - coins[j]] + 1);
            }
        }
    }

    int result = dp[amount] > amount ? -1 : dp[amount];
    free(dp);
    return result;
}

int main(void) {
    int coins[] = {1, 2, 5};
    int n = sizeof(coins) / sizeof(coins[0]);
    int amount = 11;

    int ans = coinChange(coins, n, amount);
    printf("[C] Coin Change Test\n");
    printf("Min coins for amount %d: %d (Expected: 3 [5+5+1])\n", amount, ans);
    return 0;
}
