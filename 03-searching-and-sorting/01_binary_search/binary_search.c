/**
 * Problem: Binary Search
 * LeetCode: #704 (Easy)
 * 
 * Approach: Iterative Divide & Conquer
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */

#include <stdio.h>

int binarySearch(const int *nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2; // avoid integer overflow

        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int main(void) {
    int nums[] = {-1, 0, 3, 5, 9, 12};
    int n = sizeof(nums) / sizeof(nums[0]);
    int target = 9;

    int idx = binarySearch(nums, n, target);
    printf("[C] Binary Search Test\n");
    printf("Target %d found at index: %d (Expected: 4)\n", target, idx);
    return 0;
}
