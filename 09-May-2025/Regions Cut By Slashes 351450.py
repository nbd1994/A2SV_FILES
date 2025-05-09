# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

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
            return 0
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return 1
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        def get_triangle(r,c,t):
            return (n*r+c)*4+t
        tot_triangles = n*n*4
        uf = UnionFind(tot_triangles)
        tot_regions = tot_triangles
        for r in range(n):
            for c in range(n):
                if r > 0:
                    top_triangle = get_triangle(r-1,c,2)
                    bot_triangle = get_triangle(r,c,0)
                    tot_regions -= uf.union(top_triangle, bot_triangle)
                if c > 0:
                    left_triangle = get_triangle(r,c-1,1)
                    right_triangle = get_triangle(r,c,3)
                    tot_regions -= uf.union(left_triangle, right_triangle)
                if grid[r][c] != '\\':
                    triangle_1 = get_triangle(r,c,0)
                    triangle_2 = get_triangle(r,c,3)
                    triangle_3 = get_triangle(r,c,1)
                    triangle_4 = get_triangle(r,c,2)
                    tot_regions -= uf.union(triangle_1, triangle_2)
                    tot_regions -= uf.union(triangle_3, triangle_4)
                if grid[r][c] != '/':
                    triangle_1 = get_triangle(r,c,0)
                    triangle_2 = get_triangle(r,c,1)
                    triangle_3 = get_triangle(r,c,2)
                    triangle_4 = get_triangle(r,c,3)
                    tot_regions -= uf.union(triangle_1, triangle_2)
                    tot_regions -= uf.union(triangle_3, triangle_4)
        return tot_regions