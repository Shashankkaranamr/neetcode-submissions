class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        heap=[(grid[0][0],0,0)]
        visited={(0,0)}
        while heap:
            rain_level,r,c=heapq.heappop(heap)
            if r==n-1 and c==n-1:
                return rain_level
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heapq.heappush(heap,(max(grid[nr][nc],rain_level),nr,nc))  
        return -1      

