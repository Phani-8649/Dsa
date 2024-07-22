class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                if(heights[i]<heights[j]):
                    # print(heights[i],heights[j])
                    names[i],names[j]=names[j],names[i]
                    heights[i],heights[j]=heights[j],heights[i]
        return names