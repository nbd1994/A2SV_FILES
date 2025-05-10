# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

import sys
class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}
        self.edge_count = {i:0 for i in range(size)}
        self.contain_g_node = {i:False for i in range(size)}
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
            self.edge_count[root_x] += 1
            return
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            self.edge_count[root_y] += (self.edge_count[root_x]+1)
            if self.contain_g_node[root_x]:
                self.contain_g_node[root_y] = True
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.edge_count[root_x] += (self.edge_count[root_y]+1)
            if self.contain_g_node[root_y]:
                self.contain_g_node[root_x] = True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

n,m,k = map(int, sys.stdin.readline().split())
g = list(map(int, sys.stdin.readline().split()))
gov_nodes = set(g)
uf = UnionFind(n)
for i in range(n):
    if i+1 in gov_nodes:
        uf.contain_g_node[i] = True
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    a-=1
    b-=1
    uf.union(a,b)
    root = uf.find(a)
    # if a+1 in gov_nodes or b+1 in gov_nodes:
    #     uf.contain_g_node[root] = True
for i in range(n):
    uf.find(i)

roots = list(set(uf.parent.values()))
existing_edges = 0
tot_nodes = 0
g_node = None
max_edges = float('-inf')
for root in roots:
    if not uf.contain_g_node[root]:
        existing_edges += uf.edge_count[root]
        tot_nodes += uf.size[root]
# tot_edges = (tot_nodes*(tot_nodes-1)//2)
res = float('-inf')
largest_gov_node = None
maxx = float('-inf')
for root in roots:
    if uf.contain_g_node[root]:
        v = uf.size[root]
        if v > maxx:
            maxx = v
            largest_gov_node = root
uf.edge_count[largest_gov_node] += existing_edges
uf.size[largest_gov_node] += tot_nodes

total_edges = 0
existing = 0 
for root in roots:
    if uf.contain_g_node[root]:
        s = uf.size[root]
        total_edges += (s*(s-1)//2)
        existing += uf.edge_count[root]
print(total_edges - existing)
