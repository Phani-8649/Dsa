class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        for i in s:
            if(s.rindex(i)==s.index(i)):
                return s.index(i)
        return -1