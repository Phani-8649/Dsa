class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        # s = ' '.join(s[::-1])
        s=' '.join(reversed(s))
        return s