/**
 * Problem: Climbing Stairs
 * LeetCode: #70 (Easy)
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class ClimbingStairs {
    public static int climbStairs(int n) {
        if (n <= 2) return n;
        int prev2 = 1, prev1 = 2;

        for (int i = 3; i <= n; i++) {
            int curr = prev1 + prev2;
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }

    public static void main(String[] args) {
        int n = 5;
        System.out.println("[Java] Climbing Stairs Test");
        System.out.println("Ways to climb " + n + " stairs: " + climbStairs(n));
    }
}
