class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={}
        for i in range(n):
            adj[i+1]=[]
        for s,d,time in times:
            adj[s].append([d,time])
        result={}
        min_heap=[[0,k]]
        while min_heap:
            t1,n1=heapq.heappop(min_heap)
            if n1 in result:
                continue
            result[n1]=t1
            for n2,t2 in adj[n1]:
                if n2 not in result:
                    heapq.heappush(min_heap,[t1+t2,n2])
        for i in range(1,n+1):
            if i not in result:
                return -1
        return max(result.values())
        
         
        