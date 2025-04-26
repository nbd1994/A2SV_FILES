# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        indegree = [0]*n
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        que = deque()
        # print(indegree)
        for node in range(n):
            if indegree[node] == 1:
                que.append(node)
        res = [0]
        while que:
            # print(que)
            # print(indegree)
            res = list(que)
            for _ in range(len(que)):
                node = que.popleft()
                indegree[node] -= 1
                for neig in adj_list[node]:
                    indegree[neig] -= 1
                    if indegree[neig] == 1:
                        que.append(neig)
        return res