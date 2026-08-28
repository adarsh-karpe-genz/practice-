/**
 * Problem: Coin Change
 * LeetCode: #322 (Medium)
 * 
 * Time Complexity: O(Amount * N)
 * Space Complexity: O(Amount)
 */

import java.util.Arrays;

public class CoinChange {
    public static int coinChange(int[] coins, int amount) {
        int max = amount + 1;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, max);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }

    public static void main(String[] args) {
        int[] coins = { 1, 2, 5 };
        int amount = 11;
        System.out.println("[Java] Coin Change Test");
        System.out.println("Min coins: " + coinChange(coins, amount));
    }
}
