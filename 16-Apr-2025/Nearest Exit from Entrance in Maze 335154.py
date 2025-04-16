# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        que = deque((entrance,))
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        R = len(maze)
        C = len(maze[0])
        visited =set()
        distance = 0
        def inbound(a,b):
            return 0 <= a < R and 0 <= b < C
        def on_edge(a,b):
            return a == 0 or a == R-1 or b == 0 or b == C-1
        while que:
            for _ in range(len(que)):
                pos = que.popleft()
                r,c = pos
                if on_edge(r,c) and maze[r][c] == '.' and [r,c] != entrance:
                    return distance
                for x,y in directions:
                    dx, dy = x+r, y+c
                    if inbound(dx,dy) and (dx,dy) not in visited and maze[dx][dy] == '.':
                        visited.add((dx,dy))
                        que.append([dx,dy])
            distance += 1
        return -1