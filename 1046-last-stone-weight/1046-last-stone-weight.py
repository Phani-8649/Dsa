class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq as hq
        stones=[-i for i in stones]
        hq.heapify(stones)
        while len(stones) > 1:
        # Extract the two heaviest stones
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
        
            # Smash the stones together
            if x != y:
                heapq.heappush(stones, -(y - x))
    
        # Return the weight of the last remaining stone (or 0 if none)
        return -stones[0] if stones else 0
