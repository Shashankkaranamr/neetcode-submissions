class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m=len(coins)
        n=amount
        grid=[[0 for _ in range(n+1)] for _ in range(m)]

        for i in range(m-1,-1,-1):
            for j in range(n,-1,-1):
                if j==n:
                    grid[i][j]=1
                else:
                    grid[i][j]=(grid[i][j+coins[i]] if j+coins[i]<=amount else 0)+(grid[i+1][j] if i+1<len(coins) else 0)
        return grid[0][0]