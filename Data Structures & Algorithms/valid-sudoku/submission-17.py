class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash=defaultdict(set)
        col_hash=defaultdict(set)
        index_hash=defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                num=board[i][j]
                if num!=".":
                    row=i
                    col=j
                    index=(row//3)*3+(col//3)
                    if num in row_hash[row] or num in col_hash[col] or num in index_hash[index]:
                        return False
                    row_hash[row].add(num)
                    col_hash[col].add(num)
                    index_hash[index].add(num)
        return True
