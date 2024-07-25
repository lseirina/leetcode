class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        # Using root.left, root.right = root.right, root.left is the correct way to swap the values in Python
        # Python сначала оценивает правый кортеж (root.right, root.left), который содержит исходные значения root.right и root.left.
        # Затем он присваивает эти значения root.left и root.right соответственно в рамках одной атомарной операции.
        root.left, root.right = root.right = root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
