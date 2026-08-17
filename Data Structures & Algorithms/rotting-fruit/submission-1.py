class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        fresh_count=0
        queue=deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    fresh_count+=1
                if grid[r][c]==2:
                    queue.append((r,c))
        visited=set((r,c) for r in range(m) for c in range(n) if grid[r][c]==2)
        directions=[(1,0),(-1,0),(0,-1),(0,1)]
        time=0
        while queue:
            rotted_this_round=False
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and grid[nr][nc]!=0:
                        fresh_count-=1
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        rotted_this_round=True
            if rotted_this_round:
                time+=1
        return time if fresh_count==0 else -1
        
        


