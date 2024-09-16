class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        a=[]
        md=float('inf')
        for i in timePoints:
            a.append((int(i[:2])*60)+int(i[3:]))
        a=[1440 if x==0 else x for x in a]
        a.sort()
        print(a)
        for i in range(1,len(a)):
            d=a[i]-a[i-1]
            if(d<md):
                md=d
        cd=1440-(a[-1]-a[0])
        md=min(md,cd)
        return md

