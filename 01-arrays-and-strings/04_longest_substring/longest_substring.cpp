/**
 * Problem: Longest Substring Without Repeating Characters
 * LeetCode: #3 (Medium)
 * 
 * Approach: Sliding Window with Hash Map
 * Time Complexity: O(N)
 * Space Complexity: O(min(N, charset))
 */

#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

int lengthOfLongestSubstring(const std::string& s) {
    std::unordered_map<char, int> charMap;
    int maxLength = 0;
    int left = 0;

    for (int right = 0; right < static_cast<int>(s.length()); ++right) {
        char c = s[right];
        if (charMap.find(c) != charMap.end() && charMap[c] >= left) {
            left = charMap[c] + 1;
        }
        charMap[c] = right;
        maxLength = std::max(maxLength, right - left + 1);
    }
    return maxLength;
}

int main() {
    std::cout << "[C++] Longest Substring Test\n";
    std::string s = "pwwkew";
    std::cout << "String: \"" << s << "\" -> Max Length: " << lengthOfLongestSubstring(s) << " (Expected: 3)\n";
    return 0;
}
