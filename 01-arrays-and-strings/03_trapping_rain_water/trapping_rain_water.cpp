/**
 * Problem: Trapping Rain Water
 * LeetCode: #42 (Hard)
 * 
 * Approach: Two Pointers
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <iostream>
#include <vector>
#include <algorithm>

int trap(const std::vector<int>& height) {
    int left = 0, right = static_cast<int>(height.size()) - 1;
    int leftMax = 0, rightMax = 0;
    int totalWater = 0;

    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                totalWater += (leftMax - height[left]);
            }
            left++;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                totalWater += (rightMax - height[right]);
            }
            right--;
        }
    }
    return totalWater;
}

int main() {
    std::cout << "[C++] Trapping Rain Water Test\n";
    std::vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    std::cout << "Trapped Water: " << trap(height) << " (Expected: 6)\n";
    return 0;
}
