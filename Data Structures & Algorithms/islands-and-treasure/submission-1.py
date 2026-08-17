
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n=len(grid),len(grid[0])
        queue=deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    queue.append((r,c))
        visited=set((r,c) for r in range(m) for c in range(n) if grid[r][c]==0)
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        distance=0
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                grid[r][c]=distance
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and grid[nr][nc]!=-1:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            distance+=1
        
                
        