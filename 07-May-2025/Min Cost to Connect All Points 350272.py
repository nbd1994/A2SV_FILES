# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

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
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = defaultdict(int)
        n = len(points)
        heap = []
        for i in range(n):
            for j in range(i+1, n):
                x1 = points[i][0]
                x2 = points[j][0]
                y1 = points[i][1]
                y2 = points[j][1]
                manhatan = abs(x1-x2) + abs(y1-y2)
                heappush(heap, (manhatan, i, j))
        uf = UnionFind(n)
        res = 0
        while heap:
            dist, x, y = heappop(heap)
            if not uf.connected(x,y):
                uf.union(x,y)
                res += dist
        return res