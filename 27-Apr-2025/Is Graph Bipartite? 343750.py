# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        NOT_COLORED = 0
        WHITE = 1
        BLACK = 2
        colors = [NOT_COLORED]*n
        res = True
        def dfs(node):
            if colors[node] == NOT_COLORED:
                colors[node] = WHITE
                for v in graph[node]:
                    if colors[v] == NOT_COLORED:
                        colors[v] = BLACK
                        bipartite = dfs(v)
                        if not bipartite:
                            return False
                    elif colors[v] == WHITE:
                        return False
                return True
            else:
                for v in graph[node]:
                    if colors[v] == NOT_COLORED:
                        if colors[node] == WHITE:
                            colors[v] = BLACK
                        else:
                            colors[v] = WHITE
                        bipartite = dfs(v)
                        if not bipartite:
                            return False
                    else:
                        if colors[v] == colors[node]:
                            return False
                return True
            
        for node in range(n):
            if colors[node] == NOT_COLORED:
                res = dfs(node)
                if not res:
                    break
        return res