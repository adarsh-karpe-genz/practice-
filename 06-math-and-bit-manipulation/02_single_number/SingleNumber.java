/**
 * Problem: Single Number
 * LeetCode: #136 (Easy)
 * 
 * Approach: Bitwise XOR
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class SingleNumber {
    public static int singleNumber(int[] nums) {
        int unique = 0;
        for (int num : nums) {
            unique ^= num;
        }
        return unique;
    }

    public static void main(String[] args) {
        int[] nums = { 4, 1, 2, 1, 2 };
        System.out.println("[Java] Single Number Test");
        System.out.println("Single number: " + singleNumber(nums));
    }
}
