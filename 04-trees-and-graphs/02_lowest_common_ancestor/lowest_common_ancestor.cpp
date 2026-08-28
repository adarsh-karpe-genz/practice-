/**
 * Problem: Lowest Common Ancestor of a Binary Tree
 * LeetCode: #236 (Medium)
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(H)
 */

#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;

    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);

    if (left && right) return root;
    return left ? left : right;
}

int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(5);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(6);
    root->left->right = new TreeNode(2);

    TreeNode* p = root->left; // 5
    TreeNode* q = root->right; // 1

    TreeNode* lca = lowestCommonAncestor(root, p, q);
    std::cout << "[C++] LCA Test\n";
    std::cout << "LCA of " << p->val << " and " << q->val << " is " << lca->val << " (Expected: 3)\n";
    return 0;
}
