/**
 * Problem: Longest Substring Without Repeating Characters
 * LeetCode: #3 (Medium)
 * 
 * Approach: Sliding Window with Hash Map
 * Time Complexity: O(N)
 * Space Complexity: O(min(N, charset))
 */

import java.util.HashMap;
import java.util.Map;

public class LongestSubstring {
    public static int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (map.containsKey(c) && map.get(c) >= left) {
                left = map.get(c) + 1;
            }
            map.put(c, right);
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }

    public static void main(String[] args) {
        System.out.println("[Java] Longest Substring Test");
        String s = "abcabcbb";
        System.out.println("String: \"" + s + "\" -> Max Length: " + lengthOfLongestSubstring(s) + " (Expected: 3)");
    }
}
