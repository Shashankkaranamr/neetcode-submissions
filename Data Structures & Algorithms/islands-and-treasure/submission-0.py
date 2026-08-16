from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # Step 1: seed queue with every treasure chest (0), mark visited
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        dist = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist          # write distance directly into grid
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and grid[nr][nc] != -1):   # skip walls
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            dist += 1
        # no return — grid is modified in place