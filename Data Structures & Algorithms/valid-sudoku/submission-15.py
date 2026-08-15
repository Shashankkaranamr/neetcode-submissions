class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash={}
        col_hash={}
        index_hash={}
        for i in range(len(board)):
            for j in range(len(board[0])):
                num=board[i][j]
                if num!=".":
                    row_lis=[i,num]
                    col_lis=[j,num]
                    index_lis=[(i//3)*3+(j//3),num]
                    
                    if (i,num) in row_hash or (j,num) in col_hash or ((i//3)*3+(j//3),num) in index_hash:
                        return False
                    row_hash[tuple(row_lis)]=1
                    col_hash[tuple(col_lis)]=1
                    index_hash[tuple(index_lis)]=1
        return True
        

        