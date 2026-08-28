/**
 * Problem: Maximum Subarray Sum (Kadane's Algorithm)
 * LeetCode: #53 (Medium)
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <iostream>
#include <vector>
#include <algorithm>

int maxSubArray(const std::vector<int>& nums) {
    int maxSoFar = nums[0];
    int currMax = nums[0];

    for (size_t i = 1; i < nums.size(); ++i) {
        currMax = std::max(nums[i], currMax + nums[i]);
        maxSoFar = std::max(maxSoFar, currMax);
    }
    return maxSoFar;
}

int main() {
    std::cout << "[C++] Kadane's Algorithm Test\n";
    std::vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int result = maxSubArray(nums);
    std::cout << "Max Subarray Sum: " << result << " (Expected: 6)\n";
    return 0;
}
