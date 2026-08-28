/**
 * Problem: Binary Tree Traversals
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(H) DFS, O(W) BFS
 */

import java.util.LinkedList;
import java.util.Queue;

public class BinaryTreeTraversals {
    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    public static void inorder(TreeNode root) {
        if (root == null) return;
        inorder(root.left);
        System.out.print(root.val + " ");
        inorder(root.right);
    }

    public static void preorder(TreeNode root) {
        if (root == null) return;
        System.out.print(root.val + " ");
        preorder(root.left);
        preorder(root.right);
    }

    public static void postorder(TreeNode root) {
        if (root == null) return;
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.val + " ");
    }

    public static void levelOrder(TreeNode root) {
        if (root == null) return;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            TreeNode curr = q.poll();
            System.out.print(curr.val + " ");
            if (curr.left != null) q.add(curr.left);
            if (curr.right != null) q.add(curr.right);
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        System.out.println("[Java] Binary Tree Traversals");
        System.out.print("Preorder:    "); preorder(root); System.out.println();
        System.out.print("Inorder:     "); inorder(root); System.out.println();
        System.out.print("Postorder:   "); postorder(root); System.out.println();
        System.out.print("Level-Order: "); levelOrder(root); System.out.println();
    }
}
