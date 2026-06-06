class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {i: set() for i in range(9)}
        column_hash = {i: set() for i in range(9)}
        index_hash = {i: set() for i in range(9)}
        def hash_map(board):
            for row in range(0,9):
                for column in range(0,9):
                    if board[row][column]!='.':
                        index=(column//3)*3+(row//3)
                        if int(board[row][column]) in row_hash[row] or int(board[row][column]) in column_hash[column] or int(board[row][column]) in index_hash[index]:
                            return False
                        else:
                            row_hash[row].add(int(board[row][column]))
                            column_hash[column].add(int(board[row][column]))
                            index_hash[index].add(int(board[row][column]))

            return True
                        
        return hash_map(board)
        

        