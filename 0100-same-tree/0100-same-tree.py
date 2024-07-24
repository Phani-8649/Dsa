# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def f(r1,r2):
            if(r1==None and r2==None):
                return True
            if(r1==None or r2==None):
                return False
            if r1.val==r2.val:
                return f(r1.left,r2.left) and f(r1.right,r2.right)
            return False
        return f(p,q)