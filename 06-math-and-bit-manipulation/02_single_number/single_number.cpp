/**
 * Problem: Single Number
 * LeetCode: #136 (Easy)
 * 
 * Approach: Bitwise XOR
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <iostream>
#include <vector>

int singleNumber(const std::vector<int>& nums) {
    int unique = 0;
    for (int num : nums) {
        unique ^= num;
    }
    return unique;
}

int main() {
    std::cout << "[C++] Single Number Test\n";
    std::vector<int> nums = {4, 1, 2, 1, 2};
    std::cout << "Single number is: " << singleNumber(nums) << " (Expected: 4)\n";
    return 0;
}
