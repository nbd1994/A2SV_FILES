# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

import sys
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
    def connected(self, x,y):
        return self.find(x) == self.find(y)
        
n,m,k = map(int, sys.stdin.readline().split())
for _ in range(m):
    input()
queries = [input() for _ in range(k)]
ans = []
uf = UnionFind(n)
for q in queries[::-1]:
    query = q.split()
    x = int(query[1])-1
    y = int(query[2])-1
    if query[0] == 'ask':
        if uf.connected(x,y):
            ans.append('YES')
        else:
            ans.append("NO")
    else:
        uf.union(x,y)
for a in ans[::-1]:
    print(a)