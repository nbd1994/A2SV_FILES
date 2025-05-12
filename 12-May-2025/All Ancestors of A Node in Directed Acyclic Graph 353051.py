# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        ancestors = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        queue = deque([i for i in range(n) if indegree[i] == 0])
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return [sorted(list(ancestor)) for ancestor in ancestors]

