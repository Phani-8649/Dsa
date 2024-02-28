class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mydict = {}
        ans = []
        
        # Construct frequency dictionary
        for num in nums:
            mydict[num] = mydict.get(num, 0) + 1
        
        # Sort the frequency dictionary by values in reverse order
        sorted_dict = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
        
        # Find the top k frequent elements
        for key, value in sorted_dict[:k]:
            ans.append(key)
        
        return ans
