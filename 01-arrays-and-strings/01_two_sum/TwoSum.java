/**
 * Problem: Two Sum
 * LeetCode: #1 (Easy)
 * 
 * Approach: Hash Map lookup (Single Pass)
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        System.out.println("[Java] Two Sum Test");
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;

        int[] res = twoSum(nums, target);
        System.out.println("Array: " + Arrays.toString(nums) + ", Target: " + target);
        System.out.println("Result Indices: " + Arrays.toString(res));
    }
}
