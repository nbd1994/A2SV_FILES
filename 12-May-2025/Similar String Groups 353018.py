# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

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
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        def similar(word1, word2):
            no_of_diff = 0
            c1,c2 = None, None
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    no_of_diff += 1
                    if no_of_diff == 1:
                        c1 = i
                    elif no_of_diff == 2:
                        c2 = i
                    else:
                        break
            if no_of_diff == 0:
                return True
            if no_of_diff == 2:
                if word1[c1] == word2[c2] and word1[c2] == word2[c1]:
                    return True
            return False
        for i in range(n):
            for j in range(i+1, n):
                if similar(strs[i], strs[j]):
                    uf.union(i,j)
        for k in range(n):
            uf.find(k)
        return len(set(uf.parent.values()))