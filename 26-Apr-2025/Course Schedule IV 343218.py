# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = [[] for _ in range(n)]
        indegree = [0]*n
        for a,b in prerequisites:
            adj_list[a].append(b)
            indegree[b] += 1
        que = deque()
        grid = [[0]*n for _ in range(n)]
        for node in range(n):
            if indegree[node] == 0:
                que.append(node)
        # print(list(que))
        # print(indegree)
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                for neig in adj_list[node]:
                    grid[neig][node] = 1
                    indegree[neig] -= 1
                    if indegree[neig] == 0:
                        que.append(neig)
                for neig in adj_list[node]:
                    for i in range(n):
                        if grid[node][i] == 1:
                            grid[neig][i] = 1
        # order = [0]*n
        res = []
        # for idx, node in enumerate(topo_order):
        #     order[node] = idx
        for a,b in queries:
            if grid[b][a] and prerequisites:
                res.append(True)
            else:
                res.append(False)
        return res