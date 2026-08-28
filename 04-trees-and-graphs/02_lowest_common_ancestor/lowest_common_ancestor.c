/**
 * Problem: Lowest Common Ancestor of a Binary Tree
 * LeetCode: #236 (Medium)
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(H) recursion stack
 */

#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* createNode(int val) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    if (!root || root == p || root == q) return root;

    struct TreeNode* left = lowestCommonAncestor(root->left, p, q);
    struct TreeNode* right = lowestCommonAncestor(root->right, p, q);

    if (left && right) return root;
    return left ? left : right;
}

int main(void) {
    struct TreeNode* root = createNode(3);
    root->left = createNode(5);
    root->right = createNode(1);
    root->left->left = createNode(6);
    root->left->right = createNode(2);
    root->right->left = createNode(0);
    root->right->right = createNode(8);

    struct TreeNode* p = root->left;        // 5
    struct TreeNode* q = root->left->right; // 2

    struct TreeNode* lca = lowestCommonAncestor(root, p, q);
    printf("[C] Lowest Common Ancestor Test\n");
    printf("LCA of %d and %d is: %d (Expected: 5)\n", p->val, q->val, lca ? lca->val : -1);
    return 0;
}
