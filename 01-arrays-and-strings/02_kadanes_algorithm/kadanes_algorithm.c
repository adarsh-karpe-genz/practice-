/**
 * Problem: Maximum Subarray Sum (Kadane's Algorithm)
 * LeetCode: #53 (Medium)
 * 
 * Given an integer array nums, find the subarray with the largest sum, and return its sum.
 *
 * Approach: Kadane's Dynamic Programming Algorithm
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <stdio.h>
#include <limits.h>

int maxSubArray(const int *nums, int numsSize, int *outStart, int *outEnd) {
    int maxSoFar = nums[0];
    int currMax = nums[0];

    int start = 0, end = 0, tempStart = 0;

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > currMax + nums[i]) {
            currMax = nums[i];
            tempStart = i;
        } else {
            currMax += nums[i];
        }

        if (currMax > maxSoFar) {
            maxSoFar = currMax;
            start = tempStart;
            end = i;
        }
    }

    if (outStart) *outStart = start;
    if (outEnd) *outEnd = end;
    return maxSoFar;
}

int main(void) {
    int nums[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int n = sizeof(nums) / sizeof(nums[0]);
    int start = 0, end = 0;

    int maxSum = maxSubArray(nums, n, &start, &end);
    printf("[C] Kadane's Algorithm Test\n");
    printf("Max Subarray Sum: %d (Subarray from index %d to %d)\n", maxSum, start, end);
    return 0;
}
