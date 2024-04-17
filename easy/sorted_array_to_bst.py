from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Did not really come up with this idea
    # I was think about dividing in 2 parts, but no specific thoughts
    # about recursion --> asked ChatGPT for an general idea then
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) is 0:
            return None
        if len(nums) is 1:
            return TreeNode(nums[0])
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


solver = Solution()
input = [-10, -3, 0, 5, 9]
root = solver.sortedArrayToBST(input)
print(root)