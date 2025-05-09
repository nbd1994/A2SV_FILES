# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

from collections import Counter, defaultdict
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
tests = int(sys.stdin.readline())
for _ in range(tests):
    n, k = map(int, sys.stdin.readline().split())
    uf = UnionFind(n)
    s = input()
    t = input()
    for i in range(n):
        if i + k < n:
            uf.union(i, i+k)
        if i + k+1 < n:
            uf.union(i, i+k+1)

    groups = defaultdict(list)
    for i in range(n):
        root = uf.find(i)
        groups[root].append(i)

    for group in groups.values():
        s_count = Counter(s[i] for i in group)
        t_count = Counter(t[i] for i in group)
        if s_count != t_count:
            print("NO")
            break
    else:
        print("YES")
