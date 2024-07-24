# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        def dfs(node):
            if node is None:
                return
            if low <= node.val <= high:
                self.count += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)

        self.count = 0
        dfs(root)
        return self.count
