class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        a=0
        ans=""
        for i in s:
            l.append(int(i))
        l=sorted(l)
        l=l[::-1]
        if l[-1]==0:
            a=l.pop(0)
            l.append(a)
        for i in l:
            ans+=str(i)
        return ans