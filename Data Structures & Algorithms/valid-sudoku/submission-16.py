class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash=defaultdict(list)
        col_hash=defaultdict(list)
        index_hash=defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                num=board[i][j]
                if num!=".":
                    row=i
                    col=j
                    index=(row//3)*3+(col//3)
                    if int(num) in row_hash[row] or int(num) in col_hash[col] or int(num) in index_hash[index]:
                        return False
                    row_hash[row].append(int(num))
                    col_hash[col].append(int(num))
                    index_hash[index].append(int(num))
        return True
