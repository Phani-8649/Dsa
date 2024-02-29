class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts=Counter(s)
        print(counts)
        ans=sorted(s,key=lambda x:(-counts[x]))
        return ans