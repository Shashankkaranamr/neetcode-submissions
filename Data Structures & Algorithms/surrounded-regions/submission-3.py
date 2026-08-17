import copy
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        board_copy=copy.deepcopy(board)
        m,n=len(board),len(board[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        queue=deque()
        for r in range(m):
            for c in range(n):
                if (r==0 or c==0 or r==m-1 or c==n-1) and board[r][c]=="O":
                    queue.append((r,c))
        while queue:
            r,c=queue.popleft()
            board_copy[r][c]=1
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and board_copy[nr][nc]=='O':
                    queue.append((nr,nc))
    
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O' and board_copy[r][c]!=1:
                    board[r][c]="X"
