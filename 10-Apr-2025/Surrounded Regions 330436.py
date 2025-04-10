# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        not_surrounded = set()
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def on_boundary(a, b):
            if a == 0 or a == ROWS-1 or b == 0 or b == COLS-1:
                return True
            return False
        def in_bound(a,b):
            return 0<=a<ROWS and 0<=b<COLS
        def dfs(r,c):
            if in_bound(r,c) and board[r][c] == 'O':
                board[r][c] = 'S'
                for x,y in directions:
                    new_row = r + x
                    new_col = c + y
                    dfs(new_row, new_col)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and on_boundary(r,c):
                    dfs(r,c)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
        