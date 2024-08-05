# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def bbt(roo):
            if roo==None:
                return 0
            l=bbt(roo.left)
            if(l==-1):
                return -1
            r=bbt(roo.right)
            if(r==-1):
                return -1
            if(abs(l-r)>1):
                return -1
            return 1+max(l,r)
        return bbt(root)!=-1