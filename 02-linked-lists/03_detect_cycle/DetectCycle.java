/**
 * Problem: Linked List Cycle Detection
 * LeetCode: #141 (Easy)
 * 
 * Approach: Floyd's Tortoise and Hare
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */

public class DetectCycle {
    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public static boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) return false;

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("[Java] Detect Cycle Test");
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = head; // Cycle to head

        System.out.println("Has Cycle: " + hasCycle(head));
    }
}
