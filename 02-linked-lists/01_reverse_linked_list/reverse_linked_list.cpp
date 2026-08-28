/**
 * Problem: Reverse a Singly Linked List
 * LeetCode: #206 (Easy)
 * 
 * Approach: Iterative 3-pointer method
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;

    while (curr != nullptr) {
        ListNode* nextTemp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}

void printList(ListNode* head) {
    while (head) {
        std::cout << head->val << " -> ";
        head = head->next;
    }
    std::cout << "nullptr\n";
}

int main() {
    std::cout << "[C++] Reverse Linked List Test\n";
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);

    std::cout << "Original: ";
    printList(head);

    head = reverseList(head);

    std::cout << "Reversed: ";
    printList(head);

    // Clean up
    while (head) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
    return 0;
}
