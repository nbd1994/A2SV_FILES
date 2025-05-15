# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}
        self.no_of_components = size
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
            return 0
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        self.no_of_components -= 1
        return 1
    def connected(self):
        return self.no_of_components <= 1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa, ufb = UnionFind(n), UnionFind(n)
        needed_edges = 0
        for t, a, b in edges:
            if t == 3:
                needed_edges += (ufa.union(a-1, b-1) | ufb.union(a-1, b-1))
        for t, a, b in edges:
            if t == 1:
                needed_edges += ufa.union(a-1, b-1)
            elif t == 2:
                needed_edges += ufb.union(a-1, b-1)
        if ufa.connected() and ufb.connected():
            total_edges = len(edges)
            return total_edges - needed_edges
        return -1