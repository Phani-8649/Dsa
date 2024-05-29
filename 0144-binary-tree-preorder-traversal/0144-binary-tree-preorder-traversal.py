# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root,res):
            if root!=None:
                res.append(root.val)
                preorder(root.left,res)
                preorder(root.right,res)
        res=[]
        preorder(root,res)
        return res
        