# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED, BLUE = 0, 1

        # Build adjacency list with color
        adj = [[] for _ in range(n)]
        for u, v in redEdges:
            adj[u].append((v, RED))
        for u, v in blueEdges:
            adj[u].append((v, BLUE))

        # visited[node][color] to prevent cycles
        visited = [[False, False] for _ in range(n)]
        res = [-1] * n
        res[0] = 0

        # Queue contains: (node, color)
        q = deque()
        q.append((0, RED))
        q.append((0, BLUE))
        visited[0][RED] = visited[0][BLUE] = True

        dist = 0
        while q:
            for _ in range(len(q)):
                node, color = q.popleft()
                if res[node] == -1:
                    res[node] = dist
                for nei, nei_color in adj[node]:
                    if nei_color != color and not visited[nei][nei_color]:
                        visited[nei][nei_color] = True
                        q.append((nei, nei_color))
            dist += 1

        return res
