# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

import sys
from heapq import *
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
heap = []
for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    a= a-1
    b=b-1
    heappush(heap,(w,a,b))

res = 0
while heap:
    w,a,b = heappop(heap)
    rep_a = uf.find(a)
    rep_b = uf.find(b)
    if rep_a != rep_b:
        res += w
        uf.union(a,b)
print(res)