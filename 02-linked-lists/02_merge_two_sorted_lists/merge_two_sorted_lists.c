/**
 * Problem: Merge Two Sorted Lists
 * LeetCode: #21 (Easy)
 * 
 * Approach: Iterative Dummy Head Splicing
 * Time Complexity: O(N + M)
 * Space Complexity: O(1)
 */

#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* createNode(int val) {
    struct ListNode *newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode dummy;
    struct ListNode *tail = &dummy;
    dummy.next = NULL;

    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    if (list1 != NULL) tail->next = list1;
    else tail->next = list2;

    return dummy.next;
}

void printList(struct ListNode* head) {
    while (head) {
        printf("%d -> ", head->val);
        head = head->next;
    }
    printf("NULL\n");
}

int main(void) {
    printf("[C] Merge Two Sorted Lists Test\n");
    // List 1: 1 -> 2 -> 4
    struct ListNode *l1 = createNode(1);
    l1->next = createNode(2);
    l1->next->next = createNode(4);

    // List 2: 1 -> 3 -> 4
    struct ListNode *l2 = createNode(1);
    l2->next = createNode(3);
    l2->next->next = createNode(4);

    struct ListNode *merged = mergeTwoLists(l1, l2);
    printf("Merged List: ");
    printList(merged);
    return 0;
}
