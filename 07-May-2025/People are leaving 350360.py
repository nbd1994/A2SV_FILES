# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys
class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}
        self.s = size
    def find(self, x):
        root = x
        while root != -1 and root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            next_x = self.parent[x]
            self.parent[x] = root
            x = next_x
        return root
    def remove(self,x):
        if x == self.s-1:
            self.parent[x] = -1
        else:
            self.parent[x] = self.parent[x+1]

n, q = map(int, sys.stdin.readline().split())
uf = UnionFind(n)
for _ in range(q):
    query = input().split()
    x = int(query[1])-1
    if query[0] ==  '?':
        val = uf.find(x)
        print(val) if val == -1 else print(val+1)
    else:
        uf.remove(x)