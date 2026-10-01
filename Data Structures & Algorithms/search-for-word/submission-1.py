class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row,col,i):
            if row >=rows or row<0 or col>=cols or col<0:
                return False

            if board[row][col]!=word[i]:
                return False
            
            if i == len(word)-1:
                return True

            temp = board[row][col]
            board[row][col] = "#"

            found = (
                dfs(row-1 , col , i + 1) or
                dfs(row+1 , col , i + 1) or
                dfs(row , col-1 , i + 1) or
                dfs(row , col+1 , i + 1)
            )

            board[row][col] = temp
            return found
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True
        return False 