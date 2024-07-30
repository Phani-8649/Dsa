class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        s=list(s)
        q=[]
        for i in range(len(s)):
            q.append(s[i])
            if(len(q)>1 and q[-2]=="b" and q[-1]=="a"):
                q.pop(-2)
                q.pop(-1)
                c+=1
        print(q)
        return c