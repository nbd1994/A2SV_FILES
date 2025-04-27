# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        que = deque()
        R = len(grid)
        C = len(grid[0])
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    que.append((r,c,0))
                    visited.add((r,c))
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def inbound(a,b):
            return 0 <= a < R and 0 <= b < C
        while que:
            r,c,v = que.popleft()
            for x,y in directions:
                dx, dy = x+r, y+c
                if inbound(dx,dy) and (dx,dy) not in visited:
                    grid[dx][dy] = v+1
                    visited.add((dx,dy))
                    que.append((dx,dy,v+1))
        return grid