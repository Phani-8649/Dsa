# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(roo):
            if roo==None:
                return 0
            l=depth(roo.left)
            r=depth(roo.right)
            return 1+max(l,r)
        return depth(root)
            