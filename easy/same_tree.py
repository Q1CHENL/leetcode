# Given the roots of two binary trees p and q, write a 
# function to check if they are the same or not.

# Two binary trees are considered the same if they are 
# structurally identical, and the nodes have the same value.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeChecker:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        check if both tree are the same
        """
        if q and p:
            return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        return p is None and q is None


tc = TreeChecker()

t1 = TreeNode(1, TreeNode(2, TreeNode(3, None), TreeNode(4, None)),
              TreeNode(2, TreeNode(3, None), TreeNode(4, None)))
t2 = TreeNode(1, TreeNode(2, TreeNode(3, None), TreeNode(4, None)),
              TreeNode(2, TreeNode(3, None), TreeNode(4, None)))

print(tc.is_same_tree(t1, t2))
