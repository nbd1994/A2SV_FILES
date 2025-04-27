# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe_nodes = [False]*n
        VISITED,VISITING,UNVISITED = 0, 1, 2
        visit_state = [UNVISITED]*n
        def dfs(node):
            if visit_state[node] == VISITED:
                return False
            if visit_state[node] == VISITING:
                return True
            visit_state[node] = VISITING
            for neig in graph[node]:
                cycle = dfs(neig)
                if cycle:
                    return True
            safe_nodes[node] = True
            visit_state[node] = VISITED
            return False
        for node in range(n):
            if visit_state[node] == UNVISITED:
                dfs(node)
        res = [i for i in range(n) if safe_nodes[i] == True]
        return res