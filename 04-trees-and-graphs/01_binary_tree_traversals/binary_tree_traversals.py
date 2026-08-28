"""
Problem: Binary Tree Traversals (Inorder, Preorder, Postorder, Level Order)

Time Complexity: O(N)
Space Complexity: O(H) recursion, O(W) queue
"""

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root: Optional[TreeNode]) -> List[int]:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def preorder(root: Optional[TreeNode]) -> List[int]:
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def postorder(root: Optional[TreeNode]) -> List[int]:
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

def level_order(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        curr = q.popleft()
        res.append(curr.val)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return res

if __name__ == "__main__":
    print("[Python] Binary Tree Traversals Test")
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Preorder:   ", preorder(root))
    print("Inorder:    ", inorder(root))
    print("Postorder:  ", postorder(root))
    print("Level-Order:", level_order(root))
    assert inorder(root) == [4, 2, 5, 1, 3]
    print("Tree traversals test passed!")
