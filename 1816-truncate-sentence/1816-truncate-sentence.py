class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        words=s.split()
        truncated_string = ' '.join(words[:k])
        return truncated_string