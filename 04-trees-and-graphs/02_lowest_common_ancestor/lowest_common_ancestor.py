"""
Problem: Lowest Common Ancestor of a Binary Tree
LeetCode: #236 (Medium)

Time Complexity: O(N)
Space Complexity: O(H)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left or right

if __name__ == "__main__":
    print("[Python] LCA Test")
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)

    p = root.left
    q = root.right
    lca = lowest_common_ancestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is {lca.val}")
    assert lca.val == 3
    print("LCA test passed!")
