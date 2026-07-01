import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_arr=[]
        answer_arr=[0]*k
        count=0
        for arr in points:
            heapq.heappush(heap_arr,(math.sqrt(arr[0]**2+arr[1]**2),arr))
        while count<k:
            dist,answer_arr[count]=heapq.heappop(heap_arr)
            count+=1
        return answer_arr


        