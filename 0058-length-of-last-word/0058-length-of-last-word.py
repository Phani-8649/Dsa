class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        c=0
        for i in range(len(s)-1,-1,-1):
            if(s[i]==" "):
                break
            else:
                c+=1
        print(s)
        return c
        