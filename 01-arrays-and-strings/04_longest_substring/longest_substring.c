/**
 * Problem: Longest Substring Without Repeating Characters
 * LeetCode: #3 (Medium)
 * 
 * Approach: Sliding Window with ASCII index table
 * Time Complexity: O(N)
 * Space Complexity: O(1) (fixed 256 size array)
 */

#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(const char *s) {
    int lastSeen[256];
    for (int i = 0; i < 256; i++) lastSeen[i] = -1;

    int maxLength = 0;
    int start = 0;

    for (int end = 0; s[end] != '\0'; end++) {
        unsigned char c = (unsigned char)s[end];
        if (lastSeen[c] >= start) {
            start = lastSeen[c] + 1;
        }
        lastSeen[c] = end;
        int currentLen = end - start + 1;
        if (currentLen > maxLength) {
            maxLength = currentLen;
        }
    }
    return maxLength;
}

int main(void) {
    const char *testStr = "abcabcbb";
    int ans = lengthOfLongestSubstring(testStr);
    printf("[C] Longest Substring Test\n");
    printf("String: %s -> Max Length: %d (Expected: 3)\n", testStr, ans);
    return 0;
}
