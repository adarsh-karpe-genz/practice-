"""
Problem: Reverse a Singly Linked List
LeetCode: #206 (Easy)

Approach: Iterative 3-pointer method
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def to_list(head: Optional[ListNode]):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

if __name__ == "__main__":
    print("[Python] Reverse Linked List Test")
    # 1 -> 2 -> 3 -> 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print("Original:", to_list(head))
    reversed_head = reverse_list(head)
    print("Reversed:", to_list(reversed_head))
    assert to_list(reversed_head) == [4, 3, 2, 1]
    print("Test passed!")
