class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts=Counter(s)
        ans=sorted(s,key=lambda x:(-counts[x],x))
        return ans