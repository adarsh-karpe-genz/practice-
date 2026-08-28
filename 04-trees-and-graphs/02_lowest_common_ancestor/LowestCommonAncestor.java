/**
 * Problem: Lowest Common Ancestor of a Binary Tree
 * LeetCode: #236 (Medium)
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(H)
 */

public class LowestCommonAncestor {
    public static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;

        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        if (left != null && right != null) return root;
        return (left != null) ? left : right;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(5);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(6);
        root.left.right = new TreeNode(2);

        TreeNode p = root.left; // 5
        TreeNode q = root.left.right; // 2

        TreeNode lca = lowestCommonAncestor(root, p, q);
        System.out.println("[Java] LCA Test");
        System.out.println("LCA of " + p.val + " and " + q.val + " is " + lca.val);
    }
}
