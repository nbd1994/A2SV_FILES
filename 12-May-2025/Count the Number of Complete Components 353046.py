# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}
        self.edges = {i: 0 for i in range(size)}
    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            next_x = self.parent[x]
            self.parent[x] = root
            x = next_x
        return root

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            self.edges[root_x] += 1
            return
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            self.edges[root_y] += self.edges[root_x] + 1
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.edges[root_x] += self.edges[root_y] + 1
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a,b in edges:
            uf.union(a,b)
        for k in range(n):
            uf.find(k)
        res = 0
        parents = list(set(uf.parent.values()))
        for par in parents:
            e = uf.edges[par]
            v = uf.size[par]
            t = v*(v-1)//2
            if e == t:
                res += 1
        return res