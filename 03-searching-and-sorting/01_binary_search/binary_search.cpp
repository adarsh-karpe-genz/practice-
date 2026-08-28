/**
 * Problem: Binary Search
 * LeetCode: #704 (Easy)
 * 
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */

#include <iostream>
#include <vector>

int search(const std::vector<int>& nums, int target) {
    int left = 0;
    int right = static_cast<int>(nums.size()) - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    std::cout << "[C++] Binary Search Test\n";
    std::vector<int> nums = {-1, 0, 3, 5, 9, 12};
    int target = 9;
    std::cout << "Target " << target << " found at index: " << search(nums, target) << "\n";
    return 0;
}
