class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        col_set=set()
        pos_set=set()
        neg_set=set()
        board=[["."]*n for _ in range(n)]
        def backtrack(i):
            if i==n:
                pos=["".join(row) for row in board]
                res.append(pos)
                return 
            for j in range(n):
                if j in col_set or j+i in pos_set or j-i in neg_set:
                    continue
                col_set.add(j)
                pos_set.add(j+i)
                neg_set.add(j-i)
                board[j][i]="Q"
                backtrack(i+1)

                col_set.remove(j)
                pos_set.remove(j+i)
                neg_set.remove(j-i)
                board[j][i]="."
        backtrack(0)
        return res
        