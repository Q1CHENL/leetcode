from typing import Optional
# TIME USED: 42 MIN

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode]) -> tuple[int, bool]:
            if root is None:
                return 0, True
            rh, rb = helper(root.right)
            lh, lb = helper(root.left)
            return 1 + max(rh, lh), rb and lb and abs(rh - lh) <= 1             
        return helper(root)[1]
    
# Another solution from leetcode
# class Solution:
#     res = True
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         def height(node):
#             if node == None:
#                 return 0
#             l = height(node.left) + 1
#             r = height(node.right) + 1
#             if abs(l-r)>1:
#                 self.res = False
#             return max(l,r)
#         height(root)
#         return self.res
        
            
            