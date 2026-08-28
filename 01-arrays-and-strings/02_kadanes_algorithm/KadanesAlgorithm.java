/**
 * Problem: Maximum Subarray Sum (Kadane's Algorithm)
 * LeetCode: #53 (Medium)
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class KadanesAlgorithm {
    public static int maxSubArray(int[] nums) {
        int maxSoFar = nums[0];
        int currMax = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currMax = Math.max(nums[i], currMax + nums[i]);
            maxSoFar = Math.max(maxSoFar, currMax);
        }
        return maxSoFar;
    }

    public static void main(String[] args) {
        System.out.println("[Java] Kadane's Algorithm Test");
        int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        int ans = maxSubArray(nums);
        System.out.println("Max Subarray Sum: " + ans);
    }
}
