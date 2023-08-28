# Given the root of a binary tree, return the inorder
# traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Traverser(object):
    def inorder_traversal(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)

    # Another solution from leetcode:
    # Use append() may actually be faster then list concat
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """

    #     traversal = []
    #     def traverse(curr):
    #         if curr == None:
    #             return
    #         if curr.left:
    #             traverse(curr.left)
    #         traversal.append(curr.val)
    #         if curr.right:
    #             traverse(curr.right)

    #     traverse(root)
    #     return traversal

#            1
#      2           3
# 4        5    6      7

tree = TreeNode(1,
                TreeNode(2,
                         TreeNode(4, None, None),
                         TreeNode(5, None, None)),
                TreeNode(3,
                         TreeNode(6, None, None),
                         TreeNode(7, None, None)))
traverser = Traverser()
res = traverser.inorder_traversal(tree)
print(res)
