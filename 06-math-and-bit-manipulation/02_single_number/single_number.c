/**
 * Problem: Single Number
 * LeetCode: #136 (Easy)
 * 
 * Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
 *
 * Approach: Bitwise XOR (a ^ a = 0, a ^ 0 = a)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <stdio.h>

int singleNumber(const int *nums, int numsSize) {
    int unique = 0;
    for (int i = 0; i < numsSize; i++) {
        unique ^= nums[i];
    }
    return unique;
}

int main(void) {
    int nums[] = {4, 1, 2, 1, 2};
    int n = sizeof(nums) / sizeof(nums[0]);

    printf("[C] Single Number Test\n");
    printf("Single number: %d (Expected: 4)\n", singleNumber(nums, n));
    return 0;
}
