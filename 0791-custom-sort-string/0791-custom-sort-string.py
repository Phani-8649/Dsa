class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        ans=""
        for i in order:
            if(i in s):
                ans+=i*(s.count(i))
        for i in s:
            if i not in order:
                ans+=i
        return ans