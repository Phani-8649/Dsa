# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def path(roo,maxi):
            if not roo:
                return 0
            l=max(0,path(roo.left,maxi))
            r=max(0,path(roo.right,maxi))
            maxi[0]=max(maxi[0],l+r+roo.val)
            return roo.val+max(l,r)
        maxi=[float('-inf')]
        path(root,maxi)
        return maxi[0]