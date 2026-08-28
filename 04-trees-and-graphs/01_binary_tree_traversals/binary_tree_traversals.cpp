/**
 * Problem: Binary Tree Traversals
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(H) recursion stack, O(W) BFS queue
 */

#include <iostream>
#include <queue>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

void inorder(TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    std::cout << root->val << " ";
    inorder(root->right);
}

void preorder(TreeNode* root) {
    if (!root) return;
    std::cout << root->val << " ";
    preorder(root->left);
    preorder(root->right);
}

void postorder(TreeNode* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    std::cout << root->val << " ";
}

void levelOrder(TreeNode* root) {
    if (!root) return;
    std::queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        TreeNode* curr = q.front();
        q.pop();
        std::cout << curr->val << " ";
        if (curr->left) q.push(curr->left);
        if (curr->right) q.push(curr->right);
    }
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    std::cout << "[C++] Binary Tree Traversals\n";
    std::cout << "Preorder:   "; preorder(root); std::cout << "\n";
    std::cout << "Inorder:    "; inorder(root); std::cout << "\n";
    std::cout << "Postorder:  "; postorder(root); std::cout << "\n";
    std::cout << "Level-Order:"; levelOrder(root); std::cout << "\n";
    return 0;
}
