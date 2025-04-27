# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        que = deque()
        R = len(grid)
        C = len(grid[0])
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    que.append((r,c))
                    visited.add((r,c))
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def inbound(a,b):
            return 0 <= a < R and 0 <= b < C
        level = 1
        while que:
            for _ in range(len(que)):
                r,c = que.popleft()
                for x,y in directions:
                    dx, dy = x+r, y+c
                    if inbound(dx,dy) and (dx,dy) not in visited:
                        grid[dx][dy] = level
                        visited.add((dx,dy))
                        que.append((dx,dy))
            level += 1
        return grid 