# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        ROWS = len(grid)
        COLS = len(grid[0])
        def inbound(i,j):
            return 0 <= i < ROWS and 0 <= j < COLS
        visited = set()
        def dfs(r,c):
            if inbound(r,c) and grid[r][c] == 1 and (r,c) not in visited:
                visited.add((r,c))
                temp = 0
                for p, q in directions:
                    new_row = p + r
                    new_col = q + c
                    temp += dfs(new_row, new_col)
                return temp
            elif (r,c)in visited:
                return 0
            else:
                return 1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i,j)
            