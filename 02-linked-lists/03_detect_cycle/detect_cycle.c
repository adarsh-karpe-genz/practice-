/**
 * Problem: Linked List Cycle Detection (Floyd's Tortoise and Hare)
 * LeetCode: #141 (Easy) & #142 (Medium)
 * 
 * Approach: Fast & Slow Pointer Algorithm
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

bool hasCycle(struct ListNode *head) {
    if (!head || !head->next) return false;

    struct ListNode *slow = head;
    struct ListNode *fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            return true; // Cycle detected
        }
    }
    return false;
}

int main(void) {
    printf("[C] Detect Cycle Test\n");
    struct ListNode n1 = {1, NULL};
    struct ListNode n2 = {2, NULL};
    struct ListNode n3 = {3, NULL};
    struct ListNode n4 = {4, NULL};

    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = &n2; // Cycle back to n2

    if (hasCycle(&n1)) {
        printf("Cycle successfully detected!\n");
    } else {
        printf("No cycle detected.\n");
    }
    return 0;
}
