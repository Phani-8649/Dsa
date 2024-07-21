class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=0
        v="aeiou"
        for i in v:
            c+=s.count(i)
        if(c==0):
            return False
        else:
            return True