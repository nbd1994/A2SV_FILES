# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}
        self.sett = [[i] for i in range(size)]
    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            next_x = self.parent[x]
            self.parent[x] = root
            x = next_x
        return root
    def get_equivalent(self, x):
        root_x = self.find(x)
        return self.sett[root_x][0]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            size_root_x = len(self.sett[root_x])
            for _ in range(size_root_x):
                heappush(self.sett[root_y], heappop(self.sett[root_x]))
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            size_root_y = len(self.sett[root_y])
            for _ in range(size_root_y):
                heappush(self.sett[root_x], heappop(self.sett[root_y]))
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        n = len(s1)
        def idx(char):
            return ord(char) - 97
        for i in range(n):
            uf.union(idx(s1[i]), idx(s2[i]))
        res = []
        for i in range(len(baseStr)):
            res.append(chr(uf.get_equivalent(idx(baseStr[i]))+97))
        return "".join(res)