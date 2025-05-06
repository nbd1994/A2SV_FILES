# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}
        self.exp = {i: 0 for i in range(size)}
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
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def idx(char):
            return ord(char) - 97
        ufe = UnionFind(26)
        for eqn in equations:
            a,b,operator = eqn[:1],eqn[-1:], eqn[1:3]
            if operator == '==':
                ufe.union(idx(a), idx(b))
        for eqn in equations:
            a,b,operator = eqn[:1],eqn[-1:], eqn[1:3]
            if operator == '!=' and ufe.find(idx(a)) == ufe.find(idx(b)):
                return False
        return True