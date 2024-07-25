class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)

        return max(depth_left, depth_right) + 1
    