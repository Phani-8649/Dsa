# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        res=[]
        def f(a,r,e):
            if not r:
                return
            if(r.val==e):
                a.append(r.val)
                res.append(a[:])
                return
            a.append(r.val)
            if r.left:
                f(a,r.left,e)
            if r.right:
                f(a,r.right,e)
            a.pop()
            return
        f([],root,p.val)
        f([],root,q.val)
        a,b=res[0],res[1]
        cur=a[0]
        for i in range(1,min(len(a),len(b))):
            if(a[i]==b[i]):
                cur=a[i]
            else:
                break
        return TreeNode(cur)