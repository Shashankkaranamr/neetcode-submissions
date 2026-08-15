class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        max_area=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area=0
                    grid[i][j]=0
                    stack=[(i,j)]
                    while stack:
                        area+=1
                        x,y=stack.pop()
                        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                                grid[nx][ny]=0
                                stack.append((nx,ny))
                    max_area=max(max_area,area)
        return max_area

                    



        