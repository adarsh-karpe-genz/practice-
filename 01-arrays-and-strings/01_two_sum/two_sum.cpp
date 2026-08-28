/**
 * Problem: Two Sum
 * LeetCode: #1 (Easy)
 * 
 * Approach: Hash Map lookup (Single Pass)
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */

#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> twoSum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen; // value -> index

    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        int complement = target - nums[i];
        if (seen.count(complement)) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {};
}

int main() {
    std::cout << "[C++] Two Sum Test\n";
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    std::vector<int> ans = twoSum(nums, target);
    if (!ans.empty()) {
        std::cout << "Target: " << target << "\n";
        std::cout << "Indices: [" << ans[0] << ", " << ans[1] << "]\n";
        std::cout << "Values: " << nums[ans[0]] << " + " << nums[ans[1]] << " = " << target << "\n";
    }
    return 0;
}
