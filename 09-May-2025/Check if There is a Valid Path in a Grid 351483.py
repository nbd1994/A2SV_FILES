# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        visited = set()
        R = len(grid)
        C = len(grid[0])
        def inbound(i,j):
            return 0 <= i < R and 0 <= j < C
        directions = {
            1: [(0, -1), (0, 1)],       # left, right
            2: [(-1, 0), (1, 0)],     # up, down
            3: [(0, -1), (1, 0)],     # left, down
            4: [(0, 1), (1, 0)],      # right, down
            5: [(0, -1), (-1, 0)],    # left, up
            6: [(0, 1), (-1, 0)],     # right, up
        }

        opposite = {
            (0, -1): (0, 1),   # left  -> right
            (0, 1): (0, -1),   # right -> left
            (-1, 0): (1, 0),   # up    -> down
            (1, 0): (-1, 0),   # down  -> up
        }
        def dfs(r,c):
            if r == R-1 and c == C-1:
                return True
            visited.add((r,c))
            for x,y in directions[grid[r][c]]:
                dx,dy = r+x, c+y
                if inbound(dx,dy) and (dx,dy) not in visited and opposite[(x,y)] in directions[grid[dx][dy]]:
                    if dfs(dx,dy):
                        return True
            return False
        return dfs(0,0)