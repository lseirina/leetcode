class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val]
        + self.inorderTraversal(root.right)

        return self.inorderTraversal(root)