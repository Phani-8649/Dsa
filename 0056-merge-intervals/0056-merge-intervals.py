class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res=[intervals[0]]

        for start,end in intervals[1:]:
            lastend=res[-1][1]
            if(start<=lastend):
                res[-1][1]=max(lastend,end)
            else:
                res.append([start,end])
        return res