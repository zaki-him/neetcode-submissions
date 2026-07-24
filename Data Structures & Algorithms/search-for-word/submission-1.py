class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def backtracking(row, col, index):
            if index == len(word):
                return True
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or word[index] != board[row][col] or (row, col) in path:
                return False
            
            path.add((row, col))
            res = backtracking(row + 1, col, index + 1) or backtracking(row, col + 1, index + 1) or backtracking(row - 1, col, index + 1) or backtracking(row, col - 1, index + 1)
            path.remove((row, col))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtracking(r, c, 0):
                    return True
        
        return False

