# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}

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
            return True
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            return False
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    def get_size(self, x):
        return self.size[x]
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)
        uf = UnionFind(size)
        res = []
        for x, y in edges:
            x = x-1
            y = y-1
            is_redundant = uf.union(x,y)
            if is_redundant:
                res = [x+1, y+1]

        return res