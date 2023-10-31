class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if original==None:
            return False
        if original==target:
            return cloned
        left=self.getTargetCopy(original.left,cloned.left,target)
        right=self.getTargetCopy(original.right,cloned.right,target)
        return left or right