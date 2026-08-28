/**
 * Problem: Binary Tree Traversals (Inorder, Preorder, Postorder, Level Order)
 * 
 * Time Complexity: O(N) for each traversal
 * Space Complexity: O(H) recursion stack for DFS, O(W) for BFS
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

void inorder(struct TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    printf("%d ", root->val);
    inorder(root->right);
}

void preorder(struct TreeNode* root) {
    if (!root) return;
    printf("%d ", root->val);
    preorder(root->left);
    preorder(root->right);
}

void postorder(struct TreeNode* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->val);
}

void levelOrder(struct TreeNode* root) {
    if (!root) return;
    struct TreeNode* queue[100];
    int front = 0, rear = 0;

    queue[rear++] = root;
    while (front < rear) {
        struct TreeNode* curr = queue[front++];
        printf("%d ", curr->val);
        if (curr->left) queue[rear++] = curr->left;
        if (curr->right) queue[rear++] = curr->right;
    }
}

int main(void) {
    /* Construct Tree:
            1
           / \
          2   3
         / \
        4   5
    */
    struct TreeNode* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);

    printf("[C] Binary Tree Traversals\n");
    printf("Preorder:   "); preorder(root); printf("\n");
    printf("Inorder:    "); inorder(root); printf("\n");
    printf("Postorder:  "); postorder(root); printf("\n");
    printf("Level-Order:"); levelOrder(root); printf("\n");
    return 0;
}
