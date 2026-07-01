import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_arr=[((x**2+y**2),[x,y]) for x,y in points]
        heapq.heapify(heap_arr)

        return [heapq.heappop(heap_arr)[1] for _ in range(k)]


        