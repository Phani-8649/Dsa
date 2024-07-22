class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        a=[]
        md={}
        for i in range(len(heights)):
            md[heights[i]]=names[i]
        heights.sort(reverse=True)
        for i in range(len(heights)):
            a.append(md[heights[i]])
        return a