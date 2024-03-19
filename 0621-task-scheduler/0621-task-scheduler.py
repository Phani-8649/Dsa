class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count=Counter(tasks)
        max_heap=[-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        time=0
        q=deque()  
        # pairs of [-cnt,idletime]
        while(max_heap) or q:
            time+=1
            if(max_heap):
                cnt=1+heappop(max_heap)
                if(cnt):
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(max_heap,q.popleft()[0])
        return time