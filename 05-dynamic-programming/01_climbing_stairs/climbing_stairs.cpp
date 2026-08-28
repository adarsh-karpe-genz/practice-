/**
 * Problem: Climbing Stairs
 * LeetCode: #70 (Easy)
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <iostream>

int climbStairs(int n) {
    if (n <= 2) return n;
    int prev2 = 1, prev1 = 2;

    for (int i = 3; i <= n; ++i) {
        int curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}

int main() {
    int n = 6;
    std::cout << "[C++] Climbing Stairs Test\n";
    std::cout << "Ways to climb " << n << " stairs: " << climbStairs(n) << " (Expected: 13)\n";
    return 0;
}
