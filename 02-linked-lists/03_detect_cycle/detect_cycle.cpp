/**
 * Problem: Linked List Cycle Detection
 * LeetCode: #141 (Easy) & #142 (Medium)
 * 
 * Approach: Floyd's Fast & Slow Pointers
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

bool hasCycle(ListNode *head) {
    if (!head || !head->next) return false;

    ListNode *slow = head;
    ListNode *fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

int main() {
    std::cout << "[C++] Detect Cycle Test\n";
    ListNode* head = new ListNode(3);
    head->next = new ListNode(2);
    head->next->next = new ListNode(0);
    head->next->next->next = new ListNode(-4);
    head->next->next->next->next = head->next; // Cycle: -4 -> 2

    std::cout << "Has Cycle: " << (hasCycle(head) ? "true" : "false") << "\n";
    return 0;
}
