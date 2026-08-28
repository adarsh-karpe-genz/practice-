/**
 * Problem: Climbing Stairs
 * LeetCode: #70 (Easy)
 * 
 * You are climbing a staircase. It takes n steps to reach the top.
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 *
 * Approach: Space-Optimized Fibonacci DP
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <stdio.h>

int climbStairs(int n) {
    if (n <= 2) return n;
    int first = 1, second = 2;

    for (int i = 3; i <= n; i++) {
        int third = first + second;
        first = second;
        second = third;
    }
    return second;
}

int main(void) {
    int n = 5;
    printf("[C] Climbing Stairs Test\n");
    printf("Ways to climb %d stairs: %d (Expected: 8)\n", n, climbStairs(n));
    return 0;
}
