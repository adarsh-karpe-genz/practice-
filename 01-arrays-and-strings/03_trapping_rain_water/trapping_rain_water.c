/**
 * Problem: Trapping Rain Water
 * LeetCode: #42 (Hard)
 * 
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it can trap after raining.
 *
 * Approach: Two Pointers
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <stdio.h>

int trap(const int *height, int heightSize) {
    if (heightSize <= 2) return 0;

    int left = 0, right = heightSize - 1;
    int leftMax = 0, rightMax = 0;
    int totalWater = 0;

    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                totalWater += leftMax - height[left];
            }
            left++;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                totalWater += rightMax - height[right];
            }
            right--;
        }
    }
    return totalWater;
}

int main(void) {
    int height[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    int n = sizeof(height) / sizeof(height[0]);

    int trapped = trap(height, n);
    printf("[C] Trapping Rain Water Test\n");
    printf("Trapped Water: %d units (Expected: 6)\n", trapped);
    return 0;
}
