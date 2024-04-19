from typing import Optional

# TIME USED: 23 MIN

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # first idea: go through every path and store the depths in a list
    # only store the depth value when ecounter null
    # and take the max
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        depths = []
        def helper(root, depth, depths):
            if root is None:
                depths.append(depth-1)
                return
            helper(root.left, depth + 1, depths)
            helper(root.right, depth + 1,depths)
        helper(root, 1, depths)
        print(depths)
        return max(depths)
    
    # a simpler and more intuitive approach from leetcode best solution
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

solver = Solution()
# 3rd layer
node3_1 = TreeNode(15, None, None)
node3_2 = TreeNode(7, None, None)
# 2nd layer
node2_1 = TreeNode(9, None, None)
node2_2 = TreeNode(20, node3_2, node3_1)
# 1st layer
root = TreeNode(3, node2_1, node2_2)
root1 = TreeNode(1, TreeNode(2, None), None)
depth = solver.maxDepth(root)
print(depth)