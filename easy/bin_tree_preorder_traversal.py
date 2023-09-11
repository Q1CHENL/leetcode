# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Traverser:
    # my recursive solution
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorder_traversal(root.left) + self.preorder_traversal(root.right)

    # a tail-recursive approach from leetcode
    def preorderTraversal_tr(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node):
            if not node:
                return None
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return res

    # a iterative approach from leetcode
    def preorderTraversal_itr(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)  # save right node for future visit
                curr = curr.left
            else:
                curr = stack.pop()
        return res
