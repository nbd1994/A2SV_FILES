# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(dict)
        for i in range(len(equations)):
            x, y = equations[i]
            adj_list[x][y] = values[i]
            adj_list[y][x] = 1/values[i]
        
        def dfs(s, d, vis):
            if s == d:
                return 1
            vis.add(s)
            for neighbour in adj_list[s]:
                if neighbour not in visited:
                    temp = dfs(neighbour, d,vis)
                    if temp != -1:
                        return adj_list[s][neighbour] * temp
            return -1
            

        res = []
        for i, j in queries:
            if i not in adj_list or j not in adj_list:
                res.append(-1)
            else:
                visited = set()
                temp = dfs(i, j, visited)
                res.append(temp)
        return res
