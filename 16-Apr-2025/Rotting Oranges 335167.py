# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        R = len(grid)
        C = len(grid[0])
        visited = set()
        oranges_count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    que.append((r,c))
                    visited.add((r,c))
                    oranges_count += 1
                elif grid[r][c] == 1:
                    oranges_count += 1
        directions = [(1,0), (0,1), (-1,0), (0,-1)] 
        if oranges_count == 0:
            return 0
        def inbound(a,b):
            return 0 <= a < R and 0 <= b < C
        time = 0
        while que:
            if len(visited) == oranges_count:
                return time
            for _ in range(len(que)):
                r,c = que.popleft()
                for x,y in directions:
                    dx, dy = x+r, y+c
                    if inbound(dx,dy) and (dx,dy) not in visited and grid[dx][dy] == 1:
                        # grid[dx][dy] == 2
                        que.append((dx,dy))
                        visited.add((dx,dy))
            time += 1
        return -1
