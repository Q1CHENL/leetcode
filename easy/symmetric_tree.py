# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        return self.check(root.left, root.right)
    
    # check the equility of left and right simultaneously in each recursion 
    def check(self, left, right):
        if left is None and right is None:
            return True
        if (left is None and right is not None) or (left is not None and right is None):
            return False
        if left.val != right.val:
            return False
        outside = self.check(left.left, right.right)
        inside = self.check(left.right, right.left)
        return outside and inside


root = TreeNode(1, TreeNode(3, TreeNode(4, None, None), TreeNode(5, TreeNode(8, None, None), TreeNode(9, None, None))), TreeNode(3, TreeNode(5, TreeNode(9, None, None), TreeNode(8, None, None)), TreeNode(4, None, None)))

solver = Solution()
print(solver.isSymmetric(root))
    