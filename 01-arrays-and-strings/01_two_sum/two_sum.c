/**
 * Problem: Two Sum
 * LeetCode: #1 (Easy)
 * 
 * Given an array of integers 'nums' and an integer 'target', return indices
 * of the two numbers such that they add up to target.
 *
 * Approach: Struct-based Indexed Sorting + Two Pointers (O(N log N))
 * Time Complexity: O(N log N)
 * Space Complexity: O(N)
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int value;
    int index;
} Element;

int compareElements(const void *a, const void *b) {
    return ((Element *)a)->value - ((Element *)b)->value;
}

bool twoSum(const int *nums, int numsSize, int target, int *out1, int *out2) {
    Element *arr = (Element *)malloc(numsSize * sizeof(Element));
    if (!arr) return false;

    for (int i = 0; i < numsSize; i++) {
        arr[i].value = nums[i];
        arr[i].index = i;
    }

    qsort(arr, numsSize, sizeof(Element), compareElements);

    int left = 0, right = numsSize - 1;
    bool found = false;

    while (left < right) {
        int sum = arr[left].value + arr[right].value;
        if (sum == target) {
            *out1 = arr[left].index;
            *out2 = arr[right].index;
            found = true;
            break;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    free(arr);
    return found;
}

int main(void) {
    int nums[] = {2, 7, 11, 15};
    int n = sizeof(nums) / sizeof(nums[0]);
    int target = 9;
    int i1 = -1, i2 = -1;

    printf("[C] Two Sum Test\n");
    if (twoSum(nums, n, target, &i1, &i2)) {
        printf("Found indices: [%d, %d] -> %d + %d = %d\n", i1, i2, nums[i1], nums[i2], target);
    } else {
        printf("Not found\n");
    }
    return 0;
}
