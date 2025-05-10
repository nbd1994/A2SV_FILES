# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import defaultdict
import sys
class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}
        self.indegree = {i: 0 for i in range(size)}
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
            return
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

    def connected(self, x, y):
        return self.find(x) == self.find(y)
n, m = map(int, sys.stdin.readline().split())
uf = UnionFind(n)
res = 0
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    a = a-1
    b = b-1
    uf.indegree[a] += 1
    uf.indegree[b] += 1
    uf.union(a,b)
connected_components = defaultdict(list)
for k in uf.parent:
    uf.find(k)
for i in range(n):
    connected_components[uf.find(i)].append(i)

for root, nodes in connected_components.items():
    if all(uf.indegree[node] == 2 for node in nodes):
        res += 1
print(res)