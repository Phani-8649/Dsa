# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def f(roo,maxi):
            if not roo:
                return 0
            l=f(roo.left,maxi)
            r=f(roo.right,maxi)
            maxi[0]=max(maxi[0],l+r)
            return 1+max(l,r)
        maxi=[0]
        f(root,maxi)
        return maxi[0]