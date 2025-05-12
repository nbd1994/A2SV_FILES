# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/607625/problem/B

import sys
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1 for i in range(size)]

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
    
n = int(sys.stdin.readline())
baboons = list(map(int, sys.stdin.readline().split()))
uf = UnionFind(n)
for i in range(n):
    uf.union(i, baboons[i]-1)

res = 0
for i in range(n):
    if uf.parent[i] == i:
        res += 1
print(res)